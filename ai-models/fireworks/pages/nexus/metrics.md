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
| **Spend Limits** | Current-period spend on supported Fireworks serverless models against each user's cap | [Spend Limits](/nexus/usage-limits) |

## Track one Claude Code session

Claude Code session-cost tools run on the machine where the session ran. Other harnesses send requests through Nexus but don't have this local meter yet.

`nexus claude` adds a status line unless you already have one. Until the first billed call, it shows the model name. After that, it shows two lines:

| Line | What it shows |
| - | - |
| **1** | A spend bar and the estimated session cost. Each bar segment is a model that served traffic, sized by its share of estimated cost. On Nexus Auto (`auto`), once more than one model has served the session, it adds `routed model:` and the model that served the latest turn |
| **2** | Each model's name and cache share. When more than one model has served the session, each model's estimated cost too |

![Claude Code status line with a session cost bar split across several models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireworks-nexus/session-cost/status-line.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=01b2d8a5d81c24a5d898a694feb379a6)

Session cost, model mix, and cache share in Claude Code

Several models can appear in one bar. See [Nexus Auto](/nexus/auto) for why `auto` can use more than one model in a session.

The auto-mode line below the bar belongs to Claude Code, not the Fireworks `auto` model ID.

## Inspect a session

| Command | Use |
| - | - |
| `nexus claude usage` | Choose a session, then open its live meter with model choices, tokens, and estimated cost per request |
| `nexus claude usage --days 7` | Search further back than the default 3 days (1 to 365) |
| `nexus claude usage --session <id>` | Open one session directly. Takes a session ID or a log file path |
| `nexus claude usage --plain` | Print a one-time plain-text snapshot |
| `nexus claude usage --last-n 5 --json` | Return the five most recent sessions as JSON |
| `nexus claude usage --verbose` | Print one row per request, with rate details |

In the live meter:

| Key | Action |
| - | - |
| Tab | Focus the agents pane, when the session has subagents |
| ↑ and ↓, then Enter | Choose an agent in the pane and track it |
| Esc | Leave the agents pane, or return to the session list |
| `q` | Quit |

Each call is split into separate token buckets, each priced at that model's rate:

| Column | What it is | How it bills |
| - | - | - |
| `uncached` | Input tokens that missed the cache | Full input rate |
| `cached` | Input tokens served from the prompt cache | The model's cached-input rate. The discount varies by model |
| `write` | Tokens written into the cache | Anthropic charges a write premium. Fireworks models show 0 here |
| `cache%` | Share of input tokens served from the cache | Not billed separately |
| `out` | Generated tokens | Output rate |

## Break down Fireworks usage and cost

Use the [usage dashboard](https://app.fireworks.ai/account/usage) to break down Fireworks traffic by model, user, or API key over the selected date range. The **Cost** view groups Fireworks account spend by model:

![Usage dashboard Cost view split across several models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireworks-nexus/session-cost/account-cost.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=f2b646e4aa48b555f264e29521e253df)

Account cost by model. Names and amounts are illustrative.

> [!NOTE]
>
> The account dashboard covers Fireworks model usage and cost. It does not include usage billed by closed-model providers.

## Know which number you are reading

* **Status line and session meter:** a local estimate from token counts and published model rates. Fireworks models are priced at Fireworks rates, which `nexus model list` shows. Anthropic and OpenAI models are priced at provider list prices, from a cached copy that also works offline. Tool use, service tier, and region can make the invoice differ.
* **Claude Code's built-in HUD:** uses Anthropic list prices.
* **Usage dashboard:** Fireworks model usage and cost for the selected range.
* **Billing page:** the source of truth for the Fireworks invoice.

To cap each user's spend on supported Fireworks serverless models, set [Spend Limits](/nexus/usage-limits).
