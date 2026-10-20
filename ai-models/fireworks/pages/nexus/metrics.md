---
title: "Usage and Cost"
source: https://docs.fireworks.ai/nexus/metrics
path: nexus/metrics
---

Track estimated Claude Code session cost and model mix locally. Then view Fireworks model usage by model, user, or API key and Fireworks account cost by model.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

Track estimated cost and model choices for one Claude Code session, then review Fireworks model usage and cost across your account.

| View | Best for | Open it |
| - | - | - |
| **Claude Code status line** | Live estimated session cost, model mix, cache share | Connect with `fireconnect claude` |
| **Session meter** | Requests and estimated cost for one Claude Code session | `fireconnect claude usage` |
| **Usage dashboard** | Fireworks model usage by model, user, or API key | [Account usage](https://app.fireworks.ai/account/usage) |
| **User Limits** | Current-period spend on supported Fireworks serverless models against each user's cap | [User Limits](/nexus/usage-limits) |

## Track one Claude Code session

The status line shows which models served turns during the session. Each segment is sized by its share of estimated cost.

![Claude Code status line with a session cost bar split across several models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireworks-nexus/session-cost/status-line.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=01b2d8a5d81c24a5d898a694feb379a6)

Open the session meter for request-level detail:

```bash wrap theme={null}
fireconnect claude usage
```

The meter is local to the machine where Claude Code ran. Other harnesses route through Nexus but do not have this local meter yet. See [Session Cost](/nexus/session-usage) for commands and token buckets.

## Break down Fireworks usage and cost

Use the [usage dashboard](https://app.fireworks.ai/account/usage) to break down Fireworks traffic by model, user, or API key over the selected date range. The **Cost** view groups Fireworks account spend by model:

![Usage dashboard Cost view split across several models](https://mintcdn.com/fireworksai/r6jTtNQeedroFKBW/images/fireworks-nexus/session-cost/account-cost.png?fit=max\&auto=format\&n=r6jTtNQeedroFKBW\&q=85\&s=f2b646e4aa48b555f264e29521e253df)

> [!NOTE]
>
> The account dashboard covers Fireworks model usage and cost. It does not include usage billed by closed-model providers.

## Know which number you are reading

* **Session meter:** a local estimate from token counts and published model rates.
* **Usage dashboard:** Fireworks model usage and cost for the selected range.
* **Billing page:** the source of truth for the Fireworks invoice.

To cap each user's spend on supported Fireworks serverless models, set [Spend Limits](/nexus/usage-limits).
