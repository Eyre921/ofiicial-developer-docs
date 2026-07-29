---
title: "Provisioned throughput"
source: https://docs.together.ai/docs/inference/provisioned-throughput
path: docs/inference/provisioned-throughput
---

Reserved inference capacity for production workloads.

Provisioned throughput gives you reserved capacity for a selected model or model family on Together AI's managed inference infrastructure. You commit to a number of [provisioned throughput units (PTUs)](#how-ptus-work) for a fixed term of one month or more, and Together commits to throughput and reliability targets for traffic within your purchased capacity.

Provisioned throughput uses the same [inference API](/docs/inference/overview#shared-inference-api) surface as serverless and dedicated endpoints, so your application code stays the same after you reserve capacity.

<CardGroup>
  <Card title="Contact sales to request provisioned throughput" href="https://www.together.ai/contact-sales-pt">
    Provisioned throughput is currently unavailable for self-service. Contact our sales team to request a quote or scope a commitment.
  </Card>
</CardGroup>

## Supported models

Provisioned throughput is available for the following models:

| Model                                                   | Model string           |
| ------------------------------------------------------- | ---------------------- |
| [Kimi K3](https://www.together.ai/models/kimi-k3)       | `moonshotai/Kimi-K3`   |
| [MiniMax M3](https://www.together.ai/models/minimax-m3) | `MiniMaxAI/MiniMax-M3` |
| [GLM-5.2](https://www.together.ai/models/glm-52)        | `zai-org/GLM-5.2`      |

To request provisioned throughput for a model that isn't listed, [contact sales](https://www.together.ai/contact-sales-pt).

## When to use provisioned throughput

Consider provisioned throughput when:

* You're moving high-volume production traffic off a proprietary model API and want to cut cost by switching to open models without giving up reliability.
* You need a defined SLA and committed capacity that [serverless models](/docs/serverless/models) can't guarantee.
* Your traffic is steady and predictable enough to reserve capacity for, rather than competing for the shared serverless pool.

If you need to serve a fine-tuned model, or want direct control over hardware, latency, and throughput, use [dedicated endpoints](/docs/dedicated-endpoints/overview).

|                      | Serverless                                                            | Provisioned throughput                                      | Dedicated endpoints                                                                 |
| -------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **What you reserve** | Nothing; shared fleet.                                                | Committed PT capacity for a selected model or model family. | GPUs reserved only for you.                                                         |
| **Billing unit**     | Per token, per second, or per unit of output.                         | Per PTU, on a fixed term (one-month minimum).               | Per minute of reserved hardware.                                                    |
| **SLA**              | Best-effort with [dynamic rate limits](/docs/serverless/rate-limits). | Defined targets for throughput and reliability.             | No shared-fleet rate limits; performance shaped by your hardware and settings.      |
| **Best for**         | Prototyping and variable traffic.                                     | Production workloads on stock models.                       | Fine-tuned models, custom hardware, or fine-grained latency and throughput control. |
| **How to access**    | Self-serve.                                                           | [Contact sales.](https://www.together.ai/contact-sales-pt)  | Self-serve.                                                                         |

## How PTUs work

A provisioned throughput unit (PTU) is the unit of capacity you buy. Each PTU is a fixed slice of guaranteed throughput for a model or model family, priced at a flat \$0.05 per PTU per minute. You buy PTUs for the volume you expect to send, and as traffic flows through, it draws down your committed capacity.

Input tokens, output tokens, and cached reads consume PTUs at different rates. Output tokens are more expensive to serve than input tokens, and cached reads are cheaper than fresh inputs. The exact conversion rates are model-specific and published on the [pricing page](https://www.together.ai/pricing#provisioned-throughput) as tokens per minute (TPM) per PTU for each token type.

You don't need to forecast a precise traffic mix. Whatever shape your traffic takes, it converts into a single rate that draws down your PTU capacity: each token type's TPM is divided by its published TPM per PTU, and the results are added together. Output-heavy or cache-light traffic consumes PTUs faster, while cache-heavy traffic consumes them more slowly. Traffic shape changes how quickly you consume PTUs, not the SLA.

To estimate how many PTUs your workload needs, use the [pricing calculator](https://www.together.ai/pricing#provisioned-throughput).

## SLA

Eligible traffic that fits within your purchased PTUs and the published product limits is backed by the following service level agreement (SLA):

| Dimension       | Commitment                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Throughput**  | We serve your eligible traffic up to the maximum throughput your purchased PTUs entitle you to for the selected model or model family, measured in TPM. |
| **Reliability** | At least 99% of eligible requests complete successfully each month, measured as requests that don't fail due to a Together-caused error.                |

<Note>
  **Eligible requests** include all requests made within your purchased PTU capacity and the published product limits. Customer errors, invalid requests, authentication failures, client cancellations, traffic above your purchased capacity, and requests that violate our published abuse or product protection limits are not covered by the SLA.
</Note>

## Overage behavior

Traffic above your purchased PTU capacity may fall back to the shared serverless pool on a best-effort basis when capacity is available, billed at standard serverless rates. If serverless capacity isn't available, that traffic may be rate limited or not served. Overage traffic is not covered by the provisioned throughput SLA.

If you consistently run above your PTU commitment, you may be able to expand it through your sales contact. Don't rely on overage as a substitute for buying enough PTUs to handle your steady-state traffic.

PTUs reserve capacity for your contract term. Unused PTUs don't roll over and aren't refunded or credited, so size your commitment to your expected steady-state traffic.

## Model versions

PTUs are scoped to a specific model or model family. To move your commitment to a different model, work with your sales contact.
