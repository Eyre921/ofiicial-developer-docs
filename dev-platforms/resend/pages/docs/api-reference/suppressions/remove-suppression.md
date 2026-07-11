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

  <span />

  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.
</Warning>

## Path Parameters

<ParamField type="email | id">
  The Suppression ID or email address.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Remove by suppression id
  curl -X DELETE 'https://api.resend.com/suppressions/e169aa45-1ecf-4183-9955-b1499d5701d3' \
       -H 'Authorization: Bearer re_xxxxxxxxx'

  # Remove by email
  curl -X DELETE 'https://api.resend.com/suppressions/steve.wozniak@gmail.com' \
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
