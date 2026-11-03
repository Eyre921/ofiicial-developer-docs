---
title: "SimplyBook.me"
source: https://elevenlabs.io/docs/reception-ai/integrations/simplybook.md
path: docs/reception-ai/integrations/simplybook
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# SimplyBook.me

SimplyBook.me's **MCP connector** feature includes a public [MCP server](/docs/reception-ai/integrations/mcp-server) for booking assistants. Connect it so your receptionist can tell callers about your services, find open times, and book them in.

The public server can only do what an anonymous visitor to your booking page can do. It can't see your client list or existing bookings.

## Setup

### Turn on the MCP connector

In your SimplyBook.me admin, open **Custom Features** and enable **MCP connector**.

### Copy the public connector details

Open the **MCP connector** feature and go to the **Public agent integration** section. Copy the connector URL, which ends in `/mcp/public`, and the API key.

Don't use the **Admin AI Assistant** connector. It needs a SimplyBook.me sign-in in a browser, which Reception.ai can't do, and it can see all your account's data.

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Value                    |
| ---------------- | ------------------------ |
| **Name**         | SimplyBook.me            |
| **Server type**  | Streamable HTTP          |
| **Server URL**   | The public connector URL |
| **Secret Token** | The public agent API key |

Select **Enable**. Reception.ai sends the key as a bearer token and lists the server's tools.

### Assign tools

Open the **Tools** tab and assign the tools for searching services, checking availability, and creating bookings to the **Client** (receptionist).

The tools available depend on which SimplyBook.me features you have enabled. If you enable more features later, select **Refresh tools**.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking what services you offer and booking a time. The booking appears in your SimplyBook.me calendar.

## Limitations

Your receptionist can't look up, change, or cancel a caller's existing bookings, because a booking page visitor can't either. Callers can use the links in their booking confirmation for that.

## Troubleshooting

| Problem                               | What to check                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| No tools are listed                   | Check you copied the URL from **Public agent integration**. If it still fails, reconnect with the **SSE** server type. |
| Tools stop working after a key change | **Generate new API key** cancels the old key at once. Disconnect the integration and reconnect it with the new key.    |
| A service is missing                  | The server only sees services shown on your public booking page.                                                       |
| A tool shows a **Changed** badge      | You changed features in SimplyBook.me. Review the tool in the **Tools** tab and select **Update**.                     |
