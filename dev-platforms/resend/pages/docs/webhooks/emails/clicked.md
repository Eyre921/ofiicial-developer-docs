---
title: "email.clicked"
source: https://resend.com/docs/webhooks/emails/clicked
path: docs/webhooks/emails/clicked
---

Received when an email link is clicked.

Event triggered whenever the **recipient clicks on an email link**.

<ResponseBodyParameters type="email.clicked">
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

  <ParamField type="object">
    Click tracking details

    <Expandable title="click object">
      <ParamField type="string">
        IP address of the user who clicked the link
      </ParamField>

      <ParamField type="string">
        The URL that was clicked
      </ParamField>

      <ParamField type="string">
        ISO 8601 timestamp when the click occurred
      </ParamField>

      <ParamField type="string">
        User agent string of the browser that clicked the link
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "email.clicked",
    "created_at": "2026-11-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2026-11-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "message_id": "<111-222-333@email.example.com>",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "click": {
        "ipAddress": "122.115.53.11",
        "link": "https://resend.com",
        "timestamp": "2026-11-24T05:00:57.163Z",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
      },
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</ResponseExample>
