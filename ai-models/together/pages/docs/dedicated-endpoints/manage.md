---
title: "Manage endpoints and deployments"
source: https://docs.together.ai/docs/dedicated-endpoints/manage
path: docs/dedicated-endpoints/manage
---

Create, update, and delete resources for dedicated model inference.

This page covers the lifecycle operations for dedicated model inference (DMI): creating endpoints and deployments, scaling, stopping, and deleting resources.

The CLI's `tg beta endpoints deploy` command bundles several API/SDK operations into one step for convenience: it creates the endpoint (when you pass a new endpoint name), attaches a deployment to it, and routes 100% of traffic to that deployment. This page shows the individual operations underneath it.

To create your first deployment end-to-end, [follow the quickstart](/docs/dedicated-endpoints/quickstart).

You can run every operation on this page from the Together CLI and SDK or from the [web console](https://api.together.ai/endpoints). Each section below shows both: the CLI or SDK command, and the equivalent steps in the console.

## Create an endpoint

When you deploy a model to a new endpoint, Together creates the endpoint, attaches the deployment, and routes all traffic to it. (To create an endpoint resource with no deployments, use the [SDK or API](/reference/dmi/endpoints-create).)

Before you deploy, choose a [supported model](/docs/dedicated-endpoints/models) and a [deployment profile](/docs/dedicated-endpoints/configs).

<Tabs>
  <Tab title="CLI">
    Pass a model and a new endpoint name to `tg beta endpoints deploy`. It creates the endpoint, attaches a deployment on the model's default hardware, and routes 100% of traffic to it:

    ```bash CLI theme={null}
    tg beta endpoints deploy google/gemma-4-E4B-it \
      --endpoint my-endpoint
    ```

    Add `--config <cr_...>` when the model has more than one deployment profile, and `--min-replicas` / `--max-replicas` to set the [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds).
  </Tab>

  <Tab title="Console">
    <Steps>
      <Step title="Open the create form">
        On the [Endpoints page](https://api.together.ai/endpoints), select **New endpoint**.
      </Step>

      <Step title="Name the endpoint and deployment">
        Enter an **Endpoint name** and a **Deployment name**.
      </Step>

      <Step title="Choose the model and hardware">
        Select the **Model** and its **Quantization**, then pick a **Hardware** configuration and a **Region**. The console lists one hardware card per [deployment profile](/docs/dedicated-endpoints/concepts#deployment-profile), so the model and quantization you choose determine the config.
      </Step>

      <Step title="Set autoscaling">
        Set **Min replicas** and **Max replicas** (both default to `1`).
      </Step>

      <Step title="Create the endpoint">
        Select **Create endpoint**. Together creates the endpoint and its first deployment and routes all traffic to it.
      </Step>
    </Steps>
  </Tab>
</Tabs>

The endpoint serves as a logical grouping of deployments, and the entry point for [routing traffic to your models](/docs/dedicated-endpoints/route-traffic).

## Create a deployment

Add more deployments to an endpoint to run several models or hardware configs behind it, for [traffic splitting](/docs/dedicated-endpoints/split-traffic), [A/B tests](/docs/dedicated-endpoints/ab-tests), or [shadow experiments](/docs/dedicated-endpoints/shadow-experiments). It works like [creating an endpoint](#create-an-endpoint), except you target an existing endpoint and give the deployment a traffic weight so it takes a share of the [traffic split](/docs/dedicated-endpoints/route-traffic).

<Tabs>
  <Tab title="CLI">
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

    The CLI defaults `--min-replicas` and `--max-replicas` to `1`, so a bare `deploy` creates a single-replica deployment. If you pass only `--min-replicas`, the max matches it. `--min-replicas 0` alone creates the deployment stopped.

    For the full flag list, including placement, the autoscaling windows, and the scaling percentile, see the [CLI reference](/reference/cli/endpoints-beta#deploy).
  </Tab>

  <Tab title="Console">
    Open the endpoint from the [Endpoints page](https://api.together.ai/endpoints) and select **New deployment**. The dialog has the same fields as the create form ([Create an endpoint](#create-an-endpoint)), plus a **Traffic weight**: leave it at `0` to add the deployment without serving live traffic (for example, as an [A/B](/docs/dedicated-endpoints/ab-tests) variant). Fill in the fields and select **Create deployment**.

    <Frame>
      <img alt="The New deployment dialog in the Together AI console, with fields for deployment name, model, quantization, hardware, region, autoscaling replica bounds, and traffic weight." />
    </Frame>
  </Tab>
</Tabs>

After you've created a deployment, you'll need to [route traffic](/docs/dedicated-endpoints/route-traffic) to it before it can serve requests.

## Poll deployment status

<Tabs>
  <Tab title="CLI / SDK">
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
  </Tab>

  <Tab title="Console">
    Open the deployment from the endpoint's **Overview** tab to watch its status live. The **Status** card shows the current state (for example, Ready), the ready and scheduled replica counts, and a status message, and the **Replicas** chart plots desired versus ready replicas over time.

    <Frame>
      <img alt="A deployment detail page in the Together AI console, showing the Model, Hardware and placement, Status, and Deployment configuration cards, a replica-count chart, and the deployment's logs." />
    </Frame>
  </Tab>
</Tabs>

The status object exposes these fields:

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

Deployment scale is controlled by the deployment's [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds), and optionally autoscaled using [scaling metrics](/docs/dedicated-endpoints/scaling#scaling-metrics). Set the initial bounds when you create the deployment, then change them on a running deployment.

<Tabs>
  <Tab title="CLI">
    ```bash CLI theme={null}
    tg beta endpoints update dep_abc123 --min-replicas 2 --max-replicas 4
    ```
  </Tab>

  <Tab title="Console">
    On the deployment's detail page, select **Edit** on the **Deployment configuration** card. Change **Min replicas** and **Max replicas** (and, optionally, the **Scaling metric**), then select **Save changes**. The console applies the change in place, without restarting the deployment or creating a new one.

    <Frame>
      <img alt="The Edit configuration dialog in the Together AI console, with inputs for min and max replicas, scale-up and scale-down windows, traffic weight, and a scaling-metric target." />
    </Frame>
  </Tab>
</Tabs>

## Stop a deployment

A deployment runs until you stop it. Stopping scales it to zero replicas and releases its hardware.

<Tabs>
  <Tab title="CLI">
    Set both replica bounds to `0`:

    ```bash CLI theme={null}
    tg beta endpoints update dep_abc123 --min-replicas 0 --max-replicas 0
    ```
  </Tab>

  <Tab title="Console">
    On the deployment's detail page, select **Stop**. Stopping scales the deployment to zero without deleting it, so you can start it again later.
  </Tab>
</Tabs>

The replicas keep serving until they finish draining, then the deployment moves to `DEPLOYMENT_STATE_STOPPED` and billing stops.

## Restart a deployment

A stopped deployment doesn't restart on its own. Only deployments in `DEPLOYMENT_STATE_STOPPED` can be restarted. A deployment in `FAILED` is terminal and can't be brought back this way; [deploy a new deployment](#create-a-deployment) instead. To restart a stopped deployment, raise both bounds to `1` or more.

<Tabs>
  <Tab title="CLI">
    ```bash CLI theme={null}
    tg beta endpoints update dep_abc123 --min-replicas 1 --max-replicas 2
    ```
  </Tab>

  <Tab title="Console">
    On the deployment's detail page, select **Start**, then confirm the **Min replicas** and **Max replicas** to bring it back with.
  </Tab>
</Tabs>

## List resources

<Tabs>
  <Tab title="CLI">
    List and get endpoints with the CLI:

    ```bash CLI theme={null}
    # All endpoints in the project
    tg beta endpoints ls

    # One endpoint (includes up to the 10 newest deployments' state and replica counts)
    tg beta endpoints get ep_abc123
    ```
  </Tab>

  <Tab title="Console">
    The [Endpoints page](https://api.together.ai/endpoints) lists every endpoint in the current project with its status, model, GPU, and ready/desired replica counts. Single-deployment endpoints collapse into one row; endpoints with more than one deployment expand to show each deployment.

    <Frame>
      <img alt="The Endpoints list in the Together AI console, with columns for name, status, model, GPU, replicas, and created date, and a New endpoint button." />
    </Frame>

    Select an endpoint to open its detail page. The **Overview** tab lists its deployments alongside the endpoint's details and a ready-to-run code sample.

    <Frame>
      <img alt="An endpoint detail page in the Together AI console, showing the Overview, Traffic Tests, Analytics, and Logs tabs, a deployments table, a code sample, and the endpoint's details." />
    </Frame>
  </Tab>
</Tabs>

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

<Tabs>
  <Tab title="CLI">
    The CLI's `rm` command is a smart-delete: it resolves the resource by its ID prefix, so the same command deletes an endpoint (`ep_`), a deployment (`dep_`), an A/B experiment (`abx_`), or a shadow experiment (`exp_`). When you run `tg beta endpoints rm dep_...`, the CLI automatically detaches the deployment from the traffic split and from any experiments it belongs to:

    ```bash CLI theme={null}
    # Delete the deployment (must be stopped first; auto-detaches from the traffic split)
    tg beta endpoints rm dep_abc123

    # Delete the endpoint once it has no deployments
    tg beta endpoints rm ep_abc123
    ```

    To delete an endpoint that still has deployments, pass `--force` to `rm`. If the endpoint has other deployments you want to keep, rebalance the remaining weights instead of clearing the split. See [Route traffic](/docs/dedicated-endpoints/route-traffic).
  </Tab>

  <Tab title="Console">
    First [stop](#stop-a-deployment) every deployment under the endpoint. Then open the endpoint, select **Endpoint actions**, and select **Delete endpoint**. The console keeps **Delete endpoint** disabled until every deployment is stopped or deleted, so there's no console equivalent of the CLI's `rm --force` on a running endpoint.

    <Frame>
      <img alt="The Endpoint actions menu open in the Together AI console, with a Delete endpoint item that is disabled while a deployment is still running." />
    </Frame>
  </Tab>
</Tabs>

## Troubleshooting

* **`endpoint_not_configured` (HTTP 400) though the deployment is `READY`:** Confirm the deployment is in the endpoint's [traffic split](/docs/dedicated-endpoints/route-traffic) with a non-zero weight.
* **Deployment `DEGRADED` with `Cannot place replicas: insufficient GPU capacity`:** Hardware for the config is constrained, so the scheduler couldn't place all replicas yet. Compare `status.scheduledReplicas` to `desiredReplicas`. The scheduler keeps retrying and the deployment starts once capacity frees up. To improve the chance of placement, request fewer replicas or choose a config with a smaller hardware footprint.
* **Deployment `DEGRADED` with `Startup stalled` or `Not ready`:** A placed replica is still booting or hit a startup failure. Read the detail after the colon in `status.message`. The deployment stays `DEGRADED` rather than `FAILED` once any replica has been successfully started.
* **Deployment `FAILED` with `Timed out waiting for readiness`:** No replica could be provisioned within six hours of the current run's start. Read the stall cause at the end of `status.message`. [Deploy a new deployment](#create-a-deployment) to try again with a fresh readiness budget.
* **Restart fails with `the deployment is in a terminal FAILED state and cannot be restarted; create a new deployment` (HTTP 400):** A `FAILED` deployment can't be brought back by raising replica bounds. [Deploy a new deployment](#create-a-deployment) on the endpoint instead.
* **Restart fails with `the deployment must be stopped before it can be restarted` (HTTP 400):** Wait for the deployment to reach `DEPLOYMENT_STATE_STOPPED` after you [stop it](#stop-a-deployment), or confirm both replica bounds are `0`, before raising them again.
* **Deployment `FAILED` for another reason:** Read `status.message`. Common causes include deterministic placement rejection (`Cannot place replicas: …`), manifest generation failure, or remediation exhaustion.
* **Model not supported:** Not every model can be deployed. See the [model catalog](/docs/dedicated-endpoints/models). A fine-tuned model deploys only if its base model is supported.
* **Deploy fails with `the model has no revisions to deploy`:** The model record exists but has no uploaded weights yet. Finish [uploading the model](/docs/dedicated-endpoints/custom-models#upload-the-model) and wait for the upload to succeed before you deploy it.
* **Deploy fails with a revision validation error:** When you pin a specific model or speculator revision, that revision must have passed validation first. Check `validationStatus` on the revision ([custom models](/docs/dedicated-endpoints/custom-models#check-revision-validation), [adapters](/docs/dedicated-endpoints/adapter#check-revision-validation)). Deploy the latest validated revision, or wait for the pinned revision to finish validating.
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
