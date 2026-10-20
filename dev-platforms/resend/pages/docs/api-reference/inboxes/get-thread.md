---
title: "Retrieve Thread"
source: https://resend.com/docs/api-reference/inboxes/get-thread
path: docs/api-reference/inboxes/get-thread
---

GET /inboxes/:inbox_id/threads/:thread_id
Retrieve a thread summary.

The response is the thread summary. Messages are listed separately with [List
Thread Emails](/docs/api-reference/inboxes/list-thread-emails).

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

The Thread ID.

## Response Fields

**object** `string`

Always `inbox_thread`.

**id** `string`

The ID of the thread.

**subject** `string | null`

The subject of the thread.

**folder** `string`

The folder the thread lives in. Every thread sits in exactly one folder within
its inbox. You can move a thread to `inbox`, `archive`, `spam`, or `trash`.
`sent` is assigned automatically.

* `inbox`: The default. The thread holds at least one received message.
* `archive`: The thread was archived.
* `spam`: The thread was marked as spam.
* `trash`: The thread is scheduled for deletion in 30 days.
* `sent`: Threads whose messages are all outbound.

**labels** `array`

The labels attached to the thread.

**properties**

**id** `string`

The ID of the label.

**name** `string`

The name of the label.

**color** `string`

The color of the label as an uppercase `#RRGGBB` hex code.

**read** `boolean`

True only when every message in the thread is read.

```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.inboxes.threads.get({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->threads->get(
  'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12'
);
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X GET 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes threads get b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12
```

```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "object": "inbox_thread",
  "id": "4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12",
  "subject": "Refund for order 1041",
  "folder": "inbox",
  "labels": [
    {
      "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34",
      "name": "Urgent",
      "color": "#E93D82"
    }
  ],
  "read": false
}
```
