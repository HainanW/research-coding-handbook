# GitHub 手动同步指南（公开脱敏版）

更新日期：2026-09-14

本版移除了内部项目名称、组织信息、本机用户名、绝对路径和专用环境名称。原始 Markdown 与 PDF 仅保留本地，不加入 Git 提交。

本文以公开仓库 `HainanW/research-coding-handbook` 为例。GitHub 保存的是已经提交并推送的文件；被忽略的本地原件不会自动备份到 GitHub。

## 1. 进入仓库并确认远程地址

在本地项目文件夹中打开 PowerShell，逐条执行：

```powershell
git status
git remote -v
git branch --show-current
```

本仓库的 `origin` 应指向 `https://github.com/HainanW/research-coding-handbook.git`，当前分支为 `main`。

在另一台电脑首次下载时，可以在目标父目录运行：

```powershell
git clone https://github.com/HainanW/research-coding-handbook.git
cd research-coding-handbook
```

`git clone` 的目标目录应不存在或为空。已有文件的文件夹需要先比较、备份并合并文件，不能直接覆盖。

## 2. 获取 GitHub 上的更新

工作区干净时执行：

```powershell
git pull --ff-only origin main
```

如果有尚未提交的修改，先按下一节检查并提交，再拉取。如果提示分支已经分叉，先检查 `git log --oneline --graph --all`，协调合并后再推送。不要强制覆盖远程历史。

## 3. 检查、暂存并提交本地文件

```powershell
git status --short
git diff
git add -- README.md
git diff --cached --stat
git diff --cached
git commit -m "Update handbook documentation"
```

将 `README.md` 替换为本次确实需要上传的文件名，也可以一次列出多个文件。提交说明应描述实际修改。新文件需要单独打开检查；Word、PDF 等二进制文件也要查看内容，不能只看差异摘要。

公开上传前，确认文件不含密码、令牌、内部地址或不应公开的资料。本仓库根目录下的两份 `GitHub_Manual_Push_Guide` 原件已经由 `.gitignore` 排除，不要使用 `git add -f` 强制加入。

若 Git 提示没有作者身份，可仅为当前仓库配置自己的 GitHub 用户名和已验证邮箱，或使用 GitHub 设置中提供的隐私邮箱。无需更改其他项目的全局设置。

## 4. 推送到 GitHub

```powershell
git pull --ff-only origin main
git push origin main
```

每条命令成功后再执行下一条。推送失败时先处理错误，不要使用 `--force`。

如果另有经过确认的第二个备份仓库，需要单独配置远程并分别推送；一次编辑器“同步”操作不保证更新所有远程。本示例只配置 `origin`。

## 5. 核对同步结果

```powershell
git status
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

工作区应没有待提交修改，本地 `HEAD` 与远程 `main` 的完整提交编号应一致。工作区干净本身不代表已经上传。被忽略的文件仍保留本地，不会出现在普通 `git status` 中。

## 6. 目录所有权错误

如果 Git 提示 `detected dubious ownership`，先确认当前目录确实是你信任的本地仓库，再执行：

```powershell
$TrustedRepo = (Get-Location).Path -replace '\\', '/'
git config --global --add safe.directory $TrustedRepo
```

这只为当前已确认的目录添加例外。不要将 `safe.directory` 设置为 `*`。

## 7. 常见问题

- `non-fast-forward`：远程包含本地尚未整合的提交。先获取并检查差异，处理合并后重试。
- 同名文件冲突：保留两份内容进行比较；二进制文件通常需要人工选择或分别保存。
- 文件没有上传：检查是否已经暂存、提交和推送，以及是否匹配 `.gitignore`。
- 误提交敏感资料：`.gitignore` 不会删除已有历史；先处理已暴露的凭据，再按具体情况清理历史。

日常流程是：拉取更新 → 修改文件 → 检查并提交 → 推送 → 核对提交编号。
