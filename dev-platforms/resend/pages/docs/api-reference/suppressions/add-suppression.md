---
title: "Add Suppression"
source: https://resend.com/docs/api-reference/suppressions/add-suppression
path: docs/api-reference/suppressions/add-suppression
---

POST /suppressions
Add an email address to the suppression list.

<Warning>
  The Suppressions API is currently in private beta and only available to a
  limited number of users. APIs might change before GA.
  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.18.0-canary.0
    ```
  </CodeGroup>
</Warning>

## Body Parameters

<ParamField type="string">
  The email address to suppress.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.suppressions.add({
    email: 'steve.wozniak@example.com',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/suppressions' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "email": "steve.wozniak@example.com"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "suppression",
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3"
  }
  ```
</ResponseExample>
