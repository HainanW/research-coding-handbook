# 09 — Codex skills: a beginner’s guide / Codex 技能入门

<!-- bilingual: en-zh -->

<!-- print:omit -->
[Handbook / 手册](../README.zh-CN.md) · [Other edition / 另一版本](09-main-codex-skills.md) · [Bilingual PDF / 双语 PDF](print/09-main-codex-skills.zh-CN.pdf)
<!-- /print:omit -->

## 1. What is a skill? / Skill 是什么？

A skill is a reusable set of instructions for a particular task. For example, `research-coding-handbook` tells the assistant how to turn code into a beginner-friendly, bilingual tutorial. Your prompt specifies which code and what result you want.

技能（skill）是一套可重复使用的任务说明。例如，`research-coding-handbook` 规定怎样把代码整理成适合新手的双语教程；你的提问则指定本次处理哪个文件、需要什么结果。

A Python library provides code that Python executes. A skill guides the assistant; installing one does not automatically install Python packages or read every file in a repository.

Python 库提供交给 Python 执行的代码；skill 指导助手怎么做事。安装 skill 不会自动安装 Python 软件包，也不会自动读取仓库里的全部文件。

Each skill has a `SKILL.md` entry file. `name` identifies it; `description` describes when to use it; the remaining text explains the steps. Supporting scripts and reference files are optional. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

