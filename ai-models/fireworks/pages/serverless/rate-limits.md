---
title: "Serverless Rate Limits"
source: https://docs.fireworks.ai/serverless/rate-limits
path: serverless/rate-limits
---

Adaptive rate limits grow and shrink with your usage

When using Serverless, you may experience `429 Too Many Requests` or `503 Service Overloaded`. To avoid 429s, you need to stay below our adaptive rate limits. To reduce the likelihood of 503s, you can upgrade to [Priority tier](/serverless/serverless-modes).

## What are your rate limits?

There are three metrics we use to rate limit accounts:

* **Total Prompt TPM** — input tokens per minute (cached + uncached).
* **Uncached Prompt TPM** — uncached input tokens per minute.
* **Generated TPM** — output tokens per minute.

All limits are measured and enforced in **tokens per minute (TPM)**.

Adaptive rate limit ceilings depend on the model's total parameter count. Smaller models get higher ceilings:

| Tier | Total parameters | Total Prompt TPM | Uncached Prompt TPM | Generated TPM |
| - | - | - | - | - |
| **Small** | \< 600B | 216M | 54M | 2.16M |
| **Medium** | 600B – \< 1.6T | 43.2M | 10.8M | 432k |
| **Large** | ≥ 1.6T | 21.6M | 5.4M | 216k |

Fast, Priority, and US-only variants of a model share the same tier and ceilings as the base model. Models without a known parameter count use **Large** ceilings.

### Models by tier

| Tier | Models |
| - | - |
| **Small** | DeepSeek V4.1 Flash, GLM 5.3 Flash, MiniMax M3, NVIDIA Nemotron 3 Ultra (Preview), OpenAI GPT OSS 120B, NVIDIA Nemotron 3.5 Lightning 30B A3B |
| **Medium** | GLM 5.3 |
| **Large** | Ember-1, Kimi K3, Qwen 3.8 Max |

Models not listed here are tiered by total parameter count using the thresholds above.

Based on your usage, your adaptive limits will grow and shrink within these ceilings. If your traffic ramps up too quickly, you will get 429s.

<img alt="kimi-k2p6 usage and rate limits" />

