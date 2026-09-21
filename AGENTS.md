# Research Coding Handbook — AI 工作约定

本文件记录本仓库的长期约定。开始工作前先阅读；用户在当前任务中的明确要求优先于这里的默认做法。

## 沟通与内容

- 默认使用中文与用户交流，面向科研编程初学者解释。
- 中文解释保留关键术语的英文，例如解释器（interpreter）、环境（environment）。
- 教程包含问题、具体步骤、示例和结果核对；区分教学示例与实际项目结果。
- 优先依据官方资料核对软件操作，并在教程中给出来源链接。
- 不将尚未执行的安装、组织创建或实验写成已完成的事实。

## 文档结构与双语格式

- 主教程位于 `docs/`，沿用现有顺序，以两位数字编号并加 `main`，例如 `08-main-topic.md`。先检查已有编号，不覆盖现有章节；同一主题的补充示例文档可使用 `08-example-topic.md`。
- 标题使用 `08 — ...`，不使用 `Q08`；Markdown、HTML 和 PDF 编号一致。
- 每篇主教程维护英文版 `NN-main-topic.md` 和英中双语版 `NN-main-topic.zh-CN.md`；补充示例文档同样维护两个版本。
- `.zh-CN.md` 现在表示完整双语文档，不是仅中文翻译：英文一段，紧接对应中文一段。
- 列表逐条英中对照；表格在同一单元格中英文在上、中文在下，可用 `<br>` 换行。
- 完全相同的代码和图片只放一次；不同内容不要在去重时丢失。
- 两个版本内容同步更新。双语 Markdown 是独立源文件，打印导出器不会自动翻译或拼接英文版。
- 新增或调整教程后，更新 `README.md` 和 `README.zh-CN.md` 的目录与相关说明。
- 可运行脚本位于 `examples/`，注明依赖和运行方法；只做与修改相关的必要验证。

## 图片与占位

- 图片放在 `docs/images/`，使用相对路径；双语版本可以共用图片。
- 图注在每篇文档内按 `Figure 1 / 图 1`、`Figure 2 / 图 2` 的顺序编号，不添加章节编号前缀。
- 暂无截图时，添加可见的文字占位，说明应展示的内容和建议文件名。
- 可以在 HTML 注释中保存待启用的 Markdown 图片语句；不要直接引用不存在的图片而产生破图。
- 保留已有截图占位及其替换说明。

## 打印与导出

- 修改教程后，更新对应 HTML 和 PDF，输出到 `docs/print/`。
- 使用现有 `tools/export_print.py` 和 `tools/print.css`，纸张为 US Letter，版式适合黑白打印。
- 英文输出沿用源文件名 `NN-main-topic.html/.pdf`；双语输出沿用 `NN-main-topic.zh-CN.html/.pdf`；补充示例文档保留其 `example` 文件名。
- 导出器需要 Python-Markdown，以及 Chrome 或 Edge。使用已有且满足依赖的 Python 环境。
- 只修改个别章节时，显式传入这些章节路径，避免无关文件全部重新生成。

```text
python tools/export_print.py docs/NN-main-topic.md docs/NN-main-topic.zh-CN.md
```

- 全部英文版：`python tools/export_print.py`。
- 全部双语版：`python tools/export_print.py --bilingual`。
- 新增章节时同步更新导出器的 `DEFAULT_DOCS`。
- 导出后检查标题、中文显示、链接和明显越界；如有 PDF 被占用或导出失败，应明确报告。
- 不需要把本文件等仓库管理文件当作教程导出 PDF。

## Git 与已有文件

- 开始编辑前检查 `git status` 和相关文件，保留用户已有改动，不重置或覆盖无关内容。
- `README.zh-CN.md`、`docs/*.zh-CN.md` 和 `docs/print/*.zh-CN.*` 与英文版本一起纳入 Git，不再忽略。
- 提交与推送时同步包含双语源文件和双语打印文件；原始内部指南继续按现有规则忽略。
- 提交或推送时检查实际文件清单，避免把调试日志、缓存和临时文件一起纳入。
- 教程完成不代表已经提交或推送；最终回复明确说明完成的文件和 Git 操作状态。
