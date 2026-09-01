---
title: "Prometheus & OpenTelemetry Metrics"
source: https://developers.deepgram.com/docs/prometheus-otel-sagemaker.md
path: docs/prometheus-otel-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Prometheus & OpenTelemetry Metrics

> Enable Amazon SageMaker detailed observability on Deepgram Endpoints to collect per-GPU, host, and container Prometheus metrics through an AWS-managed OpenTelemetry Collector, and query them with PromQL from CloudWatch or Prometheus-compatible observability tools.

Amazon SageMaker **detailed observability** runs an AWS-managed [OpenTelemetry (OTel) Collector](https://opentelemetry.io/docs/collector/) on every instance backing your endpoint. The collector gathers per-GPU accelerator metrics, host-level system metrics, and Prometheus metrics scraped from the model container, and exports them to CloudWatch, where you query them with [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/). This gives you finer-grained visibility than the standard CloudWatch metrics covered in [Observability for Amazon SageMaker](/docs/observability-sagemaker) — including per-GPU utilization on multi-GPU instances and metrics emitted directly by the Deepgram engine.

This page covers turning the feature on and querying the results for Deepgram workloads. For full setup details — including account prerequisites, IAM permissions, and connecting third-party observability tools — see the AWS documentation: [Detailed observability for SageMaker AI endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch-detailed-observability.html). For the standard endpoint metrics available without this feature, see [Observability for Amazon SageMaker](/docs/observability-sagemaker).

## What you get

With detailed observability enabled, three metric sources publish to CloudWatch's OTel-compatible metric store:

| Source                   | Example metrics                                                                                                           | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPU (DCGM exporter)**  | `DCGM_FI_DEV_GPU_UTIL`, `DCGM_FI_DEV_FB_USED`, `DCGM_FI_DEV_MEM_COPY_UTIL`                                                | Per-GPU series. On multi-GPU instance types (for example Aura-2 deployments on `ml.g6.12xlarge`), each GPU reports separately — no more summed or averaged utilization hiding a saturated device.                                                                                                                                                                                                                                                                                                                                                             |
| **Host (node exporter)** | `node_cpu_seconds_total`, `node_memory_MemTotal_bytes`, `node_disk_io_time_seconds_total`                                 | Standard Prometheus node-exporter metrics for the instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Deepgram container**   | `engine_active_requests{kind="stream"}`, `engine_estimated_stream_capacity`, `sagemaker_endpoint_health{state="healthy"}` | The collector scrapes the container's Prometheus endpoint on port 8080 at `/metrics`. The `api_` and `engine_` families are the same metrics documented in the self-hosted [Metrics Guide](/docs/metrics-guide). `sagemaker_endpoint_health` is specific to SageMaker deployments — see [Read health as a metric](/docs/health-checks-sagemaker#read-health-as-a-metric). Requires a Deepgram container version that serves this endpoint; GPU and host metrics work with every version because they are collected by AWS on the host, outside the container. |

Every series carries SageMaker resource labels, including `aws.sagemaker.endpoint.name`, the variant name, and the instance ID, so you can filter and group across a scaled-out fleet.

These metrics work with AWS Marketplace deployments: the collector runs on the host, outside the model container, so it is unaffected by the network isolation that Marketplace model packages require.

## Enable detailed observability

Detailed observability is **on by default for newly created endpoints**, publishing every 60 seconds — no configuration is needed to start using it on a new deployment.

To set it explicitly — for example to change the publish frequency, or to add it to an endpoint created before the feature launched — use `MetricsConfig` on the endpoint configuration, the same field used for [enhanced metrics](/docs/observability-sagemaker#enable-enhanced-metrics). The publish frequency accepts 10, 30, 60 (default), 120, 180, 240, or 300 seconds.

#### AWS CLI

```bash
aws sagemaker create-endpoint-config \
  --endpoint-config-name YOUR_CONFIG_NAME \
  --production-variants file://production-variants.json \
  --metrics-config '{"EnableDetailedObservability": true, "MetricPublishFrequencyInSeconds": 60}' \
  --region YOUR_AWS_REGION
```

#### Python (boto3)

```python
import boto3

sagemaker = boto3.client("sagemaker")

sagemaker.create_endpoint_config(
    EndpointConfigName="YOUR_CONFIG_NAME",
    ProductionVariants=[...],  # same variants as your existing config
    MetricsConfig={
        "EnableDetailedObservability": True,
        "MetricPublishFrequencyInSeconds": 60,
    },
)
```

To change the setting on an endpoint that is already serving traffic — including opting out with `"EnableDetailedObservability": false` — create a new endpoint configuration with the same production variants plus `MetricsConfig`, then run `update-endpoint`. The update is a blue/green deployment and the endpoint stays `InService`; see [Update an Amazon SageMaker Endpoint](/docs/update-amazon-sagemaker-endpoint).

* `EnableDetailedObservability` requires a recent AWS SDK — botocore/boto3 `1.43.49` or later, or an equally recent AWS CLI. Older clients reject the parameter.
* The feature has account-level prerequisites (CloudWatch OTel-enriched metrics must be active in the account). Follow the [AWS getting-started guide](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-detailed-observability-getting-started.html) to enable them.

## Query with PromQL

The metrics land in CloudWatch's OTel metric store, which is queried with PromQL rather than the classic `get-metric-statistics` API.

### CloudWatch console

In the CloudWatch console, open **Metrics** and use the PromQL query editor to explore the new series. Start by listing what a busy endpoint reports:

```promql
DCGM_FI_DEV_GPU_UTIL
```

Then filter to one endpoint. The SageMaker resource labels use OTel dotted names, so quote them in PromQL:

```promql
DCGM_FI_DEV_GPU_UTIL{"aws.sagemaker.endpoint.name"="YOUR_ENDPOINT_NAME"}
```

Substituting underscores for the dots — `aws_sagemaker_endpoint_name` — is valid PromQL that matches no series. The query succeeds and returns an empty result rather than an error, which is easy to misread as the metric not being published. Always quote the dotted label name.

### Prometheus-compatible HTTP API

CloudWatch exposes a standard Prometheus query API for these metrics at `https://monitoring.YOUR_AWS_REGION.amazonaws.com/api/v1/query`, authenticated with SigV4 (service name `monitoring`). Any tool that can sign requests works; for example with [awscurl](https://github.com/okigan/awscurl):

```bash
awscurl --service monitoring --region YOUR_AWS_REGION \
  "https://monitoring.YOUR_AWS_REGION.amazonaws.com/api/v1/query?query=DCGM_FI_DEV_GPU_UTIL"
```

The discovery endpoints work too — list every metric name the account is receiving:

```bash
awscurl --service monitoring --region YOUR_AWS_REGION \
  "https://monitoring.YOUR_AWS_REGION.amazonaws.com/api/v1/label/__name__/values"
```

Because the API is Prometheus-compatible, you can also point Grafana or other Prometheus-native observability tools at it. See the [AWS documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch-detailed-observability.html) for supported integrations.

* Detailed-observability metrics live in the OTel metric store only — they do not appear in `aws cloudwatch list-metrics` or the classic metric namespaces. Use PromQL to query them.
* `/metrics` always responds, even when the container's internal API and Engine metric sources are not yet reachable. In that case it serves the container's own health gauges alone, so a scrape during startup returns health rather than failing.

### Check endpoint health

`sagemaker_endpoint_health` reports the container's own view of whether it can serve inference. Exactly one `state` reports `1`:

```promql
sagemaker_endpoint_health{state="critical"}
```

A `1` means the container cannot recover without being replaced. Query the family without a `state` filter to see the current state across a fleet and read whichever series is `1`. See [Read health as a metric](/docs/health-checks-sagemaker#read-health-as-a-metric) for what each state means.

For earlier warning, `sagemaker_time_to_critical_seconds` counts down the seconds remaining before a container would enter `critical`. It reports `-1` when nothing is counting, so guard the comparison or the alarm fires on every healthy container:

```promql
sagemaker_time_to_critical_seconds >= 0 and sagemaker_time_to_critical_seconds < 120
```

See [Warning before a container is written off](/docs/health-checks-sagemaker#warning-before-a-container-is-written-off).

## Related resources

* [Observability for Amazon SageMaker](/docs/observability-sagemaker) — standard CloudWatch metrics, logs, and alarms
* [Metrics Guide](/docs/metrics-guide) — reference for the Deepgram API and Engine Prometheus metrics
* [Deepgram Enhanced Metrics](/docs/enhanced-metrics-sagemaker) — usage and billing metrics emitted by the Deepgram container
* [Detailed observability for SageMaker AI endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch-detailed-observability.html) (AWS)
* [Getting started with detailed observability](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-detailed-observability-getting-started.html) (AWS)
