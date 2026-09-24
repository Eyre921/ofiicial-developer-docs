---
title: "Create Draft"
source: https://resend.com/docs/api-reference/inboxes/create-draft
path: docs/api-reference/inboxes/create-draft
---

POST /inboxes/:inbox_id/drafts
Create a draft on an inbox, either as a new conversation or as a reply.

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

A draft is an unsent message. Omit `thread_id` for a new conversation. Pass
`thread_id` and `reply_to_email_id` together to attach it as a reply.

At least one of `to`, `cc`, `bcc`, `subject`, `text`, or `html` must be
non-empty. Combined recipients cannot exceed 50. Returns `201` for a new draft,
or `200` if that reply draft already exists.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

## Body Parameters

<ParamField type="string | string[] | null">
  Recipients. Each value may include a friendly name, for example
  `Ada Lovelace <ada@example.org>`.
</ParamField>

<ParamField type="string | string[] | null">
  CC recipients.
</ParamField>

<ParamField type="string | string[] | null">
  BCC recipients.
</ParamField>

<ParamField type="string | null">
  The subject. Max 2000 characters.
</ParamField>

<ParamField type="string | null">
  The HTML body.
</ParamField>

<ParamField type="string | null">
  The plain-text body.
</ParamField>

<ResendParamField type="string">
  The Thread ID to reply in. Must be sent with `reply_to_email_id`.
</ResendParamField>

<ResendParamField type="string">
  The Email ID to reply to, as returned in the thread's `messages[].id`. Must be
  sent with `thread_id`.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `inbox_draft`.
</ParamField>

<ParamField type="string">
  The ID of the draft.
</ParamField>

<ParamField type="string">
  `standalone` for a new conversation, or `reply`.
</ParamField>

<ParamField type="string[] | null">
  Recipients.
</ParamField>

<ParamField type="string[]">
  CC recipients.
</ParamField>

<ParamField type="string[]">
  BCC recipients.
</ParamField>

<ParamField type="string | null">
  The subject.
</ParamField>

<ParamField type="string | null">
  The HTML body.
</ParamField>

<ParamField type="string | null">
  The plain-text body.
</ParamField>

<ParamField type="string | null">
  The Thread ID when this draft is a reply. `null` otherwise.
</ParamField>

<ParamField type="string | null">
  The Email ID being replied to. `null` otherwise.
</ParamField>

<ParamField type="string | null">
  The queued outbound email after send. `null` until then.
</ParamField>

<ParamField type="string">
  ISO 8601 timestamp when the draft was created.
</ParamField>

<ParamField type="string">
  ISO 8601 timestamp when the draft was last saved.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.drafts.create({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    to: ['ada@example.org'],
    subject: 'Refund for order 1041',
    html: '<p>Refund issued for order 1041.</p>',
    text: 'Refund issued for order 1041.',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/drafts' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "to": ["ada@example.org"],
    "subject": "Refund for order 1041",
    "html": "<p>Refund issued for order 1041.</p>",
    "text": "Refund issued for order 1041."
  }'
  ```

  ```bash Reply draft theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/drafts' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "thread_id": "4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12",
    "reply_to_email_id": "5b1a9f47-2c8d-4e6f-9a03-1d2e3f4a5b60",
    "text": "Refund issued for order 1041."
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes drafts create \
    --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --to ada@example.org \
    --subject "Refund for order 1041" \
    --html "<p>Refund issued for order 1041.</p>" \
    --text "Refund issued for order 1041."
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_draft",
    "id": "c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32",
    "type": "standalone",
    "to": ["ada@example.org"],
    "cc": [],
    "bcc": [],
    "subject": "Refund for order 1041",
    "html": "<p>Refund issued for order 1041.</p>",
    "text": "Refund issued for order 1041.",
    "thread_id": null,
    "reply_to_email_id": null,
    "email_id": null,
    "created_at": "2026-08-05T14:12:04.110Z",
    "updated_at": "2026-08-05T14:12:04.110Z"
  }
  ```
</ResponseExample>
