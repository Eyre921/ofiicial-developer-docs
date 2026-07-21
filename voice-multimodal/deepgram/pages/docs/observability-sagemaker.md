---
title: "Observability for Amazon SageMaker"
source: https://developers.deepgram.com/docs/observability-sagemaker.md
path: docs/observability-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Observability for Amazon SageMaker

> Use Amazon CloudWatch to monitor Deepgram SageMaker Endpoints. Covers key metrics like ConcurrentRequestsPerModel and FirstChunkLatency, enhanced per-instance metrics, CloudWatch Logs for Deepgram container output, and alarm configuration for proactive alerting.

Amazon SageMaker publishes endpoint metrics and container logs to Amazon CloudWatch automatically. This page explains which metrics matter most for Deepgram workloads, how to monitor latency for streaming and pre-recorded traffic, how to enable per-instance enhanced metrics, how to access Deepgram container logs, and how to configure alarms that alert you before performance degrades.

Two companion pages cover additional metric streams: [Prometheus & OpenTelemetry Metrics](/docs/prometheus-otel-sagemaker) for per-GPU, host, and container Prometheus metrics via SageMaker detailed observability, and [Deepgram Enhanced Metrics](/docs/enhanced-metrics-sagemaker) for the usage and billing metrics the Deepgram container publishes to CloudWatch on its own.

Before configuring observability, you must have a Deepgram SageMaker Endpoint deployed and running with status `InService`. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) for setup instructions.

## CloudWatch metrics

SageMaker publishes metrics to two CloudWatch namespaces. The metrics most relevant to Deepgram streaming workloads are listed below.

### Invocation metrics (`AWS/SageMaker`)

These metrics track request-level behavior for your endpoint variant.

