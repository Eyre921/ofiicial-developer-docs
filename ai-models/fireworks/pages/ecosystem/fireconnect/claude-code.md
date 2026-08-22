---
title: "Claude Code"
source: https://docs.fireworks.ai/ecosystem/fireconnect/claude-code
path: ecosystem/fireconnect/claude-code
---

Use Fireworks AI models in Claude Code with the FireConnect CLI

[FireConnect](https://github.com/fw-ai/fireconnect) routes [Claude Code](https://claude.ai/code) through Fireworks AI models. See the [FireConnect overview](/ecosystem/fireconnect/overview) for install and CLI basics.

<Tip>
  **Change models:** `fireconnect claude on --model <id>` (or `--opus` / `--sonnet` / …). See [Models](/ecosystem/fireconnect/models).
</Tip>

## Prerequisites

* [Claude Code](https://claude.ai/code) installed
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`) or a [Fire Pass](/firepass) key (`fpk_...`)
* The FireConnect CLI v0.9.3+ (see [Install](/ecosystem/fireconnect/overview#install))

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

## Change models

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --model firerouter               # main only
fireconnect claude on --interactive                    # model mapping wizard
fireconnect claude on --opus glm-fast-latest --sonnet glm-fast-latest
fireconnect claude status
```

Slot flags are independent. Re-running `on` without flags keeps your current mapping.

## Using Fire Pass

Use your `fpk_...` key during `login` or with `--api-key`:

```bash theme={null}
fireconnect claude on --api-key fpk_...
```

FireConnect detects Fire Pass keys and routes all model aliases to `kimi-fast-latest`.

## Example model mapping

When you run `fireconnect claude on` without model flags, FireConnect applies the mapping below. First-time setup opens an interactive model picker unless you pass `--non-interactive`. Override any slot with `--model`, `--opus`, `--sonnet`, `--haiku`, `--fable`, or `--subagent`.

| Alias    | Standard key (`fw_...`)                                                                        | Fire Pass key (`fpk_...`) |
| -------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| main     | Claude default (unpinned)                                                                      | `kimi-fast-latest`        |
| opus     | `firerouter` on first connect; otherwise `deepseek-pro-latest` when FireRouter is not selected | `kimi-fast-latest`        |
| sonnet   | Claude default (unpinned)                                                                      | `kimi-fast-latest`        |
| haiku    | `deepseek-flash-latest`                                                                        | `kimi-fast-latest`        |
| fable    | `kimi-fast-latest`                                                                             | `kimi-fast-latest`        |
| subagent | `deepseek-flash-latest`                                                                        | `kimi-fast-latest`        |

Short model IDs expand automatically. Claude Code adds `[1m]` on 1M-context models (not `subagent`).

FireConnect saves your chosen mapping per key type. Reopen the wizard anytime:

```bash theme={null}
fireconnect claude on --interactive
```

Use `--non-interactive` to skip the wizard and apply saved preferences or defaults. `--interactive` cannot be combined with model flags like `--model` or `--opus`.

In the wizard, toggle between **fast models** (routers on the high-speed path) and **non-fast models** (pinned model IDs that stay stable across catalog updates).

## What gets written

FireConnect writes these settings to `~/.claude/settings.json`. Claude Code authenticates via the `X-Fireworks-Api-Key` custom header (not `apiKeyHelper`). The Fireworks key is written to the file with mode `0600`. On a first connect with a standard key, main and Sonnet are unpinned and Opus uses FireRouter:

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "firerouter[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-flash-latest[1m]",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "kimi-fast-latest[1m]",
    "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-flash-latest",
    "ANTHROPIC_CUSTOM_HEADERS": "X-Fireworks-Api-Key: YOUR_FIREWORKS_API_KEY"
  }
}
```

FireRouter is eligible for any standard Fireworks key; provider pass-through depends on the credentials available to FireRouter. Explicit slot flags always win. FireConnect v0.9.3+ also migrates an old `deepseek-v4-flash` Claude default to `deepseek-flash-latest` the next time you run `fireconnect claude on`.

FireConnect saves a backup of your previous provider settings to `~/.fireconnect/claude/` so `fireconnect claude off` can restore them.

## Web search MCP

When you run `fireconnect claude on`, FireConnect can install the Fireworks [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp) for eligible accounts. FireConnect WebSearch integration is **Claude Code only today**; other harnesses are coming soon.

The MCP itself works from any harness that supports HTTP MCP. See the [WebSearch MCP guide](/ecosystem/fireconnect/websearch-mcp) for the endpoint URL, bearer token auth, and manual setup on Claude Code or other tools.

When installation succeeds, `fireconnect claude on` prints a confirmation such as `Web search → fireworks-websearch (installed)`. Restart Claude Code, then run `/mcp` and connect to `fireworks-websearch`.

`fireconnect claude off` removes the managed MCP entry and restores your previous `~/.claude/settings.json` (including any `permissions` rules).

## Browsing and picking models

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --sonnet kimi-latest
```

