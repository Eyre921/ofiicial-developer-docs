---
title: "Create Label"
source: https://resend.com/docs/api-reference/inboxes/create-label
path: docs/api-reference/inboxes/create-label
---

POST /inboxes/:inbox_id/labels
Create a label on an inbox.

A label is a named, colored tag that belongs to one inbox. An inbox can have at
most 100 labels. Label names are unique per inbox, compared without case. A
duplicate name returns a `422`.

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

## Body Parameters

**name** `string` *required*

The name of the label. Max 64 characters.

**color** `string`

The color of the label as a `#RRGGBB` hex code, like `#E93D82`. Defaults to a
random color.

## Response Fields

**object** `string`

Always `inbox_label`.

**id** `string`

The ID of the label.

```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.inboxes.labels.create({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
  name: 'Urgent',
  color: '#E93D82',
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->labels->create('b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1', [
  'name' => 'Urgent',
  'color' => '#E93D82',
]);
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X POST 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/labels' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "name": "Urgent",
  "color": "#E93D82"
}'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes labels create b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1 \
  --name Urgent \
  --color '#E93D82'
```

```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "object": "inbox_label",
  "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34"
}
```
