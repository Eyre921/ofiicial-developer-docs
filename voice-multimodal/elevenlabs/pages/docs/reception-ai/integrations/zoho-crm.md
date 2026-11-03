---
title: "Zoho CRM"
source: https://elevenlabs.io/docs/reception-ai/integrations/zoho-crm.md
path: docs/reception-ai/integrations/zoho-crm
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Zoho CRM

Zoho MCP lets you build an [MCP server](/docs/reception-ai/integrations/mcp-server) with the Zoho CRM tools you choose. Connect it so your receptionist can recognize callers who are already in your CRM and add new callers as leads. Zoho CRM's own API uses sign-in tokens that expire every hour, so webhook tools can't connect to it directly.

## Setup

### Create an MCP server in Zoho

Sign in to the Zoho MCP console for your Zoho data center, such as `mcp.zoho.com` or `mcp.zoho.eu`. Select **Create MCP Server**, enter a name, and select **Create**.

### Add Zoho CRM tools

Open **Tools** and select **Add Tools**. Filter for Zoho CRM and check only the tools your receptionist needs, such as tools to search records, get a record, and create records. Select **Add Now**.

Leave out tools that update or delete records, or that change your CRM's modules, fields, or workflows.

### Authorize the connection in advance

Zoho tools default to **Authorize on Demand**, which asks for a Zoho sign-in in a browser the first time a tool runs. Your receptionist can't complete that sign-in during a call, so authorize the connection in the console instead:

1. Open **Connections** → **Zoho Services**, select **Edit**, choose **Authorize via Connections**, and select **Update**.
2. Select the menu (**…**) next to the connection and select **Authorize**.
3. Sign in as the Zoho user your receptionist should act as, and allow access.

The tools can do anything this user's CRM role allows. Consider a dedicated user with a role limited to the modules your receptionist needs.

### Copy the MCP URL

Open **Connect** and copy the MCP URL. The URL contains a key that gives access to your CRM tools, so treat it as a secret.

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field           | Value                  |
| --------------- | ---------------------- |
| **Name**        | Zoho CRM               |
| **Server type** | Streamable HTTP        |
| **Server URL**  | The MCP URL you copied |

Leave **Secret Token** empty, because the key is already in the URL. Select **Enable**.

### Assign tools

Open the **Tools** tab and assign the search, get, and create tools to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call from a number that's already in Zoho CRM, then with a new caller. The new caller appears as a lead.

> **Note**
>
> Calls to the Zoho MCP server use your Zoho CRM API credits, the same as other API access.

## Troubleshooting

| Problem                                | What to check                                                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| No tools are listed                    | Use the **Streamable HTTP** server type and the full URL from **Connect**.                                               |
| Tools fail with an authorization error | The connection is still set to **Authorize on Demand**, or isn't authorized yet. Authorize it in the Zoho MCP console.   |
| Known callers aren't found             | Zoho matches phone numbers as stored. Store numbers in one format.                                                       |
| A tool shows a **Changed** badge       | You changed the tool in Zoho. Review it in the **Tools** tab and select **Update**.                                      |
| The MCP URL was shared by mistake      | Select **Regenerate API Key** under **Connect** in the Zoho MCP console, then update the **Server URL** in Reception.ai. |
