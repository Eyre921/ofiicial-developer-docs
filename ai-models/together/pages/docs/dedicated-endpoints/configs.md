---
title: "Choose a deployment profile"
source: https://docs.together.ai/docs/dedicated-endpoints/configs
path: docs/dedicated-endpoints/configs
---

Pick the hardware deployment profile that your model runs on.

After [choosing](/docs/dedicated-endpoints/models) or [uploading](/docs/dedicated-endpoints/custom-models) a model, you choose a [deployment profile](/docs/dedicated-endpoints/concepts#deployment-profile): the certified pairing of a model weight (at a given quantization) with a [config](/docs/dedicated-endpoints/concepts#config) that fixes the quantization, parallelism, and hardware your deployment runs on.

Together publishes one or more profiles per model. You select one by its config revision ID, passing it to `--config <cr_...>` when you create a deployment. When a model has a single profile, the CLI selects it automatically.

## List a model's profiles

Each profile is anchored by a config revision (`cr_...`). List the configs published for a model with the CLI, passing a model ID (`ml_...`) or a model name. For a public-catalog model, the [supported-models catalog](/docs/dedicated-endpoints/models#list-supported-models-programmatically) also shows each profile's quantization alongside its config:

```bash CLI theme={null}
tg beta models configs ml_CbJNwQC2ZqCU2iFT3mrCh
tg beta models configs Qwen/Qwen3.5-9B
```

Response example:

```json theme={null}
{
  "data": [
    {
      "id": "cr_CbeuemXsU8yGStQvBBEgY",
      "referenceModel": "projects/proj_weights/models/ml_CbJ9yCnij7A47b1xkpioB",
      "referenceModelId": "ml_CbJ9yCnij7A47b1xkpioB",
      "projectId": "proj_abc123",
      "selectors": [
        { "key": "accelerator_count", "value": "1" },
        { "key": "accelerator_type", "value": "nvidia-h100-80gb" },
        { "key": "optimization", "value": "balanced" },
        { "key": "topology", "value": "aggregated" }
      ]
    }
  ],
  "object": "list"
}
```

List and get responses return `referenceModel`, the model's resource name.

The config `id` is a config revision in the format `cr_...`. Pass it as a resource name (`projects/{project_id}/configs/{config_revision_id}`) in the `config` field when you [create a deployment](/docs/dedicated-endpoints/manage#create-a-deployment). Use the config's `projectId` from the list response for `{project_id}`.

Use this command when you already have a model, including your own [uploaded fine-tuned models](/docs/dedicated-endpoints/custom-models), which aren't in the public catalog. To browse the public catalog and get certified model-and-config pairs in one call, see [List supported models programmatically](/docs/dedicated-endpoints/models#list-supported-models-programmatically).

## Selectors

Every config carries a set of selectors that describe the hardware and serving setup:

| Selector            | Description                            | Example                             |
| ------------------- | -------------------------------------- | ----------------------------------- |
| `accelerator_type`  | The GPU SKU the config targets.        | `nvidia-h100-80gb`                  |
| `accelerator_count` | Number of GPUs each replica uses.      | `1`, `2`, `4`, `8`                  |
| `optimization`      | The serving profile.                   | `balanced`, `throughput`, `latency` |
| `topology`          | How the model is laid out across GPUs. | `aggregated`                        |

A model may have more than one published profile, for example a single-GPU profile and a multi-GPU profile at a higher price and throughput.

## Instance types and capacity

A config's `accelerator_type` and `accelerator_count` selectors map to a deployable [instance type](/docs/dedicated-endpoints/concepts#instance-type), the unit of hardware you pay for while replicas run. For example, `accelerator_type: nvidia-h100-80gb` with `accelerator_count: 1` maps to the instance type `1xnvidia-h100-80gb`.

To see an instance type's per-hour price and per-region capacity, query the public instance-types endpoint:

```bash Shell theme={null}
curl -s -H "Authorization: Bearer $TOGETHER_API_KEY" \
  https://api.together.ai/v2/public/inference-instance-types
```

Each instance type lists its `regions`, and each region reports `headroom`, a best-effort hint of how many more replicas of that instance type currently fit. A `headroom` value of N with the `RELATION_GTE` relation means at least N units are free in that region, and the true number may be higher. Use it to pick a region with capacity before you deploy. For the per-hour price of each instance type, see [Pricing](/docs/dedicated-endpoints/pricing#supported-hardware).

## Pick a profile

To pick a profile, match it to your workload requirements:

* **Single-GPU, balanced:** A good default for most models. Lowest cost per replica.
* **Multi-GPU:** Higher throughput and lower latency for large models or heavy traffic, at a higher per-replica price.
* **Latency-optimized:** When time to first token matters more than aggregate throughput.

Quantization, hardware, and GPU count are set by the profile you choose, so they're fixed for the life of a deployment. To run a model on a different profile, [create a new deployment](/docs/dedicated-endpoints/manage#create-a-deployment) with a different config and [shift traffic](/docs/dedicated-endpoints/route-traffic) over to it.

<Note>
  Configs are immutable. Together publishes new revisions over time, each with a new `cr_...` ID. A deployment pins the revision you selected, so its hardware and engine don't change underneath you.
</Note>

## Decoding optimizations

Decoding optimizations such as speculative decoding are defined in the config you select. The config's `optimization` selector (for example `balanced`, `throughput`, or `latency`) sets the serving profile, and configs that enable speculative decoding declare a draft model.

When you [create a deployment](/docs/dedicated-endpoints/manage#create-a-deployment), Together derives the speculator from the config's declared draft model and pins it at creation time. You cannot set a speculator on the deployment yourself.

### Speculative decoding

Speculative decoding raises average throughput by predicting future tokens ahead of time. It usually improves performance, but it can introduce occasional tail-latency spikes that strict real-time workloads won't tolerate. If your workload is latency-sensitive, choose a config with a latency-oriented optimization profile.

When a config declares a speculative-decoding draft, list and get responses include `draftModel`, the resource name of the draft model (`projects/{project_id}/models/{model_id}`). Configs without speculative decoding omit this field.

## Next steps

<CardGroup>
  <Card title="Create a deployment" icon="layers-intersect" href="/docs/dedicated-endpoints/manage#create-a-deployment">
    Bind a model and config to an endpoint.
  </Card>

  <Card title="Configure autoscaling" icon="arrows-maximize" href="/docs/dedicated-endpoints/scaling">
    Choose replica bounds and an autoscaling metric.
  </Card>
</CardGroup>
