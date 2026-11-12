---
title: "Deployments"
source: https://docs.fireworks.ai/guides/ondemand-deployments
path: guides/ondemand-deployments
---

Create and manage on-demand Fireworks deployments on dedicated GPUs: choose accelerator shapes, autoscaling, replicas, and lifecycle controls for production.

> [!NOTE]
>
> **New to deployments?** Start with our [Deployments Quickstart](/getting-started/ondemand-quickstart) to deploy and query your first model in minutes, then return here to learn about configuration options.

On-demand deployments give you dedicated GPUs for your models, providing several advantages over serverless:

* **Better performance** – Lower latency, higher throughput, and predictable performance unaffected by other users
* **No hard rate limits** – Only limited by your deployment's capacity
* **Cost-effective at scale** – Cheaper under high utilization. Unlike serverless models (billed per token), on-demand deployments are [billed by GPU-second](https://fireworks.ai/pricing).
* **Broader model selection** – Access models not available on serverless
* **Custom models** – Upload your own models (for supported architectures) from Hugging Face or elsewhere

Need higher GPU quotas or want to reserve capacity? [Contact us](https://fireworks.ai/contact).

## Creating & querying deployments

**Create a deployment:**

```bash theme={null}
# This command returns your accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID> - save it for querying
firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
  --deployment-shape default \
  --wait
```

`--deployment-shape default` has Fireworks pick a validated shape for the model — see [Letting Fireworks pick a shape](#letting-fireworks-pick-a-shape). To choose a shape yourself, run `firectl deployment-shape-version match --model <model-id>` first and pass a shape's name to `--deployment-shape`.

> [!WARNING]
>
> **Deployment placement (`--region`) must be set at creation time and cannot be changed in place.**
>
> If you do not specify `--region`, the deployment uses the `GLOBAL` multi-region: Fireworks can place its replicas in any region and move waiting replicas to another region when capacity frees up there. To limit where it runs, set `--region` to a multi-region or a single region:
>
> ```bash theme={null}
> firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
>   --deployment-shape default \
>   --region GLOBAL   # recommended default
> firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
>   --deployment-shape default \
>   --region US
> firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
>   --deployment-shape default \
>   --region CANADA
> firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
>   --deployment-shape default \
>   --region EUROPE
> firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
>   --deployment-shape default \
>   --region APAC
> ```
>
> Only **GLOBAL** is available by default. Quota for **US**, **CANADA**, **EUROPE**, **APAC**, and single regions must be granted by Fireworks — [contact us](https://fireworks.ai/contact). Deploying with a region you have no quota for is rejected at creation. See [Regions](/deployments/regions#quotas) for details.

### Check current placement

```bash theme={null}
firectl deployment get <DEPLOYMENT_ID>
```

The deployment metadata shows where the deployment is currently allowed to schedule replicas (placement / region configuration).

### Change placement

There is no supported command to change region placement on an existing deployment. To change placement, recreate the deployment:

```bash theme={null}
# 1. Create replacement with correct region
firectl deployment create accounts/fireworks/models/<MODEL_NAME> \
  --deployment-shape default \
  --region GLOBAL \
  --min-replica-count 1

# 2. Verify it's healthy, then point your app at the new endpoint

# 3. Delete old deployment
firectl deployment delete <OLD_DEPLOYMENT_ID>
```

See [Regions](/deployments/regions) for mega-regions and hardware availability.

See [Deployment shapes](#deployment-shapes) below to optimize for speed, throughput, or cost.

**Query your deployment:**

After creating a deployment, query it using this format:

```
accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>
```

> [!TIP]
>
> You can find your deployment name anytime with `firectl deployment list` and `firectl deployment get <DEPLOYMENT_ID>`.

**Example:**

```
accounts/alice/deployments/12345678
```

### Code examples

> [tab] Python (Fireworks SDK)
>
> ```python theme={null}
> from fireworks import Fireworks
>
> client = Fireworks()
>
> response = client.chat.completions.create(
>   model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
>   messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
> )
>
> print(response.choices[0].message.content)
> ```

> [tab] Python (OpenAI SDK)
>
> ```python theme={null}
> import os
> from openai import OpenAI
>
> client = OpenAI(
>     api_key=os.environ.get("FIREWORKS_API_KEY"),
>     base_url="https://api.fireworks.ai/inference/v1"
> )
>
> response = client.chat.completions.create(
>     model="accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
>     messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
> )
>
> print(response.choices[0].message.content)
> ```

> [tab] JavaScript
>
> ```javascript theme={null}
> import OpenAI from "openai";
>
> const client = new OpenAI({
>   apiKey: process.env.FIREWORKS_API_KEY,
>   baseURL: "https://api.fireworks.ai/inference/v1",
> });
>
> const response = await client.chat.completions.create({
>   model: "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
>   messages: [
>     {
>       role: "user",
>       content: "Explain quantum computing in simple terms",
>     },
>   ],
> });
>
> console.log(response.choices[0].message.content);
> ```

> [tab] curl
>
> ```bash theme={null}
> curl https://api.fireworks.ai/inference/v1/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $FIREWORKS_API_KEY" \
>   -d '{
>     "model": "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
>     "messages": [
>       {
>         "role": "user",
>         "content": "Explain quantum computing in simple terms"
>       }
>     ]
>   }'
> ```

### Deployment status states

Deployment states from the Gateway API spec:

* `CREATING` - still being created
* `READY` - ready to be used
* `UPDATING` - in-progress updates happening
* `DELETING` - being deleted
* `DELETED` - soft-deleted
* `FAILED` - creation failed (see status for details)

UI-only states are display labels derived from deployment fields:

* `Inactive`: `state == READY && max_replica_count == 0 && ready_replica_count == 0`
* `Scaled to 0`: `state == READY && min_replica_count == 0 && max_replica_count > 0 && desired_replica_count == 0 && ready_replica_count == 0`

These are display labels computed from deployment fields; they are not new backend `Deployment.State` enum values.

## Deployment shapes

Deployment shapes are the primary way to configure deployments. They're pre-configured templates optimized for speed, cost, or efficiency, including hardware, quantization, and other [performance factors](/deployments/benchmarking). Every shape is validated by Fireworks, so a deployment created from a shape uses a known-good configuration of GPU count, precision, and serving parameters.

> [!WARNING]
>
> **Do not create deployments without a shape.** Always pass `--deployment-shape` — a concrete shape, or `default` to have Fireworks pick one. Deployments created without a shape skip these validation checks — mistakes like a GPU count that can't fit the model surface only at creation, where they cause failures. Most failed deployment creations on Fireworks are deployments without a shape. Enforcement is coming soon: shapeless creation will then require an explicit opt-in — see [Explicitly creating a deployment without a shape](#explicitly-creating-a-deployment-without-a-shape-advanced-users-only). If no shape fits your workload, [contact us](https://fireworks.ai/contact) and we'll help you find or add one.

Over the API, `deploymentShape` also accepts the special value `default`: the server picks a validated shape for the model for you — pass `--deployment-shape default` with firectl. For details, see [Letting Fireworks pick a shape](#letting-fireworks-pick-a-shape).

* **Fast** – Low latency for interactive workloads
* **Throughput** – Cost-per-token at scale for high-volume workloads
* **Minimal** – Lowest cost for testing or light workloads

**Usage:**

```bash theme={null}
# Let Fireworks pick a validated shape
firectl deployment create accounts/fireworks/models/deepseek-v3 --deployment-shape default

# Or match available shapes (the deployable set for your account) and choose one
firectl deployment-shape-version match --model <model-id>

# Create with a shape (shorthand)
firectl deployment create accounts/fireworks/models/deepseek-v3 --deployment-shape throughput
```

> [!NOTE]
>
> `match` reports the deployable set. Shapes your account cannot deploy on are dropped, exact base-model matches are preferred over same-model-type and parameter-count siblings, and LoRA addon and live-merge models are matched against their base model. Over the API, the equivalent is [Match Deployment Shape Versions](/api-reference/match-deployment-shape-versions). To see every validated shape matching a base model instead (including ones your account cannot use), use `firectl deployment-shape-version list --base-model <model-id>` — base models only, it fails on LoRA addon and live-merge models. `match` does not take addons into account. For a deployment with `--enable-addons`, use the [Match Deployment Shape Versions](/api-reference/match-deployment-shape-versions) API with `enableAddons` set.

```bash theme={null}
# Create with full shape ID
firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
  --deployment-shape accounts/fireworks/deploymentShapes/llama-v3p3-70b-instruct-fast

# View shape details
firectl deployment-shape-version get <full-deployment-shape-version-id>
```

### Letting Fireworks pick a shape

Every client surface accepts a special value that has the server pick a validated shape for the model and apply it, the same as passing that shape explicitly:

> [tab] firectl
>
> ```bash theme={null}
> firectl deployment create accounts/fireworks/models/gpt-oss-120b \
>   --deployment-shape default
> ```

> [tab] REST API
>
> Pass `"default"` as `deploymentShape`:
>
> ```bash theme={null}
> curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deployments" \
>   -H "Authorization: Bearer $FIREWORKS_API_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "baseModel": "accounts/fireworks/models/gpt-oss-120b",
>     "deploymentShape": "default"
>   }'
> ```

> [tab] Python SDK
>
> ```python theme={null}
> from fireworks import Fireworks
>
> client = Fireworks()
> client.deployments.create(
>     account_id="YOUR_ACCOUNT_ID",
>     base_model="accounts/fireworks/models/gpt-oss-120b",
>     deployment_shape="default",
> )
> ```

The pick never silently overrides fields you set. If every compatible shape conflicts with fields in your request (for example an `acceleratorType` no shape validates), the request fails with an error naming the conflicting fields, the compatible shapes, and how to create the deployment without a shape. If no shape is compatible with the model at all, the request also fails — in that case, [contact us](https://fireworks.ai/contact) and we'll help you find or add one.

### Explicitly creating a deployment without a shape (advanced users only)

Every surface accepts an explicit opt-out that creates the deployment without a shape. Setting it together with a shape is an error — a deployment is either shaped or explicitly shapeless.

> [tab] firectl
>
> ```bash theme={null}
> firectl deployment create accounts/fireworks/models/gpt-oss-120b \
>   --accept-shapeless-risk
> ```

> [tab] REST API
>
> Pass `acceptShapelessRisk=true` as a query parameter:
>
> ```bash theme={null}
> curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deployments?acceptShapelessRisk=true" \
>   -H "Authorization: Bearer $FIREWORKS_API_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "baseModel": "accounts/fireworks/models/gpt-oss-120b"
>   }'
> ```

> [tab] Python SDK
>
> ```python theme={null}
> from fireworks import Fireworks
>
> client = Fireworks()
> client.deployments.create(
>     account_id="YOUR_ACCOUNT_ID",
>     base_model="accounts/fireworks/models/gpt-oss-120b",
>     accept_shapeless_risk=True,
> )
> ```

> [!WARNING]
>
> Deployments created this way skip shape validation and are far more likely to fail at creation — most failed deployment creations on Fireworks are shapeless deployments. Only use the opt-out when you have a specific reason no shape covers, and [contact us](https://fireworks.ai/contact) so we can help. Enforcement is coming soon: shapeless creation will then *require* this flag, so use a shape (or `default`) now unless you deliberately need this path.

> [!TIP]
>
> Need even better performance with tailored optimizations? [Contact our team](https://fireworks.ai/contact).

## Managing & configuring deployments

### Basic management

```bash theme={null}
# List all deployments
firectl deployment list

# Check deployment status
firectl deployment get <DEPLOYMENT_ID>

# Delete a deployment
firectl deployment delete <DEPLOYMENT_ID>
```

Use [deployment tags](/deployments/deployment-tags) to attach customer-defined metadata such as an environment, team, or workload.

> [!NOTE]
>
> By default, deployments scale to zero if unused for 1 hour. Deployments with min replicas set to 0 are automatically deleted after 7 days of no traffic.

> [!WARNING]
>
> When a deployment is scaled to zero, requests return a `503` error immediately while the deployment scales up. Your application should implement retry logic to handle this. See [Scaling from zero behavior](/deployments/autoscaling#scaling-from-zero-behavior) for implementation details.

### GPU hardware

> [!WARNING]
>
> **Do not create deployments without a shape.** If a [deployment shape](#deployment-shapes) fits your workload, use it — this section only applies when no shape fits. Creating a deployment without a shape (not passing `--deployment-shape`) skips validation: most failed deployment creations on Fireworks are deployments without a shape, and shapeless creation will soon require an explicit opt-in. If you need a configuration no shape covers, [contact us](https://fireworks.ai/contact) and we'll help you find or add one.

Choose GPU type with `--accelerator-type`:

* `NVIDIA_A100_80GB`
* `NVIDIA_H100_80GB`
* `NVIDIA_H200_141GB`
* `NVIDIA_B200_180GB`
* `NVIDIA_B300_288GB`
* `AMD_MI325X_256GB`
* `AMD_MI350X_288GB`

GPU availability varies by [region](/deployments/regions). See the [Create Deployment API reference](/api-reference/create-deployment#body-accelerator-type) for the authoritative list of supported accelerator types.

> [!NOTE]
>
> **Not every model runs on every GPU.** Each model is validated only on specific accelerator type, GPU count, and precision combinations — many models support just one or two entries from the list above. To see what a model supports, match its deployment shapes:
>
> ```bash theme={null}
> firectl deployment-shape-version match --model accounts/fireworks/models/<MODEL_NAME>
> ```
>
> The `GPUS`, `ACCELERATOR`, and `PRECISION` columns are the validated combinations; the model's page in the [Fireworks console](https://app.fireworks.ai) shows the same options under dedicated deployments. Setting `--accelerator-type` or `--accelerator-count` to a combination no shape validates will typically fail at creation — often with a generic `Internal error occurred` message that does not name the hardware mismatch. If you need hardware no shape covers, [contact us](https://fireworks.ai/contact).

### Autoscaling

Control replica counts, scale timing, and load targets for your deployment.

See the [Autoscaling guide](/deployments/autoscaling) for configuration options.

### Multiple GPUs per replica

Use multiple GPUs to improve latency and throughput. First check whether a multi-GPU [deployment shape](#deployment-shapes) already exists for your model:

```bash theme={null}
firectl deployment-shape-version match --model <MODEL_NAME>
```

If no multi-GPU shape fits, start from the closest shape and override the GPU count with `--accelerator-count` — see the warning under [GPU hardware](#gpu-hardware) for why omitting `--deployment-shape` entirely should be a last resort:

```bash theme={null}
firectl deployment create <MODEL_NAME> \
  --deployment-shape <SHAPE_NAME> \
  --accelerator-count 2
```

More GPUs = faster generation. Note that scaling is sub-linear (2x GPUs ≠ 2x performance).

## Preemptible deployments (eval / batch)

A preemptible deployment borrows idle reserved GPUs. It serves the same API as any other deployment, but Fireworks can take the GPUs back at any time, so use it only for evals and bulk offline work whose client retries failed requests. For the training eval workflow, see [Evaluating Trained Models](/fine-tuning/evaluating-fine-tuned-models).

> [!NOTE]
>
> **Moving off Batch inference?** Batch is paused and accepts no new jobs, and Fireworks will permanently delete stored Batch input datasets and job outputs. To run your Batch input files on a preemptible deployment, follow [Migrating Batch API workloads to preemptible deployments](/guides/batch-migration). It includes a migration script that handles concurrency, retries and resume.

> [!WARNING]
>
> A replica can be preempted mid-request without warning. Never send production or latency-sensitive traffic to a preemptible deployment.

### Preemptible vs. on-demand

| | Preemptible (`preemptible: true`) | On-demand |
| - | - | - |
| **Capacity** | Borrows idle reserved GPUs at low priority; can be reclaimed at any time | GPUs held for your deployment once scheduled |
| **Price** | 50% off the on-demand GPU rate, billed per GPU-second as "Preemptible deployment GPU-hours" | On-demand GPU rate, billed per GPU-second |
| **GPU quota** | Separate account-wide quota per accelerator (`preemptible-<accelerator>-count`) | Regular quota per accelerator and placement |
| **Use for** | Evals, bulk offline jobs, one-off runs | Production and interactive serving |

Preemptible capacity is no harder to get than on-demand capacity: if a preemptible deployment can't be placed, an on-demand one can't either. The difference is that a preemptible replica can also lose its GPUs after it starts.

### When to use it

| Option | Choose it when |
| - | - |
| [Serverless](/serverless/overview) | The model is on serverless and per-token pricing with shared rate limits fits your volume. |
| Preemptible deployment | You run bulk or offline work (evals, dataset generation, former Batch jobs), or the model isn't on serverless, such as a fine-tuned model, and your client can retry and resume. |
| On-demand deployment | Traffic is production or latency-sensitive and must not be interrupted. |

### Create a preemptible deployment

Set `preemptible` at creation. You can't change it later; to switch, delete the deployment and create a new one.

Pass an explicit deployment shape. `default` can pick costlier hardware than you expect. List the shapes your account can use for the model:

```bash theme={null}
firectl deployment-shape-version match --model accounts/fireworks/models/<MODEL> -a <ACCOUNT_ID>
```

> [tab] firectl
>
> ```bash theme={null}
> firectl deployment create accounts/fireworks/models/<MODEL> \
>   -a <ACCOUNT_ID> \
>   --deployment-id <NAME> --display-name <NAME> \
>   --deployment-shape <DEPLOYMENT_SHAPE> \
>   --min-replica-count 1 --max-replica-count 1 \
>   --preemptible --wait
> ```
>
> `--wait` blocks until the deployment is ready, for up to 1 hour by default (`--wait-timeout` changes it).
>
> You need `firectl` 1.7.26 or newer; older builds ignore `--preemptible` and create an on-demand deployment. Run `firectl version` to check. Some versions hide the flag from `--help` but still accept it.

> [tab] REST API
>
> ```bash theme={null}
> curl -X POST "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/deployments?deploymentId=<NAME>" \
>   -H "Authorization: Bearer $FIREWORKS_API_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "baseModel": "accounts/fireworks/models/<MODEL>",
>     "deploymentShape": "<DEPLOYMENT_SHAPE>",
>     "minReplicaCount": 1,
>     "maxReplicaCount": 1,
>     "preemptible": true
>   }'
> ```
>
> Get `<DEPLOYMENT_SHAPE>` from `deployment-shape-version match` or the [Match Deployment Shape Versions](/api-reference/match-deployment-shape-versions) API.

Check status with `firectl deployment get <NAME> -a <ACCOUNT_ID>`, then send requests as you would to any deployment. Delete the deployment when the job finishes, to stop billing:

```bash theme={null}
firectl deployment delete <NAME> -a <ACCOUNT_ID>
```

### GPU quota

Preemptible deployments have their own GPU quota, separate from on-demand. Each accelerator type has one account-wide quota, `preemptible-<accelerator>-count`. It counts max replica count times GPUs per replica across your preemptible deployments that aren't deleted or failed.

```bash theme={null}
firectl quota get preemptible-h100-count
```

A create over the quota fails with `RESOURCE_EXHAUSTED` and names the quota. For defaults and increases, see [Account quotas](/guides/quotas_usage/account-quotas#preemptible-deployment-quotas).

### Placement: partial and cross-region

Fireworks places each replica on its own. If you ask for 20 replicas and 8 fit, those 8 start serving while the other 12 wait. The deployment shows `PARTIAL_READY` until every replica is ready, then `READY`, and its status message reports progress, for example `no available capacity for NVIDIA_H100_80GB x8 (placed 8 of 20 replicas)`. Fireworks keeps retrying the rest and doesn't fail the deployment for waiting on capacity.

Without `--region`, or with a multi-region such as `GLOBAL` or `US`, replicas can land in different regions of that placement, and requests are routed across all of them. If replicas wait more than about 5 minutes and another region in the placement has room for all of them, Fireworks can move them there, both at creation and after a preemption. To keep every replica in one region, set `--region` to a single region. See [Regions](/deployments/regions).

### What happens when a replica is preempted

Fireworks reclaims a replica when the workload that reserved its GPUs needs them back. This can happen at any time, mid-request, with no notice.

* Requests in flight on that replica fail. Other ready replicas keep serving.
* Fireworks recreates the replica, and it restarts when GPUs free up, possibly in another region. If 10 of 20 replicas are preempted, the other 10 keep serving while the 10 wait. Fireworks doesn't guarantee how long the wait is.
* The deployment's state doesn't change, and you don't need to recreate it. If every replica is preempted, requests fail until one is ready again. To see how many replicas are serving, check `replicaStats.readyReplicaCount` in `firectl deployment get <NAME> -a <ACCOUNT_ID> -o json` or the [Get Deployment](/api-reference/get-deployment) response.

### How you are notified

Each preempted replica adds an event to the deployment's activity log, in the dashboard and in `firectl deployment events list`: "Replica preempted to free capacity; it will restart when capacity is available". Rollouts, scale-downs and other restarts don't add this event.

If preemption leaves no replica ready, the deployment's creator gets an email, and a second one when the deployment can serve again. A partial preemption sends no email.

### Your responsibilities

Your client must handle replicas disappearing:

* Retry connection errors, HTTP 5xx and 429 with exponential backoff and jitter. Expect bursts of failures while a replica restarts, and longer gaps if every replica was preempted.
* Give each input a stable ID and write each result once under that ID, so a retry doesn't create a duplicate.
* Record finished inputs as results arrive, so you can resume from the rest after an interruption.
* Set an overall deadline. If no replica is ready for longer than you can wait, delete the deployment and retry later, or move the work to on-demand or serverless.

## Advanced

* **[Speculative decoding](/deployments/speculative-decoding)** - Speed up text generation using draft models or n-gram speculation
* **[Quantization](/models/quantization)** - Reduce model precision (e.g., FP16 to FP8) to improve speeds and reduce costs by 30-50%
* **[Performance benchmarking](/deployments/benchmarking)** - Measure and optimize your deployment's performance with load testing
* **[Managing default deployments](/deployments/managing-default-deployments)** - Control which deployment handles queries when using just the model name
* **[Publishing deployments](/deployments/publishing-deployments)** - Make your deployment accessible to other Fireworks users

## Next steps

> [card] [Autoscaling](/deployments/autoscaling)
>
> Configure autoscaling for optimal cost and performance

> [card] [Upload custom models](/models/uploading-custom-models)
>
> Deploy your own models from Hugging Face

> [card] [Quantization](/models/quantization)
>
> Reduce costs with model quantization

> [card] [Regions](/deployments/regions)
>
> Choose deployment regions for optimal latency

> [card] [Reserved capacity](/deployments/reservations)
>
> Purchase reserved GPUs for guaranteed capacity

> [card] [Training](/fine-tuning/finetuning-intro)
>
> Train models for your specific use case
