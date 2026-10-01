---
title: "HubSpot"
source: https://elevenlabs.io/docs/reception-ai/integrations/hubspot.md
path: docs/reception-ai/integrations/hubspot
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# HubSpot

The HubSpot integration adds a summary of each conversation to the caller's contact in HubSpot. Your team sees what callers asked for without leaving your CRM.

## Connecting HubSpot

Go to **Integrations**, select **Add integration**, choose **HubSpot**, and select **Connect with HubSpot**. Sign in and approve access. Reception.ai only requests permission to read and write contacts.

## What gets synced

When a conversation ends, Reception.ai finds the HubSpot contact with the caller's phone number:

* If a contact matches, a note is added to its timeline with the conversation summary and a link to the conversation in Reception.ai.
* If no contact matches, a new contact is created. Only empty contact properties are filled in; existing values are never overwritten.

Under **What we sync**, choose which conversations to sync:

| Option                         | Default | Description                                                                       |
| ------------------------------ | ------- | --------------------------------------------------------------------------------- |
| **Phone calls**                | On      | Calls to your receptionist                                                        |
| **Conversations on your site** | On      | Web widget and booking page conversations where the visitor shared a phone number |

## Troubleshooting

If the connection stops working, the integration shows **HubSpot sync stopped working**. Select reconnect to sign in again and resume syncing.
