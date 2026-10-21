---
title: "Usage and Cost"
source: https://docs.fireworks.ai/nexus/metrics
path: nexus/metrics
---

Track estimated Claude Code session cost and model mix locally. Then view Fireworks model usage by model, user, or API key and Fireworks account cost by model.

Track estimated cost and model choices for one Claude Code session, then review Fireworks model usage and cost across your account.

| View | Best for | Open it |
| - | - | - |
| **Claude Code status line** | Live estimated session cost, model mix, cache share | Connect with `nexus claude` |
| **Session meter** | Requests and estimated cost for one Claude Code session | `nexus claude usage` |
| **Usage dashboard** | Fireworks model usage by model, user, or API key | [Account usage](https://app.fireworks.ai/account/usage) |
| **User Limits** | Current-period spend on supported Fireworks serverless models against each user's cap | [User Limits](/nexus/usage-limits) |

## Track one Claude Code session

Claude Code session-cost tools run on the machine where the session ran. Other harnesses send requests through Nexus but do not have this local meter yet.

`nexus claude` installs a status line unless you already have one. After the first billed call, it shows two lines:

| Line | What it shows |
| - | - |
| **1** | A spend bar, the estimated session cost, and, for Nexus Auto (`auto`), `routed model:` with the model that served the latest turn. Each bar segment represents a model that served traffic, sized by its share of estimated cost |
| **2** | Each model's name, estimated cost, and cache share |

![Claude Code status line with a session cost bar split across several models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireworks-nexus/session-cost/status-line.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=01b2d8a5d81c24a5d898a694feb379a6)

Several models can appear in one bar. See [Nexus Auto](/nexus/auto) for why `auto` can use multiple backends.

The auto-mode line below the bar belongs to Claude Code, not the Fireworks `auto` model ID.

## Inspect a session

| Command | Use |
| - | - |
| `nexus claude usage` | Choose a session, then open its live meter |
| `nexus claude usage --days 7` | Search more than the default 3 days |
| `nexus claude usage --session <id>` | Open one session directly |
| `nexus claude usage --plain` | Print a one-time snapshot |
| `nexus claude usage --last-n 5 --json` | Return the five most recent sessions as JSON |
| `nexus claude usage --verbose` | Show one row per request |
| `nexus claude live` | Open Claude Code beside a live per-turn meter showing model choices, tokens, and estimated cost |

In the meter, press Tab to move between agents, Esc to return to the session list, or `q` to quit.

Each call is split into disjoint token buckets, priced at that model's rate:

| Column | What it is | How it bills |
| - | - | - |
| `uncached` | Input tokens that missed the cache | Full input rate |
| `cached` | Input tokens served from the prompt cache | The model's cached-input rate; the discount varies by model |
| `write` | Tokens written into the cache | Anthropic charges a write premium. Fireworks models show 0 here |
| `cache%` | Share of input tokens served from the cache | Not billed separately |
| `out` | Generated tokens | Output rate |

## Break down Fireworks usage and cost

Use the [usage dashboard](https://app.fireworks.ai/account/usage) to break down Fireworks traffic by model, user, or API key over the selected date range. The **Cost** view groups Fireworks account spend by model:

![Usage dashboard Cost view split across several models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireworks-nexus/session-cost/account-cost.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=f2b646e4aa48b555f264e29521e253df)

> [!NOTE]
>
> The account dashboard covers Fireworks model usage and cost. It does not include usage billed by closed-model providers.

## Know which number you are reading

* **Status line and session meter:** a local estimate from token counts and published model rates. They price Fireworks models at Fireworks rates, which `nexus model list` shows, and Anthropic and OpenAI models at provider list prices, from a cached copy that also works offline. Tool use, service tier, and region can make the invoice differ.
* **Claude Code's built-in HUD:** uses Anthropic list prices.
* **Usage dashboard:** Fireworks model usage and cost for the selected range.
* **Billing page:** the source of truth for the Fireworks invoice.

To cap each user's spend on supported Fireworks serverless models, set [Spend Limits](/nexus/usage-limits).
