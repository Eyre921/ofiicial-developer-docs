---
title: "Resend"
source: https://elevenlabs.io/docs/reception-ai/integrations/resend.md
path: docs/reception-ai/integrations/resend
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Resend

Your receptionist can email your team when a caller leaves a message, asks for a callback, or needs something your team must handle. A [webhook tool](/docs/reception-ai/integrations/webhooks) sends the email through Resend's API.

## Before you start

### Verify your domain

In Resend, open **Domains**, add the domain to send from, and add the DNS records it shows. Until a domain is verified, Resend only sends test emails to your own account's address.

### Create an API key

Open **API Keys** and select **Create API key**. Set **Permission** to **Sending access** and restrict it to your domain. The key starts with `re_`. Treat it as a secret.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `email_team_message`                                                                                                                                                                                                                                                                                                                                      |
| **Description**      | "Email the team a summary when a caller leaves a message, asks for a callback, or needs something only the team can handle."                                                                                                                                                                                                                              |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                      |
| **URL**              | `https://api.resend.com/emails`                                                                                                                                                                                                                                                                                                                           |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your API key                                                                                                                                                                                                                                                                                                       |
| **Body Parameters**  | `from` (string, required): "Always the exact value `Reception <reception@YOURDOMAIN.com>`."  `to` (string, required): "Always the exact value `team@YOURDOMAIN.com`."  `subject` (string, required): "For example: Callback request from Jane Doe."  `text` (string, required): "The caller's name, phone number, what they need, and when to call back." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                          |

Replace both addresses: `from` must be on your verified domain, and `to` is your team's inbox.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by leaving a message. The email arrives in your team's inbox and shows under **Emails** in Resend.

> **Warning**
>
> Keep `to` fixed to your own team. Don't let your receptionist email callers with this tool: a
> caller could give any address, and your domain's reputation depends on what you send.

## Troubleshooting

| Problem                      | What to check                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------- |
| Resend returns 401           | The header value must be `Bearer ` followed by the key.                           |
| Resend returns 403           | The `from` domain isn't verified, or the key is restricted to a different domain. |
| The email doesn't arrive     | Check **Emails** in Resend for a bounce, and your team inbox's spam folder.       |
| The receptionist never sends | Make the tool's description name the situations where it should send.             |
