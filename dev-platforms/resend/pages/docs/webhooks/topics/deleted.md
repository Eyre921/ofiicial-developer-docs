---
title: "topic.deleted"
source: https://resend.com/docs/webhooks/topics/deleted
path: docs/webhooks/topics/deleted
---

Received when a topic is deleted.

Event triggered whenever a **topic is deleted**.

<ResponseBodyParameters type="topic.deleted">
  <ParamField type="string">
    Unique identifier for the topic
  </ParamField>

  <ParamField type="string">
    The topic name
  </ParamField>

  <ParamField type="string | null">
    The topic description
  </ParamField>

  <ParamField type="opt_in | opt_out">
    The default subscription preference for new contacts
  </ParamField>

  <ParamField type="boolean">
    Whether the topic was deleted
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the topic was created
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the topic was last updated
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "topic.deleted",
    "created_at": "2026-02-12T10:00:00.000Z",
    "data": {
      "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
      "name": "Product Updates",
      "description": "New features and improvements",
      "default_subscription": "opt_in",
      "deleted": true,
      "created_at": "2026-02-12T10:00:00.000Z",
      "updated_at": "2026-02-12T10:00:00.000Z"
    }
  }
  ```
</ResponseExample>
