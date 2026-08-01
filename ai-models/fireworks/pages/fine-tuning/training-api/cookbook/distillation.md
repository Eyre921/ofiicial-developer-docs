---
title: "Cookbook: Distillation"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/distillation
path: fine-tuning/training-api/cookbook/distillation
---

On-policy distillation recipes with one or more frozen teachers.

## What this is

The cookbook's `training.recipes.distillation_loop` trains one student from its own rollouts while frozen teacher deployments score those same responses.

Use it when you want recipe-managed trainer provisioning, student sampling, teacher scoring, checkpointing, and cleanup for distillation experiments.

## Modes

| Mode                 | Use when                                                   | Teacher signal                                 | Training loss                         |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------- | ------------------------------------- |
| `sampled_reverse_kl` | You want OPD-style sampled-token distillation              | Teacher logprob on each sampled response token | `importance_sampling`                 |
| `topk_forward_kl`    | You want sparse SDFT soft labels from teacher top-K tokens | Teacher `top_logprobs=K` per response position | `cross_entropy` with `[N, K]` targets |

`sampled_reverse_kl` is the default. The student samples on policy, the teacher scores the sampled tokens, and the recipe trains on the dense per-token gap:

```text theme={null}
teacher_logprob - sampling_logprob
```

For `topk_forward_kl`, set `distill_mode=DistillMode.TOPK_FORWARD_KL` and `sdft_top_k`.

## Current limits and logprobs

The distillation recipe depends on the public inference `logprobs` response:

| Field or request option | Meaning                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `top_k`                 | Request-side sampling filter. It limits which next-token logits remain eligible for sampling and redistributes probability mass over that set.                                     |
| `sampling_mask`         | Optional request flag for generated tokens. It can return the count or token IDs still eligible after sampling filters such as `top_p` and `top_k`.                                |
| `logprob`               | Model logprob for the returned token before sampling-temperature and sampling-filter renormalization. In the legacy response, this is `token_logprobs`.                            |
| `sampling_logprob`      | Generation-only logprob of the sampled token after temperature and sampling filters are applied. Use this when comparing against the distribution that actually sampled the token. |
| `top_logprobs`          | Response option for returning likely alternatives at each position. The public inference API currently caps this at `5`, so `sdft_top_k` must be at most `5`.                      |

`top_k` and `top_logprobs` are different knobs: `top_k` changes sampling; `top_logprobs` only controls how many alternatives are returned in the response.

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

Set `multi_teacher=MultiTeacherConfig(...)` when you have more than one teacher.

With `sampled_reverse_kl`, multi-teacher OPD is routed: each dataset row is scored by exactly one teacher selected by the configured route key, defaulting to `teacher`. With `topk_forward_kl`, every configured teacher can score the sampled response and the recipe blends sparse top-K probability mass using `TeacherConfig.blend_weight`.

## Dataset contract

Rows are JSONL objects. The only required field is `messages`, the student-visible OpenAI-style chat prompt.

Optional fields:

| Field              | Use                                                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `teacher`          | Default route key for routed sampled reverse-KL MOPD. The value must match a configured `TeacherConfig.route_value`, or the teacher `model` when `route_value` is unset. |
| `teacher_messages` | Teacher-side prompt for privileged-context scoring. If omitted, the teacher scores under `messages`.                                                                     |
| `expected_answer`  | Optional metadata for eval callbacks and smoke checks.                                                                                                                   |

Student and teacher token IDs must use a compatible tokenizer and vocabulary. Prefer teachers from the same model family, and set `TeacherConfig.tokenizer_model` when you want the recipe to validate teacher tokenizers against `DeployConfig.tokenizer_model`.

## Examples

The cookbook includes distillation examples under `training/examples/distillation`:

| Example                     | Path                                    | Use                                                                    |
| --------------------------- | --------------------------------------- | ---------------------------------------------------------------------- |
| Privileged-context OPD/SDFT | `gsm8k_privileged`                      | Student sees the problem; teacher can see privileged solution context. |
| Routed MOPD smoke           | `routed_mopd/train_two_teacher_lora.py` | Tiny generated dataset with two route labels and a LoRA student.       |

Run from the cookbook repository:

```bash theme={null}
cd training
FIREWORKS_API_KEY=... \
python examples/distillation/routed_mopd/train_two_teacher_lora.py
```

## Next steps

* [Cookbook Reference](/fine-tuning/training-api/cookbook/reference) - config classes and common recipe fields
* [Loss Functions](/fine-tuning/training-api/loss-functions) - built-in and custom Training API losses
* [Weight sync](/fine-tuning/training-api/cookbook/weight-sync) - how updated weights reach serving deployments
