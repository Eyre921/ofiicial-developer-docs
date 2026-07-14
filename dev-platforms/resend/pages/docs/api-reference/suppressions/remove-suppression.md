---
title: "Remove Suppression"
source: https://resend.com/docs/api-reference/suppressions/remove-suppression
path: docs/api-reference/suppressions/remove-suppression
---

DELETE /suppressions/:suppression
Remove a single suppression by ID or email.

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

## Path Parameters

<ParamField type="email | id">
  The Suppression ID or email address.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  // Remove by suppression id
  const { data, error } = await resend.suppressions.remove(
    'e169aa45-1ecf-4183-9955-b1499d5701d3',
  );

  // Remove by email
  const { data, error } = await resend.suppressions.remove(
    'steve.wozniak@example.com',
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by suppression id
  curl -X DELETE 'https://api.resend.com/suppressions/e169aa45-1ecf-4183-9955-b1499d5701d3' \
       -H 'Authorization: Bearer re_xxxxxxxxx'

  # Remove by email
  curl -X DELETE 'https://api.resend.com/suppressions/steve.wozniak@example.com' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "suppression",
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
    "deleted": true
  }
  ```
</ResponseExample>
