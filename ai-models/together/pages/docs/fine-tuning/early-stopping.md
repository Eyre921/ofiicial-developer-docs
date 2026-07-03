---
title: "Early stopping"
source: https://docs.together.ai/docs/fine-tuning/early-stopping
path: docs/fine-tuning/early-stopping
---

Halt a fine-tuning job when validation loss stops improving.

Early stopping halts a job when the validation loss stops improving and promotes the best available checkpoint as the final model. Use this feature when you're not sure how many epochs the run actually needs, and you want to avoid paying for steps that don't improve model performance. The job still finishes as `completed` with a deployable model, and the unused steps are refunded automatically.

You can enable early stopping for both [supervised fine-tuning](/docs/fine-tuning/supervised) and [preference tuning (DPO)](/docs/fine-tuning/preference-tuning) jobs.

Early stopping is driven by validation, so it requires a validation file and one or more evaluations. See [split into train and validation](/docs/fine-tuning/data-preparation#split-into-train-and-validation) for details on how to prepare a `validation_file` and set `n_evals`.

## Enable early stopping

To turn on early stopping, supply a validation file, set `n_evals` high enough to detect a plateau, and set `early_stopping_enabled=true` in your job creation call:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.create(
      training_file="<TRAINING_FILE_ID>",
      validation_file="<VALIDATION_FILE_ID>",
      model="Qwen/Qwen3.5-9B",
      n_epochs=5,
      n_evals=10,
      early_stopping_enabled=True,
      early_stopping_patience=2,
      early_stopping_min_delta=0.0,
      early_stopping_warmup_evals=1,
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.create({
    training_file: "<TRAINING_FILE_ID>",
    validation_file: "<VALIDATION_FILE_ID>",
    model: "Qwen/Qwen3.5-9B",
    n_epochs: 5,
    n_evals: 10,
    early_stopping_enabled: true,
    early_stopping_patience: 2,
    early_stopping_min_delta: 0.0,
    early_stopping_warmup_evals: 1,
  });
  console.log(job.id);
  ```

  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<TRAINING_FILE_ID>" \
    --validation-file "<VALIDATION_FILE_ID>" \
    --model "Qwen/Qwen3.5-9B" \
    --n-epochs 5 \
    --n-evals 10 \
    --early-stopping-enabled \
    --early-stopping-patience 2 \
    --early-stopping-min-delta 0.0 \
    --early-stopping-warmup-evals 1
  ```
</CodeGroup>

## Parameters

| Parameter                     | Default | Description                                                                                                                                              |
| ----------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `early_stopping_enabled`      | `false` | Turn early stopping on. Requires `validation_file` and `n_evals >= patience + warmup_evals + 1`.                                                         |
| `early_stopping_patience`     | `2`     | Number of consecutive non-improving evaluations to allow before stopping.                                                                                |
| `early_stopping_min_delta`    | `0.0`   | Minimum decrease in `eval_loss` that counts as an improvement.                                                                                           |
| `early_stopping_warmup_evals` | `1`     | Initial evaluations to skip before patience starts counting. Their `eval_loss` still updates the best value that later evaluations are compared against. |

## Retrieve the result

When the job finishes, retrieve it and read the early stopping fields off the response:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.retrieve(id="<JOB_ID>")

  print(job.early_stopped)  # True if the run was halted early
  print(job.early_stopping_best_step)  # step of the promoted checkpoint
  print(job.early_stopping_best_metric)  # eval_loss at that step
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.retrieve("<JOB_ID>");

  console.log(job.early_stopped); // true if the run was halted early
  console.log(job.early_stopping_best_step); // step of the promoted checkpoint
  console.log(job.early_stopping_best_metric); // eval_loss at that step
  ```
</CodeGroup>

The response surfaces the early stopping decision and the best checkpoint:

* `early_stopped`: `true` if patience was exhausted or a non-finite (NaN/Inf) eval loss halted the run, otherwise `false`.
* `early_stopping_best_step`: The training step whose checkpoint was promoted as the final model, or the halt step when no improving evaluation was recorded.
* `early_stopping_best_metric`: The value of `eval_loss` at that step (`null` if no improving evaluation was recorded).

For example, a job that requested 5 epochs but stopped once the validation loss plateaued returns something like this (abbreviated to the relevant fields):

```json theme={null}
{
  "id": "ft-9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d",
  "status": "completed",
  "model": "Qwen/Qwen3.5-9B",
  "n_epochs": 5,
  "epochs_completed": 3,
  "n_evals": 10,
  "evals_completed": 6,
  "total_steps": 120,
  "steps_completed": 72,
  "early_stopped": true,
  "early_stopping_best_step": 48,
  "early_stopping_best_metric": 0.4213
}
```

Here the best evaluation landed at step 48; the next two evaluations didn't improve on it (because `early_stopping_patience` is 2), so the run halted at step 72 and the step-48 checkpoint was promoted as the final model. `steps_completed` (72) is below `total_steps` (120), and the unused steps are refunded.

The [events log](/reference/get-fine-tunes-id-events) also records an `early_stopped` entry at the halt step and a `refund` entry for the unused steps, which are credited back to your project automatically. To see the full history of `eval_loss` across evaluations and understand why early stopping fired, [retrieve the job's metrics](/docs/fine-tuning/monitoring#retrieve-metrics).

## Find the final checkpoint

An early-stopped job ships the final checkpoint from `early_stopping_best_step`, not the halt step. When you [list checkpoints](/reference/cli/finetune#list-checkpoints), the final entry's `step` field reports that promoted step, so it matches `early_stopping_best_step` on the job. A job that didn't stop early reports the last completed step instead.

To confirm this, retrieve the job and compare its `early_stopping_best_step` against the final checkpoint's `step`:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.retrieve("<JOB_ID>")
  checkpoints = client.fine_tuning.list_checkpoints("<JOB_ID>")

  final = next(
      c
      for c in checkpoints.data
      if "intermediate" not in c.checkpoint_type.lower()
  )
  # For an early-stopped job, these two values match.
  print(final.step, job.early_stopping_best_step)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.retrieve("<JOB_ID>");
  const checkpoints = await client.fineTuning.listCheckpoints("<JOB_ID>");

  const final = checkpoints.data.find(
    (c) => !c.checkpoint_type.toLowerCase().includes("intermediate"),
  );
  // For an early-stopped job, these two values match.
  console.log(final?.step, job.early_stopping_best_step);
  ```

  ```bash CLI theme={null}
  tg fine-tuning list-checkpoints <JOB_ID>
  ```
</CodeGroup>
