---
title: "Troubleshooting fine-tuning jobs"
source: https://docs.together.ai/docs/fine-tuning/troubleshooting
path: docs/fine-tuning/troubleshooting
---

Diagnose failed or cancelled fine-tuning jobs, understand job timing, and resolve common errors.

This page covers what to expect while a job runs and how to diagnose the most common failures. To inspect a job's status and history, run `tg fine-tuning retrieve <JOB_ID>` and `tg fine-tuning list-events <JOB_ID>`, or open the [jobs dashboard](https://api.together.ai/jobs).

## Job timing

**Time to start:** A job moves through `pending`, `queued`, and `running` before training begins. Start time depends on queue depth and hardware availability. With no other pending jobs and free hardware, a job usually reaches `running` within a minute, and most jobs start within an hour. There is no SLA on queue wait time.

**Run time:** Run time depends on model size, dataset size, and network speed during the model and data downloads. Once a job is running, its estimated time remaining may appear on the [jobs dashboard](https://api.together.ai/jobs) or in the `tg fine-tuning retrieve` output. For a rough estimate of total training time, multiply the time the first epoch takes by your `n_epochs` value.

## Diagnose a failed or stopped job

A job that doesn't finish ends in one of three states:

* **Cancelled:** Usually an automatic cancellation, most often from a failed balance check. Add funds or raise your spending limit, then resubmit.
* **User error:** A problem with your inputs, most often a dataset that fails server-side validation or an incompatible continued-fine-tuning checkpoint. The event log names the specific reason. See [Data validation failures](#data-validation-failures) below. Invalid Weights & Biases credentials also end a job this way: a wrong `wandb_api_key` fails the job during training with an `Unable to authenticate with Weights & Biases` event, and a `wandb_entity` you lack access to fails it with a permission error.
* **Error:** A problem on Together AI's side. These are usually transient. Our support team will follow up about the failure, or you can reach out at [together.ai/contact](https://www.together.ai/contact).

Read the event log to confirm the specific cause before you act:

```bash theme={null}
tg fine-tuning list-events <JOB_ID>
```

In the web UI, the same events appear under the **Logs** tab on the job's page in the [jobs dashboard](https://api.together.ai/jobs).

## File upload failures

If a training file fails to upload, the CLI and web UI return the specific reason. A 401 or 403 status means your API key is missing or inactive, so verify it's set and active. Other failures, such as an insufficient balance, are described in the returned error.

## Data validation failures

Most dataset validation runs server-side during ingestion, after upload and before training. If a job stops with a data-related error, inspect the event log and the file's validation report. See [Wait for server-side validation](/docs/fine-tuning/data-preparation#wait-for-server-side-validation) for how to read `processing_status` and `validation_report`.

## Automatic restarts

If a job hits an internal (Together AI-side) error, such as a hardware failure, it may be restarted automatically. Restarts aren't guaranteed. Check the event log for a restart event, the new job ID, and a refund line. The refund is automatic.

If a job doesn't restart, our support team will follow up about the failure, or you can reach out at [together.ai/contact](https://www.together.ai/contact).

## Error codes

Fine-tuning API requests return standard HTTP status codes. For the full list of codes, causes, and fixes, see [Error codes](/docs/error-codes). Transient 5xx errors (503, 504, 524, and 529) are safe to retry after a short wait. [Contact support](https://www.together.ai/contact) if they persist.
