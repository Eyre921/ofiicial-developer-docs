---
title: "Introduction"
source: https://docs.fireworks.ai/fine-tuning/training-api/introduction
path: fine-tuning/training-api/introduction
---

Fireworks Training API — custom training loops with full Python control over objectives, while Fireworks handles distributed GPU infrastructure.

<Info>
  The Training API is currently in **private preview**. [Request early access](https://fireworks.ai/contact-training) to get started.
</Info>

<Tip>
  **Using a coding agent?** Install the [Fireworks training skill](/fine-tuning/agent/use-with-coding-agents). One skill covers managed training and Training API serverless or dedicated cookbook workflows.
</Tip>

## What is the Training API?

Fireworks Training API lets you write training logic in plain Python on your local machine while model computation runs on remote GPUs managed by Fireworks.

Most users should start from [cookbook recipes](/fine-tuning/training-api/cookbook/overview), the recommended entry point for standard SFT, DPO, GRPO-style training, and experimental async RL loops for agentic RL. Fork a recipe when you want to adapt an existing loop with your own loss, reward, rollout function, data loading, or checkpointing behavior.

Use the Direct SDK when you need full control over Training API behavior.

| Mode                 | Best for                                                                                                               | Infrastructure                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Cookbook recipes** | Recommended entry point for adapting existing SFT/DPO/GRPO-style loops, including experimental async RL for agentic RL | You configure and implement simple loss, reward, or rollout functions; platform runs GPUs |
| **Direct SDK**       | Full control over training behavior                                                                                    | You drive the training flow; platform runs GPUs                                           |

## Choose serverless or dedicated infrastructure

After choosing the Training API, decide how compute is provided:

* [**Serverless Training**](/fine-tuning/training-api/serverless): shared pooled trainer, LoRA SFT or RL on supported models, no provisioning, per-token billing.
* [**Dedicated Training**](/fine-tuning/training-api/dedicated): provisioned trainer and deployment resources, broader model and method support, explicit checkpoint/resume/deployment control.

Use the [infrastructure decision guide](/fine-tuning/training-api/choose-infrastructure) before adapting a recipe.

## Who does what

| Fireworks handles                                                        | Cookbook recipes handle                                                    | Direct SDK users implement                                                     |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| GPU provisioning and cluster management                                  | Training loop structure for supported recipes                              | Training loop logic (`forward_backward_custom` + `optim_step`)                 |
| Service-mode trainer lifecycle (create, health-check, reconnect, delete) | Resource setup, health checks, reconnect, and cleanup                      | Managed service setup with `FiretitanServiceClient.from_firetitan_config(...)` |
| Distributed forward pass, backward pass, optimizer execution             | Common losses and reward/evaluation plumbing                               | Loss function and batch construction                                           |
| Checkpoint storage and export                                            | Checkpoint save, resume, promotion, and sampler refresh                    | Checkpoint calls (`save_weights_for_sampler`, DCP snapshots)                   |
| Inference deployments and weight sync                                    | Deployment sampling and serving-integrated evaluation for RL recipes       | Custom rollout, sampling, and evaluation logic through the managed service     |
| Preemption recovery and job resume                                       | Resume logic for supported recipe checkpoints                              | Resume policy and state restoration calls                                      |
| Distributed training (multi-node, sharding, FSDP)                        | Config surfaces for learning rate, grad accumulation, context length, W\&B | Hyperparameter schedules, data pipeline, and experiment tracking               |

## System architecture

```mermaid theme={null}
flowchart LR
  local["Your Python Code<br/>(loss function, data loading, metrics)"] <-->|HTTP API| gpu["Fireworks GPUs<br/>(forward pass, backward pass, optimizer)"]
```

## How service-mode training works

<Warning>
  **Most common gotchas**

  * Remote operations such as `forward`, `forward_backward`, `optim_step`, sampling, and checkpoint saves return future-like results. Call `.result()` on operations that return one.
  * `token_weights=0` means prompt/no-loss tokens, `token_weights=1` means response/learned tokens.
  * `forward_backward_custom` computes gradients only; you still need `optim_step` to apply updates.
</Warning>

### Minimal training step lifecycle

1. Create an SDK-managed service and connect a training client.
2. Send tokenized datums (with loss weights).
3. Run `forward_backward_custom(...).result()`.
4. Run `optim_step(...).result()`.
5. Save sampler weights and refresh the SDK-managed sampler.

### Datums

A **Datum** is the unit of training data sent to the remote GPU. It wraps tokenized input and per-token weights that your loss function needs.

For SFT, token weight `0.0` marks prompt tokens and `1.0` marks response tokens. Cookbook renderers construct these weights from chat messages.

### Logprobs and forward\_backward\_custom

When you call `forward_backward_custom`, the GPU runs a forward pass and returns **per-token log-probabilities** as PyTorch tensors with `requires_grad=True`. Your loss function computes a scalar loss, the API calls `loss.backward()`, and gradients are sent back to the GPU for the model backward pass.

After accumulating gradients, call `optim_step` to apply the update. See the [Dedicated Training Quickstart](/fine-tuning/training-api/quickstart) for one complete runnable Datum, loss, and optimizer loop.

### Futures

Remote training operations such as `forward`, `forward_backward`, `optim_step`, and checkpoint saves return **future-like results**. Call `.result()` on operations that return one so failures surface.

### Checkpointing and weight sync

After training, you export checkpoints for serving:

* **Base snapshot:** a complete chain anchor for the trainable state. For LoRA this is the adapter; for full-parameter training it is model weights.
* **Delta snapshot:** a change relative to a prior full-parameter base snapshot.

The SDK selects base versus delta automatically unless the recipe overrides it.

Checkpoint-to-sampler behavior depends on the infrastructure:

* **Serverless:** save a snapshot and bind an in-session sampling client to that snapshot. There is no deployment weight sync. See [Serverless Training](/fine-tuning/training-api/serverless).
* **Dedicated:** save a snapshot and refresh an SDK-managed deployment sampler, which syncs weights onto the deployment. See [Dedicated Training and Sampling](/fine-tuning/training-api/training-and-sampling).

For dedicated RL rollouts that continue across weight sync, see [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts).

## Key APIs

| API                                                                             | Purpose                                                                                                                                       |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [`FiretitanServiceClient`](/fine-tuning/training-api/reference/service-client)  | Recommended direct SDK entry point. Creates or reattaches trainers/deployments and returns training, reference, and sampling clients.         |
| [`FiretitanTrainingClient`](/fine-tuning/training-api/reference/service-client) | Tinker-compatible training client: `forward_backward_custom`, `optim_step`, `save_weights_for_sampler`, `save_state`, and load methods.       |
| [`DeploymentSampler`](/fine-tuning/training-api/reference/deployment-sampler)   | FireTitan-native sampler for tokenized rollout/evaluation from SDK-managed deployments.                                                       |
| [`FireworksClient`](/fine-tuning/training-api/reference/fireworks-client)       | Standalone checkpoint operations such as listing checkpoints or promoting a model without a live training instance.                           |
| [`TrainerJobManager`](/fine-tuning/training-api/reference/trainer-job-manager)  | Legacy/compatibility lifecycle manager. Documented for existing SDK users and advanced debugging; not the recommended user-facing path.       |
| [`DeploymentManager`](/fine-tuning/training-api/reference/deployment-manager)   | Legacy/compatibility deployment manager. Documented for existing SDK users and advanced debugging; normal code uses `FiretitanServiceClient`. |

## Renderers

Chat-template formatting, stop-token handling, and loss-weight masking for SFT/DPO datasets are handled by **renderers** — pluggable per-model classes that turn raw conversations into the trainer's `Datum` shape. Most users never touch a renderer directly; cookbook recipes pick the right one for the `base_model` you set. If you need to author a new one or debug parity against HuggingFace, the implementation depth lives in the cookbook's [`skills/renderer/`](https://github.com/fw-ai/cookbook/tree/main/skills/renderer) skill.

## Comparing Training API pricing vs DIY bare metal

When comparing a managed training platform with a self-managed bare-metal stack,
optimize for **cost per successful iteration**, not just headline `$ / GPU-hour`.

### What to compare

* **Time to first deployed model**: include environment setup, training orchestration, checkpoint handoff, and serving integration.
* **Iteration cycle time** (`train -> eval -> deploy -> repeat`): include all retrain/redeploy plumbing, not just GPU runtime.
* **Infra engineering overhead**: include one-time setup and recurring maintenance for containers, runtimes, deployment workflows, and compatibility fixes.
* **Effective `$ / GPU-hour` at real utilization**: include idle capacity, reservation constraints, and burst/overflow behavior.
* **Train/serve parity risk**: account for potential quality drift when training and inference runtimes diverge.
* **Parallel experiment capacity**: compare fixed-reservation throughput against elastic capacity for sweeps and multi-seed runs.

### Useful formulas

```text theme={null}
iterations_per_month = available_working_days / cycle_time_days
effective_cost_per_gpu_hour = total_monthly_spend / gpu_hours_consumed
multi_turn_success ~= (single_turn_success)^turn_count
```

### Keep assumptions explicit

Document assumptions so readers can adjust them for their own workload:

* team size and fully-loaded engineering cost
* average cycle duration in each setup
* expected utilization and burst profile
* average turn count for production agent workflows
* required concurrent experiment count

## FAQ

### Why is my training run "doing nothing" even though code executed?

Usually because `.result()` was not called on futures, so failures were never surfaced.

### What's the difference between base and delta checkpoints, and when should I use each?

Let the SDK select automatically. LoRA snapshots contain the full adapter; full-parameter delta snapshots can accelerate synchronization but are not promotable. See [Saving and Loading](/fine-tuning/training-api/saving-and-loading#sampler-checkpoints).

### Do I need to manage distributed training infra?

No. You implement training logic while Fireworks manages GPU provisioning and distributed infrastructure.

### Should I start with Cookbook or Direct SDK?

Start with Cookbook for most SFT/DPO/GRPO adaptations. Use the Direct SDK when you need custom loop semantics and full control.

### Can I evaluate serving behavior during training?

Yes. On serverless, save a snapshot and sample from it in the same session. On dedicated infrastructure, sync a snapshot to the SDK-managed deployment sampler and evaluate there.

### How should I compare Training API pricing vs a DIY bare-metal setup?

Use the framework in [Comparing Training API pricing vs DIY bare metal](#comparing-training-api-pricing-vs-diy-bare-metal). Focus on total iteration economics (cycle time, engineering overhead, utilization-adjusted cost, and quality-parity risk), then plug in your own assumptions.

### How can I compare rollout cost vs other providers?

See the [Price comparison vs Tinker](/fine-tuning/multi-turn-cost-comparison) calculator to estimate scenario-based costs on Fireworks Dedicated against Tinker's per-token pricing.

## Next steps

* [Dedicated quickstart](/fine-tuning/training-api/quickstart) — run a minimal dedicated custom loop
* [Choose infrastructure](/fine-tuning/training-api/choose-infrastructure) — compare serverless and dedicated training
* [Serverless Training](/fine-tuning/training-api/serverless) — shared pooled LoRA training
* [Dedicated Training](/fine-tuning/training-api/dedicated) — provisioned trainer and deployment lifecycle
* [Dedicated Training and Sampling](/fine-tuning/training-api/training-and-sampling) — deployment-sampling lifecycle
* [Loss Functions](/fine-tuning/training-api/loss-functions) — built-in and custom loss functions
* [Vision Inputs](/fine-tuning/training-api/vision-inputs) — fine-tune vision-language models with image and text data
* [The Cookbook](/fine-tuning/training-api/cookbook/overview) — ready-to-run recipes for SFT, DPO, ORPO, GRPO/IGPO, and async RL (experimental)
