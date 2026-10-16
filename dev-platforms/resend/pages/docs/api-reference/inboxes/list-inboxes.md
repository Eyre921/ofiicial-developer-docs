---
title: "List Inboxes"
source: https://resend.com/docs/api-reference/inboxes/list-inboxes
path: docs/api-reference/inboxes/list-inboxes
---

GET /inboxes
Retrieve a list of inboxes for the team.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.33.0
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.25.0
    ```
  </CodeGroup>
</Warning>

Inboxes are returned newest first. Results are paginated with cursors. See
[Pagination](/docs/api-reference/pagination) for how `after` and `before` work. The
cursors take an inbox ID. A value that is not a UUID returns a `422`, and an
unknown ID returns a `404`.

The list items carry fewer fields than a single inbox. [Retrieve an
inbox](/docs/api-reference/inboxes/get-inbox) to get all its fields.

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
      The name recipients see when mail is sent from this inbox. `null` when
      not set.
    </ParamField>

    <ParamField type="number">
      The number of unread threads in the Inbox folder.
    </ParamField>

    <ParamField type="string | null">
      ISO 8601 timestamp of the newest received email in the Inbox folder.
      `null` when the folder has no received email.
    </ParamField>

    <ParamField type="string">
      ISO 8601 timestamp when the inbox was created.
    </ParamField>

    <ParamField type="string">
      ISO 8601 timestamp when the inbox was updated.
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
        "from_name": "Ada from Support",
        "unread": 3,
        "last_received": "2026-08-05T14:03:11.229Z",
        "created_at": "2026-08-01T09:12:44.512Z",
        "updated_at": "2026-08-03T16:20:05.004Z"
      },
      {
        "id": "1c5e0f3a-6b21-4d9a-8e77-5c0a9d8b4e12",
        "name": "billing@example.com",
        "email_address": "billing@example.com",
        "from_name": null,
        "unread": 0,
        "last_received": null,
        "created_at": "2026-07-20T11:00:00.000Z",
        "updated_at": "2026-07-20T11:00:00.318Z"
      }
    ]
  }
  ```
</ResponseExample>
