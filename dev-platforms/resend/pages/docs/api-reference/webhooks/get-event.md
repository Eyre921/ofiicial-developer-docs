---
title: "Retrieve Event"
source: https://resend.com/docs/api-reference/webhooks/get-event
path: docs/api-reference/webhooks/get-event
---

GET /webhooks/:webhook_id/events/:event_id
Retrieve the details of a single event delivered to a webhook.

<Warning>
  Webhook events and delivery attempts are currently in private beta and only
  available to a limited number of users. APIs might change before it is
  generally available. [Get in touch](https://resend.com/help) if you're
  interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.19.0-preview-headless-dashboard.7
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

## Response Fields

<ParamField type="string">
  Always `webhook_event`.
</ParamField>

<ParamField type="string">
  The event ID.
</ParamField>

<ParamField type="string">
  The event type, for example `email.sent`.
</ParamField>

<ParamField type="string">
  When the event was created.
</ParamField>

<ParamField type="string">
  Delivery status of the event to this webhook: `success`, `failed`,
  `attempting`, or `pending`.
</ParamField>

<ParamField type="string | null">
  When the next delivery attempt is scheduled. `null` once the event reaches
  `success` or `failed`.
</ParamField>

<ParamField type="object">
  The event payload that was sent to your endpoint.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.webhooks.events.get({
    eventId: 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2',
    webhookId: '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0/events/msg_1srOrx2ZWZBpBUvZwXKQmoEYga2' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "webhook_event",
    "id": "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
    "type": "email.sent",
    "created_at": "2026-08-22T15:28:00.000Z",
    "status": "attempting",
    "next_attempt_at": "2026-08-22T15:33:00.000Z",
    "payload": {
      "type": "email.sent",
      "created_at": "2026-08-22T15:28:00.000Z",
      "data": {
        "email_id": "571f1f42-1c2d-4b1f-8f8e-8b3b5b3b5b3b",
        "from": "onboarding@resend.dev",
        "to": ["delivered@resend.dev"],
        "subject": "Welcome",
        "created_at": "2026-08-22T15:27:59.000Z"
      }
    }
  }
  ```
</ResponseExample>
