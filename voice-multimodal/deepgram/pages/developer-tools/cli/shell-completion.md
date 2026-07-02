---
title: "Shell Completion"
source: https://developers.deepgram.com/developer-tools/cli/shell-completion.md
path: developer-tools/cli/shell-completion
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Shell Completion

## Generate Completion Script

```shell
dg completion bash > dg-completion.bash
dg completion zsh > dg-completion.zsh
dg completion fish > dg-completion.fish
```

## bash

Add to your `~/.bashrc`:

```shell
source ~/dg-completion.bash
```

Or copy to the completion directory:

```shell
sudo cp dg-completion.bash //bash_completion.d/
```

## zsh

Add to your `~/.zshrc`:

```shell
source ~/dg-completion.zsh
```

Or copy to the completion directory:

```shell
mkdir -p ~/.zsh/completions
cp dg-completion.zsh ~/.zsh/completions/_dg
```

Make sure completions are enabled:

```shell
autoload -Uz compinit
compinit
```

## fish

Add to your `~/.config/fish/config.fish`:

```shell
source ~/dg-completion.fish
```

## Verify Installation

```shell
dg completion --verify
```

## What Gets Completed

* Commands: `dg listen`, `dg speak`, `dg read`, etc.
* Subcommands: `--mic`, `--model`, `-o json`, etc.
* File paths after `dg listen`
* Project IDs and key names

## Refresh Completions

After updating the CLI, regenerate completions:

```shell
dg completion bash > dg-completion.bash
```
