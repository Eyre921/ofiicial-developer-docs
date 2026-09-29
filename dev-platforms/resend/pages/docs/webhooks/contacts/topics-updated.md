---
title: "contact.topics.updated"
source: https://resend.com/docs/webhooks/contacts/topics-updated
path: docs/webhooks/contacts/topics-updated
---

Received when a contact's topic subscriptions change.

Event triggered whenever a **contact's topic subscriptions change**.

<ResponseBodyParameters type="contact.topics.updated">
  <ParamField type="string">
    Contact's email address
  </ParamField>

  <ParamField type="array">
    Topics changed in this update, each with its new subscription

    <Expandable title="topic object">
      <ParamField type="string">
        Unique identifier for the topic
      </ParamField>

      <ParamField type="opt_in | opt_out">
        The contact's new subscription to the topic
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "contact.topics.updated",
    "created_at": "2026-02-12T10:00:00.000Z",
    "data": {
      "email": "steve.wozniak@gmail.com",
      "topics": [
        {
          "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
          "subscription": "opt_in"
        },
        {
          "id": "07d84122-7224-4881-9c31-1c048e204602",
          "subscription": "opt_out"
        }
      ]
    }
  }
  ```
</ResponseExample>
