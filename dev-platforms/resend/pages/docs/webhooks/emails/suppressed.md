---
title: "email.suppressed"
source: https://resend.com/docs/webhooks/emails/suppressed
path: docs/webhooks/emails/suppressed
---

Received when an email is suppressed.

Event triggered whenever the **email is suppressed** by Resend.

<Info>
  Learn more about [suppressed
  emails](/docs/knowledge-base/why-are-my-emails-landing-on-the-suppression-list).
</Info>

<ResponseBodyParameters type="email.suppressed">
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
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "email.suppressed",
    "created_at": "2026-11-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2026-11-22T23:41:11.894Z",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "message_id": "<111-222-333@email.example.com>",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "suppressed": {
        "message": "Resend has suppressed sending to this address because it is on the account-level suppression list. This does not count toward your bounce rate metric",
        "type": "OnAccountSuppressionList"
      },
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</ResponseExample>
