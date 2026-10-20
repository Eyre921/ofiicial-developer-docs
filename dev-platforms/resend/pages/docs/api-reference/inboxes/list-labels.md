---
title: "List Labels"
source: https://resend.com/docs/api-reference/inboxes/list-labels
path: docs/api-reference/inboxes/list-labels
---

GET /inboxes/:inbox_id/labels
Retrieve the labels on an inbox.

## Path Parameters

The Inbox ID or the inbox email address, such as `support@example.com`.

## Response Fields

**object** `string`

Always `list`.

**data** `array`

The labels on the inbox, oldest first.

**properties**

**id** `string`

The ID of the label.

**name** `string`

The name of the label.

**color** `string`

The color of the label as an uppercase `#RRGGBB` hex code, like
`#E93D82`.

**created\_at** `string`

ISO 8601 timestamp when the label was created.

```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.inboxes.labels.list({
  inboxId: 'b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1',
});
```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->inboxes->labels->list('b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1');
```

```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
curl -X GET 'https://api.resend.com/inboxes/b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1/labels' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```

```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
resend inboxes labels list b3e2b2b6-3f0e-4c8e-9ad3-2f43a1e2c7f1
```

```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "object": "list",
  "data": [
    {
      "id": "2a8b4c6d-1e3f-4a5b-9c7d-8e0f1a2b3c4d",
      "name": "Billing",
      "color": "#00A2C7",
      "created_at": "2026-08-01T09:12:03.004Z"
    },
    {
      "id": "7f9c1d2e-4a6b-4c3d-8e15-9b0a7c6d5e34",
      "name": "Urgent",
      "color": "#E93D82",
      "created_at": "2026-08-05T14:07:42.881Z"
    }
  ]
}
```
