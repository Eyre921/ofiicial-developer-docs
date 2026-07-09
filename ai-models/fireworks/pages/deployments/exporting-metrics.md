---
title: "Exporting Metrics"
source: https://docs.fireworks.ai/deployments/exporting-metrics
path: deployments/exporting-metrics
---

Export metrics from your dedicated deployments to your observability stack

## Overview

Fireworks provides a metrics endpoint in Prometheus format, enabling integration with popular observability tools like Prometheus, OpenTelemetry (OTel) Collector, Datadog Agent, and Vector.

<Note>
  This page covers real-time performance metrics (latency, throughput, etc.) for on-demand deployments. For billing and usage data across all Fireworks services, see [Exporting Billing Metrics](/accounts/exporting-billing-metrics).
</Note>

## Setting Up Metrics Collection

### Endpoint

The metrics endpoint is as follows. This URL and authorization header can be directly used by services like Grafana Cloud to ingest Fireworks metrics.

```
https://api.fireworks.ai/v1/accounts/<account-id>/metrics
```

### Authentication

Use the Authorization header with your Fireworks API key:

```json theme={null}
{
  "Authorization": "Bearer YOUR_API_KEY"
}
```

### Scrape Interval

We recommend using a 1-minute scrape interval as metrics are updated every 30s.

### Rate Limits

To ensure service stability and fair usage:

* Maximum of 6 requests per minute per account
* Exceeding this limit results in HTTP 429 (Too Many Requests) responses
* Use a 1-minute scrape interval to stay within limits

## Integration Options

Fireworks metrics can be integrated with various observability platforms through multiple approaches:

### OpenTelemetry Collector Integration

The Fireworks metrics endpoint can be integrated with OpenTelemetry Collector by configuring a Prometheus receiver that scrapes the endpoint. This allows Fireworks metrics to be pushed to a variety of popular exporters—see the [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/) for a full list.

### Direct Prometheus Integration

To integrate directly with Prometheus, specify the Fireworks metrics endpoint in your scrape config:

```yaml theme={null}
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'fireworks'
    metrics_path: 'v1/accounts/<account-id>/metrics'
    authorization:
      type: "Bearer"
      credentials: "YOUR_API_KEY"
    static_configs:
      - targets: ['api.fireworks.ai']
    scheme: https
```

For more details on Prometheus configuration, refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

### Supported Platforms

Fireworks metrics can be exported to various observability platforms including:

* Prometheus
* Datadog
* Grafana
* New Relic

## Available Metrics

### Common Labels

All metrics include the following common labels:

* `base_model`: The base model identifier (e.g., "accounts/fireworks/models/deepseek-v3")
* `deployment`: Full deployment path (e.g., "accounts/account-name/deployments/deployment-id")
* `deployment_account`: The account name
* `deployment_id`: The deployment identifier

### Rate Metrics (per second)

These metrics show activity rates calculated using 1-minute windows:

#### Request Rate

* `request_counter_total:sum_by_deployment`: Request rate per deployment

#### Error Rate

* `requests_error_total:sum_by_deployment`: Error rate per deployment, broken down by HTTP status code (includes additional `http_code` label)

#### Token Processing Rates

* `tokens_cached_prompt_total:sum_by_deployment`: Rate of cached prompt tokens per deployment
* `tokens_prompt_total:sum_by_deployment`: Rate of total prompt tokens processed per deployment

### Latency Histogram Metrics

These metrics provide latency distribution data with histogram buckets, calculated using 1-minute windows:

#### Generation Latency

* `latency_generation_per_token_ms_bucket:sum_by_deployment`: Per-token generation time distribution
* `latency_generation_queue_ms_bucket:sum_by_deployment`: Time spent waiting in generation queue

#### Request Latency

* `latency_overall_ms_bucket:sum_by_deployment`: End-to-end request latency distribution
* `latency_to_first_token_ms_bucket:sum_by_deployment`: Time to first token distribution

#### Prefill Latency

* `latency_prefill_ms_bucket:sum_by_deployment`: Prefill processing time distribution
* `latency_prefill_queue_ms_bucket:sum_by_deployment`: Time spent waiting in prefill queue

### Token Distribution Metrics

These histogram metrics show token count distributions per request, calculated using 1-minute windows:

* `tokens_generated_per_request_bucket:sum_by_deployment`: Distribution of generated tokens per request
* `tokens_prompt_per_request_bucket:sum_by_deployment`: Distribution of prompt tokens per request

### Resource Utilization Metrics

These gauge metrics show average resource usage:

* `generator_kv_blocks_fraction:avg_by_deployment`: Average fraction of KV cache blocks in use
* `generator_kv_slots_fraction:avg_by_deployment`: Average fraction of KV cache slots in use
* `generator_model_forward_time:avg_by_deployment`: Average time spent in model forward pass
* `prefiller_prompt_cache_ttl:avg_by_deployment`: Average prompt cache time-to-live
