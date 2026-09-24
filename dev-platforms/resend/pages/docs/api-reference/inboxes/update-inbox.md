---
title: "Update Inbox"
source: https://resend.com/docs/api-reference/inboxes/update-inbox
path: docs/api-reference/inboxes/update-inbox
---

PATCH /inboxes/:inbox_id
Update the internal inbox name or the name recipients see when sending.

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

At least one of `name` or `friendly_name` is required.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  New internal name for the inbox. Recipients do not see it.
</ParamField>

<ResendParamField type="string">
  The name recipients see when mail is sent from this inbox. A plain name, not
  a `Name <email>` address.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.update(
    'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    { name: 'Customer Support', friendlyName: 'Ada from Support' },
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "name": "Customer Support",
    "friendly_name": "Ada from Support"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes update b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --name "Customer Support" \
    --friendly_name "Ada from Support"
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox",
    "id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1"
  }
  ```
</ResponseExample>
