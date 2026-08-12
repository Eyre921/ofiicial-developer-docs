---
title: "Retrieve Metrics"
source: https://resend.com/docs/api-reference/emails/get-metrics
path: docs/api-reference/emails/get-metrics
---

GET /emails/metrics
Retrieve account-level email metrics.

<Warning>
  Email metrics are currently in private beta and only available to a
  limited number of users. APIs might change before it is generally available.
  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}} theme={"theme":{"light":"github-light","dark":"vesper"}} theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.19.0-preview-headless-dashboard.3
    ```
  </CodeGroup>
</Warning>

<Note>
  Metrics are retained according to your plan's data retention window.
  Requesting a `start_date` older than your retention window returns data
  clamped to the oldest date your plan retains.
</Note>

<Note>
  Responses are cached for up to 15 minutes, so a request for the same range may
  return slightly stale data within that window.
</Note>

## Query Parameters

<ParamField type="string">
  The start of the date range, as an ISO 8601 date (`2026-07-01`) or datetime
  (`2026-07-01T00:00:00Z`). Must be on or before `end_date`. Defaults to 6 days
  before `end_date`.
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
  effect otherwise. The date range can't produce more than 10,000 periods at the
  chosen granularity. This limit only applies when `period` is in `dimensions`.
</ParamField>

<ParamField type="string[]">
  Comma-separated list of metrics to include in the response. Defaults to all
  of the following:

  `received`, `delivered`, `complained`, `suppressed`, `bounced`,
  `bounced_transient`, `bounced_permanent`, `bounced_undetermined`, `opened`,
  `clicked`, `unsubscribed`, `delivery_delayed`, `failed`, `sent`,
  `unique_opened`, `unique_clicked`, `delivery_rate`, `open_rate`, `click_rate`,
  `bounce_rate`, `complaint_rate`, `unsubscribe_rate`
</ParamField>

<ParamField type="string[]">
  Comma-separated list of dimensions to break the response down by. Combine
  `period` with `domain` or `email` for a joint breakdown (one row per unique
  `period` + `domain`/`email` pair). Defaults to `[]`, returning a single
  `totals` row for the whole range, with no `data`.

  Possible values:

  * `period`: one row per `granularity` period, in chronological order.
  * `domain`: one row per sending domain. Cannot be combined with `email`.
  * `email`: one row per email. Cannot be combined with `domain`.
</ParamField>

<ParamField type="string[]">
  Comma-separated list of sending domain IDs to restrict the response to.
  Unrecognized query params are ignored rather than rejected.
</ParamField>

<ParamField type="string[]">
  Comma-separated list of email IDs to restrict the response to. Cannot be
  combined with the `domain` dimension. Unrecognized query params are ignored
  rather than rejected.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/emails/metrics?start_date=2026-07-01&end_date=2026-07-08&metrics=sent,delivered,open_rate&dimensions=period,domain' \
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
    "dimensions": ["period", "domain"],
    "granularity": "daily",
    "totals": {
      "sent": 1204,
      "delivered": 1180,
      "open_rate": 50.0
    },
    "data": [
      {
        "period": "2026-07-01",
        "domain_id": "d91cd9bd-1176-4f47-2a4b-fce2d5399cbf",
        "domain_name": "example.com",
        "sent": 172,
        "delivered": 169,
        "open_rate": 49.7
      }
    ]
  }
  ```
</ResponseExample>
