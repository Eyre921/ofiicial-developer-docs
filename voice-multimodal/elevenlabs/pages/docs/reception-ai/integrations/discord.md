---
title: "Discord"
source: https://elevenlabs.io/docs/reception-ai/integrations/discord.md
path: docs/reception-ai/integrations/discord
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Discord

A Discord channel webhook lets your receptionist post a message to a channel during a call, for example when a caller asks for a callback or reports something urgent.

## Create a webhook in Discord

You need the **Manage Webhooks** permission on the server.

### Open the server's webhooks

In Discord, open **Server Settings** → **Integrations** → **Webhooks**, and select **New Webhook**.

### Pick the channel

Open the new webhook, give it a name, such as "Reception", and choose the channel to post to. Select **Save Changes**.

### Copy the webhook URL

Select **Copy Webhook URL**. The URL starts with `https://discord.com/api/webhooks/`. Treat it as a secret: anyone who has it can post to the channel.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `notify_team_in_discord`                                                                                                                            |
| **Description**      | "Post a message to the team's Discord channel. Use it when a caller asks for a callback, wants to speak to a person, or reports an urgent problem." |
| **Method**           | POST                                                                                                                                                |
| **URL**              | The Discord webhook URL, with `?wait=true` added to the end                                                                                         |
| **Body Parameters**  | `content` (string, required): "The message to post, under 2,000 characters: the caller's name, phone number, and what they need."                   |
| **Assign to agents** | **Receptionist**                                                                                                                                    |

With `?wait=true`, Discord replies with the posted message instead of an empty response, so your receptionist can tell the message went through.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The message appears in the channel.

> **Tip**
>
> Each webhook posts to one channel. To post to several channels, create one webhook and one tool
> per channel.

## Troubleshooting

| Problem                                 | What to check                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Discord returns 400                     | The body parameter must be named exactly `content`, and the message must be under 2,000 characters. |
| Discord returns 401 or 404              | The webhook was deleted or its URL was reset. Copy the current URL and update the tool.             |
| Discord returns 400 for a forum channel | Forum channels need a thread for each post. Point the webhook at a text channel instead.            |
| The receptionist never posts            | Make the tool's description name the situations where it should post.                               |
