---
title: "Zapier"
source: https://elevenlabs.io/docs/reception-ai/integrations/zapier.md
path: docs/reception-ai/integrations/zapier
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Zapier

The Zapier integration connects your receptionist to over 7,000 apps through Zapier's MCP (Model Context Protocol) server, including CRMs, email marketing, and project management tools.

## How it works

Unlike traditional Zapier automations with triggers and actions, Reception.ai connects to Zapier through MCP. Your receptionist and business assistant **call Zapier actions directly** during conversations, based on what the caller asks for.

## Setting up Zapier

### Create a Zapier MCP server

Go to [mcp.zapier.com](https://mcp.zapier.com), select **+ New MCP Server**, and choose **Other** as the client.

### Add actions

Add the Zapier actions you want your receptionist to use, such as creating a CRM contact or sending a Slack message.

### Generate a token

Open the **Connect** tab and select **Generate token**. Copy the token.

### Add the integration

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **Zapier**. Paste the token into **Secret Token** and select **Enable**. Leave **MCP URL** empty to use the default Zapier endpoint.

### Assign tools

Open the **Tools** tab. Reception.ai lists the available actions. Assign each to the **Client** (receptionist), the **Assistant**, or both, or select **Enable all**. Select **Refresh tools** after adding actions in Zapier.

## What you can do

Example automations your receptionist can trigger during a call:

| During a call...                      | Zapier action                      |
| ------------------------------------- | ---------------------------------- |
| Caller wants to join the mailing list | Add contact to Mailchimp           |
| New appointment booked                | Post a message in Slack            |
| Caller reports an issue               | Create a ticket in Zendesk or Jira |
| New client identified                 | Create a contact in Salesforce     |
| Caller requests a callback            | Create a task in Asana or Notion   |

Each workspace can connect one Zapier account. Zapier is available on every plan.
