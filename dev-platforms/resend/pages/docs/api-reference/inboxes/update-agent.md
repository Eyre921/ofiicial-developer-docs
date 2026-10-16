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
    npm install resend@6.33.0
    ```

    ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli@2.25.0
    ```
  </CodeGroup>
</Warning>

## Path Parameters

<ResendParamField type="string">
  The Inbox ID. An email address is not accepted.
</ResendParamField>

## Body Parameters

<ParamField type="string | null">
  Instructions the agent follows when handling the inbox's threads. Max 4000
  characters.
</ParamField>

<ParamField type="'concise_professional' | 'concise_casual' | 'expanded_professional' | 'expanded_casual' | null">
  Tone the agent writes in. Send `null` to clear it.

  * `concise_professional`: Brief responses in a professional tone.
  * `concise_casual`: Brief responses in a casual tone.
  * `expanded_professional`: Detailed responses in a professional tone.
  * `expanded_casual`: Detailed responses in a casual tone.
</ParamField>

<ParamField type="string[]">
  Actions the agent is allowed to take.

  * `draft_reply`: Draft a reply.
  * `forward_thread`: Forward a thread.
  * `add_labels`: Add labels to a thread.
  * `assign_thread`: Assign a thread.
  * `mark_as_spam`: Mark a thread as spam.
  * `archive_thread`: Archive a thread.
  * `delete_thread`: Delete a thread.
</ParamField>

## Response Fields

<ParamField type="string">
  Always `inbox_agent`.
</ParamField>

<ParamField type="string">
  The ID of the agent.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.agent.update({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    instructions: 'Answer refund questions yourself. Escalate legal threats.',
    tone: 'concise_professional',
    actions: ['draft_reply', 'add_labels'],
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/agent' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "instructions": "Answer refund questions yourself. Escalate legal threats.",
    "tone": "concise_professional",
    "actions": ["draft_reply", "add_labels"]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes agent update b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
    --instructions "Answer refund questions yourself. Escalate legal threats." \
    --tone concise_professional \
    --actions draft_reply,add_labels
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