Your current limits for each model are in the [Serverless dashboard](https://app.fireworks.ai/dashboard/serverless). See [Checking your current limit](#checking-your-current-limit).

Adaptive rate limits have an upper and lower bound. A higher account [Spending Tier](/guides/quotas_usage/account-quotas#spending-tiers) correlates with higher upper bound rate limits; **enterprise accounts** get higher upper bounds automatically.

## How do adaptive limits change?

Your limit for each model starts at a default value and grows in steps as you use it. If your recent one-minute usage is above 50% of your current limit, the limit increases by 25%, and no more than once every 15 minutes, until it reaches your ceiling. If you stop using it, the limit shrinks slowly and eventually resets.

Each of the three metrics (Total Prompt TPM, Uncached Prompt TPM, and Generated TPM) has its own limit and changes on its own. Heavy usage on one metric does not change the other two.

### Your ceiling

The ceiling is the highest your limit can grow. Two things set it:

* **Model size** picks the row in the [table above](#model-size-tiers).
* **Your [spending tier](/guides/quotas_usage/account-quotas#spending-tiers)** sets how much of that row you can reach. The table shows the maximum ceilings, available at Tier 3 and above. Tiers below Tier 3 have lower ceilings.

### When limits go up, down, or reset

| Change | When it happens | Amount |
| - | - | - |
| **Increase** | Your recent usage is above 50% of your current limit. Increases happen at most once every 15 minutes. | Up 25%, capped at your ceiling |
| **Decrease** | Your highest sampled 15-minute usage over the past 3 days stayed below 33% of your current limit, and at least 24 hours have passed since the limit last changed. | Down 20%, never below the lower bound |
| **Reset** | You send no traffic to the model for more than 72 hours. | Back to the starting default |

A few details:

* A decrease is skipped if your recent usage would be at least 50% of the lower limit. This keeps the limit from dropping and then immediately climbing back up.
* With [Reserved Throughput](/serverless/reserved-throughput), these thresholds apply to burst usage above your reservation and to the adaptive portion of your limit. Your reservation is added to that adaptive limit, and usage within the reservation does not count toward the thresholds.
* Resets do not apply to accounts with a custom limit or a reservation for that model.
* If you have reserved throughput, your limit never drops below your reservation.

### How slowly limits shrink

Say your Total Prompt TPM limit is 10,000,000 and your traffic drops to a steady 1,000,000 tokens per minute:

| Day | Limit (tokens per minute) | What happens |
| - | - | - |
| 0 to 3 | 10,000,000 | No change. Your earlier, heavier traffic is still in the 3 day window. |
| 3 | 8,000,000 | First decrease, once the heavy traffic ages out of the window. |
| 4 | 6,400,000 | |
| 5 | 5,120,000 | |
| 6 | 4,096,000 | |
| 7 | 3,276,800 | |
| 8 | 2,621,440 | Last decrease. 1,000,000 is now more than one third of the limit. |

If you stop sending traffic completely, you don't go through these steps. After more than 72 hours with no traffic, the limit resets to the starting default.

### Example: ramping up

Say your current Total Prompt TPM limit is 1,000,000.

1. Send more than 500,000 but less than 1,000,000 prompt tokens per minute. This keeps you above half your limit without hitting 429s.
2. More than 15 minutes later, your limit rises to 1,250,000.
3. Raise your traffic to match, staying between 625,000 and 1,250,000.
4. Repeat until your limit stops rising.

At this pace, you reach your ceiling in a few hours. If you are using more than half your limit and it has stopped rising after an increase interval, you are at the ceiling for your spending tier. Moving to a higher spending tier, up to Tier 3, raises the ceiling, and the limit keeps growing in the same 25% steps.

A short burst does not lock in a higher limit. If you go 72 hours without traffic, the limit resets to the default.

### Checking your current limit

Check your current limit in the [Serverless dashboard](https://app.fireworks.ai/dashboard/serverless).

The same limits are also returned in the [response headers](/serverless/overview#response-headers) on each request. Header values are tokens per minute, so you can compare them directly with the TPM ceilings above.

## FAQ

<AccordionGroup>
  <Accordion title="Am I guaranteed successful responses up to my rate limit?">
    **No.** Staying within your rate limits does not guarantee that every request succeeds. When a deployment is busy, your traffic can still be **load shed**, and those responses are **`503 Service Overloaded`**. To **decrease the chance** of being load shed, you can use [Priority tier](/serverless/serverless-modes), which is prioritized during high load.
  </Accordion>

  <Accordion title="How are rate limits scoped?">
    Rate limits are scoped **per account** and **per model**. **Fast** and **regular** model variants have **separate** limits. **Priority tier** and **regular** requests share the **same** rate limits for a given model.
  </Accordion>

  <Accordion title="How is my model's ceiling tier determined?">
    Ceiling tiers are based on the model's **total parameter count**: **Small** (\< 600B), **Medium** (600B – \< 1.6T), or **Large** (≥ 1.6T). See [Model size tiers](#model-size-tiers) for the ceiling values and [Models by tier](#models-by-tier) for where each Serverless model falls.
  </Accordion>

  <Accordion title="What should I do first when I see 429s?">
    First, try **exponential backoff** when retrying.
  </Accordion>

  <Accordion title="How do I get higher limits sooner?">
    Reach out to [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) for a custom solution if either of these applies:

    * **You need higher than the defaults from day one.** Your launch traffic exceeds the starting limit and you can't wait for the adaptive ramp.
    * **You're ramping past the highest upper bound.** You are already at the highest account Spending Tier and the adaptive rate limits are not growing.
  </Accordion>
</AccordionGroup>
