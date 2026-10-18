---
title: "Delete Draft"
source: https://resend.com/docs/api-reference/inboxes/delete-draft
path: docs/api-reference/inboxes/delete-draft
---

DELETE /inboxes/:inbox_id/drafts/:draft_id
Discard an unsent draft.

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

Discards an unsent draft. A draft that was already sent returns a `409`.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID or the inbox email address, such as `support@example.com`.
</ResendParamField>

<ResendParamField type="string">
  The Draft ID.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `inbox_draft`.
</ParamField>

<ParamField type="string">
  The ID of the draft.
</ParamField>

<ParamField type="boolean">
  Returns `true` when the draft is deleted.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.drafts.remove({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    draftId: 'c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X DELETE 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/drafts/c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes drafts delete b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32 \
    --yes
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_draft",
    "id": "c3a1e8b4-2d5f-4a7c-9e10-6b8d7f5a4c32",
    "deleted": true
  }
  ```
</ResponseExample>
