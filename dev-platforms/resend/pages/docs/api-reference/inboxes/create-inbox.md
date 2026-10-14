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
`support@example.com`. The domain must belong to the team.

Without `forwarding`, the domain must have receiving enabled, with DKIM and SPF
verified and the inbound MX record verified or pending. With `forwarding` set to
`true`, the domain only needs DKIM and SPF verified for sending.

* A domain that does not meet these rules returns a `422` `validation_error`.
* An address or receiving address that is already in use returns a `409`.
* A team that has reached the inbox limit of its plan returns a `403`
  `validation_error`.
* A blocked account returns a `451`.

## Body Parameters

<ResendParamField type="string">
  The inbox email address on one of your domains. The API trims and lowercases
  it. The part before the `@` is at most 64 characters and contains only
  letters, numbers, and `. _ % + -`. It cannot start or end with a dot or
  contain two dots in a row.
</ResendParamField>

<ParamField type="string">
  Internal name for the inbox. Recipients do not see it. Max 64 characters.
  Defaults to `email_address`.
</ParamField>

<ResendParamField type="string">
  The name recipients see when mail is sent from this inbox. A plain name, not
  a `Name <email>` address. Max 78 characters. It cannot contain a colon, `<`,
  `>`, line breaks, or other control characters. An email address inside the
  name must be on a domain the team has verified for sending. An empty string
  leaves it unset.
</ResendParamField>

<ParamField type="boolean">
  When `true`, Resend provisions a receiving address so you can receive mail
  without adding an MX record. Read it from `receiving_address` with [Get
  Inbox](/docs/api-reference/inboxes/get-inbox). Defaults to `false`.
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
