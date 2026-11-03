---
title: "Google Chat"
source: https://elevenlabs.io/docs/reception-ai/integrations/google-chat.md
path: docs/reception-ai/integrations/google-chat
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Google Chat

A Google Chat incoming webhook lets your receptionist post a message to a space during a call, for example when a caller asks for a callback or reports something urgent.

## Create an incoming webhook in Google Chat

You need a Google Workspace Business or Enterprise account, and your Workspace admin must allow incoming webhooks.

### Open the space's integrations

In a browser, open [chat.google.com](https://chat.google.com) and go to the space to post to. Next to the space name, open the menu and select **Apps & integrations**.

### Add a webhook

Select **Add webhooks**. Enter a name, such as "Reception", and optionally an avatar URL. Select **Save**.

### Copy the webhook URL

Next to the new webhook, select **More** → **Copy link**. The URL starts with `https://chat.googleapis.com/v1/spaces/` and ends with a `key` and a `token`. Treat it as a secret: anyone who has it can post to the space.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `notify_team_in_google_chat`                                                                                                                          |
| **Description**      | "Post a message to the team's Google Chat space. Use it when a caller asks for a callback, wants to speak to a person, or reports an urgent problem." |
| **Method**           | POST                                                                                                                                                  |
| **URL**              | The full webhook URL, including `key` and `token`                                                                                                     |
| **Body Parameters**  | `text` (string, required): "The message to post: the caller's name, phone number, and what they need."                                                |
| **Assign to agents** | **Receptionist**                                                                                                                                      |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The message appears in the space.

> **Tip**
>
> Each webhook posts to the one space it was added to. To post to several spaces, create one webhook
> and one tool per space. To send direct messages or read Google Chat, use
> [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                          | What to check                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Nothing appears in the space     | The body parameter must be named exactly `text`, and the URL must include both `key` and `token`.                     |
| **Add webhooks** isn't available | Your Workspace admin hasn't allowed incoming webhooks, or you're on a personal Google account.                        |
| Google returns 429               | Google Chat accepts about one message per second per space. This only matters if several calls post at the same time. |
| The receptionist never posts     | Make the tool's description name the situations where it should post.                                                 |
