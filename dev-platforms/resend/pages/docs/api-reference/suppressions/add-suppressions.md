---
title: "Add Suppressions"
source: https://resend.com/docs/api-reference/suppressions/add-suppressions
path: docs/api-reference/suppressions/add-suppressions
---

POST /suppressions/batch/add
Add up to 100 email addresses to the suppression list at once.

<Warning>
  The Suppressions API is currently in private beta and only available to a
  limited number of users. APIs might change before GA.

  <span />

  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.
</Warning>

## Body Parameters

<ParamField type="array">
  The email addresses to suppress. Must contain between 1 and 100 email
  addresses.
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/suppressions/batch/add' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "emails": ["steve.wozniak@gmail.com", "bill.gates@microsoft.com"]
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "data": [
      {
        "object": "suppression",
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3"
      },
      {
        "object": "suppression",
        "id": "520784e2-887d-4c25-b53c-4ad46ad38100"
      }
    ]
  }
  ```
</ResponseExample>