| Metric                       | Description                                                                                                                                                                | Relevance to Deepgram                                                                                                                                                                    |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConcurrentRequestsPerModel` | Number of in-flight requests per instance, including queued requests. Emitted every 10 seconds (high-resolution).                                                          | **Primary metric for Deepgram streaming.** Each bidirectional streaming connection holds GPU resources for its entire duration. This metric directly reflects the load on each instance. |
| `Invocations`                | Total number of requests sent to the endpoint. Each streaming session counts as one invocation, as does each pre-recorded request.                                         | Useful for tracking overall request volume and correlating with billing.                                                                                                                 |
| `InvocationsPerInstance`     | Invocations normalized by instance count. Emitted every minute.                                                                                                            | Secondary throughput indicator. Less useful for streaming workloads than `ConcurrentRequestsPerModel` because it counts completed invocations, not active connections.                   |
| `ModelLatency`               | Time taken by the Deepgram container to process a pre-recorded request sent through `InvokeEndpoint` and return the response. Units: microseconds.                         | Tracks inference latency for pre-recorded requests. **Not emitted for streaming sessions** — use `FirstChunkLatency` for streaming latency.                                              |
| `OverheadLatency`            | Time added by SageMaker infrastructure (request routing, response serialization) outside the model container, measured for `InvokeEndpoint` requests. Units: microseconds. | High values indicate SageMaker platform overhead rather than Deepgram processing delays. Only meaningful for pre-recorded requests.                                                      |
| `FirstChunkLatency`          | Time from the start of a streaming session until the first response chunk is sent back to the client. One sample per session. Units: microseconds.                         | **Primary latency metric for Deepgram streaming.** Measures how quickly a new streaming connection becomes productive. See [Monitor latency](#monitor-latency).                          |
| `MidStreamErrors`            | Errors that occur after a response has started streaming. Only populated when mid-stream failures occur.                                                                   | Catches failures on established streaming sessions, which otherwise surface only in container logs.                                                                                      |
| `Invocation4XXErrors`        | Count of requests that returned a 4xx HTTP status.                                                                                                                         | Indicates client-side issues such as malformed requests or unsupported parameters.                                                                                                       |
| `Invocation5XXErrors`        | Count of requests that returned a 5xx HTTP status.                                                                                                                         | Indicates server-side failures. Spikes may signal container crashes, out-of-memory errors, or GPU issues.                                                                                |
| `InvocationModelErrors`      | Count of requests that did not result in a 2xx response, including timeouts and malformed responses.                                                                       | Broader error metric that captures both 4xx and 5xx errors plus low-level failures.                                                                                                      |

Dimensions for invocation metrics: `EndpointName`, `VariantName`. Invocation metrics publish at 1-minute granularity, except `ConcurrentRequestsPerModel`, which publishes every 10 seconds. Each streaming session also publishes one sample to the error metrics (`0` on success), so error-rate alarms cover streaming and pre-recorded traffic alike.

### Endpoint instance metrics (`/aws/sagemaker/Endpoints`)

These metrics track resource utilization on the EC2 instances backing your endpoint.

| Metric                 | Description                                                                  | Relevance to Deepgram                                                                                                              |
| ---------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `CPUUtilization`       | Sum of utilization across all CPU cores. Range: 0%–(100% × number of cores). | Deepgram is primarily GPU-bound, but high CPU utilization can indicate bottlenecks in audio preprocessing or API request handling. |
| `GPUUtilization`       | Sum of utilization across all GPUs. Range: 0%–(100% × number of GPUs).       | **Key resource metric.** Deepgram inference runs on GPU. Sustained values near maximum indicate the instance is at capacity.       |
| `GPUMemoryUtilization` | Percentage of GPU memory in use, summed across GPUs.                         | High GPU memory utilization can preclude loading additional models or serving more concurrent streams.                             |
| `MemoryUtilization`    | Percentage of system RAM in use.                                             | Monitor to detect memory leaks or insufficient instance sizing.                                                                    |
| `DiskUtilization`      | Percentage of disk space in use.                                             | Models and logs consume disk. Alert if utilization approaches capacity.                                                            |

Dimensions for endpoint instance metrics: `EndpointName`, `VariantName`. With [enhanced metrics](#enable-enhanced-metrics) enabled, per-instance and per-GPU variants of these metrics become available.

### Focused: `ConcurrentRequestsPerModel`

For Deepgram streaming workloads, `ConcurrentRequestsPerModel` is the most important metric. It reflects the actual concurrency load because Deepgram uses long-lived bidirectional streaming connections where each connection holds GPU resources for the entire session.

Key characteristics:

* **High-resolution**: Emitted every 10 seconds, making it up to 6x faster than standard 1-minute metrics at detecting load changes.
* **Includes queued requests**: The count includes requests waiting in the SageMaker queue, not just those actively being processed.
* **Directly maps to capacity**: Each instance supports a finite number of concurrent streams at acceptable latency. See [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker-streaming#choose-a-target-value) for guidance on determining the right concurrency limit for your instance type.

To query this metric with the AWS CLI:

```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/SageMaker \
  --metric-name ConcurrentRequestsPerModel \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
               Name=VariantName,Value=AllTraffic \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 60 \
  --statistics Maximum \
  --region YOUR_AWS_REGION
```

AWS documents `Min` and `Max` as the valid statistics for `ConcurrentRequestsPerModel` — use `Maximum` for capacity monitoring and alarms. Set `--period 10` to see the full 10-second resolution.

## Monitor latency

Total request latency has three components: network latency (client ↔ SageMaker runtime, not visible in CloudWatch — measure it client-side), `OverheadLatency` (SageMaker routing and platform processing), and `ModelLatency` (processing time inside the Deepgram container).

All SageMaker latency metrics are reported in **microseconds**: a 2-second threshold is `2000000`.

### Pre-recorded requests

`ModelLatency` and `OverheadLatency` are emitted once per `InvokeEndpoint` request. Use percentile statistics rather than averages — averages hide tail latency. `ModelLatency` scales with the duration of the submitted audio, so tune thresholds against your own traffic baseline:

```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/SageMaker \
  --metric-name ModelLatency \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
               Name=VariantName,Value=AllTraffic \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 60 \
  --extended-statistics p50 p95 p99 \
  --region YOUR_AWS_REGION
