---
title: "inbox.email.received"
source: https://resend.com/docs/webhooks/inboxes/email-received
path: docs/webhooks/inboxes/email-received
---

Received when an inbound email is added to a thread.

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

Event triggered whenever an **inbound email is added to a thread**.

*Note: `source` is always `system`, because the email pipeline sends this event, even when the API or an agent sent the email.*

<ResponseBodyParameters type="inbox.email.received">
  <ParamField type="api | dashboard | agent | system">
    What made the change
  </ParamField>

  <ParamField type="string">
    The ID of the inbox
  </ParamField>

  <ParamField type="string">
    The ID of the thread
  </ParamField>

  <ParamField type="string">
    The ID of the email
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

  <ParamField type="object">
    The email, as it is when the webhook is sent, without `html` or `text`. Fetch the body with [Retrieve Thread Email](/docs/api-reference/inboxes/get-thread-email)

    <Expandable title="email object">
      <ParamField type="string">
        The ID of the email
      </ParamField>

      <ParamField type="inbound | outbound">
        Whether the email was received by the inbox or sent from it
      </ParamField>

      <ParamField type="string">
        Sender email address
      </ParamField>

      <ParamField type="string[]">
        The recipients of the email
      </ParamField>

      <ParamField type="string[]">
        The CC recipients of the email
      </ParamField>

      <ParamField type="string[]">
        The BCC recipients of the email
      </ParamField>

      <ParamField type="string[]">
        The Reply-To addresses
      </ParamField>

      <ParamField type="string | null">
        The subject of the email
      </ParamField>

      <ParamField type="string | null">
        The Message-ID header of the email
      </ParamField>

      <ParamField type="array">
        The attachments on the email

        <Expandable title="attachment object">
          <ParamField type="string">
            The ID of the attachment
          </ParamField>

          <ParamField type="string | null">
            The filename of the attachment
          </ParamField>

          <ParamField type="number | null">
            The size of the attachment in bytes
          </ParamField>
        </Expandable>
      </ParamField>

      <ParamField type="boolean">
        Whether the email has been read
      </ParamField>

      <ParamField type="string">
        ISO 8601 timestamp when the email arrived or was sent
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "inbox.email.received",
    "created_at": "2026-09-29T12:00:00.000Z",
    "data": {
      "source": "system",
      "inbox_id": "b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1",
      "thread_id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
      "email_id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
      "thread": {
        "object": "inbox_thread",
        "id": "7c1f0a2e-5d3b-4e8a-9f61-2b8d4c6e1a90",
        "subject": "Question about my invoice",
        "folder": "inbox",
        "labels": [],
        "read": false
      },
      "email": {
        "id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
        "direction": "inbound",
        "from": "Steve Wozniak <steve.wozniak@gmail.com>",
        "to": ["support@example.com"],
        "cc": [],
        "bcc": [],
        "reply_to": [],
        "subject": "Question about my invoice",
        "message_id": "<CAF7c1f0a2e5d3b@mail.gmail.com>",
        "attachments": [
          {
            "id": "2a0c9ce0-3112-4728-976e-47ddcd16a318",
            "filename": "invoice.pdf",
            "size": 48213
          }
        ],
        "read": false,
        "received_at": "2026-09-29T12:00:00.000Z"
      }
    }
  }
  ```
</ResponseExample>
