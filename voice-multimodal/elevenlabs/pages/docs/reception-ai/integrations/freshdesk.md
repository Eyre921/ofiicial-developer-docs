---
title: "Freshdesk"
source: https://elevenlabs.io/docs/reception-ai/integrations/freshdesk.md
path: docs/reception-ai/integrations/freshdesk
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Freshdesk

With a [webhook tool](/docs/reception-ai/integrations/webhooks), your receptionist can open a Freshdesk ticket whenever a caller reports a problem or asks for help, so your team can pick it up. On Growth, Pro, and Enterprise plans, you can also connect Freshdesk's [MCP server](#look-up-tickets-with-the-mcp-server) to look up existing tickets.

## Create tickets

### Get your API key

In Freshdesk, select your profile picture, open **Profile settings**, and select **View API key**. Copy the key. It acts as your agent account, so tickets are created with your permissions.

### Build the authorization header

Freshdesk uses the API key as a username with `X` as the password. Encode it in a terminal, replacing `YOUR_API_KEY` with your key:

```bash
printf 'YOUR_API_KEY:X' | base64
```

The header value is `Basic ` followed by the output.

> **Warning**
>
> Don't paste your API key into an online encoder. Anyone with the key or the encoded header can
> read and change your tickets.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `create_freshdesk_ticket`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Description**      | "Open a support ticket when a caller reports a problem or needs help from the team."                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **URL**              | `https://YOURDOMAIN.freshdesk.com/api/v2/tickets`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Request Headers**  | `Authorization`: `Basic ` followed by the encoded key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Body Parameters**  | `name` (string, required): "The caller's full name."  `phone` (string): "The caller's phone number."  `email` (string): "The caller's email address, if they gave it."  `subject` (string, required): "A short summary of the problem."  `description` (string, required): "What the caller reported, in their words, with any details they gave."  `status` (number, required): "Always the exact value `2`."  `priority` (number, required): "Always the exact value `1`."  `source` (number, required): "Always the exact value `3`." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Replace `YOURDOMAIN` with your Freshdesk subdomain. Select **Enable**.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by reporting a problem. The ticket appears in Freshdesk.

The fixed values create the ticket as **Open** (status `2`) with **Low** priority (priority `1`), and mark it as coming from **Phone** (source `3`). To let the receptionist set the priority, describe the values instead, for example: "1 for low, 2 for medium, 3 for high, 4 for urgent."

Freshdesk needs a phone number or email to find or create the requester. Tell your receptionist to always collect the caller's phone number.

## Look up tickets with the MCP server

Freshdesk's [MCP server](/docs/reception-ai/integrations/mcp-server) is available on Growth, Pro, and Enterprise plans. Use it to let your receptionist look up a caller's existing tickets. MCP actions count against a yearly allowance that depends on your plan.

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Name**         | Freshdesk                                     |
| **Server type**  | Streamable HTTP                               |
| **Server URL**   | `https://YOURDOMAIN.freshdesk.com/mcp`        |
| **HTTP Headers** | `Authorization`: your API key, with no prefix |

Leave **Secret Token** empty, so Reception.ai sends your `Authorization` header exactly as entered. Use your `freshdesk.com` subdomain even if you have a custom domain. Select **Enable**.

Open the **Tools** tab and assign the ticket lookup tools, such as `fetchSearchTickets` and `fetchTicket`, to the **Client** (receptionist). Leave tools that update tickets, agents, groups, or articles unassigned.

## Troubleshooting

| Problem                       | What to check                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 401 from Freshdesk            | Encode the key with `:X` after it, and start the header value with `Basic ` and a space.                               |
| 400 about the requester       | The ticket needs a phone number or email, plus the name. Make sure the receptionist collects them.                     |
| 400 about status or priority  | `status`, `priority`, and `source` must be number parameters, not strings.                                             |
| The MCP server lists no tools | Use your `freshdesk.com` subdomain, and put the raw API key in the `Authorization` header with no `Basic` or `Bearer`. |
