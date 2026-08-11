---
title: "Dedicated Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/dedicated
path: fine-tuning/training-api/dedicated
---

Run Training API workloads with provisioned trainer and deployment resources, explicit checkpoints, and lifecycle control.

<Info>
  The Training API is currently in **private preview**. [Request access](https://fireworks.ai/contact-training) before running this guide.
</Info>

Dedicated training provisions trainer and deployment resources for your run. Use it when you need broader model or method support, full-parameter training, ORPO or distillation, sustained RL, explicit checkpoint resume, or control over rollout and evaluation deployments.

If LoRA SFT, DPO, or RL on the shared pool is sufficient, compare this path with [Serverless Training](/fine-tuning/training-api/serverless) before provisioning resources.

<Tip>
  **Start from the cookbook.** Clone [`fw-ai/cookbook`](https://github.com/fw-ai/cookbook), fork the closest recipe under [`training/recipes/`](https://github.com/fw-ai/cookbook/tree/main/training/recipes), and use the [Fireworks training skill](https://github.com/fw-ai/cookbook/tree/main/skills/fireworks-training) for losses, checkpoints, and debugging depth.
</Tip>

## How dedicated training runs

<div aria-label="Dedicated Training lifecycle using provisioned trainer and inference resources">
  <div>
    <div>1 · Local</div>
    <strong>Your Python loop</strong>
    <div>Controls data, losses, rewards, and experiment logic.</div>
  </div>

  <div>
    <div>2 · Provisioned</div>
    <strong>Dedicated trainer</strong>
    <div>Runs remote model and optimizer operations on the selected shape.</div>
  </div>

  <div>
    <div>3 · Persistent</div>
    <strong>Training artifacts</strong>
    <div>Stores sampler snapshots or resumable training state.</div>
  </div>

  <div>
    <div>4 · Optional</div>
    <strong>Inference deployment</strong>
    <div>Loads sampler weights for rollouts and evaluation.</div>
  </div>

  <div>
    <div>5 · Explicit</div>
    <strong>Promote and clean up</strong>
    <div>Register the selected model, then release billable compute.</div>
  </div>
</div>

The trainer and inference deployment are separate resources with separate billing and cleanup. Promotion registers a model but does not deploy it.

## What you can run

<CardGroup>
  <Card title="SFT, DPO, and ORPO" icon="messages">
    Use cookbook recipes with LoRA or full-parameter configurations supported by the selected training shape.
  </Card>

  <Card title="RL and RFT" icon="brain">
    Run synchronous or asynchronous rollouts with custom rewards, losses, environments, and deployment sampling.
  </Card>

  <Card title="Distillation" icon="arrows-left-right">
    Provision student and teacher resources for sampled reverse KL, top-k forward KL, and related workflows.
  </Card>

  <Card title="Custom loops" icon="code">
    Use the Tinker-compatible training client directly when a maintained recipe does not express the required behavior.
  </Card>
</CardGroup>

<h2>
  Dedicated training quickstart
</h2>

### Step 1: Install the SDK and cookbook

```bash theme={null}
git clone https://github.com/fw-ai/cookbook
cd cookbook
pip install -e ./training
export FIREWORKS_API_KEY="fw_..."
```

### Step 2: Choose the closest recipe

| Task         | Start here                                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| SFT          | [`sft_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/sft_loop.py)                   |
| DPO          | [`dpo_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/dpo_loop.py)                   |
| RL           | [`rl_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/rl_loop.py)                     |
| Async RL     | [`async_rl_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/async_rl_loop.py)         |
| Distillation | [`distillation_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/distillation_loop.py) |

Smoke test (bounded SFT):

```bash theme={null}
python training/examples/sft/train_sft.py \
  --output-model-id dedicated-sft-smoke \
  --max-examples 10 --epochs 1 --lora-rank 8 \
  --training-shape accounts/fireworks/trainingShapes/<shape>
```

### Step 3: Pick model and shape

Choose a shape from [Models](/fine-tuning/models). Pass the full shared shape ID as `training_shape_id`; the SDK resolves the validated version and linked deployment shape.

### Step 4–10: Train, checkpoint, promote, deploy, tear down

Follow the forked recipe. Record trainer and deployment IDs, checkpoint cadence, and cleanup flags before launch.

<h2>
  Training and sampling lifecycle
</h2>

Dedicated recipes use two independently billed resources:

1. Create or reconnect to a trainer from the selected training shape.
2. Create an inference deployment when the loop needs rollouts or evaluation.
3. Run one or more forward/backward calls, then apply one optimizer step.
4. Save sampler weights and refresh the deployment before collecting new rollouts.
5. Save resumable state on the approved cadence, promote the selected checkpoint, then delete or scale down billable resources.

Keep stable trainer and deployment IDs so retries reconnect instead of provisioning duplicates. The trainer owns optimization state; the deployment owns serving and sampling.

<h2>
  Loss functions
</h2>

| Need                   | Start from                                                             |
| ---------------------- | ---------------------------------------------------------------------- |
| SFT                    | `sft_loop.py` and its weighted token objective                         |
| DPO or ORPO            | `dpo_loop.py` or `orpo_loop.py`                                        |
| Standard RL            | `rl_loop.py` or `async_rl_loop.py`                                     |
| New research objective | Fork the closest recipe and use `forward_backward_custom` deliberately |

Call forward/backward multiple times before one `optim_step()` for gradient accumulation. Validate datum fields, token masks, and normalization locally. Detailed loss and datum routing lives in the [Training API losses skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/training-api-losses.md).

<h2>
  Saving and loading
</h2>

Dedicated training has three distinct checkpoint purposes:

| Purpose               | Contains                    | Use                                               |
| --------------------- | --------------------------- | ------------------------------------------------- |
| Sampler snapshot      | Weights for inference       | Refresh a rollout or evaluation deployment        |
| Resumable state       | Weights and optimizer state | Continue an interrupted training run              |
| Promotable checkpoint | Deployable model artifact   | Register the selected result as a Fireworks model |

Do not pass a sampler snapshot to a resumable-state API. Keep the same trainer ID and log path for exact continuation; use the recipe's explicit initialization option for a new job. See the [checkpoint skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-checkpoints.md).

## Deep dives (cookbook skill)

| Topic                                 | Skill reference                                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Losses, datums, gradient accumulation | [training-api-losses](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/training-api-losses.md) |
| Checkpoints, resume, promote          | [sdk-checkpoints](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-checkpoints.md)         |
| Custom RL objectives                  | [rl-custom-loss](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-custom-loss.md)           |
| Async RL and concurrency              | [rl-async](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-async.md)                       |
| Recipe catalog                        | [sdk-recipes](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-recipes.md)                 |

Config class reference (short): [Cookbook Reference](/fine-tuning/training-api/cookbook/reference).

## Compare infrastructure

See [Serverless vs dedicated](/fine-tuning/training-api/introduction#infrastructure).

## Next steps

<CardGroup>
  <Card title="Cookbook overview" icon="book" href="/fine-tuning/training-api/cookbook/overview">
    Recipe entry points
  </Card>

  <Card title="Training Shapes" icon="microchip" href="/fine-tuning/training-api/training-shapes">
    What a shape pins
  </Card>

  <Card title="Models" icon="table" href="/fine-tuning/models">
    Per-model shape catalog
  </Card>

  <Card title="Cleanup" icon="broom" href="/fine-tuning/training-api/reference/cleanup">
    Teardown contract
  </Card>
</CardGroup>
