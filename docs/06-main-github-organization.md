# 06 — Create a GitHub organization

<!-- print:omit -->
[Back / 返回](../README.md) · [PDF](print/06-main-github-organization.pdf) · [HTML](print/06-main-github-organization.html)
<!-- /print:omit -->

## Question and scope

> How do I create a GitHub organization for research collaboration and make sure a repository belongs to it?

An organization groups repositories and access permissions; each collaborator still uses their own personal account. This is a walkthrough, not a record that an organization has already been created. The sample name `research-lab-example` is a placeholder; choose an available name for your own group. Interface wording was checked against GitHub documentation on 2026-09-20.

## 1. Identify the three names

| Item | Example | Meaning |
| --- | --- | --- |
| Personal account | `HainanW` | The person who signs in |
| Organization account | `research-lab-example` | A shared owner for repositories |
| Repository | `research-coding-handbook` | A particular project |

A personal repository has an address like `github.com/HainanW/research-coding-handbook`. An organization-owned repository would instead use `github.com/research-lab-example/research-coding-handbook`. Creating an organization does not move your existing personal repository.

## 2. Open the creation page

Sign in to GitHub. Open your profile picture menu, choose **Settings**, then **Organizations** in the Access section. Select **New organization** and follow the setup prompts. This is the route documented in [GitHub's creation guide](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).

> **Screenshot placeholder 06-1** — Settings → Organizations → New organization.
> Suggested file: `docs/images/06-organization-entry.png`

<!-- Replace the placeholder above after saving the screenshot:
![Settings → Organizations → New organization.](images/06-organization-entry.png)
-->

## 3. Complete the setup

Prepare an available organization account name and a contact email. Read the current plan choices and select the one that meets your group's needs; record the plan you select rather than assuming a particular price or feature list. Complete any account verification and required setup fields shown by GitHub. If the flow offers member invitations, you can handle membership when ready.

> **Screenshot placeholder 06-2** — Organization setup: account name and selected plan; hide contact and billing details.
> Suggested file: `docs/images/06-organization-setup.png`

<!-- Replace the placeholder above after saving the screenshot:
![Organization setup: account name and selected plan; hide contact and billing details.](images/06-organization-setup.png)
-->

After creation, open the organization's page and check that its account name matches your intention. A newly created organization has no repositories. For your own notes, fill in:

| Field | Your record |
| --- | --- |
| Organization account name | To fill in |
| Organization URL | To fill in |
| Selected plan | To fill in |
| Creation date | To fill in |
| Intended projects | To fill in |

## 4. Choose between a new repository and an existing one

For a **new project**, use GitHub's new-repository form and choose the organization in **Owner**. Enter the repository name, description, and intended visibility. Check the resulting address after creating it. See [creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

> **Screenshot placeholder 06-3** — Repository creation form showing the organization as Owner.
> Suggested file: `docs/images/06-repository-owner.png`

<!-- Replace the placeholder above after saving the screenshot:
![Repository creation form showing the organization as Owner.](images/06-repository-owner.png)
-->

For an **existing personal project**, creation and transfer are separate actions. If the intended goal is to move `HainanW/research-coding-handbook`, first review its collaborators, destination, and any name conflict, then follow [GitHub's repository transfer guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository). Do not create a same-named empty repository in the organization if you intend to transfer the existing one there.

Only after an actual transfer, update the existing clone's remote using its real new URL:

```powershell
git remote -v
# Replace YOUR-ORG and YOUR-REPO with the actual destination.
git remote set-url origin https://github.com/YOUR-ORG/YOUR-REPO.git
git remote -v
git fetch origin
```

`git remote set-url` only changes the local connection address; it does not transfer a repository or upload any files.

## 5. Verify the result

- The organization page exists with the intended account name.
- The repository address begins with the intended organization name.
- The repository's public/private setting is the one you selected.
- The intended collaborators have access through their own accounts.
- If you moved an existing repository, the local `origin` now targets its new location.

## 6. Add screenshots later

The three visible blocks are intentional placeholders, not missing image files. They remain readable in Markdown and the PDF. Save each future screenshot under the suggested filename, replace its block with the image line stored in the adjacent HTML comment, and remove the comment markers. Both language editions can use the same image. See [02, Markdown images](02-main-markdown-images.md).

Regenerate with `python tools/export_print.py docs/06-main-github-organization.md`. The image will then be embedded into the print HTML and PDF.
