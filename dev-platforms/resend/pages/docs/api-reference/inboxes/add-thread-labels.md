---
title: "Add Thread Labels"
source: https://resend.com/docs/api-reference/inboxes/add-thread-labels
path: docs/api-reference/inboxes/add-thread-labels
---

POST /inboxes/:inbox_id/threads/:thread_id/labels
Apply one or more labels to a thread.

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

Labels already on the thread stay on it. If any label ID is not found, the
request returns a `404` and nothing changes. To replace the thread's labels
instead, use [Set Thread Labels](/docs/api-reference/inboxes/set-thread-labels).

## Path Parameters

<ResendParamField type="string">
  The Inbox ID or the inbox email address, such as `support@example.com`.
</ResendParamField>

<ResendParamField type="string">
  The Thread ID.
</ResendParamField>

## Body Parameters

<ParamField type="string[]">
  The IDs of the labels to apply. Between 1 and 10 IDs, each belonging to the
  inbox.
</ParamField>

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="array">
  Every label on the thread after the change.

  <Expandable title="properties">
    <ParamField type="string">
      The ID of the label.
    </ParamField>

    <ParamField type="string">
      The name of the label.
    </ParamField>

    <ParamField type="string">
      The color of the label as an uppercase `#RRGGBB` hex code, like
      `#E93D82`.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.threads.labels.add({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
    labels: ['7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34'],
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/labels' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "labels": ["7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34"]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes threads labels add b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 \
    --labels 7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "data": [
      {
        "id": "2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d",
        "name": "Billing",
        "color": "#00A2C7"
      },
      {
        "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34",
        "name": "Urgent",
        "color": "#E93D82"
      }
    ]
  }
  ```
</ResponseExample>
