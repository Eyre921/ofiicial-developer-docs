---
title: "Claude Code (manual setup)"
source: https://docs.fireworks.ai/ecosystem/firerouter/claude-code
path: ecosystem/firerouter/claude-code
---

Configure FireRouter in Claude Code by editing settings.json

<Tip>
  **Prefer FireConnect.** Use `--model firerouter` for Main, a slot flag such as `--opus firerouter` for one alias, or `--interactive` to choose aliases. See [Claude Code — FireRouter](/ecosystem/fireconnect/claude-code#choose-where-firerouter-is-used).
</Tip>

This page is only for manual `~/.claude/settings.json` setup when you cannot use FireConnect.

## Prerequisites

* [Claude Code](https://claude.ai/code) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* Optional Anthropic credentials to make Claude Opus 5 eligible — usually your existing Claude Code login (subscription, OAuth, or API key). Without them, FireRouter can still use eligible Fireworks-hosted models. See [Authentication](/ecosystem/firerouter/authentication#claude-code-with-fireconnect).

Merge the `env` keys from one configuration below into your existing `~/.claude/settings.json` (on Windows: `%USERPROFILE%\.claude\settings.json`). Do not replace unrelated settings. Then restart Claude Code.

## With a Claude subscription

You do not need to add an Anthropic token to this file. Use `ANTHROPIC_CUSTOM_HEADERS` to pass your Fireworks API key. Claude Code sends your existing login with each request.

**Route Main through FireRouter without adding or changing other alias pins.** All Claude Code requests still use the Fireworks base URL:

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_MODEL": "firerouter[1m]",
    "ANTHROPIC_CUSTOM_HEADERS": "x-fireworks-api-key: YOUR_FIREWORKS_API_KEY"
  }
}
```

**Route the Opus alias through FireRouter.** Select Opus from `/model`; this does not add or change other alias pins, and all requests still use the Fireworks base URL:

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "firerouter[1m]",
    "ANTHROPIC_CUSTOM_HEADERS": "x-fireworks-api-key: YOUR_FIREWORKS_API_KEY"
  }
}
```

## With an Anthropic API key

Add `ANTHROPIC_API_KEY` to make Claude Opus 5 eligible. You still need `ANTHROPIC_CUSTOM_HEADERS` for your Fireworks API key. This example routes Main through FireRouter without adding or changing other alias pins:

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_MODEL": "firerouter[1m]",
    "ANTHROPIC_CUSTOM_HEADERS": "x-fireworks-api-key: YOUR_FIREWORKS_API_KEY",
    "ANTHROPIC_API_KEY": "YOUR_ANTHROPIC_API_KEY"
  }
}
```
