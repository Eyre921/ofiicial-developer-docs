---
title: "Retrieve Metrics"
source: https://resend.com/docs/api-reference/broadcasts/get-broadcasts-metrics
path: docs/api-reference/broadcasts/get-broadcasts-metrics
---

GET /broadcasts/metrics
Retrieve account-wide broadcast metrics, aggregated across all broadcasts.

<Warning>
  Broadcast metrics and recipients are currently in private beta and only
  available to a limited number of users. APIs might change before it is generally available.
  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.19.0-preview-headless-dashboard.7
    ```
  </CodeGroup>
</Warning>

<Note>
  Metrics are retained according to your plan's data retention window.
  Requesting a `start_date` older than your retention window returns data
  clamped to the oldest date your plan retains. This doesn't apply when
  `broadcast_id` is set.
</Note>

<Note>
  Responses are cached for up to 15 minutes, so a request for the same range may
  return slightly stale data within that window.
</Note>

## Query Parameters

<ParamField type="string">
  The start of the date range, as an ISO 8601 date (`2026-07-01`) or datetime
  (`2026-07-01T00:00:00Z`). Must be on or before `end_date`. Defaults to 6 days
  before `end_date`, unless `broadcast_id` is set, in which case it defaults to
  `2023-01-01` instead, since no broadcast could exist before Resend launched.
</ParamField>

<ParamField type="string">
  The end of the date range, as an ISO 8601 date or datetime. Values in the
  future are clamped to the current time. Defaults to now.
</ParamField>

<ParamField type="string">
  The IANA timezone (e.g. `America/New_York`) used to bucket periods when
  `period` is in `dimensions`.
</ParamField>

<ParamField type="hourly | daily | weekly | monthly">
  The bucket size used when `period` is in `dimensions`. Accepted but has no
  effect otherwise.
</ParamField>

<ParamField type="string[]">
  Comma-separated list of metrics to include in the response. Defaults to all
  of the following:

  `delivered`, `complained`, `suppressed`, `bounced`, `bounced_transient`,
  `bounced_permanent`, `bounced_undetermined`, `opened`, `clicked`,
  `unsubscribed`, `delivery_delayed`, `failed`, `sent`, `unique_opened`,
  `unique_clicked`, `delivery_rate`, `open_rate`, `click_rate`, `bounce_rate`,
  `complaint_rate`, `unsubscribe_rate`
</ParamField>

<ParamField type="string[]">
  Comma-separated list of dimensions to break the response down by. Combine
  `period` with `broadcast` for a joint breakdown (one row per unique `period`

  * `broadcast` pair). Defaults to `[]`, returning a single `totals` row for
    the whole range, with no `data`.

  Possible values:

  * `period`: one row per `granularity` period, in chronological order.
  * `broadcast`: one row per broadcast, including its `name` resolved from your
    account.
</ParamField>

<ParamField type="string[]">
  Comma-separated list of broadcast IDs to restrict the response to, up to 100.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/broadcasts/metrics?start_date=2026-07-01&end_date=2026-07-08&metrics=sent,delivered,open_rate&dimensions=period,broadcast' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "metrics",
    "start_date": "2026-07-01T00:00:00.000Z",
    "end_date": "2026-07-08T00:00:00.000Z",
    "metrics": ["sent", "delivered", "open_rate"],
    "dimensions": ["period", "broadcast"],
    "granularity": "daily",
    "totals": {
      "sent": 1204,
      "delivered": 1180,
      "open_rate": 50.0
    },
    "data": [
      {
        "period": "2026-07-01",
        "id": "d91cd9bd-1176-4f47-2a4b-fce2d5399cbf",
        "name": "July Newsletter",
        "sent": 172,
        "delivered": 169,
        "open_rate": 49.7
      }
    ]
  }
  ```
</ResponseExample>
