---
title: "Serverless Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/serverless
path: fine-tuning/training-api/serverless
---

Run LoRA fine-tuning, preference optimization, and RL on a shared pooled trainer, with no provisioning and per-token pricing.

<Info>
  Serverless training is currently in **private preview** and access is gated per account. [Request access](https://fireworks.ai/contact-training) and select "Serverless Training API."
</Info>

Serverless training connects to a shared, already-running pooled trainer through the gateway and returns training and sampling clients. There is no trainer job or inference deployment to provision or delete. Close each sampler and the service client when finished.

Not sure whether the shared pool fits your workload? [Compare serverless and dedicated training](/fine-tuning/training-api/introduction#infrastructure).

<Info>
  **What you need**

  * **Install the SDK** (same one as the dedicated path, no separate console flow): `pip install "fireworks-ai[training]"`
  * **For the runnable example, clone the cookbook:** `git clone https://github.com/fw-ai/cookbook && pip install -e ./cookbook/training`
  * **Point at the serverless endpoint:** `base_url="https://api.fireworks.ai/training/v1/serverless"`
  * **Pick a base model enabled for serverless training on your account.** See [Models](#models) below. Availability changes during private preview; verify it before launch.
  * Set your API key and run the [Quickstart](#quickstart) below.
</Info>

<Tip>
  **Using a code agent?** Start with the self-contained [`serverless_rl` Countdown example](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl), or fork the experimental [`async_rl_loop_serverless` recipe](https://github.com/fw-ai/cookbook/blob/main/training/recipes/experiment/async_rl_loop_serverless.py) when you need rollout functions, rollout/training overlap, or agentic trajectories. Both run against the serverless gateway.
</Tip>

## What is serverless training?

You write the training loop, for supervised fine-tuning, preference optimization, or reinforcement learning, and Fireworks runs the forward pass, backward pass, and optimizer on remote GPUs, then serves your latest weights for sampling in the same session.

The [quickstart](#quickstart) shows the exact client setup and operation order. The cookbook provides a compact [`serverless_rl` implementation](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl) and an experimental [`async_rl_loop_serverless` recipe](https://github.com/fw-ai/cookbook/blob/main/training/recipes/experiment/async_rl_loop_serverless.py) with the same rollout contract as the dedicated async RL recipe.

### Serverless lifecycle

<div aria-label="Serverless Training lifecycle using shared pooled training and sampling infrastructure">
  <div>
    <div>1 · Local</div>
    <strong>Your Python loop</strong>
    <div>Builds batches, rewards, and optimizer requests.</div>
  </div>

  <div>
    <div>2 · Shared</div>
    <strong>Pooled trainer</strong>
    <div>Runs remote LoRA forward, backward, and optimizer work.</div>
  </div>

  <div>
    <div>3 · In session</div>
    <strong>Sampler snapshot</strong>
    <div>Captures the current adapter weights for sampling.</div>
  </div>

  <div>
    <div>4 · Shared</div>
    <strong>Pooled sampler</strong>
    <div>Returns rollouts for local scoring and the next step.</div>
  </div>
</div>

You do not create or delete a trainer job or inference deployment. Close each sampler and the service client when the run finishes.

## What you can run

<CardGroup>
  <Card title="Supervised Fine-Tuning (SFT)" icon="message">
    Run the loop with a cross-entropy loss over your labeled data.
  </Card>

  <Card title="Direct Preference Optimization (DPO)" icon="arrows-left-right">
    Train from chosen/rejected preference pairs. LoRA DPO uses the policy session's shared base reference, so there is no separate reference trainer to provision.
  </Card>

  <Card title="Reinforcement Learning (RL)" icon="brain">
    Sample completions from the current adapter, score them with your own reward function, and train with an importance-sampling loss (GRPO-style). This is the primary serverless use case.
  </Card>
</CardGroup>

All three run as LoRA on the shared pool. For full-parameter training, ORPO, distillation, or the broader Training API method set, use [Dedicated Training](/fine-tuning/training-api/dedicated). For standard platform-managed jobs, use [Managed Fine-Tuning](/fine-tuning/managed-finetuning-intro).

## When to use dedicated

Use [Dedicated Training](/fine-tuning/training-api/dedicated) when you need full-parameter training, broader model or method support, explicit resource lifecycle control, or sustained utilization. See the canonical [serverless versus dedicated comparison](/fine-tuning/training-api/introduction#infrastructure).

## Core concepts

**Session.** `create_lora_training_client(base_model, rank)` attaches you to a pooled trainer for that base model. That attachment is your training session (`service.training_session_id`) — your LoRA state lives there.

**Run.** The training client is your run (`training_client.run_id`). One run is one training trajectory: the `forward_backward` and `optim_step` calls plus the checkpoints you save.

**LoRA adapter.** Serverless is LoRA only. Pass a positive `rank` (e.g. `rank=8`); base weights stay frozen and shared across the pool, and you train an adapter on top.

**Checkpoint / snapshot.** `save_weights_for_sampler(name)` writes your current adapter weights and returns a snapshot path. That path is a public sampler identity, not a raw storage URI — hand it to the sampler to serve exactly those weights. See [Saving and loading checkpoints](#saving-and-loading-checkpoints) for the full save / resume / promote surface.

**Sampling.** `create_sampling_client(model_path=snapshot, tokenizer=...)` returns a sampler bound to that snapshot through the completions API (`/inference/v1/completions`). The snapshot selects the weights to serve; it is not a prompt-cache affinity key. The sampler runs in the same session, so there's no deployment to create or hot-load. Serverless and dedicated sampling share the [`DeploymentSampler` request contract](/fine-tuning/training-api/reference/deployment-sampler).

### Sampling with prompt caching

Check [Inference for RL rollouts](https://docs.fireworks.ai/guides/rollout-inference#inference-for-rl-rollouts) for guidance on session affinity and KV-cache behavior. Its **Training SDK** tab shows how to pass a stable trajectory ID through `DeploymentSampler`.

Install SDK version 1.2.9 or later and restart the client process after upgrading:

```bash theme={null}
pip install --upgrade "fireworks-ai[training]>=1.2.9"
```

<Warning>
  SDK versions 1.2.0 through 1.2.8 derived a shared session-affinity value from the sampler checkpoint, overriding per-request session values. Upgrade before using per-request affinity.
</Warning>

For batched rollout generation, see [`DeploymentSampler`: RL rollout sampling](/fine-tuning/training-api/reference/deployment-sampler#rl-rollout-sampling) for the two-samples-per-prompt pattern and `n=1` behavior.

## Quickstart

### Step 1: Create a key, install, and authenticate

Create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys) (click **Create API key** and store it somewhere safe), or run `firectl api-key create`. Then install the SDK and export the key:

```bash theme={null}
git clone https://github.com/fw-ai/cookbook
pip install -e ./cookbook/training
export FIREWORKS_API_KEY="fw_..."   # the key you just created
```

### Step 2: Run the complete serverless RL example

The cookbook includes its dataset, reward, loop, metrics, and cleanup behavior:

```bash theme={null}
cd cookbook/training
python -m examples.serverless_rl.countdown_rl
```

The default is a real paid run. For a cheaper smoke test, fork
`examples/serverless_rl/countdown_rl.py` and reduce `steps`, `group_size`,
`prompt_groups_per_step`, and `max_sample_tokens` before execution.

The remaining snippets explain the core calls used by that runnable example.

### Step 3: Connect to the serverless session

```python theme={null}
import os
from fireworks.training.sdk import FiretitanServiceClient

service = FiretitanServiceClient(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/training/v1/serverless",
)

base_model = "accounts/fireworks/models/qwen3p6-27b"
max_seq_len = 131072  # enforce this when rendering prompts and training datums
training_client = service.create_lora_training_client(base_model=base_model, rank=8)

print(f"session={service.training_session_id} run={training_client.run_id}")
```

This doubles as your setup check: if it prints a session id beginning with `ts-`, serverless routing is working. If the base URL does not end in `/training/v1/serverless`, sampling errors out.

### Step 4: Train, checkpoint, and sample

The complete example defines `datums`, `tinker`, `tokenizer`, `prompt`, and
`params`, and rejects prompt plus completion lengths above `max_seq_len`. The
excerpt below shows the operation order:

```python theme={null}
# One optimizer step
training_client.forward_backward(datums, "importance_sampling").result()
training_client.optim_step(
    tinker.AdamParams(learning_rate=2.5e-5, beta1=0.9, beta2=0.95, eps=1e-8, weight_decay=0.0)
).result()

# Save weights and open a sampler bound to that exact snapshot
snapshot = training_client.save_weights_for_sampler("step-0001").result().path
sampler = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
completions = sampler.sample(
    prompt=prompt,
    num_samples=8,
    sampling_params=params,
).result()
sampler.close()
```

<Warning>
  * Remote training and sampling operations return future-like results. Call `.result()` on operations that return one, or failures can be missed.
  * The tokenizer you pass must match `base_model`. It renders prompts and decodes sampled tokens client-side, so a mismatch silently corrupts your rewards.
  * Give each checkpoint a distinct `name`. Saving twice with the same name currently resolves to the same snapshot path.
</Warning>

## Reinforcement learning example

The end-to-end serverless RL pattern is the standard GRPO / importance-sampling loop: each step saves the current adapter, rolls out a batch of prompts through a sampler bound to that snapshot, scores completions with your reward function, turns group-relative advantages into training datums, and takes one optimizer step.

Track reward over time; improvement depends on the task, data, reward function, and configuration. Use the cookbook [`serverless_rl` example](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl) for a compact synchronous loop, or [`async_rl_loop_serverless`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/experiment/async_rl_loop_serverless.py) for experimental async scheduling and custom rollout functions. For a supervised loop, use cross-entropy loss. For a preference loop, use the DPO loss over chosen/rejected pairs — see [Cookbook: DPO](/fine-tuning/training-api/cookbook/dpo) for the dataset format and loss details. For the broader RL loss menu and dedicated provisioning, see the [cookbook RL recipes](/fine-tuning/training-api/cookbook/rl).

## Evaluating serverless checkpoints

There is no serverless chat endpoint for your adapter. To evaluate it, open a **sampling client** bound to a sampler checkpoint. `sampler.sample()` generates completions from that checkpoint, which you can score with your own metric.

Use the **sampler checkpoint** returned by `save_weights_for_sampler`, not a promoted model resource (`accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>`). Promoted models are for on-demand deployment and cannot be passed to `create_sampling_client`.

The following save-and-sample sequence comes from the [quickstart](#step-4-train-checkpoint-and-sample) and the cookbook [`serverless_rl` example](https://github.com/fw-ai/cookbook/blob/main/training/examples/serverless_rl/countdown_rl.py). Set up `prompt`, `tokenizer`, and `params` as shown in that example.

```python theme={null}
snapshot = training_client.save_weights_for_sampler("eval").result().path
sampler = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
try:
    result = sampler.sample(
        prompt=prompt,
        num_samples=1,
        sampling_params=params,
    ).result()
    for seq in result.sequences or []:
        tokens = list(seq.tokens or [])
        completion = get_text_content(renderer.parse_response(tokens)[0])
        # Score `completion` against your held-out label or grader.
finally:
    sampler.close()
```

`sampler.sample(...)` is the evaluation call. Repeat it over held-out prompts, then close the sampler. The Countdown example scores with `composite_reward`; replace that with your evaluation metric.

For checkpoint and promotion details, see [Saving and loading checkpoints](#saving-and-loading-checkpoints).

<Note>
  Sampler checkpoints live in the training session. If the session is gone, you cannot open a sampling client from that checkpoint. Promote checkpoints you need to retain, then evaluate the promoted model with a [preemptible deployment](/fine-tuning/evaluating-fine-tuned-models).
</Note>

## Saving and loading checkpoints

Serverless training writes **two different kinds of checkpoint**, and they are not interchangeable:

|                                                            | **Training checkpoint**                 | **Sampler checkpoint**           |
| ---------------------------------------------------------- | --------------------------------------- | -------------------------------- |
| Saved by                                                   | `save_state(name)`                      | `save_weights_for_sampler(name)` |
| Contains                                                   | Adapter weights **and** optimizer state | Current adapter weights only     |
| Resumable — the trainer can load it back and keep training | ✅ Yes                                   | ❌ No                             |
| Promotable to a deployable model                           | ❌ No                                    | ✅ Yes                            |

<Warning>
  Only **sampler checkpoints** can be promoted to a final model, and only **training checkpoints** can be loaded back by the trainer to resume. A training checkpoint cannot be served or promoted; a sampler checkpoint cannot restore training state (weights + optimizer).
</Warning>

Checkpoint storage is included during private preview.

### Save and resume training checkpoints

Save training checkpoints periodically so an interrupted run can continue:

```python theme={null}
# Save a training checkpoint (adapter weights + optimizer) for resume
training_client.save_state("step-0100").result()

# Resume inside the same run: restores weights and optimizer state
training_client.load_state_with_optimizer("step-0100").result()

# Weights-only load (optimizer resets to zero — a warm start)
training_client.load_state("step-0100").result()
```

Save and load calls return futures — call `.result()` to block and surface failures. `save_state` also accepts a `timeout` to bound the wait. Give each checkpoint a distinct name: overwriting an existing name (`overwrite=True`) is not supported.

To see what checkpoints a run has saved, use the session-scoped control-plane list in [Promote a sampler checkpoint to a model](#promote-a-sampler-checkpoint-to-a-model) below — the trainer-local `training_client.list_checkpoints()` is not routed on the serverless surface.

### Resume a new run from a training checkpoint

To fork a new run from a previous run's training checkpoint, use `create_training_client_from_state` on the service client. The SDK reads the base model and LoRA configuration from the checkpoint itself, creates a fresh run, and loads the saved state:

```python theme={null}
# Continue a previous run's training checkpoint in a new run (weights + optimizer)
resumed_client = service.create_training_client_from_state_with_optimizer(
    "<account>/<run-id>/step-0100",
)

# Or warm start from those weights with a fresh optimizer
resumed_client = service.create_training_client_from_state(
    "<account>/<run-id>/step-0100",
)
```

Checkpoint references are fully qualified as `<account>/<run-id>/<checkpoint-name>`, where `run-id` is the previous run's `training_client.run_id` (`run-<hex>`). `weights_access_token` is not supported — load checkpoints accessible to your API key.

### Promote a sampler checkpoint to a model

Promotion turns a **sampler checkpoint** into a deployable Fireworks model (a standard LoRA addon model). Training checkpoints are not promotable — save a sampler checkpoint first.

<Steps>
  <Step title="Save a sampler checkpoint during training">
    ```python theme={null}
    snapshot = training_client.save_weights_for_sampler("final").result().path
    ```

    Save one at the end of training, and at any intermediate step you may want to deploy later.
  </Step>

  <Step title="List the session's checkpoints">
    Listing and promotion are session-scoped control-plane operations on `FireworksClient` (against the regular API gateway, not the serverless base URL). The session resource name is available as `service.training_session_name`:

    ```python theme={null}
    import os
    from datetime import datetime
    from fireworks.training.sdk import FireworksClient

    fw_client = FireworksClient(api_key=os.environ["FIREWORKS_API_KEY"])

    rows = fw_client.list_training_session_checkpoints(service.training_session_name)
    target = max(
        (row for row in rows if row.get("promotable")),
        key=lambda row: datetime.fromisoformat(row["createTime"].replace("Z", "+00:00")),
    )
    ```

    Each row carries `name` (the full 4-segment resource name), `checkpointName`, `checkpointType`, `promotable`, and `createTime`. Two things to know about the values:

    * `checkpointName` is the server-side checkpoint id, **not** the bare name you passed: it is prefixed with the source run id and, for sampler checkpoints, suffixed with an 8-hex-char session id — a save named `final` surfaces as `run-<hex>-final-<8hex>`. Select rows on `promotable` + `createTime` as above, or with a prefix/substring test — never by equality with your logical name.
    * `checkpointType` is a server enum string: `CHECKPOINT_TYPE_TRAINING_LORA` for training checkpoints, `CHECKPOINT_TYPE_INFERENCE_LORA` for sampler checkpoints. Treat it as opaque and filter on `promotable`, which is authoritative.
  </Step>

  <Step title="Promote the checkpoint">
    ```python theme={null}
    model = fw_client.promote_session_checkpoint(
        name=target["name"],  # accounts/<a>/trainingSessions/<s>/checkpoints/<c>
        output_model_id="my-serverless-lora",
        base_model="accounts/fireworks/models/qwen3p6-27b",
    )
    ```

    `output_model_id` must be 1-63 characters of lowercase a-z, 0-9, and hyphens. The promoted model appears in your account's model list like any other fine-tuned model.
  </Step>
</Steps>

<Note>
  Session-scoped list and promote require the training session and its bound trainer to still exist. Once the session is deleted or its trainer is drained, both calls return `NOT_FOUND` and the checkpoints are no longer reachable through this API — promote any checkpoint you want to keep before the session is torn down. Cross-run training-checkpoint resume (above) is resolved per run and is not subject to this limit.
</Note>

### Deploy the promoted model to production

A promoted model deploys like any LoRA model fine-tuned on Fireworks: with **live merge**, Fireworks merges the adapter into the base weights at deployment time, so the deployment performs identically to the base model.

<Warning>
  Fine-tuned LoRA models can only be deployed to **on-demand (dedicated) deployments**. Serverless per-token serving of your own fine-tuned LoRA is not available.
</Warning>

Deploy the promoted model directly:

```bash theme={null}
firectl deployment create "accounts/<account-id>/models/my-serverless-lora"
```

Then send requests with the model name:

```python theme={null}
from fireworks import Fireworks

client = Fireworks()
response = client.chat.completions.create(
    model="accounts/<account-id>/models/my-serverless-lora",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

For deployment configuration, performance, and troubleshooting, see [Deploying fine-tuned models](/fine-tuning/deploying-loras).

For the full SDK-level checkpoint reference (base/delta sampler types, weight sync, and cross-job resolution), see [Dedicated Training](/fine-tuning/training-api/dedicated#saving-and-loading) and the [Cookbook Reference](/fine-tuning/training-api/cookbook/reference#checkpoints).

## Pricing

Serverless training is billed per token, across three meters: prefill, sample, and train. Current rates per model are in [Models](#models) below. Available models, meter definitions, and rates can change during private preview, so verify current availability and [pricing](https://fireworks.ai/pricing) before launch.

## Supported models and limits

### Models

Serverless models are not selected by shape. You attach to a shared, always-on trainer pool with a base model and your own `max_seq_len`, and pay only for the tokens you prefill, sample, and train. Serverless is LoRA only, for SFT, DPO, and RL.

<ServerlessModelsTable />

* Checkpoint storage for serverless models is included during private preview.
* The serverless model catalog evolves, and other frontier models are coming soon. For full-parameter training, ORPO, distillation, or a model not on that list, use [Dedicated Training](/fine-tuning/training-api/dedicated).
* For per-model availability across all training surfaces, see the [Models](/fine-tuning/models) catalog.

#### What the meters mean

Serverless training bills three separate token meters, so a run's cost depends on the mix of rollout and training tokens your loop generates:

| Meter       | What it counts                                                                                                                          |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Prefill** | Prompt tokens processed by the sampler before generation. Repeated prefixes hit the cache and bill at the cached rate, an 80% discount. |
| **Sample**  | Tokens generated by the sampler during rollouts.                                                                                        |
| **Train**   | Tokens passed through `forward_backward`, i.e. the datums you train on.                                                                 |

### Capacity and rate limits (private preview)

* **Concurrent runs:** The default quota is 8, although account overrides may differ. Slots are released when runs become terminal after session expiration.
* **Request and token limits:** Contact Fireworks for the current limits on your account.
* **Shared-pool capacity:** if the pool is full, `create_lora_training_client` returns an out-of-capacity error; retry, or switch to the dedicated path.

### Behavior to know

* **Set `max_seq_len` explicitly.** Serverless has no dedicated instance to infer sequence length from.
* **Cross-run checkpoint resume.** A training checkpoint can be resumed inside the same run (`load_state_with_optimizer`), or forked into a new run with `create_training_client_from_state` / `create_training_client_from_state_with_optimizer` using a fully qualified `<account>/<run-id>/<checkpoint-name>` reference. See [Saving and loading checkpoints](#saving-and-loading-checkpoints).
* **Serving your trained adapter.** Sample in-session during the run. To serve afterward, [promote a sampler checkpoint to a model](#promote-a-sampler-checkpoint-to-a-model) and [deploy it on an on-demand dedicated deployment](#deploy-the-promoted-model-to-production); serverless per-token serving of your own fine-tuned LoRA is not available.

## Video walkthrough: Train a prompt router

This walkthrough fine-tunes Qwen 3.5 9B with LoRA SFT to classify prompts and route them to a small or large model. It covers the local Python loop, pooled serverless trainer, in-session evaluation, and the before-and-after comparison.

<Frame>
  <iframe title="Train a prompt router with Fireworks Serverless Training" />
</Frame>

<Card title="Open the serverless prompt-router notebook" icon="github" href="https://github.com/fw-ai/cookbook/blob/main/training/case-studies/sft_prompt_router/prompt_router_serverless.ipynb">
  Follow the complete Cookbook example for dataset preparation, LoRA SFT, sampling, and evaluation.
</Card>

## Next steps

* [Serverless RL cookbook example](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl): runnable serverless loop
* [Async serverless RL recipe](https://github.com/fw-ai/cookbook/blob/main/training/recipes/experiment/async_rl_loop_serverless.py): experimental rollout-function loop with rollout/training overlap
* [Choose infrastructure](/fine-tuning/training-api/introduction#infrastructure): compare serverless and dedicated
* [Dedicated Training](/fine-tuning/training-api/dedicated): the provisioned path from setup through teardown
* [Training and Sampling](/fine-tuning/training-api/dedicated#training-and-sampling): dedicated lifecycle internals
* [Loss Functions](/fine-tuning/training-api/dedicated#loss-functions): built-in and custom losses
* [The Cookbook](/fine-tuning/training-api/cookbook/overview): ready-to-run recipes, including [`serverless_rl`](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl)
