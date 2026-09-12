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
* FireConnect CLI v0.9.5+ (see [Install](/ecosystem/fireconnect/overview#install))

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

Restart Claude Code after enabling, then test with a simple prompt.

After `fireconnect claude on`, start a new Claude Code session or run `/model` to pick up model changes. To use a new model in the same session, start a new session or `/exit` and resume with `claude --resume <id>`.

## Change models

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --model firerouter               # main only
fireconnect claude on --interactive                    # model mapping wizard
fireconnect claude on --opus glm-fast-latest --sonnet auto-instant
fireconnect claude status
```

Model flags directly override the named slot. Set every slot you want to control explicitly. Use `native` as a slot value to leave a slot unpinned so Claude Code chooses its default for that role.

Re-running `on` without flags preserves your current mapping when FireConnect is already active (including `/model` changes made inside Claude Code). Reopen the wizard anytime:

```bash theme={null}
fireconnect claude on --interactive
```

Use `--non-interactive` to skip the wizard and apply saved preferences or the current profile. `--interactive` cannot be combined with model flags like `--model` or `--opus`.

Use the wizard to choose aliases, or use explicit model flags for a reproducible configuration.

### Smart router mixes

Pin Fireworks' open-model mixes on any slot:

```bash theme={null}
fireconnect claude on --sonnet auto              # default open-model mix
fireconnect claude on --sonnet auto-instant      # latency-first mix
```

`auto` appears on every slot in the picker; `auto-instant` is available on Sonnet. These route among Fireworks open models only — unlike FireRouter, they do not pass through to Claude Opus 5.

## What gets written

FireConnect writes the selected mapping to `~/.claude/settings.json`. Claude Code authenticates via the `X-Fireworks-Api-Key` custom header (not `apiKeyHelper`). The Fireworks key is written to the file with mode `0600`.

**Why the custom header?** The gateway authenticates via `X-Fireworks-Api-Key`, which wins over any stray `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` — so a leftover Anthropic key can't silently break routing.

**Model IDs and `[1m]`.** Short slugs are accepted everywhere. FireConnect adds a `[1m]` suffix on 1M-context models for every slot — subagent included — so Claude Code sizes the context window correctly. The gateway still sees the bare model ID; Claude Code strips the tag before sending.

`on` also:

* Denies Anthropic **server-side** `WebSearch` / `WebFetch` tools the gateway can't run, and installs the Fireworks [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp) when your account is eligible
* Installs a **status line** showing routed models and estimated session cost (see [Status line](#status-line)). Your own `statusLine` is never replaced
* Sends privacy-safe attribution headers (`X-Title`, `HTTP-Referer`) where supported

FireConnect saves a backup of your previous provider settings to `~/.fireconnect/claude/`. When that backup is available, `fireconnect claude off` restores it byte-for-byte; otherwise it removes FireConnect-managed settings. Legacy pins like `deepseek-v4-flash` migrate to `deepseek-flash-latest` on the next `on`.

## Status line

When you don't already have a custom `statusLine`, `on` installs one that shows which models actually served the session and their estimated cost:

```text theme={null}
━━━━━━━━━━━━ ━ ━ · $70.39
━ Claude Opus 5 $62.91 98% cache · ━ GLM 5.2 $7.35 96% cache · ━ DeepSeek V4 Flash $0.13 87% cache
```

The first line is a **multi-color bar** sized by each backend model's share of session spend, followed by the session total. The second line names each model with its cost and cache hit rate. FireRouter sessions show the whole mix at a glance — not just the latest model.

The cost uses Fireworks serverless rates for Fireworks models and Anthropic list rates for Anthropic models. Calls without a matched rate remain in usage totals but are not assigned a dollar cost.

`off` removes the status line. **If you already have a `statusLine`, FireConnect leaves it alone** — delete yours and re-run `fireconnect claude` to opt in.

## Web search MCP

When you run `fireconnect claude on`, FireConnect can install the Fireworks [WebSearch MCP](/ecosystem/fireconnect/websearch-mcp) for eligible accounts. FireConnect WebSearch integration is **Claude Code only today**; other harnesses can add the HTTP MCP manually.

When installation succeeds, `fireconnect claude on` prints `Web search → fireworks-websearch (installed)`. Restart Claude Code, then run `/mcp` and connect to `fireworks-websearch`.

`fireconnect claude off` removes the managed MCP entry and restores your previous `~/.claude/settings.json`.

## Browsing and picking models

```bash theme={null}
fireconnect model list --search glm
fireconnect model list --refresh
fireconnect claude on --sonnet kimi-latest
```

`fireconnect model list` shows serverless endpoints and pricing (cached for one hour; works offline). `fireconnect claude status` shows your current mapping, every slot including defaults, and available rates per slot.

Fire Pass keys only list Fire Pass routers. FireConnect rejects `--model firerouter` with Fire Pass (`fpk_...`) on every harness; use an `fw_...` key.

## FireRouter

Route requests through [FireRouter](/ecosystem/firerouter/overview). The default `firerouter` model ID is more likely to use **GLM 5.3** for lower-complexity work and **Claude Opus 5** for harder work. See [current routing pair](/ecosystem/firerouter/overview#current-routing-pair).

### Choose where FireRouter is used

Use `--model` for Main or a slot-specific flag for an alias:

```bash theme={null}
fireconnect claude on --model firerouter
fireconnect claude on --opus firerouter
```

<Warning>
  On first setup, FireConnect assigns models to slots you do not specify. Use `--interactive` to choose alias slots. To control the complete mapping including Main, set every slot explicitly. Use `native` to leave a slot unpinned.
</Warning>

```bash theme={null}
fireconnect claude on --interactive

# FireRouter on Main; leave every alias unpinned
fireconnect claude on --model firerouter \
  --opus native --sonnet native --haiku native \
  --fable native --subagent native
```

### Custom routing pairs

```bash theme={null}
fireconnect claude on --sonnet firerouter/claude-opus-5/glm-5p3-fast   # custom pair
```

Use a [slash-delimited FireRouter slug](/ecosystem/firerouter/overview#choose-different-models) on any slot (`firerouter/<primary>/<redirect>`, …) to change which models FireRouter can pick.

Anthropic credentials are needed only when the slug includes a Claude model (including bare `firerouter`). A Fireworks-only slug such as `firerouter/kimi-k3/glm-5p2-fast` needs only the Fireworks API key.

### Anthropic auth for pass-through

The default bare `firerouter` route's Claude Opus 5 leg needs Anthropic credentials. With FireConnect you usually **do not** pass a new key:

* **Claude subscription or browser OAuth** — Claude Code already attaches Anthropic auth on each request; Fireworks forwards it for pass-through.
* **Anthropic API key** — if Claude Code is configured with `ANTHROPIC_API_KEY`, that works too.
* **Explicit BYOK** — pass `--anthropic-api-key sk-ant-...` on `on`, or store once with `fireconnect configure --anthropic-api-key sk-ant-...`.
* **Workspace BYOK** — when enabled on your Fireworks account, no local Anthropic key is required.

### See which models served the session

After assistant messages run, check:

1. **Status line** (installed by `on` unless you already have a custom `statusLine`) — lists backend models that served the session (for example `Claude Opus 5` or `GLM 5.3`) and estimated session cost. Before a billed response, it may show `FireRouter` rather than a resolved backend. See [Status line](#status-line).
2. **`fireconnect claude status`** — shows the configured slot mapping and which slots use FireRouter. It does not show per-request routing decisions.

### Tune cost vs quality

Set routing preference with `--routing-preference` on `on` (`1`–`5` or a named level):

```bash theme={null}
fireconnect claude on --model firerouter --routing-preference 4
# max-intelligence (1) · more-intelligence (2) · balanced (3) · more-savings (4) · max-savings (5)
```

See [Routing preferences](/ecosystem/firerouter/routing-preferences).

Omit the flag to use FireRouter's default. Re-running `on` without `--routing-preference` clears a preference that FireConnect previously wrote.

## Usage and live meter

Claude Code's `/model` picker shows Anthropic list prices. Use `fireconnect claude usage` to estimate session cost from Fireworks serverless rates and Anthropic list rates.

On a TTY, `usage` opens a session picker (last 3 days by default), then a live cost meter. Tab: agents pane. Esc: session list. q: quit.

```bash theme={null}
fireconnect claude usage                 # picker → live meter
fireconnect claude usage --days 7        # picker lookback only (1–365)
fireconnect claude usage --session <id>  # start on one session
fireconnect claude usage --last-n 5      # snapshot, no picker (--days ignored)
fireconnect claude usage --plain         # plain text
fireconnect claude usage --json          # JSON
fireconnect claude usage --verbose       # request-level rows and rate details
```

For a tmux split (Claude Code left, meter right):

```bash theme={null}
fireconnect claude live
fireconnect claude live --session <id>
```

Requires `tmux`. Neither command changes harness settings.

Scripting:

```bash theme={null}
fireconnect claude status --json
fireconnect claude usage --last-n 5 --json
```

## Troubleshooting

### Text-only models and images

Claude Code cannot mark a model as non-vision. Pasting an image on a **text-only** slot (for example `glm-fast-latest` or `deepseek-flash-latest`) can break the session.

**Recover with `/rewind`**, then avoid images on that slot or map it to a vision model:

```bash theme={null}
fireconnect claude on --sonnet kimi-fast-latest
```

`fireconnect claude on` warns when your mapping includes text-only models. `fireconnect claude status` labels each slot `vision` or `text-only`.

### Pricing estimates

Claude Code's session cost uses **Anthropic list prices**, while Fireworks bills at **serverless rates**. Use `fireconnect claude status`, `fireconnect model list`, and the [billing dashboard](https://app.fireworks.ai/account/billing) for actual spend.

## CLI reference

```bash theme={null}
fireconnect claude on         # Route Claude Code through Fireworks
fireconnect claude off        # Restore your previous provider
fireconnect claude status     # Provider, auth, and model mapping
fireconnect claude usage      # Session cost meter
fireconnect claude live       # tmux split with live meter
fireconnect claude demo       # Race two models on a prompt
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
