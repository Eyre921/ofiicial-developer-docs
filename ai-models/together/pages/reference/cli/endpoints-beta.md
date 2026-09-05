---
title: "Endpoints"
source: https://docs.together.ai/reference/cli/endpoints-beta
path: reference/cli/endpoints-beta
---

Deploy and manage dedicated inference endpoints from your terminal.

Manage [dedicated model inference](/docs/dedicated-endpoints/overview) deployments and endpoints on the 2.0 API.

<Note>
  These commands target the 2.0 API. For the 1.0 endpoint commands, see [`endpoints`](/reference/cli/endpoints). Commands run within a Together [project](/docs/projects).
</Note>

## Deploy

Deploy a model to a new endpoint. If you pass the name or ID of an existing endpoint to `--endpoint`, the model deploys to that endpoint. If you pass a new name, the CLI creates the endpoint first, then deploys. The model is passed as the positional `MODEL` argument.

```bash Shell theme={null}
tg beta endpoints deploy zai-org/GLM-5.2 \
  --endpoint my-glm-endpoint \
  --min-replicas 1 \
  --max-replicas 3
```

When a model has more than one [deployment profile](/docs/dedicated-endpoints/concepts#deployment-profile), pass the profile's exact `modelName` (from `tg beta models public`) as `MODEL` to select that profile, or re-run with `--config <cr_...>`. If the name still matches more than one profile, `deploy` returns an error that lists each profile's `modelName`, config ID, quantization, GPUs, and parallelism, and shows an example `--model <modelName> --config <cr_...>` command. When a model has a single profile, the CLI selects it automatically.

The CLI defaults `--min-replicas` and `--max-replicas` to 1, which may differ from the raw API defaults. If you pass only one bound, the CLI infers the other: `--min-replicas` alone mirrors into the max (including `0` to create the deployment stopped), and `--max-replicas 0` alone lowers the min to `0`. Passing `0` for one bound and a positive value for the other is an error.

### Parameters

| Flag                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MODEL`                                           | (**required**) The model to deploy. Accepts a public architecture name (for example `zai-org/GLM-5.2`), a profile `modelName` from [`tg beta models public`](/reference/cli/models-beta#list-public-models) (for example `zai-org/GLM-5.2-FP8`), a private model name, a private model ID (for example `ml_abc123`), or a fully resolved model path. An exact profile `modelName` selects that profile when it uniquely matches. |
| `--endpoint [string]`                             | (**required**) The endpoint to deploy to. Pass an existing endpoint name or ID to add the deployment to it, or a new name to create the endpoint first.                                                                                                                                                                                                                                                                          |
| `--config [string]`                               | Config ID (`cr_...`) for this model. Run `tg beta models configs <model_id>` to list available configs. Auto-selected when the model has a single deployment profile, or when `MODEL` is an exact profile `modelName` that uniquely matches. Required when more than one profile still matches.                                                                                                                                  |
| `--min-replicas [number]`                         | Minimum number of replicas. Default: 1. When passed alone, `--max-replicas` matches it. `--min-replicas 0` alone creates the deployment stopped.                                                                                                                                                                                                                                                                                 |
| `--max-replicas [number]`                         | Maximum number of replicas. Must be greater than or equal to `--min-replicas`. Defaults to the `--min-replicas` value, or 1 when neither flag is set. `--max-replicas 0` alone also lowers the minimum to `0`.                                                                                                                                                                                                                   |
| `--scale-up-window [string]`                      | How long the scaling metric must stay above target before adding replicas, in seconds (for example `30` or `30s`). Prevents thrashing from brief spikes.                                                                                                                                                                                                                                                                         |
| `--scale-down-window [string]`                    | Cooldown after a scale-down before removing more replicas, in seconds (for example `60` or `60s`). Higher values improve stability.                                                                                                                                                                                                                                                                                              |
| `--scaling-metric [string]`                       | Autoscaling metric to scale on: `inflight_requests`, `gpu_utilization`, `token_utilization`, `cache_hit_rate`, `throughput_per_replica`, `ttft`, `decoding_speed`, or `e2e_latency`. Must be set together with `--scaling-target`. See [Configure autoscaling](/docs/dedicated-endpoints/scaling#scaling-metrics).                                                                                                               |
| `--scaling-target [number]`                       | Target value for `--scaling-metric`. Utilization metrics use `0`–`100`. Other metrics use their native units.                                                                                                                                                                                                                                                                                                                    |
| `--scaling-percentile [p50 \| p90 \| p95 \| p99]` | Optional percentile for the latency metrics (`ttft`, `decoding_speed`, `e2e_latency`). Defaults to `p95`.                                                                                                                                                                                                                                                                                                                        |
| `--deployment-name [string]`                      | Name for the deployment created by this command. Defaults to a combination of the endpoint and model names.                                                                                                                                                                                                                                                                                                                      |
| `--model-revision [string]`                       | Deprecated. Model revision ID to pin the deployment to. Prefer passing a fully qualified model path ending in `/revisions/<REVISION_ID>` as the `MODEL` argument.                                                                                                                                                                                                                                                                |
| `--placement [string]`                            | Placement profile to use.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `--placement.regions [string]`                    | Comma-separated inline placement regions.                                                                                                                                                                                                                                                                                                                                                                                        |
| `--placement.constraint [required \| preferred]`  | How strictly to enforce the inline placement.                                                                                                                                                                                                                                                                                                                                                                                    |
| `--enable-lora`                                   | Run the multi-LoRA kernel so adapters hot-load after deploy. Toggling this later requires a redeploy.                                                                                                                                                                                                                                                                                                                            |
| `--traffic-weight [number]`                       | Relative capacity weight for this deployment in the endpoint's live traffic split. Set to `0` for no live traffic, or omit to leave routing unchanged.                                                                                                                                                                                                                                                                           |

## List

List endpoints in the current project.

```bash Shell theme={null}
tg beta endpoints ls
```

### Parameters

| Flag               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `--org`            | List org-scoped endpoints instead of project-scoped ones. |
| `--public`         | List public endpoints.                                    |
| `--limit [number]` | Maximum number of endpoints to return.                    |
| `--after [string]` | Pagination cursor to start from.                          |

## Get

Print details for an endpoint or deployment. Pass an endpoint ID (`ep_...`) to see its deployments and traffic split, or pass a deployment ID (`dep_...`) to inspect that deployment directly.

Endpoint responses include at most the 10 newest deployment summaries per endpoint. To list every deployment, use the [deployments list API](/docs/dedicated-endpoints/manage#list-resources).

```bash Shell theme={null}
tg beta endpoints get ep_abc123
tg beta endpoints get dep_abc123
```

With `--json`, endpoint responses expose deployment state under `deployments[].state`, while deployment responses expose it under `status.state`.

## Update

Update a deployment's parameters: change its [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds), adjust autoscaling, set its share of endpoint traffic, or change an A/B variant's percent. Pass the deployment ID (`dep_...`). The CLI resolves its parent endpoint automatically. At least one option must be set.

```bash Shell theme={null}
# Set a deployment's replica bounds
tg beta endpoints update dep_abc123 --min-replicas 2 --max-replicas 4

# Scale on a specific metric and target
tg beta endpoints update dep_abc123 --scaling-metric gpu_utilization --scaling-target 70

# Stop a deployment by scaling it to zero
tg beta endpoints update dep_abc123 --min-replicas 0 --max-replicas 0

# Set a deployment's weight in the endpoint traffic split
tg beta endpoints update dep_abc123 --traffic-weight 30

# Take a deployment out of rotation without scaling it down
tg beta endpoints update dep_abc123 --traffic-weight 0

# Set an A/B variant's percent (takes from or returns to control)
tg beta endpoints update dep_variant456 --ab-percent 20
```

### Parameters

| Flag                                              | Description                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ID`                                              | (**required**) The deployment ID to update (`dep_...`).                                                                                                                                                                                                                                                            |
| `--min-replicas [number]`                         | Updated minimum replicas. To stop the deployment, pass both `--min-replicas 0` and `--max-replicas 0`. A single zero bound is an error.                                                                                                                                                                            |
| `--max-replicas [number]`                         | Updated maximum replicas. Must be greater than or equal to `--min-replicas`.                                                                                                                                                                                                                                       |
| `--scale-up-window [string]`                      | Autoscaling scale-up stabilization window.                                                                                                                                                                                                                                                                         |
| `--scale-down-window [string]`                    | Autoscaling scale-down stabilization window.                                                                                                                                                                                                                                                                       |
| `--scaling-metric [string]`                       | Autoscaling metric to scale on: `inflight_requests`, `gpu_utilization`, `token_utilization`, `cache_hit_rate`, `throughput_per_replica`, `ttft`, `decoding_speed`, or `e2e_latency`. Must be set together with `--scaling-target`. See [Configure autoscaling](/docs/dedicated-endpoints/scaling#scaling-metrics). |
| `--scaling-target [number]`                       | Target value for `--scaling-metric`. Utilization metrics use `0`–`100`. Other metrics use their native units.                                                                                                                                                                                                      |
| `--scaling-percentile [p50 \| p90 \| p95 \| p99]` | Optional percentile for the latency metrics (`ttft`, `decoding_speed`, `e2e_latency`). Defaults to `p95`.                                                                                                                                                                                                          |
| `--traffic-weight [number]`                       | Capacity weight for this deployment in the endpoint traffic split. Preserves the weights of the other deployments. Set to `0` to stop routing to this deployment. See [Split traffic](/docs/dedicated-endpoints/split-traffic).                                                                                    |
| `--ab-percent [number]`                           | A/B experiment traffic percentage for this **variant** deployment (1–99). Takes from or returns percentage to the control only. Other variants are unchanged. Errors if the deployment is not in an A/B experiment or is the control. See [Ramp the variant](/docs/dedicated-endpoints/ab-tests#ramp-the-variant). |
| `--etag [string]`                                 | ETag for optimistic concurrency on the deployment update. Does not apply to `--ab-percent` or `--traffic-weight`.                                                                                                                                                                                                  |

<Note>
  LoRA loading can't be changed after a deployment is created. To turn LoRA on or off, redeploy the model with [`deploy --enable-lora`](#deploy).
</Note>

## Delete

Delete an endpoint, deployment, A/B experiment, or shadow experiment. The command infers the resource type from the ID prefix (`ep_`, `dep_`, `abx_`, or `exp_`).

```bash Shell theme={null}
tg beta endpoints rm ep_abc123
```

Alias: `tg beta endpoints -d`.

### Parameters

| Flag      | Description                                                                              |
| --------- | ---------------------------------------------------------------------------------------- |
| `ID`      | (**required**) The resource ID to delete (`ep_...`, `dep_...`, `abx_...`, or `exp_...`). |
| `--force` | Force-delete an endpoint that still has deployments.                                     |

## Events

List an endpoint's audit and lifecycle events, newest first. The feed merges endpoint-scoped events with the deployment-scoped events of every deployment under the endpoint. See [Monitoring](/docs/dedicated-endpoints/monitoring#events) for how to read the feed.

```bash Shell theme={null}
tg beta endpoints events ep_abc123
```

The command prints one page of events with time, type, source, and message columns. When more events remain, it prints the `--after` command that displays the next page. Add `--json` for the raw event objects, including fields the table view omits, such as the event ID, level, and source kind.

### Parameters

| Flag                                           | Description                                                                                                                  |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `ID`                                           | (**required**) The endpoint ID or name whose events to list.                                                                 |
| `--deployment-ids [string]`                    | Comma-separated deployment IDs whose events should be included. Filtering by deployment excludes endpoint-scoped events.     |
| `--min-level [debug \| info \| warn \| error]` | Minimum severity to include. Omit to disable severity filtering.                                                             |
| `--types [string]`                             | Comma-separated event types to include, such as `deployment.scaled` or `condition.set`.                                      |
| `--subject-id [string]`                        | ID of a subject associated with the event, such as a rollout (`rol_...`), to read one subject's audit trail out of the feed. |
| `--since [datetime]`                           | Return only events at or after this time.                                                                                    |
| `--until [datetime]`                           | Return only events strictly before this time.                                                                                |
| `--limit [number]`                             | Maximum number of events to return. Max 10000, default 50.                                                                   |
| `--after [string]`                             | Pagination cursor from a previous response.                                                                                  |

## A/B test

Fork a percentage of an endpoint's live traffic from a control deployment to a new variant model, then compare the two. See [A/B testing](/docs/dedicated-endpoints/ab-tests) for the full workflow.

```bash Shell theme={null}
tg beta endpoints ab zai-org/GLM-5.2 \
  --control dep_control123 \
  --percent 10
```

### Parameters

| Flag                 | Description                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `MODEL`              | (**required**) The variant model to test. Accepts the same forms as [`deploy`](#deploy).                                        |
| `--control [string]` | (**required**) The control deployment ID currently serving live traffic.                                                        |
| `--percent [number]` | (**required**) Percentage of traffic (1–99) to route to the variant. The control keeps the remainder and must stay at least 1%. |
| `--config [string]`  | Config revision ID for the variant deployment. Defaults to the model's default config.                                          |
| `--enable-lora`      | Run the multi-LoRA kernel so adapters hot-load after deploy.                                                                    |
| `--name [string]`    | Name for the variant deployment. Defaults to the model name with a short suffix.                                                |

## Shadow

Mirror a fraction of an endpoint's live traffic to a new model without affecting responses returned to clients. See [Shadow deployments](/docs/dedicated-endpoints/shadow-experiments) for details.

```bash Shell theme={null}
tg beta endpoints shadow ep_abc123 zai-org/GLM-5.2 \
  --rate 0.1
```

### Parameters

| Flag                    | Description                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------- |
| `ENDPOINT`              | (**required**) The endpoint ID serving the live traffic to shadow from.               |
| `MODEL`                 | (**required**) The model to shadow to. Accepts the same forms as [`deploy`](#deploy). |
| `--config [string]`     | Config revision ID for the shadow deployment. Defaults to the model's default config. |
| `--name [string]`       | Name for the shadow deployment. Defaults to the model name with a short suffix.       |
| `--rate [number]`       | Fraction of live traffic to mirror (0.0–1.0).                                         |
| `--key [string]`        | Request-body field to use for sticky, key-based sampling.                             |
| `--target-qps [number]` | Per-gateway-replica target QPS for adaptive sampling.                                 |
| `--window [string]`     | Sliding window for adaptive-sampling QPS observation. Default: `60s`.                 |
| `--enable-lora`         | Run the multi-LoRA kernel so adapters hot-load after deploy.                          |

## Global options

Every command also accepts the [global parameters](/reference/cli/getting-started#global-parameters), including `--json` for machine-readable output and `--project` to override the target project.

The 2.0 endpoint commands operate within a Together project. The CLI reads the project from the `TOGETHER_PROJECT_ID` environment variable, or you can pass `--project` on any command. Without either setting, an interactive `deploy` asks you to confirm the project associated with your API key. In CI, agents, `--non-interactive` mode, or `--json` mode, set the project explicitly before deploying.

```bash Shell theme={null}
export TOGETHER_PROJECT_ID=<your_project_id>
```

## Resource IDs

The 2.0 API models an endpoint as a stable address that points at one or more deployments. Most commands take a resource ID that identifies which object to operate on:

| Prefix | Resource                                                     | Returned by                                        |
| ------ | ------------------------------------------------------------ | -------------------------------------------------- |
| `ep_`  | Endpoint.                                                    | `tg beta endpoints deploy`, `tg beta endpoints ls` |
| `dep_` | Deployment (a model plus config running behind an endpoint). | `tg beta endpoints get`                            |
| `abx_` | A/B experiment.                                              | `tg beta endpoints ab`                             |
| `exp_` | Shadow experiment.                                           | `tg beta endpoints shadow`                         |
