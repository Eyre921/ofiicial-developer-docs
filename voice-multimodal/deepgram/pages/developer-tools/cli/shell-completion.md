---
title: "Shell Completion"
source: https://developers.deepgram.com/developer-tools/cli/shell-completion.md
path: developer-tools/cli/shell-completion
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Shell Completion

## Install Completion

```shell
dg completion bash --install
dg completion zsh --install
dg completion fish --install
```

The command appends the appropriate completion setup to your shell profile. Restart your shell or source that profile after installation.

## Current Shell Session

To enable Bash completion only for the current session:

```shell
eval "$(_DG_COMPLETE=bash_source dg)"
```

For zsh or fish, use the `--install` command above.

## What Gets Completed

* Commands: `dg listen`, `dg speak`, `dg read`, etc.
* Options: command options such as `--mic` and `--model`, and root options such as `-o`
* File paths after `dg listen`

The installed setup evaluates completion support from the current `dg` command, so it automatically reflects a CLI update.
