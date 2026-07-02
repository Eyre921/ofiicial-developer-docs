---
title: "The Cookbook"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/overview
path: fine-tuning/training-api/cookbook/overview
---

Ready-to-run training recipes for GRPO, DPO, SFT, and distillation built on top of the Training API.

## What is the Cookbook?

The [Fireworks Cookbook](https://github.com/fw-ai/cookbook/tree/main/training) is a collection of training recipes and utilities built on top of the [Training API](/fine-tuning/training-api/introduction). It provides config-driven training loops that handle trainer provisioning, data loading, tokenization, gradient accumulation, checkpointing, and cleanup automatically.

The cookbook is **optional** — everything it does can be done with the API directly. Use the cookbook when you want a working training loop quickly; use the API when you need full control.

## Installation

```bash theme={null}
git clone https://github.com/fw-ai/cookbook.git
cd cookbook/training && pip install -e .
```

Set your credentials:

```bash theme={null}
export FIREWORKS_API_KEY="your-api-key"
```

## Available recipes

| Recipe                           | Module                               | Use case                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RL** *(primary, experimental)* | `training.recipes.async_rl_loop`     | Reinforcement learning — you write a rollout function, the recipe owns the loop. Async rollout/training overlap by default; fully synchronous on-policy with `synchronous_training=True`. GRPO, importance sampling, DAPO, DRO, GSPO, CISPO. See [Cookbook RL](/fine-tuning/training-api/cookbook/rl). **No backward-compatibility guarantee.** |
| **RL** *(simpler, synchronous)*  | `training.recipes.rl_loop`           | Synchronous on-policy GRPO scaffold — reach for it when you want the server-side fast loss path or don't need rollout/train overlap                                                                                                                                                                                                             |
| **IGPO**                         | `training.recipes.igpo_loop`         | Information Gain-based Policy Optimization — turn-level IG rewards for multi-turn agent trajectories (extends GRPO)                                                                                                                                                                                                                             |
| **DPO**                          | `training.recipes.dpo_loop`          | Direct preference optimization from chosen/rejected pairs                                                                                                                                                                                                                                                                                       |
| **SFT**                          | `training.recipes.sft_loop`          | Supervised fine-tuning with cross-entropy loss                                                                                                                                                                                                                                                                                                  |
| **Distillation**                 | `training.recipes.distillation_loop` | On-policy distillation with sampled-token OPD, routed multi-teacher MOPD, and top-K SDFT                                                                                                                                                                                                                                                        |
| **ORPO**                         | `training.recipes.orpo_loop`         | Odds ratio preference optimization                                                                                                                                                                                                                                                                                                              |

Each recipe follows the same pattern: import `Config` and `main`, set your config, and call `main(cfg)`. Trainer and deployment provisioning is handled internally by the recipe — you describe *what* you want with `TrainerConfig` / `DeployConfig`, and the SDK attaches or creates the resources.

All launch examples below use `trainer=TrainerConfig(training_shape_id=...)` for explicit shape selection. Cookbook recipes can also auto-select validated shapes when `training_shape_id` is unset. The main run-level trainer knob you may set alongside a shape is `replica_count` for replicated HSDP launches; reference shapes can usually be left unset because the cookbook auto-selects or uses a shared-session reference when appropriate.

If you want field-level details about what a training shape controls and what stays configurable, see [Training Shapes](/fine-tuning/training-api/training-shapes) and the [Cookbook Reference](/fine-tuning/training-api/cookbook/reference).

<Note>
  `InfraConfig` and the standalone `setup_infra` / `ResourceCleanup` helpers are **deprecated and removed from the recipe surface**. Recipes now take `trainer=TrainerConfig(...)` (and `deployment=DeployConfig(...)` for RL). See [Migrating from the deprecated managed infra](/fine-tuning/training-api/cookbook/reference#deprecated-managed-infra-infraconfig).
</Note>

## Quick example: SFT

```python theme={null}
from training.recipes.sft_loop import Config, main
from training.utils import TrainerConfig

cfg = Config(
    log_path="./sft_quickstart",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/training_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    trainer=TrainerConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
)

main(cfg)
```

## Quick example: GRPO

```python theme={null}
from training.recipes.rl_loop import Config, main
from training.utils import DeployConfig, TrainerConfig

cfg = Config(
    log_path="./grpo_quickstart",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/prompts.jsonl",
    max_rows=100,
    trainer=TrainerConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
    deployment=DeployConfig(
        deployment_id="grpo-serving",
        tokenizer_model="Qwen/Qwen3-8B",
    ),
    weight_sync_interval=1,
)

main(cfg)
```

## W\&B logging

All cookbook recipes accept a `WandBConfig` to stream metrics to [Weights & Biases](https://wandb.ai):

```python theme={null}
from training.utils import WandBConfig

cfg = Config(
    # ... same config as above ...
    wandb=WandBConfig(
        entity="my-team",
        project="grpo-experiment",
        run_name="qwen3-8b-sft-v1",  # optional, auto-generated if omitted
    ),
)

main(cfg)
```

## Vision-language model support

All cookbook recipes support VLM fine-tuning. Use a VLM training shape and tokenizer, and provide multimodal datasets with `image_url` content. See [Vision Inputs](/fine-tuning/training-api/vision-inputs) for dataset format and examples.

## Next steps

* [Cookbook SFT](/fine-tuning/training-api/cookbook/sft) — supervised fine-tuning
* [Cookbook DPO](/fine-tuning/training-api/cookbook/dpo) — preference optimization with pairwise data
* [Cookbook RL (GRPO)](/fine-tuning/training-api/cookbook/rl) — full GRPO walkthrough with reward functions
* [Cookbook Distillation](/fine-tuning/training-api/cookbook/distillation) — OPD, routed MOPD, and top-K SDFT
* [Vision Inputs](/fine-tuning/training-api/vision-inputs) — fine-tune VLMs with image and text data
* [Cookbook Reference](/fine-tuning/training-api/cookbook/reference) — all config classes and parameters
