---
title: "Postmark"
source: https://elevenlabs.io/docs/reception-ai/integrations/postmark.md
path: docs/reception-ai/integrations/postmark
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Postmark

Your receptionist can email your team when a caller leaves a message, asks for a callback, or needs something your team must handle. A [webhook tool](/docs/reception-ai/integrations/webhooks) sends the email through Postmark's Email API.

## Before you start

### Add a sender

In Postmark, open **Sender Signatures** and add the address to send from, such as `reception@YOURDOMAIN.com`, or verify your whole domain. Postmark only sends from confirmed senders.

### Copy the server token

Open your server, go to the **API Tokens** tab, and copy the **Server API token**. It can send email from this server only. Treat it as a secret.

> **Note**
>
> Until Postmark approves your account, it only delivers to addresses on your own domain. A team
> address on that domain works for testing. Request approval in Postmark before sending elsewhere.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `email_team_message`                                                                                                                                                                                                                                                                                                                              |
| **Description**      | "Email the team a summary when a caller leaves a message, asks for a callback, or needs something only the team can handle."                                                                                                                                                                                                                      |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                              |
| **URL**              | `https://api.postmarkapp.com/email`                                                                                                                                                                                                                                                                                                               |
| **Request Headers**  | `X-Postmark-Server-Token`: your server token  `Accept`: `application/json`                                                                                                                                                                                                                                                                        |
| **Body Parameters**  | `From` (string, required): "Always the exact value `reception@YOURDOMAIN.com`."  `To` (string, required): "Always the exact value `team@YOURDOMAIN.com`."  `Subject` (string, required): "For example: Callback request from Jane Doe."  `TextBody` (string, required): "The caller's name, phone number, what they need, and when to call back." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                  |

Replace both addresses with your confirmed sender and your team's inbox. Postmark field names start with a capital letter; keep them exactly as shown.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by leaving a message. The email arrives in your team's inbox and shows in the server's **Activity** tab.

> **Warning**
>
> Keep `To` fixed to your own team. Don't let your receptionist email callers with this tool: a
> caller could give any address, and your sender reputation depends on what you send.

## Troubleshooting

| Problem                               | What to check                                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Postmark returns 401 or error code 10 | The header must be named `X-Postmark-Server-Token` and hold a server token, not an account token.           |
| Error about the sender signature      | The `From` address isn't a confirmed sender signature or on a verified domain.                              |
| Error about a pending account         | The account isn't approved yet, so it can only send to your own domain.                                     |
| The email doesn't arrive              | Check the server's **Activity** tab. A recipient that bounced before is suppressed until you reactivate it. |
