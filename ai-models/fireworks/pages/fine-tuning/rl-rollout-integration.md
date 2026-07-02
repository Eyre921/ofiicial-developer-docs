---
title: "RL Rollouts with Your Own Trainer"
source: https://docs.fireworks.ai/fine-tuning/rl-rollout-integration
path: fine-tuning/rl-rollout-integration
---

Integrate an external RL trainer with Fireworks inference: hot-load new checkpoints from your bucket and run rollouts via the OpenAI-compatible API.

<Warning>
  **Early Access Feature.** External-bucket hot-load for RL rollouts is a
  private preview. [Contact Fireworks](https://fireworks.ai/contact) to enable
  this path on your account before you use `S3`, `MINIO`, `NEBIUS`, or similar
  non-`FW_HOSTED` storage.
</Warning>

<Tip>
  **Using a code agent?** Follow sections in order: [Prerequisites](#prerequisites)
  → [Quickstart checklist](#quickstart-checklist) → [Hot-load API](#hot-load-api).
  Required env: `FIREWORKS_API_KEY`. After your first full snapshot is serving,
  read [Incremental snapshots](/fine-tuning/rl-rollout-delta-checkpoints) before
  production training loops. For active stream, session ID, and `reset_prompt_cache`
  semantics, see [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts).
  For ledger and hot-load status debugging, see [Ledger & debugging](/fine-tuning/rl-rollout-debugging).
</Tip>

This guide is for teams already running their own RL trainer (Megatron, TorchTitan, Slime, Verl, etc) who want Fireworks purely for inference during rollouts. It also covers the raw hot-load API, which Training API users can call directly when they need rollout behaviors beyond what `WeightSyncer` and `DeploymentManager` expose.

Fireworks offers three paths for reinforcement learning, along a spectrum that trades convenience for control:

* **BYOT rollouts** — the most hands-on, for teams already running their own trainer who want Fireworks purely for high-scale rollout inference.
* **Training API** — the middle ground, for teams who want to own their training logic without managing infrastructure.
* **Managed RFT** — the turnkey path, for teams who just want a tuned model without running the loop themselves.

## Where this guide fits

| Path                                                         | You own                                                  | Fireworks owns                                                                    | Use this guide?                                               |
| ------------------------------------------------------------ | -------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **This guide (BYOT rollouts)**                               | Trainer, rewards, environment, checkpoint upload cadence | Hot-load deployment, distributed weight swap, inference, KV cache across rollouts | Yes                                                           |
| [Training API](/fine-tuning/training-api/introduction)       | Training logic (recipes or SDK)                          | GPUs, trainer lifecycle, often `FW_HOSTED` bucket                                 | Only if you need rollout behavior beyond what the SDK exposes |
| [Managed RFT](/fine-tuning/reinforcement-fine-tuning-models) | Dataset and evaluator                                    | End-to-end hosted RL                                                              | No                                                            |

**Why BYOT rollout inference?**

* **Disaggregated:** Your trainer and rollout cluster can run in different regions or clouds; deployments can span multiple regions to pool capacity.
* **Full-parameter scale:** Full (non-LoRA) tuning for large models supported on Fireworks inference shapes.
* **Fast checkpoint transfer:** Lossless compressed incremental snapshots (`arc_v2`, typically 20×+ compression) over standard object storage—no special RDMA networking between trainer and inference.
* **Async / off-policy friendly:** Background download during rollouts; configurable swap semantics similar in spirit to [PipelineRL](https://arxiv.org/pdf/2509.19128)—see [checkpoint-swap behavior](/fine-tuning/rl-rollout-debugging#checkpoint-swap-behavior).

For **Online RL** (live user traffic as rollouts with rolling per-replica updates), the same hot-load infrastructure applies; contact Fireworks for production Online RL setup.

## Placeholders

Reuse these values in every command below:

| Placeholder                            | Example                                                           |
| -------------------------------------- | ----------------------------------------------------------------- |
| `<account_id>`                         | `my-team`                                                         |
| `<model_id>`                           | `qwen3-30b-a3b`                                                   |
| `<deployment_id>`                      | `rl-rollout-prod`                                                 |
| `<fireworks_api_key>`                  | From [API keys](https://app.fireworks.ai/settings/users/api-keys) |
| `<your_bucket>` / `<your_upload_path>` | Parent prefix configured on the deployment (no trailing slash)    |
| `<checkpoint_id>`                      | Snapshot directory name, e.g. `version_001` (no slashes)          |

## Prerequisites

Complete this checklist before creating a deployment:

1. **Fireworks account** and **API key** — [create a key](https://app.fireworks.ai/settings/users/api-keys) and set `export FIREWORKS_API_KEY="<key>"`.
2. **Account ID** — In the [dashboard](https://app.fireworks.ai/), open your account settings or any resource URL; the account slug is the segment after `/accounts/` (for example `accounts/<account_id>/...`).
3. **Feature enablement** — Request **external-bucket hot-load for RL rollouts** on account `<account_id>`, including your bucket provider (`S3`, `GCS`/`gs://`, or `NEBIUS`).
4. **Object storage read access for Fireworks** — Fireworks needs read-only access to the bucket prefix you will pass as `--hot-load-bucket-url`. At enablement, Fireworks shares the IAM principal to grant access. Typical setup:
   * **Amazon S3:** Grant the Fireworks principal `s3:GetObject` (and `s3:ListBucket` on the prefix) on `s3://<your_bucket>/<your_upload_path>/*`.
   * **Google Cloud Storage:** Grant `roles/storage.objectViewer` on the bucket or prefix to the Fireworks service account provided at onboarding.
   * **Nebius / MinIO:** Equivalent read-only credentials or access key scoped to the upload prefix.
5. **`firectl` installed** — See [firectl](/tools-sdks/firectl/firectl).
6. **Base model and deployment shape** — An RL-capable shape for your model (GPU count, precision). If you omit `--deployment-shape`, `firectl` prompts you to pick one interactively.

## Architecture

```mermaid theme={null}
flowchart LR
  trainer["Your RL Trainer"] -->|"1. Upload checkpoint"| bucket[("External bucket")]
  trainer -->|"2. Signal snapshot ready"| api["Fireworks Hot-Load API"]
  api -->|"3. Load weights"| deployment["Inference Deployment"]
  trainer -->|"4. Rollout via /v1/completions"| deployment
  deployment -->|"Tokens + optional routing_matrix"| trainer
```

**You own:** trainer, reward shaping, checkpoint cadence, rollout orchestration.

**Fireworks owns:** hot-load logistics, distributed weight swap, inference serving, KV cache across rollouts.

## End-to-end loop

1. Create a hot-load deployment.
2. Upload and hot-load an initial **full** snapshot.
3. Run rollouts against that snapshot.
4. For each training step: upload and hot-load the next **incremental** snapshot (see [Incremental snapshots](/fine-tuning/rl-rollout-delta-checkpoints)).
5. Run rollouts again.
6. Every 20th or 30th step, publish a **full** snapshot instead of an incremental one. If the incremental chain fails, fall back to a full snapshot.

## Quickstart checklist

Use this table for your **first** rollout end-to-end:

| Step | Action                                                                     | Done when                                                                                   |
| ---- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1    | [Create hot-load deployment](#1-create-a-hot-load-deployment)              | `firectl deployment get <deployment_id>` shows a healthy deployment                         |
| 2    | [Upload full HF snapshot](#2-upload-and-hot-load-an-initial-full-snapshot) | All files exist under `.../<checkpoint_id>/` in object storage                              |
| 3    | `POST` [signal snapshot](#hot-load-api)                                    | HTTP 200                                                                                    |
| 4    | `GET` [poll status](#hot-load-api)                                         | Every replica has `readiness: true` and `current_snapshot_identity` matches your `identity` |
| 5    | [Run rollouts](#3-run-rollouts)                                            | Chat/completions returns tokens                                                             |

## 1. Create a hot-load deployment

Create the deployment that will serve rollouts. During preview, `--enable-hot-load` flags may be hidden from CLI help but can still be passed explicitly.

```bash theme={null}
firectl create deployment accounts/<account_id>/models/<model_id> \
  --deployment-shape <shape_name> \
  --deployment-id <deployment_id> \
  --enable-hot-load \
  --hot-load-bucket-type S3 \
  --hot-load-bucket-url s3://<your_bucket>/<your_upload_path> \
  --hot-load-transition-type ASYNC \
  --region US_OHIO_1
```

<Note>
  **Flags**

  * `--deployment-shape` — Optional. If omitted, `firectl` prompts you to pick one.
  * `--hot-load-bucket-type` — `MINIO`, `S3`, `NEBIUS`, or `FW_HOSTED`. This guide focuses on external buckets (`S3`, `gs://`, etc.). `FW_HOSTED` is for Fireworks-managed trainers.
  * `--hot-load-bucket-url` — Required when `--enable-hot-load` is set. Examples: `s3://mybucket/path`, `gs://mybucket/path`. **No trailing slash.** This is the **parent prefix**; each snapshot is a subdirectory named by `identity` (see [snapshot layout](#snapshot-layout)).
  * `--hot-load-transition-type` — `ASYNC` (recommended for RL) or `SYNC`. Defaults to `ASYNC` when hot load is enabled. See [checkpoint-swap behavior](/fine-tuning/rl-rollout-debugging#checkpoint-swap-behavior).
  * `--region` — Where the deployment runs (for example `US_OHIO_1`, `US_VIRGINIA_1`). Keep the trainer upload path geographically close to the bucket and deployment.
</Note>

Save the **account ID**, **deployment ID**, and **model ID** from the output for hot-load and rollout calls.

If you do not set a shape, the CLI shows a shape picker:

<Frame>
  <img alt="firectl deployment shape picker" />
</Frame>

## 2. Upload and hot-load an initial full snapshot

Upload a full HuggingFace-format checkpoint, then signal Fireworks to load it.

### Snapshot layout

Place each snapshot under its own subdirectory. The `identity` you signal in the API must match the directory name (a single path segment—no slashes):

```
s3://<your_bucket>/<your_upload_path>/<checkpoint_id>/
├── config.json
├── tokenizer.json
├── tokenizer_config.json
├── model-00000.safetensors
├── model-00001.safetensors
└── ...
```

Example with the recommended path pattern:

```
s3://<your_bucket>/<account_id>/<account_id>-<deployment_id>/version_001/
```

* **`identity` / `<checkpoint_id>`** — Any opaque string (for example `version_001` or `step_00100`).
* **Format** — Same layout as the base model on HuggingFace: `config.json`, tokenizer files, and safetensors weights. **No tensor-parallel sharding** in uploaded files.
* **File size** — Split weights into multiple `.safetensors` files, each under about 5 GB. Group weights by layer when possible; putting one layer per file minimizes load time.

Optional: call the [per-file hint API](/fine-tuning/rl-rollout-delta-checkpoints#per-file-hints-optional) as each file lands to speed up loading on large models.

### Signal and poll

Use the [Hot-load API](#hot-load-api) below with `{ "identity": "<checkpoint_id>" }` and poll until all replicas are ready.

## Hot-load API

All hot-load requests use these headers:

| Header                 | Value                                               |
| ---------------------- | --------------------------------------------------- |
| `Authorization`        | `Bearer <fireworks_api_key>`                        |
| `fireworks-model`      | `accounts/<account_id>/models/<model_id>`           |
| `fireworks-deployment` | `accounts/<account_id>/deployments/<deployment_id>` |
| `Content-Type`         | `application/json`                                  |

| Operation                | Method | URL                                                         |
| ------------------------ | ------ | ----------------------------------------------------------- |
| Signal snapshot ready    | `POST` | `https://api.fireworks.ai/hot_load/v1/models/hot_load`      |
| Poll load status         | `GET`  | `https://api.fireworks.ai/hot_load/v1/models/hot_load`      |
| Per-file hint (optional) | `POST` | `https://api.fireworks.ai/hot_load/v1/models/hot_load/hint` |

### Signal snapshot ready

**Full snapshot** body:

```json theme={null}
{ "identity": "version_001" }
```

**Incremental snapshot** bodies, compression, hints, and `checksum_format` are documented in [Incremental snapshots](/fine-tuning/rl-rollout-delta-checkpoints).

<ParamField type="string">
  Snapshot directory name under the configured bucket prefix. Must not contain `/`.
</ParamField>

<ParamField type="object">
  Required for incremental snapshots. Includes `previous_snapshot_identity`, `compression_format` (`arc_v2`), and `checksum_format` (`alder32`). See the incremental snapshots guide.
</ParamField>

<ParamField type="string">
  Prompt-cache policy after the swap: `all` (default), `none`, or `new_session`. See [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts) for active stream, session ID, and reset-option semantics.
</ParamField>

<ParamField type="string[]">
  Top-level `config.json` fields to ignore during snapshot validation. Only use for known-safe metadata fields.
</ParamField>

```bash theme={null}
curl -X POST https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "Content-Type: application/json" \
  -d '{ "identity": "version_001" }'
```

```python theme={null}
import os
import requests

API_KEY = os.environ["FIREWORKS_API_KEY"]
ACCOUNT = "<account_id>"
MODEL = f"accounts/{ACCOUNT}/models/<model_id>"
DEPLOYMENT = f"accounts/{ACCOUNT}/deployments/<deployment_id>"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "fireworks-model": MODEL,
    "fireworks-deployment": DEPLOYMENT,
    "Content-Type": "application/json",
}

resp = requests.post(
    "https://api.fireworks.ai/hot_load/v1/models/hot_load",
    headers=HEADERS,
    json={"identity": "version_001"},
    timeout=60,
)
resp.raise_for_status()
```

### Poll load status

Poll until **every** replica has `readiness: true` and `current_snapshot_identity` equals the `identity` you signaled.

```bash theme={null}
curl https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>"
```

```python theme={null}
status = requests.get(
    "https://api.fireworks.ai/hot_load/v1/models/hot_load",
    headers=HEADERS,
    timeout=30,
).json()

replicas = status.get("replicas", [])
ready = (
    replicas
    and all(r.get("readiness") for r in replicas)
    and all(r.get("current_snapshot_identity") == "version_001" for r in replicas)
)
```

### When to start rollouts

* **Default (on-policy):** Wait until all replicas report readiness on the new `identity`.
* **Off-policy / higher utilization:** You may start sending rollouts when a **subset** of replicas is ready—inspect each entry in `replicas` in the `GET` response. Stale-policy rollouts are expected; use async transition mode and monitor policy version in streaming responses (see [Policy version in responses](/guides/rollout-inference#policy-version-in-responses)).

Per-file hints are optional but recommended for large checkpoints—see [Incremental snapshots](/fine-tuning/rl-rollout-delta-checkpoints#per-file-hints-optional).

## 3. Run rollouts

Call the OpenAI-compatible inference API. For multi-turn RL, set session headers so KV cache stays on one replica:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "x-multi-turn-session-id: <trajectory_id>" \
  -H "x-session-affinity: <trajectory_id>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<account_id>/models/<model_id>",
    "messages": [{"role": "user", "content": "..."}]
  }'
```

See [Inference for RL rollouts](/guides/rollout-inference) for session affinity, weight-swap behavior, MoE Router Replay (R3), and policy-version fields.

## Steady-state training loop

After the first full snapshot:

1. **Intermediate steps** — Build and upload an [incremental snapshot](/fine-tuning/rl-rollout-delta-checkpoints) (`arc_v2`), signal with `incremental_snapshot_metadata`, poll until ready, then run rollouts.
2. **Every 20th or 30th step** — Publish a new **full** snapshot for faster recovery and chain reset.
3. **On failure** — Fall back to a full snapshot; see [Ledger & debugging](/fine-tuning/rl-rollout-debugging).

Brief incremental signal example (full details on the incremental page):

```bash theme={null}
curl -X POST https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "Content-Type: application/json" \
  -d '{
    "identity": "version_002",
    "incremental_snapshot_metadata": {
      "previous_snapshot_identity": "version_001",
      "compression_format": "arc_v2",
      "checksum_format": "alder32"
    }
  }'
```

## Numerics alignment

For best training–inference alignment:

* Match **quantization / precision** between trainer checkpoints and the deployment shape (work with Fireworks if you need a custom shape).
* Measure **logprob divergence** between trainer forward passes and rollout inference on the same tokens.
* For MoE models, use **Router Replay (R3)** during rollouts—see [MoE Router Replay](/guides/rollout-inference#moe-router-replay).

## Next steps

<CardGroup>
  <Card title="Incremental snapshots" icon="layer-group" href="/fine-tuning/rl-rollout-delta-checkpoints">
    Build ARC2 deltas, per-file hints, and incremental signal bodies.
  </Card>

  <Card title="Ledger & debugging" icon="bug" href="/fine-tuning/rl-rollout-debugging">
    Inspect snapshot history, reset the ledger, and reason about request behavior during weight swaps.
  </Card>

  <Card title="Inference for RL rollouts" icon="bolt" href="/guides/rollout-inference">
    Session affinity headers, policy version in streams, weight-swap behavior, and MoE Router Replay (R3).
  </Card>

  <Card title="Fireworks-hosted trainer" icon="flask" href="/fine-tuning/training-api/introduction">
    The alternative path where Fireworks runs the trainer through the Training API.
  </Card>
</CardGroup>
