---
title: "Manage endpoints and deployments"
source: https://docs.together.ai/docs/dedicated-endpoints/manage
path: docs/dedicated-endpoints/manage
---

Create, update, and delete resources for dedicated model inference.

This page covers the lifecycle operations for dedicated model inference (DMI): creating endpoints and deployments, scaling, stopping, and deleting resources.

The CLI's `tg beta endpoints deploy` command bundles several API/SDK operations into one step for convenience: it creates the endpoint (when you pass a new endpoint name), attaches a deployment to it, and routes 100% of traffic to that deployment. This page shows the individual operations underneath it.

To create your first deployment end-to-end, [follow the quickstart](/docs/dedicated-endpoints/quickstart).

## Create an endpoint

Before you can create a deployment, you must [select a model](/docs/dedicated-endpoints/models), [choose a config](/docs/dedicated-endpoints/configs), and create an endpoint.

The CLI has no standalone create-endpoint command: `tg beta endpoints deploy` creates the endpoint and its first deployment together (see [Create a deployment](#create-a-deployment) below). To create an empty endpoint on its own, use the SDK or API:

```python Python theme={null}
from together import Together

client = Together()
project_id = client.whoami().project_id

endpoint = client.beta.endpoints.create(
    project_id=project_id,
    name="my-endpoint",
)
print(endpoint)
```

The endpoint serves as a logical grouping of deployments, and the entry point for [routing traffic to your models](/docs/dedicated-endpoints/route-traffic).

## Create a deployment

A deployment binds a model and a hardware config to an endpoint, and sets the [autoscaling policy](/docs/dedicated-endpoints/scaling) for spinning replicas up and down based on demand. `--min-replicas` and `--max-replicas` set the [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds).

Pass an existing endpoint ID (or a new endpoint name) to `tg beta endpoints deploy --endpoint` to add a deployment. The model is the positional argument, and the config is `--config`:

```bash CLI theme={null}
tg beta endpoints deploy ml_CbJNwQC2ZqCU2iFT3mrCh \
  --endpoint ep_abc123 \
  --deployment-name my-deployment \
  --config cr_CbzGdmn14t3HYrXXitmKa \
  --min-replicas 1 --max-replicas 2
```

When a model has more than one [deployment profile](/docs/dedicated-endpoints/concepts#deployment-profile), `deploy` returns an error that lists the available profiles, for example:

```text theme={null}
Model has multiple deployment profiles. Re-run with --config <config_id>:
  cr_CbzGdmn14t3HYrXXitmKa  NVIDIA-H100 x1  BF16  TP1
  cr_CciJqTB35QmpMupbQNPPW  NVIDIA-H100 x1  FP8   TP1
```

Re-run with `--config <cr_...>` to choose one. When a model has a single profile, the CLI selects it automatically. List a model's profiles anytime with `tg beta models configs <model_id>`.

The CLI defaults `--min-replicas` and `--max-replicas` to `1`, so a bare `deploy` creates a single-replica deployment.

List and retrieve responses return a flat deployment object whose `model` and `config` resource names you can copy straight into a new create request:

```json theme={null}
{
  "id": "dep_abc123",
  "projectId": "proj_abc123",
  "endpointId": "ep_abc123",
  "name": "your-project-slug/my-endpoint/my-deployment",
  "createdAt": "2026-07-13T18:52:00Z",
  "updatedAt": "2026-07-13T18:52:00Z",
  "model": "projects/proj_abc123/models/ml_CbJNwQC2ZqCU2iFT3mrCh/revisions/rv_CbJ9yNrws93VQrZum1fTE",
  "config": "projects/proj_abc123/configs/cr_CbzGdmn14t3HYrXXitmKa",
  "autoscaling": {"minReplicas": 1, "maxReplicas": 2},
  "hardware": "1xnvidia-h100-80gb",
  "trafficMode": "TRAFFIC_MODE_LIVE",
  "desiredReplicas": 1,
  "status": {"state": "DEPLOYMENT_STATE_PROVISIONING", "scheduledReplicas": 0, "readyReplicas": 0, "message": "Scheduling replicas"}
}
```

The `hardware` field reports the deployment's instance type in `<count>x<accelerator-type>` form (for example `1xnvidia-h100-80gb`). It may be empty when the config has no fixed instance type (for example disaggregated serving).

After you've created a deployment, you'll need to [route traffic](/docs/dedicated-endpoints/route-traffic) to it before it can serve requests.

### Create request flags

Set these flags on `tg beta endpoints deploy` when you create a deployment:

| Flag                | Required | Description                                                                                                                                                             |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MODEL`             | Yes      | Positional argument. The model to deploy: a public model name, a private model name, a private model ID (`ml_...`), or a fully resolved model path.                     |
| `--endpoint`        | Yes      | The endpoint to deploy to. Pass an existing endpoint name or ID, or a new name to create the endpoint first.                                                            |
| `--config`          | No       | Config ID (`cr_...`). Required when the model has more than one deployment profile; auto-selected when it has a single one.                                             |
| `--deployment-name` | No       | Name for the deployment. Defaults to a combination of the endpoint and model names.                                                                                     |
| `--min-replicas`    | No       | Minimum replicas. Default `1`.                                                                                                                                          |
| `--max-replicas`    | No       | Maximum replicas. Default `1`.                                                                                                                                          |
| `--scaling-metric`  | No       | Metric to autoscale on, set together with `--scaling-target`. Omit to use the default metric. See [scaling metrics](/docs/dedicated-endpoints/scaling#scaling-metrics). |
| `--scaling-target`  | No       | Target value for `--scaling-metric`.                                                                                                                                    |
| `--enable-lora`     | No       | Run the multi-LoRA kernel so adapters hot-load after deploy. Set at create time only: it can't be changed on a running deployment, so redeploy to toggle it.            |

For the full flag list, including placement, the autoscaling windows, and the scaling percentile, see the [CLI reference](/reference/cli/endpoints-beta#deploy).

[Decoding optimizations](/docs/dedicated-endpoints/configs#decoding-optimizations), including speculative decoding, come from the config you select.

## Poll deployment status

To check a deployment's status, run `tg beta endpoints get` on its endpoint. The output lists up to the 10 newest deployments' `state` and ready/desired replica counts, so re-run it to watch a specific deployment come up:

```bash CLI theme={null}
# Show the endpoint with each deployment's state and replica counts
tg beta endpoints get ep_abc123
```

For the full set of status fields (scheduled replicas, status message), retrieve the deployment from the SDK or API and read `status`:

```python Python theme={null}
from together import Together

client = Together()
project_id = client.whoami().project_id

deployment = client.beta.endpoints.deployments.retrieve(
    "dep_abc123",
    project_id=project_id,
    endpoint_id="ep_abc123",
)
print(deployment.status.state)
```

From here you can track its progress scaling up:

| Field                      | Description                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `desiredReplicas`          | Target replica count from autoscaling.                                                                                                                                         |
| `status.scheduledReplicas` | Replicas the scheduler has placed on clusters. May trail `desiredReplicas` while capacity is still being found, and exceed `status.readyReplicas` while placed replicas start. |
| `status.readyReplicas`     | Replicas actively serving traffic.                                                                                                                                             |
| `status.message`           | Human-readable explanation of the current stage or cause. Replica progress lives in the counts above, not in this string.                                                      |
| `status.state`             | [See below](#deployment-states).                                                                                                                                               |

### Deployment states

A deployment reports its lifecycle in `status.state`. The API returns the fully-qualified enum (for example `DEPLOYMENT_STATE_READY`). This page uses the short name for readability.

| State              | Description                                                                                                                                                                                               |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`PROVISIONING`** | The scheduler is placing replicas on clusters. `status.message` is `Scheduling replicas`.                                                                                                                 |
| **`SCALING`**      | Replicas are starting or draining to reach the desired count. `status.message` is `Starting replicas` or `Scaling down`.                                                                                  |
| **`READY`**        | All replicas are healthy and serving. `status.message` is `All replicas ready`. A deployment must also be in the endpoint's [traffic split](/docs/dedicated-endpoints/route-traffic) to receive requests. |
| **`DEGRADED`**     | The deployment is below the requested capacity or blocked by a transient issue. `status.message` explains the cause. It usually resolves on its own.                                                      |
| **`STOPPING`**     | A transient teardown state. Replicas are draining after a stop was requested. It settles to `STOPPED` once cleanup completes, or to `FAILED` if teardown ends with a failure.                             |
| **`STOPPED`**      | Scaled to zero replicas. The deployment isn't billing and isn't serving.                                                                                                                                  |
| **`FAILED`**       | Terminal state. The `status.message` field explains why.                                                                                                                                                  |

A deployment that never reaches `READY` within six hours after starting will be marked as `FAILED`.

## Scale a deployment

Deployment scale is controlled by the deployment's [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds), and optionally autoscaled using [scaling metrics](/docs/dedicated-endpoints/scaling#scaling-metrics). Set the initial bounds at deploy time (`--min-replicas`/`--max-replicas`), then change them on a running deployment:

```bash CLI theme={null}
tg beta endpoints update dep_abc123 --min-replicas 2 --max-replicas 4
```

## Stop a deployment

A deployment runs until you stop it. To stop a deployment and release its hardware, set both its replica bounds to `0`:

```bash CLI theme={null}
tg beta endpoints update dep_abc123 --min-replicas 0 --max-replicas 0
```

The replicas keep serving until they finish draining, then the deployment moves to `DEPLOYMENT_STATE_STOPPED` and billing stops.

## Restart a deployment

A stopped deployment doesn't restart on its own. To bring it back, raise both bounds to `1` or more:

```bash CLI theme={null}
tg beta endpoints update dep_abc123 --min-replicas 1 --max-replicas 2
```

## List resources

List and get endpoints with the CLI:

```bash CLI theme={null}
# All endpoints in the project
tg beta endpoints ls

# One endpoint (includes up to the 10 newest deployments' state and replica counts)
tg beta endpoints get ep_abc123
```

Endpoint get and list responses embed lightweight deployment summaries in each endpoint's `deployments` array. The array includes at most the 10 newest deployments per endpoint (ordered by `createdAt`, descending). To list every deployment on an endpoint, use the [SDK or API](/reference/dmi/deployments-list).

### List flags

`tg beta endpoints ls` accepts these flags:

| Flag       | Description                                               |
| ---------- | --------------------------------------------------------- |
| `--limit`  | Maximum number of endpoints to return.                    |
| `--after`  | Pagination cursor to start from.                          |
| `--org`    | List org-scoped endpoints instead of project-scoped ones. |
| `--public` | List public endpoints.                                    |

List responses are paginated: when more results are available, the response includes `next_cursor`, which you pass as `--after` on the next request.

## Delete resources

Deletion is permanent. A deployment must be stopped before it can be deleted. Follow this order:

1. [Scale the deployment to zero](#stop-a-deployment) and wait for `DEPLOYMENT_STATE_STOPPED`.
2. Delete the deployment. If you use the SDK or API (not the CLI), set the deployment's [traffic split](/docs/dedicated-endpoints/route-traffic) weight to 0 on the endpoint first.
3. Delete the endpoint once it has no deployments.

The CLI's `rm` command is a smart-delete: it resolves the resource by its ID prefix, so the same command deletes an endpoint (`ep_`), a deployment (`dep_`), an A/B experiment (`abx_`), or a shadow experiment (`exp_`). When you run `tg beta endpoints rm dep_...`, the CLI automatically detaches the deployment from the traffic split and from any experiments it belongs to:

```bash CLI theme={null}
# Delete the deployment (must be stopped first; auto-detaches from the traffic split)
tg beta endpoints rm dep_abc123

# Delete the endpoint once it has no deployments
tg beta endpoints rm ep_abc123
```

To delete an endpoint that still has deployments, pass `--force` to `rm`. If the endpoint has other deployments you want to keep, rebalance the remaining weights instead of clearing the split. See [Route traffic](/docs/dedicated-endpoints/route-traffic).

## Troubleshooting

* **`endpoint_not_configured` (HTTP 400) though the deployment is `READY`:** Confirm the deployment is in the endpoint's [traffic split](/docs/dedicated-endpoints/route-traffic) with a non-zero weight.
* **Deployment `DEGRADED` with `Cannot place replicas: insufficient GPU capacity`:** Hardware for the config is constrained, so the scheduler couldn't place all replicas yet. Compare `status.scheduledReplicas` to `desiredReplicas`. The scheduler keeps retrying and the deployment starts once capacity frees up. To improve the chance of placement, request fewer replicas or choose a config with a smaller hardware footprint.
* **Deployment `DEGRADED` with `Startup stalled` or `Not ready`:** A placed replica is still booting or hit a startup failure. Read the detail after the colon in `status.message`. The deployment stays `DEGRADED` rather than `FAILED` once any replica has been successfully started.
* **Deployment `FAILED` with `Timed out waiting for readiness`:** No replica could be provisioned within six hours of the current run's start. Read the stall cause at the end of `status.message`. Restart the deployment to begin a fresh budget.
* **Deployment `FAILED` for another reason:** Read `status.message`. Common causes include deterministic placement rejection (`Cannot place replicas: …`), manifest generation failure, or remediation exhaustion.
* **Model not supported:** Not every model can be deployed. See the [model catalog](/docs/dedicated-endpoints/models). A fine-tuned model deploys only if its base model is supported.
* **Deploy fails with `the model has no revisions to deploy`:** The model record exists but has no uploaded weights yet. Finish [uploading the model](/docs/dedicated-endpoints/custom-models#upload-the-model) and wait for the upload to succeed before you deploy it.
* **Deploy fails with a revision validation error:** When you pin a specific model or speculator revision, that revision must have passed validation first. Deploy the latest validated revision, or wait for the pinned revision to finish validating.
* **Deployment delete fails with `the deployment is referenced by an endpoint's traffic split and cannot be deleted; please drop traffic split weight to 0 before deleting the deployment` (HTTP 400):** The deployment still has weight in the endpoint's [traffic split](/docs/dedicated-endpoints/route-traffic). Set its weight to 0 (or remove it from the split) before deleting. The CLI's `tg beta endpoints rm dep_...` detaches it automatically.

## Next steps

<CardGroup>
  <Card title="Configure autoscaling" icon="arrows-maximize" href="/docs/dedicated-endpoints/scaling">
    Autoscale a deployment on the right metric.
  </Card>

  <Card title="Route traffic" icon="route" href="/docs/dedicated-endpoints/route-traffic">
    Split traffic across deployments behind one endpoint.
  </Card>

  <Card title="Observability" icon="chart-line" href="/docs/dedicated-endpoints/monitoring">
    Monitor metrics and scrape the Prometheus-compatible endpoint.
  </Card>

  <Card title="Pricing" icon="cash" href="/docs/dedicated-endpoints/pricing">
    Understand per-minute and reserved pricing.
  </Card>
</CardGroup>
