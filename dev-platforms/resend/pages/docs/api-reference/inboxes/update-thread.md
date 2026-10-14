---
title: "Update Thread"
source: https://resend.com/docs/api-reference/inboxes/update-thread
path: docs/api-reference/inboxes/update-thread
---

PATCH /inboxes/:inbox_id/threads/:thread_id
Mark a thread read or unread, move it, or add and remove labels.

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

At least one of `read`, `folder`, `add_label_ids`, or `remove_label_ids` is
required. A label ID cannot be both added and removed in the same request.
Moving a thread out of `trash` restores it and clears its deletion deadline.

The changes apply in this order: `read`, `folder`, added labels, removed labels.
They are not atomic, so a `404` for a label leaves the earlier changes applied.
A body with none of these keys returns a `422`, even when it has other keys.

## Path Parameters

<ResendParamField type="string">
  The Inbox ID. An email address is not accepted.
</ResendParamField>

<ResendParamField type="string">
  The Thread ID.
</ResendParamField>

## Body Parameters

<ParamField type="boolean">
  Marks every message in the thread read or unread.
</ParamField>

<ParamField type="string">
  Moves the thread to this folder. One of `inbox`, `archive`, `spam`, or
  `trash`. `sent` is assigned automatically and cannot be set.
</ParamField>

<ResendParamField type="string[]">
  Applies these labels to the thread. Between 1 and 10 label IDs. A label ID
  cannot appear in both `add_label_ids` and `remove_label_ids`. A label ID that
  does not exist in the inbox returns a `404`.
</ResendParamField>

<ResendParamField type="string[]">
  Takes these labels off the thread. Between 1 and 10 label IDs. The labels
  themselves are kept and stay on every other thread carrying them. A label ID
  that does not exist in the inbox returns a `404`.
</ResendParamField>

## Folders

Every thread sits in exactly one folder within its inbox.

| Folder | Meaning |
| - | - |
| `inbox` | The default. The thread holds at least one received message. |
| `archive` | The thread was archived. |
| `spam` | The thread was marked as spam. |
| `trash` | The thread is scheduled for deletion in 30 days. |
| `sent` | Threads whose messages are all outbound. |

You can move a thread to `inbox`, `archive`, `spam`, or `trash`. `sent` is
assigned automatically.

## Response Fields

<ParamField type="string">
  Always `inbox_thread`.
</ParamField>

<ParamField type="string">
  The ID of the thread.
</ParamField>

<ParamField type="string | null">
  The subject of the thread.
</ParamField>

<ParamField type="string">
  The folder the thread lives in after the update.
</ParamField>

<ParamField type="array">
  The labels attached to the thread, each with an `id`, `name`, and `color`.
</ParamField>

<ParamField type="boolean">
  True only when every message in the thread is read.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.inboxes.threads.update({
    inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
    threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
    read: true,
    folder: 'spam',
  });
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "read": true,
    "folder": "spam"
  }'
  ```

  ```bash Restore a trashed thread theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "folder": "inbox"
  }'
  ```

  ```bash Apply a label theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "add_label_ids": ["7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34"]
  }'
  ```

  ```bash Swap labels theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "add_label_ids": ["7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34"],
    "remove_label_ids": ["2c6a8e4b-1d3f-4a5c-9b7e-0f1a2b3c4d5e"]
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend inboxes threads update b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 \
    --read \
    --folder spam
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "inbox_thread",
    "id": "4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12",
    "subject": "Refund for order 1041",
    "folder": "spam",
    "labels": [],
    "read": true
  }
  ```
</ResponseExample>
