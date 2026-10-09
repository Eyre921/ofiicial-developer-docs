---
title: "inbox.draft.updated"
source: https://resend.com/docs/webhooks/inboxes/draft-updated
path: docs/webhooks/inboxes/draft-updated
---

Received when a draft is edited.

<Warning>
  Inboxes are currently in private beta and only available to a limited
  number of users. The response shape might change before GA.

  <span />

  [Get early access](https://resend.com/settings/labs) if you're interested in testing this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the new methods:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.32.1-preview-inboxes.6
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.22.0-preview-inboxes.9
    ```
  </CodeGroup>
</Warning>

Event triggered whenever a **draft is edited**.

<ResponseBodyParameters type="inbox.draft.updated">
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

  <ParamField type="object">
    The draft, as it is when the webhook is sent, without `html` or `text`. Fetch the body with [Retrieve Draft](/docs/api-reference/inboxes/get-draft)

    <Expandable title="draft object">
      <ParamField type="string">
        Always `inbox_draft`
      </ParamField>

      <ParamField type="string">
        The ID of the draft
      </ParamField>

      <ParamField type="standalone | reply">
        `standalone` for a new conversation, or `reply`
      </ParamField>

      <ParamField type="string[] | null">
        Recipients
      </ParamField>

      <ParamField type="string[]">
        CC recipients
      </ParamField>

      <ParamField type="string[]">
        BCC recipients
      </ParamField>

      <ParamField type="string | null">
        The subject
      </ParamField>

      <ParamField type="string | null">
        The Thread ID when this draft is a reply. `null` otherwise
      </ParamField>

      <ParamField type="string | null">
        The Email ID being replied to. `null` otherwise
      </ParamField>

      <ParamField type="string | null">
        The queued outbound email after send. `null` until then
      </ParamField>

      <ParamField type="string">
        ISO 8601 timestamp when the draft was created
      </ParamField>

      <ParamField type="string">
        ISO 8601 timestamp when the draft was last saved
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "inbox.draft.updated",
    "created_at": "2026-09-29T12:00:00.000Z",
    "data": {
      "source": "agent",
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
      },
      "draft": {
        "object": "inbox_draft",
        "id": "9a2b7c4d-1e3f-4a5b-8c6d-0e1f2a3b4c5d",
        "type": "reply",
        "to": ["steve.wozniak@gmail.com"],
        "cc": [],
        "bcc": [],
        "subject": "Re: Question about my invoice",
        "thread_id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
        "reply_to_email_id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
        "email_id": null,
        "created_at": "2026-09-29T11:58:00.000Z",
        "updated_at": "2026-09-29T12:00:00.000Z"
      }
    }
  }
  ```
</ResponseExample>
