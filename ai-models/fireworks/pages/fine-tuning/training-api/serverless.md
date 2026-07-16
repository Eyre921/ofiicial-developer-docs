---
title: "Serverless Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/serverless
path: fine-tuning/training-api/serverless
---

Run LoRA fine-tuning and RL on a shared pooled trainer, with no provisioning and per-token pricing.

<Info>
  Serverless training is currently in **private preview** and access is gated per account. [Request access](https://fireworks.ai/contact-training) and mention "serverless training"; we'll enable your account and provide onboarding credits so you can start testing the same week.
</Info>

Serverless training is the fastest way to run post-training on Fireworks. You connect to a shared, already-running pooled trainer through the gateway and get back a single service object that hands you both a training client and a sampling client. There is nothing to provision: no trainer job to launch, no inference deployment to stand up, and nothing to tear down.

<Info>
  **What you need**

  * **Install the SDK** (same one as the dedicated path, no separate console flow): `pip install --pre "fireworks-ai[training]"`
  * **Point at the serverless endpoint:** `base_url="https://api.fireworks.ai/training/v1/serverless"`
  * **Pick a base model:** `accounts/fireworks/models/qwen3p5-9b` (**Qwen 3.5 9B**) or `accounts/fireworks/models/qwen3p6-27b` (**Qwen 3.6 27B**)
  * Set your API key and run the [Quickstart](#quickstart) below.
</Info>

<Tip>
  **Using a code agent?** A complete, forkable serverless RL loop lives in the cookbook at [`training/examples/serverless_rl/`](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl). It runs out of the box against the serverless gateway.
</Tip>

## What is serverless training?

You write the training loop, for supervised fine-tuning or reinforcement learning, and Fireworks runs the forward pass, backward pass, and optimizer on remote GPUs, then serves your latest weights for sampling in the same session.

```python theme={null}
from fireworks.training.sdk import FiretitanServiceClient

service = FiretitanServiceClient(
    api_key=api_key,
    base_url="https://api.fireworks.ai/training/v1/serverless",
)

training_client = service.create_lora_training_client(base_model, rank=8)

for step in range(steps):
    snapshot = training_client.save_weights_for_sampler(name).result().path
    sampler  = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
    # sample completions, score them, build training datums
    training_client.forward_backward(datums, "importance_sampling").result()
    training_client.optim_step(adam).result()
```

## What you can run

<CardGroup>
  <Card title="Supervised Fine-Tuning (SFT)" icon="message">
    Run the loop with a cross-entropy loss over your labeled data.
  </Card>

  <Card title="Reinforcement Learning (RL)" icon="brain">
    Sample completions from the current adapter, score them with your own reward function, and train with an importance-sampling loss (GRPO-style). This is the primary serverless use case.
  </Card>
</CardGroup>

Both run as LoRA on the shared pool. For full-parameter training, DPO, or the full menu of managed methods, use the [dedicated path](/fine-tuning/training-api/training-and-sampling).

## Serverless vs dedicated

The two paths share the same SDK surface and the same primitives; they differ in how compute is provisioned.

| Dimension     | Serverless                                                                                                    | Dedicated                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Provisioning  | None. Attach to a shared pooled trainer.                                                                      | SDK provisions a trainer job and an inference deployment for your run.                                 |
| Tuning method | LoRA only (SFT or RL).                                                                                        | LoRA and full-parameter.                                                                               |
| Capacity      | Shared pool, subject to availability.                                                                         | Reserved for your run.                                                                                 |
| Lifecycle     | Nothing to manage or tear down.                                                                               | You manage and tear down the trainer and deployment.                                                   |
| Idle cost     | None. Pay per token.                                                                                          | Deployment bills per GPU-hour until scaled to zero or deleted.                                         |
| Best for      | Fast iteration, small-to-mid LoRA experiments, RL loops with inference in the loop, first-time training runs. | Large-model or full-parameter training, sustained production RL, long rollouts, guaranteed throughput. |

Start on serverless to move fast. Move to [dedicated](/fine-tuning/training-api/training-and-sampling) when you need full-parameter training, reserved capacity, or the cost curve of a saturated GPU at scale.

## Core concepts

**Session.** `create_lora_training_client(base_model, rank)` attaches you to a pooled trainer for that base model. That attachment is your training session (`service.training_session_id`) — your LoRA state lives there.

**Run.** The training client is your run (`training_client.run_id`). One run is one training trajectory: the `forward_backward` and `optim_step` calls plus the checkpoints you save.

**LoRA adapter.** Serverless is LoRA only. Pass a positive `rank` (e.g. `rank=8`); base weights stay frozen and shared across the pool, and you train an adapter on top.

**Checkpoint / snapshot.** `save_weights_for_sampler(name)` writes your current adapter weights and returns a snapshot path. That path is a public sampler identity, not a raw storage URI — hand it to the sampler to serve exactly those weights.

**Sampling.** `create_sampling_client(model_path=snapshot, tokenizer=...)` returns a sampler bound to that snapshot, served through Fireworks' OpenAI-compatible completions API (`/inference/v1/chat/completions`). For multi-turn rollouts, session-affinity headers pin an episode to one replica so the KV cache is reused across turns (see [RL rollout integration](/fine-tuning/rl-rollout-integration)). The sampler runs in the same session, so there's no deployment to create or hot-load.

## Quickstart

### Step 1: Create a key, install, and authenticate

Create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys) (click **Create API key** and store it somewhere safe), or run `firectl api-key create`. Then install the SDK and export the key:

```bash theme={null}
pip install --pre "fireworks-ai[training]"
export FIREWORKS_API_KEY="fw_..."   # the key you just created
```

### Step 2: Connect to the serverless session

```python theme={null}
import os
from fireworks.training.sdk import FiretitanServiceClient

service = FiretitanServiceClient(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/training/v1/serverless",
)

base_model = "accounts/fireworks/models/qwen3p6-27b"
training_client = service.create_lora_training_client(base_model=base_model, rank=8)

print(f"session={service.training_session_id} run={training_client.run_id}")
```

This doubles as your setup check: if it prints a session id beginning with `ts-`, serverless routing is working. If the base URL does not end in `/training/v1/serverless`, sampling errors out.

### Step 3: Train, checkpoint, and sample

```python theme={null}
# One optimizer step
training_client.forward_backward(datums, "importance_sampling").result()
training_client.optim_step(
    tinker.AdamParams(learning_rate=2.5e-5, beta1=0.9, beta2=0.95, eps=1e-8, weight_decay=0.0)
).result()

# Save weights and open a sampler bound to that exact snapshot
snapshot = training_client.save_weights_for_sampler("step-0001").result().path
sampler = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
completions = sampler.sample(prompt=prompt, num_samples=8, sampling_params=params)
```

<Warning>
  * Every training-client call returns a future. Always call `.result()`, or failures can be missed.
  * The tokenizer you pass must match `base_model`. It renders prompts and decodes sampled tokens client-side, so a mismatch silently corrupts your rewards.
  * Give each checkpoint a distinct `name`. Saving twice with the same name currently resolves to the same snapshot path.
</Warning>

## Reinforcement learning example

The end-to-end serverless RL pattern is the standard GRPO / importance-sampling loop: each step saves the current adapter, rolls out a batch of prompts through a sampler bound to that snapshot, scores completions with your reward function, turns group-relative advantages into training datums, and takes one optimizer step.

```python theme={null}
for step in range(steps):
    snapshot = training_client.save_weights_for_sampler(f"countdown-{step:04d}").result().path
    sampler  = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)

    # sample group_size completions per prompt, score each with your reward_fn,
    # standardize rewards within each prompt group (GRPO), drop zero-spread groups
    datums = build_importance_sampling_datums(sampler, batch, reward_fn)

    training_client.forward_backward(datums, "importance_sampling").result()
    training_client.optim_step(adam).result()
```

Reward should climb as the policy learns the task. The complete runnable version is the cookbook's [`serverless_rl`](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl) example. For a supervised loop, run the same structure with a cross-entropy loss instead of importance sampling. For the full menu of RL losses (GRPO, DAPO, GSPO, CISPO) and the dedicated provisioned path, see the [cookbook RL recipes](/fine-tuning/training-api/cookbook/rl).

## Pricing

Serverless training is billed per token, with three meters: **prefill** (reading the prompt), **sample** (generating tokens), and **train** (the tokens you learn from), each priced per 1M tokens. There is no idle cost: you pay only for tokens processed. Long-context variants are priced as separate SKUs, and MoE models are priced by active parameters.

**Cached prefill.** Fireworks is KV-cache-aware on the sampler side and passes the benefit through to you. When an agent accumulates context turn after turn, the repeated prefill tokens hit the cache and are billed at **20% of the prefill rate (an 80% discount)**, so multi-turn rollouts cost materially less than the headline prefill rate suggests.

| Base model   | Context | Prefill (per 1M) | Cached prefill (per 1M) | Sample (per 1M) | Train (per 1M) |
| ------------ | ------- | ---------------- | ----------------------- | --------------- | -------------- |
| Qwen 3.5 9B  | 65K     | \$0.44           | \$0.088                 | \$1.33          | \$1.33         |
| Qwen 3.6 27B | 65K     | \$1.24           | \$0.248                 | \$3.73          | \$3.73         |

Additional models are added to the table as they come online.

Checkpoint storage is billed at \$0.10 / GB-month. See the [pricing page](https://fireworks.ai/pricing) for the current authoritative rates.

For sustained or multi-turn RL at scale, dedicated GPU-hour billing is often cheaper overall, because session-affinity KV-cache reuse turns cache savings into more work per hour. Use the [cost comparison calculator](/fine-tuning/multi-turn-cost-comparison) to estimate your workload on serverless per-token pricing against Fireworks Dedicated.

## Supported models and limits

### Models

* **Qwen 3.5 9B** and **Qwen 3.6 27B**, up to **65K context**. LoRA only, dense only. Additional models roll out as they come online.
* For full-parameter training or MoE base models, use the [dedicated path](/fine-tuning/training-api/training-and-sampling).

### Capacity and rate limits (private preview)

* **Concurrent runs:** 8 per account. Sessions auto-release \~10 minutes after the last heartbeat, so a fast iterate/retry loop can briefly hit `HTTP 429: maximum concurrent serverless training runs exceeded` until slots free up.
* **Rate limits:** per-account budget shared across training and sampling — 60 requests/min, 60K prompt tokens/min, 12K generated tokens/min. RL rollouts run against raised limits. The SDK backs off on 429s, so steps may slow rather than fail. Reach out if you need higher throughput.
* **Shared-pool capacity:** if the pool is full, `create_lora_training_client` returns an out-of-capacity error; retry, or switch to the dedicated path.

### Behavior to know

* **Set `max_seq_len` explicitly.** Serverless has no dedicated instance to infer sequence length from.
* **Cross-run checkpoint resume is not yet supported.** A checkpoint saved during a run can only be resumed by that same run. Forking a new run from a prior run's checkpoint (Tinker's `create_training_client_from_state`) is dedicated-only today.
* **Serving your trained adapter.** Sample in-session during the run. To serve afterward, deploy the adapter on a dedicated or preemptible deployment; serverless per-token serving of your own fine-tuned LoRA is not available yet.

## Next steps

* [Quickstart](/fine-tuning/training-api/quickstart): a custom training loop from scratch
* [Training and Sampling](/fine-tuning/training-api/training-and-sampling): the dedicated provisioned path
* [Loss Functions](/fine-tuning/training-api/loss-functions): built-in and custom losses
* [The Cookbook](/fine-tuning/training-api/cookbook/overview): ready-to-run recipes, including [`serverless_rl`](https://github.com/fw-ai/cookbook/tree/main/training/examples/serverless_rl)
