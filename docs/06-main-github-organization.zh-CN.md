# 06 — Create a GitHub organization / 06 — 创建 GitHub 组织（Organization）

<!-- bilingual: en-zh -->

<!-- print:omit -->
[返回手册 / Handbook](../README.zh-CN.md) · [English](06-main-github-organization.md)

[英中双语 PDF / Bilingual PDF](print/06-main-github-organization.zh-CN.pdf) · [打印 HTML / Print HTML](print/06-main-github-organization.zh-CN.html)
<!-- /print:omit -->

## Question and scope / 问题与范围（Question and scope）

> How do I create a GitHub organization for research collaboration and make sure a repository belongs to it?
>
> 如何创建 GitHub 组织（Organization）用于科研协作，并确认仓库确实属于该组织？

An organization groups repositories and access permissions; each collaborator still uses their own personal account. This is a walkthrough, not a record that an organization has already been created. The sample name `research-lab-example` is a placeholder; choose an available name for your own group. Interface wording was checked against GitHub documentation on 2026-09-20.

组织用于集中管理仓库与访问权限（access permissions）；每位合作者仍使用自己的个人账号。本篇是操作指南，不表示已经创建了组织。示例名 `research-lab-example` 只是占位名称，实际操作需选择可用名称。界面步骤依据 2026-09-20 查阅的官方文档。

## 1. Identify the three names / 1. 区分三个名称（Names）

| Item<br>项目（item） | Example<br>示例（example） | Meaning<br>含义（meaning） |
| --- | --- | --- |
| Personal account<br>个人账号（personal account） | `HainanW` | The person who signs in<br>登录 GitHub 的个人 |
| Organization account<br>组织账号（organization account） | `research-lab-example` | A shared owner for repositories<br>集中拥有和管理仓库 |
| Repository<br>仓库（repository） | `research-coding-handbook` | A particular project<br>某个具体项目 |

A personal repository has an address like `github.com/HainanW/research-coding-handbook`. An organization-owned repository would instead use `github.com/research-lab-example/research-coding-handbook`. Creating an organization does not move your existing personal repository.

个人仓库地址例如 `github.com/HainanW/research-coding-handbook`；组织仓库则可能是 `github.com/research-lab-example/research-coding-handbook`。创建组织不会自动迁移已有的个人仓库。

## 2. Open the creation page / 2. 找到创建入口（Creation entry）

