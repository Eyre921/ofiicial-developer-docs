---
title: "Overview"
source: https://docs.together.ai/docs/dedicated-endpoints/overview
path: docs/dedicated-endpoints/overview
---

Reserved-hardware inference endpoints with predictable performance, no shared rate limits, and per-endpoint configuration.

<Tip>
  Using a coding agent? Install the [together-dedicated-endpoints](/docs/agent-skills) skill to let your agent create and manage dedicated endpoints for you.
</Tip>

A dedicated endpoint serves a single model on hardware reserved only for you, offering predictable latency and no [shared-fleet rate limits](/docs/serverless/rate-limits). They are highly configurable, allowing you to upload custom fine-tuned models, and configure autoscaling and decoding optimizations to match your workload.

Dedicated endpoints use the same [inference APIs](/docs/inference/overview#shared-inference-api) as [serverless models](/docs/serverless/models), allowing you to prototype with serverless, then switch to dedicated endpoints without changing your application code.

## Get started

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/dedicated-endpoints/quickstart">
    Deploy and call your first endpoint in 5 minutes.
  </Card>

  <Card title="Manage endpoints" icon="tool" href="/docs/dedicated-endpoints/manage">
    Create, start, stop, update, and delete via the UI or API.
  </Card>

  <Card title="Endpoint settings" icon="adjustments-horizontal" href="/docs/dedicated-endpoints/settings">
    Configure endpoint hardware, autoscaling, decoding, prompt caching.
  </Card>

  <Card title="Inference APIs" icon="code" href="/docs/inference/overview">
    Explore the API surface for chat, vision, audio, embeddings, and more.
  </Card>

  <Card title="Available models" icon="list" href="/docs/dedicated-endpoints/models">
    Browse Together-hosted models you can deploy on dedicated endpoints.
  </Card>

  <Card title="Upload a custom model" icon="upload" href="/docs/dedicated-endpoints/custom-models">
    Upload your own model weights.
  </Card>
</CardGroup>

## Pricing

Dedicated endpoints bill per-minute by hardware while the endpoint is running, regardless of your model or request volume.

The following table lists the single-GPU price for each hardware type.

| GPU            | Hardware ID                | Cost/hour |
| -------------- | -------------------------- | --------- |
| H100 80GB SXM  | `1x_nvidia_h100_80gb_sxm`  | \$5.40    |
| H200 140GB SXM | `1x_nvidia_h200_140gb_sxm` | \$6.60    |
| B200 180GB SXM | `1x_nvidia_b200_180gb_sxm` | \$9.00    |

### Scaling out

You can deploy [multiple autoscaling replicas](/docs/dedicated-endpoints/settings#replica-count) of your model on a single endpoint to reduce latency under high traffic and provide resiliency in case a single replica fails. Each running replica bills independently, and stops billing as soon as it is [scaled down](/docs/dedicated-endpoints/scaling).

You can also deploy multiple GPUs per replica (2, 4, or 8 GPUs) to increase throughput and lower latency. Cost scales with the GPU count, and the hardware ID carries a matching prefix—for example, the ID for four H100s is `4x_nvidia_h100_80gb_sxm`.

<Tip>
  For best practices on when to increase replicas vs. GPUs per replica, see [Vertical vs. horizontal scaling](/docs/dedicated-endpoints/scaling#vertical-vs-horizontal).
</Tip>

### List hardware options

To get a list of available hardware options, GPU counts, and per-minute rates for a given model, run this command:

```bash theme={null}
tg endpoints hardware --model <MODEL_ID>
```
