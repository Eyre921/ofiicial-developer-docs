---
title: "Brevo"
source: https://elevenlabs.io/docs/reception-ai/integrations/brevo.md
path: docs/reception-ai/integrations/brevo
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Brevo

Your receptionist can send a caller a text message through Brevo, for example your address or a summary of what was agreed on the call. A [webhook tool](/docs/reception-ai/integrations/webhooks) sends the SMS. To look up and save contacts, connect Brevo's [MCP server](/docs/reception-ai/integrations/mcp-server).

> **Warning**
>
> Only text callers who ask for a message or agree to one on the call, and keep these messages
> transactional: no promotions. Marketing texts need prior consent and an opt-out under rules such
> as the TCPA in the US and GDPR in the EU. Check what applies to your business before you turn this
> on.

## Send a follow-up text

### Prepare your Brevo account

SMS uses prepaid credits. In Brevo, buy SMS credits and check that SMS sending is available for the countries you text. Some countries, such as the US and Canada, don't accept a custom sender name.

### Create an API key

In Brevo, open **SMTP & API** → **API Keys** and select **Generate a new API key**. Leave **Create MCP server API key** off for this key. Copy the key, which starts with `xkeysib-`.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `send_followup_text`                                                                                                                                                                                                                                                                                                                                                                            |
| **Description**      | "Send the caller a text message. Only use it after the caller asks for a text or agrees to receive one. Never send promotions."                                                                                                                                                                                                                                                                 |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                                                            |
| **URL**              | `https://api.brevo.com/v3/transactionalSMS/send`                                                                                                                                                                                                                                                                                                                                                |
| **Request Headers**  | `api-key`: your API key  `accept`: `application/json`                                                                                                                                                                                                                                                                                                                                           |
| **Body Parameters**  | `sender` (string, required): "Always the exact value `YOUR_SENDER`."  `recipient` (string, required): "The caller's mobile number with country code, digits only, without `+` or spaces. For example 14155550123."  `content` (string, required): "The text message, under 160 characters. Start with the business name."  `type` (string, required): "Always the exact value `transactional`." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                                                                |

Replace `YOUR_SENDER` with your sender name (up to 11 letters and digits) or sending number (up to 15 digits).

### Test it

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for your address by text, using your own mobile number. You can check delivery in Brevo's SMS logs.

Messages over 160 characters are sent as several texts, and each uses credits.

## Look up and save contacts

### Create an MCP key

In Brevo, open **SMTP & API** → **API Keys**, select **Generate a new API key**, and turn on **Create MCP server API key**. Copy the key.

> **Warning**
>
> An MCP key has full read and write access to your Brevo account. Keep it separate from the SMS
> key, and connect only the contacts module below.

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| **Name**         | Brevo contacts                                |
| **Server type**  | Streamable HTTP                               |
| **Server URL**   | `https://mcp.brevo.com/v1/brevo_contacts/mcp` |
| **Secret Token** | Your MCP key                                  |

Select **Enable**. Reception.ai sends the key as a bearer token and lists Brevo's contact tools.

### Assign tools

Open the **Tools** tab. Assign the tools that look up and create contacts to the **Client** (receptionist). Leave tools that delete contacts or change lists unassigned, or assign them only to the **Assistant**.

> **Note**
>
> `https://mcp.brevo.com/v1/brevo/mcp` exposes every Brevo module, including email campaigns. Use it
> only if you want your team to manage campaigns from the **Assistant**.

## Troubleshooting

| Problem                 | What to check                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Brevo returns 401       | The header must be named `api-key`. If Brevo mentions an unrecognized IP address, check the authorized IPs in Brevo's security settings. |
| Brevo returns 400       | Check the number has its country code and no `+`, and that the sender name is at most 11 characters.                                     |
| The text never arrives  | Check your SMS credits and whether Brevo can send SMS to that country with your sender.                                                  |
| No MCP tools are listed | Use **Streamable HTTP**, and an MCP key, not the SMS key.                                                                                |
| You changed the MCP key | The secret token can only be set when you create the integration. Disconnect and reconnect it with the new key.                          |
