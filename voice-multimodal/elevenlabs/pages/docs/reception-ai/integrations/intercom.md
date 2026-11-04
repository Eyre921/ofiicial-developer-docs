---
title: "Intercom"
source: https://elevenlabs.io/docs/reception-ai/integrations/intercom.md
path: docs/reception-ai/integrations/intercom
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Intercom

Connect Intercom's hosted [MCP server](/docs/reception-ai/integrations/mcp-server) so your receptionist can recognize callers who are your customers, check on their open conversations, and answer questions from your Help Center articles.

> **Warning**
>
> Conversations can contain private details. Tell your receptionist, in its instructions or a
> [procedure](/docs/reception-ai/receptionist/rules-and-procedures), to share conversation details
> only after confirming the caller is the contact, for example by matching their phone number or
> email.

## Setup

### Create a private app

In Intercom, open the **Developer Hub** and create a new app for your workspace. Open the app and go to **Configure** → **Authentication**, then copy the access token.

Check the app's permissions include reading users, companies, and conversations, plus reading articles. Add writing conversations only if you want your receptionist to leave internal notes.

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Value                                      |
| ---------------- | ------------------------------------------ |
| **Name**         | Intercom                                   |
| **Server type**  | Streamable HTTP                            |
| **Server URL**   | The URL for your workspace's region, below |
| **Secret Token** | Your access token                          |

| Workspace region                        | Server URL                        |
| --------------------------------------- | --------------------------------- |
| US (you sign in at app.intercom.com)    | `https://mcp.intercom.com/mcp`    |
| EU (you sign in at app.eu.intercom.com) | `https://mcp.eu.intercom.com/mcp` |

Select **Enable**. Reception.ai sends the token as a bearer token and lists Intercom's tools.

### Assign tools

Open the **Tools** tab and assign these to the **Client** (receptionist):

* `search_contacts` and `get_contact`: find the caller and their details.
* `search_conversations` and `get_conversation`: check the status of the caller's requests.
* `search_articles` and `get_article`: answer questions from your Help Center.

Optionally, assign `add_internal_note` so your receptionist can add a summary of the call to the caller's conversation. Notes are only visible to your team. Leave `create_article` and `update_article` unassigned.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by calling from a number saved on a test contact and asking about an open conversation.

## Limitations

Intercom's MCP server doesn't support workspaces hosted in Australia.

## Troubleshooting

| Problem                              | What to check                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| No tools are listed                  | Use the **Streamable HTTP** server type and the URL for your workspace's region.                       |
| A tool returns a permission error    | Add the missing permission to the app in the **Developer Hub**.                                        |
| The receptionist can't find a caller | Intercom matches phone numbers as stored on the contact. Store numbers in one format.                  |
| You changed the token                | Edit the integration and use **Rotate Secret Token (optional)**. The saved token is never shown again. |
