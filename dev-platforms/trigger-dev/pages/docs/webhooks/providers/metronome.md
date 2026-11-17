---
title: "Metronome webhooks"
source: https://trigger.dev/docs/webhooks/providers/metronome
path: docs/webhooks/providers/metronome
---

Receive and verify Metronome webhooks with Trigger.dev. Check the HMAC-SHA256 signature in metronome-webhook-signature and run a task for each Metronome event, filtered on event.type.

**`webhooks.metronome()` verifies the HMAC-SHA256 signature Metronome sends in `metronome-webhook-signature` on every request.**

```ts /trigger/metronome.ts theme={"theme":"css-variables"}
import { webhook, webhooks } from "@trigger.dev/sdk";

export const metronome = webhooks.endpoint.define({
  id: "metronome",
  source: webhooks.metronome(),
});

export const metronomeEvents = webhook({
  id: "metronome-events",
  endpoint: metronome,
  onEvent: async ({ event }) => {
    console.log(event);
  },
});
```

To run a subscriber only for some events, add a [filter](/docs/webhooks/filters) on `event.type`.

| Setting | Value |
| - | - |
| Source | `webhooks.metronome()` |
| Verification | HMAC-SHA256 in `metronome-webhook-signature` |
| Credential | Signing secret issued by Metronome |
| Event type | `event.type` |
| Metronome docs | [Metronome webhook docs](https://docs.metronome.com/guides/platform-configuration/setup-webhooks) |

## Set up Metronome

1. Start `trigger dev` or deploy, then copy the endpoint's **Webhook URL** from the **Webhooks** page.
2. In the Metronome app, go to **Developer > Notifications > Webhooks > Add** and enter the webhook URL.
3. Copy the webhook's secret key, then choose **Set signing secret** on the Trigger.dev endpoint.
4. Create the notifications your subscribers need, such as a low credit balance alert, under **Developer > Notifications > Create Notification**.
5. Send a test event from Metronome, or use the endpoint's **Test** tab, and check the endpoint's **Deliveries** tab. See [Verify the connection](/docs/webhooks/connect#verify-the-connection) if nothing arrives.
