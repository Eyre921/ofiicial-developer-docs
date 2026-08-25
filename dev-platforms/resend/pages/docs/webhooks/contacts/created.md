---
title: "contact.created"
source: https://resend.com/docs/webhooks/contacts/created
path: docs/webhooks/contacts/created
---

Received when a contact is created.

Event triggered whenever a **contact was successfully created**.

*Note: When importing multiple contacts using CSV, these events won't be triggered. [Contact support](https://resend.com/contact) if you have any questions.*

<ResponseBodyParameters type="contact.created">
  <ParamField type="string">
    Unique identifier for the contact
  </ParamField>

  <ParamField type="string">
    Unique identifier for the audience this contact belongs to
  </ParamField>

  <ParamField type="array">
    Array of segment IDs the contact belongs to
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the contact was created
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the contact was last updated
  </ParamField>

  <ParamField type="string">
    Contact's email address
  </ParamField>

  <ParamField type="string | null">
    Contact's first name. May be absent from the payload
  </ParamField>

  <ParamField type="string | null">
    Contact's last name. May be absent from the payload
  </ParamField>

  <ParamField type="boolean">
    Whether the contact has unsubscribed from all emails sent from your team
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "contact.created",
    "created_at": "2026-11-17T19:32:22.980Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "audience_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
      "segment_ids": ["78261eea-8f8b-4381-83c6-79fa7120f1cf"],
      "created_at": "2026-11-17T19:32:22.980Z",
      "updated_at": "2026-11-17T19:32:22.980Z",
      "email": "steve.wozniak@gmail.com",
      "first_name": null,
      "last_name": null,
      "unsubscribed": false
    }
  }
  ```
</ResponseExample>
