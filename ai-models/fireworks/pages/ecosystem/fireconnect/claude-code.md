---
title: "Claude Code"
source: https://docs.fireworks.ai/ecosystem/fireconnect/claude-code
path: ecosystem/fireconnect/claude-code
---

Use Fireworks AI models in Claude Code with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [Claude Code](https://claude.ai/code) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

## Prerequisites

* [Claude Code](https://claude.ai/code) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* The FireConnect CLI (see [Install](/ecosystem/fireconnect/overview#install))

## Enable Fireworks routing

```bash theme={null}
export FIREWORKS_API_KEY=fw_...
fireconnect claude on
```

Or pass the key once:

```bash theme={null}
fireconnect claude on --api-key fw_...
```

Restart Claude Code after enabling, then test with:

```text theme={null}
hi
```

After `fireconnect claude on`, `model select`, or `model reset`, settings are updated immediately. To use a new model in the same session, run `/model` in Claude Code, start a new session, or `/exit` and resume with `claude --resume <id>`.

## Using Fire Pass

Use your `fpk_...` key instead of a standard `fw_...` key:

```bash theme={null}
fireconnect claude on --api-key fpk_...
```

FireConnect detects Fire Pass keys and routes all model aliases to `glm-latest`.

## Default model mapping

| Alias    | Standard key (`fw_...`) | Fire Pass key (`fpk_...`) |
| -------- | ----------------------- | ------------------------- |
| main     | `glm-latest`            | `glm-latest`              |
| opus     | `glm-latest`            | `glm-latest`              |
| sonnet   | `glm-5p1`               | `glm-latest`              |
| haiku    | `deepseek-v4-flash`     | `glm-latest`              |
| subagent | `deepseek-v4-flash`     | `glm-latest`              |

Short model IDs like `glm-latest` are expanded to full Fireworks paths (for example, `accounts/fireworks/routers/glm-latest[1m]`). FireConnect appends the `[1m]` suffix on `main` and `opus` so Claude Code enables 1M context. The `subagent` slot is written without `[1m]` because Claude Code forwards that value verbatim to the provider API.

## What gets written

FireConnect writes these settings to `~/.claude/settings.json`:

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_API_KEY": "fw_YOUR_FIREWORKS_API_KEY",
    "ANTHROPIC_AUTH_TOKEN": "fw_YOUR_FIREWORKS_API_KEY",
    "ANTHROPIC_MODEL": "accounts/fireworks/routers/glm-latest[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "accounts/fireworks/routers/glm-latest[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "accounts/fireworks/models/glm-5p1",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "accounts/fireworks/models/deepseek-v4-flash",
    "CLAUDE_CODE_SUBAGENT_MODEL": "accounts/fireworks/models/deepseek-v4-flash"
  }
}
```

FireConnect writes both `ANTHROPIC_API_KEY` (preferred) and `ANTHROPIC_AUTH_TOKEN` (compatibility alias) with the same Fireworks key. It saves a backup of your previous provider settings to `~/.fireconnect/claude/` so `fireconnect claude off` can restore them.

## Browsing and picking models

```bash theme={null}
fireconnect claude model list              # browse callable serverless endpoints
fireconnect claude model select            # pick a model for Claude Code
fireconnect claude model select --slot sonnet   # update one alias
```

### `fireconnect claude model list`

Lists serverless models from the Fireworks API (`supports_serverless=true`) and merges known public platform aliases (`glm-latest`, `kimi-fast-latest`, `kimi-latest`, `kimi-k2p6-turbo`, and `kimi-k2p7-code-fast`). Every row is tagged `serverless`.

```bash theme={null}
fireconnect claude model list
fireconnect claude model list --search glm
fireconnect claude model list --json
```

Resolves the key from `--api-key`, harness settings, `~/.fireconnect/config.json`, or `FIREWORKS_API_KEY`. Fire Pass keys (`fpk_...`) show Fire Pass-supported models only.

### `fireconnect claude model select`

Interactive picker. Requires a terminal and Fireworks to be enabled.

```bash theme={null}
fireconnect claude model select
fireconnect claude model select --slot sonnet
fireconnect claude model select --slot sonnet --search glm
```

### `fireconnect claude status` vs `fireconnect claude model list`

| Command                         | Shows                                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------- |
| `fireconnect claude status`     | Your current provider, auth, configured alias mapping, and Fireworks serverless rates per slot |
| `fireconnect claude model list` | Available serverless endpoints from the Fireworks API, with IN / OUT pricing where known       |

## Claude Code pricing estimates

Claude Code's `/model` picker and session cost estimates use **Anthropic list prices**, not Fireworks serverless rates. For example, the default `glm-latest` mapping may show Opus-tier estimates around **$5 / $25 per Mtok** while Fireworks bills at model-specific serverless rates (often much lower).

FireConnect cannot override Claude Code's price column. Use `fireconnect claude status` and `fireconnect claude model list` for Fireworks rates, and check the [billing dashboard](https://app.fireworks.ai/account/billing) for actual spend.

## CLI reference

```bash theme={null}
fireconnect claude on         # Route Claude Code through Fireworks
fireconnect claude off        # Restore your previous provider
fireconnect claude status     # Show the current provider and model mapping
fireconnect claude model list # Browse serverless models
fireconnect claude model select   # Pick a model interactively
fireconnect claude model reset    # Reset model aliases to defaults
fireconnect claude help       # Show harness-specific help
```

Run `fireconnect claude help` for all options.

### Switch models

```bash theme={null}
fireconnect claude on --main glm-latest --sonnet glm-5p1 --haiku deepseek-v4-flash --subagent deepseek-v4-flash
```

Or pick interactively:

```bash theme={null}
fireconnect claude model select --slot opus
```

### Turn off Fireworks routing

```bash theme={null}
fireconnect claude off
```

This restores your previous `~/.claude/settings.json` from the backup saved in `~/.fireconnect/claude/`.

## Uninstall

To remove FireConnect from your machine entirely (all harnesses):

```bash theme={null}
fireconnect uninstall
```

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
