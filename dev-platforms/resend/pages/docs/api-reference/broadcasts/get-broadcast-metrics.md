---
title: "Retrieve Metrics"
source: https://resend.com/docs/api-reference/broadcasts/get-broadcast-metrics
path: docs/api-reference/broadcasts/get-broadcast-metrics
---

GET /broadcasts/:broadcast_id/metrics
Retrieve aggregate metrics for a broadcast.

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
    npm install resend@6.19.0-preview-headless-dashboard.3
    ```
  </CodeGroup>
</Warning>

Delivery and engagement counters for a single broadcast. Each counter reports a
`total` (the number of recipients) and a `percentage`. Opens and clicks are
reported as unique counts.

<Info>
  While a broadcast is still sending, percentages divide by the number of emails
  sent so far (delivered + bounced). Once the broadcast has finished, they
  divide by the full audience total. Suppressions are decided before sending, so
  they always divide by the full audience total.
</Info>

<Info>
  Responses are cached for up to 15 minutes, so requesting the same broadcast's
  metrics again may return slightly stale data within that window.
</Info>

## Path Parameters

<ResendParamField type="string">
  The broadcast ID.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `broadcast_metrics`.
</ParamField>

<ParamField type="string">
  The broadcast's ID.
</ParamField>

<ParamField type="string">
  The broadcast's status. See all available `status` types in [the Broadcasts
  overview](/docs/dashboard/broadcasts/introduction#understand-broadcast-statuses).
</ParamField>

<ParamField type="string">
  When the broadcast was created.
</ParamField>

<ParamField type="string | null">
  When the broadcast is or was scheduled to send. `null` if it was never
  scheduled.
</ParamField>

<ParamField type="string | null">
  When the broadcast started sending. `null` if it hasn't started.
</ParamField>

<ParamField type="number">
  The total number of recipients in the broadcast's audience.
</ParamField>

<ParamField type="number">
  The total number of recipients processed so far. Calculated as `delivered +
      bounced`.
</ParamField>

<ParamField type="number">
  The total number of recipients not yet processed. Calculated as `total` minus
  `sent` minus `suppressed`, floored at `0`.
</ParamField>

<ParamField type="object">
  The total number and percentage of emails accepted by the recipient's mail
  server. Shaped as `{ total, percentage }`.
</ParamField>

<ParamField type="object">
  The total number and percentage of recipients who opened, counted once
  per recipient. Shaped as `{ total, percentage }`.
</ParamField>

<ParamField type="object">
  The total number and percentage of recipients who clicked, counted once
  per recipient. Shaped as `{ total, percentage }`.
</ParamField>

<ParamField type="object">
  The total number and percentage of recipients who unsubscribed. Shaped as
  `{ total, percentage }`.
</ParamField>

<ParamField type="object">
  The total number and percentage of emails that bounced. Shaped as `{ total,
      percentage }`.
</ParamField>

<ParamField type="object">
  The total number and percentage of emails marked as spam by the recipient.
  Shaped as `{ total, percentage }`.
</ParamField>

<ParamField type="object">
  The total number and percentage of emails not sent because the recipient
  was suppressed. Shaped as `{ total, percentage }`.
</ParamField>

<ParamField type="array">
  Every link that was clicked, with per-link counts.

  <Expandable title="properties">
    <ParamField type="string">
      The URL that was clicked.
    </ParamField>

    <ParamField type="number">
      The total number of clicks on this link, including repeat clicks by
      the same recipient.
    </ParamField>

    <ParamField type="number">
      The total number of recipients who clicked this link, counted once
      per recipient.
    </ParamField>

    <ParamField type="number">
      The percentage of `unique_clicks` out of the same denominator used for
      the other counters.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.broadcasts.metrics(
    '559ac32e-9ef5-46fb-82a1-b76b840c0f7b',
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/broadcasts/559ac32e-9ef5-46fb-82a1-b76b840c0f7b/metrics' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "broadcast_metrics",
    "broadcast_id": "559ac32e-9ef5-46fb-82a1-b76b840c0f7b",
    "status": "sent",
    "created_at": "2026-12-01 19:32:22.980+00",
    "scheduled_at": "2026-12-02 19:32:22.980+00",
    "sent_at": "2026-12-02 19:32:22.980+00",
    "total": 1000,
    "sent": 995,
    "remaining": 0,
    "delivered": { "total": 945, "percentage": 94.5 },
    "opened": { "total": 500, "percentage": 50 },
    "clicked": { "total": 100, "percentage": 10 },
    "unsubscribed": { "total": 20, "percentage": 2 },
    "bounced": { "total": 50, "percentage": 5 },
    "complained": { "total": 10, "percentage": 1 },
    "suppressed": { "total": 5, "percentage": 0.5 },
    "clicked_links": [
      {
        "url": "https://resend.com/pricing",
        "clicks": 90,
        "unique_clicks": 65,
        "percentage": 6.5
      },
      {
        "url": "https://resend.com/docs",
        "clicks": 45,
        "unique_clicks": 35,
        "percentage": 3.5
      }
    ]
  }
  ```
</ResponseExample>
