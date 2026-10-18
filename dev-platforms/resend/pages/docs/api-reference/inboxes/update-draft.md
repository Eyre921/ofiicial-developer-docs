---
title: "Update Draft"
source: https://resend.com/docs/api-reference/inboxes/update-draft
path: docs/api-reference/inboxes/update-draft
---

PATCH /inboxes/:inbox_id/drafts/:draft_id
Update an unsent draft.

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

Updates the content of an unsent draft. A draft that was already sent returns
a `409`.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID or the inbox email address, such as `support@example.com`.
</ResendParamField>

<ResendParamField type="string">
  The Draft ID.
</ResendParamField>

## Body Parameters

Send at least one field. Omitted fields keep their current value. A request
with `html` or `text` replaces both, and the one you leave out is saved as
`null`. After the update, the draft must still have at least one non-empty
field, and `to`, `cc`, and `bcc` combined cannot exceed 50 recipients.

<ParamField type="string | string[] | null">
  Recipients. Send `null` or `[]` to clear them.
</ParamField>

<ParamField type="string | string[] | null">
  CC recipients. Send `null` or `[]` to clear them.
</ParamField>

<ParamField type="string | string[] | null">
  BCC recipients. Send `null` or `[]` to clear them.
</ParamField>

<ParamField type="string | null">
  The subject. 1 to 2000 characters, with no line breaks. Send `null` to clear
  it.
</ParamField>

<ParamField type="string | null">
  The HTML body. Send `null` to clear it.
</ParamField>

<ParamField type="string | null">
  The plain-text body. Send `null` to clear it.
</ParamField>

<ParamField type="array | null">
  Files to store on the draft, up to 25 MB in total. Sending the field replaces
  every attachment on the draft. Send `null` or `[]` to remove them all. Drafts
  do not accept `path` or `content_id`.

  <Expandable title="properties">
    <ParamField type="buffer | string">
      Content of an attached file, passed as a buffer or Base64 string.
    </ParamField>

    <ParamField type="string">
      Name of attached file.
    </ParamField>

    <ResendParamField type="string">
      Content type for the attachment. Must be a valid MIME type, such as
      `application/pdf`.
    </ResendParamField>
  </Expandable>
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

  const { data, error } = await resend.inboxes.drafts.update({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    draftId: 'c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32',
    subject: 'Refund issued for order 1041',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/drafts/c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "subject": "Refund issued for order 1041"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes drafts update b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32 \
    --subject "Refund issued for order 1041"
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
