---
title: "email.received"
source: https://resend.com/docs/webhooks/emails/received
path: docs/webhooks/emails/received
---

Received when an inbound email is received.

Event triggered whenever Resend **successfully receives an email**.

<Info>
  Webhooks do not include the email body, headers, or attachments, only their
  metadata. You must call the [Received emails
  API](/docs/api-reference/emails/retrieve-received-email) or the [Attachments
  API](/docs/api-reference/emails/list-received-email-attachments) to retrieve them.
  This design choice supports large attachments in serverless environments that
  have limited request body sizes.
</Info>

<ResponseBodyParameters type="email.received">
  <ParamField type="string">
    Unique identifier for the broadcast campaign (if applicable)
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the email was created
  </ParamField>

  <ParamField type="string">
    Unique identifier for the specific email
  </ParamField>

  <ParamField type="string">
    RFC Message-ID header value for the email
  </ParamField>

  <ParamField type="string">
    Sender's email address. For sent events, this matches the value passed at send time and may include a display name (e.g., `Name <email@domain.com>`). For received events, this is the bare email address only; the display name from the original `From:` header is preserved in `headers.from` on the [retrieve endpoint](/docs/api-reference/emails/retrieve-received-email).
  </ParamField>

  <ParamField type="array">
    Array of impacted recipient email addresses
  </ParamField>

  <ParamField type="string">
    Email subject line
  </ParamField>

  <ParamField type="string">
    Unique identifier for the template used (if applicable)
  </ParamField>

  <ParamField type="Record<string, string>">
    Object of tag key-value pairs associated with the email.

    Example:

    ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
    {
      "category": "welcome",
      "user_id": "1234567890"
    }
    ```
  </ParamField>

  <ParamField type="array">
    The recipient addresses the email was forwarded for, taken from the `for` clause of the message's `Received` headers.
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "email.received",
    "created_at": "2026-02-22T23:41:12.126Z",
    "data": {
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "created_at": "2026-02-22T23:41:11.894719+00:00",
      "from": "onboarding@resend.dev",
      "to": ["delivered@resend.dev"],
      "bcc": [],
      "cc": [],
      "received_for": ["forwarded@example.com"],
      "message_id": "<111-222-333@email.example.com>",
      "subject": "Sending this example",
      "attachments": [
        {
          "id": "2a0c9ce0-3112-4728-976e-47ddcd16a318",
          "filename": "avatar.png",
          "content_type": "image/png",
          "content_disposition": "inline",
          "content_id": "img001"
        }
      ]
    }
  }
  ```
</ResponseExample>
