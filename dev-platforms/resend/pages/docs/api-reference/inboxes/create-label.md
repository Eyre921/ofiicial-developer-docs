---
title: "Create Label"
source: https://resend.com/docs/api-reference/inboxes/create-label
path: docs/api-reference/inboxes/create-label
---

POST /inboxes/:inbox_id/labels
Create a label on an inbox.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.32.1-preview-inboxes.6
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.9
    ```
  </CodeGroup>
</Warning>

A label is a named, colored tag that belongs to one inbox.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  The name of the label.
</ParamField>

<ParamField type="string">
  The color of the label as a `#RRGGBB` hex code, like `#E93D82`. If you leave
  it out, Resend picks one for you.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.labels.create({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    name: 'Urgent',
    color: '#E93D82',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/labels' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "name": "Urgent",
    "color": "#E93D82"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes labels create \
    --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --name Urgent \
    --color '#E93D82'
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
