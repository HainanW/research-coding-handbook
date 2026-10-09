# 09 — Codex skills: a beginner’s guide

<!-- print:omit -->
[Handbook / 手册](../README.md) · [Other edition / 另一版本](09-main-codex-skills.zh-CN.md) · [Bilingual PDF / 双语 PDF](print/09-main-codex-skills.zh-CN.pdf)
<!-- /print:omit -->

## 1. What is a skill?

A skill is a reusable set of instructions for a particular task. For example, `research-coding-handbook` tells the assistant how to turn code into a beginner-friendly, bilingual tutorial. Your prompt specifies which code and what result you want.

A Python library provides code that Python executes. A skill guides the assistant; installing one does not automatically install Python packages or read every file in a repository.

Each skill has a `SKILL.md` entry file. `name` identifies it; `description` describes when to use it; the remaining text explains the steps. Supporting scripts and reference files are optional. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## 2. Use the installed handbook skill

This machine already has a personal installation of `research-coding-handbook`, recognized in the current session. In the **Codex chat box**, type `$` to select it, or send this request. Do not type it in PowerShell:

```text
$research-coding-handbook
Explain examples/10_python_annotations_and_parsing.py.
Keep it concise and suitable for a beginner.
Maintain English and bilingual Markdown;
generate only a bilingual PDF.
```

A useful result should explain the selected code, show how to run it, and give a result to check. To confirm which skill was used, ask: “Report the path of the SKILL.md you loaded.” A folder existing on disk is not proof that a session loaded it.

## 3. Personal, project, and built-in skills

| Type | Where and who uses it |
| --- | --- |
| Personal | Under your user folder; usable across your projects. |
| Project | Under the project’s `.agents/skills/`; scoped to that project. |
| Built-in | Bundled with Codex; this machine stores them under `.codex/skills/.system/`. |

The installed handbook skill on this machine is at:

```text
C:\Users\TQD\.codex\skills\research-coding-handbook\SKILL.md
```

That is a personal installation for user TQD, not an installation for every Windows user. The `.system` label means Codex-provided skills; it does not grant Windows administrator permissions.

Current official guidance lists `~/.agents/skills` for personal skills and `<project>/.agents/skills` for project skills; `~` means your home folder. The bundled installer inspected here defaults to `~/.codex/skills`. For an installation, confirm the actual destination and recognition in your client. See [skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

The repository’s [skill source](../skills/research-coding-handbook/SKILL.md) and the installed personal copy are separate files. Updating this repository does not automatically update the installed copy.

## 4. What do the built-in skills do?

These six folders were found in this machine’s `.system` directory. This is a local snapshot, not a universal list for every Codex version or a guarantee that each is loaded:

| Skill | Purpose |
| --- | --- |
| `imagegen` | Generate or edit images. |
| `openai-docs` | Check official OpenAI instructions. |
| `plugin-creator` | Package skills and tools as a plugin. |
| `review-agent` | Review delegated code changes without editing them. |
| `skill-creator` | Create or improve a reusable skill. |
| `skill-installer` | Install a skill from a supported source or repository. |

## 5. Install one on another machine

On a machine where this skill is missing, send the following in the **Codex chat box**. First confirm the source and destination; keep an existing installation if one is found.

```text
$skill-installer
Install the skill from HainanW/research-coding-handbook,
folder skills/research-coding-handbook.
Use a personal installation and report its destination.
If a copy already exists, report it before replacing it.
```

After installation, look for it using `$` or `/skills`. If it is missing, restart Codex and check again. Ask for the loaded path to confirm recognition. See [official installation guidance](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use).

For an update, compare the installed copy with the source and preserve local edits before replacing it. Creating your own workflow is a separate task for `$skill-creator`.

## 6. Quick checks

| Symptom | First check |
| --- | --- |
| Cannot find the skill | Check the directory and `SKILL.md`, then restart Codex. |
| Wrong behavior or an old version | Ask which SKILL.md path was loaded. |
| Python import fails | Check the interpreter and package; the skill folder does not install it. |

Checked on 2026-10-09 against official documentation and local skill files. The handbook skill was available in this session. This edit reorganized the tutorial only; the installation prompts above were not executed.
