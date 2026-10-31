---
title: "Integrations"
source: https://elevenlabs.io/docs/reception-ai/integrations/overview.md
path: docs/reception-ai/integrations/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Integrations

Integrations connect your receptionist to your calendar, CRM, phone system, and custom tools.

## Available integrations

| Integration                                                                   | Category   | What it does                                                          |
| ----------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------- |
| [Google Calendar](/docs/reception-ai/integrations/google-calendar)            | Scheduling | Syncs staff calendars for real-time availability                      |
| [Calendly](/docs/reception-ai/integrations/calendly)                          | Scheduling | Books appointments through your Calendly account                      |
| [Cal.com](/docs/reception-ai/integrations/cal-com)                            | Scheduling | Books appointments through your Cal.com account                       |
| [HubSpot](/docs/reception-ai/integrations/hubspot)                            | CRM        | Logs conversation summaries on HubSpot contacts                       |
| [Twilio](/docs/reception-ai/phone-numbers/bring-your-own-number#twilio)       | Telephony  | Use numbers from your own Twilio account                              |
| [SIP Trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk) | Telephony  | Use numbers from your carrier or PBX                                  |
| [Zapier](/docs/reception-ai/integrations/zapier)                              | Automation | Connects your receptionist to 7,000+ apps through Zapier's MCP server |
| [Webhook Tool](/docs/reception-ai/integrations/webhooks)                      | Developer  | Custom HTTP tools your receptionist can call during conversations     |
| [MCP Server](/docs/reception-ai/integrations/mcp-server)                      | Developer  | Connects custom tool servers                                          |

All integrations are available on every plan, including the free trial.

## Setup guides

These services have no built-in integration, but you can connect them with a SIP trunk, a webhook tool, an MCP server, or Zapier. They take more setup, so they appear after the built-in integrations in the catalog. Selecting one opens its guide.

| Guide                                                      | Category      | Connects through        |
| ---------------------------------------------------------- | ------------- | ----------------------- |
| [RingCentral](/docs/reception-ai/integrations/ringcentral) | Telephony     | Call forwarding or SIP  |
| [Telnyx](/docs/reception-ai/integrations/telnyx)           | Telephony     | SIP trunk               |
| [Plivo](/docs/reception-ai/integrations/plivo)             | Telephony     | SIP trunk               |
| [Ozonetel](/docs/reception-ai/integrations/ozonetel)       | Telephony     | Call forwarding or SIP  |
| [n8n](/docs/reception-ai/integrations/n8n)                 | Automation    | Webhook tool or MCP     |
| [Make](/docs/reception-ai/integrations/make)               | Automation    | Webhook tool            |
| [Pipedrive](/docs/reception-ai/integrations/pipedrive)     | CRM           | Webhook tools           |
| [Jotform](/docs/reception-ai/integrations/jotform)         | Forms         | Webhook tools           |
| [Monday.com](/docs/reception-ai/integrations/monday)       | Productivity  | Webhook tools           |
| [Asana](/docs/reception-ai/integrations/asana)             | Productivity  | Zapier and webhook tool |
| [Airtable](/docs/reception-ai/integrations/airtable)       | Productivity  | Webhook tools           |
| [Stripe](/docs/reception-ai/integrations/stripe)           | Payments      | MCP server              |
| [Slack](/docs/reception-ai/integrations/slack)             | Communication | Webhook tool            |
| [Mailchimp](/docs/reception-ai/integrations/mailchimp)     | Communication | Webhook tool            |
| [Shopify](/docs/reception-ai/integrations/shopify)         | E-commerce    | MCP server              |
| [Supabase](/docs/reception-ai/integrations/supabase)       | Developer     | Webhook tools           |

## Adding an integration

Go to **Integrations** and select **Add integration** to browse the catalog by category. Select an integration to open its settings, then select **Enable**. Most integrations have **Settings**, **Tools**, and **About** tabs.

Some integrations in the catalog are marked as coming soon. Select **I'm interested** to register interest, or **Request an integration** to suggest one that isn't listed.

## Tool assignment

Zapier, webhook, and MCP integrations provide tools. Each tool can be assigned to:

* **Receptionist**: used during calls and website conversations with your customers.
* **Assistant**: used by the [business assistant](/docs/reception-ai/features/assistant) in the dashboard.

This keeps customer-facing tools separate from internal management tools.

#### [Google Calendar](/docs/reception-ai/integrations/google-calendar)

Sync staff availability in real time.

#### [HubSpot](/docs/reception-ai/integrations/hubspot)

Log conversations to your CRM.

#### [Zapier](/docs/reception-ai/integrations/zapier)

Connect to thousands of apps.

#### [Webhooks](/docs/reception-ai/integrations/webhooks)

Custom HTTP tools for your receptionist.
