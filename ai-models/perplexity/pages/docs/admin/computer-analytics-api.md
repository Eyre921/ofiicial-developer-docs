---
title: "Computer Analytics API"
source: https://docs.perplexity.ai/docs/admin/computer-analytics-api
path: docs/admin/computer-analytics-api
---

Query your organization's Computer usage analytics programmatically with a free, org-scoped API key

## Overview

The Computer Analytics API gives Perplexity Enterprise organizations programmatic access to the same Computer usage analytics shown in the web dashboard — credits, connectors, artifacts, skills, spaces, workflows, and task durations — as bucketed time series you can pull into BI tools or internal reporting.

Analytics requests are free and don't consume API credits.

<Info>
  This API is available to Perplexity Enterprise organizations. If you don't see the Analytics API toggle described below, the feature may not be enabled for your organization yet — contact your Perplexity representative.
</Info>

## Getting Access

Access is managed by your organization's admins from the Perplexity web app:

<Steps>
  <Step title="Enable the Analytics API">
    In the Perplexity web app, open your organization's **Computer** settings and find the **Analytics** section. Turn on **Analytics API** to provision API access for your organization.
  </Step>

  <Step title="Generate your API key">
    In the row that appears below the toggle, select **Generate key**.
  </Step>
</Steps>

A few properties of analytics API keys:

* **Org-scoped, admin-managed** — the key belongs to your organization, not to the admin who created it. Any org admin can view the current key and regenerate it.
* **One active key** — your organization has at most one active analytics key. Regenerating revokes the previous key.
* **Analytics-only** — the key authenticates analytics endpoints only; it cannot call other Perplexity APIs and has no billing attached.
* **Disabling revokes** — turning the Analytics API toggle off permanently revokes the key.

## Authentication

Pass the key as a bearer token:

```bash theme={null}
curl --request GET \
  --url "https://api.perplexity.ai/v1/analytics/computer/usage?dataset=credit_usage&start_time=1746057600" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

## Querying Usage

`GET /v1/analytics/computer/usage` returns one time series per request, for a single dataset.

### Parameters

| Parameter      | Required | Description                                                                                                                   |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `dataset`      | Yes      | One of `credit_usage`, `connectors`, `artifacts`, `skills`, `spaces`, `workflows`, `task_durations`.                          |
| `start_time`   | Yes      | Window start, unix seconds (UTC). Inclusive. Snapped down to the bucket grid.                                                 |
| `end_time`     | No       | Window end, unix seconds (UTC). Exclusive. Defaults to now; values in the future are capped at now.                           |
| `bucket_width` | No       | `1d` (default) or `1h`. Buckets align to the UTC grid.                                                                        |
| `limit`        | No       | Buckets per page. `1d`: default 7, max 31. `1h`: default 24, max 168.                                                         |
| `page`         | No       | Opaque pagination cursor from a previous response's `next_page`. Valid only with the same query parameters it was issued for. |
| `user_email`   | No       | Restrict results to a single member of your organization. See [Filtering by member](#filtering-by-member).                    |

### Response

```json theme={null}
{
  "categories": ["Model", "Credit Source"],
  "data": [
    {
      "start_time": 1746057600,
      "end_time": 1746144000,
      "count": 350,
      "by_categories": {
        "Model": [
          { "category": "claude-opus-4-8", "count": 210 },
          { "category": "claude-sonnet-4-6", "count": 120 }
        ],
        "Credit Source": [
          { "category": "paid", "count": 250 },
          { "category": "promo", "count": 80 }
        ]
      }
    }
  ],
  "has_more": false,
  "next_page": null
}
```

* `categories` lists the breakdown axes the dataset surfaces, in canonical render order. Most datasets carry one axis; `credit_usage` carries two (`Model` and `Credit Source`).
* `data` contains every bucket in the page's window, in chronological order. Buckets without data carry `count: 0` and an empty list under each axis in `by_categories`.
* `by_categories` maps each axis label to its breakdown for the bucket. Categories within an axis are the dataset's dimension values — connector names for `connectors`, artifact types for `artifacts`, duration bands for `task_durations`, `paid`/`promo` for `credit_usage`'s `Credit Source`, model names for `credit_usage`'s `Model`, and the titles your members gave the items for `spaces`/`skills`/`workflows`.
* For `credit_usage`, `count` can exceed the sum of any single breakdown — usage without a category attribution counts toward the total but not the breakdown.

### Time Windows and Buckets

The API serves **complete UTC grid buckets only**:

* `start_time` snaps down to the start of its bucket, so the first bucket can include usage from before your requested start.
* `end_time` is exclusive and is capped at the current time, then snapped down — the in-progress bucket is never returned. With `bucket_width=1d`, today's bucket is not included; use `1h` for intraday data.
* A valid window that contains no complete buckets returns `200` with empty `data`.

<Note>
  **Data freshness.** The analytics store is synced periodically, not in real time. A `count` of `0` in a recent bucket can mean the data hasn't synced yet rather than zero usage. When `has_more` is `false` you have reached the current data frontier — poll again later for newer buckets.
</Note>

### Pagination

When the window spans more buckets than `limit`, the response sets `has_more: true` and a `next_page` cursor. Pass it back as `page`, keeping every other parameter identical — cursors are strictly validated and a cursor used with different parameters returns `400`.

```python theme={null}
import requests

BASE_URL = "https://api.perplexity.ai/v1/analytics/computer/usage"
HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

params = {
    "dataset": "credit_usage",
    "start_time": 1746057600,
    "bucket_width": "1d",
}

buckets = []
while True:
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    payload = response.json()
    buckets.extend(payload["data"])
    if not payload["has_more"]:
        break
    params["page"] = payload["next_page"]

print(f"Fetched {len(buckets)} buckets")
```

### Filtering by Member

Pass `user_email` to restrict the series to a single member of your organization:

```bash theme={null}
curl --request GET \
  --url "https://api.perplexity.ai/v1/analytics/computer/usage?dataset=credit_usage&start_time=1746057600&user_email=member@example.com" \
  --header "Authorization: Bearer YOUR_API_KEY"
```

The email must belong to a current member of your organization. Any other value — including emails with no Perplexity account — returns the same generic `400`:

```json theme={null}
{
  "error": {
    "message": "user_email does not match a member of this organization.",
    "type": "invalid_request",
    "code": 400
  }
}
```

## Errors

Errors use a consistent envelope:

```json theme={null}
{
  "error": {
    "message": "Human-readable description.",
    "type": "machine_readable_type",
    "code": 400
  }
}
```

| Status | `type`                        | Meaning                                                                                                                                                                                      |
| ------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`  | `bad_request`                 | A parameter failed validation (wrong type, malformed value).                                                                                                                                 |
| `400`  | `invalid_request`             | Parameters are well-formed but semantically invalid — e.g. `start_time` after `end_time`, a window over 90 days, a misused pagination cursor, or a `user_email` that doesn't match a member. |
| `401`  | `unauthorized`                | Missing or invalid API key.                                                                                                                                                                  |
| `404`  | `feature_disabled`            | The Computer Analytics API is not enabled for your organization.                                                                                                                             |
| `429`  | `request_rate_limit_exceeded` | Rate limit exceeded. Requests are limited per organization across all of its keys; retry with backoff.                                                                                       |

## Limits

* Time windows are limited to **90 days** per request (paginate within the window for long ranges).
* Requests are rate-limited **per organization** — all keys minted by your org share one allowance.
