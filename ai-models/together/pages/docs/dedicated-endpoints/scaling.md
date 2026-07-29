---
title: "Configure autoscaling"
source: https://docs.together.ai/docs/dedicated-endpoints/scaling
path: docs/dedicated-endpoints/scaling
---

Autoscale a deployment between replica bounds, pick the right scaling metric, and understand the cost tradeoff.

Configure your deployment to scale automatically by setting limits on how many replicas it can run. You set the minimum and maximum replica count, and the platform autoscales between those bounds based on a metric that you choose.

## Replica bounds

A replica is one instance of your model running on its own hardware. Adding more replicas raises the aggregate requests per second that a deployment can serve, and which also adds redundancy in case a single replica fails.

Two parameters control the number of replicas that a deployment can run:

* **`minReplicas`:** The floor. The deployment never scales below this. On a running deployment, it must be at least `1`.
* **`maxReplicas`:** The ceiling. Caps how far the deployment scales up, which determines the deployment's maximum cost.

You can set both at [creation time](/docs/dedicated-endpoints/manage#create-a-deployment) with the CLI's `tg beta endpoints deploy --min-replicas`/`--max-replicas`. To update the bounds on a running deployment, pass the deployment ID (`dep_...`) to `tg beta endpoints update`; the CLI resolves its parent endpoint automatically:

```bash CLI theme={null}
tg beta endpoints update dep_abc123 \
  --min-replicas 1 \
  --max-replicas 4
```

Setting `minReplicas` equal to `maxReplicas` fixes the size of the deployment and disables autoscaling. Setting both to `0` stops the deployment. A `minReplicas` of `0` paired with a positive `maxReplicas` is rejected.

## Enable autoscaling

To enable autoscaling, set `minReplicas` to less than `maxReplicas`. With a range set but no metric specified, the platform applies a default scaling metric (concurrent in-flight requests per replica), so you can enable autoscaling without first choosing a metric or target.

To scale on a specific metric, pass `--scaling-metric` and `--scaling-target` together. A deployment scales on a single metric, so you set exactly one. Choose the metric when you first deploy:

```bash CLI theme={null}
tg beta endpoints deploy zai-org/GLM-5.2 \
  --endpoint my-glm-endpoint \
  --min-replicas 1 \
  --max-replicas 4 \
  --scaling-metric gpu_utilization \
  --scaling-target 70
```

You can also set or change the metric later on a running deployment. Pass the deployment ID (`dep_...`); the CLI resolves its parent endpoint automatically. With the Python SDK, use snake\_case field names and set the metric target `type` explicitly:

<CodeGroup>
  ```bash CLI theme={null}
  tg beta endpoints update dep_abc123 \
    --min-replicas 1 \
    --max-replicas 4 \
    --scaling-metric gpu_utilization \
    --scaling-target 70
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()
  project_id = client.whoami().project_id

  deployment = client.beta.endpoints.deployments.update(
      "dep_abc123",
      project_id=project_id,
      endpoint_id="ep_abc123",
      autoscaling={
          "min_replicas": 1,
          "max_replicas": 4,
          "scaling_metrics": [
              {
                  "name": "gpu_utilization",
                  "target": 70,
                  "type": "METRIC_TARGET_TYPE_UTILIZATION",
              }
          ],
      },
  )
  ```
</CodeGroup>

The SDK converts the snake\_case fields above to the API's camelCase fields. You can pass the same `autoscaling` object to `client.beta.endpoints.deployments.create`. For create requests, `model` and `config` must be fully qualified resource names, such as `projects/{project_id}/models/{model_id}` and `projects/{project_id}/configs/{config_id}`. See the [create deployment](/reference/dmi/deployments-create) and [update deployment](/reference/dmi/deployments-update) API references.

## Scaling metrics

`--scaling-metric` accepts one of eight metrics, and `--scaling-target` sets the threshold the platform holds it near. The unit of the target depends on the metric:

| Metric (`--scaling-metric`) | What `--scaling-target` sets                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `inflight_requests`         | Concurrent in-flight requests per replica. The default metric; the target is `8` when no metric is specified. |
| `gpu_utilization`           | GPU compute utilization, as a percentage (`0`–`100`).                                                         |
| `token_utilization`         | KV-cache utilization, as a percentage (`0`–`100`).                                                            |
| `cache_hit_rate`            | Prompt-cache hit rate, as a percentage (`0`–`100`).                                                           |
| `throughput_per_replica`    | Tokens generated per second, per replica.                                                                     |
| `ttft`                      | Time to first token, in milliseconds.                                                                         |
| `decoding_speed`            | Time per output token, in milliseconds.                                                                       |
| `e2e_latency`               | End-to-end request latency, in milliseconds.                                                                  |

The target is interpreted in one of three ways, depending on the metric:

* **Utilization** (`gpu_utilization`, `token_utilization`, `cache_hit_rate`): an average percentage across all replicas, from `0` to `100`. `gpu_utilization` with `--scaling-target 70` holds GPU utilization near 70%.
* **Average value** (`inflight_requests`, `throughput_per_replica`): an average value across all replicas. `inflight_requests` with `--scaling-target 16` aims for about 16 concurrent requests per replica.
* **Absolute value** (`ttft`, `decoding_speed`, `e2e_latency`): a value across the whole deployment, measured at a percentile. `e2e_latency` with `--scaling-target 2000` targets a p95 of 2000 ms (2 seconds). [See below](#how-latency-is-calculated) for details.

<Warning>
  The per-token metrics `throughput_per_replica`, `ttft`, and `decoding_speed` are recorded only for streaming responses. When scaling on one of these metrics, make sure to send [streaming requests](/docs/inference/chat/overview#stream-responses) (`"stream": true`), or the deployment won't scale correctly. (`e2e_latency` is the exception: it's measured for both streaming and non-streaming traffic.)
</Warning>

### Choose a metric

The eight metrics fall into three families. Which one fits depends on what you want to protect the deployment against.

* **Concurrency-driven (`inflight_requests`) is the safe default.** In-flight count is a *leading* indicator: it rises when demand outpaces service, but before latency visibly degrades. It needs no streaming and no percentile choice, and it maps directly onto how inference engines batch requests. A target of `8` says "hold each replica at about eight concurrent requests." Raise it for short-prompt chat workloads that batch well, and lower it for long-context traffic (like coding agents) that spends longer in prefill.
* **SLO-driven (`ttft`, `e2e_latency`, `decoding_speed`) scale on the promise you make to users.** If your contract is "first token in under a second," scaling on `ttft` targets exactly that. Latency is a *trailing* signal: by the time p95 breaches the target, users can already notice it, so pair a latency metric with honest headroom in `minReplicas` rather than letting the deployment scale from a cold floor.
* **Efficiency-driven (`gpu_utilization`, `token_utilization`, `throughput_per_replica`, `cache_hit_rate`) put cost first.** They keep replicas busy and add capacity only when the fleet is genuinely saturated. Understand what "utilized" means for your workload before you rely on them: a GPU can be busy without the workload being latency-healthy, and a utilization target near `100` leaves no headroom for arrival bursts. When you scale on one of these, watch your p95 latency in [monitoring](/docs/dedicated-endpoints/monitoring).

Use this as a quick reference when picking a metric:

| Metric (`name`)          | Good to use when                                             |
| ------------------------ | ------------------------------------------------------------ |
| `inflight_requests`      | Default choice. Robust, leading, and engine-agnostic.        |
| `ttft`                   | You have a latency SLO on responsiveness (first-token time). |
| `e2e_latency`            | You have an SLO on total request-completion time.            |
| `gpu_utilization`        | Cost-first workloads that tolerate some latency variance.    |
| `token_utilization`      | Batch or throughput workloads running near engine limits.    |
| `throughput_per_replica` | Sustained-generation pipelines.                              |
| `decoding_speed`         | Guarding per-request generation speed for each user.         |
| `cache_hit_rate`         | Specialist: cache-heavy serving patterns.                    |

When the metric rises above the target, the platform raises `desiredReplicas` and new replicas [cold-start](/docs/dedicated-endpoints/concepts#cold-starts). When load falls, it scales back down after a [stabilization window](#scaling-rate-and-timing). Track progress by polling the deployment: `desiredReplicas` reflects the decision immediately, `status.scheduledReplicas` shows how many replicas the scheduler has placed, and `status.readyReplicas` catches up once cold start finishes.

<Note>
  When you test autoscaling, measure the change in `desiredReplicas` as scaling-decision latency and the change in `status.readyReplicas` as usable-capacity latency. Sustain the test load through the expected cold-start period. A short spike can raise `desiredReplicas` and then subside before a new replica becomes ready, so it demonstrates a scaling decision but not completed scale-up.
</Note>

### How latency is calculated

To calculate the overall latency of a deployment, the platform looks at a percentile of the request latency over each measurement window and scales replicas to keep the metric near your target.

The default is the 95th percentile (`p95`), meaning that 95% of requests should come in at or below your target, allowing only the slowest 5% of requests to run longer. To track a different point in the distribution, add `--scaling-percentile` with `p50`, `p90`, `p95`, or `p99`:

```bash CLI theme={null}
tg beta endpoints update dep_abc123 \
  --scaling-metric e2e_latency \
  --scaling-target 2000 \
  --scaling-percentile p90
```

`--scaling-percentile` applies only to the latency metrics (`ttft`, `decoding_speed`, and `e2e_latency`); the platform ignores it for other metrics.

## Scaling rate and timing

After the platform computes how many replicas a deployment needs from your metric and target, two layers shape how quickly the replica count can change.

**Stabilization windows** control how long the metric must stay above or below your target before the platform acts. Pass `--scale-up-window` and `--scale-down-window` on [`deploy`](/reference/cli/endpoints-beta#deploy) or [`update`](/reference/cli/endpoints-beta#update) to override them. When omitted, scale-up has no stabilization delay (`0` seconds), and scale-down waits five minutes before removing replicas.

**Rate limits** cap how many replicas can be added or removed per evaluation. DE 2.0 applies fleet defaults that you cannot override through the public API:

| Direction  | Rate limit                                   | Period     |
| ---------- | -------------------------------------------- | ---------- |
| Scale up   | The smaller of a 100% increase or 4 replicas | 15 seconds |
| Scale down | The smaller of a 25% decrease or 1 replica   | 60 seconds |

The platform evaluates scaling roughly every 60 seconds. Each evaluation applies the stabilization windows first, then clamps the replica delta to these rate limits, then clamps the result to your [replica bounds](#replica-bounds). A deployment at zero replicas stays at zero until you raise its floor above zero.

## Release hardware

A deployment runs until you stop it. To release the hardware, stop the deployment or lower its [replica bounds](#replica-bounds) to zero (set both `minReplicas` and `maxReplicas` to `0`). A stopped deployment doesn't restart on its own. To bring it back, raise both bounds to `1` or more. See [Stop a deployment](/docs/dedicated-endpoints/manage#stop-a-deployment).

## Next steps

<CardGroup>
  <Card title="Observability" icon="chart-line" href="/docs/dedicated-endpoints/monitoring">
    Query the metrics that drive autoscaling decisions.
  </Card>

  <Card title="Pricing" icon="cash" href="/docs/dedicated-endpoints/pricing#how-scaling-affects-cost">
    See how replica count maps to cost.
  </Card>
</CardGroup>
