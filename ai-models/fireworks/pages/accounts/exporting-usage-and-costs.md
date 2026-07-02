---
title: "Usage & Cost Breakdown"
source: https://docs.fireworks.ai/accounts/exporting-usage-and-costs
path: accounts/exporting-usage-and-costs
---

Break down usage and rated costs by deployment, model, API key, or custom tags — via firectl or the billingUsage API

## Overview

Fireworks exposes the same usage-and-cost data through two equivalent surfaces:

* **CLI** — [`firectl billing get-usage`](/tools-sdks/firectl/commands/billing-get-usage), best for ad-hoc queries, shell scripting, and one-off cost reviews.
* **HTTP API** — [`GET /v1/accounts/{account_id}/billingUsage`](/api-reference/get-billing-usage), best for cron jobs, dashboards, and downstream cost-attribution pipelines.

Both return the same response shape and accept the same dimensions. Every example below shows the CLI form and the equivalent cURL side-by-side. Pick whichever fits your workflow.

The output has two parts:

* **Account costs** — rated dollar totals for the range (CLI: prints by default; API: companion `GetBillingSummary` endpoint).
* **Usage** — metered quantities (tokens, accelerator-seconds, audio input seconds) grouped by your chosen dimensions.

This page complements [Exporting Billing Metrics](/accounts/exporting-billing-metrics): use `export-metrics` for a raw per-event CSV dump, and the workflows on this page for grouped, rated views.

<Note>
  CLI examples require `firectl` 1.7.21 or later. Run `firectl version`, then `firectl upgrade` if needed.
</Note>

## Authentication

For the API, send your Fireworks API key as a bearer token. Any key on the target account works.

```bash theme={null}
export ACCOUNT_ID="<your-account-slug>"
export FIREWORKS_API_KEY="fw_..."
```

For the CLI, run `firectl login` once and `firectl` reads credentials from `~/.fireworks/auth.ini`.

## Basic usage

Get a 30-day account-wide breakdown (defaults to all usage types, grouped by model for serverless and by deployment + accelerator for dedicated):

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 \
      --end-time   2026-06-01
    ```

    Add `-o json` for machine-readable output.
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
      -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
      --data-urlencode "startTime=2026-05-01T00:00:00Z" \
      --data-urlencode "endTime=2026-06-01T00:00:00Z"
    ```
  </Tab>
</Tabs>

## Examples

### Serverless usage by model

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 --end-time 2026-06-01 \
      --usage-type serverless \
      --group-by model_name
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
      -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
      --data-urlencode "startTime=2026-05-01T00:00:00Z" \
      --data-urlencode "endTime=2026-06-01T00:00:00Z" \
      --data-urlencode "usageType=SERVERLESS" \
      --data-urlencode "groupBy=model_name"
    ```
  </Tab>
</Tabs>

### Serverless usage by API key

Breaks out serverless token consumption per API key. Pass both `api_key_id` (stable internal ID) and `api_key_name` (human-readable label from the console / `firectl api-key create --name`) so the response carries both.

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 --end-time 2026-06-01 \
      --usage-type serverless \
      --group-by api_key_id \
      --group-by api_key_name \
      --group-by model_name
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
      -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
      --data-urlencode "startTime=2026-05-01T00:00:00Z" \
      --data-urlencode "endTime=2026-06-01T00:00:00Z" \
      --data-urlencode "usageType=SERVERLESS" \
      --data-urlencode "groupBy=api_key_id" \
      --data-urlencode "groupBy=api_key_name" \
      --data-urlencode "groupBy=model_name"
    ```
  </Tab>
</Tabs>

Sample row from the API response:

```json theme={null}
{
  "startTime": "2026-05-28T00:00:00Z",
  "endTime":   "2026-05-29T00:00:00Z",
  "promptTokens":     "1842301",
  "completionTokens": "412980",
  "audioInputSeconds": 0,
  "usageType": "TEXT_COMPLETION_INFERENCE_USAGE",
  "group": {
    "api_key_id":   "key_4nMFyHCSZP4CRKqa",
    "api_key_name": "prod-eng",
    "model_name":   "accounts/fireworks/models/kimi-k2.6"
  }
}
```

<Note>
  Token counts come back as JSON **strings** (int64 over JSON). Cast them with `tonumber` in `jq` or the equivalent in your client before doing arithmetic. The deprecated top-level `apiKeyId` field is only populated when `groupBy=api_key_id` is requested — always read API-key values from the `group` map.
</Note>

### Filter to a specific API key

