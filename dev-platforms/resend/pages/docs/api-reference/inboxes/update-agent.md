---
title: "Update Agent Settings"
source: https://resend.com/docs/api-reference/inboxes/update-agent
path: docs/api-reference/inboxes/update-agent
---

PATCH /inboxes/:inbox_id/agent
Update the agent settings for an inbox.

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

At least one of `instructions`, `tone`, or `enabled_actions` is required.
Omitted fields keep their current value.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

## Body Parameters

<ParamField type="string | null">
  Instructions the agent follows when handling the inbox's threads. Max 4000
  characters and must not be an empty string. Send `null` to clear them.
</ParamField>

<ParamField type="string | null">
  Tone the agent writes in, such as `friendly and concise`. Max 64 characters
  and must not be an empty string. Send `null` to clear it.
</ParamField>

<ParamField type="string[]">
  Actions the agent is allowed to take. Replaces the whole set. Each entry must
  be one of `draft_reply`, `forward_thread`, `add_labels`, `assign_thread`,
  `mark_as_spam`, `archive_thread`, or `delete_thread`. Send an empty array to
  disable all actions.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.agent.update({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    instructions: 'Answer refund questions yourself. Escalate legal threats.',
    tone: 'friendly and concise',
    enabledActions: ['draft_reply', 'add_labels'],
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/agent' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "instructions": "Answer refund questions yourself. Escalate legal threats.",
    "tone": "friendly and concise",
    "enabled_actions": ["draft_reply", "add_labels"]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes agent update \
    --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --instructions "Answer refund questions yourself. Escalate legal threats." \
    --tone "friendly and concise" \
    --enabled_actions draft_reply,add_labels
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_agent",
    "id": "a1f84a4e-6f2b-4f0a-9c1d-8a2e5b3c7d90"
  }
  ```
</ResponseExample>
