# Research Coding Handbook

[English handbook](README.md)

科研编程手册：记录从研究问题、数学模型到可靠代码、可复现实验和论文结果的实践方法。

本仓库用于积累科研中反复用到的编程经验、工作流程和模板，重点关注 Python / MATLAB、数值计算、优化与机器学习。目标是让研究过程有据可查，让代码可以维护，让结果能够复现。

> 当前状态：已有九篇指南（guides），涵盖 Spyder 调试、Markdown 插图、Python 数据类型、GitHub 同步、dunder、组织创建、conda 环境、Python 类与 Codex skills，附可运行示例（runnable examples）及生成的图片。

## 工作环境（Workspace context）

| 项目（field） | 记录值（recorded value） |
| --- | --- |
| 设备（device） | `Legion T7 34IRZ8` |
| 对话名（conversation title） | `Locate research-coding-handbook` |

## 问题与示例（Questions and worked examples）

**问题 1：在 Spyder 中逐个理解随机数据生成函数的变量**

> 作为 Python 新手，如果有一个函数（function），想查看其中每个变量（variable）的种类和大小（size），应该如何在 Spyder 中拆解这个函数（break down a function），逐步执行并理解各个变量？

- [阅读双语指南](docs/01-main-spyder-function-inspection.zh-CN.md)：断点（breakpoint）、局部变量（local variables）、单步执行（stepping），以及 `type`、`dtype`、`shape`、`size` 和 `len` 的区别。
- [运行示例](examples/01_spyder_function_inspection.py)：局部／全局随机数函数，显式保留信号与噪声数组，标出断点（breakpoints），并在指南中讲解形状检查（shape checks）。

**问题 2：Markdown 中插入和管理图片**

> `.md` 文件中要插入截图（screenshot）或科研图（figure），怎样操作和组织图片文件比较方便？

- [阅读中文插图指南](docs/02-main-markdown-images.zh-CN.md)：相对路径（relative paths）、VS Code 插入与预览（preview）、显示宽度，以及双语共用图片的方法。
- [重新生成示例图](examples/02_plot_generated_data.py)：将两组随机数据对比图保存到 `docs/images/01-generated-data.png`。

**问题 3：Python 数据类型与 Case 1 利润方程**

> `float`、`tuple` 等数据类型（data types）有什么区别？如何查看变量类型、大小与可变性，并对应到 Case 1 方程？

- [阅读双语指南](docs/03-main-python-data-types.zh-CN.md)：主要内置类型、NumPy 数组、别名与复制，以及利润函数逐行解析。
- [运行示例](examples/03_python_data_types.py)：类型速查对象、四个利润情景和独立循环验证。
- [US Letter 英中双语 PDF](docs/print/03-main-python-data-types.zh-CN.pdf) · [双语打印 HTML](docs/print/03-main-python-data-types.zh-CN.html)。

**04：GitHub 手动同步（Manual GitHub sync）**

- [双语指南](docs/04-main-github-manual-push.zh-CN.md) · [英中双语 PDF](docs/print/04-main-github-manual-push.zh-CN.pdf) · [双语打印 HTML](docs/print/04-main-github-manual-push.zh-CN.html)。包含在 VS Code 中打开 PowerShell、确认项目目录的逐步操作和缩略截图，可通过图注链接查看原尺寸图片。 另含 `git pull --ff-only` 的原文解释、快进与分叉示意，以及 `origin main` 的含义。

**05：Python 双下划线方法（Dunder methods）**

- [双语指南](docs/05-main-python-dunder.zh-CN.md)：特殊方法、利润容器与 `__name__` 入口判断。
- [运行示例](examples/05_dunder_methods.py) · [英中双语 PDF](docs/print/05-main-python-dunder.zh-CN.pdf) · [双语打印 HTML](docs/print/05-main-python-dunder.zh-CN.html)。

**06：创建 GitHub 组织（Organization）**

- [双语指南](docs/06-main-github-organization.zh-CN.md) · [英中双语 PDF](docs/print/06-main-github-organization.zh-CN.pdf) · [HTML](docs/print/06-main-github-organization.zh-CN.html)。
- 组织创建、仓库归属及三个插图占位（screenshot placeholders）。

**07：安装和使用 conda 环境（Environment）**

