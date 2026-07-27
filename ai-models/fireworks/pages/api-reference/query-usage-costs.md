---
title: "Query grouped usage cost subtotals for an account."
source: https://docs.fireworks.ai/api-reference/query-usage-costs
path: api-reference/query-usage-costs
---

post /v1/accounts/{account_id}/usageCosts:query
Returns rated dollar subtotals for usage over a time range, grouped by up to two of: HOUR, DAY, MODEL, USER, or API_KEY. Unlike `GET /billingUsage` (metered quantities) and `GET /billing/summary` (line items by billing category), this endpoint returns *rated costs* broken down by caller-supplied dimensions, with pagination and an account-wide `subtotal`. Requires account administrator access for `ACCOUNT` scope; `SELF` scope returns costs for the authenticated principal only.
