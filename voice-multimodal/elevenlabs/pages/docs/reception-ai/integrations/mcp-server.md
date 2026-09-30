---
title: "MCP server"
source: https://elevenlabs.io/docs/reception-ai/integrations/mcp-server.md
path: docs/reception-ai/integrations/mcp-server
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# MCP server

MCP (Model Context Protocol) lets you connect any compatible tool server to your receptionist. Reception.ai discovers the server's tools automatically, and your receptionist can call them during conversations.

## What is MCP?

MCP is an open protocol for connecting AI to external tools and data sources. If your service exposes an MCP interface, the receptionist can use its tools without custom integration code.

## Setting up an MCP connection

Go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Description                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| **Name**         | Display name for this integration                                                               |
| **Description**  | Optional. What this server provides.                                                            |
| **Server type**  | SSE (default) or Streamable HTTP                                                                |
| **Server URL**   | The HTTPS URL of your MCP server endpoint                                                       |
| **Secret Token** | Optional. Sent to authenticate with your server. Can only be set when creating the integration. |
| **HTTP Headers** | Optional headers sent with every request                                                        |

Select **Enable**. Reception.ai connects and lists the available tools.

## Server types

| Type                | When to use                                     |
| ------------------- | ----------------------------------------------- |
| **SSE**             | Long-lived connections and streaming responses  |
| **Streamable HTTP** | Standard request and response, easier to deploy |

## Managing tools

Open the **Tools** tab to see the tools your server provides. Assign each tool to the **Client** (receptionist), the **Assistant**, or both, or select **Enable all**. Unassigned tools are not used.

Select **Refresh tools** after adding tools to your server.

## Use cases

* **Custom booking logic**: connect to your existing reservation system.
* **Inventory lookup**: let the receptionist check stock in real time.
* **CRM queries**: pull customer data from your internal systems during calls.
* **Custom workflows**: trigger any backend process based on the conversation.

You can connect multiple MCP servers. All their tools appear in the same assignment interface.

> **Note**
>
> MCP servers are available on every plan. Your server must be reachable from the internet over
> HTTPS.