```

### Streaming sessions

`ModelLatency` is not emitted for streaming sessions, and `OverheadLatency` carries no useful signal for them. Monitor `FirstChunkLatency` instead: it records one sample per session, measuring the time from session start until the first response chunk reaches the client — how quickly a new connection becomes productive. It supports percentile statistics, so alert on `p99` (see [Streaming latency alarm](#streaming-latency-alarm)).

`MidStreamErrors` counts errors that occur after a response has started streaming. It is only populated when mid-stream failures occur — on a healthy endpoint this metric may not appear in CloudWatch at all.

## Enable enhanced metrics

By default, SageMaker reports utilization metrics aggregated across all instances behind the endpoint. Because Deepgram streaming connections are long-lived and remain on the instance that accepted them, load is not always spread evenly — an endpoint-level average can look healthy while one instance or GPU is saturated.

Enhanced metrics add per-instance and per-GPU utilization visibility, the same way per-instance Log Streams isolate logs:

* `CPUUtilizationNormalized` and `MemoryUtilization` gain an `InstanceId` dimension.
* `GPUUtilizationNormalized` and `GPUMemoryUtilizationNormalized` gain `InstanceId` and per-GPU `GpuId` dimensions.
* The `*Normalized` variants report 0–100% regardless of core or GPU count, unlike their summed counterparts.
* Utilization metrics publish at a configurable interval: 10, 30, 60 (default), 120, 180, 240, or 300 seconds.

Enhanced metrics are enabled with `MetricsConfig` on the endpoint configuration:

#### AWS CLI

```bash
aws sagemaker create-endpoint-config \
  --endpoint-config-name YOUR_CONFIG_NAME \
  --production-variants file://production-variants.json \
  --metrics-config '{"EnableEnhancedMetrics": true, "MetricPublishFrequencyInSeconds": 10}' \
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
        "EnableEnhancedMetrics": True,
        "MetricPublishFrequencyInSeconds": 10,
    },
)
```

To enable enhanced metrics on an endpoint that is already serving traffic, create a new endpoint configuration with the same production variants plus `MetricsConfig`, then update the endpoint. The update runs as a blue/green deployment (typically several minutes) and the endpoint stays `InService` throughout; the new metrics appear once it completes. See [Update an Amazon SageMaker Endpoint](/docs/update-amazon-sagemaker-endpoint) for how rollouts interact with long-lived streaming sessions.

```bash
aws sagemaker update-endpoint \
  --endpoint-name YOUR_ENDPOINT_NAME \
  --endpoint-config-name YOUR_CONFIG_NAME \
  --region YOUR_AWS_REGION

aws sagemaker describe-endpoint \
  --endpoint-name YOUR_ENDPOINT_NAME \
  --query 'MetricsConfig' \
  --region YOUR_AWS_REGION
```

After the deployment completes and traffic arrives, list the per-instance and per-GPU metric streams:

```bash
aws cloudwatch list-metrics \
  --namespace /aws/sagemaker/Endpoints \
  --metric-name GPUUtilizationNormalized \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
  --region YOUR_AWS_REGION
```

Metrics published at intervals below 60 seconds are high-resolution and are retained by CloudWatch for only 3 hours. CloudWatch bills utilization metrics per metric stream, and per-instance and per-GPU dimensions add streams as the endpoint scales out. See [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## CloudWatch Logs

SageMaker streams container output to Amazon CloudWatch Logs automatically. Deepgram server logs — including startup messages, inference activity, configuration application, and error details — appear in these log streams.

### Log Group and Log Streams

Each SageMaker Endpoint writes to a CloudWatch Log Group named:

```
/aws/sagemaker/Endpoints/YOUR_ENDPOINT_NAME
```

Within the Log Group, SageMaker creates **one Log Stream per EC2 instance** backing the endpoint. If auto-scaling adds instances, new Log Streams appear automatically. The Log Stream name includes the variant name and instance identifier, following the pattern:

```
AllTraffic/i-0123456789abcdef0
```

This per-instance separation lets you isolate issues to a specific instance when diagnosing problems across a scaled-out fleet.

### View logs in the console

#### Open the SageMaker console

Navigate to the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/home) and select **Endpoints** from the left menu.

#### Select your endpoint

Click the endpoint name to open its details page.

#### Open CloudWatch Logs

Under **Monitor**, click the **View logs** link. This opens the CloudWatch Log Group for the endpoint.

#### Select a Log Stream

Choose a Log Stream corresponding to the instance you want to inspect. Each stream contains the full Deepgram container output for that instance.

### View logs with the AWS CLI

Stream logs in near-real-time using the CloudWatch Logs [Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) feature:

```bash
aws logs tail --follow \
  /aws/sagemaker/Endpoints/YOUR_ENDPOINT_NAME \
  --region YOUR_AWS_REGION
