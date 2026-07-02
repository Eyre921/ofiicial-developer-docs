---
title: "CLI Installation"
source: https://developers.deepgram.com/developer-tools/cli/installation.md
path: developer-tools/cli/installation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# CLI Installation

## macOS and Linux

The fastest way to install on macOS and Linux:

```shell
curl -fsSL deepgram.com/install.sh | sh
```

This script detects your OS, checks for Python 3.10+, and installs the `dg` command to your PATH.

## Windows

In PowerShell:

```powershell
iwr deepgram.com/install.ps1 -useb | iex
```

## Package Managers

### Homebrew

On macOS and Linux:

```shell
brew tap deepgram/tap
brew install deepgram
```

The first command adds Deepgram's official tap (`deepgram/homebrew-tap`); the second installs the CLI from it. After tapping, future installs and upgrades don't need the `deepgram/tap/` prefix — `brew upgrade deepgram` is enough.

Homebrew brings in `ffmpeg` and `portaudio` automatically, so `dg listen --mic`, `dg debug probe`, and the raw audio piping flows work out of the box without any further setup.

### pip

```shell
pip install deepctl
```

### pipx

```shell
pipx install deepctl
```

### uv

```shell
uv tool install deepctl
```

## Verify Installation

```shell
dg --version
dg --help
```

## Update

If you installed via Homebrew:

```shell
brew upgrade deepgram
```

Otherwise, re-run the install script:

```shell
curl -fsSL deepgram.com/install.sh | sh
```

Or update via pip:

```shell
pip install --upgrade deepctl
```

## Uninstall

```shell
brew uninstall deepgram   # Homebrew
pip uninstall deepctl     # pip
uv tool uninstall deepctl # uv
```

## Requirements

* Python 3.10 or later
* `ffmpeg` (for audio processing — installed automatically when using Homebrew)
