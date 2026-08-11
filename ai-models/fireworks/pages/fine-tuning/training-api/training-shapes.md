---
title: "Training Shapes"
source: https://docs.fireworks.ai/fine-tuning/training-api/training-shapes
path: fine-tuning/training-api/training-shapes
---

Pre-configured GPU and model training profiles that simplify distributed training setup.

In practice, a training shape is the user-facing launch input for trainer jobs. Most users only need to choose a training shape ID such as `accounts/fireworks/trainingShapes/qwen3-8b-128k` and pass it to the API as `training_shape_id`.

The `fireworks` account is the shared public shape catalog. Shapes published under `accounts/fireworks/trainingShapes/<shape>` can be referenced by all users. [See the full training shapes catalog here](/fine-tuning/models#model-availability).

You do not need to know the versioned shape reference, image tag, GPU layout, or linked deployment shape ahead of time. The API resolves those details internally.

## Concepts

**Training shape.** A validated trainer configuration for one base model and one training method. It fixes the GPU layout for each trainer replica and the training context limit for that model and method. Shapes exist so you do not have to size distributed training yourself.

**Shape ID vs. shape version.** The shape ID is the stable name you pass, such as `accounts/fireworks/trainingShapes/qwen3-8b-128k`. Behind it sits a series of pinned versions holding the exact GPU counts, context limit, and trainer image. You pass the ID; the API resolves the validated version at launch.

**Training shape vs. deployment shape.** A training shape configures the trainer. Each one links to a deployment shape that configures the inference instance used for RL rollouts / sampling, and on the shape path that linked shape owns the deployment's GPU type, node count, and serving engine configuration. You normally do not name a deployment shape at all, because the API reads it from the training shape's `deploymentShapeVersion`.

**Training method.** Each shape declares one training method, either LoRA or full-parameter, and a model may offer both. Your `lora_rank` must agree with the method the shape declares: `0` for a full-parameter shape, a positive integer for a LoRA shape. These are not two independent settings. Changing `lora_rank` does not convert a shape to the other method, because the method is part of the profile the shape was validated for and it affects the GPU layout and context limit the shape carries.

Read the method off the shape card before you launch. For the same model, the LoRA shape and the full-parameter shape often differ in both GPU count and maximum context, so the two are rarely interchangeable.

## What You Need To Know

For most users, the workflow is:

1. Pick a training shape ID from the per-model shape cards in the [model catalog](/fine-tuning/models#model-availability). In most cases this should be the full shared path `accounts/fireworks/trainingShapes/<shape>`.
2. Pass it as `training_shape_id` to a cookbook recipe's `TrainerConfig`, or to `FiretitanServiceClient.from_firetitan_config(...)`.
3. Let the API resolve the pinned shape version and linked deployment shape.

The shape ID is normally the only shape-specific value you set. Everything else about the shape is resolved for you.

Whether you can skip the shape ID depends on which of the two paths you use:

* **Cookbook recipe.** You can leave `training_shape_id` unset, and the recipe picks a validated shape for you from your `base_model`, `lora_rank`, and `max_seq_len`.
* **`FiretitanServiceClient` directly.** Set the shape ID yourself. The recipe layer is what does the picking, so there is nothing to pick for you here.

On either path, set the shape ID yourself when you need a specific GPU layout or context limit.

## What A Training Shape Controls

A validated shape version can pin every field below. Together these are the launch profile, and none of them are yours to set. The hardware fields size one trainer replica: `acceleratorCount` × `nodeCount` is the GPU count for a single replica.

| Field                       | What it pins                                                                                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `baseModel`                 | The single base model this shape is validated for. A shape is not portable to another model.                                                                             |
| `trainerMode`               | The training method, shown as Full-Param or LoRA in the catalog.                                                                                                         |
| `acceleratorType`           | The GPU type, such as B200 or B300.                                                                                                                                      |
| `acceleratorCount`          | GPUs per node.                                                                                                                                                           |
| `nodeCount`                 | Nodes per trainer replica.                                                                                                                                               |
| `minTotalAcceleratorCount`  | The smallest total world size, across all data-parallel replicas, that the shape has been validated at, when validation recorded one.                                    |
| `trainerShardingScheme`     | The sharding and parallelism profile validated for the trainer launch.                                                                                                   |
| `baseModelWeightPrecision`  | The precision for base weights during training, when the shape sets one. `BFLOAT16` applies no quantization; `FP8`, `FP4_FP8`, `INT8`, and `NF4` are quantized variants. |
| `maxSupportedContextLength` | The validated training context limit for this model and method.                                                                                                          |
| `trainerImageTag`           | The validated trainer runtime image.                                                                                                                                     |
| `deploymentShapeVersion`    | The linked deployment shape version used for rollouts and sampling.                                                                                                      |

The shape resource also carries metadata that does not affect a launch: `name`, `displayName`, `description`, `createTime`, `updateTime`, `modelType`, and `parameterCount`.

Total GPUs for a run are the shape's per-replica GPUs multiplied by your replica count, so a 4-GPU shape launched with `replica_count=2` consumes 8 GPUs.

For example, `qwen3-8b-128k` is the full-parameter shape for Qwen 3 8B. Below is version `vnuk8fdq` in full.

| Field                       | Value in version `vnuk8fdq`                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| `name`                      | `accounts/fireworks/trainingShapes/qwen3-8b-128k`                           |
| `baseModel`                 | `accounts/fireworks/models/qwen3-8b`                                        |
| `trainerMode`               | `POLICY_TRAINER`, shown as Full-Param in the catalog. Use `lora_rank=0`.    |
| `acceleratorType`           | `NVIDIA_B200_180GB`, shown as B200                                          |
| `acceleratorCount`          | `4`                                                                         |
| `nodeCount`                 | `1`                                                                         |
| `trainerShardingScheme`     | Tensor 1, pipeline 1, context 4, expert 1, sequence parallelism not enabled |
| `maxSupportedContextLength` | `128000`, shown as 128K (128,000 tokens)                                    |
| `baseModelWeightPrecision`  | `WEIGHT_PRECISION_UNSPECIFIED`, so this shape does not pin a precision      |
| `minTotalAcceleratorCount`  | Not set on this shape                                                       |
| `trainerImageTag`           | `0.383.0`                                                                   |
| `deploymentShapeVersion`    | `accounts/fireworks/deploymentShapes/rft-qwen3-8b/versions/gyiqbrd6`        |

To read the same fields for the version you will actually launch on:

```bash theme={null}
firectl training-shape-version get \
  accounts/fireworks/trainingShapes/qwen3-8b-128k/versions/latest
```

## What You Can And Can't Change

You can still configure normal training-loop fields such as:

* `lora_rank`, which must match the shape's training method
* `learning_rate`
* Trainer replica count (`TrainerConfig.replica_count` or `trainer_replica_count`)
* Deployment replica count (`DeployConfig.replica_count` or `replica_count`)

<Note>
  Shape-owned infra is locked on the shape path. Do not set `accelerator_type`, `accelerator_count`, `node_count`, or `custom_image_tag`; the shape supplies all four. The linked deployment shape can be overridden through `deployment_shape`, but only for deployments you manage outside the normal flow.
</Note>

Gradient accumulation is not a trainer-launch setting. To accumulate gradients, call `forward_backward...` multiple times from your client loop before a single `optim_step(...)`; see [Loss Functions](/fine-tuning/training-api/dedicated#loss-functions).

For field-level behavior and dataclass details, see the [`FiretitanServiceClient`](/fine-tuning/training-api/reference/service-client) and [Cookbook Reference](/fine-tuning/training-api/cookbook/reference).

## Using a Training Shape

At launch, the shape ID resolves in three steps:

1. **You provide the shape ID** (e.g. `accounts/fireworks/trainingShapes/qwen3-8b-128k`), with no version needed.
2. **The API resolves the latest validated version** when the service client provisions the trainer.
3. **The API applies the linked deployment shape** when you request a sampler deployment.

Pass the shape ID to the SDK-managed service client (`FiretitanServiceClient`):

```python theme={null}
from fireworks.training.sdk import FiretitanServiceClient

shape_id = "accounts/fireworks/trainingShapes/qwen3-8b-128k"

service = FiretitanServiceClient.from_firetitan_config(
    api_key=api_key,
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_id=shape_id,
    lora_rank=0,
    create_deployment=False,
)
training_client = service.create_training_client(
    base_model="accounts/fireworks/models/qwen3-8b",
    lora_rank=0,
)
```

*Note: You do not need to hand-write a versioned `training_shape_ref` yourself. Advanced compatibility launches can still use manager-level shape refs and direct infra fields, but take that path only when you know the exact hardware and image configuration.*

## Model and shape availability

See the [Models](/fine-tuning/models) page for the searchable per-model matrix and training method support.
