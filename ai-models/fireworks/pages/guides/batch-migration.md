---
title: "Migrating Batch API workloads to preemptible deployments"
source: https://docs.fireworks.ai/guides/batch-migration
path: guides/batch-migration
---

Run your existing Batch input files on a preemptible deployment with the Batch migration script

We're moving to a more secure way of running Batch jobs and changing how Fireworks handles customer data for Batch. As part of this change, Batch is paused: new Batch jobs are no longer accepted, dataset uploads return an error, and all Batch input datasets and job outputs stored on Fireworks will be permanently deleted.

This guide walks you through moving your Batch workloads to preemptible deployments.

## Options for running large, non-urgent workloads on Fireworks

*For example, evals, synthetic data generation, or backfill workloads.*

We will no longer support an async Batch dataset upload interface. Instead, you keep your dataset locally and send each request to the inference API yourself, so your client has to:

1. Control how many requests run at once
2. Retry requests that fail for lack of capacity, rate limits or a lost replica
3. Save results and resume after an interruption

### Preemptible deployments (50% off on-demand pricing)

Run your own deployment on spare capacity at a discount. This works with any model you can deploy on demand, including custom and fine-tuned models, and it suits bulk non-urgent jobs that can handle occasional interruptions.

**How it works.** Passing `--preemptible` to `firectl deployment create` opts the deployment into borrowing capacity:

* The deployment runs on GPUs that are currently idle, tapping into a large fleet.
* When higher priority jobs need the GPUs back, your replica can be preempted at any time, including mid-request. There is currently no advance notice.
* Fireworks doesn't guarantee how many GPUs are available at a given time or how long a replica stays up although historically they stay available for a few hours. A preempted replica is placed again automatically when GPUs free up, so you don't need to create another deployment.

**Before you use it:**

* **Bulk and non-urgent work only.** Treat a preempted replica as a normal outcome, not an error. We do not recommend sending production or latency-sensitive traffic to a preemptible deployment.
* **`--preemptible` is immutable.** It's set at creation and can't be turned on or off later. To change it, delete the deployment and create a new one.
* **Clean up when done.** Delete the deployment when the job finishes, so you stop paying for it and release the borrowed capacity.

