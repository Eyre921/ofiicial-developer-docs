---
title: "Session Cost"
source: https://docs.fireworks.ai/nexus/session-usage
path: nexus/session-usage
---

Use FireConnect commands to inspect Claude Code session cost, model mix, cache share, token buckets, and request-level estimates.

Claude Code session-cost tools run on the machine where the session ran. After you [connect Claude Code](/nexus/harnesses#claude-code), use the status line for a live estimate or `fireconnect claude usage` for a detailed breakdown.

## Read the status line

`fireconnect claude` installs a status line unless you already have one. After the first billed call, it shows two lines:

| Line  | What it shows                                                                                                                                   |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | A spend bar and the estimated session cost. Each segment represents a model that served traffic                                                 |
| **2** | Each model's name, estimated cost, and cache share. For bare `firerouter`, it also shows the routing level, such as `balanced` or `max-savings` |

Several models can appear in one bar. See [FireRouter](/nexus/firerouter) for why `firerouter/...` can use multiple backends.

The auto-mode line below the bar belongs to Claude Code, not the Fireworks `auto` model ID.

The FireConnect status line and session meter use Fireworks rates. `fireconnect model list` shows those rates. Claude Code's built-in HUD uses Anthropic list prices.

## Inspect a session

| Command                                      | Use                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `fireconnect claude usage`                   | Choose a session, then open its live meter                                                      |
| `fireconnect claude usage --days 7`          | Search more than the default 3 days                                                             |
| `fireconnect claude usage --session <id>`    | Open one session directly                                                                       |
| `fireconnect claude usage --plain`           | Print a one-time snapshot                                                                       |
| `fireconnect claude usage --last-n 5 --json` | Return the five most recent sessions as JSON                                                    |
| `fireconnect claude usage --verbose`         | Show one row per request                                                                        |
| `fireconnect claude live`                    | Open Claude Code beside a live per-turn meter showing model choices, tokens, and estimated cost |

In the meter, press Tab to move between agents, Esc to return to the session list, or `q` to quit.

Each call is split into disjoint token buckets, priced at that model's rate:

| Column     | What it is                                | How it bills                                                    |
| ---------- | ----------------------------------------- | --------------------------------------------------------------- |
| `uncached` | Input tokens that missed the cache        | Full input rate                                                 |
| `cached`   | Input tokens served from the prompt cache | The model's cached-input rate; the discount varies by model     |
| `write`    | Tokens written into the cache             | Anthropic charges a write premium. Fireworks models show 0 here |
| `out`      | Generated tokens                          | Output rate                                                     |

## Understand the estimate

<Note>
  The meter estimates cost from token counts and published model rates. Tool use, service tier, and region can make the invoice differ. See [Usage and Cost](/nexus/metrics) for account usage and billing sources.
</Note>
