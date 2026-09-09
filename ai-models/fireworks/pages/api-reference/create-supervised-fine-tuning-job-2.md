---
title: "Create Supervised Fine-tuning Job"
source: https://docs.fireworks.ai/api-reference/create-supervised-fine-tuning-job
path: api-reference/create-supervised-fine-tuning-job
---

post /v1/accounts/{account_id}/supervisedFineTuningJobs

## Learning rate scheduler

Supervised fine-tuning jobs accept an optional `lrScheduler` object on the request body. Set **exactly one** of `constant`, `linear`, or `cosine`. When omitted, the trainer uses a constant learning rate after warmup.

Configure warmup separately with `learningRateWarmupSteps` (not inside `lrScheduler`).

| Schedule   | Object shape                                             | Notes                                               |
| ---------- | -------------------------------------------------------- | --------------------------------------------------- |
| `constant` | `{ "constant": {} }`                                     | Flat LR after warmup                                |
| `linear`   | `{ "linear": { "minLrRatio": 0.1, "decayRatio": 0.8 } }` | Linear decay toward `learningRate * minLrRatio`     |
| `cosine`   | `{ "cosine": { "minLrRatio": 0.1, "decayRatio": 0.8 } }` | Cosine annealing toward `learningRate * minLrRatio` |

For `linear` and `cosine`:

* `minLrRatio` — floor LR as a fraction of `learningRate` (0.0–1.0).
* `decayRatio` — fraction of total training steps over which to decay. Omit or set `0` to decay over the full run.

`linear` and `cosine` require a base model on the **Training V2** path. V1-routed models only support a constant schedule.

### Example: cosine schedule

```json theme={null}
{
  "supervisedFineTuningJob": {
    "baseModel": "accounts/my-account/models/qwen3-8b",
    "dataset": "accounts/my-account/datasets/my-data",
    "outputModel": "accounts/my-account/models/my-tuned-model",
    "learningRate": 0.0001,
    "learningRateWarmupSteps": 10,
    "lrScheduler": {
      "cosine": {
        "minLrRatio": 0.1,
        "decayRatio": 0.8
      }
    }
  }
}
```

See also [Training models](/fine-tuning/fine-tuning-models) for CLI equivalents (`--learning-rate-scheduler`, `--learning-rate-min-lr-ratio`, `--learning-rate-decay-ratio`).
