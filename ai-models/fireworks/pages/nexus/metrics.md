---
title: "Usage and Cost"
source: https://docs.fireworks.ai/nexus/metrics
path: nexus/metrics
---

Track estimated Claude Code session cost and model mix locally. Then view Fireworks model usage by model, user, or API key and Fireworks account cost by model.

Track estimated cost and model choices for one Claude Code session, then review Fireworks model usage and cost across your account.

| View                        | Best for                                                                              | Open it                                                 |
| --------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Claude Code status line** | Live estimated session cost, model mix, cache share                                   | Connect with `fireconnect claude`                       |
| **Session meter**           | Requests and estimated cost for one Claude Code session                               | `fireconnect claude usage`                              |
| **Usage dashboard**         | Fireworks model usage by model, user, or API key                                      | [Account usage](https://app.fireworks.ai/account/usage) |
| **User Limits**             | Current-period spend on supported Fireworks serverless models against each user's cap | [User Limits](/nexus/usage-limits)                      |

## Track one Claude Code session

The status line shows which models served turns during the session. Each segment is sized by its share of estimated cost.

<Frame>
  <img alt="Claude Code status line with a session cost bar split across several models" />
</Frame>

Open the session meter for request-level detail:

```bash wrap theme={null}
fireconnect claude usage
```

The meter is local to the machine where Claude Code ran. Other harnesses route through Nexus but do not have this local meter yet. See [Session Cost](/nexus/session-usage) for commands and token buckets.

## Break down Fireworks usage and cost

Use the [usage dashboard](https://app.fireworks.ai/account/usage) to break down Fireworks traffic by model, user, or API key over the selected date range. The **Cost** view groups Fireworks account spend by model:

<Frame>
  <img alt="Usage dashboard Cost view split across several models" />
</Frame>

<Note>
  The account dashboard covers Fireworks model usage and cost. It does not include usage billed by closed-model providers.
</Note>

## Know which number you are reading

* **Session meter:** a local estimate from token counts and published model rates.
* **Usage dashboard:** Fireworks model usage and cost for the selected range.
* **Billing page:** the source of truth for the Fireworks invoice.

To cap each user's spend on supported Fireworks serverless models, set [Spend Limits](/nexus/usage-limits).
