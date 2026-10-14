---
title: "Update Label"
source: https://resend.com/docs/api-reference/inboxes/update-label
path: docs/api-reference/inboxes/update-label
---

PATCH /inboxes/:inbox_id/labels/:label_id
Rename or recolor an existing label.

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

Omitted fields keep their current value. A new name must not match another
label on the inbox, compared without case, or the request returns a `422`
`validation_error`.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID. An email address is not accepted.
</ResendParamField>

<ResendParamField type="string">
  The Label ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  A new name for the label. Max 64 characters. Leading and trailing whitespace
  is trimmed.
</ParamField>

<ParamField type="string">
  A new color for the label as a `#RRGGBB` hex code, like `#E93D82`. It is
  stored in uppercase.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.labels.update({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    labelId: '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34',
    color: '#F76B15',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/labels/7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "color": "#F76B15"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes labels update b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34 \
    --color '#F76B15'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_label",
    "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34"
  }
  ```
</ResponseExample>
