---
title: "Retrieve Metrics"
source: https://resend.com/docs/api-reference/segments/get-segment-metrics
path: docs/api-reference/segments/get-segment-metrics
---

GET /segments/metrics
Retrieve segment metrics.

<Warning>
  Segment metrics are currently in private beta and only available to a limited
  number of users. The response shape might change before GA. [Get in
  touch](https://resend.com/help) if you're interested in testing this
  feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.19.0-preview-headless-dashboard.7
    ```
  </CodeGroup>
</Warning>

Contact counts for your account, optionally broken down by segment. Works
across your whole account by default, or scoped to specific segments via
`segment_id`.

<Info>
  Responses are cached for up to 15 minutes, so repeating the same request may
  return slightly stale data within that window.
</Info>

All parameters are optional. With none, the response covers your whole account,
includes every metric, and returns only `totals`. There's no date range, so
counts are a point-in-time snapshot rather than a historical window.

## Query Parameters

<ListParamFormatNote />

<ResendParamField type="string[]">
  List of metrics to include in `totals` and `data`. Omit for all. See
  [Metrics](#metrics).
</ResendParamField>

<ResendParamField type="string[]">
  List of dimensions to break `data` down by. Omit for only `totals`, with no
  `data`.

  Possible values:

  * `segment`: one row per segment, using its current contact counts.
</ResendParamField>

<ResendParamField type="string[]">
  List of segment IDs. Narrows `totals` (and `data`, when requested) to just
  these segments, without double-counting contacts that belong to more than one.
</ResendParamField>

<Info>
  When `dimensions` includes `segment`, `data` is ordered by each segment's
  creation date, newest first.
</Info>

## Metrics

Every metric counts contacts, not emails.

| Metric          | Description                                              |
| --------------- | -------------------------------------------------------- |
| `all_contacts`  | Every contact. Sum of `subscribers` and `unsubscribers`. |
| `subscribers`   | Contacts with `unsubscribed` set to `false`.             |
| `unsubscribers` | Contacts with `unsubscribed` set to `true`.              |

<Info>
  `totals` counts each contact once. `data` counts a contact in every segment it
  belongs to.
</Info>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.segments.metrics({
    dimensions: ['segment'],
    metrics: ['all_contacts'],
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/segments/metrics?dimensions=segment&metrics=all_contacts' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "metrics",
    "metrics": ["all_contacts"],
    "dimensions": ["segment"],
    "totals": {
      "all_contacts": 12450
    },
    "data": [
      {
        "id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
        "name": "Registered Users",
        "all_contacts": 4300
      }
    ]
  }
  ```
</ResponseExample>
