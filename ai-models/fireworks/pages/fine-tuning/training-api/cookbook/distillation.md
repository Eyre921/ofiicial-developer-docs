---
title: "Cookbook: Distillation"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/distillation
path: fine-tuning/training-api/cookbook/distillation
---

On-policy distillation and top-K self-distillation recipes.

## What this is

The cookbook's `training.recipes.distillation_loop` trains one student from its own rollouts while a frozen teacher scores those same responses.

Use it when you want recipe-managed trainer provisioning, student sampling, teacher scoring, checkpointing, and cleanup for distillation experiments.

## Recipes

| Recipe | Teacher signal |
| - | - |
| `distillation_loop` | Sampled-token OPD: teacher logprob minus sampling logprob on the student's own completions. |
| `sdft_loop` | Top-K self-distillation on serverless, with privileged answer context. |

SDFT is a separate recipe and requires `pip install -e '.[sdft]'`; it is not a
`distill_mode` flag on `distillation_loop`. See the [distillation skill](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/sdk-distillation.md)
for teacher setup and algorithm details.

## Minimal example

```python theme={null}
from training.recipes.distillation_loop import Config, main
from training.utils import DeployConfig, TrainerConfig

cfg = Config(
    log_path="./distillation_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    teacher_model="accounts/fireworks/models/qwen3-32b",
    dataset="/path/to/prompts.jsonl",
    trainer=TrainerConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    ),
    deployment=DeployConfig(tokenizer_model="Qwen/Qwen3-8B"),
    max_rows=100,
    epochs=1,
)

main(cfg)
```

If `teacher_model` is a base model resource, the recipe creates a frozen teacher deployment for scoring. If it is already an inference model or deployment resource, the recipe uses it directly.

## Multi-teacher runs

The current OPD recipe uses one frozen teacher. Fork its loop to route prompts
to multiple teachers.

## Dataset contract

Rows are JSONL objects. The only required field is `messages`, the student-visible OpenAI-style chat prompt.

Optional fields:

| Field | Use |
| - | - |
| `teacher_messages` | Teacher-side prompt for privileged-context scoring. If omitted, the teacher scores under `messages`. |
| `expected_answer` | Optional metadata for eval callbacks and smoke checks. |

Student and teacher token IDs must use a compatible tokenizer and vocabulary. Prefer teachers from the same model family, and use a matching tokenizer for `DeployConfig.tokenizer_model`.

## Examples

The cookbook includes distillation examples under `training/examples/distillation`:

| Example | Path | Use |
| - | - | - |
| Privileged-context OPD | `gsm8k_privileged` | Student sees the problem; teacher can see privileged solution context. |
| Serverless privileged distillation | `serverless_k3_privileged` | LoRA student trained from teacher scores on a privileged prompt. |

Run from the cookbook repository:

```bash theme={null}
cd training
FIREWORKS_API_KEY=... \
python -m training.examples.distillation.gsm8k_privileged.train_gsm8k_privileged --help
```

## Next steps

* [Cookbook Reference](/fine-tuning/training-api/cookbook/reference) - config classes and common recipe fields
* [Loss Functions](/fine-tuning/training-api/dedicated#loss-functions) - built-in and custom Training API losses
* [Weight sync](/fine-tuning/training-api/cookbook/reference#weight-sync) - how updated weights reach serving deployments
