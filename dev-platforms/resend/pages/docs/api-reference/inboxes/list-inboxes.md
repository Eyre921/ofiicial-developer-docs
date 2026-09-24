---
title: "List Inboxes"
source: https://resend.com/docs/api-reference/inboxes/list-inboxes
path: docs/api-reference/inboxes/list-inboxes
---

GET /inboxes
Retrieve a list of inboxes for the authenticated user.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/help?type=report\&message=I+would+like+early+access+to+Inboxes.\&priority=low) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.28.1-preview-inboxes.1
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.2
    ```
  </CodeGroup>
</Warning>

Inboxes are returned newest first. Results are paginated with cursors. See
[Pagination](/docs/api-reference/pagination) for how `after` and `before` work.

<QueryParams type="inboxes" />

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="boolean">
  Whether more inboxes exist beyond this page.
</ParamField>

<ParamField type="array">
  The inboxes on this page.

  <Expandable title="properties">
    <ParamField type="string">
      The ID of the inbox.
    </ParamField>

    <ParamField type="string | null">
      Internal name for the inbox. Recipients do not see it.
    </ParamField>

    <ParamField type="string">
      The address of the inbox.
    </ParamField>

    <ParamField type="string | null">
      The name recipients see when mail is sent from this inbox. A plain name,
      not a `Name <email>` address.
    </ParamField>

    <ParamField type="number">
      The number of unread threads in the inbox.
    </ParamField>

    <ParamField type="string | null">
      ISO 8601 timestamp when a thread in this inbox was last active.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.list();
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/inboxes' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes list
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
        "name": "Customer Support",
        "email_address": "support@example.com",
        "friendly_name": "Ada from Support",
        "unread": 3,
        "last_received": "2026-08-05T14:03:11.229Z"
      },
      {
        "id": "1c5e0f3a-6b21-4d9a-8e77-5c0a9d8b4e12",
        "name": "billing@example.com",
        "email_address": "billing@example.com",
        "friendly_name": null,
        "unread": 0,
        "last_received": null
      }
    ]
  }
  ```
</ResponseExample>