Sign in to GitHub. Open your profile picture menu, choose **Settings**, then **Organizations** in the Access section. Select **New organization** and follow the setup prompts. This is the route documented in [GitHub's creation guide](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).

登录 GitHub，点击右上角头像 → **Settings（设置）** → Access 区域的 **Organizations（组织）** → **New organization（新建组织）**，再按页面提示继续。该入口来自 [GitHub 创建组织指南](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)。

> **Screenshot placeholder 06-1** — Settings → Organizations → New organization.
> Suggested file: `docs/images/06-organization-entry.png`
>
> **插图占位（Screenshot placeholder） 06-1** — 设置（Settings）→ 组织（Organizations）→ 新建组织（New organization）的入口。
> 建议文件：`docs/images/06-organization-entry.png`

<!-- Replace the placeholder above after saving the screenshot:
![设置（Settings）→ 组织（Organizations）→ 新建组织（New organization）的入口。](images/06-organization-entry.png)
-->

## 3. Complete the setup / 3. 填写创建信息（Setup）

Prepare an available organization account name and a contact email. Read the current plan choices and select the one that meets your group's needs; record the plan you select rather than assuming a particular price or feature list. Complete any account verification and required setup fields shown by GitHub. If the flow offers member invitations, you can handle membership when ready.

准备可用的组织账号名（account name）和联系邮箱（contact email）。查看当前方案（plan），选择适合团队需求的方案，并记录实际选择；不要假设价格或功能永久不变。按页面要求完成验证及必填项目。如流程提供成员邀请（member invitations），可在准备好成员安排后处理。

> **Screenshot placeholder 06-2** — Organization setup: account name and selected plan; hide contact and billing details.
> Suggested file: `docs/images/06-organization-setup.png`
>
> **插图占位（Screenshot placeholder） 06-2** — 组织创建页面：组织账号名及所选方案；隐藏联系邮箱和账单信息。
> 建议文件：`docs/images/06-organization-setup.png`

<!-- Replace the placeholder above after saving the screenshot:
![组织创建页面：组织账号名及所选方案；隐藏联系邮箱和账单信息。](images/06-organization-setup.png)
-->

After creation, open the organization's page and check that its account name matches your intention. A newly created organization has no repositories. For your own notes, fill in:

创建后打开组织页面，检查账号名是否正确。新组织起初没有仓库。可以在自己的记录中填写：

| Field<br>字段（field） | Your record<br>记录（record） |
| --- | --- |
| Organization account name<br>组织账号名 | To fill in<br>待填写 |
| Organization URL<br>组织网址（URL） | To fill in<br>待填写 |
| Selected plan<br>所选方案（plan） | To fill in<br>待填写 |
| Creation date<br>创建日期 | To fill in<br>待填写 |
| Intended projects<br>计划管理的项目 | To fill in<br>待填写 |

## 4. Choose between a new repository and an existing one / 4. 新仓库与已有仓库（New versus existing repository）

For a **new project**, use GitHub's new-repository form and choose the organization in **Owner**. Enter the repository name, description, and intended visibility. Check the resulting address after creating it. See [creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

对于**新项目**，进入 GitHub 新建仓库页面，在 **Owner（所属者）** 中选择组织，再填写仓库名、说明和可见性（visibility）。创建后核对地址。参见[创建仓库官方指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。

> **Screenshot placeholder 06-3** — Repository creation form showing the organization as Owner.
> Suggested file: `docs/images/06-repository-owner.png`
>
> **插图占位（Screenshot placeholder） 06-3** — 新建仓库页面，突出显示所属者（Owner）已选为组织。
> 建议文件：`docs/images/06-repository-owner.png`

<!-- Replace the placeholder above after saving the screenshot:
![新建仓库页面，突出显示所属者（Owner）已选为组织。](images/06-repository-owner.png)
-->

For an **existing personal project**, creation and transfer are separate actions. If the intended goal is to move `HainanW/research-coding-handbook`, first review its collaborators, destination, and any name conflict, then follow [GitHub's repository transfer guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository). Do not create a same-named empty repository in the organization if you intend to transfer the existing one there.

对于**已有个人项目**，创建组织与迁移仓库（transfer）是两件事。如果目标是迁移 `HainanW/research-coding-handbook`，应先核对协作者、目标组织及名称冲突，再按[仓库迁移指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)操作。打算迁移已有仓库时，不要先在组织里创建同名空仓库。

Only after an actual transfer, update the existing clone's remote using its real new URL:

只有完成实际迁移后，才将本地副本的远程地址（remote URL）改为真实的新地址：

```powershell
git remote -v
# Replace YOUR-ORG and YOUR-REPO with the actual destination.
git remote set-url origin https://github.com/YOUR-ORG/YOUR-REPO.git
git remote -v
git fetch origin
```

`git remote set-url` only changes the local connection address; it does not transfer a repository or upload any files.

将 `YOUR-ORG` 和 `YOUR-REPO` 替换为真实名称。`git remote set-url` 仅修改本地连接地址，本身不会迁移仓库或上传文件。

## 5. Verify the result / 5. 核对结果（Verification）

- The organization page exists with the intended account name.

  组织页面存在，账号名符合预期。

- The repository address begins with the intended organization name.

  仓库地址以目标组织名开头。

- The repository's public/private setting is the one you selected.

  仓库可见性（public/private）符合选择。

- The intended collaborators have access through their own accounts.

  预期合作者通过各自账号拥有访问权限。

- If you moved an existing repository, the local `origin` now targets its new location.

  若迁移了已有仓库，本地 `origin` 已指向新位置。

## 6. Add screenshots later / 6. 后续添加插图（Screenshots）

The three visible blocks are intentional placeholders, not missing image files. They remain readable in Markdown and the PDF. Save each future screenshot under the suggested filename, replace its block with the image line stored in the adjacent HTML comment, and remove the comment markers. Both language editions can use the same image. See [02, Markdown images](02-main-markdown-images.md).

三个可见区块是明确的插图占位，不是失效图片。Markdown 和 PDF 都能正常阅读。以后将截图保存到建议文件名，用相邻 HTML 注释（comment）中的图片语句替换占位区块，并去掉注释标记。双语版本可以共用图片。参见 [02：Markdown 插图](02-main-markdown-images.zh-CN.md)。

Regenerate with `python tools/export_print.py docs/06-main-github-organization.md`. The image will then be embedded into the print HTML and PDF.

运行 `python tools/export_print.py docs/06-main-github-organization.zh-CN.md`，即可将图片嵌入新的打印 HTML 和 PDF。
