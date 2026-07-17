---
title: "Migrate from v1"
source: https://docs.together.ai/docs/dedicated-endpoints/migrate-from-v1
path: docs/dedicated-endpoints/migrate-from-v1
---

Move a dedicated endpoint from the v1 API to the v2 dedicated model inference resource model.

This guide is for existing [dedicated endpoints (v1)](/docs/dedicated-endpoints/v1/overview) users moving to the current platform (v2). It explains what changed, what stays the same, and how to recreate a v1 endpoint under the [v2 resource model](/docs/dedicated-endpoints/concepts).

<Warning>
  Creating a new v1 endpoint and restarting a stopped or paused one are no longer available. These operations now return `endpoints_v1_create_access_disabled` (HTTP 403) through the API (`POST /v1/endpoints`), SDK (`client.endpoints.create(...)`), CLI (`tg endpoints create`), and web UI. To create a new endpoint or bring a stopped v1 endpoint back online, deploy the model on v2 using the [steps below](#migrate-an-endpoint). If you're troubleshooting one of these errors, jump to [Troubleshooting](#troubleshooting).
</Warning>

Endpoints that are already running on v1 keep serving and stay supported until further notice, so you can migrate those on your own schedule. Once a running v1 endpoint stops, it can't be restarted on v1, so you'll need to redeploy it as a new v2 endpoint. Migrating also unlocks v2-only capabilities such as traffic splitting, A/B tests, shadow experiments, metric-based autoscaling, and monitoring dashboards. See [v2 capabilities](#v2-capabilities) below.

## What stays the same

The inference API hasn't changed. You still send requests to `POST /v1/chat/completions` (and the other inference endpoints) with your endpoint name in the `model` field. Dedicated model inference is served at `https://api-inference.together.ai`:

```bash theme={null}
curl -s -X POST https://api-inference.together.ai/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "your-project-slug/my-endpoint",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

The same applies to billing: dedicated model inference still bills per minute per running replica by hardware. See [Pricing](/docs/dedicated-endpoints/pricing) for details.

The main thing you'll need to change in your application is the `model` string. When you recreate an endpoint in v2, it gets a new endpoint string (`<project_slug>/<endpoint_name>`), so update your inference calls to use the new name.

## What's changed

v1 modeled a dedicated endpoint as a single model running on a hardware type. v2 splits that into a small resource model so one endpoint can host more than one model version and shift traffic between them:

* **Endpoint:** A stable inference URL. It no longer carries the model or hardware itself.
* **Deployment:** Binds a model and a config to an endpoint with an [autoscaling policy](/docs/dedicated-endpoints/scaling). A deployment is what runs replicas and serves traffic. One endpoint can host several deployments at once.
* **Config:** Describes how a model runs, including the hardware selectors and optimization profile. In v1 you passed a hardware ID and decoding flags. In v2 you select a [published config](/docs/dedicated-endpoints/configs) instead.
* **Traffic split:** Routes requests across an endpoint's deployments by weight. Even if it's `READY`, a deployment receives no traffic until you [route traffic](/docs/dedicated-endpoints/route-traffic) to it.

Read [Concepts](/docs/dedicated-endpoints/concepts) to review the full resource model before you migrate.

## Feature mapping

| v1                                                          | v2                                                     | Notes                                                                                                                                                                            |
| ----------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One model per endpoint.                                     | Endpoint plus one or more deployments.                 | The endpoint is now just a stable URL. The deployment runs the model.                                                                                                            |
| `--hardware <hardware_id>`                                  | A published config (`cr_...`).                         | Hardware is chosen through a config's selectors, not a hardware ID flag. See [Choose a config](/docs/dedicated-endpoints/configs).                                               |
| `--min-replicas` / `--max-replicas` on the endpoint         | `--min-replicas` / `--max-replicas` on the deployment. | Autoscaling is a property of the deployment. On a running deployment `min-replicas` is at least `1`.                                                                             |
| `--inactive-timeout <minutes>` (default 60) on the endpoint | No equivalent at launch.                               | v2 deployments run until you stop them or scale their [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds) to zero. There is no automatic idle shutdown at launch. |
| `--no-speculative-decoding` and other decoding flags.       | Config optimization profile.                           | Decoding optimizations are properties of the [config you select](/docs/dedicated-endpoints/configs#decoding-optimizations), not per-endpoint flags.                              |
| `--availability-zone`                                       | No direct equivalent yet.                              | Contact support if you have a specific zone requirement.                                                                                                                         |
| Custom model upload.                                        | Fine-tuned model upload.                               | Uploads are restricted to fine-tuned variants of the supported models. See [Upload a fine-tuned model](/docs/dedicated-endpoints/custom-models).                                 |
| LoRA adapter deployment.                                    | Not available at the initial launch.                   | Contact support if you rely on LoRA adapters.                                                                                                                                    |

## API mapping

v1 used the top-level `tg endpoints` CLI and SDK methods. v2 exposes these operations under the `tg beta` CLI and the `/v2` management API under `https://api.together.ai`. A few operations (editing a traffic split, listing deployments) are available from the SDK and API rather than the CLI. The table below maps each v1 command to its v2 equivalent:

| v1 operation                                             | v2 equivalent                                                                                                                                                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tg endpoints hardware --model <model>`                  | `tg beta models configs <model_id>` (configs encode the hardware).                                                                                                                                      |
| `tg endpoints create --model <m> --hardware <h>`         | `tg beta endpoints deploy <model_id> --endpoint <name> [--config <config_id>]` (creates the endpoint, deployment, and traffic split in one step).                                                       |
| `tg endpoints update --min-replicas --max-replicas <id>` | `tg beta endpoints update <deployment_id> --min-replicas <n> --max-replicas <n>` (pass the deployment ID; the CLI resolves the endpoint).                                                               |
| `tg endpoints stop <id>`                                 | `tg beta endpoints update <deployment_id> --min-replicas 0 --max-replicas 0` (scales the deployment to `0/0`).                                                                                          |
| `tg endpoints start <id>`                                | `tg beta endpoints update <deployment_id> --min-replicas 1 --max-replicas <n>` (raises both bounds to `1` or more).                                                                                     |
| `tg endpoints list` / `retrieve <id>`                    | `tg beta endpoints ls` and `tg beta endpoints get <endpoint_id>`. List deployments from the SDK or API.                                                                                                 |
| `tg endpoints delete <id>`                               | Stop the deployment, then smart-delete with `tg beta endpoints rm <deployment_id>` and `tg beta endpoints rm <endpoint_id>`. See [Delete resources](/docs/dedicated-endpoints/manage#delete-resources). |

For the individual CLI commands and SDK methods behind these operations, see [Manage deployments](/docs/dedicated-endpoints/manage).

## Migrate an endpoint

To move a v1 endpoint to v2, recreate it using the new resource model. Your v1 endpoint keeps serving while you stand up the v2 one, so you can cut over with no downtime. While both endpoints run during the cutover, you pay for the GPUs of both, so retire the v1 endpoint as soon as traffic is on v2.

1. **Find the model and a config:** List the [supported models](/docs/dedicated-endpoints/models) and the [configs](/docs/dedicated-endpoints/configs) published for the model your v1 endpoint runs, and save a model ID (`ml_...`) and config ID (`cr_...`).
2. **Deploy the model:** Run `tg beta endpoints deploy <model_id> --endpoint <name> --config <config_id>`, matching the replica bounds to your v1 endpoint with `--min-replicas` and `--max-replicas`. This creates the endpoint, deployment, and traffic split, and returns while the deployment provisions in the background. Save the qualified endpoint name (`your-project-slug/<name>`); this is the new value for your inference `model` field.
3. **Cut over:** Update your application's `model` field to the new qualified endpoint name and [send a test request](/docs/dedicated-endpoints/requests).
4. **Retire the v1 endpoint:** Once traffic is on v2, stop the v1 endpoint with `tg endpoints stop <id>` so it stops billing.

The [quickstart](/docs/dedicated-endpoints/quickstart) walks through deploying and calling a v2 endpoint end-to-end.

## Migrate fine-tuned models

Uploaded models carry over, but you must re-upload them into the v2 model catalog and reference them by model ID in a deployment:

* **Fine-tuned models:** See [Upload a fine-tuned model](/docs/dedicated-endpoints/custom-models).
* **LoRA adapters:** Not available at the initial launch.

Note the eligibility change: in v1 you could upload arbitrary models, but a v2 upload must be a fine-tuned variant of a base model architecture that Together AI already serves.

## Troubleshooting

Most migration errors have one cause: v1 create and restart are retired. This is not a permissions problem. Your models, fine-tuned checkpoints, hardware, and API key still work, so there is nothing to enable or restore. The fix is always the same: deploy the model on v2 using the [steps above](#migrate-an-endpoint).

| Error or symptom                                                                                         | What to do                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `endpoints_v1_create_access_disabled` (HTTP 403) when creating an endpoint through the API, SDK, or CLI. | Create the endpoint on v2 instead, through the [UI](https://api.together.ai/endpoints/configure), the [SDK or API](/reference/dmi/endpoints-create), or `tg beta endpoints deploy`.                                                    |
| A stopped or paused v1 endpoint won't start again.                                                       | Stopped v1 endpoints can't be restarted. Redeploy the same model as a new v2 endpoint; fine-tuned models don't need retraining (see [Migrate fine-tuned models](#migrate-fine-tuned-models)).                                          |
| Create still fails after changing replica bounds, autoscaling, or start settings.                        | Those settings don't affect the v1 create restriction. Deploy the model on v2.                                                                                                                                                         |
| The SDK still calls the v1 endpoints API.                                                                | Upgrade to `together>=2.24.0` ([release notes](https://github.com/togethercomputer/together-py/releases/tag/v2.24.0)), which introduces the v2 endpoint flow, and follow the [v2 endpoint reference](/reference/dmi/endpoints-create). |
| The CLI still calls v1 (`tg endpoints ...`).                                                             | Install or upgrade the CLI (below), then use the `tg beta models` and `tg beta endpoints` commands.                                                                                                                                    |
| You can't find a `/v2/endpoints` route in the docs or SDK.                                               | The v2 management API is served under `https://api.together.ai`. See the [endpoint reference](/reference/dmi/endpoints-create) and [CLI reference](/reference/cli/endpoints-beta).                                                     |

To move the CLI to the v2 commands, install or upgrade it:

```bash theme={null}
uv tool install "together[cli]"
uv tool upgrade "together[cli]"
```

See the [models](/reference/cli/models-beta) and [endpoints](/reference/cli/endpoints-beta) CLI reference for the full command set.

## v2 capabilities

Migrating your endpoint to v2 gives you access to several new capabilities:

* [Split traffic across deployments](/docs/dedicated-endpoints/split-traffic): Host several deployments behind one endpoint URL and route requests between them by weight.
* [Run A/B tests](/docs/dedicated-endpoints/ab-tests): Compare a candidate deployment against a baseline on live traffic before you promote it.
* [Run a shadow experiment](/docs/dedicated-endpoints/shadow-experiments): Test a new deployment in production without affecting live traffic.
* [Autoscale on a metric](/docs/dedicated-endpoints/scaling): Scale each deployment on the metric that fits your workload, and stop it when you don't need it to release the hardware.
* [Monitor endpoints](/docs/dedicated-endpoints/monitoring): Track latency, throughput, and utilization in built-in dashboards, and trace lifecycle changes through the events feed.

## Timeline and support

Existing v1 endpoints keep running until further notice, so you can migrate on your own schedule. Create all new endpoints and redeploy v1 endpoints that have stopped on v2.

## Next steps

<CardGroup>
  <Card title="Concepts" icon="sitemap" href="/docs/dedicated-endpoints/concepts">
    Learn the project, model, config, endpoint, and deployment model.
  </Card>

  <Card title="Quickstart" icon="rocket" href="/docs/dedicated-endpoints/quickstart">
    Recreate an endpoint end to end with the CLI or SDK.
  </Card>

  <Card title="Choose a deployment profile" icon="adjustments-horizontal" href="/docs/dedicated-endpoints/configs">
    Find the config that replaces your v1 hardware ID.
  </Card>

  <Card title="Manage deployments" icon="tool" href="/docs/dedicated-endpoints/manage">
    Create, inspect, scale, stop, and delete endpoints and deployments.
  </Card>
</CardGroup>