每个 skill 都有入口文件 `SKILL.md`：`name` 是名称，`description` 说明何时使用，后面的正文写操作步骤。辅助脚本和参考文件按需要添加。参见[官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

## 2. Use the installed handbook skill / 先用本机已有的技能

This machine already has a personal installation of `research-coding-handbook`, recognized in the current session. In the **Codex chat box**, type `$` to select it, or send this request. Do not type it in PowerShell:

本机已有个人级 `research-coding-handbook`，当前会话也已识别。在 **Codex 聊天框**输入 `$` 选择它，或发送下面的请求。不要输入到 PowerShell 终端：

```text
$research-coding-handbook
Explain examples/10_python_annotations_and_parsing.py.
Keep it concise and suitable for a beginner.
Maintain English and bilingual Markdown;
generate only a bilingual PDF.
```

```text
$research-coding-handbook
请讲解 examples/10_python_annotations_and_parsing.py。
面向新手，篇幅适中。
维护英文和双语 Markdown，只生成双语 PDF。
```

A useful result should explain the selected code, show how to run it, and give a result to check. To confirm which skill was used, ask: “Report the path of the SKILL.md you loaded.” A folder existing on disk is not proof that a session loaded it.

结果应说明选定代码的作用、运行步骤，以及可核对的输出。想确认用了哪一份 skill，可问：“请告诉我本次读取的 SKILL.md 路径。”文件夹存在，不等于当前会话已经加载。

## 3. Personal, project, and built-in skills / 个人级、项目级与内置技能

| Type<br>类型 | Where and who uses it<br>位置与使用范围 |
| --- | --- |
| Personal<br>个人级 | Under your user folder; usable across your projects.<br>放在自己的用户目录中，可供自己的不同项目使用。 |
| Project<br>项目级 | Under the project’s `.agents/skills/`; scoped to that project.<br>放在项目的 `.agents/skills/` 中，供该项目使用。 |
| Built-in<br>内置 | Bundled with Codex; this machine stores them under `.codex/skills/.system/`.<br>Codex 自带；本机位于 `.codex/skills/.system/`。 |

The installed handbook skill on this machine is at:

本机已安装的手册技能位于：

```text
C:\Users\TQD\.codex\skills\research-coding-handbook\SKILL.md
```

That is a personal installation for user TQD, not an installation for every Windows user. The `.system` label means Codex-provided skills; it does not grant Windows administrator permissions.

这是 TQD 用户的个人安装，不是所有 Windows 用户共用的安装。`.system` 表示 Codex 提供的内置技能，不代表拥有 Windows 管理员权限。

Current official guidance lists `~/.agents/skills` for personal skills and `<project>/.agents/skills` for project skills; `~` means your home folder. The bundled installer inspected here defaults to `~/.codex/skills`. For an installation, confirm the actual destination and recognition in your client. See [skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

当前官方说明将个人技能放在 `~/.agents/skills`，项目技能放在 `<项目>/.agents/skills`；`~` 表示用户主目录。本次检查的内置安装器默认使用 `~/.codex/skills`。安装时应核对实际位置，以及客户端是否识别。参见[技能位置说明](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。

The repository’s [skill source](../skills/research-coding-handbook/SKILL.md) and the installed personal copy are separate files. Updating this repository does not automatically update the installed copy.

仓库里的[技能源文件](../skills/research-coding-handbook/SKILL.md)和个人目录中的已安装版本是两份文件。更新仓库，不会自动更新个人安装版本。

## 4. What do the built-in skills do? / 内置技能各做什么？

These six folders were found in this machine’s `.system` directory. This is a local snapshot, not a universal list for every Codex version or a guarantee that each is loaded:

本次在这台电脑的 `.system` 中发现以下六个技能。这是本机记录，不代表所有 Codex 版本的清单，也不表示每个都已加载：

| Skill<br>技能 | Purpose<br>用途 |
| --- | --- |
| `imagegen`<br>图片生成 | Generate or edit images.<br>生成或修改图片。 |
| `openai-docs`<br>官方文档 | Check official OpenAI instructions.<br>核对 OpenAI 产品和 API 的官方说明。 |
| `plugin-creator`<br>插件创建 | Package skills and tools as a plugin.<br>把技能和工具整理成可安装的插件。 |
| `review-agent`<br>代码检查 | Review delegated code changes without editing them.<br>接受委派，检查代码改动中的问题；只检查，不修改文件。 |
| `skill-creator`<br>技能创建 | Create or improve a reusable skill.<br>把做事流程编写成技能，或改进已有技能。 |
| `skill-installer`<br>技能安装 | Install a skill from a supported source or repository.<br>从支持的来源或仓库安装技能。 |

## 5. Install one on another machine / 换电脑后如何安装？

On a machine where this skill is missing, send the following in the **Codex chat box**. First confirm the source and destination; keep an existing installation if one is found.

在尚未安装该技能的电脑上，将下面的请求发送到 **Codex 聊天框**。先确认来源和安装位置；若已有安装，先保留原版本。

```text
$skill-installer
Install the skill from HainanW/research-coding-handbook,
folder skills/research-coding-handbook.
Use a personal installation and report its destination.
If a copy already exists, report it before replacing it.
```

```text
$skill-installer
请安装 HainanW/research-coding-handbook 仓库中
skills/research-coding-handbook 目录下的技能。
安装为个人级技能，并告诉我安装位置。
如果已有版本，请先说明，不直接覆盖。
```

After installation, look for it using `$` or `/skills`. If it is missing, restart Codex and check again. Ask for the loaded path to confirm recognition. See [official installation guidance](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use).

安装后，通过 `$` 或 `/skills` 查找；未出现时，重启 Codex 再检查。让助手报告读取路径，可进一步确认识别情况。参见[官方安装说明](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use)。

For an update, compare the installed copy with the source and preserve local edits before replacing it. Creating your own workflow is a separate task for `$skill-creator`.

更新时，先比较已安装版本与源文件，保留自己的修改后再替换。若要制作自己的流程，则使用 `$skill-creator`。

## 6. Quick checks / 遇到问题先查什么？

| Symptom<br>现象 | First check<br>先检查 |
| --- | --- |
| Cannot find the skill<br>找不到技能 | Check the directory and `SKILL.md`, then restart Codex.<br>检查目录和 `SKILL.md` 是否存在，再重启 Codex。 |
| Wrong behavior or an old version<br>行为不符或版本旧 | Ask which SKILL.md path was loaded.<br>询问实际读取的 SKILL.md 路径。 |
| Python import fails<br>Python 导入报错 | Check the interpreter and package; the skill folder does not install it.<br>检查解释器和软件包；技能文件夹不会替你安装依赖。 |

Checked on 2026-10-09 against official documentation and local skill files. The handbook skill was available in this session. This edit reorganized the tutorial only; the installation prompts above were not executed.

核对日期：2026-10-09，依据官方文档与本机技能文件。当前会话可使用手册技能。本次只重整教程，没有执行上面的安装请求。
