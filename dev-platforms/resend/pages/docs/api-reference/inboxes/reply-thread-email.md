---
title: "Reply to Thread Email"
source: https://resend.com/docs/api-reference/inboxes/reply-thread-email
path: docs/api-reference/inboxes/reply-thread-email
---

POST /inboxes/:inbox_id/threads/:thread_id/emails/:email_id/reply
Send a reply to a message in an inbox thread.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}} theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.33.0
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}} theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.25.0
    ```
  </CodeGroup>
</Warning>

Sends a reply from the inbox address.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID or the inbox email address, such as `support@example.com`.
</ResendParamField>

<ResendParamField type="string">
  The Thread ID.
</ResendParamField>

<ResendParamField type="string">
  The Email ID of the message to reply to, as returned by [List Thread
  Emails](/docs/api-reference/inboxes/list-thread-emails) in `data[].id`.
</ResendParamField>

## Body Parameters

<ParamField type="string | string[]">
  CC recipient email address.
</ParamField>

<ParamField type="string | string[]">
  BCC recipient email address.
</ParamField>

<ParamField type="string">
  The HTML body of the reply.
</ParamField>

<ParamField type="string">
  The plain-text body of the reply.
</ParamField>

<ParamField type="string">
  The subject of the reply. Max 2000 characters.
</ParamField>

<ResendParamField type="boolean">
  Reply to everyone on the original message.
</ResendParamField>

<ParamField type="array">
  Files to attach, as on [Send Email](/docs/api-reference/emails/send-email).

  <Expandable title="properties">
    <ParamField type="buffer | string">
      Content of an attached file, passed as a buffer or Base64 string.
    </ParamField>

    <ParamField type="string">
      Name of attached file.
    </ParamField>

    <ParamField type="string">
      Path where the attachment file is hosted.
    </ParamField>

    <ResendParamField type="string">
      Content type for the attachment. When not set, it is derived from the
      `filename`.
    </ResendParamField>

    <ResendParamField type="string">
      Content ID for embedding inline images with a `cid:` reference in the
      `html`. [Learn about inline images](/docs/dashboard/emails/embed-inline-images).
    </ResendParamField>
  </Expandable>
</ParamField>

<ParamField type="object">
  Custom headers to add to the email.
</ParamField>

## Headers

<ParamField type="string">
  Add an idempotency key to prevent duplicated emails.

  * Should be **unique per API request**
  * Idempotency keys expire after **24 hours**
  * Have a maximum length of **256 characters**
  * A retry with the same key returns the first successful response, with the
    `idempotent-replayed: true` header
  * A failed request is not stored, so you can retry it with the same key
  * Reusing the key with a different body, or while the first request is still
    running, returns a `409`

  [Learn more](/docs/dashboard/emails/idempotency-keys)
</ParamField>

## Response Fields

<ParamField type="string">
  The ID of the sent email. Use it with the [emails
  endpoints](/docs/api-reference/emails/retrieve-email).
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.threads.emails.reply({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
    emailId: '5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60',
    cc: ['billing@example.com'],
    bcc: ['records@example.com'],
    html: '<p>Refund issued for order 1041.</p>',
    text: 'Refund issued for order 1041.',
    attachments: [
      {
        path: 'https://resend.com/static/sample/invoice.pdf',
        filename: 'invoice.pdf',
      },
    ],
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/emails/5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60/reply' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "cc": ["billing@example.com"],
    "bcc": ["records@example.com"],
    "html": "<p>Refund issued for order 1041.</p>",
    "text": "Refund issued for order 1041.",
    "attachments": [
      {
        "path": "https://resend.com/static/sample/invoice.pdf",
        "filename": "invoice.pdf"
      }
    ]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes threads emails reply b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60 \
    --cc billing@example.com \
    --bcc records@example.com \
    --html "<p>Refund issued for order 1041.</p>" \
    --text "Refund issued for order 1041." \
    --attachment ./invoice.pdf
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "id": "6a0c8e58-3d9e-4f7a-8b14-2e3f4a5b6c71"
  }
  ```
</ResponseExample>
