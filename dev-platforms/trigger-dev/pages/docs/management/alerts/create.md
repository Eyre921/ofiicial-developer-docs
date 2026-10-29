---
title: "Create an alert"
source: https://trigger.dev/docs/management/alerts/create
path: docs/management/alerts/create
---

POST https://api.trigger.dev/api/v1/projects/{projectRef}/monitoring-alerts
Create a monitoring alert for a project, including Limits alerts.

> [!WARNING]
>
> **Private beta.** This feature is only available to some organizations right now.

Authenticate with a [personal access token](/docs/management/authentication).

## Body

**capabilityKey** `string` *required*

What to alert on. Use `limits.all` for a combined Limits alert, or a single limit such as `limits.api`,
`limits.concurrency`, `limits.queue`, `limits.webhooks.processing`,
`limits.webhooks.env_rate`, `limits.webhooks.endpoint_rate` or `limits.webhooks.waiters`.

**environment** `string` *required*

One of `dev`, `staging`, `prod` or `preview`.

**branch** `string`

Preview branch. Only valid when `environment` is `preview`.

**params** `object` *required*

**properties**

**windowSec** `number`

Evaluation window in seconds.

**condition** `object` *required*

For Limits alerts, set `kind` to `state` and `stateKey` to the same value as `capabilityKey`.

**properties**

**components** `string[]`

`limits.all` only. The limits to watch. Defaults to all of them. Values are the single limit
capability keys above.

**compositeMode** `"any" | "all"`

`limits.all` only. Raise when any selected limit is true, or only when all are.

**signals** `("approaching" | "limited")[]`

Which limit signals to watch. `approaching` means usage has reached the utilisation share;
`limited` means the limit is already affecting traffic. `limits.queue` only supports
`approaching`.

**params** `object`

Thresholds, for example `utilisationPct` (default 80, from 1 to 100).

**notifiers** `object[]` *required*

At least one notifier, for example `{ "type": "channel", "channelId": "..." }`.

**behavior** `object` *required*

Optional `expiresAt` (ISO 8601 date in the future).

**name** `string`

A name for the alert.

Invalid `components` or `signals` return a `400` with an error message.

## Examples

Watch every limit and raise when any is true:

```bash theme={"theme":"css-variables"}
curl -X POST "https://api.trigger.dev/api/v1/projects/proj_1234/monitoring-alerts" \
  -H "Authorization: Bearer $TRIGGER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "capabilityKey": "limits.all",
    "environment": "prod",
    "params": { "windowSec": 300 },
    "condition": {
      "kind": "state",
      "stateKey": "limits.all",
      "compositeMode": "any",
      "signals": ["approaching", "limited"],
      "params": { "utilisationPct": 80 }
    },
    "behavior": {},
    "notifiers": [{ "type": "channel", "channelId": "channel_1234" }]
  }'
```

Watch only the API rate limit, when usage reaches 90%:

```bash theme={"theme":"css-variables"}
curl -X POST "https://api.trigger.dev/api/v1/projects/proj_1234/monitoring-alerts" \
  -H "Authorization: Bearer $TRIGGER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "capabilityKey": "limits.api",
    "environment": "prod",
    "params": { "windowSec": 300 },
    "condition": {
      "kind": "state",
      "stateKey": "limits.api",
      "signals": ["approaching"],
      "params": { "utilisationPct": 90 }
    },
    "behavior": {},
    "notifiers": [{ "type": "channel", "channelId": "channel_1234" }]
  }'
```
