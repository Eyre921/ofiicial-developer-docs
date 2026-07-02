---
title: "contact.updated"
source: https://resend.com/docs/webhooks/contacts/updated
path: docs/webhooks/contacts/updated
---

Received when a contact is updated.

Event triggered whenever a **contact was successfully updated**.

<ResponseBodyParameters type="contact.updated">
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

  <ParamField type="string">
    Contact's first name
  </ParamField>

  <ParamField type="string">
    Contact's last name
  </ParamField>

  <ParamField type="boolean">
    Whether the contact has unsubscribed from all emails sent from your team
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "contact.updated",
    "created_at": "2026-10-11T23:47:56.678Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "audience_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
      "segment_ids": ["78261eea-8f8b-4381-83c6-79fa7120f1cf"],
      "created_at": "2026-10-10T15:11:54.110Z",
      "updated_at": "2026-10-11T23:47:56.678Z",
      "email": "steve.wozniak@gmail.com",
      "first_name": "Steve",
      "last_name": "Wozniak",
      "unsubscribed": false
    }
  }
  ```
</ResponseExample>
