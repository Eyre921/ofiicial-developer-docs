---
title: "Shell completion"
source: https://developers.deepgram.com/developer-tools/cli/shell-completion.md
path: developer-tools/cli/shell-completion
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Shell completion

> Deepgram CLI shell completion: install tab completion for bash, zsh, and fish with dg completion --install, or enable it for the current shell session only.

## Install completion

```shell
dg completion bash --install
dg completion zsh --install
dg completion fish --install
```

The command appends completion setup to your shell profile. Restart your shell or source the profile afterwards.

`dg completion` with no shell argument detects the shell from `$SHELL`. Without `--install`, `dg completion bash` (or `zsh`, or `fish`) prints the setup line and installs nothing.

## Current shell session

To enable Bash completion only for the current session:

```shell
eval "$(_DG_COMPLETE=bash_source dg)"
```

For zsh:

```shell
eval "$(_DG_COMPLETE=zsh_source dg)"
```

For fish:

```shell
eval (env _DG_COMPLETE=fish_source dg)
```

## What gets completed

* Commands: `dg listen`, `dg speak`, `dg read`, etc.
* Options: command options such as `--mic` and `--model`, and root options such as `-o`
* Values for choice options, such as `json`, `yaml`, `table`, and `csv` after `-o`

The installed setup reads completions from the current `dg` command, so a CLI update is reflected automatically.
