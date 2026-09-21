# 02 — What is a practical way to insert images into Markdown? / 02 — Markdown 文件中怎样插入和管理图片？

<!-- bilingual: en-zh -->

<!-- print:omit -->
[返回手册 / Handbook](../README.zh-CN.md) · [English](02-main-markdown-images.md)

[英中双语 PDF / Bilingual PDF](print/02-main-markdown-images.zh-CN.pdf) · [打印 HTML / Print HTML](print/02-main-markdown-images.zh-CN.html)
<!-- /print:omit -->

## Question / 问题（Question）

> How should I insert screenshots or figures into a `.md` file and organize their image files?
>
> `.md` 文件中要插入截图（screenshot）或科研图（figure），怎样操作和组织图片文件比较方便？

**For this repository, save images in `docs/images/` and reference them with relative paths.** This keeps a chapter and its figures portable when the repository is copied or cloned.

**本仓库将图片放在 `docs/images/`，文档使用相对路径（relative path）引用。** 这样复制或克隆（clone）仓库后，文档仍能找到对应图片。

## 1. Save the image, then reference it / 1. 先保存图片，再写引用（Image reference）

The repository already contains this example:

仓库中已经有一个可用示例：

```text
research-coding-handbook/
├── README.md
└── docs/
    ├── 01-main-spyder-function-inspection.md
    ├── 02-main-markdown-images.md
    └── images/
        └── 01-generated-data.png
```

In a chapter inside `docs/`, write:

在 `docs/` 里的章节文件中写：

English example:

```markdown
![Local and global random samples compared with an exponential curve.](images/01-generated-data.png)
```

中文示例：

```markdown
![局部和全局随机数据与指数曲线的对比。](images/01-generated-data.png)
```

In the root `README.md`, write:

在仓库根目录的 `README.md` 或 `README.zh-CN.md` 中写：

English example:

```markdown
![Local and global random samples compared with an exponential curve.](docs/images/01-generated-data.png)
```

中文示例：

```markdown
![局部和全局随机数据与指数曲线的对比。](docs/images/01-generated-data.png)
```

The path starts from the directory containing the Markdown file. In these examples, `images/` means a child directory and `../` would mean one directory up. Use forward slashes `/` in links, including on Windows. The text in brackets is **alternative text**, a short description of the image. See [GitHub: images and relative links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images).

路径从**当前 Markdown 文件所在目录**开始计算。本例 `images/` 是子目录（child directory），`../` 表示上一级目录（parent directory）。链接中使用正斜杠（forward slash）`/`，Windows 下也一样。方括号内是替代文本（alternative text / alt text），用一句话描述图片内容。参见 [GitHub：图片与相对链接](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images)。

## 2. See an actual embedded figure / 2. 看一个实际插图（Embedded figure）

![Local and global random samples compared with an exponential curve. / 局部和全局随机数据与指数曲线的对比。](images/01-generated-data.png)

*Figure: Both versions use seed 5, ten observations, and noise standard deviation 0.12.*

*图注（caption）：两种方法都使用种子 5、10 个观测值及标准差 0.12。*

The image above is a real file generated from the [Q1 example](../examples/01_spyder_function_inspection.py). To regenerate it from the repository root, use an environment with NumPy and Matplotlib:

上图是真实图片文件，数据来自[问题 1 的代码](../examples/01_spyder_function_inspection.py)。需要重新生成时，在仓库根目录使用装有 NumPy、Matplotlib 的环境运行：

```text
python examples/02_plot_generated_data.py
```

The script writes `docs/images/01-generated-data.png`; running it again updates that figure.

脚本输出 `docs/images/01-generated-data.png`，再次运行会更新这张图。

## 3. Insert a Spyder screenshot in VS Code / 3. 在 VS Code 中插入 Spyder 截图（Screenshot workflow）

1. Capture the relevant Spyder panes and save the screenshot as a PNG in `docs/images/`, for example `01-spyder-local-breakpoint.png`.

   截取相关 Spyder 面板，保存为 PNG 图片，例如 `docs/images/01-spyder-local-breakpoint.png`。

