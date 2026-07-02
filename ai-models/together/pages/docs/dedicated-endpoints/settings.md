---
title: "Endpoint settings"
source: https://docs.together.ai/docs/dedicated-endpoints/settings
path: docs/dedicated-endpoints/settings
---

Configure replica count, hardware, decoding optimizations, and prompt caching on a dedicated endpoint.

This page lists the configuration options you can set when creating or updating a dedicated endpoint.

## Replica count

A replica (also called a *worker*) is an instance of your model running on independent hardware, capable of handling requests in parallel with other replicas.

Increasing the number of replicas on an endpoint improves throughput under high traffic, lowers latency, and provides resiliency if a single replica fails. You can configure the minimum and maximum number of replicas to scale between:

* `min-replicas` determines the minimum number of replicas to keep running. These will never scale down, and will always be available to handle requests.
* `max-replicas` determines the maximum number of replicas to scale up to, allowing you to set a ceiling on cost.

The endpoint scales the minimum and maximum values you choose based on server load.

Configure replicas at create time:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
    --model Qwen/Qwen3.5-9B-FP8 \
    --hardware 1x_nvidia_h100_80gb_sxm \
    --display-name "My endpoint" \
    --min-replicas 1 \
    --max-replicas 3 \
    --wait
  ```
</CodeGroup>

To change replica counts on an existing endpoint, use `update` and pass the endpoint ID:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints update --min-replicas 2 --max-replicas 4 <endpoint_id>
  ```
</CodeGroup>

<Note>
  Both `--min-replicas` and `--max-replicas` must be specified together when updating.
</Note>

For guidance on when to add replicas vs. when to add GPUs per replica, see [Scaling](/docs/dedicated-endpoints/scaling).

## Hardware and GPU count

A hardware configuration ID follows this format:

```text theme={null}
<gpu_count>x_<vendor>_<gpu_type>_<gpu_memory>_<gpu_link>
```

For example: `2x_nvidia_h100_80gb_sxm`

Pass it to the CLI with `--hardware <hardware_id>`. To see what's available for a model:

```shell Shell theme={null}
together endpoints hardware --model <model_id>
```

For guidance on when to choose multi-GPU hardware, see [Scaling](/docs/dedicated-endpoints/scaling).

### Availability zone

If you have specific latency or geographic needs, target an availability zone at create time. Restricting to a zone can limit hardware availability, so don't set this unless you need to.

```shell Shell theme={null}
# List zones
together endpoints availability-zones
```

Pass the zone with `--availability-zone <zone>` on the create command.

## Auto-shutdown

To avoid charges from idle replicas, a dedicated endpoint automatically stops after a period of inactivity. The default is **60 minutes**. Configure the threshold with the `inactive-timeout` parameter on the create command (in minutes). Pass `0` to disable auto-shutdown entirely.

Set the timeout at create time:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints create \
    --model Qwen/Qwen3.5-9B-FP8 \
    --hardware 1x_nvidia_h100_80gb_sxm \
    --display-name "My endpoint" \
    --inactive-timeout 30 \
    --wait
  ```
</CodeGroup>

To change it on an existing endpoint, use `update`:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints update --inactive-timeout 30 <endpoint_id>
  ```
</CodeGroup>

An auto-stopped endpoint isn't deleted. Its configuration is preserved, and you can restart it at any time with `together endpoints start <endpoint_id>`.

## Speculative decoding

Speculative decoding is an optimization that improves average throughput by speculatively predicting future tokens. It usually improves performance, but it can introduce occasional tail-latency spikes that real-time or mission-critical workloads won't tolerate.

By default, speculative decoding is **enabled**. To turn it off, pass the `--no-speculative-decoding` flag to the create command.

## Prompt caching

Prompt caching stores the result of previously executed prompts so the model can return cached responses instead of recomputing. It significantly reduces redundant compute for repeated prefixes.

Prompt caching is **enabled by default** on every dedicated endpoint and cannot be disabled. Because replicas are reserved for you, cached prefixes stay active as long as your endpoint is running. For prompt caching behavior on serverless models, see [Cached input discounts](/docs/inference/pricing#cached-input-discounts).

<Note>
  The `--no-prompt-cache` CLI flag and `disable_prompt_cache` API field are deprecated and will be removed in February 2026. They are currently accepted but ignored; prompt caching is always enabled.
</Note>
