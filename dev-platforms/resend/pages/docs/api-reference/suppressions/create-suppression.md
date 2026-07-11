---
title: "Create Suppression"
source: https://resend.com/docs/api-reference/suppressions/create-suppression
path: docs/api-reference/suppressions/create-suppression
---

POST /suppressions
Add an email address to the suppression list.

<Warning>
  The Suppressions API is currently in private beta and only available to a
  limited number of users. APIs might change before GA.

  <span />

  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.
</Warning>

## Body Parameters

<ParamField type="string">
  The email address to suppress.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/suppressions' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "email": "steve.wozniak@gmail.com"
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
