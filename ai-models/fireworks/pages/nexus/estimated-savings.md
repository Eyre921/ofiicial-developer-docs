---
title: "Estimated Savings"
source: https://docs.fireworks.ai/nexus/estimated-savings
path: nexus/estimated-savings
---

Compare eligible serverless usage at public list prices with what the same tokens would have cost on Claude Opus 5.5.

* Open it at Analytics → [Savings](https://nexus.fireworks.ai/savings).
* Only account admins on Nexus-enabled accounts can view it.
* It counts direct Fireworks serverless usage and Nexus Auto turns, including turns that went to a closed model.

![Analytics Savings tab showing total saved this month, cache hit rate, and a Spend vs Opus 5.5 chart with per-day stacked bars and a baseline line](https://mintcdn.com/fireworksai/NqCTPiMRl6q7tf99/images/fireworks-nexus/savings/savings-view.png?fit=max\&auto=format\&n=NqCTPiMRl6q7tf99\&q=85\&s=3ced1c7cca9c2bf0d5d6dd6490a4332b)

The Savings view, with example data.

## How savings are calculated

```text theme={null}
Estimated savings = baseline cost − actual cost at public list price
Savings rate = estimated savings ÷ baseline cost
```

* **Actual cost:** the models that served the requests, at public list prices.
* **Baseline cost:** the same tokens on Claude Opus 5.5.

For example, usage that cost **\$2.45** but would have cost **\$8.15** on Opus 5.5 shows **\$5.70** saved, or **69.9%**. These amounts are illustrative.

A result can be negative when the serving model cost more than Opus 5.5 would have. Usage already served by Opus 5.5 usually saves nothing.

* The calculation runs for each comparable token category.
* Baseline cost covers the same uncached input, cached input, cache-write, and output tokens.
* Estimated savings can be positive, zero, or negative, and all are shown. A negative amount is not rounded to zero.
* The Savings view names the baseline model it compares against. Today that is Claude Opus 5.5. The baseline can change when the comparison is updated.

| Result | What it means |
| - | - |
| **Positive** | The serving models cost less than Claude Opus 5.5 for the same tokens |
| **Zero** | The usage cost the same as Claude Opus 5.5 |
| **Negative** | The serving model cost more than Claude Opus 5.5 would have |

Worked example: `Estimated savings = $8.15 − $2.45 = $5.70`, `Savings rate = $5.70 ÷ $8.15 = 69.9%`.

## What's included

* **Included:** Fireworks-hosted serverless models, closed models called through Nexus Auto, and direct eligible Fireworks serverless requests.
* **Not included:** dedicated deployments, and discounts, credits, taxes, negotiated rates, or other invoice adjustments.

- Included tokens: priced uncached input, cached input, cache-write, and output tokens from eligible serverless inference usage recorded for the account.
- Not included: token categories without both an actual price and a baseline price, and unpriced token quantities.
- Groups with no comparable priced usage are omitted.
- When you group usage by user or model, usage without a recorded user or model appears as unattributed.
- Variants of a Fireworks-hosted model are grouped under that model where possible.

## Savings are estimates

Savings figures are for comparison, not invoice amounts. For Fireworks billing totals, use the Costs view or your billing statement.

* Actual cost uses public list prices, not your account's contracted pricing.
* Closed-model provider costs are estimates too, and can differ from the provider's invoice.
* Recent usage can take a while to appear in Savings.

Related: [Nexus Auto](/nexus/auto), [Effort](/nexus/orchestration-preferences), [Usage and Cost](/nexus/metrics), [Spend Limits](/nexus/usage-limits), [Provider Keys](/nexus/provider-keys).