Repeat `--filter` (CLI) or `filter[<dim>][values]=` (API) to OR multiple values for the same dimension.

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 --end-time 2026-06-01 \
      --usage-type serverless \
      --group-by model_name \
      --filter api_key_name=prod-eng
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
      -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
      --data-urlencode "startTime=2026-05-01T00:00:00Z" \
      --data-urlencode "endTime=2026-06-01T00:00:00Z" \
      --data-urlencode "usageType=SERVERLESS" \
      --data-urlencode "groupBy=model_name" \
      --data-urlencode 'filter[api_key_name][values]=prod-eng'
    ```
  </Tab>
</Tabs>

### Dedicated deployment usage by deployment and GPU type

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 --end-time 2026-06-01 \
      --usage-type dedicated-deployment \
      --group-by deployment_name \
      --group-by accelerator_type
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
      -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
      --data-urlencode "startTime=2026-05-01T00:00:00Z" \
      --data-urlencode "endTime=2026-06-01T00:00:00Z" \
      --data-urlencode "usageType=DEDICATED_DEPLOYMENT" \
      --data-urlencode "groupBy=deployment_name" \
      --data-urlencode "groupBy=accelerator_type"
    ```
  </Tab>
</Tabs>

### Filter to a single deployment

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 --end-time 2026-06-01 \
      --filter deployment_name=accounts/my-account/deployments/my-deployment
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
      -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
      --data-urlencode "startTime=2026-05-01T00:00:00Z" \
      --data-urlencode "endTime=2026-06-01T00:00:00Z" \
      --data-urlencode 'filter[deployment_name][values]=accounts/my-account/deployments/my-deployment'
    ```
  </Tab>
</Tabs>

### Account-level cost totals only

<Tabs>
  <Tab title="firectl">
    ```bash theme={null}
    firectl billing get-usage \
      --start-time 2026-05-01 --end-time 2026-06-01 \
      --account-costs-only
    ```
  </Tab>

  <Tab title="cURL">
    Rated dollar totals come from a companion endpoint, `GetBillingSummary`. Use the CLI for this view today; we'll surface the same data through the API in a future release.
  </Tab>
</Tabs>

## Reference

### CLI flags

| Flag                   | Description                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------- |
| `--start-time`         | Start time (inclusive), as `YYYY-MM-DD` or `'YYYY-MM-DD hh:mm:ss'`.                |
| `--end-time`           | End time (exclusive), same formats.                                                |
| `--usage-type`         | `all`, `serverless`, or `dedicated-deployment`. Defaults to all.                   |
| `--group-by`           | Dimension to group by. Repeatable.                                                 |
| `--filter`             | `key=value` filter. Repeatable; repeated values for the same key are OR'ed.        |
| `--timezone`           | IANA timezone for daily aggregation (e.g. `America/Los_Angeles`). Defaults to UTC. |
| `--account-costs-only` | Print only account-level cumulative costs for the range.                           |
| `-o, --output`         | `text` (default) or `json`.                                                        |

Run `firectl billing get-usage --help` for the full list.

### API parameters

The same dimensions are passed as `groupBy=<dim>` (repeat for multiple) and `filter[<dim>][values]=<value>` (repeat for OR). `usageType` takes `SERVERLESS`, `DEDICATED_DEPLOYMENT`, or omitted for all. `timezone` and `startTime`/`endTime` mirror the CLI flags. See [the full API reference](/api-reference/get-billing-usage) for parameter schemas and response types.

### Grouping dimensions

Valid `--group-by` / `groupBy` and `--filter` / `filter` dimensions depend on the usage type:

* **Serverless**: `model_name`, `api_key_id`, `api_key_name`, `annotations.team`, `annotations.project`, `annotations.environment`
* **Dedicated deployment**: `deployment_name`, `accelerator_type`, `annotations.team`, `annotations.project`, `annotations.environment`

Dedicated-deployment rows also include the deployment's region (`placement`, e.g. `US`, `EUROPE`, `GLOBAL`) and metered `accelerator_seconds`.

## Custom tags (team / project / environment)

Group by `annotations.team`, `annotations.project`, or `annotations.environment` to split usage by your own labels. The tag source depends on usage type:

* **Dedicated deployments**: set an `annotations` map on the deployment, e.g. `{"team": "search", "project": "x", "environment": "prod"}`.
* **Serverless**: send a per-request header on inference calls:

  ```http theme={null}
  POST /inference/v1/chat/completions HTTP/1.1
  Host: api.fireworks.ai
  Authorization: Bearer fw_...
  Fireworks-Annotations: team=search,project=ranker,environment=prod
  Content-Type: application/json
  ```

  Annotation values are validated server-side; unrecognized keys are dropped silently.

## Cookbook: per-API-key reporting recipes

These recipes target the HTTP API, where downstream aggregation in `jq` (or any client) is easiest.

### Aggregate per key, across models

Sums prompt and completion tokens for each API key across every model it called, sorted by prompt volume.

```bash theme={null}
curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  --data-urlencode "startTime=2026-05-01T00:00:00Z" \
  --data-urlencode "endTime=2026-06-01T00:00:00Z" \
  --data-urlencode "usageType=SERVERLESS" \
  --data-urlencode "groupBy=api_key_id" \
  --data-urlencode "groupBy=api_key_name" \
  --data-urlencode "groupBy=model_name" \
  | jq '.serverlessCosts
        | group_by(.group.api_key_id)
        | map({
            api_key_id:        .[0].group.api_key_id,
            api_key_name:      .[0].group.api_key_name,
            models:            (map(.group.model_name) | unique),
            prompt_tokens:     ([.[].promptTokens     | tonumber] | add),
            completion_tokens: ([.[].completionTokens | tonumber] | add)
          })
        | sort_by(-.prompt_tokens)'
