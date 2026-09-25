---
name: research-coding-handbook
description: "Create research-code tutorials, numbered worked examples, and technical reports using Research Coding Handbook conventions: equation-to-code explanations, reproducibility evidence, English/Chinese editions, and printable outputs. Use for handbook-style documentation, not isolated syntax questions or unrelated translation."
---

# Research Coding Handbook

Turn an identified research problem or runnable example into an inspectable learning report. The audience may know MATLAB well but be new to Python. Explain key terms in Chinese with the English term in parentheses; do not require understanding advanced Python before explaining the model.

## Select the scope and destination

- Follow the user's topic, filename, language, output format, and destination. If the subject is missing, ask one focused question before drafting a long report. An explanation request alone does not authorize creating files.
- Read applicable repository instructions and the selected code/documents. Inspect current changes before editing; preserve unrelated material. Distinguish updating a handbook chapter from writing a report in another project.
- Locate the `research-coding-handbook` repository from the user's supplied path or the current workspace. When working there, read its current `AGENTS.md`, `README.md`, and `README.zh-CN.md`; do not treat this skill's snapshot as newer than those files. If the repository is unavailable, use the conventions below without inventing access or scanning unrelated directories.
- Only use sources in the requested scope. Do not enumerate or ingest technical-library collections, protected company documents, credentials, or business datasets just because they are adjacent to the handbook. A tutorial can use clearly labeled synthetic or textbook inputs.

## Write the report

Adapt the structure to the question rather than imposing a fixed chapter count. For a model/code report, useful components are: problem and assumptions; inputs and units; mathematical formulation; symbol-to-code mapping; execution/inspection; independently checked results; interpretation, limits, and references.

- Establish whether each quantity is given data, an optimization variable, a symbolic expression, or a computed result. Keep notation consistent across prose, formulas, tables, and code.
- Explain the mathematical purpose before the Python syntax. Use short snippets from the actual implementation and stable section/cell labels instead of relying only on changing line numbers. For Spyder examples, prefer inspectable scalars/tables and `# %%` cells when consistent with the existing code.
- Distinguish continuous LP, integer/MILP, and repeated rolling-horizon execution when relevant. An integral-looking solution is not evidence of integer constraints. Do not transfer a teaching model's performance or assumptions to a real factory.
- Separate source claims, local adaptations, actual execution evidence, and proposed extensions. Verify library-specific claims with installed code or primary documentation. Include source links and retain applicable licenses when adapting code.
- Keep headings compact, table columns reasonably narrow, and code lines short for print. Use a figure only when it clarifies a nontrivial relationship. A missing screenshot should have a visible explanatory placeholder, not a broken image or an invented GUI capture.

## Handbook organization and bilingual editions

These are defaults for the original handbook, not a command to restructure other repositories:

- Main guides: `docs/NN-main-topic.md`; a supplementary example can be `docs/NN-example-01-topic.md`. Inspect existing numbering first. A user-specified name takes precedence. A chapter-03 example is linked under chapter 03, not silently substituted for the existing main chapter.
- Maintain the English source and the corresponding `.zh-CN.md` full bilingual source. In the bilingual edition, each English paragraph is followed immediately by its Chinese counterpart; lists are paired item by item; table cells place English above Chinese using `<br>` where useful. Identical code, formulas, and figures appear once. The exporter does not translate or combine editions.
- Keep runnable teaching code in `examples/`, figures in `docs/images/`, and derived HTML/PDF in `docs/print/`, with matching filename stems. Use relative links and per-document Figure 1 / 图 1 numbering.
- Update both README indexes and, where helpful, the parent chapter's example links. If the new document should be part of the full export, update the existing exporter's default document list. Do not regenerate unrelated chapters unless shared changes actually require it.

## Reproducibility and validation

- Run the relevant example if permitted and practical; otherwise explicitly label values as expected/unverified. A successful import or compilation does not establish numerical correctness.
- Inspect execution side effects first. Permission to document a script does not imply permission to run it against production services, overwrite business data, or trigger external messages. Use a safe small case or explain why execution was not performed.
- Record the actual interpreter/dependency versions, input configuration, command, numerical status and tolerance, and checks appropriate to the claim. Use a source hash or Git revision plus dirty-state notes to identify the code used. Avoid exposing personal paths or unrelated file inventories in portable records.
- For optimization reports, check solver termination before using a solution; verify bounds, constraints, units, and objective independently. Feasibility checks alone do not prove optimality. Small analytical bounds or separate reference calculations are valuable when available.
- Preserve material test evidence, including expected infeasibility or failed experiments, without overwriting business inputs. Keep bulky/debug artifacts separate from the reader's report. Do not claim a Spyder GUI run when only terminal execution or shared-namespace cell simulation was performed.
- If changing a plain Python input requires rebuilding the model, say so explicitly. Document which results the user should see after a clean rerun.

## Print and handoff

- In the original handbook, reuse `tools/export_print.py` and `tools/print.css`; default to US Letter and black-and-white-friendly styling. Select only the changed sources for export, for example `python tools/export_print.py docs/NN-example-01-topic.md docs/NN-example-01-topic.zh-CN.md`.
- Check existing environments for Python-Markdown and Chrome/Edge before proposing installation. Missing dependencies are not proof that the report cannot be made; report the gap and stay within authorized environment changes.
- Inspect the renderer before assuming LaTeX will render. For simple algebra, offline Unicode plus HTML subscripts/superscripts can suffice. For complex mathematics, use an available local math renderer or prepared vector equations; do not silently leave raw TeX or depend on a remote CDN for an offline report.
- Check local links, both language editions, PDF page size, Chinese glyphs, equation symbols, pagination, and overflow. Visually inspect representative or all pages as appropriate. Explain any missing checks or locked output files.
- Handoff with links to the main reading/printing files and the example, a short verification summary, and unresolved limitations. State whether commit/push occurred; generating a report does not authorize either. Installing this skill does not authorize installing packages, accessing new data sources, or publishing reports.