`fireconnect model list` shows serverless endpoints and pricing. `fireconnect claude status` shows your current mapping and rates.

Fire Pass keys only list Fire Pass routers. FireConnect rejects `--model firerouter` with Fire Pass (`fpk_...`) on every harness; use an `fw_...` key.

## FireRouter

Route requests through [FireRouter](/ecosystem/firerouter/overview). FireConnect rejects `--model firerouter` with Fire Pass (`fpk_...`) on every harness; use an `fw_...` key.

```bash theme={null}
fireconnect claude on --model firerouter
fireconnect claude on --opus firerouter --anthropic-api-key sk-ant-...
```

Use `--model firerouter` for main, or slot flags like `--opus firerouter`. Pass `--anthropic-api-key sk-ant-...` on `on`, or store it once with `fireconnect configure --anthropic-api-key sk-ant-...`.

Bias savings vs quality with `--routing-preference` (`1`-`5`; default `3`):

```bash theme={null}
fireconnect claude on --model firerouter --routing-preference 4
```

See [Routing preferences](/ecosystem/firerouter/routing-preferences).

## Usage and live meter

Claude Code's `/model` picker shows Anthropic list prices, not Fireworks rates. Use `fireconnect claude usage` to estimate real Fireworks spend from session logs.

On a TTY, `usage` opens a session picker (last 3 days by default), then a live cost meter. Tab: agents pane. Esc: session list. q: quit.

```bash theme={null}
fireconnect claude usage                 # picker → live meter
fireconnect claude usage --days 7        # picker lookback only (1–365)
fireconnect claude usage --session <id>  # start on one session
fireconnect claude usage --last-n 5      # snapshot, no picker (--days ignored)
fireconnect claude usage --plain         # plain text
fireconnect claude usage --json          # JSON
```

For a tmux split (Claude Code left, meter right):

```bash theme={null}
fireconnect claude live
fireconnect claude live --session <id>
```

Requires `tmux`. Neither command changes harness settings.

## Troubleshooting

### Text-only models and images

Claude Code cannot mark a model as non-vision. Pasting an image on a **text-only** slot (for example `glm-fast-latest` or `deepseek-flash-latest`) can break the session.

**Recover with `/rewind`**, then avoid images on that slot or map it to a vision model (for example `kimi-fast-latest`):

```bash theme={null}
fireconnect claude on --sonnet kimi-fast-latest
```

`fireconnect claude on` warns when your mapping includes text-only models. `fireconnect claude status` labels each slot `vision` or `text-only`.

## CLI reference

```bash theme={null}
fireconnect claude on         # Route Claude Code through Fireworks
fireconnect claude off        # Restore your previous provider
fireconnect claude status     # Provider, auth, and model mapping
fireconnect claude usage      # Session cost meter
fireconnect claude live       # tmux split with live meter
fireconnect claude help       # Harness-specific help
```

Run `fireconnect claude help` for all options.

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