```

### Group by model, then by key (cost-by-tool view)

If reporting starts from "how much did each model cost me, and which keys drove that", flip the nesting:

```bash theme={null}
curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  --data-urlencode "startTime=2026-05-01T00:00:00Z" \
  --data-urlencode "endTime=2026-06-01T00:00:00Z" \
  --data-urlencode "usageType=SERVERLESS" \
  --data-urlencode "groupBy=api_key_id" \
  --data-urlencode "groupBy=api_key_name" \
  --data-urlencode "groupBy=model_name" \
  | jq '.serverlessCosts
        | group_by(.group.model_name)
        | map({
            model: .[0].group.model_name,
            api_keys: (
              group_by(.group.api_key_id)
              | map({
                  api_key_id:        .[0].group.api_key_id,
                  api_key_name:      .[0].group.api_key_name,
                  prompt_tokens:     ([.[].promptTokens     | tonumber] | add),
                  completion_tokens: ([.[].completionTokens | tonumber] | add)
                })
              | sort_by(-.prompt_tokens)
            )
          })
        | sort_by(.model)'
```

Multiply the token totals by the published [serverless prices](/serverless/pricing) to convert to dollars for chargeback.

### Backfill more than 31 days

The endpoint caps each request at a 31-day window. To pull a longer history, loop month-by-month:

```bash theme={null}
start_date="2026-01-01"
end_date="2026-06-01"
current="$start_date"

while [ "$(date -u -d "$current" '+%s')" -lt "$(date -u -d "$end_date" '+%s')" ]; do
  next="$(date -u -d "$current +30 days" '+%Y-%m-%d')"
  if [ "$(date -u -d "$next" '+%s')" -gt "$(date -u -d "$end_date" '+%s')" ]; then
    next="$end_date"
  fi

  curl -sG "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/billingUsage" \
    -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
    --data-urlencode "startTime=${current}T00:00:00Z" \
    --data-urlencode "endTime=${next}T00:00:00Z" \
    --data-urlencode "usageType=SERVERLESS" \
    --data-urlencode "groupBy=api_key_id" \
    --data-urlencode "groupBy=api_key_name" \
    > "usage_${current}_to_${next}.json"

  current="$next"
done
```

## Granularity and freshness

* Usage is aggregated into **daily** buckets (`--timezone` / `timezone=` sets the day boundary). There are no sub-daily buckets.
* Responses are cached for several minutes — fine for cron jobs and dashboards, not for real-time.

## Coverage caveats

* **Tokens, not dollars.** The endpoint returns metered quantities (`promptTokens`, `completionTokens`, `accelerator_seconds`, `audioInputSeconds`). Multiply by the [serverless prices](/serverless/pricing) for cost, or use `--account-costs-only` for account-level dollar totals.
* **Inference types covered today**: text completion / chat completion and audio inference. Embeddings and image generation aren't yet reflected in `billingUsage` responses; coverage will expand in subsequent releases.
* **Dedicated deployments** are attributed at the deployment level, not by API key. Use `usageType=DEDICATED_DEPLOYMENT` with `groupBy=deployment_name` for that breakdown.

<Tip>
  Run `firectl billing get-usage --help` to see all available CLI flags and options.
</Tip>

## See also

* [`firectl billing get-usage`](/tools-sdks/firectl/commands/billing-get-usage) - CLI command reference
* [`GET /v1/accounts/{account_id}/billingUsage`](/api-reference/get-billing-usage) - HTTP API reference
* [Exporting Billing Metrics](/accounts/exporting-billing-metrics) - Raw per-event billing CSV export
* [Account quotas](/guides/quotas_usage/account-quotas) - Spending tiers and budget controls
