# Research Coding Handbook

[中文目录与英中双语教程](README.zh-CN.md)

[00 — Table of Content](docs/00-Table-of-Content.md) · [Bilingual landscape PDF](docs/print/00-Table-of-Content.zh-CN.pdf) · [English–Chinese contents](docs/00-Table-of-Content.zh-CN.md).

The printed contents uses a narrower chapter/topic column (32%) and indents worked examples beneath their parent chapter. Each page leaves a clear 30 mm top margin for hole punching.

The contents list all ten guides, the chapter 01 Spyder supplement, the chapter 03 worked example, and Koopman reading materials. Chapter titles link to their sources. The default print export includes this table of contents.

A practical handbook for turning research questions and mathematical models into reliable code, reproducible experiments, and publication results.

This repository collects recurring programming practices, workflows, and templates for research, with a focus on Python / MATLAB, numerical computing, optimization, and machine learning. Its goal is to make research traceable, code maintainable, and results reproducible.

> Status: Ten guides cover VS Code running/debugging (with a Spyder supplement), Markdown images, Python data types, GitHub synchronization, dunder names, GitHub organizations, conda environments, Python classes, Codex skills, and Python imports/type annotations/parsing. Runnable examples and a generated figure are included.

## Workspace Context

| Field | Recorded value |
| --- | --- |
| Device | `Legion T7 34IRZ8` |
| Conversation title | `Locate research-coding-handbook` |

## Questions and Worked Examples

**01. Run and debug Python scripts in VS Code**

- [Main guide](docs/01-main-running-and-debugging.md): interpreter selection, running a script, breakpoints, stepping, and preparing inputs.
- [Bilingual PDF](docs/print/01-main-running-and-debugging.zh-CN.pdf) · [Practice script](examples/10_python_annotations_and_parsing.py).
- Sections 2 and 3 explain parameters versus arguments, whether input is required, fixed test inputs, `launch.json` arguments, and interactive `input()` debugging.
- **01-SI: Spyder supplementary information**
  - [Guide](docs/01-SI-spyder.md) · [Bilingual PDF](docs/print/01-SI-spyder.zh-CN.pdf).
  - [Original example](examples/01_spyder_function_inspection.py): the full exercise on random data, local variables, array types and shapes.

**Q2. Inserting images into Markdown**

> How should I insert screenshots or figures into a `.md` file and organize their image files?

- [Read the image guide](docs/02-main-markdown-images.md): relative paths, VS Code insertion and preview, display width, and shared images for both languages.
- [Regenerate the example figure](examples/02_plot_generated_data.py): save a comparison of the two random datasets to `docs/images/01-generated-data.png`.
- [US Letter PDF](docs/print/02-main-markdown-images.pdf) · [Print HTML](docs/print/02-main-markdown-images.html).

**Q3. Python data types through a Case 1 profit equation**

> How do types such as `float` and `tuple` differ, and how do type, size, and mutability connect to variables in a real Case 1 equation?

- [Read the guide](docs/03-main-python-data-types.md): core built-in types, NumPy arrays, aliases and copies, and the profit function explained line by line.
- [Run the example](examples/03_python_data_types.py): inspectable type examples, four profit scenarios, and independent loop verification.
- [US Letter PDF](docs/print/03-main-python-data-types.pdf) · [Print HTML](docs/print/03-main-python-data-types.html).

- **Example 1: MO-book production planning — from equations to Python objects**
  - [Technical learning report](docs/03-example-01-mo-book-production.md) · [English–Chinese edition](docs/03-example-01-mo-book-production.zh-CN.md).
  - [US Letter PDF](docs/print/03-example-01-mo-book-production.pdf) · [Print HTML](docs/print/03-example-01-mo-book-production.html).
  - [Runnable example](examples/03_example_01_mo_book_production.py) · [Verification script](examples/verify_03_example_01.py) · [Run record](examples/results/03-example-01-mo-book-production-verification.json).
  - Textbook LP, not a factory MILP or a rolling-horizon implementation; includes symbolic variables, dictionaries, Series/DataFrame, and independently checked results.

