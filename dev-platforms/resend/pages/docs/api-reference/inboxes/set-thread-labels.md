---
title: "Set Thread Labels"
source: https://resend.com/docs/api-reference/inboxes/set-thread-labels
path: docs/api-reference/inboxes/set-thread-labels
---

PUT /inboxes/:inbox_id/threads/:thread_id/labels
Replace every label on a thread.

The thread ends up with exactly the labels given, in one atomic change. Labels
on the thread that are not listed are taken off, and the labels themselves are
kept. If any label ID is not found, the request returns a `404` and nothing
changes.

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

The Thread ID.

## Body Parameters

**labels** `string[]` *required*

The IDs of the labels the thread should carry. Up to 100 IDs, each belonging
to the inbox. Pass an empty array to take every label off the thread.

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

const { data, error } = await resend.inboxes.threads.labels.set({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  threadId: '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
  labels: ['2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d'],
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->threads->labels->set(
  'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  '4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12',
  [
    'labels' => ['2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d'],
  ]
);
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X PUT 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/labels' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "labels": ["2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d"]
}'
```

```bash Clear all labels theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X PUT 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/threads/4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12/labels' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "labels": []
}'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes threads labels set b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 4d8e2a1c-9b3f-4c6d-8a21-3e5f7c9c0d12 \
  --labels 2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d
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
