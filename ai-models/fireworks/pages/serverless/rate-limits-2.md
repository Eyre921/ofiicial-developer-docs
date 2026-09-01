---
title: "Serverless Rate Limits"
source: https://docs.fireworks.ai/serverless/rate-limits
path: serverless/rate-limits
---

Adaptive rate limits grow and shrink with your usage

When using Serverless, you may experience `429 Too Many Requests` or `503 Service Overloaded`. To avoid 429s, you need to stay below our adaptive rate limits. To reduce the likelihood of 503s, you can upgrade to [Priority tier](/serverless/serving-paths).

## What are your rate limits?

There are three metrics we use to rate limit accounts:

* **Total Prompt TPM** — input tokens per minute (cached + uncached).
* **Uncached Prompt TPM** — uncached input tokens per minute.
* **Generated TPM** — output tokens per minute.

**Default ceilings:** 21.6M Total Prompt TPM, 5.4M Uncached Prompt TPM, 216k Generated TPM (\~360k / \~90k / \~3.6k TPS). **Enforcement uses TPM**, not TPS.

Based on your usage, your adaptive limits will grow and shrink. If your traffic ramps up too quickly, you will get 429s.

<img alt="kimi-k2p6 usage and rate limits" />

Your current effective rate limits (described in tokens per second) are in the response headers `X-Ratelimit-Limit-Tokens-Prompt`, `X-Ratelimit-Limit-Tokens-Cache-Adjusted-Prompt`, and `X-Ratelimit-Limit-Tokens-Generated`.

Adaptive rate limits have an upper and lower bound. A higher account [Spending Tier](/guides/quotas_usage/account-quotas#spending-tiers) correlates with higher upper bound rate limits; **enterprise accounts** get higher upper bounds automatically.

## FAQ

<AccordionGroup>
  <Accordion title="Am I guaranteed successful responses up to my rate limit?">
    **No.** Staying within your rate limits does not guarantee that every request succeeds. When a deployment is busy, your traffic can still be **load shed**, and those responses are **`503 Service Overloaded`**. To **decrease the chance** of being load shed, you can use [Priority tier](/serverless/serving-paths), which is prioritized during high load.
  </Accordion>

  <Accordion title="How are rate limits scoped?">
    Rate limits are scoped **per account** and **per model**. **Fast** and **regular** model variants have **separate** limits. **Priority tier** and **regular** requests share the **same** rate limits for a given model.
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
