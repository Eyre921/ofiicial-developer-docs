---
title: "Dedicated Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/dedicated
path: fine-tuning/training-api/dedicated
---

Run Training API workloads with provisioned trainer and deployment resources, explicit checkpoints, and lifecycle control.

<Info>
  The Training API is currently in **private preview**. [Request access](https://fireworks.ai/contact-training) before running this guide.
</Info>

Dedicated training provisions trainer and deployment resources for your run. Use it when you need broader model or method support, full-parameter training, DPO, sustained RL, explicit checkpoint resume, or control over rollout and evaluation deployments.

If LoRA SFT or RL on the shared pool is sufficient, compare this path with [Serverless Training](/fine-tuning/training-api/serverless) before provisioning resources.

<Tip>
  **Start from the cookbook.** Clone [`fw-ai/cookbook`](https://github.com/fw-ai/cookbook), then fork the closest recipe under [`training/recipes/`](https://github.com/fw-ai/cookbook/tree/main/training/recipes). Recipes own provisioning, checkpoints, reconnect, and sampling where applicable. Cleanup is configuration-specific; review and set each recipe's cleanup flags before launch.
</Tip>

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

## Dedicated training steps

### Step 1: Install the SDK and cookbook

```bash theme={null}
git clone https://github.com/fw-ai/cookbook
cd cookbook
pip install -e ./training
export FIREWORKS_API_KEY="fw_..."
```

Check the SDK requirement declared by your cookbook revision:

```bash theme={null}
grep 'fireworks-ai\[training\]' training/pyproject.toml
pip show fireworks-ai | grep -i version
```

### Step 2: Choose the closest recipe

| Task                              | Start here                                                                                                                   |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| SFT                               | [`training/recipes/sft_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/sft_loop.py)                   |
| DPO                               | [`training/recipes/dpo_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/dpo_loop.py)                   |
| ORPO                              | [`training/recipes/orpo_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/orpo_loop.py)                 |
| RL                                | [`training/recipes/rl_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/rl_loop.py)                     |
| Async or agentic RL, experimental | [`training/recipes/async_rl_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/async_rl_loop.py)         |
| Distillation                      | [`training/recipes/distillation_loop.py`](https://github.com/fw-ai/cookbook/blob/main/training/recipes/distillation_loop.py) |

Fork the recipe and change only the task-specific data, loss, reward, rollout, evaluation, or configuration.

For a complete bounded SFT smoke using the bundled text-to-SQL dataset:

```bash theme={null}
python training/examples/sft/train_sft.py \
  --output-model-id dedicated-sft-smoke \
  --max-examples 10 \
  --epochs 1 \
  --lora-rank 8 \
  --training-shape accounts/fireworks/trainingShapes/<shape>
```

This command creates paid trainer resources. Replace `<shape>`, then review the
model, shape, parameters, cost ceiling, and cleanup flags before running it.

### Step 3: Choose the model and training shape

Use the live [Training Shapes](/fine-tuning/training-api/training-shapes) catalog. Pass the full shared shape ID and let the SDK resolve its validated version and linked deployment shape.

Do not copy accelerator type, GPU count, image tag, or deployment-shape details into the config when the training shape owns them.

### Step 4: Configure stable run outputs

Record:

* cookbook commit and installed SDK version;
* account, base model, recipe, and dataset;
* complete configuration, including defaults;
* training shape and linked deployment shape;
* stable trainer, output-model, and deployment IDs where the API exposes them;
* checkpoint cadence and resume policy;
* cost ceiling, success metric, and teardown policy.

### Step 5: Provision the SDK-managed service

Cookbook recipes provision through the SDK-managed service. If you are writing a direct loop, follow the exact [`FiretitanServiceClient.from_firetitan_config(...)` quickstart](/fine-tuning/training-api/quickstart#step-1-create-the-managed-service).

Provisioning happens on the first client creation. Capture `service.trainer_job_id` and every rollout or evaluation deployment ID immediately.

### Step 6: Train and monitor

Run the forked recipe. Monitor:

* trainer state and real optimizer-step progress;
* recipe metrics and W\&B when configured;
* rollout success, reward distribution, and sampler latency for RL;
* checkpoints and deployment weight-sync state;
* quota, billing, and capacity separately.

State alone is not proof of progress. Use a bounded no-progress interval and preserve IDs and timestamps for escalation.

### Step 7: Save, sample, and evaluate

Save weights for the sampler, create or refresh the SDK-managed sampler, and evaluate the base and tuned policy on the same held-out set.

For checkpoint and sampler details, see [Saving and Loading](/fine-tuning/training-api/saving-and-loading) and [Training and Sampling](/fine-tuning/training-api/training-and-sampling).

### Step 8: Promote the selected checkpoint

List checkpoints from the control plane, choose a row marked promotable, validate the output model ID, and promote the full checkpoint resource name.

Do not choose a winner from training loss alone. Use the agreed held-out metric or evaluator.

### Step 9: Deploy and prove serving

Create the final on-demand deployment, wait for `READY`, then send a real request. `READY` without a successful response is not serving proof.

Fine-tuned LoRA adapters are served through an on-demand deployment, not the shared serverless inference catalog.

### Step 10: Tear down

Set the recipe's cleanup flags explicitly. Close the SDK-managed service in `try/finally`, then verify every trainer and deployment reached the requested final state. Resources are not deleted or scaled down unless the configuration requests it. Use the complete [Cleanup and Teardown](/fine-tuning/training-api/reference/cleanup) contract.

Checkpoint storage and promoted models can remain after compute teardown. Report them separately from billable trainer and deployment resources.

## Compare infrastructure

For the canonical decision rules and comparison table, see [Choose Serverless or Dedicated Training](/fine-tuning/training-api/choose-infrastructure).

## Next steps

* [Dedicated quickstart](/fine-tuning/training-api/quickstart)
* [Training and Sampling](/fine-tuning/training-api/training-and-sampling)
* [Training Shapes](/fine-tuning/training-api/training-shapes)
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading)
* [Cookbook overview](/fine-tuning/training-api/cookbook/overview)
* [Cleanup and Teardown](/fine-tuning/training-api/reference/cleanup)
