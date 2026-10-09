---
title: "Retrieve Agent Settings"
source: https://resend.com/docs/api-reference/inboxes/get-agent
path: docs/api-reference/inboxes/get-agent
---

GET /inboxes/:inbox_id/agent
Retrieve the agent settings for an inbox.

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

An inbox without a configured agent returns empty settings.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `inbox_agent`.
</ParamField>

<ParamField type="string | null">
  Instructions the agent follows when handling the inbox's threads. `null` when
  no instructions are set.
</ParamField>

<ParamField type="string | null">
  Tone the agent writes in, such as `friendly and concise`. `null` when no tone
  is set.
</ParamField>

<ParamField type="string[]">
  Actions the agent is allowed to take. Each entry is one of `draft_reply`,
  `forward_thread`, `add_labels`, `assign_thread`, `mark_as_spam`,
  `archive_thread`, or `delete_thread`.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.agent.get({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/agent' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes agent get --inbox_id b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_agent",
    "instructions": "Answer refund questions yourself. Escalate legal threats.",
    "tone": "friendly and concise",
    "enabled_actions": ["draft_reply", "add_labels"]
  }
  ```
</ResponseExample>
