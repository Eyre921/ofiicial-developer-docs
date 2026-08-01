---
title: "RFT Cost Planning"
source: https://docs.fireworks.ai/fine-tuning/rft-cost-estimator
path: fine-tuning/rft-cost-estimator
---

Plan RFT cost using current model eligibility, training shapes, pricing, and workload assumptions.

RFT cost depends on the selected model and compatible training shape, rollout volume, generated tokens, evaluator latency, and total runtime. These inputs change as models, shapes, and pricing evolve, so this page does not provide a hardcoded dollar calculator.

<Warning>
  Do not estimate cost from model size alone. Confirm that the live Training Shapes matrix supports RFT for the selected model and tuning mode, then use current pricing and the resolved shape.
</Warning>

## Before estimating

1. Choose an RFT-enabled model on [Models](/fine-tuning/models).
2. Resolve the shape and parameter mode used by the job.
3. Read current [pricing](https://fireworks.ai/pricing), including any eligible managed RFT promotion.
4. Record dataset rows, epochs, rollout candidates, maximum output tokens, expected average output length, evaluator latency, and concurrency.
5. Set a cost ceiling and label any unknown line item rather than guessing.

## Cost drivers

| Driver                         | Why it matters                                            | User control                                        |
| ------------------------------ | --------------------------------------------------------- | --------------------------------------------------- |
| Model and compatible shape     | Determines available hardware and runtime characteristics | Choose from the live method-support matrix          |
| Dataset rows                   | Determines prompt groups processed                        | Curate representative prompts                       |
| Epochs                         | Repeats the dataset                                       | Start with one                                      |
| Rollout candidates             | Multiplies sampled completions per prompt                 | Use the minimum that gives useful reward variance   |
| Output length                  | Drives rollout generation and evaluation time             | Set a realistic maximum                             |
| Evaluator latency              | Slow evaluation increases wall-clock runtime              | Cache, batch, and remove unnecessary external calls |
| Trainer and deployment runtime | Dedicated resources are metered by runtime                | Monitor progress and tear down promptly             |

## Planning formulas

Use formulas to expose assumptions, not to replace current platform pricing:

```text theme={null}
rollout_count = prompts × epochs × candidates_per_prompt
estimated_output_tokens = rollout_count × average_output_tokens
runtime_cost = measured_or_estimated_runtime × resolved_resource_rate
```

For a first run, estimate a range using conservative and expected output lengths. If throughput or a resource rate is unavailable, mark the total as incomplete and keep a hard runtime or budget ceiling.

## Reduce cost safely

* Validate the evaluator offline and confirm that representative outputs receive different scores.
* Start with a small RFT-compatible model when the live matrix and pricing support it.
* Run a bounded dataset sample before the full dataset.
* Start with one epoch.
* Reduce rollout candidates only if reward variance remains sufficient.
* Set output limits to the task's real needs.
* Stop runs that show no real progress or a constant reward.
* Delete or scale down billable deployments after evaluation.

## Managed versus Training API

* **Managed RFT:** use the current managed pricing and any eligibility rules shown on the pricing and model-support pages.
* **Training API serverless:** verify current per-token meter definitions and rates during private preview.
* **Training API dedicated:** use the resolved trainer and deployment resources, current runtime rates, and measured or bounded duration.

For broader serverless-versus-dedicated economics, use [Choose Serverless or Dedicated Training](/fine-tuning/training-api/choose-infrastructure) and the [multi-turn cost comparison](/fine-tuning/multi-turn-cost-comparison).
