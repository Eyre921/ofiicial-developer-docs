---
title: "Health Checks & Automatic Recovery"
source: https://developers.deepgram.com/docs/health-checks-sagemaker.md
path: docs/health-checks-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Health Checks & Automatic Recovery

> Understand the health check contract between Deepgram containers and Amazon SageMaker: what the container reports while models load and while it serves traffic, how SageMaker replaces unhealthy instances, the WebSocket ping/pong requirement for streaming connections, and the health-related log lines to look for in CloudWatch.

Amazon SageMaker polls a `/ping` endpoint on every instance backing your Endpoint. That response decides whether the instance receives inference requests, and whether SageMaker replaces it.

Deepgram containers report healthy only when they can actually serve inference — models loaded, inference path functional — rather than answering a static `200`. An instance that has failed to load its model reports that state instead of silently collecting requests it cannot serve.

For the platform side of this contract — request timeouts, the startup window, and replacement behavior — see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests) in the AWS documentation.

## While the container is starting

A Deepgram Endpoint downloads its model artifacts and loads them into GPU memory before serving anything. For larger bundles this takes several minutes. Throughout, `/ping` returns `503`, the Endpoint stays in `Creating`, and SageMaker routes no traffic. The container logs the reason at `INFO`:

```
/ping returning 503 — system still initializing (expected during container startup; not yet ready to serve)
```

Once the models load, `/ping` returns `200`, the Endpoint moves to `InService`, and SageMaker begins routing.

SageMaker allows a bounded window for a new instance to start passing health checks. Miss it and the instance launch fails, leaving the Endpoint in a failed state. Two fields on the production variant extend that window for a large bundle or a slow artifact download:

| Field                                         | Purpose                                                                |
| --------------------------------------------- | ---------------------------------------------------------------------- |
| `ModelDataDownloadTimeoutInSeconds`           | Time allowed to download model artifacts from Amazon S3.               |
| `ContainerStartupHealthCheckTimeoutInSeconds` | Time allowed for the container to begin passing `/ping` health checks. |

Both accept up to 3600 seconds. They are ceilings, not delays — raising them does not slow a healthy deployment.

## While the Endpoint is serving

SageMaker keeps polling `/ping` every few seconds. If the container reaches a state where it should not serve — the inference engine stops responding, for example — it reports unhealthy and refuses new requests, so callers get a fast error instead of a stalled one.

SageMaker then replaces the instance automatically. Replacement is not instantaneous: AWS requires a sustained failure signal, so a brief blip does not cycle your fleet.

## Read health as a metric

`/ping` is a yes/no signal consumed by SageMaker. The container also publishes the same health state as a Prometheus gauge, `sagemaker_endpoint_health`, so you can chart it and alarm on it. With [detailed observability](/docs/prometheus-otel-sagemaker) enabled, it reaches CloudWatch automatically.

All four series are always present. The current state reports `1`, the rest report `0`:

```
sagemaker_endpoint_health{state="healthy"} 1
sagemaker_endpoint_health{state="initializing"} 0
sagemaker_endpoint_health{state="degraded"} 0
sagemaker_endpoint_health{state="critical"} 0
```

| `state`        | Meaning                                                                                  | What to do                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `initializing` | Normal startup while models load. `/ping` returns `503` and SageMaker routes no traffic. | Nothing. Expect this on every new instance.                                                                                                               |
| `healthy`      | The container is serving inference.                                                      | Nothing.                                                                                                                                                  |
| `degraded`     | A recoverable fault. The container refuses new requests until it clears.                 | Watch it. A brief `degraded` that returns to `healthy` is self-recovery working as designed.                                                              |
| `critical`     | The container cannot recover on its own. Only replacement clears this state.             | SageMaker replaces the instance. If it recurs, contact your [Deepgram representative](https://deepgram.com/contact-us) with the Endpoint name and Region. |

Because every state is always emitted, an alarm on any one of them never reads "no data" while the container is running. A series that disappears entirely means the scrape failed — a different condition, worth alarming on separately.

The container emits this gauge itself, so `/metrics` answers even when the internal API and Engine metric sources are not yet reachable — during startup, for example. In that window the response carries the health gauge alone rather than failing the scrape.

## Streaming connections use a separate check

`/ping` reports instance health. Each bidirectional streaming connection has its own liveness check defined by the WebSocket protocol ([RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2)): SageMaker sends a Ping frame about once a minute, the container replies with a Pong, and several consecutive unanswered Pings close that connection.

The two are independent — a closed connection does not mean the instance is unhealthy, so client applications should reconnect on an unexpected close. See [Container Contract to Support Bidirectional Streaming Capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-bidi).

## Health-related log lines

These appear in the Endpoint's CloudWatch Log Group, `/aws/sagemaker/Endpoints/YOUR_ENDPOINT_NAME`. See [Observability for Amazon SageMaker](/docs/observability-sagemaker#cloudwatch-logs) for how to read and filter them.

| Log pattern                                       | Meaning                                                                                                                                                                                                    |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/ping returning 503 — system still initializing` | Logged at `INFO`. Normal during startup while models load. It stops once the container is ready.                                                                                                           |
| `INFO Deepgram Engine is ready`                   | The inference engine has loaded models and is accepting requests.                                                                                                                                          |
| `composite health check failed`                   | **Not expected in normal operation.** Contact your [Deepgram representative](https://deepgram.com/contact-us) to help troubleshoot. Include your Endpoint name, AWS Region, and the surrounding log lines. |

## When to take action

| What you observe                                                              | What to do                                                                                                                                                                                              |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint stays in `Creating`, then `Failed`                                   | Check the container logs — the reason is in the container output, not the SageMaker console error. If the container was still loading when the window expired, raise the two timeout fields above.      |
| An instance was replaced once and service recovered                           | Nothing. Automatic recovery worked.                                                                                                                                                                     |
| Instances are replaced repeatedly, or `composite health check failed` appears | Contact your [Deepgram representative](https://deepgram.com/contact-us) with the Endpoint name, Region, and log excerpts.                                                                               |
| `sagemaker_endpoint_health{state="critical"}` is `1`                          | The instance will not self-recover. Let SageMaker replace it. Contact your [Deepgram representative](https://deepgram.com/contact-us) if it recurs — a restart alone will not fix the underlying fault. |
| `sagemaker_endpoint_health{state="degraded"}` is `1` briefly, then `healthy`  | Nothing. Self-recovery worked.                                                                                                                                                                          |

To catch this before your users do, alarm on `Invocation5XXErrors` — see [Configure CloudWatch alarms](/docs/observability-sagemaker#configure-cloudwatch-alarms).

***

## Related resources

* [Observability for Amazon SageMaker](/docs/observability-sagemaker)
* [Prometheus & OpenTelemetry Metrics](/docs/prometheus-otel-sagemaker) — how to collect `sagemaker_endpoint_health` and query it with PromQL
* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Update an Amazon SageMaker Endpoint](/docs/update-amazon-sagemaker-endpoint)
* [Status Endpoint](/docs/self-hosted-status-endpoint) — the health states a Deepgram node reports, shared with self-hosted deployments
* [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests) (AWS)
* [Custom Inference Code with Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html) (AWS)
