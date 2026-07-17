---
title: "Deepgram Enhanced Metrics"
source: https://developers.deepgram.com/docs/enhanced-metrics-sagemaker.md
path: docs/enhanced-metrics-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deepgram Enhanced Metrics

> Reference for the CloudWatch metrics Deepgram SageMaker containers emit via Embedded Metric Format: billing metrics in the Deepgram/SageMakerInference namespace and per-feature usage metrics in the Deepgram/SelfHosted namespace, with dimensions, units, and example queries.

Beyond the metrics SageMaker itself publishes, the Deepgram container emits its own usage and billing metrics directly into **your** CloudWatch account. They are written as [CloudWatch Embedded Metric Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html) lines on container stdout: SageMaker forwards container output to the endpoint's CloudWatch log group, and CloudWatch Logs extracts the metrics automatically. No agent, sidecar, or extra IAM permission is required, and the metrics keep flowing even in network-isolated Marketplace deployments.

Two namespaces are published, from two different layers of the container:

| Namespace                     | Layer                            | Purpose                                                                       | Can be disabled?                                          |
| ----------------------------- | -------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------- |
| `Deepgram/SageMakerInference` | Deepgram's SageMaker integration | Billing: consumed units per request, with audio duration and character counts | No — always on                                            |
| `Deepgram/SelfHosted`         | Deepgram API server              | Usage: per-method, per-tier, and per-feature utilization                      | Yes — on by default, opt out with an environment variable |

Unlike the [Prometheus & OpenTelemetry metrics](/docs/prometheus-otel-sagemaker), these are classic CloudWatch metrics: they appear in `aws cloudwatch list-metrics`, work with `get-metric-statistics`, dashboards, and alarms, and need nothing enabled on the endpoint configuration.

All dimensions are low-cardinality and contain no PII — never transcripts, TTS input, or per-request identifiers.

## Billing metrics: `Deepgram/SageMakerInference`

One EMF record is emitted per completed request (each streaming session and each pre-recorded or TTS request). These are the same consumed-unit values that drive AWS Marketplace metered billing, so this namespace is the tool for reconciling your AWS bill against actual traffic.

| Metric                 | Unit         | Description                                                                                                        |
| ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------ |
| `ConsumedUnits`        | Count        | Billable inference units for the request. `Sum` over a period is the total billed volume.                          |
| `AudioDurationSeconds` | Seconds      | Duration of audio processed (speech-to-text requests).                                                             |
| `CharCount`            | Count        | Characters synthesized (text-to-speech requests).                                                                  |
| `BillingLatencyMs`     | Milliseconds | Internal latency of the billing pipeline. Useful only for diagnosing billing delays; not a request-latency metric. |

Dimensions are published in three sets — `[Category]`, `[Category, Model]`, and `[Category, Model, Transport]` — so you can query at any granularity:

| Dimension   | Values                                                                          |
| ----------- | ------------------------------------------------------------------------------- |
| `Category`  | `stt_streaming`, `stt_batch`, `tts`                                             |
| `Model`     | The deployed model, for example `nova-3`, `flux-general-en`, `aura-2-thalia-en` |
| `Transport` | `ws` (streaming), `http` (pre-recorded / batch TTS)                             |

Example — total consumed units per hour, per category:

```bash
aws cloudwatch get-metric-statistics \
  --namespace Deepgram/SageMakerInference \
  --metric-name ConsumedUnits \
  --dimensions Name=Category,Value=stt_streaming \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum SampleCount \
  --region YOUR_AWS_REGION
```

`SampleCount` is the number of billed requests; `Sum` is the units consumed.

## Usage metrics: `Deepgram/SelfHosted`

The Deepgram API server emits a second EMF stream with raw usage broken down by method, model tier, and enabled features — independent of billing. Use it to understand *how* your endpoint is used: which features are enabled, how much audio each tier processes, and how much of the traffic is streaming versus pre-recorded.

| Metric           | Unit         | Dimensions              | Description                                                                                                                 |
| ---------------- | ------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `AudioMs`        | Milliseconds | `Deployment`, `Method`  | Audio processed per request (speech-to-text).                                                                               |
| `Requests`       | Count        | `Deployment`, `Method`  | Completed requests.                                                                                                         |
| `TtsCharacters`  | Count        | `Deployment`, `Method`  | Characters synthesized (text-to-speech).                                                                                    |
| `Tokens`         | Count        | `Deployment`, `Method`  | Tokens consumed by intelligence features (summarization, sentiment, and so on).                                             |
| `VoiceAgentMs`   | Milliseconds | `Deployment`, `Method`  | Voice-agent connection time.                                                                                                |
| `TierAudioMs`    | Milliseconds | `Deployment`, `Tier`    | Audio processed, broken down by model tier (for example `nova-3`, `flux`).                                                  |
| `FeatureAudioMs` | Milliseconds | `Deployment`, `Feature` | Audio processed with a given feature enabled. A request with several features enabled attributes its full duration to each. |
| `FeatureTokens`  | Count        | `Deployment`, `Feature` | Tokens consumed per intelligence feature.                                                                                   |

Dimension values: `Deployment` is `sagemaker`; `Method` is `streaming` or `sync` (pre-recorded); `Feature` is the request parameter name, for example `diarize`, `smart_format`, `punctuate`, `redact`, `keyterm`, `interim_results`.

Example — how much audio ran with diarization enabled today:

```bash
aws cloudwatch get-metric-statistics \
  --namespace Deepgram/SelfHosted \
  --metric-name FeatureAudioMs \
  --dimensions Name=Deployment,Value=sagemaker Name=Feature,Value=diarize \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum \
  --region YOUR_AWS_REGION
```

### Opting out

The usage stream is on by default. To disable it, set an environment variable override in the endpoint configuration's `Environment` map (see [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)):

```json
"Environment": {
  "DEEPGRAM_API_01": "emf.enabled=false"
}
```

The billing stream (`Deepgram/SageMakerInference`) cannot be disabled — it is part of the metering pipeline.

Because EMF metrics are extracted from the endpoint's CloudWatch log group, they stop if the log group is deleted or the container's logging permissions are removed. Standard CloudWatch metric pricing applies per unique metric/dimension combination; both streams keep dimension cardinality small by design.

## Related resources

* [Observability for Amazon SageMaker](/docs/observability-sagemaker) — SageMaker's own metrics, logs, and alarms
* [Prometheus & OpenTelemetry Metrics](/docs/prometheus-otel-sagemaker) — per-GPU and container Prometheus metrics via detailed observability
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments) — environment variable overrides
* [CloudWatch Embedded Metric Format specification](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html) (AWS)