**05. Python dunder methods and special names**

- [Read the guide](docs/05-main-python-dunder.md): special methods, a profit container, and the `__name__` entry-point guard.
- [Run the example](examples/05_dunder_methods.py) · [PDF](docs/print/05-main-python-dunder.pdf) · [Print HTML](docs/print/05-main-python-dunder.html).

**06. Create a GitHub organization**

- [Read the guide](docs/06-main-github-organization.md) · [PDF](docs/print/06-main-github-organization.pdf) · [HTML](docs/print/06-main-github-organization.html).
- Organization setup, repository ownership, and three screenshot placeholders.

**07. Install and use a conda environment**

- [Read the Windows guide](docs/07-main-conda-environment.md) · [PDF](docs/print/07-main-conda-environment.pdf) · [HTML](docs/print/07-main-conda-environment.html).
- Installation checks, environment creation, VS Code interpreter selection, and three screenshot placeholders.

**08. Understand Python classes and objects**

- [Read the guide](docs/08-main-python-classes.md): classes, instances, `self`, initialization, attributes, methods, and independent experiment records.
- [Run the example](examples/08_python_classes.py) · [PDF](docs/print/08-main-python-classes.pdf) · [Print HTML](docs/print/08-main-python-classes.html).

**09. Codex skills: installation and scientific plotting**

- [Read the guide](docs/09-main-codex-skills.md): skill structure, personal and project installation, `.agents/skills` versus `.codex/skills`, invocation, maintenance, and scientific plotting with `scientific-visualization`.
- Includes copyable prompts, a Matplotlib example, and the original tutorial request. The installation commands are documented examples; adding this chapter does not install a skill or change Python environments.
- [US Letter PDF](docs/print/09-main-codex-skills.pdf) · [Print HTML](docs/print/09-main-codex-skills.html).

**10. Python imports, type annotations, and parsing**

- [Read the guide](docs/10-main-python-imports-annotations-parsing.md): the WO Table 4 imports, type hints, `from __future__ import annotations` in Python 3.9, dunder names, and command-line parsing.
- [Run the small example](examples/10_python_annotations_and_parsing.py): standard library only; prints values without creating files or running optimization.
- Section 5 explains `__annotations__`, object and module `__name__`, dunder naming, and the entry-point guard with direct-run/import examples. Section 6 includes the complete runnable source in both language editions and their print versions.
- [US Letter PDF](docs/print/10-main-python-imports-annotations-parsing.pdf) · [Print HTML](docs/print/10-main-python-imports-annotations-parsing.html).
- [English–Chinese PDF](docs/print/10-main-python-imports-annotations-parsing.zh-CN.pdf) · [Bilingual print HTML](docs/print/10-main-python-imports-annotations-parsing.zh-CN.html).

Reusable handbook-writing skill: [research-coding-handbook](skills/research-coding-handbook/SKILL.md). Its source captures reporting conventions, not the handbook's entire document collection. Once installed as a personal skill, invoke `$research-coding-handbook` with the target code, destination, and requested formats; this does not authorize uploads or Git pushes.

## GitHub Sync and Koopman Learning Materials

- [04. Manual GitHub sync guide (sanitized, English)](docs/04-main-github-manual-push.md) · [PDF](docs/print/04-main-github-manual-push.pdf). Includes step-by-step instructions and a compact screenshot, with a link to the full image, for opening PowerShell in VS Code and confirming the project directory. Also explains `git pull --ff-only`, with fast-forward and diverged-history examples and the meaning of `origin main`.
- [Koopman operator: Day 1](Koopman_Operator_Day_1_Learning_Materials.docx).
- [Koopman operator: Days 2–7](Koopman_Operator_Day_2_to_Day_7_Learning_Materials.docx).
- [Koopman operator: Days 8–14](Koopman_Operator_Week_2_Day_8_to_Day_14_Learning_Materials.docx).
- [Koopman operator: Days 15–21](Koopman_Operator_Week_3_Day_15_to_Day_21_Learning_Materials.docx).
- [Koopman operator: Days 22–30 and final project](Koopman_Operator_Week_4_Day_22_to_Day_30_Final_Project_Learning_Materials.docx).