- [双语指南](docs/07-main-conda-environment.zh-CN.md) · [英中双语 PDF](docs/print/07-main-conda-environment.zh-CN.pdf) · [HTML](docs/print/07-main-conda-environment.zh-CN.html)。
- Windows 安装检查、创建环境、VS Code 解释器选择及三个插图占位。

**08：理解 Python 类与对象（Classes and objects）**

- [双语指南](docs/08-main-python-classes.zh-CN.md)：类、实例、`self`、初始化、属性、方法，以及各自保存数据的实验记录对象。
- [运行示例](examples/08_python_classes.py) · [英中双语 PDF](docs/print/08-main-python-classes.zh-CN.pdf) · [双语打印 HTML](docs/print/08-main-python-classes.zh-CN.html)。

**09：Codex Skills 入门、安装与科研绘图**

- [英中双语指南](docs/09-main-codex-skills.zh-CN.md)：skill 文件结构、个人级与项目级安装、`.agents/skills` 与 `.codex/skills` 的区别、调用、维护，以及 `scientific-visualization` 科研绘图案例。
- 收录可复制提示词、Matplotlib 示例和本篇教程的原始编写请求。安装命令仅作为教程示例；新增本章不代表已安装 skill 或修改 Python 环境。
- [US Letter 英中双语 PDF](docs/print/09-main-codex-skills.zh-CN.pdf) · [双语打印 HTML](docs/print/09-main-codex-skills.zh-CN.html)。

## 打印版本（Print editions）

`docs/` 中 01–09 的 `.zh-CN.md` 文件是英中双语文档：英文一段、中文一段，列表逐条对照，表格在同一单元格内上下对照。英文 `.md` 继续单独保留；相同代码和图片只放一次。双语文件保留 `.zh-CN` 后缀，与英文版本及对应的 HTML/PDF 打印版一起纳入 Git 并发布到 GitHub。

运行 `python tools/export_print.py --bilingual` 可直接从这些双语 Markdown 生成全部 01–09 的 PDF 和 HTML。也可以在命令后显式传入某个 `.zh-CN.md` 路径。导出器不再自动拼接两个语言文件。

问题 1 已提供 [US Letter 英中双语 PDF](docs/print/01-main-spyder-function-inspection.zh-CN.pdf) 和[独立双语打印 HTML](docs/print/01-main-spyder-function-inspection.zh-CN.html)。版式采用黑色文字、灰度图片（grayscale figures）、页码（page numbers）、跨页重复表头（repeated table headers）及编号来源网址，方便纸面阅读。

修改 Markdown 后，可在装有 Python-Markdown 且能使用 Chrome 或 Edge 的 Python 环境中运行 `python tools/export_print.py`，重新生成 01–09 英文版；双语版本可用 `--bilingual`，或在命令后显式传入对应 `.zh-CN.md` 路径。导出器已在 Windows、Python-Markdown 3.8、Chrome 152 下验证。样式表（stylesheet）为 `tools/print.css`，输出目录为 `docs/print/`。双语导出文件与源文件一起提交到 Git。

## 基本原则

- **先明确问题，再实现算法。** 写清研究目标、假设、变量、单位、约束和评价指标。
- **从最小可验证案例开始。** 优先用解析解、小规模算例或可靠基准检查实现，再扩展到完整问题。
- **保留可追溯的实验记录。** 将结果关联到代码版本、配置、数据来源、环境和运行命令。
- **区分事实与判断。** 分开记录论文原述、代码实现、实验观察和个人推断。
- **保留原始结果。** 数据处理与绘图由脚本完成；失败、不收敛和不可行的运行也应记录。
- **让文档跟随代码。** 重要假设、参数选择和实现偏差，应在相关代码或文档中说明。

## 内容规划

| 主题 | 计划整理的内容 |
| --- | --- |
| 项目组织 | 目录约定、命名、配置管理、脚本与 Notebook 的分工 |
| 环境与依赖 | Python / MATLAB 环境、版本记录、跨机器运行 |
| Git 工作流 | 提交粒度、分支、结果与代码版本的关联 |
| 数学到代码 | 公式核对、符号映射、单位、维度和假设检查 |
| 数值计算与优化 | 缩放、容差、初始化、导数检查、求解器状态与可行性验证 |
| 机器学习与代理模型 | 数据划分、预处理、基准模型、不确定性与评价指标 |
| 论文复现 | 提取实验条件、搭建基线、对照表格与分析差异 |
| 实验管理 | 参数扫描、随机性、日志、结果归档与失败分析 |
| 科研绘图与写作 | 图表生成、标注、导出，以及论文数字的来源追踪 |
| AI 辅助编程 | 提供上下文、限定修改范围、审查代码与验证结果 |

