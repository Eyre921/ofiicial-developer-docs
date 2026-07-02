---
title: "Monitor a fine-tuning job"
source: https://docs.together.ai/docs/fine-tuning/monitoring
path: docs/fine-tuning/monitoring
---

Poll job status, retrieve per-step loss and evaluation metrics, and stream training progress to Weights & Biases.

The Together AI platform records metrics at every training and evaluation step. You can pull them during a job to watch loss curves live, or after the job completes to compare runs.

## Poll until the job is done

A fine-tuning job moves through the states: `pending → queued → running → uploading → completed`. Queue wait is typically under an hour but varies with platform load. Once a job is running, multiply the duration of the first epoch by `n_epochs` to estimate remaining training time.

Use this loop to poll until the job reaches a terminal state, then fetch the metrics. The terminal states are `completed`, `error`, and `cancelled`.

If you launched the job with [early stopping](/docs/fine-tuning/early-stopping), the terminal status is still `completed` even when training ended ahead of `n_epochs`. The response sets `early_stopped=true` and exposes the winning checkpoint via `early_stopping_best_step` and `early_stopping_best_metric`.

<CodeGroup>
  ```python Python theme={null}
  import os
  import time
  from together import Together

  client = Together()

  job_id = "ft-xxxx-yyyy"
  deadline = time.time() + 6 * 60 * 60  # safety cap: 6 hours

  while True:
      job = client.fine_tuning.retrieve(id=job_id)
      print(job.status)
      if job.status in ("completed", "error", "cancelled"):
          break
      if time.time() > deadline:
          raise TimeoutError(f"Job {job_id} still {job.status} after 6 hours")
      time.sleep(60)

  if job.status != "completed":
      raise RuntimeError(f"Job ended with status: {job.status}")

  metrics = client.fine_tuning.list_metrics(job_id)
  for step in metrics.metrics:
      print(step)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const jobId = "ft-xxxx-yyyy";
  const deadline = Date.now() + 6 * 60 * 60 * 1000;
  const terminal = new Set(["completed", "error", "cancelled"]);

  let job = await client.fineTuning.retrieve(jobId);
  while (!terminal.has(job.status)) {
    if (Date.now() > deadline) {
      throw new Error(`Job ${jobId} still ${job.status} after 6 hours`);
    }
    await new Promise((r) => setTimeout(r, 60000));
    job = await client.fineTuning.retrieve(jobId);
    console.log(job.status);
  }

  if (job.status !== "completed") {
    throw new Error(`Job ended with status: ${job.status}`);
  }

  const metrics = await client.fineTuning.listMetrics(jobId);
  console.log(metrics);
  ```

  ```bash CLI theme={null}
  tg fine-tuning retrieve "<JOB_ID>"

  # When status is "completed", pull metrics:
  tg fine-tuning list-metrics "<JOB_ID>" --json > metrics.json
  ```
</CodeGroup>

<Note>
  **Expected job durations:** A small LoRA job on an 8B model with under 1,000 examples typically completes in 10 to 30 minutes after queue. A full job on a 70B model with hundreds of thousands of examples can take several hours. Save your job ID: you can poll from any session without re-uploading data.
</Note>

## Cancel or delete a job

Cancel a running job if you started it by mistake or no longer need it. You're billed only for the steps that completed before cancellation.

<CodeGroup>
  ```python Python theme={null}
  client.fine_tuning.cancel(id="<JOB_ID>")
  ```

  ```bash CLI theme={null}
  tg fine-tuning cancel "<JOB_ID>"
  ```
</CodeGroup>

Delete a finished job to remove it along with the files it produced.

<CodeGroup>
  ```python Python theme={null}
  client.fine_tuning.delete(id="<JOB_ID>")
  ```

  ```bash CLI theme={null}
  tg fine-tuning delete "<JOB_ID>"
  ```
</CodeGroup>

<Warning>
  Deleting a job can't be undone. It destroys every file the job produced, including intermediate and final checkpoints.
</Warning>

## Retrieve metrics

The `list_metrics` call returns every recorded step. The CLI renders ASCII charts by default; pass `--json` to get raw output.

<CodeGroup>
  ```python Python theme={null}
  metrics = client.fine_tuning.list_metrics("<JOB_ID>")
  for step in metrics.metrics:
      print(step)
  ```

  ```typescript TypeScript theme={null}
  const metrics = await client.fineTuning.listMetrics("<JOB_ID>");
  for (const step of metrics.metrics) {
    console.log(step);
  }
  ```

  ```bash CLI theme={null}
  # ASCII charts (default)
  tg fine-tuning list-metrics "<JOB_ID>"

  # Raw JSON metrics
  tg fine-tuning list-metrics "<JOB_ID>" --json

  # Save the ASCII charts to a file
  tg fine-tuning list-metrics "<JOB_ID>" > plots.txt

  # Save the JSON metrics to a file
  tg fine-tuning list-metrics "<JOB_ID>" --json > metrics.json
  ```