```

To filter for a specific Log Stream (a specific instance):

```bash
aws logs tail --follow \
  /aws/sagemaker/Endpoints/YOUR_ENDPOINT_NAME \
  --log-stream-name-prefix AllTraffic/ \
  --region YOUR_AWS_REGION
```

To search recent logs for errors:

```bash
aws logs filter-log-events \
  --log-group-name /aws/sagemaker/Endpoints/YOUR_ENDPOINT_NAME \
  --filter-pattern "ERROR" \
  --start-time $(date -u -d '1 hour ago' +%s000) \
  --region YOUR_AWS_REGION
```

### What to look for in Deepgram logs

| Log pattern                                         | Meaning                                                                                                                                                        |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `INFO Starting Deepgram SageMaker configuration...` | Container is applying environment variable overrides. See [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments).                     |
| `INFO Configuration complete.`                      | Environment variables were applied successfully.                                                                                                               |
| `INFO Deepgram Engine is ready`                     | The inference engine has loaded models and is accepting requests.                                                                                              |
| `ERROR`                                             | An error occurred. Check the message for details — common causes include GPU initialization failures, model loading errors, or out-of-memory conditions.       |
| `thread 'main' panicked at`                         | A Rust-level application panic. The container process has crashed and the instance will restart. Capture the full backtrace from the log stream for diagnosis. |
| `WARNING` entries with `skipped`                    | An environment variable override was not applied, usually due to a parse error in the TOML expression.                                                         |

## Configure CloudWatch alarms

CloudWatch alarms monitor a metric and trigger notifications or actions when the metric crosses a threshold. Use alarms to detect capacity issues, error spikes, and infrastructure problems before they affect users.

### Recommended alarms

The following alarms cover the most critical failure and capacity scenarios for Deepgram on SageMaker.

#### High concurrency alarm

Alert when concurrent streams approach the capacity limit of your instances. Set the threshold to approximately 80–90% of the maximum concurrent streams your instance type can handle at acceptable latency.

#### AWS CLI

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name deepgram-high-concurrency \
  --namespace AWS/SageMaker \
  --metric-name ConcurrentRequestsPerModel \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
               Name=VariantName,Value=AllTraffic \
  --statistic Maximum \
  --period 60 \
  --evaluation-periods 3 \
  --threshold 80 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --alarm-actions arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC \
  --region YOUR_AWS_REGION
```

#### Python (boto3)

```python
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_alarm(
    AlarmName="deepgram-high-concurrency",
    Namespace="AWS/SageMaker",
    MetricName="ConcurrentRequestsPerModel",
    Dimensions=[
        {"Name": "EndpointName", "Value": "YOUR_ENDPOINT_NAME"},
        {"Name": "VariantName", "Value": "AllTraffic"},
    ],
    Statistic="Maximum",
    Period=60,
    EvaluationPeriods=3,
    Threshold=80,
    ComparisonOperator="GreaterThanOrEqualToThreshold",
    AlarmActions=[
        "arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC"
    ],
)
```

Adjust `Threshold` based on your benchmarking results. For example, if a `g5.2xlarge` instance handles 100 concurrent streams at acceptable latency, set the alarm threshold to `80`.

#### Error rate alarm

Alert when the endpoint returns errors. A sustained error rate indicates a container or model issue that needs investigation.

