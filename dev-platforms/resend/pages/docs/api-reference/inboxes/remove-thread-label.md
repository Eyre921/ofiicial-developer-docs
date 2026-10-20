---
title: "Remove Thread Label"
source: https://resend.com/docs/api-reference/inboxes/remove-thread-label
path: docs/api-reference/inboxes/remove-thread-label
---

DELETE /inboxes/:inbox_id/threads/:thread_id/labels/:label_id
Take one label off a thread.

The label itself is kept, and stays on every other thread that carries it. To
delete the label everywhere, use
[Delete Label](/docs/api-reference/inboxes/delete-label).

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

The Thread ID.

The Label ID.

## Response Fields

**object** `string`

Always `list`.

**data** `array`

Every label on the thread after the change.

**properties**

**id** `string`

The ID of the label.

**name** `string`

The name of the label.

**color** `string`

The color of the label as an uppercase `#RRGGBB` hex code, like
`#E93D82`.

```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.inboxes.threads.labels.remove({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
  labelId: '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34',
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->threads->labels->remove(
  'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
  '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34'
);
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X DELETE 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/labels/7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes threads labels remove b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34
```

```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "object": "list",
  "data": [
    {
      "id": "2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d",
      "name": "Billing",
      "color": "#00A2C7"
    }
  ]
}
```
