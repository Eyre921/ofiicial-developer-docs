---
title: "Retrieve Thread Email"
source: https://resend.com/docs/api-reference/inboxes/get-thread-email
path: docs/api-reference/inboxes/get-thread-email
---

GET /inboxes/:inbox_id/threads/:thread_id/emails/:email_id
Retrieve a single message from a thread.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/help?type=report\&message=I+would+like+early+access+to+Inboxes.\&priority=low) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.28.1-preview-inboxes.1
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.2
    ```
  </CodeGroup>
</Warning>

Returns one message of a thread, in the same shape [Retrieve
Thread](/docs/api-reference/inboxes/get-thread) returns inside `messages`.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

<ResendParamField type="string">
  The Thread ID.
</ResendParamField>

<ResendParamField type="string">
  The Email ID, as returned in the thread's `messages[].id`.
</ResendParamField>

## Response Fields

<ParamField type="string">
  The ID of the message.
</ParamField>

<ParamField type="string">
  Whether the message was received by the inbox or sent from it.
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
  The Reply-To addresses.
</ParamField>

<ParamField type="string | null">
  The subject of the message.
</ParamField>

<ParamField type="string | null">
  The Message-ID header of the message.
</ParamField>

<ParamField type="string | null">
  The HTML body.
</ParamField>

<ParamField type="string | null">
  The plain-text body.
</ParamField>

<ParamField type="array">
  The attachments on the message.

  <Expandable title="properties">
    <ParamField type="string">
      The ID of the attachment.
    </ParamField>

    <ParamField type="string | null">
      The filename of the attachment.
    </ParamField>

    <ParamField type="number | null">
      The size of the attachment in bytes.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField type="boolean">
  Whether the message has been read.
</ParamField>

<ParamField type="string">
  ISO 8601 timestamp when the message arrived or was sent.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.threads.emails.get({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
    emailId: '5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/emails/5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes threads emails get \
    --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --thread_id 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 \
    --email_id 5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "id": "5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60",
    "direction": "inbound",
    "from": "Ada Lovelace <ada@example.org>",
    "to": ["support@example.com"],
    "cc": [],
    "bcc": [],
    "reply_to": ["replies@example.org"],
    "subject": "Refund for order 1041",
    "message_id": "<1041@example.org>",
    "html": "<p>Could I get a refund for order 1041?</p>",
    "text": "Could I get a refund for order 1041?",
    "attachments": [
      {
        "id": "9d4f2b81-6c3a-4e7d-8b12-0a5c6d7e8f90",
        "filename": "receipt.pdf",
        "size": 20841
      }
    ],
    "read": false,
    "received_at": "2026-08-05T14:03:11.229Z"
  }
  ```
</ResponseExample>