#### AWS CLI

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name deepgram-invocation-errors \
  --namespace AWS/SageMaker \
  --metric-name Invocation5XXErrors \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
               Name=VariantName,Value=AllTraffic \
  --statistic Sum \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 5 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --alarm-actions arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC \
  --region YOUR_AWS_REGION
```

#### Python (boto3)

```python
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_alarm(
    AlarmName="deepgram-invocation-errors",
    Namespace="AWS/SageMaker",
    MetricName="Invocation5XXErrors",
    Dimensions=[
        {"Name": "EndpointName", "Value": "YOUR_ENDPOINT_NAME"},
        {"Name": "VariantName", "Value": "AllTraffic"},
    ],
    Statistic="Sum",
    Period=300,
    EvaluationPeriods=2,
    Threshold=5,
    ComparisonOperator="GreaterThanOrEqualToThreshold",
    AlarmActions=[
        "arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC"
    ],
)
```

#### Streaming latency alarm

Alert when the time to first response on new streaming sessions degrades. `FirstChunkLatency` supports percentiles — alarm on `p99` so a handful of slow session starts is caught without being averaged away. Baseline your endpoint first and set the threshold above the steady-state `p99` (in microseconds).

#### AWS CLI

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name deepgram-streaming-first-chunk-latency \
  --namespace AWS/SageMaker \
  --metric-name FirstChunkLatency \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
               Name=VariantName,Value=AllTraffic \
  --extended-statistic p99 \
  --period 60 \
  --evaluation-periods 3 \
  --threshold 5000000 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --treat-missing-data notBreaching \
  --alarm-actions arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC \
  --region YOUR_AWS_REGION
```

#### Python (boto3)

```python
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_alarm(
    AlarmName="deepgram-streaming-first-chunk-latency",
    Namespace="AWS/SageMaker",
    MetricName="FirstChunkLatency",
    Dimensions=[
        {"Name": "EndpointName", "Value": "YOUR_ENDPOINT_NAME"},
        {"Name": "VariantName", "Value": "AllTraffic"},
    ],
    ExtendedStatistic="p99",
    Period=60,
    EvaluationPeriods=3,
    Threshold=5000000,
    ComparisonOperator="GreaterThanOrEqualToThreshold",
    TreatMissingData="notBreaching",
    AlarmActions=[
        "arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC"
    ],
)
```

`FirstChunkLatency` only receives samples when new sessions start, so keep `--treat-missing-data notBreaching` to avoid alarming during idle periods. For pre-recorded endpoints, create the equivalent alarm on `ModelLatency` with `p95` or `p99`, and remember that its value scales with the duration of the submitted audio.

#### GPU utilization alarm

GPU utilization is not a primary metric for Deepgram workloads — `ConcurrentRequestsPerModel` is a more direct indicator of load. However, GPU utilization is still useful for gauging the general level of load that a particular GPU instance is under and for detecting hardware-level saturation.

#### AWS CLI

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name deepgram-high-gpu \
  --namespace /aws/sagemaker/Endpoints \
  --metric-name GPUUtilization \
  --dimensions Name=EndpointName,Value=YOUR_ENDPOINT_NAME \
               Name=VariantName,Value=AllTraffic \
  --statistic Average \
  --period 300 \
  --evaluation-periods 3 \
  --threshold 80 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --alarm-actions arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC \
  --region YOUR_AWS_REGION
