---
title: "Remove Suppressions"
source: https://resend.com/docs/api-reference/suppressions/remove-suppressions
path: docs/api-reference/suppressions/remove-suppressions
---

POST /suppressions/batch/remove
Remove up to 100 suppressions from the suppression list at once.

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

Provide either `emails` or `ids`, but not both.

<ParamField type="array">
  The email addresses to remove from the suppression list. Must contain between
  1 and 100 email addresses.
</ParamField>

<ParamField type="array">
  The suppression IDs to remove from the suppression list. Must contain between
  1 and 100 IDs.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  // Remove by email
  const { data, error } = await resend.suppressions.batch.remove({
    emails: ['steve.wozniak@example.com', 'susan.kare@example.com'],
  });

  // Remove by id
  const { data, error } = await resend.suppressions.batch.remove({
    ids: ['e169aa45-1ecf-4183-9955-b1499d5701d3'],
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by email
  curl -X POST 'https://api.resend.com/suppressions/batch/remove' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "emails": ["steve.wozniak@example.com", "susan.kare@example.com"]
  }'

  # Remove by id
  curl -X POST 'https://api.resend.com/suppressions/batch/remove' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "ids": ["e169aa45-1ecf-4183-9955-b1499d5701d3"]
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "data": [
      {
        "object": "suppression",
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "deleted": true
      }
    ]
  }
  ```
</ResponseExample>
