---
title: "inbox.thread.labels.updated"
source: https://resend.com/docs/webhooks/inboxes/thread-labels-updated
path: docs/webhooks/inboxes/thread-labels-updated
---

Received when a label is applied to or removed from a thread.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/help?type=report\&message=I+would+like+early+access+to+Inboxes.\&priority=low) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.28.1-preview-inboxes.2
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.2
    ```
  </CodeGroup>
</Warning>

Event triggered whenever a **label is applied to or removed from a thread**.

*Note: Moving a thread to a label can send both this event and `inbox.thread.folder.updated` for the same thread.*

*Note: Deleting a label doesn't send this event for the threads that had it.*

<ResponseBodyParameters type="inbox.thread.labels.updated">
  <ParamField type="array">
    The labels applied, each with an `id`, `name`, and `color`. One event carries one label
  </ParamField>

  <ParamField type="array">
    The labels removed, each with an `id`, `name`, and `color`. One event carries one label
  </ParamField>

  <ParamField type="api | dashboard | agent | system">
    What made the change
  </ParamField>

  <ParamField type="string">
    The ID of the inbox
  </ParamField>

  <ParamField type="string">
    The ID of the thread
  </ParamField>

  <ParamField type="object">
    The thread, as it is when the webhook is sent

    <Expandable title="thread object">
      <ParamField type="string">
        Always `inbox_thread`
      </ParamField>

      <ParamField type="string">
        The ID of the thread
      </ParamField>

      <ParamField type="string | null">
        The subject of the thread
      </ParamField>

      <ParamField type="inbox | archive | spam | sent | trash">
        The folder the thread lives in
      </ParamField>

      <ParamField type="array">
        The labels attached to the thread, each with an `id`, `name`, and `color`
      </ParamField>

      <ParamField type="boolean">
        True only when every message in the thread is read
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "inbox.thread.labels.updated",
    "created_at": "2026-09-29T12:00:00.000Z",
    "data": {
      "added": [
        {
          "id": "c0a8012e-3b4f-4d7a-9e21-5f6a7b8c9d0e",
          "name": "Billing",
          "color": "orange"
        }
      ],
      "removed": [],
      "source": "dashboard",
      "inbox_id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
      "thread_id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
      "thread": {
        "object": "inbox_thread",
        "id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
        "subject": "Question about my invoice",
        "folder": "inbox",
        "labels": [
          {
            "id": "c0a8012e-3b4f-4d7a-9e21-5f6a7b8c9d0e",
            "name": "Billing",
            "color": "orange"
          }
        ],
        "read": false
      }
    }
  }
  ```
</ResponseExample>
