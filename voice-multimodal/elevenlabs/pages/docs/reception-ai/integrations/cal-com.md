---
title: "Cal.com"
source: https://elevenlabs.io/docs/reception-ai/integrations/cal-com.md
path: docs/reception-ai/integrations/cal-com
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Cal.com

The Cal.com integration makes Cal.com your scheduling system. Your receptionist checks availability and books, reschedules, and cancels appointments directly in Cal.com. Your Cal.com event types appear as services in Reception.ai.

## Connecting Cal.com

### Create an API key

In Cal.com, go to **Settings** → **Developer** → **API keys**, select **Add**, and copy the key.

### Add the integration

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **Cal.com**.

### Enter the key

Paste the key into **API key** and select **Enable**.

To replace the key later, edit the integration and use **Rotate API key**.

## What changes when Cal.com is connected

Like [Calendly](/docs/reception-ai/integrations/calendly#what-changes-when-calendly-is-connected), connecting Cal.com hides Reception.ai's staff, assets, availability, and booking page, and locks those features until you disconnect. Existing data is kept. Your Cal.com scheduling settings apply instead of Reception.ai's booking rules.

## Limits

* One Cal.com account per workspace.
* A booking's service or duration can't be changed after it is created. Cancel it and book again instead. Rescheduling to a new time is supported.
