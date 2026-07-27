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
* The FireConnect CLI v0.9.0+ (see [Install](/ecosystem/fireconnect/overview#install))

<Note>
  **Azure routing not implemented yet for Claude Code.** `fireconnect claude on` always configures direct Fireworks, even when global config has `--provider azure` or you pass `--azure`. See [Microsoft Foundry in FireConnect](/ecosystem/fireconnect/microsoft-foundry#supported-harnesses).
</Note>

## Enable Fireworks routing

```bash theme={null}
fireconnect login
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

After `fireconnect claude on`, start a new Claude Code session or run `/model` to pick up model changes. To use a new model in the same session, start a new session or `/exit` and resume with `claude --resume <id>`.

## Using Fire Pass

Use your `fpk_...` key during `login` or with `--api-key`:

```bash theme={null}
fireconnect claude on --api-key fpk_...
```

FireConnect detects Fire Pass keys and routes all model aliases to `glm-fast-latest`.

## Default model mapping

| Alias    | Standard key (`fw_...`) | Fire Pass key (`fpk_...`) |
| -------- | ----------------------- | ------------------------- |
| main     | `glm-fast-latest`       | `glm-fast-latest`         |
| opus     | `glm-fast-latest`       | `glm-fast-latest`         |
| fable    | `glm-fast-latest`       | `glm-fast-latest`         |
| sonnet   | `kimi-fast-latest`      | `glm-fast-latest`         |
| haiku    | `deepseek-v4-flash`     | `glm-fast-latest`         |
| subagent | `deepseek-v4-flash`     | `glm-fast-latest`         |

Short model IDs like `glm-fast-latest` are expanded to full Fireworks paths (for example, `accounts/fireworks/routers/glm-fast-latest[1m]`). FireConnect appends the `[1m]` suffix on `main`, `opus`, and `fable` so Claude Code enables 1M context. The `subagent` slot is written without `[1m]` because Claude Code forwards that value verbatim to the provider API.

## What gets written

FireConnect writes these settings to `~/.claude/settings.json`. Claude Code authenticates via the `X-Fireworks-Api-Key` custom header (not `apiKeyHelper`). The Fireworks key is written to the file with mode `0600`:

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_MODEL": "accounts/fireworks/routers/glm-fast-latest[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "accounts/fireworks/routers/glm-fast-latest[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "accounts/fireworks/routers/kimi-fast-latest",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "accounts/fireworks/models/deepseek-v4-flash",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "accounts/fireworks/routers/glm-fast-latest[1m]",
    "CLAUDE_CODE_SUBAGENT_MODEL": "accounts/fireworks/models/deepseek-v4-flash",
    "ANTHROPIC_CUSTOM_HEADERS": "x-fireworks-api-key: YOUR_FIREWORKS_API_KEY"
  }
}
```

FireConnect saves a backup of your previous provider settings to `~/.fireconnect/claude/` so `fireconnect claude off` can restore them.

## Web search MCP

When you run `fireconnect claude on`, FireConnect can install the Fireworks [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp) for eligible accounts. FireConnect WebSearch integration is **Claude Code only today**; other harnesses are coming soon.

The MCP itself works from any harness that supports HTTP MCP. See the [WebSearch MCP guide](/ecosystem/fireconnect/websearch-mcp) for the endpoint URL, bearer token auth, and manual setup on Claude Code or other tools.

When installation succeeds, `fireconnect claude on` prints a confirmation such as `Web search → fireworks-websearch (installed)`. Restart Claude Code, then run `/mcp` and connect to `fireworks-websearch`.

`fireconnect claude off` removes the managed MCP entry and restores your previous `~/.claude/settings.json` (including any `permissions` rules).

## Browsing and picking models

Browse the global catalog, then configure Claude Code through `on`:

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --sonnet kimi-latest
fireconnect claude on --model glm-fast-latest --sonnet kimi-fast-latest
```

### `fireconnect model list`

Lists the shared Fireworks serverless catalog (coding-tagged models plus known platform routers). Every row is tagged `serverless`.

```bash theme={null}
fireconnect model list
fireconnect model list --search glm
fireconnect model list --json
```

Resolves the key from `--api-key`, the OS keychain, `~/.fireconnect/config.json`, or `FIREWORKS_API_KEY`. Fire Pass keys (`fpk_...`) show Fire Pass-supported routers only and cannot select `firerouter`. Standard keys include `firerouter`.

### `fireconnect claude status` vs `fireconnect model list`

| Command                     | Shows                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| `fireconnect claude status` | Your current provider, auth, configured alias mapping, and Fireworks serverless rates per slot |
| `fireconnect model list`    | Available serverless endpoints from the Fireworks API, with IN / OUT pricing where known       |

## FireRouter

Route requests through [FireRouter](/ecosystem/firerouter/overview), a managed service that sends simple work to cheaper open models and passes hard requests to Claude Opus 4.8. Requires a standard Fireworks API key (`fw_...`); Fire Pass keys cannot select `firerouter`.

```bash theme={null}
fireconnect claude on --model firerouter
fireconnect claude on --opus firerouter --anthropic-api-key sk-ant-...
```

Use `--model firerouter` for the primary model or alias flags like `--opus firerouter` for specific slots.

Pass `--anthropic-api-key sk-ant-...` on `on`, or store a key once with `fireconnect configure --anthropic-api-key sk-ant-...`.

Bias routing toward savings or quality with `--routing-preference` (`1`–`5`; default `3`):

```bash theme={null}
fireconnect claude on --model firerouter --routing-preference 4
```

See [Routing preferences](/ecosystem/firerouter/routing-preferences) for level names.

## Session usage

Claude Code's `/model` picker shows **Anthropic list prices**, not Fireworks serverless rates. For actual spend, use `fireconnect claude usage`. It reads Claude Code session logs and estimates Fireworks cost from your configured models.

```bash theme={null}
fireconnect claude usage                    # latest session
fireconnect claude usage --last-n 5         # five most recent parent sessions
fireconnect claude usage --session <id>     # session id prefix or path to a .jsonl log
fireconnect claude usage --plain            # plain-text summary (scripts)
fireconnect claude usage --verbose          # per-request token rows
fireconnect claude usage --json             # machine-readable output
```

Pair with `fireconnect claude status` for per-slot Fireworks rates and `fireconnect model list` to browse serverless pricing.

## Claude Code pricing estimates

Claude Code's cost column in the `/model` picker still uses Anthropic list prices. The [session usage](#session-usage) section above is the better place to estimate real Fireworks spend.

FireConnect cannot override Claude Code's price column. For example, the default `glm-fast-latest` mapping may show Opus-tier estimates around **$5 / $25 per Mtok** while Fireworks bills at model-specific serverless rates (often much lower). Check the [billing dashboard](https://app.fireworks.ai/account/billing) for actual spend.

FireConnect also writes `ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION` with Fireworks rates for your **main** model. That text appears as the subtitle on the custom picker entry at the bottom of `/model`, not in the price column.

## CLI reference

```bash theme={null}
fireconnect claude on         # Route Claude Code through Fireworks
fireconnect claude off        # Restore your previous provider
fireconnect claude status     # Show the current provider and model mapping
fireconnect claude usage      # Session token usage and estimated Fireworks cost
fireconnect claude help       # Show harness-specific help
```

Run `fireconnect claude help` for all options, including `--settings-path` (custom `settings.json` location) and `--routing-preference` when using FireRouter.

### Switch models

```bash theme={null}
fireconnect claude on --model glm-fast-latest --sonnet kimi-fast-latest --haiku deepseek-v4-flash --subagent deepseek-v4-flash
fireconnect claude on --model firerouter   # route through FireRouter
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
