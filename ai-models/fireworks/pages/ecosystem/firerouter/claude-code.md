---
title: "Claude Code (manual setup)"
source: https://docs.fireworks.ai/ecosystem/firerouter/claude-code
path: ecosystem/firerouter/claude-code
---

Configure FireRouter in Claude Code by editing settings.json

<Tip>
  **Prefer FireConnect.** Run `fireconnect claude on --model firerouter` (v0.9.0+) instead of editing JSON by hand. See [Claude Code](/ecosystem/fireconnect/claude-code#firerouter) and [Models](/ecosystem/fireconnect/models).
</Tip>

This page is only for manual `~/.claude/settings.json` setup when you cannot use FireConnect.

## Prerequisites

* [Claude Code](https://claude.ai/code) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* An Anthropic API key if you need pass-through to Claude Opus 4.8. See [Authentication](/ecosystem/firerouter/authentication).

Add one of the configs below to `~/.claude/settings.json` (on Windows: `%USERPROFILE%\.claude\settings.json`), then restart Claude Code.

## With a Claude subscription

You do not need to pass any access or API token. Use `ANTHROPIC_CUSTOM_HEADERS` to pass your Fireworks API key.

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_MODEL": "firerouter[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "firerouter[1m]",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "glm-fast-latest[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-latest",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
    "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
    "ANTHROPIC_CUSTOM_HEADERS": "x-fireworks-api-key: YOUR_FIREWORKS_API_KEY"
  }
}
```

## With an Anthropic API key

Add `ANTHROPIC_API_KEY` for pass-through. You still need `ANTHROPIC_CUSTOM_HEADERS` for your Fireworks API key.

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_MODEL": "firerouter[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "firerouter[1m]",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "glm-fast-latest[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-latest",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
    "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
    "ANTHROPIC_CUSTOM_HEADERS": "x-fireworks-api-key: YOUR_FIREWORKS_API_KEY",
    "ANTHROPIC_API_KEY": "YOUR_ANTHROPIC_API_KEY"
  }
}
```
