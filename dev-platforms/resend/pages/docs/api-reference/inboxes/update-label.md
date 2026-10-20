---
title: "Update Label"
source: https://resend.com/docs/api-reference/inboxes/update-label
path: docs/api-reference/inboxes/update-label
---

PATCH /inboxes/:inbox_id/labels/:label_id
Rename or recolor an existing label.

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

The Label ID.

## Body Parameters

Omitted fields keep their current value.

**name** `string`

A new name for the label. Max 64 characters. A name that another label in the
inbox already uses, compared without case, returns a `422`.

**color** `string`

A new color for the label as a `#RRGGBB` hex code, like `#E93D82`.

## Response Fields

**object** `string`

Always `inbox_label`.

**id** `string`

The ID of the label.

```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.inboxes.labels.update({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  labelId: '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34',
  color: '#F76B15',
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->labels->update(
  'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  '7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34',
  ['color' => '#F76B15']
);
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X PATCH 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/labels/7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "color": "#F76B15"
}'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes labels update b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34 \
  --color '#F76B15'
```

```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "object": "inbox_label",
  "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34"
}
```
