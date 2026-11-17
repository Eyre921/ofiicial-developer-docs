---
title: "Skills"
source: https://developers.deepgram.com/developer-tools/cli/skills.md
path: developer-tools/cli/skills
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Skills

`dg skills` installs the Deepgram skills as folders in each AI coding tool's skills folder, so the tool can load Deepgram reference material on demand. It writes and deletes folders in your home directory; this page lists what it touches.

## Commands

```shell
# Show detected AI tools and skill installation status
dg skills status
# Interactive setup: detect tools and choose where to install
dg skills setup
# Install for every detected tool without prompting
dg skills install --all
# Install for one tool only
dg skills install --cli claude
# Replace the folders the CLI installed with the current bundle
dg skills update
# Show installed skill folders and their source
dg skills list
# Remove every folder the CLI installed
dg skills remove --all
# Remove the folders for one tool
dg skills remove --cli cursor
```

`setup`, `install`, and `update` accept `--ref` to install another git ref of `deepgram/skills`; `setup --all` installs for every detected tool without prompting.

## Skills folder per tool

| `--cli` key | Tool         | Skills folder               |
| ----------- | ------------ | --------------------------- |
| `claude`    | Claude Code  | `~/.claude/skills`          |
| `codex`     | OpenAI Codex | `~/.agents/skills`          |
| `gemini`    | Gemini CLI   | `~/.gemini/skills`          |
| `cursor`    | Cursor       | `~/.cursor/skills`          |
| `opencode`  | OpenCode     | `~/.config/opencode/skills` |
| `cline`     | Cline        | `~/.cline/skills`           |

Amazon Q Developer and Aider have no skills folder; the CLI prints where to get the skills.

## Pinned bundle

By default, the CLI installs `deepgram-skills-v1.8.0`, pinned by commit and checked against the tarball's SHA-256. To install another ref, pass `--ref` or set `DEEPCTL_SKILLS_REF`.

## Which folders the CLI changes

The CLI replaces or deletes a skill folder only when all of these hold:

* `~/.deepctl/skills/skills.json` records the folder for that tool.
* It is a real folder directly in the tool's skills folder.
* It holds the `.deepctl-skill` marker.
* Its contents still match what the CLI installed.

As a result:

* Folders from `npx skills add` and symlinked skill folders are left alone.
* An edit freezes a folder: `update` stops without changing anything and `remove` leaves it in place. Opening a folder in Finder or Explorer can add `.DS_Store`, `Thumbs.db`, or `desktop.ini`, which counts as an edit.
* To get updates again, rename or move the edited copy, or delete it yourself.

## Other commands that install skills

`dg login` offers to install the skills, and `dg plugin install`, `update`, and `remove` refresh the installed ones. A skills failure prints a warning on stderr and leaves the command's exit code unchanged.

## Concurrent runs

While another `dg skills`, `dg login`, or `dg plugin` command is changing skills, the next one waits up to 30 seconds. If the first is still running after 30 seconds, the second stops, changes nothing, and says to run the command again.

On a filesystem that cannot provide locking or no-replace directory moves, these commands abort. Installed skill folders and `skills.json` stay as they were, though the tool's skills folder and `~/.deepctl/skills/skills.json.lock` may already exist.

## Upgrading from 0.2.16 through 0.3.x

On macOS and Linux, once the CLI has installed a tool's skill folders, it removes the files earlier releases wrote for that tool and prints which ones on stderr:

* `~/.claude/commands/deepgram/*.md`, `~/.cursor/rules/deepctl.mdc`, and `~/.cline/rules/deepctl.md`
* In `~/.codex/instructions.md`, `~/.gemini/GEMINI.md`, and `~/.opencode/agents.md`, the section between the `<!-- BEGIN deepctl CLI Reference` and `<!-- END deepctl CLI Reference -->` lines, including anything you changed inside it. The rest of each file is kept.

The CLI keeps each original file next to it as `.deepctl-kept-v03-*`. It removes a file only when its content exactly matches a `deepgram/skills` version an earlier release copied; it keeps a file you edited, a link, and a file reached through a link. On Windows, the CLI leaves this content untouched; remove it yourself if you do not need it.

## First-run hint

When the CLI detects an AI coding tool and no skills are installed, it prints a one-time hint on stderr. The hint is suppressed in CI and when the CLI runs through `uvx` or `pipx run`.

## Install without the CLI

`npx skills add deepgram/skills` installs the same skills without `dg`, and [Agentic Developer Tools](/developer-tools/agentic-tools) covers the Claude Code plugin marketplace route.
