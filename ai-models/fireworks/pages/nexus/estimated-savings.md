---
title: "Estimated Savings"
source: https://docs.fireworks.ai/nexus/estimated-savings
path: nexus/estimated-savings
---

Compare eligible serverless usage at public list prices with what the same tokens would have cost on Claude Opus 5.5.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

The Savings view estimates how much your account saved by using Fireworks models and FireRouter instead of serving the same tokens entirely with the baseline model.

Savings includes eligible direct Fireworks serverless usage as well as usage routed through FireRouter. It is not limited to requests where FireRouter selected an open model.

To view your savings, go to Analytics → [Savings](https://app.fireworks.ai/account/usage?type=savings).

![Analytics Savings tab showing total saved this month, cache hit rate, and a Spend vs Opus 5.5 chart with per-day stacked bars and a baseline line](https://mintcdn.com/fireworksai/NqCTPiMRl6q7tf99/images/fireworks-nexus/savings/savings-view.png?fit=max\&auto=format\&n=NqCTPiMRl6q7tf99\&q=85\&s=3ced1c7cca9c2bf0d5d6dd6490a4332b)

> [!NOTE]
>
> Only account admins on Nexus-enabled accounts can view Estimated Savings.

## How savings are calculated

For each comparable token category, Fireworks calculates:

```text theme={null}
Estimated savings = baseline cost − actual cost at public list price
Savings rate = estimated savings ÷ baseline cost
```

| Amount | Meaning |
| - | - |
| **Actual cost** | Estimated cost of the models that served the requests, at public list prices. |
| **Baseline cost** | What the same uncached input, cached input, cache-write, and output tokens would have cost on Claude Opus 5.5. |
| **Estimated savings** | Baseline cost minus actual cost. Positive, zero, and negative values are all shown. |

The Savings view displays the baseline model used for the comparison. The current baseline is Claude Opus 5.5. The baseline may change as the comparison is updated.

## How to read a result

| Result | What it means |
| - | - |
| **Positive** | The serving models cost less than Claude Opus 5.5 for the same tokens. |
| **Zero** | The usage cost the same as Claude Opus 5.5. Usage already served by Opus 5.5 usually saves nothing. |
| **Negative** | The serving model cost more than Claude Opus 5.5 would have. The amount is not rounded to zero. |

### Example

Suppose an account's eligible usage cost an estimated **\$2.45** at public list prices. The same tokens would have cost an estimated **\$8.15** on Claude Opus 5.5.

```text theme={null}
Estimated savings = $8.15 − $2.45 = $5.70
Savings rate = $5.70 ÷ $8.15 = 69.9%
```

The Savings view reports **\$5.70** in estimated savings, or **69.9%**. These amounts are illustrative.

## What is included

Savings includes eligible serverless inference usage recorded for the account:

* Fireworks-hosted serverless models
* Closed models called through FireRouter
* Direct eligible Fireworks serverless requests
* Priced uncached input, cached input, cache-write, and output tokens

When usage is grouped by user or model, usage without recorded attribution appears as unattributed. Fireworks-hosted internal model variants are grouped under their public model where possible.

## What is not included

Savings does not include:

* Dedicated deployment usage
* Token categories without both an actual price and a baseline price
* Unpriced token quantities
* Discounts, credits, taxes, negotiated rates, or other invoice adjustments

Groups with no comparable priced usage are omitted.

## Savings are estimates

> [!WARNING]
>
> Savings figures are for comparison and are not invoice amounts. Actual cost uses public list prices rather than your account's contracted pricing. Costs from closed-model providers are also estimates and may differ from the provider's invoice. For Fireworks billing totals, use the Costs view or your billing statement. Recent usage may take time to appear in Savings.

## Related

* [FireRouter](/nexus/firerouter)
* [Routing Preferences](/nexus/routing-preferences)
* [Usage and Cost](/nexus/metrics)
* [Spend Limits](/nexus/usage-limits)
* [Provider Keys](/nexus/provider-keys)
