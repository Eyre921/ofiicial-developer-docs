---
title: "Claude Code"
source: https://docs.fireworks.ai/ecosystem/firerouter/claude-code
path: ecosystem/firerouter/claude-code
---

Use FireRouter in Claude Code with settings.json

## Prerequisites

* [Claude Code](https://claude.ai/code) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)

## `settings.json`

Add one of these to `~/.claude/settings.json` (on Windows: `%USERPROFILE%\.claude\settings.json`).

### With a Claude subscription

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

### With an Anthropic API key

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
