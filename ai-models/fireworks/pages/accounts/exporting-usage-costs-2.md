---
title: "Exporting Usage Costs"
source: https://docs.fireworks.ai/accounts/exporting-usage-costs
path: accounts/exporting-usage-costs
---

Export rated serverless usage costs to CSV, grouped by model, model tier, user, or API key

## Overview

Fireworks provides a CLI tool to export **rated dollar costs** for serverless inference as a CSV. Rows are bucketed by UTC day and grouped by one dimension you choose — model, model tier, user, or API key — which makes it the fastest way to produce a chargeback or per-team spend report.

The export is the CSV counterpart of [`POST /usageCosts:query`](/api-reference/query-usage-costs).

<Note title="Which export do I want?">
  * **This page** — rated dollar costs for serverless inference, as a CSV grouped by model, model tier, user, or API key.
  * **[Exporting Billing Metrics](/accounts/exporting-billing-metrics)** — metered quantities (tokens, accelerator-seconds) for every usage type, one CSV row per usage event. No dollars.
  * **[Usage & Cost Breakdown](/accounts/exporting-usage-and-costs)** — the same data as ad-hoc CLI or HTTP API queries rather than a CSV, with richer grouping and filtering.
</Note>

<Note>
  This export reports costs for the whole account, so it requires **account administrator** access. Non-admin users can read their own costs through [`POST /usageCosts:query`](/api-reference/query-usage-costs) at `SELF` scope.
</Note>

## Exporting usage costs

```bash theme={null}
# Authenticate (once)
firectl login

# Export usage costs to CSV
firectl billing export-usage-costs
```

With no flags, this exports the last 24 hours grouped by model and writes `usage_costs.csv` to the current directory.

## Examples

Group costs by API key instead of model:

```bash theme={null}
firectl billing export-usage-costs --group-by api_key
```

Export a specific date range, dimension, and filename:

```bash theme={null}
firectl billing export-usage-costs \
  --start-time "2026-05-01" \
  --end-time "2026-06-01" \
  --group-by user \
  --filename may_costs_by_user.csv
```

## Output format

The exported CSV always has these six columns, regardless of which dimension you group by:

* **account\_id**: Your Fireworks account ID
* **date**: UTC day bucket, as `YYYY-MM-DD`
* **group\_by\_dimension**: The dimension the row is grouped by — `model`, `model_tier`, `user`, or `api_key`
* **group\_by\_value**: The value for that dimension (see below)
* **subtotal\_usd**: Rated cost for that day and value, as an exact decimal with nine fractional digits
* **currency**: Currency code for `subtotal_usd`, for example `USD`

`group_by_value` depends on `--group-by`:

| `--group-by`      | `group_by_value`                                                             |
| ----------------- | ---------------------------------------------------------------------------- |
| `model` (default) | Model resource name, e.g. `accounts/my-account/models/glm-5p2`               |
| `model_tier`      | Serving capability tier used to price the usage, e.g. `GLM 5.2 (Fast)`       |
| `user`            | User resource name, e.g. `accounts/my-account/users/alice`                   |
| `api_key`         | Stable API key ID, e.g. `key_4nMFyHCSZP4CRKqa`. Never plaintext key material |

<Note>
  Two reserved values can appear in `group_by_value`: `unattributed`, when the underlying billing
  event carries no value for the requested dimension, and `unknown_model`, when a billing model
  can't be mapped to a public model. Days with an exact-zero subtotal are omitted rather than
  written as `0.000000000` rows, so a dimension value only appears on days it actually cost money.
</Note>

### Sample row

```csv theme={null}
account_id,date,group_by_dimension,group_by_value,subtotal_usd,currency
my-account,2026-05-14,model,accounts/my-account/models/glm-5p2,8.400000000,USD
```

## Automation

Each `firectl billing export-usage-costs` call supports a maximum 31-day time range, and
`--start-time` cannot be more than 100 days in the past. To export longer historical ranges, run
the command in multiple 31-day chunks and combine the CSV files in your downstream pipeline.

```bash theme={null}
# Example: Daily export with dated filename
firectl billing export-usage-costs \
  --start-time "$(date -v-1d '+%Y-%m-%d')" \
  --end-time "$(date '+%Y-%m-%d')" \
  --group-by api_key \
  --filename "usage_costs_$(date '+%Y%m%d').csv"
```

```bash theme={null}
# Example: Backfill 90 days in 31-day chunks
start_date="2026-03-01"
end_date="2026-06-01"
current_start="$start_date"

while [ "$(date -j -f "%Y-%m-%d" "$current_start" "+%s")" -lt "$(date -j -f "%Y-%m-%d" "$end_date" "+%s")" ]; do
  current_end="$(date -j -v+31d -f "%Y-%m-%d" "$current_start" "+%Y-%m-%d")"

  # Clamp the chunk end to the requested end_date
  if [ "$(date -j -f "%Y-%m-%d" "$current_end" "+%s")" -gt "$(date -j -f "%Y-%m-%d" "$end_date" "+%s")" ]; then
    current_end="$end_date"
  fi

  firectl billing export-usage-costs \
    --start-time "$current_start" \
    --end-time "$current_end" \
    --filename "usage_costs_${current_start}_to_${current_end}.csv"

  current_start="$current_end"
done
```

<Tip>
  Run `firectl billing export-usage-costs --help` to see all available flags and options.
</Tip>

## Coverage

* **Serverless token usage only.** Costs are priced from cached input, uncached input, and output tokens. Dedicated deployment and training spend are not included — for those, use [Exporting Billing Metrics](/accounts/exporting-billing-metrics) or the account-level totals from [`firectl billing get-usage --account-costs-only`](/accounts/exporting-usage-and-costs#account-level-cost-totals-only).
* **Subtotals are rated, not invoiced.** They price usage with the subscription prices that apply to your account and exclude fixed fees, invoice-level discounts, minimums, credits, and taxes, so they may differ from the final invoice.
* **One dimension at a time.** Rows are always bucketed by day plus the single dimension passed to `--group-by`. To combine dimensions, use [`POST /usageCosts:query`](/api-reference/query-usage-costs), which accepts up to two.

## See also

* [`POST /v1/accounts/{account_id}/usageCosts:query`](/api-reference/query-usage-costs) - The HTTP API behind this export
* [Exporting Billing Metrics](/accounts/exporting-billing-metrics) - Raw per-event usage CSV across all usage types
* [Usage & Cost Breakdown](/accounts/exporting-usage-and-costs) - Grouped usage and rated cost queries via `firectl billing get-usage` and the billing APIs
* [Serverless pricing](/serverless/pricing) - Published per-token prices
