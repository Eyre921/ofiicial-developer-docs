---
title: "CLI Authentication"
source: https://developers.deepgram.com/developer-tools/cli/authentication.md
path: developer-tools/cli/authentication
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# CLI Authentication

## Interactive Login

The simplest way to authenticate:

```shell
dg login
```

This opens your browser to the Deepgram Console where you can authorize the CLI. Once authorized, your API key is stored securely in `~/.config/deepgram/credentials`.

## API Key Flag

For CI/CD environments or scripted usage, pass your API key directly:

```shell
dg --api-key YOUR_API_KEY listen audio.mp3
```

## Environment Variable

Set your API key as an environment variable:

```shell
export DEEPGRAM_API_KEY=YOUR_API_KEY
dg listen audio.mp3
```

## Named Profiles

Use multiple API keys with named profiles:

```shell
dg login --profile production
dg login --profile development

# Use a specific profile
dg --profile production listen audio.mp3
```

Profiles store credentials in `~/.config/deepgram/profiles/<name>/credentials`.

## Check Auth Status

```shell
dg whoami
```

Output:

```
Logged in as: you@company.com
API Key: sk_live_...1234
Source: ~/.config/deepgram/credentials
```

## CI/CD Usage

For CI/CD pipelines, use the `--api-key` flag or environment variable:

```yaml
# Example GitHub Actions
- name: Transcribe audio
  env:
    DEEPGRAM_API_KEY: ${{ secrets.DEEPGRAM_API_KEY }}
  run: dg listen audio.mp3 -o json > transcript.json
```
