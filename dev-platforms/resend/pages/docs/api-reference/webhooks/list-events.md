---
title: "List Events"
source: https://resend.com/docs/api-reference/webhooks/list-events
path: docs/api-reference/webhooks/list-events
---

GET /webhooks/:webhook_id/events
Retrieve a list of events delivered to a webhook.

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

## Query Parameters

<ParamField type="number">
  Number of events to return. Between `1` and `100`. Defaults to `20`.
</ParamField>

<ParamField type="string">
  The event ID to fetch the next page after.

  The `before` parameter is not supported for this endpoint.
</ParamField>

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="boolean">
  Whether more events exist beyond this page.
</ParamField>

<ParamField type="array">
  The events delivered to this webhook, most recent first.

  <Expandable title="properties">
    <ParamField type="string">
      The event ID. Use this to [retrieve its details](/docs/api-reference/webhooks/get-event)
      or [list its attempts](/docs/api-reference/webhooks/list-event-attempts).
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
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.webhooks.events.list({
    webhookId: '4dd369bc-aa82-4ff3-97de-514ae3000ee0',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0/events' \
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
        "id": "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        "type": "email.sent",
        "created_at": "2026-08-22T15:28:00.000Z",
        "status": "success"
      },
      {
        "id": "msg_1srOsB4mXhCqCVwAxYRNnpFZhb3",
        "type": "email.delivered",
        "created_at": "2026-08-22T15:27:42.000Z",
        "status": "failed"
      }
    ]
  }
  ```
</ResponseExample>
