---
title: "Monitor endpoints and deployments"
source: https://docs.together.ai/docs/dedicated-endpoints/monitoring
path: docs/dedicated-endpoints/monitoring
---

Monitor endpoint and deployment metrics with built-in dashboards and a Prometheus-compatible metrics endpoint.

Dedicated model inference records latency, throughput, and utilization metrics for every endpoint and deployment. These are the same series that drive [autoscaling](/docs/dedicated-endpoints/scaling#scaling-metrics).

## Analytics dashboard

The [Together AI console](https://api.together.ai/endpoints) shows per-endpoint charts for requests, tokens per second, input and output tokens, latency, and time to first token, built on the metric series below.

Open an endpoint and select the **Analytics** tab. Switch between **Usage** and **Errors**, view the endpoint **Total** or break it down **By deployment**, and adjust the time range. Use the dashboard to monitor an endpoint at a glance and to compare deployments during an [A/B test](/docs/dedicated-endpoints/ab-tests).

<Frame>
  <img alt="The Analytics tab for an endpoint in the Together AI console, with charts for requests, tokens per second, input tokens, and output tokens, plus Usage and Errors toggles, a Total and By deployment breakdown, and a time-range selector." />
</Frame>

The charts populate once the endpoint starts serving requests.

## Events

Each endpoint has an audit feed of events, newest first. It merges endpoint-scoped events with the deployment-scoped events for every deployment under the endpoint, so scale-ups, traffic shifts, readiness changes, and pauses across every deployment all surface here. Use it to trace what happened during an autoscaling event or a traffic-split change.

In the console, open an endpoint and select the **Logs** tab to browse the feed, with columns for time, type, source, level, and message.

<Frame>
  <img alt="The Logs tab for an endpoint in the Together AI console, an event feed with Time, Type, Source, Level, and Message columns showing the deployment's lifecycle events." />
</Frame>

To read the feed programmatically, use the SDK or API to list events:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  project_id = client.whoami().project_id

  events = client.beta.endpoints.list_events(
      "ep_abc123",
      project_id=project_id,
      limit=50,
  )
  print(events)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const client = new Together();
  const { project_id: projectId } = await client.whoami();

  const events = await client.beta.endpoints.listEvents('ep_abc123', {
    projectId,
    limit: 50,
  });
  console.log(events);
  ```
</CodeGroup>

Optional parameters narrow the feed:

* `types` restricts to specific event-type strings.
* `min_level` sets the minimum severity.
* `source_kinds` selects endpoint- or deployment-scoped events.
* `since` and `until` bound a time range.
* `subject_id` filters to a single subject.
* `deployment_ids` scopes to specific deployments.
* `limit` / `after` paginate (max `500`, default `50`).

<Note>
  Endpoint mutation events such as `endpoint.updated` record when a change happened, but they don't include a field-level diff. Keep configuration history in your deployment system if you need to reconstruct exactly what changed.
</Note>

### Deployment events

To follow a single deployment instead of the whole endpoint, pass its ID to the `deployment_ids` filter on the same events feed:

```python Python theme={null}
from together import Together

client = Together()
project_id = client.whoami().project_id

events = client.beta.endpoints.list_events(
    "ep_abc123",
    project_id=project_id,
    deployment_ids=["dep_abc123"],
    limit=50,
)
print(events)
```

## Prometheus-compatible metrics endpoint

<Note>
  The metrics endpoint is in beta. The host and path below are subject to change, and access may need to be enabled for your organization. Confirm availability with your Together AI contact before you build against it.
</Note>

Scrape real-time, per-organization performance metrics for your dedicated endpoints in standard Prometheus format. The endpoint works with any Prometheus-compatible scraper, including Prometheus, Grafana Agent, the Datadog OpenMetrics integration, and Vector.

### Authentication and URL

Metrics are served per organization at:

```text theme={null}
GET https://o11y-de2-metrics.cloud.together.ai/organizations/{org_id}/metrics
```

Authenticate with your API key as a bearer token. The endpoint is org-scoped by design, so it returns only your organization's data:

```bash Shell theme={null}
curl -H "Authorization: Bearer $TOGETHER_API_KEY" \
  "https://o11y-de2-metrics.cloud.together.ai/organizations/$ORG_ID/metrics"
```

### Prometheus scrape config

Point a Prometheus-compatible scraper at the endpoint:

```yaml theme={null}
scrape_configs:
  - job_name: together-endpoint-metrics
    scheme: https
    authorization:
      credentials: <TOGETHER_API_KEY>
    metrics_path: /organizations/<ORG_ID>/metrics
    static_configs:
      - targets: ["o11y-de2-metrics.cloud.together.ai"]
```

### Available metrics

Metrics are grouped by the stage of the request path they measure: the edge (front-door proxy), the router, and the worker (model server). Latency metrics are histograms, exposed as `_bucket`, `_sum`, and `_count` series; counters end in `_total`; gauges are point-in-time values.

#### Edge (front-door proxy)

| Metric                               | Type      | Unit         | Notes                                                            |
| ------------------------------------ | --------- | ------------ | ---------------------------------------------------------------- |
| `edge_inference_requests_total`      | Counter   | requests     | Broken down by `status_code`.                                    |
| `edge_inference_request_duration_ms` | Histogram | milliseconds | End-to-end request duration at the edge.                         |
| `edge_inference_ttft_ms`             | Histogram | milliseconds | Time to first token. Most meaningful with `is_streaming="true"`. |
| `edge_inference_inflight_requests`   | Gauge     | requests     | Concurrent in-flight requests at the edge.                       |

#### Router

| Metric                                      | Type      | Unit     | Notes                                                            |
| ------------------------------------------- | --------- | -------- | ---------------------------------------------------------------- |
| `router_inference_requests_total`           | Counter   | requests | Broken down by `status_code`.                                    |
| `router_inference_request_duration_seconds` | Histogram | seconds  | Request duration at the router.                                  |
| `router_inference_ttft_seconds`             | Histogram | seconds  | Time to first token.                                             |
| `router_pre_worker_duration_seconds`        | Histogram | seconds  | Routing and queue overhead before the worker.                    |
| `router_inference_inflight_requests`        | Gauge     | requests | Concurrent in-flight requests at the router.                     |
| `router_token_count`                        | Counter   | tokens   | Broken down by `token_type`, and by `requester_organization_id`. |
| `router_tokens_per_request`                 | Histogram | tokens   | Broken down by `token_type`.                                     |

#### Worker (model server)

| Metric                               | Type      | Unit        | Notes                                                                                    |
| ------------------------------------ | --------- | ----------- | ---------------------------------------------------------------------------------------- |
| `worker_inference_request_total`     | Counter   | requests    | Broken down by `status_code`.                                                            |
| `worker_ttft_seconds`                | Histogram | seconds     | Time to first token.                                                                     |
| `worker_generation_duration_seconds` | Histogram | seconds     | Total generation duration.                                                               |
| `worker_tpot_seconds`                | Histogram | seconds     | Time per output token (inter-token latency).                                             |
| `worker_token_total`                 | Counter   | tokens      | Broken down by `token_type`.                                                             |
| `worker_tokens_per_request`          | Histogram | tokens      | Broken down by `token_type`.                                                             |
| `worker_engine_kv_cache_utilization` | Gauge     | ratio (0-1) | Fraction of the engine's KV-cache capacity in use.                                       |
| `worker_engine_cache_hit_rate`       | Gauge     | ratio (0-1) | Hit rate of the engine's KV cache. Higher values mean more prefix reuse across requests. |

### Labels

Series carry labels that identify the resource and slice the data. Not every label appears on every metric.

| Label                                | Description                                               |
| ------------------------------------ | --------------------------------------------------------- |
| `owner_organization_id`              | Organization that owns the endpoint.                      |
| `owner_project_id`                   | Project that owns the endpoint.                           |
| `endpoint_id` / `endpoint_name`      | The endpoint.                                             |
| `deployment_id` / `deployment_name`  | The deployment.                                           |
| `deployment_service_id`              | Internal service identifier for the deployment.           |
| `model` (edge) / `model_id` (worker) | The served model.                                         |
| `deployment_region` (edge)           | Region the deployment runs in.                            |
| `edge_region` (edge)                 | Region of the edge proxy that served the request.         |
| `replica_id`                         | The specific replica.                                     |
| `status_code`                        | HTTP status code of the request.                          |
| `is_streaming`                       | Whether the request was streamed (`"true"` or `"false"`). |
| `token_type`                         | Token category (for example input or output).             |
| `path`                               | Request path.                                             |
| `requester_organization_id`          | Organization that made the request.                       |

## Next steps

<CardGroup>
  <Card title="Configure autoscaling" icon="arrows-maximize" href="/docs/dedicated-endpoints/scaling">
    Pick a metric to autoscale a deployment on.
  </Card>

  <Card title="Route traffic" icon="route" href="/docs/dedicated-endpoints/route-traffic">
    See how the endpoint routes requests across deployments.
  </Card>
</CardGroup>
