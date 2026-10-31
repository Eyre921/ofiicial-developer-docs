---
title: "Slack"
source: https://elevenlabs.io/docs/reception-ai/integrations/slack.md
path: docs/reception-ai/integrations/slack
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Slack

A Slack incoming webhook lets your receptionist post a message to a channel during a call, for example when a caller asks for a callback or reports something urgent.

## Create an incoming webhook in Slack

### Create a Slack app

Go to [api.slack.com/apps](https://api.slack.com/apps), select **Create New App**, choose **From scratch**, and pick your workspace.

### Turn on incoming webhooks

Open **Incoming Webhooks**, turn on **Activate Incoming Webhooks**, and select **Add New Webhook to Workspace**. Pick the channel to post to and select **Allow**.

### Copy the webhook URL

Copy the URL, which starts with `https://hooks.slack.com/services/`. Treat it as a secret: anyone who has it can post to the channel.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `notify_team_in_slack`                                                                                                                            |
| **Description**      | "Post a message to the team's Slack channel. Use it when a caller asks for a callback, wants to speak to a person, or reports an urgent problem." |
| **Method**           | POST                                                                                                                                              |
| **URL**              | The Slack webhook URL                                                                                                                             |
| **Body Parameters**  | `text` (string, required): "The message to post: the caller's name, phone number, and what they need."                                            |
| **Assign to agents** | **Receptionist**                                                                                                                                  |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The message appears in the channel.

> **Tip**
>
> Each incoming webhook posts to one channel. To post to several channels, create one webhook and
> one tool per channel. To send direct messages or read Slack, use
> [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                        | What to check                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------- |
| Nothing appears in the channel | The body parameter must be named exactly `text`.                                                |
| Slack returns `no_service`     | The webhook was removed or the app uninstalled. Create a new webhook and update the tool's URL. |
| The receptionist never posts   | Make the tool's description name the situations where it should post.                           |
