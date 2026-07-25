---
title: "suppression.added"
source: https://resend.com/docs/webhooks/suppressions/added
path: docs/webhooks/suppressions/added
---

Received when an email address is added to your suppression list.

Event triggered whenever an **email address is added to your suppression
list**. Addresses are added automatically after a hard bounce or spam
complaint, or manually through the dashboard or API.

<ResponseBodyParameters type="suppression.added">
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
    "type": "suppression.added",
    "created_at": "2026-11-17T19:32:22.980Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "email": "steve.wozniak@gmail.com",
      "origin": "bounce",
      "source_id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
      "created_at": "2026-11-17T19:32:22.980Z"
    }
  }
  ```
</ResponseExample>
