---
title: "Calendly"
source: https://elevenlabs.io/docs/reception-ai/integrations/calendly.md
path: docs/reception-ai/integrations/calendly
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Calendly

The Calendly integration makes Calendly your scheduling system. Your receptionist checks availability and books, reschedules, and cancels appointments directly in Calendly. Your Calendly event types appear as services in Reception.ai.

## Connecting Calendly

### Create a personal access token

In your Calendly account's API and webhooks settings, create a personal access token and copy it.

### Add the integration

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **Calendly**.

### Enter the token

Paste the token into **Personal Access Token** and select **Enable**.

To replace the token later, edit the integration and use **Rotate Personal Access Token**.

## What changes when Calendly is connected

Reception.ai turns on the features Calendly needs and hides the ones it replaces. Existing data is kept.

| Enabled                         | Hidden                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------ |
| Services, Appointments, Clients | Staff, Assets, Availability, Home and mobile services, Group sessions, Rentals |

These features can't be changed in **Settings** → **Features** while Calendly is connected. Disconnect Calendly to restore them.

Your Calendly scheduling settings, such as availability and notice periods, apply instead of Reception.ai's booking rules.

## Requirements and limits

* One Calendly account per workspace.
* Bookings require the client's email address, so your receptionist asks for it.
* Calendly limits how many bookings its API can create, for example 5 bookings per 24 hours on some Calendly accounts. When the limit is reached, the receptionist can't book through Calendly until the limit resets, which can take up to 24 hours.

If the token stops working, the integration shows that it needs reconnecting. Rotate the token to restore it.
