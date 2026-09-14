"""Export the Q1-Q3 Markdown guides to US Letter HTML and PDF.

Requires Python-Markdown and an installed Chrome or Edge browser.
Run from the repository root: python tools/export_print.py
"""

import argparse
import base64
import html
import mimetypes
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import quote

import markdown


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOCS = (
    "docs/01-spyder-function-inspection.md",
    "docs/02-markdown-images.md",
    "docs/03-python-data-types.md",
)


def find_browser(requested):
    if requested:
        browser = Path(requested)
        if not browser.is_file():
            raise FileNotFoundError(browser)
        return browser
    candidates = [
        Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Google/Chrome/Application/chrome.exe",
    ]
    for browser in candidates:
        if browser.is_file():
            return browser
    raise RuntimeError("Chrome/Edge not found. Supply --browser with its executable path.")


def split_listing(match):
    """Keep a long Python listing's top-level functions together on paper."""
    attributes, encoded_code = match.groups()
    code = html.unescape(encoded_code)
    if len(code.splitlines()) < 30 or "language-python" not in attributes:
        return match.group(0)
    chunks = re.split(r"\n\n\n(?=(?:def |if __name__))", code)
    # Keep the import preamble with the first function.
    if len(chunks) > 1 and not chunks[0].lstrip().startswith(("def ", "if __name__")):
        chunks = [chunks[0] + "\n\n\n" + chunks[1]] + chunks[2:]
    return "\n".join(
        '<pre><code class="language-python">' + html.escape(chunk.rstrip()) + "\n</code></pre>"
        for chunk in chunks
    )


def render_html(source, destination, css):
    text = source.read_text(encoding="utf-8")
    # Navigation and PDF-download links are useful on screen, not in the printout.
    text = re.sub(r"<!-- print:omit -->.*?<!-- /print:omit -->", "", text, flags=re.S)
    text = re.sub(r"^\[(?:Back to the handbook|返回手册)\].*$", "", text, flags=re.M)
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    body = re.sub(r"<pre><code([^>]*)>(.*?)</code></pre>", split_listing, body, flags=re.S)
    references = []

    def link(match):
        target, label = html.unescape(match.group(1)), match.group(2)
        if target.startswith(("https://", "http://")):
            if target not in references:
                references.append(target)
            number = references.index(target) + 1
            return (f'<a href="{html.escape(target, quote=True)}">{label}</a>'
                    f'<sup class="reference">[{number}]</sup>')
        relative = os.path.relpath((source.parent / target).resolve(), destination.parent).replace("\\", "/")
        return f'<a href="{quote(relative, safe="/#")}">{label}</a>'

    body = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', link, body, flags=re.S)

    def embed(match):
        path = (source.parent / html.unescape(match.group(1))).resolve()
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        payload = base64.b64encode(path.read_bytes()).decode("ascii")
        return f'src="data:{mime};base64,{payload}"'

    body = re.sub(r'src="([^"]+)"', embed, body)
    body = re.sub(
        r"<p>(<img [^>]+>)</p>\s*<p><em>(.*?)</em></p>",
        r"<figure>\1<figcaption>\2</figcaption></figure>", body, flags=re.S,
    )
    chinese = ".zh-CN" in source.stem
    if references:
        heading = "参考资料（References）" if chinese else "References"
        body += f'<h2>{heading}</h2><ol class="references">'
        for target in references:
            escaped = html.escape(target, quote=True)
            body += f'<li><a href="{escaped}">{escaped}</a></li>'
        body += "</ol>"
    title_match = re.search(r"^# (.+)$", text, flags=re.M)
    title = html.escape(title_match.group(1) if title_match else source.stem)
    language = "zh-CN" if chinese else "en"
    document = (f'<!doctype html>\n<html lang="{language}"><head><meta charset="utf-8">'
                f'<title>{title}</title><style>{css}</style></head><body>{body}</body></html>')
    destination.write_text(document, encoding="utf-8")


def print_pdf(browser, source, destination):
    previous_mtime = destination.stat().st_mtime_ns if destination.exists() else None
    # An isolated temporary profile avoids touching an existing browser session.
    profile_root = Path(tempfile.gettempdir()).resolve()
    profile = Path(tempfile.mkdtemp(prefix="handbook-print-", dir=profile_root)).resolve()
    if profile.parent != profile_root or not profile.name.startswith("handbook-print-"):
        raise RuntimeError("Unexpected temporary profile path")
    try:
        command = [
            str(browser), "--headless", "--disable-gpu", "--no-first-run",
            "--no-default-browser-check", "--disable-extensions", "--disable-background-networking",
            f"--user-data-dir={profile}", "--no-pdf-header-footer",
            "--virtual-time-budget=2500", f"--print-to-pdf={destination}", source.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=90,
                                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        if result.returncode != 0 or not destination.is_file():
            raise RuntimeError("PDF export failed: " + result.stderr[-2000:])
        if previous_mtime is not None and destination.stat().st_mtime_ns == previous_mtime:
            raise RuntimeError(
                f"PDF was not updated: {destination}. Close any application using this file and retry."
            )
        if destination.read_bytes()[:5] != b"%PDF-":
            raise RuntimeError(f"Invalid PDF output: {destination}")
    finally:
        # Delete only the verified temporary directory created by this call.
        if profile.parent == profile_root and profile.name.startswith("handbook-print-"):
            shutil.rmtree(profile, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("documents", nargs="*", help="Markdown files, relative to the repository root")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "docs/print")
    parser.add_argument("--browser", help="Full path to Chrome or Edge")
    args = parser.parse_args()
    browser = find_browser(args.browser)
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    css = (ROOT / "tools/print.css").read_text(encoding="utf-8")
    for document in args.documents or DEFAULT_DOCS:
        source = (ROOT / document).resolve()
        html_path = output / (source.stem + ".html")
        pdf_path = output / (source.stem + ".pdf")
        render_html(source, html_path, css)
        print_pdf(browser, html_path, pdf_path)
        print(pdf_path, flush=True)


if __name__ == "__main__":
    main()
