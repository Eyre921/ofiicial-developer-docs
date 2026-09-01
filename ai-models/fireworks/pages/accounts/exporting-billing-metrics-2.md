---
title: "Exporting Billing Metrics"
source: https://docs.fireworks.ai/accounts/exporting-billing-metrics
path: accounts/exporting-billing-metrics
---

Export billing and usage metrics for all Fireworks services

## Overview

Fireworks provides a CLI tool to export comprehensive billing metrics for all usage types including serverless inference, on-demand deployments, and training jobs. The exported data can be used for cost analysis, internal billing, and usage tracking.

<Note>
  This export reports metered **quantities** — tokens and accelerator-seconds — not dollars. For a
  CSV of rated serverless **costs** grouped by model, model tier, user, or API key, use
  [Exporting Usage Costs](/accounts/exporting-usage-costs).
</Note>

## Exporting billing metrics

Use the Fireworks CLI to export a billing CSV that includes all usage:

```bash theme={null}
# Authenticate (once)
firectl login

# Export billing metrics to CSV
firectl billing export-metrics
```

## Examples

Export all billing metrics for an account:

```bash theme={null}
firectl billing export-metrics
```

Export metrics for a specific date range and filename:

```bash theme={null}
firectl billing export-metrics \
  --start-time "2025-01-01" \
  --end-time "2025-01-31" \
  --filename january_metrics.csv
```

## Output format

The exported CSV includes the following columns:

* **email**: Account email
* **start\_time**: Request start timestamp
* **end\_time**: Request end timestamp
* **usage\_type**: Type of usage (e.g., TEXT\_COMPLETION\_INFERENCE\_USAGE)
* **accelerator\_type**: GPU/hardware type used
* **accelerator\_seconds**: Compute time in seconds
* **base\_model\_name**: The model used
* **model\_bucket**: Model category
* **parameter\_count**: Model size
* **prompt\_tokens**: Input tokens
* **completion\_tokens**: Output tokens
* **cached\_prompt\_tokens**: Prompt tokens served from cache (text inference only). Subset of `prompt_tokens`.
* **uncached\_prompt\_tokens**: Prompt tokens not served from cache (text inference only). `prompt_tokens - cached_prompt_tokens`.

<Note>
  Older usage records and non-text usage types may not have a cached/uncached split
  in the underlying data. Exports normalize these rows to `cached_prompt_tokens=0`
  and `uncached_prompt_tokens=prompt_tokens`, so `prompt_tokens =
      cached_prompt_tokens + uncached_prompt_tokens` always holds.
</Note>

### Sample row

```csv theme={null}
email,start_time,end_time,usage_type,accelerator_type,accelerator_seconds,base_model_name,model_bucket,parameter_count,prompt_tokens,completion_tokens,cached_prompt_tokens,uncached_prompt_tokens
user@example.com,2025-10-20 17:16:48 UTC,2025-10-20 17:16:48 UTC,TEXT_COMPLETION_INFERENCE_USAGE,,,accounts/fireworks/models/llama4-maverick-instruct-basic,Llama 4 Maverick Basic,401583781376,803,109,200,603
```

## Automation

Each `firectl billing export-metrics` call supports a maximum 31-day time range.
To export longer historical ranges, run the command in multiple 31-day chunks and
combine the CSV files in your downstream pipeline.

You can automate exports in cron jobs and load the CSV into your internal systems:

```bash theme={null}
# Example: Daily export with dated filename
firectl billing export-metrics \
  --start-time "$(date -v-1d '+%Y-%m-%d')" \
  --end-time "$(date '+%Y-%m-%d')" \
  --filename "billing_$(date '+%Y%m%d').csv"
```

```bash theme={null}
# Example: Backfill 6 months in 31-day chunks
start_date="2025-01-01"
end_date="2025-07-01"
current_start="$start_date"

while [ "$(date -j -f "%Y-%m-%d" "$current_start" "+%s")" -lt "$(date -j -f "%Y-%m-%d" "$end_date" "+%s")" ]; do
  current_end="$(date -j -v+31d -f "%Y-%m-%d" "$current_start" "+%Y-%m-%d")"

  # Clamp the chunk end to the requested end_date
  if [ "$(date -j -f "%Y-%m-%d" "$current_end" "+%s")" -gt "$(date -j -f "%Y-%m-%d" "$end_date" "+%s")" ]; then
    current_end="$end_date"
  fi

  firectl billing export-metrics \
    --start-time "$current_start" \
    --end-time "$current_end" \
    --filename "billing_${current_start}_to_${current_end}.csv"

  current_start="$current_end"
done
```

<Tip>
  Run `firectl billing export-metrics --help` to see all available flags and
  options.
</Tip>

## Coverage

This export includes:

* **Serverless inference**: All serverless API usage
* **On-demand deployments**: Deployment usage (see also [Exporting deployment metrics](/deployments/exporting-metrics) for real-time Prometheus metrics)
* **Training jobs**: Training compute usage
* **Other services**: All billable Fireworks services

<Note>
  For real-time monitoring of on-demand deployment performance metrics (latency,
  throughput, etc.), use the [Prometheus metrics
  endpoint](/deployments/exporting-metrics) instead.
</Note>

## See also

* [firectl CLI overview](/tools-sdks/firectl/firectl)
* [Exporting Usage Costs](/accounts/exporting-usage-costs) - Rated serverless cost CSV grouped by model, model tier, user, or API key
* [Exporting deployment metrics](/deployments/exporting-metrics) - Real-time Prometheus metrics for on-demand deployments
* [Account quotas](/guides/quotas_usage/account-quotas) - Spending tiers, monthly spend limits, and account-wide request limits
* [Serverless rate limits](/serverless/rate-limits) - Adaptive serverless TPM bounds
