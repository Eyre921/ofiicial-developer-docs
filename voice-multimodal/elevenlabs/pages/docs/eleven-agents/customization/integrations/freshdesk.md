---
title: "Freshdesk"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/freshdesk.md
path: docs/eleven-agents/customization/integrations/freshdesk
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Freshdesk

## Overview

Connect your ElevenLabs AI agents with Freshdesk to drive customer support workflows. The integration covers two scopes:

* **Tools**: let an agent look up tickets and contacts, search the helpdesk, post replies and internal notes, and create new tickets while a conversation is running.
* **Triggers**: have an agent automatically respond to new tickets or customer replies on existing tickets, posted back as an admin reply through the Freshdesk Conversations API.

## Setup

#### Get your Freshdesk API key

In Freshdesk, click your profile picture (top-right) → **Profile settings**. Your API key is shown below the change-password section. Copy it.

#### Find your Freshdesk subdomain

It's the part of your portal URL before `.freshdesk.com`. For example, if your portal is `acme.freshdesk.com`, your subdomain is `acme`.

#### Connect in ElevenLabs

In the ElevenLabs Freshdesk integration page, click **Connect** and provide:

* **API Key**: the token from step 1.
* **Subdomain**: the slug from step 2.

ElevenLabs authenticates with HTTP Basic auth using your API key as the username and `X` as the password — the standard Freshdesk authentication scheme.

#### Enable the trigger (optional)

If you want the agent to respond automatically to customer activity on tickets, enable the **Freshdesk Ticket Event** trigger and select:

* **Agent**: the agent that should handle incoming conversations.
* **Responder**: the Freshdesk agent identity the bot posts replies as.

When you activate the trigger, ElevenLabs creates a Freshdesk automation rule in your account that POSTs to our webhook on ticket creation and customer reply. Deactivating removes the rule. No manual Freshdesk admin steps are required.

**Automation rule ordering for new tickets.** Freshdesk runs **Ticket Creation** automation rules
top to bottom and executes only the **first** rule whose conditions match a new ticket — it then
stops. If you already have one or more Ticket Creation rules that match the same tickets and sit
**above** the ElevenLabs rule, our rule will never fire and the agent won't respond to new
tickets. If that happens, open **Admin → Workflows → Automations → Ticket Creation** and move the
`ElevenLabs agent …` rule above any conflicting rule. (Ticket-reply triggers use the **Ticket
Updates** category, where all matching rules run, so this only affects responses to brand-new
tickets.)

### CLI

CLI documentation for this integration is coming soon.

### SDK

SDK documentation for this integration is coming soon.

## Useful links

* [Freshdesk REST API reference](https://developers.freshdesk.com/api/)
* [Freshdesk search query syntax](https://developers.freshdesk.com/api/#filter_tickets)
* [Freshdesk automation rules with webhooks](https://support.freshdesk.com/en/support/solutions/articles/132589-using-webhooks-in-automation-rules-that-run-on-ticket-updates)
