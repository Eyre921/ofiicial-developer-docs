---
title: "Pricing"
source: https://docs.together.ai/docs/inference/pricing
path: docs/inference/pricing
---

How Together AI bills for inference.

Inference billing works differently depending on your deployment mode:

* [Serverless models](/docs/serverless/models) bill based on usage, with no minimums and no provisioning cost.
* [Provisioned throughput](/docs/inference/provisioned-throughput) bills per provisioned throughput unit (PTU) on a reserved term, with a one-month minimum.
* [Dedicated endpoints](/docs/dedicated-endpoints/overview) bill per-minute, depending on the hardware you reserve.

For per-model and per-hardware rates, see [together.ai/pricing](https://together.ai/pricing).

## Serverless models

You pay per unit of work, with units determined by model type:

* **Chat, language, embedding, and rerank:** Per input and output token.
* **Image generation:** Per megapixel of output.
* **Video generation:** Per second of output.
* **Speech-to-text and text-to-speech:** Per second of audio.

Find per-model rates in the [serverless model catalog](/docs/serverless/models).

### Cached input discounts

Select serverless chat models bill cached input tokens at a steep discount. Caching is:

* **Automatic:** There is no header, parameter, or account toggle to enable it. Send the same prompt prefix again and any portion that's still warm in the shared cache is billed at the cached rate.
* **Prefix-based:** Only the longest matching prefix of your input counts as cached. Tokens after the first difference are billed at the standard input rate.
* **Best-effort and short-lived:** The serverless cache is shared across the fleet and entries are evicted as traffic shifts, so cache hits aren't guaranteed and there's no configurable retention window. For predictable cache behavior, use a [dedicated endpoint](/docs/dedicated-endpoints/settings#prompt-caching), where prompt caching is enabled by default and scoped to your own replicas.
* **Limited to supported models:** Only models with a value in the **Cached input pricing** column on [Chat models](/docs/serverless/models#chat-models) support cached input billing. Models without a cached price bill all input tokens at the standard rate.

## Provisioned throughput

You commit to a fixed number of PTUs for a selected model or model family over a reserved term, with a one-month minimum. Each PTU is priced at a flat \$0.05 per minute; how many PTUs you need depends on the model, your traffic shape, and your committed capacity. Input tokens, output tokens, and cached reads consume PTUs at model-specific conversion ratios defined in your contract.

Estimate your requirements with the [pricing calculator](https://www.together.ai/provisioned-throughput), and see [Provisioned throughput](/docs/inference/provisioned-throughput) for details on PTUs and the SLA.

## Dedicated endpoints

You pay per minute for the hardware you reserve, regardless of your model or request volume. Billing starts when the endpoint is running. Provisioning, queuing, and failed deployments are not billed.

See [Dedicated endpoint pricing](/docs/dedicated-endpoints/overview#pricing) for more details.

## Batch processing

When you don't need real-time responses, you can use the [batch processing API](/docs/inference/batch/overview) for a 50% discount when running [selected serverless models](/docs/inference/batch/overview#supported-models). Dedicated endpoints can also run batch jobs, but at full price.
