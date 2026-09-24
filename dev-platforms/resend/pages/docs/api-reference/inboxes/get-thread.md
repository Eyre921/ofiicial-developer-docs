---
title: "Retrieve Thread"
source: https://resend.com/docs/api-reference/inboxes/get-thread
path: docs/api-reference/inboxes/get-thread
---

GET /inboxes/:inbox_id/threads/:thread_id
Retrieve a thread with its full message history.

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

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

<ResendParamField type="string">
  The Thread ID.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `inbox_thread`.
</ParamField>

<ParamField type="string">
  The ID of the thread.
</ParamField>

<ParamField type="string | null">
  The subject of the thread.
</ParamField>

<ParamField type="string">
  The folder the thread lives in. One of `inbox`, `archive`, `spam`, `sent`, or
  `trash`.
</ParamField>

<ParamField type="array">
  The labels attached to the thread, each with an `id`, `name`, and `color`.
</ParamField>

<ParamField type="boolean">
  True only when every message in the thread is read.
</ParamField>

<ParamField type="array">
  The thread's messages, oldest first. The full history is returned in one
  response.

  <Expandable title="properties">
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
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.threads.get({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes threads get \
    --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --thread_id 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_thread",
    "id": "4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12",
    "subject": "Refund for order 1041",
    "folder": "inbox",
    "labels": [
      {
        "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34",
        "name": "Urgent",
        "color": "crimson"
      }
    ],
    "read": false,
    "messages": [
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
    ]
  }
  ```
</ResponseExample>
