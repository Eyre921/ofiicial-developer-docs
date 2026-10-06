---
title: "inbox.deleted"
source: https://resend.com/docs/webhooks/inboxes/deleted
path: docs/webhooks/inboxes/deleted
---

Received when an inbox is deleted.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.32.1-preview-inboxes.2
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.4
    ```
  </CodeGroup>
</Warning>

Event triggered whenever an **inbox is deleted**.

<ResponseBodyParameters type="inbox.deleted">
  <ParamField type="api | dashboard | agent | system">
    What made the change
  </ParamField>

  <ParamField type="string">
    The ID of the inbox
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "inbox.deleted",
    "created_at": "2026-09-29T12:00:00.000Z",
    "data": {
      "source": "api",
      "inbox_id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1"
    }
  }
  ```
</ResponseExample>
