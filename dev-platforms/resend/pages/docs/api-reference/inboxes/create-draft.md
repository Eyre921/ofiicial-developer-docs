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

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.33.0
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.25.0
    ```
  </CodeGroup>
</Warning>

A draft is an unsent message. Omit `thread_id` and `reply_to_email_id` for a
draft that starts a new thread. Pass both together for a reply draft in an
existing thread.

A reply draft without `to` is addressed to the sender of the email it replies
to, or to its Reply-To when set. For an email the inbox sent, it defaults to
that email's `to` recipients. Send `to: []` to leave it empty. `cc`, `bcc`, and
`subject` are never filled in.

At least one of `to`, `cc`, `bcc`, `subject`, `text`, `html`, or `attachments`
must be non-empty. The combined recipients of `to`, `cc`, and `bcc` cannot
exceed 50.

Returns `201` for a new draft. Only one unsent reply draft can target an email,
so a reply draft request for an email that already has one returns `200` with
the ID of the existing draft. That request ignores every other field, except
`attachments`, which replaces the attachments of the existing draft.

A reply draft created without `subject` stores an empty subject and gets no
`Re:` prefix. Set a subject before you send it.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID. An email address is not accepted.
</ResendParamField>

## Body Parameters

<ParamField type="string | string[] | null">
  Recipients. For multiple addresses, send an array of strings. Each value can
  include a friendly name, for example `Ada Lovelace <ada@example.org>`.
</ParamField>

<ParamField type="string | string[] | null">
  CC recipients. For multiple addresses, send an array of strings.
</ParamField>

<ParamField type="string | string[] | null">
  BCC recipients. For multiple addresses, send an array of strings.
</ParamField>

<ParamField type="string | null">
  The subject. Max 2000 characters. A string that is only whitespace, or that
  contains a line break, is rejected.
</ParamField>

<ParamField type="string | null">
  The HTML body.
</ParamField>

<ParamField type="string | null">
  The plain-text body.
</ParamField>

<ParamField type="array">
  Files to store on the draft. Each one needs `content`, `filename`, and
  `content_type`. `path` and `content_id` return `422`. An empty file or a
  blocked file type, such as `.exe`, returns `422`. The files on a draft can
  total at most 25 MB. A file counts as
  draft content.

  <Expandable title="properties">
    <ParamField type="buffer | string">
      Content of an attached file, passed as a buffer or Base64 string.
    </ParamField>

    <ParamField type="string">
      Name of attached file.
    </ParamField>

    <ResendParamField type="string">
      Content type for the attachment.
    </ResendParamField>
  </Expandable>
</ParamField>

<ResendParamField type="string">
  The Thread ID to reply in. Must be sent with `reply_to_email_id`.
</ResendParamField>

<ResendParamField type="string">
  The Email ID to reply to, as returned by [List Thread
  Emails](/docs/api-reference/inboxes/list-thread-emails) in `data[].id`. Must be
  sent with `thread_id`.
</ResendParamField>

## Headers

<ParamField type="string">
  Add an idempotency key to prevent duplicated drafts.

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
  Always `inbox_draft`.
</ParamField>

<ParamField type="string">
  The ID of the draft.
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
    attachments: [
      {
        filename: 'note.txt',
        content: 'aGVsbG8=',
        contentType: 'text/plain',
      },
    ],
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
    "text": "Refund issued for order 1041.",
    "attachments": [
      {
        "filename": "note.txt",
        "content": "aGVsbG8=",
        "content_type": "text/plain"
      }
    ]
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
  resend inboxes drafts create b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --to ada@example.org \
    --subject "Refund for order 1041" \
    --html "<p>Refund issued for order 1041.</p>" \
    --text "Refund issued for order 1041." \
    --attachment "./note.txt;type=text/plain"
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_draft",
    "id": "c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32"
  }
  ```
</ResponseExample>
