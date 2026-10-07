---
title: "Forward Thread Email"
source: https://resend.com/docs/api-reference/inboxes/forward-thread-email
path: docs/api-reference/inboxes/forward-thread-email
---

POST /inboxes/:inbox_id/threads/:thread_id/emails/:email_id/forward
Forward a message in an inbox thread to new recipients.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.32.1-preview-inboxes.4
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.6
    ```
  </CodeGroup>
</Warning>

Forwards from the inbox address. `to` is required. The original message is
quoted under a forwarded-message banner.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

<ResendParamField type="string">
  The Thread ID.
</ResendParamField>

<ResendParamField type="string">
  The Email ID of the message to forward, as returned by [List Thread
  Emails](/docs/api-reference/inboxes/list-thread-emails) in `data[].id`.
</ResendParamField>

## Body Parameters

<ParamField type="string | string[]">
  Recipient email address. For multiple addresses, send as an array of strings.
  `to`, `cc`, and `bcc` combined cannot exceed 50 recipients.
</ParamField>

<ParamField type="string | string[]">
  CC recipient email address. For multiple addresses, send as an array of
  strings. Counts toward the 50-recipient limit with `to`.
</ParamField>

<ParamField type="string | string[]">
  BCC recipient email address. For multiple addresses, send as an array of
  strings. Counts toward the 50-recipient limit with `to`.
</ParamField>

<ParamField type="string">
  An HTML note sent above the quoted original.
</ParamField>

<ParamField type="string">
  A plain-text note sent above the quoted original.
</ParamField>

<ParamField type="string">
  The subject of the forward. When omitted, the thread subject is used, prefixed
  with `Fwd:` if it isn't already. Max 2000 characters.
</ParamField>

## Headers

<ParamField type="string">
  Add an idempotency key to prevent duplicated emails.

  * Should be **unique per API request**
  * Idempotency keys expire after **24 hours**
  * Have a maximum length of **256 characters**

  [Learn more](/docs/dashboard/emails/idempotency-keys)
</ParamField>

## Response Fields

<ParamField type="string">
  The ID of the queued outbound email.
</ParamField>

<ParamField type="string">
  The ID of the queued outbound email. Same value as `id`.
</ParamField>

<ParamField type="string">
  Always `outbound`.
</ParamField>

<ParamField type="string">
  Sender email address.
</ParamField>

<ParamField type="string[]">
  The recipients of the message.
</ParamField>

<ParamField type="string[]">
  The CC recipients of the message.
</ParamField>

<ParamField type="string[]">
  The BCC recipients of the message.
</ParamField>

<ParamField type="string[]">
  Always empty in this response.
</ParamField>

<ParamField type="string">
  The subject of the sent forward.
</ParamField>

<ParamField type="string | null">
  Always `null` in this response.
</ParamField>

<ParamField type="string | null">
  The HTML body, including the note and the quoted original.
</ParamField>

<ParamField type="string | null">
  The plain-text body, including the note and the quoted original.
</ParamField>

<ParamField type="array">
  Always empty in this response.
</ParamField>

<ParamField type="boolean">
  Always `true`.
</ParamField>

<ParamField type="string">
  ISO 8601 timestamp when the message was sent.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.threads.emails.forward({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
    emailId: '5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60',
    to: ['colleague@example.org'],
    cc: ['billing@example.com'],
    bcc: ['records@example.com'],
    text: 'Flagging this refund request for you.',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/emails/5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60/forward' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "to": ["colleague@example.org"],
    "cc": ["billing@example.com"],
    "bcc": ["records@example.com"],
    "text": "Flagging this refund request for you."
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes threads emails forward \
    --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --thread_id 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 \
    --email_id 5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60 \
    --to colleague@example.org \
    --text "Flagging this refund request for you."
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "id": "6a0c8e58-3d9e-4f7a-8b14-2e3f4a5b6c71",
    "email_id": "6a0c8e58-3d9e-4f7a-8b14-2e3f4a5b6c71",
    "direction": "outbound",
    "from": "support@example.com",
    "to": ["colleague@example.org"],
    "cc": ["billing@example.com"],
    "bcc": ["records@example.com"],
    "reply_to": [],
    "subject": "Fwd: Refund for order 1041",
    "message_id": null,
    "html": "<div>Flagging this refund request for you.<br>\n<br>\n---------- Forwarded message ---------<br>\nFrom: Ada Lovelace &lt;ada@example.org&gt;<br>\nDate: Wed, Aug 5, 2026 at 2:03 PM<br>\nSubject: Refund for order 1041<br>\nTo: support@example.com<br>\n<br>\nCould I get a refund for order 1041?</div>",
    "text": "Flagging this refund request for you.\n\n---------- Forwarded message ---------\nFrom: Ada Lovelace <ada@example.org>\nDate: Wed, Aug 5, 2026 at 2:03 PM\nSubject: Refund for order 1041\nTo: support@example.com\n\nCould I get a refund for order 1041?",
    "attachments": [],
    "read": true,
    "received_at": "2026-08-05T14:12:04.110Z"
  }
  ```
</ResponseExample>
