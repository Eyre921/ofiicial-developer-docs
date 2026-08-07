---
title: "Cleanup and Teardown"
source: https://docs.fireworks.ai/fine-tuning/training-api/reference/cleanup
path: fine-tuning/training-api/reference/cleanup
---

Delete trainer jobs and deployments after experiments to avoid leaked resources.

## What this is

RLOR trainer jobs and weight-sync-enabled deployments hold GPU resources. Always clean up after experiments — especially if jobs terminate unexpectedly. In new SDK and cookbook code, cleanup is owned by the SDK-managed service client.

## Automatic cleanup via the SDK-managed service

Create the service with cleanup options, then close it in `finally`:

```python theme={null}
from fireworks.training.sdk import FiretitanServiceClient

service = FiretitanServiceClient.from_firetitan_config(
    api_key=api_key,
    base_url=base_url,
    base_model="accounts/fireworks/models/qwen3-8b",
    tokenizer_model="Qwen/Qwen3-8B",
    lora_rank=0,
    training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    deployment_id="research-serving",
    cleanup_trainer_on_close=True,
    cleanup_deployment_on_close="scale_to_zero",
)

try:
    run_training_loop()
finally:
    service.close()
```

`cleanup_trainer_on_close=True` deletes SDK-managed trainers. Separate reference trainers are governed by `cleanup_reference_trainer_on_close` (default `True`). `cleanup_deployment_on_close="scale_to_zero"` releases deployment GPUs while keeping the deployment resource around; use `"delete"` only when you want to remove the deployment entirely.

Cookbook recipes use the same service-client lifecycle internally and close the service through an `ExitStack`.

<Note>
  The standalone `ResourceCleanup` context manager and `setup_infra` helper have been **removed** from the cookbook. Provisioning and teardown now live behind the SDK-managed service client. See [Migrating from the deprecated managed infra](/fine-tuning/training-api/cookbook/reference#deprecated-managed-infra-infraconfig).
</Note>

## Trainer inactivity cleanup

Long-running RLOR trainer jobs are automatically stopped after 10 minutes with no tracked activity. The trainer reports this activity to the control plane, and tracked activity includes trainer API operations and active-session heartbeats.

When creating a trainer through the REST API (`POST /v1/accounts/{account_id}/rlorTrainerJobs`), set `inactivityTimeout` to a positive protobuf JSON duration to choose a different timeout:

```json theme={null}
{
  "inactivityTimeout": "1800s"
}
```

When creating a trainer through the legacy manager API, set `TrainerJobConfig.inactivity_timeout` and pass the config to `TrainerJobManager.create(...)` or `TrainerJobManager.create_and_wait(...)`:

```python theme={null}
from datetime import timedelta
from fireworks.training.sdk import TrainerJobConfig

config = TrainerJobConfig(
    base_model="accounts/fireworks/models/qwen3-8b",
    training_shape_ref="accounts/fireworks/trainingShapes/<shape>/versions/<version>",
    inactivity_timeout=timedelta(minutes=30),
)
```

With `firectl`, use `--inactivity-timeout 30m` or `--inactivity-timeout 2h`. When the value is omitted or set to `0`, Fireworks uses the 10-minute default.

To disable automatic inactivity cleanup, set `disableInactivityCleanup` in the REST API, set `TrainerJobConfig.disable_inactivity_cleanup=True` in the Python SDK, or pass `--disable-inactivity-cleanup` in `firectl`. The trainer will not be stopped due to inactivity, and GPU usage continues to accrue while the trainer is running, so delete the trainer when you no longer need it.

## Manual compatibility cleanup

If you provisioned resources yourself with `TrainerJobManager` / `DeploymentManager` instead of the managed service, delete them directly.

### Cleaning up RLOR trainer jobs

```python theme={null}
import os
from fireworks.training.sdk import TrainerJobManager, DeploymentManager

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

rlor_mgr = TrainerJobManager(api_key=api_key, base_url=base_url)
deploy_mgr = DeploymentManager(api_key=api_key, base_url=base_url)

# Delete known trainer jobs from this run
for job_id in ["<policy-job-id>", "<reference-job-id>"]:
    rlor_mgr.delete(job_id=job_id)
```

### Cleaning up deployments

```python theme={null}
deploy_mgr.delete(deployment_id="<deployment-id>")
```

If you want to keep the deployment resource but release GPUs (lighter alternative to delete):

```python theme={null}
deploy_mgr.scale_to_zero(deployment_id="<deployment-id>")
```

This sets both `minReplicaCount` and `maxReplicaCount` to `0`, releasing all accelerators while keeping the deployment available for future scale-up.

### Manual cleanup with try/finally

```python theme={null}
policy_job_id = "<policy-job-id>"
reference_job_id = "<reference-job-id>"
deployment_id = "research-loop-serving"

try:
    run_training_loop()
finally:
    rlor_mgr.delete(policy_job_id)
    rlor_mgr.delete(reference_job_id)
    deploy_mgr.delete(deployment_id)
```

## Checking for leaked resources

Track the IDs you create (trainer job IDs + deployment ID) and clean those explicitly. For broad account-wide discovery, use the Fireworks console or the managed `fw.*.list()` APIs.

## Operational guidance

* **Delete both policy and reference trainers** when running GRPO (which uses 2 RLOR jobs).
* **Close the managed service** in `finally` so trainer/reference/deployment cleanup runs on Ctrl+C or exceptions.
* **Don't delete a trainer** while a `save_weights_for_sampler` operation is in progress — wait for it to complete first.

## Related Guides

* [FiretitanServiceClient](/fine-tuning/training-api/reference/service-client)
* [Training and Sampling](/fine-tuning/training-api/training-and-sampling)
