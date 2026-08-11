---
title: "Overview"
source: https://docs.fireworks.ai/fine-tuning/training-api/introduction
path: fine-tuning/training-api/introduction
---

Fireworks Training API — custom training loops with full Python control over objectives, while Fireworks handles distributed GPU infrastructure.

<Info>
  The Training API is currently in **private preview**. [Request early access](https://fireworks.ai/contact-training) to get started.
</Info>

<Tip>
  **Using a coding agent?** Install the [Fireworks training skill](/fine-tuning/agent/use-with-coding-agents) to help configure, run, and troubleshoot training jobs using current Fireworks best practices.
</Tip>

## What is the Training API?

Fireworks Training API lets you write training logic in plain Python on your local machine while model computation runs on remote GPUs managed by Fireworks.

Most users should start from [Cookbook recipes](/fine-tuning/training-api/cookbook/overview), the recommended entry point for standard SFT, DPO, GRPO-style training, and experimental async RL loops for agentic RL. Recipes use the Python SDK and can be run directly or through your agent.

Use the Python SDK directly when you need full control over Training API behavior.

| Starting point      | Best for                                                               | How you use it                                              |
| ------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Cookbook recipe** | Adapting a working SFT, DPO, GRPO-style, or experimental async RL loop | Run it with the Python SDK directly or through your agent   |
| **Python SDK**      | Full control over training behavior                                    | Write the training flow in Python while Fireworks runs GPUs |

<h2>
  Choose infrastructure
</h2>

After choosing the Training API, decide how compute is provided:

* [**Serverless Training**](/fine-tuning/training-api/serverless): shared pooled trainer, LoRA SFT, DPO, or RL on supported models, no provisioning, per-token billing.
* [**Dedicated Training**](/fine-tuning/training-api/dedicated): provisioned trainer and deployment resources, broader model and method support, explicit checkpoint/resume/deployment control.

<CardGroup>
  <Card title="Serverless Training" icon="bolt" href="/fine-tuning/training-api/serverless">
    Attach to a shared pooled trainer. There is no trainer or rollout deployment to provision.
  </Card>

  <Card title="Dedicated Training" icon="server" href="/fine-tuning/training-api/dedicated">
    Provision trainer and deployment resources for your run, with broader model and method support.
  </Card>
</CardGroup>

### Quick decision

<div aria-label="Decision guide comparing serverless and dedicated Training API infrastructure">
  <div>
    <strong>Start with Serverless Training</strong>

    <div>
      The model is supported, LoRA SFT or RL covers the task, and you want pooled compute with per-token billing.
    </div>
  </div>

  <div>
    <strong>Choose Dedicated Training</strong>

    <div>
      You need full-parameter training, DPO, explicit resume or deployment control, or sustained provisioned compute.
    </div>
  </div>
</div>

### Comparison

| Dimension         | Serverless                                                       | Dedicated                                                                                     |
| ----------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Provisioning      | Shared pooled trainer; no trainer or sampler deployment creation | SDK provisions trainer and deployment resources                                               |
| Billing           | Per token; no idle GPU charge                                    | Time-based trainer and deployment billing                                                     |
| Parameter mode    | LoRA only                                                        | LoRA and full-parameter                                                                       |
| Methods           | SFT and RL on the supported serverless surface                   | SFT, DPO, ORPO, RL, distillation, and custom loops supported by the selected shape and recipe |
| Models            | Current serverless model list                                    | Models with an enabled dedicated training shape                                               |
| Capacity          | Shared pool and per-account limits                               | Resources allocated to the run, subject to account quota and platform availability            |
| Checkpoint resume | In-run snapshots; cross-run resume is limited                    | Explicit checkpoint, reconnect, promotion, and deployment lifecycle                           |
| Sampling          | In-session sampler, no deployment to create                      | SDK-managed rollout or evaluation deployment                                                  |
| Teardown          | Session lifecycle is managed by the service                      | You must close trainers and delete or scale down deployments                                  |
| Best fit          | Fast LoRA experiments and first RL iterations                    | Full-parameter work, DPO, sustained RL, larger workloads, explicit lifecycle control          |

Always verify current models, limits, prices, and feature status in the [Serverless Training](/fine-tuning/training-api/serverless) and [Dedicated Training](/fine-tuning/training-api/dedicated) pages before launch.

## Who does what

| Fireworks handles                                                        | Cookbook recipes handle                                                    | Python SDK users implement                                                     |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| GPU provisioning and cluster management                                  | Training loop structure for supported recipes                              | Training loop logic (`forward_backward_custom` + `optim_step`)                 |
| Service-mode trainer lifecycle (create, health-check, reconnect, delete) | Resource setup, health checks, reconnect, and cleanup                      | Managed service setup with `FiretitanServiceClient.from_firetitan_config(...)` |
| Distributed forward pass, backward pass, optimizer execution             | Common losses and reward/evaluation plumbing                               | Loss function and batch construction                                           |
| Checkpoint storage and export                                            | Checkpoint save, resume, promotion, and sampler refresh                    | Checkpoint calls (`save_weights_for_sampler`, DCP snapshots)                   |
| Inference deployments and weight sync                                    | Deployment sampling and serving-integrated evaluation for RL recipes       | Custom rollout, sampling, and evaluation logic through the managed service     |
| Preemption recovery and job resume                                       | Resume logic for supported recipe checkpoints                              | Resume policy and state restoration calls                                      |
| Distributed training (multi-node, sharding, FSDP)                        | Config surfaces for learning rate, grad accumulation, context length, W\&B | Hyperparameter schedules, data pipeline, and experiment tracking               |

## System architecture

<div aria-label="Training API lifecycle from a local Python loop through Fireworks training and sampling infrastructure">
  <div>
    <div>1 · Your laptop</div>
    <strong>Python loop</strong>

    <div>
      Loads data, builds batches, computes rewards, and controls the experiment.
    </div>
  </div>

  <div>
    <div>2 · Fireworks API</div>
    <strong>Control plane</strong>

    <div>
      Authenticates requests, routes operations, and manages the selected infrastructure.
    </div>
  </div>

  <div>
    <div>3 · Remote compute</div>
    <strong>GPU trainer</strong>

    <div>
      Runs forward passes, backward passes, and optimizer steps.
    </div>
  </div>

  <div>
    <div>4 · Separate compute</div>
    <strong>Sampling</strong>

    <div>
      Serves saved weights for rollouts and evaluation outside the trainer.
    </div>
  </div>

  <div>
    <div>5 · Persistent output</div>
    <strong>Artifacts</strong>

    <div>
      Stores sampler snapshots and resumable training state for later use.
    </div>
  </div>
</div>

Your Python process stays on your laptop throughout the run. It sends model operations to Fireworks and receives metrics or completions back. Sampling uses separate inference infrastructure rather than the trainer itself.

## How service-mode training works

<Warning>
  **Most common gotchas**

  * Remote operations such as `forward`, `forward_backward`, `optim_step`, sampling, and checkpoint saves return future-like results. Call `.result()` on operations that return one.
  * `token_weights=0` means prompt/no-loss tokens, `token_weights=1` means response/learned tokens.
  * `forward_backward_custom` computes gradients only; you still need `optim_step` to apply updates.
</Warning>

### Minimal training step lifecycle

The shape of the loop is the same on both infrastructures. Toggle between them to see what changes at each stage:

<TrainingLifecycle />

### Datums

A **Datum** is the unit of training data sent to the remote GPU. It wraps tokenized input and per-token weights that your loss function needs.

For SFT, token weight `0.0` marks prompt tokens and `1.0` marks response tokens. Cookbook renderers construct these weights from chat messages.

### Logprobs and forward\_backward\_custom

When you call `forward_backward_custom`, the GPU runs a forward pass and returns **per-token log-probabilities** as PyTorch tensors with `requires_grad=True`. Your loss function computes a scalar loss, the API calls `loss.backward()`, and gradients are sent back to the GPU for the model backward pass.

After accumulating gradients, call `optim_step` to apply the update. See the [Dedicated Training Quickstart](/fine-tuning/training-api/dedicated#quickstart) for one complete runnable Datum, loss, and optimizer loop.

### Futures

Remote training operations such as `forward`, `forward_backward`, `optim_step`, and checkpoint saves return **future-like results**. Call `.result()` on operations that return one so failures surface.

### Checkpointing and weight sync

After training, you export checkpoints for serving:

* **Base snapshot:** a complete chain anchor for the trainable state. For LoRA this is the adapter; for full-parameter training it is model weights.
* **Delta snapshot:** a change relative to a prior full-parameter base snapshot.

The SDK selects base versus delta automatically unless the recipe overrides it.

Checkpoint-to-sampler behavior depends on the infrastructure:

* **Serverless:** save a snapshot and bind an in-session sampling client to that snapshot. There is no deployment weight sync. See [Serverless Training](/fine-tuning/training-api/serverless).
* **Dedicated:** save a snapshot and refresh an SDK-managed deployment sampler, which syncs weights onto the deployment. See [Dedicated Training and Sampling](/fine-tuning/training-api/dedicated#training-and-sampling).

For dedicated RL rollouts that continue across weight sync, see [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts).

### Dedicated RL rollout transition mode

When a dedicated RL recipe provisions a hot-load rollout deployment, you can set `hot_load_transition_type` to `ASYNC` or `SYNC` in the SDK provisioning config or the cookbook rollout deployment config. Leave it unset to keep the recommended `ASYNC` default; set `SYNC` when a rollout must not span a weight transition. For the tradeoffs and KV-cache behavior, see [Async transition (recommended, default for RL)](/fine-tuning/rl-rollout-integration#async-transition-recommended-default-for-rl).

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

Chat-template formatting, stop-token handling, and loss-weight masking for SFT/DPO datasets are handled by **renderers** — pluggable per-model classes that turn raw conversations into the trainer's `Datum` shape. Most users never touch a renderer directly; cookbook recipes pick the right one for the `base_model` you set. If you need to author a new one or debug parity against HuggingFace, use the canonical training skill's [renderer implementation reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/renderer.md) and [verification reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/renderer-verification.md).

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

Let the SDK select automatically. LoRA snapshots contain the full adapter; full-parameter delta snapshots can accelerate synchronization but are not promotable. See [Saving and Loading](/fine-tuning/training-api/dedicated#saving-and-loading).

### Do I need to manage distributed training infra?

No. You implement training logic while Fireworks manages GPU provisioning and distributed infrastructure.

### Should I start with a Cookbook recipe or the Python SDK?

Start with a Cookbook recipe for most SFT, DPO, or GRPO adaptations. Use the Python SDK directly when you need custom loop semantics and full control.

### Can I evaluate serving behavior during training?

Yes. On serverless, save a snapshot and sample from it in the same session. On dedicated infrastructure, sync a snapshot to the SDK-managed deployment sampler and evaluate there.

### How should I compare Training API pricing vs a DIY bare-metal setup?

Use the framework in [Comparing Training API pricing vs DIY bare metal](#comparing-training-api-pricing-vs-diy-bare-metal). Focus on total iteration economics (cycle time, engineering overhead, utilization-adjusted cost, and quality-parity risk), then plug in your own assumptions.

### How can I compare rollout cost vs other providers?

See the [Price comparison vs Tinker](/fine-tuning/multi-turn-cost-comparison) calculator to estimate scenario-based costs on Fireworks Dedicated against Tinker's per-token pricing.

## Next steps

* [Dedicated quickstart](/fine-tuning/training-api/dedicated#quickstart) — run a minimal dedicated custom loop
* [Choose infrastructure](/fine-tuning/training-api/introduction#infrastructure) — compare serverless and dedicated training
* [Serverless Training](/fine-tuning/training-api/serverless) — shared pooled LoRA training
* [Dedicated Training](/fine-tuning/training-api/dedicated) — provisioned trainer and deployment lifecycle
* [Dedicated Training and Sampling](/fine-tuning/training-api/dedicated#training-and-sampling) — deployment-sampling lifecycle
* [Loss Functions](/fine-tuning/training-api/dedicated#loss-functions) — built-in and custom loss functions
* [Vision Inputs](/fine-tuning/models) — fine-tune vision-language models with image and text data
* [The Cookbook](/fine-tuning/training-api/cookbook/overview) — ready-to-run recipes for SFT, DPO, ORPO, GRPO/IGPO, and async RL (experimental)