```

#### Python (boto3)

```python
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_alarm(
    AlarmName="deepgram-high-gpu",
    Namespace="/aws/sagemaker/Endpoints",
    MetricName="GPUUtilization",
    Dimensions=[
        {"Name": "EndpointName", "Value": "YOUR_ENDPOINT_NAME"},
        {"Name": "VariantName", "Value": "AllTraffic"},
    ],
    Statistic="Average",
    Period=300,
    EvaluationPeriods=3,
    Threshold=80,
    ComparisonOperator="GreaterThanOrEqualToThreshold",
    AlarmActions=[
        "arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_SNS_TOPIC"
    ],
)
```

For instances with a single GPU (such as `g5.2xlarge`), `GPUUtilization` ranges from 0–100%. For multi-GPU instances, the range is 0%–(100% × number of GPUs). Adjust the threshold accordingly.

### Alarm actions

Each alarm example above sends a notification to an [Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/welcome.html). Create an SNS topic and subscribe your preferred notification channel (email, Slack via AWS Chatbot, PagerDuty, or a Lambda function) before configuring alarms.

```bash
aws sns create-topic --name deepgram-sagemaker-alerts --region YOUR_AWS_REGION
aws sns subscribe \
  --topic-arn arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:deepgram-sagemaker-alerts \
  --protocol email \
  --notification-endpoint your-team@example.com \
  --region YOUR_AWS_REGION
```

### View alarms

List active alarms for your endpoint:

```bash
aws cloudwatch describe-alarms \
  --alarm-name-prefix deepgram- \
  --region YOUR_AWS_REGION
```

You can also view alarms in the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home) under **Alarms** → **All alarms**.

## Build a CloudWatch dashboard

Combine the key metrics into a single dashboard for at-a-glance monitoring. The following AWS CLI command creates a dashboard with widgets for concurrency, GPU utilization, errors, and latency.

```bash title="Create a CloudWatch dashboard"
aws cloudwatch put-dashboard \
  --dashboard-name deepgram-sagemaker \
  --dashboard-body '{
    "widgets": [
      {
        "type": "metric",
        "properties": {
          "title": "Concurrent Requests Per Model",
          "metrics": [
            ["AWS/SageMaker", "ConcurrentRequestsPerModel",
             "EndpointName", "YOUR_ENDPOINT_NAME",
             "VariantName", "AllTraffic"]
          ],
          "period": 60,
          "stat": "Maximum",
          "region": "YOUR_AWS_REGION"
        }
      },
      {
        "type": "metric",
        "properties": {
          "title": "GPU Utilization",
          "metrics": [
            ["/aws/sagemaker/Endpoints", "GPUUtilization",
             "EndpointName", "YOUR_ENDPOINT_NAME",
             "VariantName", "AllTraffic"]
          ],
          "period": 300,
          "stat": "Average",
          "region": "YOUR_AWS_REGION"
        }
      },
      {
        "type": "metric",
        "properties": {
          "title": "Invocation Errors (5xx)",
          "metrics": [
            ["AWS/SageMaker", "Invocation5XXErrors",
             "EndpointName", "YOUR_ENDPOINT_NAME",
             "VariantName", "AllTraffic"]
          ],
          "period": 300,
          "stat": "Sum",
          "region": "YOUR_AWS_REGION"
        }
      },
      {
        "type": "metric",
        "properties": {
          "title": "First Chunk Latency p99 (streaming, microseconds)",
          "metrics": [
            ["AWS/SageMaker", "FirstChunkLatency",
             "EndpointName", "YOUR_ENDPOINT_NAME",
             "VariantName", "AllTraffic"]
          ],
          "period": 60,
          "stat": "p99",
          "region": "YOUR_AWS_REGION"
        }
      },
      {
        "type": "metric",
        "properties": {
          "title": "Model Latency p99 (pre-recorded only, microseconds)",
          "metrics": [
            ["AWS/SageMaker", "ModelLatency",
             "EndpointName", "YOUR_ENDPOINT_NAME",
             "VariantName", "AllTraffic"]
          ],
          "period": 60,
          "stat": "p99",
          "region": "YOUR_AWS_REGION"
        }
      }
    ]
  }' \
  --region YOUR_AWS_REGION
```

After creating the dashboard, view it in the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home) under **Dashboards**.

***

## Related resources

* [Prometheus & OpenTelemetry Metrics](/docs/prometheus-otel-sagemaker)
* [Deepgram Enhanced Metrics](/docs/enhanced-metrics-sagemaker)
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker-streaming)
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)
* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Amazon SageMaker AI metrics in Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
* [Amazon SageMaker AI enhanced metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch-enhanced-metrics.html)
* [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
