---
title: "List Suppressions"
source: https://resend.com/docs/api-reference/suppressions/list-suppressions
path: docs/api-reference/suppressions/list-suppressions
---

GET /suppressions
Show all suppressions.

<Warning>
  The Suppressions API is currently in private beta and only available to a
  limited number of users. APIs might change before GA.

  <span />

  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.
</Warning>

<QueryParams type="suppressions" />

<ParamField type="bounce | complaint | manual">
  Filter suppressions by origin.

  Possible values:
  `bounce`: emails suppressed automatically after a bounce
  `complaint`: emails suppressed due to a user complaint
  `manual`: emails suppressed by your team manually
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/suppressions' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "email": "steve.wozniak@gmail.com",
        "origin": "manual",
        "source_id": null,
        "created_at": "2026-10-06T23:47:56.678Z"
      }
    ]
  }
  ```
</ResponseExample>