2. Open the intended `.md` file. Run **Markdown: Insert Image from Workspace** from the command palette and select the saved image. Alternatively, drag it over the Markdown editor, then hold **Shift** as you drop it.

   打开目标 `.md` 文件，在命令面板（command palette）执行 **Markdown: Insert Image from Workspace**，选择刚保存的图片。也可以先把图片拖到 Markdown 编辑区上方，再按住 **Shift** 松开鼠标插入。

3. Add descriptive alternative text and a short caption stating where execution paused and what the image demonstrates.

   补写替代文本（alt text），并在图片下方写一行图注（caption），说明暂停位置和想展示的现象。

4. On Windows, press **Ctrl+Shift+V** to preview the Markdown, or press **Ctrl+K**, then **V**, for a preview beside the editor.

   Windows 下按 **Ctrl+Shift+V** 打开 Markdown 预览（preview）；依次按 **Ctrl+K**、**V** 可在右侧预览。

Pasting image data is also supported. Check where the editor saved the image; VS Code's `markdown.copyFiles.destination` setting controls that destination. See [VS Code: Markdown images and preview](https://code.visualstudio.com/docs/languages/markdown).

也可以粘贴剪贴板里的图片；粘贴后检查实际保存位置。VS Code 的 `markdown.copyFiles.destination` 设置用于控制图片保存目录。参见 [VS Code：Markdown 图片与预览](https://code.visualstudio.com/docs/languages/markdown)。

For Q1, a useful screenshot shows the paused `return x, y` line and the Variable Explorer entries for `x`, `y_true`, `noise`, and `y` together.

问题 1 的截图可以同时展示：暂停在 `return x, y` 的编辑器（Editor），以及变量浏览器（Variable Explorer）中的 `x`、`y_true`、`noise` 和 `y`。

## 4. Control display width when needed / 4. 需要时控制显示宽度（Display width）

For a renderer that supports raw HTML, you can use:

如果所用渲染器（renderer）支持原始 HTML，可以写：

English example:

```html
<img src="images/01-generated-data.png"
     alt="Local and global random samples compared with an exponential curve."
     width="760">
```

中文示例：

```html
<img src="images/01-generated-data.png"
     alt="局部和全局随机数据与指数曲线的对比。"
     width="760">
```

Here the path is for a Markdown file inside `docs/`; a root README needs `docs/images/01-generated-data.png`. HTML rendering varies by viewer, so check the target preview. Ordinary Markdown image syntax is the more portable starting point.

这里的路径适用于 `docs/` 中的文件；根目录 README 应改为 `docs/images/01-generated-data.png`。不同查看器对 HTML 的处理可能不同，写完后检查目标预览效果；普通 Markdown 图片语法更适合作为通用写法。

## 5. File and Git conventions / 5. 文件与 Git 约定（File and Git conventions）

- Use descriptive filenames, such as `01-spyder-local-breakpoint.png`. PNG is a practical choice for screenshots; for generated plots, retain the script so labels or resolution can be changed later.

  使用能说明内容的文件名（filename），如 `01-spyder-local-breakpoint.png`。截图使用 PNG 比较方便；生成的科研图应保留绘图脚本（plotting script），便于修改标注和分辨率（resolution）。

- Keep the image and its Markdown reference together in version control when the image should be shared. Ignoring a Markdown file does not automatically ignore the images it references.

  需要共享图片时，图片文件与 Markdown 引用一起纳入版本控制（version control）。忽略一个 `.md` 文件，不会自动忽略它引用的图片。

- The two language versions can reference the same image; each supplies its own alternative text and caption. This repository tracks both language versions, their HTML/PDF print editions, and the shared example PNG in Git.

  中英两版可以共用同一张图，分别写各自的替代文本和图注。本仓库将两个语言版本、对应的 HTML/PDF 打印版，以及共享示例 PNG 一起纳入 Git 版本控制（version control）。

- If an image does not display, check that it exists, that the path is relative to the current `.md` file, and that filename capitalization matches. Also check that you wrote `![description](path)`: omitting `!` produces a link instead of an image.

  图片无法显示时，检查文件是否存在、路径是否相对于当前 `.md` 文件、文件名大小写是否一致，并确认语法是 `![说明](路径)`；少了 `!` 就会变成普通链接（link）。
