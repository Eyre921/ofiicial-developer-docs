---
title: "Reserved Throughput"
source: https://docs.fireworks.ai/serverless/reserved-throughput
path: serverless/reserved-throughput
---

Reserve throughput backed by an SLA

## Overview

Reserved throughput lets you pre-purchase throughput that **guarantees availability and uptime** up to your reservation level.

If you are experiencing rate limits on Serverless, you should consider Reserved Throughput. [Contact us](https://fireworks.ai/contact) to purchase reserved throughput or learn more.

You can re-allocate throughput between models served on Serverless. Usage above your reserved throughput is billed at standard Serverless pricing and subject to Serverless adaptive rate limits.

## How it works

You purchase Reserved Throughput as a reserved dollar-per-minute amount. Each minute, your eligible usage is priced and deducted from that amount. Any usage above the reserved amount is charged at standard [Serverless pricing](/serverless/pricing).

For example, with a **\$10-per-minute reservation**:

* Eligible usage is deducted from your reserved amount each minute.
* In any minute when your eligible usage is \$10 or less, it is fully covered by your reservation.
* If your usage exceeds \$10 in a minute, the amount above is billed at standard Serverless rates. If you use \$12 in a minute, \$10 is covered and \$2 is billed as overage.
* Reserved throughput is use-it-or-lose-it per minute and does not accumulate.

<img alt="Bar chart showing eligible usage covered by a $10-per-minute reservation and usage above $10 billed as overage" />

<img alt="Bar chart showing eligible usage covered by a $10-per-minute reservation and usage above $10 billed as overage" />

## Example: Kimi K3

Assume an average workload shape of 5,000 uncached input tokens, 50,000 cached input tokens (about a 91% cache hit rate), and 200 output tokens per request, with average QPS of 4 and p95 QPS of 5.

You decide to reserve to p95, so you size for 5 QPS × 60 seconds = 300 requests per minute.

| Token type     | Tokens per request | TPM at 300 requests/min | List price   | Cost per minute |
| -------------- | ------------------ | ----------------------- | ------------ | --------------- |
| Uncached input | 5,000              | 1.5M                    | \$3.00 / 1M  | \$4.50          |
| Cached input   | 50,000             | 15M                     | \$0.30 / 1M  | \$4.50          |
| Output         | 200                | 0.06M                   | \$15.00 / 1M | \$0.90          |
| **Total**      |                    |                         |              | **\$9.90**      |

Your p95 workload costs \$9.90 per minute, so you purchase a **\$10-per-minute reservation** for some headroom.

Your dollar-per-minute rate is derived from:

* The throughput you need—tokens per minute across uncached input, cached input, and output.
* Per-token list pricing for the models you are serving.

## Burst usage

If your usage exceeds your reserved amount in a minute, the amount above is billed at standard Serverless rates. This burst usage is not covered by an SLA and is subject to standard [Serverless adaptive rate limits](/serverless/rate-limits).

For example, with a \$10-per-minute reservation and \$12 of usage in one minute, \$10 is covered and \$2 is billed as overage.

## Move throughput across models

Reserved Throughput can be allocated to any model served on Serverless. We are working on making this self-service. Until then, contact your Fireworks account team to move your reservation.

For example, consider moving all of a \$10-per-minute reservation from Kimi K3 to DeepSeek V4 Pro (0813), while holding the workload shape from the previous example constant:

|                          | Kimi K3      | DeepSeek V4 Pro (0813) |
| ------------------------ | ------------ | ---------------------- |
| Uncached input           | \$3.00 / 1M  | \$1.32 / 1M            |
| Cached input             | \$0.30 / 1M  | \$0.044 / 1M           |
| Output                   | \$15.00 / 1M | \$3.96 / 1M            |
| Cost per 1,000 requests  | \$33.00      | \$9.59                 |
| Requests/min at \$10/min | \~303        | \~1,042                |
| Sustained QPS            | \~5          | \~17                   |

Because DeepSeek V4 Pro (0813) has lower token pricing than Kimi K3, the same \$10-per-minute reservation sustains roughly 3.4 times the throughput—about 17 QPS instead of 5.

The uplift is not a single price ratio. DeepSeek V4 Pro (0813) is 2.3 times cheaper on uncached input, 6.8 times cheaper on cached input, and 3.8 times cheaper on output. The improvement depends on your workload shape; a cache-heavy workload like this one benefits more than a generation-heavy workload.

## Pricing and SLAs

<AccordionGroup>
  <Accordion title="How is Reserved Throughput priced?">
    Reserved throughput is priced per token at standard [Serverless list prices](/serverless/pricing).
  </Accordion>

  <Accordion title="How should I size my reservation?">
    Size your reservation against per-minute TPM levels, such as your peak or p95 usage.
  </Accordion>

  <Accordion title="What happens once I hit my reserved amount?">
    Usage above your reservation is processed pay-as-you-go and billed at list price. Overage carries no SLA and is subject to your standard adaptive rate limits.
  </Accordion>

  <Accordion title="Is my reserved traffic subject to an SLA?">
    Yes. Traffic within your reservation is covered by a throughput SLA.
  </Accordion>

  <Accordion title="Does unused reserved throughput roll over?">
    No. Reserved throughput is use-it-or-lose-it on a per-minute basis.
  </Accordion>
</AccordionGroup>

## Rate limits and usage

<img alt="Diagram showing reserved throughput added on top of existing Serverless adaptive rate limits" />

<img alt="Diagram showing reserved throughput added on top of existing Serverless adaptive rate limits" />

<AccordionGroup>
  <Accordion title="How do I enable calls to use Reserved Throughput?">
    This happens automatically for models chosen in coordination with Fireworks. Eligible traffic on your account is counted against your reserved amount—no new endpoint, parameter, or code change is required.
  </Accordion>

  <Accordion title="How does this affect my rate limits?">
    Reserved Throughput is added to your Serverless adaptive rate limits. Usage within your reservation does not count against adaptive rate limits.
  </Accordion>

  <Accordion title="How does my cache hit rate affect what I get?">
    Cached input is priced well below uncached input, so a higher cache hit rate means more throughput per dollar reserved. See [prompt caching](/guides/prompt-caching).
  </Accordion>

  <Accordion title="Can I reserve throughput for custom or fine-tuned models?">
    Yes. [Contact us](https://fireworks.ai/contact) to discuss your requirements.
  </Accordion>
</AccordionGroup>
