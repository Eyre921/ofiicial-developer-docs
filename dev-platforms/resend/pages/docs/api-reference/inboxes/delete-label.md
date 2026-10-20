---
title: "Delete Label"
source: https://resend.com/docs/api-reference/inboxes/delete-label
path: docs/api-reference/inboxes/delete-label
---

DELETE /inboxes/:inbox_id/labels/:label_id
Remove an existing label from an inbox.

Deletes the label and removes it from every thread that carries it.

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

The Label ID.

## Response Fields

**object** `string`

Always `inbox_label`.

**id** `string`

The ID of the label.

**deleted** `boolean`

Returns `true` when the label is deleted.

```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.inboxes.labels.remove({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  labelId: '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34',
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->labels->remove(
  'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34'
);
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X DELETE 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/labels/7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes labels delete b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34 \
  --yes
```

```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "object": "inbox_label",
  "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34",
  "deleted": true
}
```
