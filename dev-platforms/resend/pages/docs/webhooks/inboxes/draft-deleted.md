---
title: "inbox.draft.deleted"
source: https://resend.com/docs/webhooks/inboxes/draft-deleted
path: docs/webhooks/inboxes/draft-deleted
---

Received when a draft is discarded.

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

Event triggered whenever a **draft is discarded**.

*Note: The draft is already gone, so the payload has no `draft` object.*

<ResponseBodyParameters type="inbox.draft.deleted">
  <ParamField type="api | dashboard | agent | system">
    What made the change
  </ParamField>

  <ParamField type="string">
    The ID of the inbox
  </ParamField>

  <ParamField type="string">
    The ID of the thread. Only on reply drafts
  </ParamField>

  <ParamField type="string">
    The ID of the draft
  </ParamField>

  <ParamField type="object">
    The thread, as it is when the webhook is sent. Only on reply drafts

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
    "type": "inbox.draft.deleted",
    "created_at": "2026-09-29T12:00:00.000Z",
    "data": {
      "source": "dashboard",
      "inbox_id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
      "thread_id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
      "draft_id": "9a2b7c4d-1e3f-4a5b-8c6d-0e1f2a3b4c5d",
      "thread": {
        "object": "inbox_thread",
        "id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
        "subject": "Question about my invoice",
        "folder": "inbox",
        "labels": [],
        "read": false
      }
    }
  }
  ```
</ResponseExample>