</CodeGroup>

## Filter by step or time

All filter parameters are optional. Omit them to retrieve every recorded step.

<CodeGroup>
  ```python Python theme={null}
  from datetime import datetime

  metrics = client.fine_tuning.list_metrics(
      "<JOB_ID>",
      global_step_from=100,
      global_step_to=500,
      logged_at_from=datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
      logged_at_to=datetime.fromisoformat("2026-01-02T00:00:00+00:00"),
  )
  ```

  ```typescript TypeScript theme={null}
  const metrics = await client.fineTuning.listMetrics("<JOB_ID>", {
    global_step_from: 100,
    global_step_to: 500,
    logged_at_from: "2026-01-01T00:00:00",
    logged_at_to: "2026-01-02T00:00:00",
  });
  ```

  ```bash CLI theme={null}
  tg fine-tuning list-metrics "<JOB_ID>" \
    --global-step-from 100 \
    --global-step-to 500 \
    --logged-at-from 2026-01-01T00:00:00 \
    --logged-at-to 2026-01-02T00:00:00 \
    --json
  ```
</CodeGroup>

## Downsample with resolution

For long runs, pass `resolution` to cap the response at a fixed number of uniformly sampled training steps. Eval metrics are always returned in full regardless of this setting.

<CodeGroup>
  ```python Python theme={null}
  metrics = client.fine_tuning.list_metrics("<JOB_ID>", resolution=50)
  ```

  ```typescript TypeScript theme={null}
  const metrics = await client.fineTuning.listMetrics("<JOB_ID>", {
    resolution: 50,
  });
  ```

  ```bash CLI theme={null}
  tg fine-tuning list-metrics "<JOB_ID>" --resolution 50 --json
  ```
</CodeGroup>

## Sample output

Training and eval steps are returned as separate objects. Training steps contain `train/*` keys, eval steps contain `eval/*`. When both fire at the same step, both objects appear:

```json theme={null}
[
  { "timestamp": 1779196193564587000, "train/global_step": 1, "train/epoch": 0.1, "train/loss": 2.43, "train/grad_norm": 1.21, "train/learning_rate": 1e-5 },
  { "timestamp": 1779196253564587000, "train/global_step": 2, "train/epoch": 0.2, "train/loss": 2.11, "train/grad_norm": 0.94, "train/learning_rate": 9e-6 },
  { "timestamp": 1779196313564587000, "train/global_step": 3, "train/epoch": 0.3, "train/loss": 1.98, "train/grad_norm": 0.87, "train/learning_rate": 8e-6 },
  { "timestamp": 1779196314564587000, "train/global_step": 3, "train/epoch": 0.3, "eval/loss": 2.05 }
]
```

## Parameters

| Parameter          | Type               | Description                                                                               |
| ------------------ | ------------------ | ----------------------------------------------------------------------------------------- |
| `global_step_from` | integer            | Return only metrics with `global_step` ≥ this value.                                      |
| `global_step_to`   | integer            | Return only metrics with `global_step` ≤ this value.                                      |
| `logged_at_from`   | string or datetime | Return only metrics logged at or after this ISO 8601 timestamp.                           |
| `logged_at_to`     | string or datetime | Return only metrics logged at or before this ISO 8601 timestamp.                          |
| `resolution`       | integer            | Maximum number of uniformly sampled training metric points. Does not affect eval metrics. |

## Available metrics

Every job reports `train/global_step`, `train/loss`, `train/grad_norm`, `train/learning_rate`, and `timestamp`. When you supply `validation_file` and set `n_evals > 0`, the response also includes `eval/loss` and other validation metrics.

### Preference-tuning jobs

A DPO job emits everything above and adds reward and divergence metrics to the same `list_metrics` payload. They show up as extra `train/*` keys during training and, when evaluation is enabled, matching `eval/*` keys:

* **Reward and accuracy:** The reward assigned to the preferred and non-preferred responses, plus the share of examples where the preferred reward is higher.
* **KL divergence:** How far the trained model's output distribution has drifted from the reference model.
* **Per-side log probabilities:** Separate values for the preferred and non-preferred outputs, useful for debugging stalled runs.

Retrieval, filtering, and downsampling work the same way regardless of method. For what these values mean and how to interpret them during a run, see [DPO metrics](/docs/fine-tuning/preference-tuning#dpo-metrics).

## Stream to Weights & Biases

Pass `wandb_api_key` when creating the job to mirror these metrics to your W\&B workspace in real time. See the [quickstart](/docs/fine-tuning/quickstart#step-2-launch-the-job) for the call structure.
