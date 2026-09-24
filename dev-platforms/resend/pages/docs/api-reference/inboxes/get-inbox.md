---
title: "Retrieve Inbox"
source: https://resend.com/docs/api-reference/inboxes/get-inbox
path: docs/api-reference/inboxes/get-inbox
---

GET /inboxes/:inbox_id
Retrieve a single inbox by its ID.

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

## Response Fields

<ParamField type="string">
  Always `inbox`.
</ParamField>

<ParamField type="string">
  The ID of the inbox.
</ParamField>

<ParamField type="string | null">
  Internal name for the inbox. Recipients do not see it.
</ParamField>

<ParamField type="string">
  The address of the inbox.
</ParamField>

<ParamField type="string | null">
  The address to forward mail to when forwarding is enabled. `null` otherwise.
</ParamField>

<ParamField type="string | null">
  The name recipients see when mail is sent from this inbox. A plain name, not
  a `Name <email>` address.
</ParamField>

<ParamField type="number">
  The number of unread threads in the inbox.
</ParamField>

<ParamField type="number">
  The number of unsent drafts.
</ParamField>

<ParamField type="string | null">
  ISO 8601 timestamp when a thread in this inbox was last active.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.get(
    'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes get b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox",
    "id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
    "name": "Customer Support",
    "email_address": "support@example.com",
    "forwarding_address": null,
    "friendly_name": "Ada from Support",
    "unread": 3,
    "drafts": 2,
    "last_received": "2026-08-05T14:03:11.229Z"
  }
  ```
</ResponseExample>
