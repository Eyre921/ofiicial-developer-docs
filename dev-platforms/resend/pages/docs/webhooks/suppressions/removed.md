---
title: "suppression.removed"
source: https://resend.com/docs/webhooks/suppressions/removed
path: docs/webhooks/suppressions/removed
---

Received when an email address is removed from your suppression list.

Event triggered whenever an **email address is removed from your suppression
list**.

<ResponseBodyParameters type="suppression.removed">
  <ParamField type="string">
    Unique identifier for the suppression
  </ParamField>

  <ParamField type="string">
    The suppressed email address
  </ParamField>

  <ParamField type="string">
    How the address was suppressed: `bounce`, `complaint`, or `manual`
  </ParamField>

  <ParamField type="string | null">
    ID of the email that triggered the suppression. For suppressions with a
    `manual` origin, `source_id` is `null`
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the suppression was created
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "suppression.removed",
    "created_at": "2026-11-17T19:32:22.980Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "email": "steve.wozniak@gmail.com",
      "origin": "manual",
      "source_id": null,
      "created_at": "2026-11-15T08:12:45.120Z"
    }
  }
  ```
</ResponseExample>
