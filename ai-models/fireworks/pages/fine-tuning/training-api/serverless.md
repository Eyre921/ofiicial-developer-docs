---
title: "Serverless Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/serverless
path: fine-tuning/training-api/serverless
---

Run LoRA fine-tuning and RL on a shared pooled trainer, with no provisioning and per-token pricing.

<Info>
  Serverless training is currently in **private preview** and access is gated per account. [Request access](https://fireworks.ai/contact-training) and mention "serverless training."
</Info>

Serverless training connects to a shared, already-running pooled trainer through the gateway and returns training and sampling clients. There is no trainer job or inference deployment to provision or delete. Close each sampler and the service client when finished.

Not sure whether the shared pool fits your workload? [Compare serverless and dedicated training](/fine-tuning/training-api/choose-infrastructure).

<Info>
  **What you need**

  * **Install the SDK** (same one as the dedicated path, no separate console flow): `pip install --pre "fireworks-ai[training]"`
  * **For the runnable example, clone the cookbook:** `git clone https://github.com/fw-ai/cookbook && pip install -e ./cookbook/training`
  * **Point at the serverless endpoint:** `base_url="https://api.fireworks.ai/training/v1/serverless"`
  * **Pick a base model enabled for serverless training on your account.** Availability changes during private preview; verify it before launch.
  * Set your API key and run the [Quickstart](#quickstart) below.
</Info>

<Tip>
  **Using a code agent?** A complete, forkable serverless RL loop lives in the cookbook at [`training/examples/serverless_rl/`](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl). It runs out of the box against the serverless gateway.
</Tip>

## What is serverless training?

You write the training loop, for supervised fine-tuning or reinforcement learning, and Fireworks runs the forward pass, backward pass, and optimizer on remote GPUs, then serves your latest weights for sampling in the same session.

The [quickstart](#quickstart) shows the exact client setup and operation order. The complete implementation lives in the cookbook's [`serverless_rl` example](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl).

## What you can run

<CardGroup>
  <Card title="Supervised Fine-Tuning (SFT)" icon="message">
    Run the loop with a cross-entropy loss over your labeled data.
  </Card>

  <Card title="Reinforcement Learning (RL)" icon="brain">
    Sample completions from the current adapter, score them with your own reward function, and train with an importance-sampling loss (GRPO-style). This is the primary serverless use case.
  </Card>
</CardGroup>

Both run as LoRA on the shared pool. For full-parameter training, DPO, or the broader Training API method set, use [Dedicated Training](/fine-tuning/training-api/dedicated). For standard platform-managed jobs, use [Managed Fine-Tuning](/fine-tuning/managed-finetuning-intro).

## When to use dedicated

Use [Dedicated Training](/fine-tuning/training-api/dedicated) when you need full-parameter training, broader model or method support, explicit resource lifecycle control, or sustained utilization. See the canonical [serverless versus dedicated comparison](/fine-tuning/training-api/choose-infrastructure).

## Core concepts

**Session.** `create_lora_training_client(base_model, rank)` attaches you to a pooled trainer for that base model. That attachment is your training session (`service.training_session_id`) — your LoRA state lives there.

**Run.** The training client is your run (`training_client.run_id`). One run is one training trajectory: the `forward_backward` and `optim_step` calls plus the checkpoints you save.

**LoRA adapter.** Serverless is LoRA only. Pass a positive `rank` (e.g. `rank=8`); base weights stay frozen and shared across the pool, and you train an adapter on top.

**Checkpoint / snapshot.** `save_weights_for_sampler(name)` writes your current adapter weights and returns a snapshot path. That path is a public sampler identity, not a raw storage URI — hand it to the sampler to serve exactly those weights.

**Sampling.** `create_sampling_client(model_path=snapshot, tokenizer=...)` returns a sampler bound to that snapshot through the completions API (`/inference/v1/completions`). For multi-turn rollouts, session-affinity headers pin an episode to one replica so the KV cache is reused across turns (see [RL rollout integration](/fine-tuning/rl-rollout-integration)). The sampler runs in the same session, so there's no deployment to create or hot-load.

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
max_seq_len = 65536  # enforce this when rendering prompts and training datums
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

Track reward over time; improvement depends on the task, data, reward function, and configuration. Use the complete cookbook [`serverless_rl` example](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl) rather than rebuilding the loop from this page. For a supervised loop, use cross-entropy loss. For the broader RL loss menu and dedicated provisioning, see the [cookbook RL recipes](/fine-tuning/training-api/cookbook/rl).

## Pricing

Serverless training is billed per token. Available models, meter definitions, and rates can change during private preview. Verify current availability and [pricing](https://fireworks.ai/pricing) before launch.

## Supported models and limits

### Models

Use a base model enabled for serverless training on your account. Serverless is LoRA only. For full-parameter training or a model not enabled on the shared pool, use [Dedicated Training](/fine-tuning/training-api/dedicated).

### Capacity and rate limits (private preview)

* **Concurrent runs:** The default quota is 8, although account overrides may differ. Slots are released when runs become terminal after session expiration.
* **Request and token limits:** Contact Fireworks for the current limits on your account.
* **Shared-pool capacity:** if the pool is full, `create_lora_training_client` returns an out-of-capacity error; retry, or switch to the dedicated path.

### Behavior to know

* **Set `max_seq_len` explicitly.** Serverless has no dedicated instance to infer sequence length from.
* **Cross-run checkpoint resume is not yet supported.** A checkpoint saved during a run can only be resumed by that same run. Forking a new run from a prior run's checkpoint (Tinker's `create_training_client_from_state`) is dedicated-only today.
* **Serving your trained adapter.** Sample in-session during the run. To serve afterward, deploy the adapter on a dedicated or preemptible deployment; serverless per-token serving of your own fine-tuned LoRA is not available yet.

## Next steps

* [Serverless RL cookbook example](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl): runnable serverless loop
* [Choose infrastructure](/fine-tuning/training-api/choose-infrastructure): compare serverless and dedicated
* [Dedicated Training](/fine-tuning/training-api/dedicated): the provisioned path from setup through teardown
* [Training and Sampling](/fine-tuning/training-api/training-and-sampling): dedicated lifecycle internals
* [Loss Functions](/fine-tuning/training-api/loss-functions): built-in and custom losses
* [The Cookbook](/fine-tuning/training-api/cookbook/overview): ready-to-run recipes, including [`serverless_rl`](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl)