The original internal push guides are kept locally and excluded from Git. Only their sanitized edition is published.

## Print Editions

The default print output is now **English–Chinese PDF only**, on US Letter paper (8.5 × 11 inches), with black-and-white-friendly styling. English and bilingual Markdown sources are still maintained together. Previously published English PDFs and HTML files remain available, but are not automatically regenerated.

Run `python tools/export_print.py` to export the bilingual contents, guides 01–10, the 01-SI Spyder supplement, and chapter 03's Example 1. For one document, run `python tools/export_print.py docs/00-Table-of-Content.zh-CN.md`. The exporter reads the existing bilingual source; it does not translate. HTML is created temporarily for rendering and removed afterward.

Use an existing Python environment with Python-Markdown and Chrome or Edge. The stylesheet is `tools/print.css`; PDFs go to `docs/print/`. `--bilingual` remains supported. Only when an additional format is explicitly wanted, use `--english` for an English PDF or `--html` to retain print HTML.

Before publishing PDFs, inspect embedded links for local paths. The [PDF link sanitizer](tools/sanitize_pdf_links.py) uses PyMuPDF to replace in-repository file links with URLs under an explicitly supplied HTTPS repository base. Run `python tools/sanitize_pdf_links.py --help` for arguments; it writes a separate PDF and preserves the input.

## Core Principles

- **Define the problem before implementing the algorithm.** State the research objective, assumptions, variables, units, constraints, and evaluation metrics.
- **Start with the smallest verifiable case.** Check the implementation against an analytical solution, a small example, or a trusted benchmark before expanding to the full problem.
- **Keep experiments traceable.** Connect results to the code version, configuration, data sources, environment, and run commands.
- **Separate evidence from interpretation.** Distinguish what a paper states, what the code implements, what experiments show, and what you infer.
- **Preserve raw results.** Use scripts for data processing and plotting. Record failed, nonconvergent, and infeasible runs as well.
- **Maintain documentation alongside code.** Explain important assumptions, parameter choices, and implementation deviations in the relevant code or documentation.

## Planned Topics

| Topic | Planned coverage |
| --- | --- |
| Project organization | Directory conventions, naming, configuration management, and the roles of scripts and notebooks |
| Environments and dependencies | Python / MATLAB environments, version records, and running on different machines |
| Git workflows | Commit scope, branches, and linking results to code versions |
| From mathematics to code | Checking equations, mapping notation to code, and verifying units, dimensions, and assumptions |
| Numerical computing and optimization | Scaling, tolerances, initialization, derivative checks, solver status, and feasibility checks |
| Machine learning and surrogate models | Data splits, preprocessing, baselines, uncertainty, and evaluation metrics |
| Paper reproduction | Extracting experimental conditions, establishing baselines, comparing tables, and investigating discrepancies |
| Experiment management | Parameter sweeps, randomness, logging, result archiving, and failure analysis |
| Research figures and writing | Generating, labeling, and exporting figures and tables, and tracing reported numbers to their sources |
| AI-assisted coding | Providing context, defining the scope of changes, reviewing code, and verifying results |

## Workflow for a Research Task

1. **Define the problem:** State the question, inputs and outputs, success criteria, and known limitations.
2. **Check the sources:** Record papers, data, and reference implementations. Identify the equations, parameters, and conditions under which they apply.
3. **Establish a baseline:** Run a minimal case and check units, dimensions, boundary conditions, and expected behavior.
4. **Implement and verify:** Add complexity gradually, using meaningful checks to verify key properties and numerical results.
5. **Run experiments:** Save configurations and run information, and compare results using predefined metrics.
6. **Explain discrepancies:** Distinguish differences in models and implementations from numerical errors and random variation. Keep a record of unresolved questions.
7. **Prepare the deliverables:** Provide run instructions, a results summary, and scripts for generating figures and tables. State the scope of the conclusions.

## Experiment Records

For each experiment worth retaining or using in a paper, aim to record:

- **Purpose and identity:** Experiment name, date and time, and research question.
- **Code and environment:** Git commit, uncommitted changes, interpreter and key dependency versions, and hardware when relevant.
- **Data and configuration:** Data sources, preprocessing, parameters, random seeds, and the configuration actually used.
- **Execution:** Working directory, full command, and expected or actual runtime.
- **Numerical status:** Exit status, convergence information, tolerances, constraint residuals, and other applicable diagnostics.
- **Outputs and interpretation:** Raw outputs, summary metrics, figures and tables, observations, and questions requiring further checks.

Random seeds are only one part of reproducibility. The environment, data, and parallel execution can also affect results. When comparing algorithms, document the computational budget, stopping criteria, and evaluation conventions.

## Repository Structure

`docs/` contains ten guides, with runnable scripts in `examples/`; shared figures live in `docs/images/`. `templates/` and `references/` are planned and have not been created yet.

Main guides use `NN-main-topic.md`, with bilingual editions named `NN-main-topic.zh-CN.md`. Both editions are included in the repository. Supplementary example documents can share the chapter number, for example `01-example-topic.md`; this filename is reserved for future additions. HTML and PDF editions in `docs/print/` use the same stem as their source. Runnable Python scripts remain in `examples/`.

```text
research-coding-handbook/
├── README.md
├── README.zh-CN.md
├── docs/
│   ├── 01-main-running-and-debugging.md
│   ├── 01-main-running-and-debugging.zh-CN.md
│   ├── 01-SI-spyder.md
│   ├── 01-SI-spyder.zh-CN.md
│   ├── 02-main-markdown-images.md
│   ├── 02-main-markdown-images.zh-CN.md
│   ├── 03-main-python-data-types.md
│   ├── 03-main-python-data-types.zh-CN.md
│   ├── 03-example-01-mo-book-production.md
│   ├── 03-example-01-mo-book-production.zh-CN.md
│   ├── 04-main-github-manual-push.md
│   ├── 04-main-github-manual-push.zh-CN.md
│   ├── 05-main-python-dunder.md
│   ├── 05-main-python-dunder.zh-CN.md
│   ├── 06-main-github-organization.md
│   ├── 06-main-github-organization.zh-CN.md
│   ├── 07-main-conda-environment.md
│   ├── 07-main-conda-environment.zh-CN.md
│   ├── 08-main-python-classes.md
│   ├── 08-main-python-classes.zh-CN.md
│   ├── 09-main-codex-skills.md
│   ├── 09-main-codex-skills.zh-CN.md
│   ├── 10-main-python-imports-annotations-parsing.md
│   ├── 10-main-python-imports-annotations-parsing.zh-CN.md
│   ├── print/     # PDF and self-contained HTML editions
│   └── images/
│       └── 01-generated-data.png
├── examples/
│   ├── 01_spyder_function_inspection.py
│   ├── 02_plot_generated_data.py
│   ├── 03_python_data_types.py
│   ├── 03_example_01_mo_book_production.py
│   ├── verify_03_example_01.py
│   ├── 05_dunder_methods.py
│   ├── 08_python_classes.py
│   └── 10_python_annotations_and_parsing.py
├── tools/         # Print exporter and stylesheet
├── skills/        # Reusable handbook-writing skill source
├── templates/     # Planned: project, experiment, and report templates
└── references/    # Planned: source links and reading notes
```

Each example should specify its dependencies, run instructions, and expected results. Manage large datasets and bulk experiment outputs separately, and document how to obtain them or where they are stored.

## Use and Maintenance

When addressing a concrete problem, first build a small runnable example, then turn the reusable method into documentation or a template. Each note should aim to include the **problem context, approach, verification evidence, scope, and sources**.

When using AI to explain equations, generate code, investigate errors, or organize documentation, provide the necessary context and check key equations, interfaces, references, and execution results. Judgments that affect research conclusions must be traceable to original sources or actual experiments.

Prioritize practices that have been verified in real research and are likely to be reused. Clearly mark ideas that still need validation.
