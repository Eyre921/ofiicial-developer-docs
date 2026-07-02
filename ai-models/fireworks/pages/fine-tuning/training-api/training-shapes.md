---
title: "Training Shapes"
source: https://docs.fireworks.ai/fine-tuning/training-api/training-shapes
path: fine-tuning/training-api/training-shapes
---

Pre-configured GPU and model training profiles that simplify distributed training setup.

# Training Shapes

In practice, a training shape is the user-facing launch input for trainer jobs. Most users only need to choose a training shape ID such as `accounts/fireworks/trainingShapes/qwen3p5-9b-256k` and pass it to the API.

<Warning>
  **A training shape is the recommended launch path for normal trainer jobs.** In most cases, pass the full shared shape path  as `training_shape_id`, and the SDK resolves the pinned version for you. Advanced compatibility launches can still use manager-level shape refs and direct infra fields, but use that path only when you know the exact hardware and image configuration.
</Warning>

The `fireworks` account is the shared public shape catalog. Shapes published under  can be referenced by all users.

You do not need to know the versioned shape reference, image tag, GPU layout, or linked deployment shape ahead of time. The API resolves those details internally.

## What You Need To Know

For most users, the workflow is:

1. Pick a training shape ID from the available shapes list below. In most cases this should be the full shared path .
2. Pass it as `training_shape_id` to a cookbook recipe's `TrainerConfig`, or to `FiretitanServiceClient.from_firetitan_config(...)`.
3. Let the SDK resolve the pinned shape version and linked deployment shape.

That is the only shape-specific value you choose yourself.

## What A Training Shape Controls

When you specify a training shape, it provides the trainer with:

* GPU and node layout: `acceleratorType`, `acceleratorCount`, `nodeCount`
* Model limits: `maxSupportedContextLength`
* Trainer runtime: `trainerImageTag`
* Linked serving setup: `deploymentShapeVersion`

## What You Can And Can't Change

You can still configure normal training-loop fields such as:

* `base_model`
* `lora_rank`
* `learning_rate`
* `display_name`
* Trainer replica count (`TrainerConfig.replica_count` or `trainer_replica_count`)
* Deployment replica count (`DeployConfig.replica_count` or `replica_count`)

<Note>
  Shape-owned infra is locked. Do not try to override `accelerator_type`, `accelerator_count`, `node_count`, `custom_image_tag`, or the linked deployment shape.
</Note>

Gradient accumulation is not a trainer-launch setting. To accumulate gradients, call `forward_backward...` multiple times from your client loop before a single `optim_step(...)`; see [Loss Functions](/fine-tuning/training-api/loss-functions#applying-the-optimizer-step).

For field-level behavior and dataclass details, see the [`FiretitanServiceClient`](/fine-tuning/training-api/reference/service-client) and [Cookbook Reference](/fine-tuning/training-api/cookbook/reference).

## Using a Training Shape

The only shape-specific input you provide is the shape ID:

1. **You provide the shape ID** (e.g. `accounts/fireworks/trainingShapes/qwen3p5-9b-256k`) — no version needed.
2. **The SDK resolves the latest validated version** during managed service provisioning.
3. **The SDK applies the linked deployment shape** when you request a sampler deployment.

Pass the shape ID to the managed service:

```python theme={null}
from fireworks.training.sdk import FiretitanServiceClient

shape_id = "accounts/fireworks/trainingShapes/qwen3p5-9b-256k"

service = FiretitanServiceClient.from_firetitan_config(
    api_key=api_key,
    base_model="accounts/fireworks/models/qwen3p5-9b",
    training_shape_id=shape_id,
    lora_rank=0,
    create_deployment=False,
)
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3p5-9b",
    lora_rank=0,
)
```

<Warning>
  Use the full training shape ID including the account prefix (for example `accounts/fireworks/trainingShapes/qwen3p5-9b-256k`). The `fireworks` account is the shared public account for training shapes, and you do **not** need to hand-write a versioned `training_shape_ref` yourself.
</Warning>

## Available Training Shapes

Below is a searchable catalog of customer-ready training shapes per model. During Reinforcement Fine-Tuning (RFT), two types of models are often deployed: a **policy trainer** (which updates its weights) and a **reference model** (which is forward-only).

* **Policy trainer shapes** are used for standard Supervised Fine-Tuning (SFT) or as the active policy model during Reinforcement Learning (RL).
* **LoRA trainer shapes** are used for parameter-efficient fine-tuning.
* **Forward-only / reference shapes** are used for reference models in RL pipelines. They do not require optimizer states or backward passes, and thus often require fewer resources.

The **Surfaces** column shows whether each shape supports direct **API** training jobs, customer-facing **Managed** training (SFT/DPO/RFT webapp), or both — based on model tunability, shape readiness, and linked deployment configuration.

Select a model from the dropdown to view the **Training method support** matrix (SFT / DPO / RFT × LoRA / Full-Param) with per-method surfaces and total GPU requirements, plus the backing training shapes for that model.

<TrainingShapesCatalog />
