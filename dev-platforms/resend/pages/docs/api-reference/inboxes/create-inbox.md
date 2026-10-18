---
title: "Create Inbox"
source: https://resend.com/docs/api-reference/inboxes/create-inbox
path: docs/api-reference/inboxes/create-inbox
---

POST /inboxes
Create an inbox to send, receive and organize email.

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

An inbox sends and receives email at an address on one of your domains, such as
`support@example.com`.

Without `forwarding`, the domain must have receiving enabled, with DKIM and SPF
verified and the inbound MX record verified or pending. With `forwarding` set to
`true`, the domain needs only DKIM and SPF verified. Otherwise, the request
returns a `422`. An address that is already in use
returns a `409`. A team at the inbox limit of its plan gets a `403`.

## Body Parameters

<ResendParamField type="string">
  The inbox email address on one of your verified domains. The part before the
  `@` can contain only letters, numbers, and `.`, `_`, `%`, and `-`, up to 64
  characters. It cannot start or end with `.` or have two `.` in a row. To call
  an inbox with a `%` in its address, use the Inbox ID in the path.
</ResendParamField>

<ParamField type="string">
  Internal name for the inbox. Recipients do not see it. Max 64 characters.
  Defaults to `email_address`.
</ParamField>

<ResendParamField type="string">
  The name recipients see when mail is sent from this inbox. Use a plain name,
  without `:`, `<`, `>`, or line breaks. Max 78 characters. An email address in
  the name must be on one of your verified domains.
</ResendParamField>

<ParamField type="boolean">
  When `true`, Resend provisions a receiving address so you can receive mail
  without adding an MX record. Read it from `receiving_address` with [Get
  Inbox](/docs/api-reference/inboxes/get-inbox).
</ParamField>

## Response Fields

<ParamField type="string">
  Always `inbox`.
</ParamField>

<ParamField type="string">
  The ID of the inbox.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.create({
    emailAddress: 'support@example.com',
    name: 'Customer Support',
    fromName: 'Ada from Support',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "email_address": "support@example.com",
    "name": "Customer Support",
    "from_name": "Ada from Support"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes create \
    --email-address support@example.com \
    --name "Customer Support" \
    --from-name "Ada from Support"
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