## 一次研究任务的工作流程

1. **定义问题**：写下要回答的问题、输入输出、成功标准和已知限制。
2. **核对来源**：记录论文、数据和参考实现；标明公式、参数及适用条件。
3. **建立基线**：跑通最小案例，检查单位、维度、边界条件和预期行为。
4. **实现与验证**：逐步增加复杂度，用有意义的检查验证关键性质与计算结果。
5. **开展实验**：保存配置和运行信息，按预先定义的指标比较结果。
6. **解释差异**：区分模型差异、实现差异、数值误差和随机波动；对未解释的问题保留记录。
7. **整理交付**：提供运行说明、结果摘要及生成图表的脚本，并写清结论的适用范围。

## 实验记录约定

每次需要保留或用于论文的实验，尽量记录：

- **目的与标识**：实验名称、时间、研究问题。
- **代码与环境**：Git 提交号、未提交修改、解释器和关键依赖版本；必要时记录硬件。
- **数据与配置**：数据来源、预处理、参数、随机种子及实际使用的配置。
- **运行方式**：工作目录、完整命令、预计或实际耗时。
- **数值状态**：退出状态、收敛信息、容差和约束残差等适用指标。
- **产出与判断**：原始输出、汇总指标、图表、观察到的现象及待核查问题。

随机种子只是复现记录的一部分；环境、数据、并行计算方式等也可能影响结果。比较算法时，应说明计算预算、终止条件和评价口径。

## 仓库结构（Repository structure）

`docs/` 已包含九篇指南，可运行脚本位于 `examples/`，共用图片放在 `docs/images/`；`templates/` 和 `references/` 为规划目录，尚未创建。英文与双语 Markdown、打印版和共享图片均纳入版本控制。原始内部推送指南继续仅保留在本地，仓库发布其脱敏版。

主教程使用 `NN-main-topic.md`，英中双语版使用 `NN-main-topic.zh-CN.md`。同主题的补充示例文档可沿用章节编号，例如 `01-example-topic.md`；该名称用于说明后续命名方式，目前尚未创建。`docs/print/` 内 HTML 和 PDF 与源文件同名，仅扩展名不同。可运行 Python 脚本继续放在 `examples/`。

```text
research-coding-handbook/
├── README.md
├── README.zh-CN.md                     # 中文目录（Chinese contents）
├── docs/
│   ├── 01-main-spyder-function-inspection.md
│   ├── 01-main-spyder-function-inspection.zh-CN.md
│   ├── 02-main-markdown-images.md
│   ├── 02-main-markdown-images.zh-CN.md
│   ├── 03-main-python-data-types.md
│   ├── 03-main-python-data-types.zh-CN.md
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
│   ├── print/                          # US Letter PDF 与打印 HTML
│   └── images/
│       └── 01-generated-data.png       # 双语共用（shared image）
├── examples/
│   ├── 01_spyder_function_inspection.py
│   ├── 02_plot_generated_data.py
│   ├── 03_python_data_types.py
│   ├── 05_dunder_methods.py
│   └── 08_python_classes.py
├── tools/                              # 打印导出器与样式表
├── templates/                          # 规划：项目、实验、报告模板
└── references/                         # 规划：来源链接与阅读笔记
```

示例应说明依赖、运行方法和预期结果。大型数据与批量实验输出应单独管理，并在仓库中记录获取方式或存放位置。

## 使用与维护

遇到一个具体问题时，先形成可运行的小例子，再把可复用的方法整理成文档或模板。每篇笔记尽量包含：**问题背景、解决方法、验证依据、适用范围和参考来源**。

使用 AI 协助解释公式、生成代码、排查错误或整理文档时，应提供必要上下文，并核对关键公式、接口、引用及运行结果。涉及研究结论的判断，需要能追溯到原始来源或实际实验。

优先补充实际研究中已经验证、会反复使用的内容；未经验证的想法明确标记为待验证。
