---
title: "List Attempts"
source: https://resend.com/docs/api-reference/webhooks/list-event-attempts
path: docs/api-reference/webhooks/list-event-attempts
---

GET /webhooks/:webhook_id/events/:event_id/attempts
Retrieve the delivery attempts for a single webhook event.

<Warning>
  Webhook events and delivery attempts are currently in private beta and only
  available to a limited number of users. APIs might change before it is
  generally available. [Get in touch](https://resend.com/contact) if you're
  interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.19.0-preview-headless-dashboard.4
    ```
  </CodeGroup>
</Warning>

## Path Parameters

<ParamField type="string">
  The Webhook ID.
</ParamField>

<ParamField type="string">
  The Webhook Event ID.
</ParamField>

## Query Parameters

<ParamField type="number">
  Number of attempts to return. Between `1` and `100`. Defaults to `20`.
</ParamField>

<ParamField type="string">
  The attempt ID to fetch the next page after.

  The `before` parameter is not supported for this endpoint.
</ParamField>

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="boolean">
  Whether more attempts exist beyond this page.
</ParamField>

<ParamField type="array">
  The delivery attempts for this event, most recent first.

  <Expandable title="properties">
    <ParamField type="string">
      The attempt ID.
    </ParamField>

    <ParamField type="number">
      The HTTP status code your endpoint returned for this attempt.
    </ParamField>

    <ParamField type="string">
      The response body your endpoint returned for this attempt.
    </ParamField>

    <ParamField type="string">
      When this attempt was sent.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.webhooks.events.attempts.list({
    eventId: 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
    webhookId: '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0/events/msg_1srOrx2ZWZBpBUvZwXKQmoEYga2/attempts' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        "http_status_code": 200,
        "response": "{\"ok\":true}",
        "sent_at": "2026-08-22T15:33:12.000Z"
      },
      {
        "id": "atmpt_2ZbUCwvGmIT4mLIN6d3Yz0Ainbd",
        "http_status_code": 500,
        "response": "Internal Server Error",
        "sent_at": "2026-08-22T15:28:05.000Z"
      }
    ]
  }
  ```
</ResponseExample>