> [!TIP]
>
> **Use the [Batch migration script](https://github.com/fw-ai-external/cookbook/tree/main/case-studies/batch-migration) to make the switch.** It reads your existing Batch JSONL files and sends the requests with concurrency and retries, writing results back to JSONL in the Batch output format. It handles all three steps above, so your downstream parsing keeps working. Use it as is, or as a reference for your own client.

## What you need

Set up the following before you run the script:

| Requirement | How to get it |
| - | - |
| **Python 3.10 or newer** | The script uses only the Python standard library, so there is nothing else to install. Check with `python3 --version`. |
| **A Fireworks API key** | Create one on the [API keys page](https://app.fireworks.ai/settings/users/api-keys), then `export FIREWORKS_API_KEY=<your key>` in the shell that runs the script. |
| **`firectl` 1.7.26 or newer, signed in** | [Install `firectl`](/tools-sdks/firectl/firectl), then run `firectl signin`. Check the version with `firectl version`: older builds silently ignore `--preemptible` and create a regular on-demand deployment. |
| **Your account ID** | Run `firectl whoami` to see the account you're signed in to. |
| **Preemptible GPU quota** | Preemptible deployments have their own account-wide GPU quota per accelerator type, separate from your on-demand quota. Check it on the [Quotas page](https://app.fireworks.ai/settings/quotas) (**Settings → Quotas**) in the app, or with `firectl quota get preemptible-<accelerator>-count` (for example `preemptible-h100-count`). If you need more, contact your account team and we'll review it based on your recent Batch usage. |
| **Your Batch input file, stored locally** | The JSONL file you used to upload to Batch, in the [OpenAI batch format](/guides/batch-inference) (`custom_id` plus `body`). The script reads local files only, not `gs://` paths. If your file is in Cloud Storage, copy it down first with `gcloud storage cp gs://<BUCKET>/<PATH>/batch_input.jsonl .`, and copy `results.jsonl` back up when the run finishes. |
| **The script** | Download [`batch_to_realtime.py`](https://github.com/fw-ai-external/cookbook/blob/main/case-studies/batch-migration/batch_to_realtime.py). |

## Step 1: Create a preemptible deployment

Use the model ID of the model your Batch jobs ran on:

* A Fireworks model: `accounts/fireworks/models/<MODEL>`
* Your own fine-tuned or uploaded model, including LoRA adapters: `accounts/<ACCOUNT_ID>/models/<MODEL_ID>`. Point the deployment at your fine-tuned model ID, not the base model.

Pick an explicit deployment shape. For control over cost based on which hardware and number of GPUs per replica, don't use `--deployment-shape default` for a preemptible deployment. List the shapes your account can deploy the model on:

```bash theme={null}
firectl deployment-shape-version match --model <MODEL_ID> -a <ACCOUNT_ID>
```

Then create the deployment with one of those shapes:

```bash theme={null}
firectl deployment create <MODEL_ID> \
  -a <ACCOUNT_ID> \
  --deployment-id <DEPLOYMENT_ID> \
  --display-name <DISPLAY_NAME> \
  --deployment-shape <DEPLOYMENT_SHAPE> \
  --min-replica-count 1 --max-replica-count 1 \
  --preemptible --wait
```

Replace the placeholders:

* `<MODEL_ID>`: the full model ID from the list above.
* `<DEPLOYMENT_ID>` / `<DISPLAY_NAME>`: a name of your choice, for example `batch-migration`.
* `<DEPLOYMENT_SHAPE>`: a shape from `deployment-shape-version match`. See [Deployment shapes](/guides/ondemand-deployments#deployment-shapes).

`--wait` blocks until the deployment is ready (1 hour by default; change it with `--wait-timeout`). A create that would go over your preemptible quota fails with `RESOURCE_EXHAUSTED` and a message naming the quota.

## Step 2: Check the deployment status

A deployment answers `404` until it's ready, and the script stops on that `404`, so confirm the deployment is ready before you start.

> [tab] firectl
>
> ```bash theme={null}
> firectl deployment get <DEPLOYMENT_ID> -a <ACCOUNT_ID>
> ```
>
> Wait for `State: READY`. The other states are `CREATING`, `UPDATING`, `DELETING`, `DELETED` and `FAILED`; see [Deployment status states](/guides/ondemand-deployments#deployment-status-states).
>
> > [!NOTE]
> >
> > `State` stays `READY` when a replica is preempted, and while it's placed again. It isn't marked `FAILED` or `UPDATING`. To see whether replicas are serving, check `replicaStats` instead:
>
> ```bash theme={null}
> firectl deployment get <DEPLOYMENT_ID> -a <ACCOUNT_ID> -o json
> ```
>
> | `replicaStats` field | What it means for a preemptible deployment |
> | - | - |
> | `readyReplicaCount` | Replicas serving traffic. It drops when a replica is preempted, and is `0` if every replica was preempted. |
> | `pendingSchedulingReplicaCount` | Replicas waiting for free GPUs. A preempted replica is counted here until it's placed again. |
> | `downloadingModelReplicaCount` | Replicas that were placed and are downloading model weights. |
> | `initializingReplicaCount` | Replicas starting the model server. Once it's up, the replica moves back to `readyReplicaCount`. |
>
> A field that's `0` can be left out of the output.
>
> To see what happened to the deployment, including preempted replicas:
>
> ```bash theme={null}
> firectl deployment events list <DEPLOYMENT_ID> -a <ACCOUNT_ID>
> ```

> [tab] Fireworks app
>
> Open the [Deployments page](https://app.fireworks.ai/dashboard/deployments) and select your deployment. The page shows its status; wait until it's ready before you start the script. As with `firectl`, the status stays ready after a preemption, so check how many replicas are ready.
>
> The deployment's activity log shows what happened to it. Each preempted replica adds a "Replica preempted to free capacity; it will restart when capacity is available" event.

Then send one test request to confirm the deployment answers:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "<MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Step 3: Run your Batch file

Point `--model` at your deployment with the `<MODEL>#<DEPLOYMENT>` form:

```bash theme={null}
python batch_to_realtime.py --input batch_input.jsonl --output results.jsonl \
  --model "<MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>" \
  --concurrency 16
```

The script:

* Reads your existing Batch input file in the [OpenAI batch format](/guides/batch-inference) (`custom_id` plus `body`)
* Writes successful rows to `--output` and failed rows to `<output>.errors.jsonl`, in the matching Batch output format
* Retries `408`, `409`, `425`, `429`, `5xx` (except `501` and `505`), timeouts and dropped connections, honoring `Retry-After`, for up to 30 minutes per row
* Resumes where it stopped when you rerun the same command, sending every row without a result: failed rows and rows a stopped run never finished. Add `--skip-errors` to rerun without resending rows that already failed.

Rows are written as they finish, so match output rows on `custom_id`, not line order. See the [script README](https://github.com/fw-ai-external/cookbook/tree/main/case-studies/batch-migration) for every flag, the output formats and the exit codes.

### Tips

* **Validate on a sample first.** Run a few hundred rows and compare outputs with your Batch results before running the full file.
* **Tune `--concurrency`** (default 16, up to 256). Start at about 8 to 16 per replica and raise it while latency stays acceptable.
* **Ride out preemption.** If a replica is preempted mid-run, its in-flight requests fail with dropped connections or `503` until it's back, and the script retries them. The replica is placed again automatically when GPUs free up, and the deployment stays `READY`, so you don't need to recreate it. Watch `replicaStats` (see [Step 2](#step-2-check-the-deployment-status)) to see it come back. If that takes longer than 30 minutes, raise `--max-retry-time`, or rerun the same command later.
* **Know when it happens.** Each preempted replica adds an event to the deployment's activity log, in the app and in `firectl deployment events list` (see [Step 2](#step-2-check-the-deployment-status)). If preemption leaves the deployment with no ready replicas, the user who created it gets an email, and another when it can serve again.

## Step 4: Delete the deployment

Delete the deployment when the job is done to stop billing and release the borrowed capacity:

```bash theme={null}
firectl deployment delete <DEPLOYMENT_ID> -a <ACCOUNT_ID>
```

## Errors

| Status | Meaning | What the script does |
| - | - | - |
| `429` | Rate limited, or the deployment is saturated | Retries with backoff and jitter |
| `503` | The deployment has no running replica (`DEPLOYMENT_SCALING_UP`), for example after preemption | Retries, waiting for `Retry-After` when sent |
| `404` | Model or deployment not available, including a deployment that isn't `READY` | Stops the run (exit 2); rerun once it's available |
| `401` | Bad API key | Stops the run (exit 2) |
| Other `4xx` | Request problem, such as a prompt that's too long | Writes the row to the errors file |

See [Reliability and Error Handling](/guides/reliability) for more patterns.

## FAQ

> [accordion] Can I choose the region for a preemptible deployment?
>
> Yes, you can choose a multi-region: `GLOBAL` (the default), `US`, `CANADA`, `EUROPE` or `APAC`. Pass it with `--region` when you create the deployment:
>
> ```bash theme={null}
> firectl deployment create <MODEL_ID> \
>   -a <ACCOUNT_ID> \
>   --deployment-id <DEPLOYMENT_ID> \
>   --deployment-shape <DEPLOYMENT_SHAPE> \
>   --min-replica-count 1 --max-replica-count 1 \
>   --region US \
>   --preemptible --wait
> ```
>
> There is less capacity if you specify a region other than `GLOBAL`.

## Get help

We understand this change may disrupt your workflow, and we're sorry for the inconvenience. Contact your Fireworks account team with questions about your migration or to request more preemptible GPU quota.
