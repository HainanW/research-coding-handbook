"""Replace local PDF file links with repository URLs before publication.

Requires PyMuPDF. Does not modify PDF input files; choose an output directory.
Example from the handbook root after exporting:
python tools/sanitize_pdf_links.py docs/print/example.pdf --output-dir public-pdf \
    --repository-base-url https://github.com/OWNER/REPO/blob/main
"""

import argparse
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import pymupdf


ROOT = Path(__file__).resolve().parents[1]


def sanitize(source, destination, source_root, repository_base_url):
    """Only map file links within the explicitly selected repository root."""
    if source.resolve() == destination.resolve():
        raise ValueError("Use a different output directory; input PDFs are preserved.")
    changed = 0
    with pymupdf.open(source) as document:
        for page in document:
            for link in page.get_links():
                raw = link.get("file")
                uri = link.get("uri", "")
                fragment = ""
                if uri.lower().startswith("file:"):
                    parts = urlsplit(uri)
                    if parts.netloc:
                        raise ValueError("Network file link requires separate review.")
                    raw, fragment = unquote(parts.path), parts.fragment
                if not raw:
                    continue
                normalized = unquote(raw).replace("\\", "/")
                if len(normalized) > 3 and normalized[0] == "/" and normalized[2] == ":":
                    normalized = normalized[1:]
                local_path = Path(normalized)
                if not local_path.is_absolute():
                    local_path = source.parent / local_path
                relative = local_path.resolve().relative_to(source_root.resolve())
                if not (source_root / relative).is_file():
                    raise ValueError(f"Link target is missing: {relative}")
                url = repository_base_url.rstrip("/") + "/" + quote(relative.as_posix(), safe="/")
                if fragment:
                    url += "#" + quote(fragment, safe="-")
                page.update_link({"kind": pymupdf.LINK_URI, "xref": link["xref"],
                                  "from": link["from"], "uri": url})
                changed += 1
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Full rewrite discards old annotation objects containing local paths.
        document.save(destination, garbage=4, deflate=True)
    with pymupdf.open(destination) as checked:
        for page in checked:
            if any(link.get("file") or link.get("uri", "").lower().startswith("file:")
                   for link in page.get_links()):
                raise ValueError("Output still contains a local file link.")
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("documents", nargs="+", type=Path)
    parser.add_argument("--source-root", type=Path, default=ROOT)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--repository-base-url", required=True)
    args = parser.parse_args()
    base = urlsplit(args.repository_base_url)
    if base.scheme != "https" or not base.netloc or base.username or base.password or base.query or base.fragment:
        parser.error("Use an HTTPS repository URL without credentials, query, or fragment.")
    for source in args.documents:
        destination = args.output_dir / source.name
        count = sanitize(source.resolve(), destination.resolve(), args.source_root.resolve(),
                         args.repository_base_url)
        print(f"{destination.name}: replaced {count} local file links")


if __name__ == "__main__":
    main()
