---
title: "inbox.created"
source: https://resend.com/docs/webhooks/inboxes/created
path: docs/webhooks/inboxes/created
---

Received when an inbox is created.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.32.1-preview-inboxes.4
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.6
    ```
  </CodeGroup>
</Warning>

Event triggered whenever an **inbox is created**.

<ResponseBodyParameters type="inbox.created">
  <ParamField type="api | dashboard | agent | system">
    What made the change
  </ParamField>

  <ParamField type="string">
    The ID of the inbox
  </ParamField>

  <ParamField type="object">
    The inbox, as it is when the webhook is sent

    <Expandable title="inbox object">
      <ParamField type="string">
        Always `inbox`
      </ParamField>

      <ParamField type="string">
        The ID of the inbox
      </ParamField>

      <ParamField type="string">
        Internal name for the inbox. Recipients do not see it. Falls back to the inbox
        address
      </ParamField>

      <ParamField type="string">
        The address of the inbox
      </ParamField>

      <ParamField type="string">
        The ID of the domain the inbox belongs to
      </ParamField>

      <ParamField type="string | null">
        The address to forward mail to when forwarding is enabled. `null` otherwise
      </ParamField>

      <ParamField type="string | null">
        The name recipients see when mail is sent from this inbox
      </ParamField>

      <ParamField type="number">
        The number of unread threads in the inbox
      </ParamField>

      <ParamField type="number">
        The number of unsent drafts
      </ParamField>

      <ParamField type="string | null">
        ISO 8601 timestamp when a thread in this inbox was last active
      </ParamField>

      <ParamField type="string">
        ISO 8601 timestamp when the inbox was created
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "inbox.created",
    "created_at": "2026-09-29T12:00:00.000Z",
    "data": {
      "source": "api",
      "inbox_id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
      "inbox": {
        "object": "inbox",
        "id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
        "name": "Customer Support",
        "email_address": "support@example.com",
        "domain_id": "d91cd9bd-1176-453e-8fc1-35364d380206",
        "receiving_address": null,
        "from_name": "Ada from Support",
        "unread": 0,
        "drafts": 0,
        "last_received": null,
        "created_at": "2026-09-29T12:00:00.000Z"
      }
    }
  }
  ```
</ResponseExample>
