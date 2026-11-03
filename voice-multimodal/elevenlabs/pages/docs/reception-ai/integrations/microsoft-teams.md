---
title: "Microsoft Teams"
source: https://elevenlabs.io/docs/reception-ai/integrations/microsoft-teams.md
path: docs/reception-ai/integrations/microsoft-teams
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Microsoft Teams

A Teams workflow can give your channel a webhook URL. Your receptionist posts to it with a [webhook tool](/docs/reception-ai/integrations/webhooks) during a call, for example when a caller asks for a callback or reports something urgent.

> **Note**
>
> Microsoft retired the Office 365 connector incoming webhooks in Teams. Use the **Workflows** app,
> as below.

## Create a webhook workflow in Teams

The built-in **Send webhook alerts to a channel** templates expect an Adaptive Card, a nested message format webhook tools can't send. Build the workflow from a blank flow instead, so it posts a plain `text` field.

### Start a blank workflow

In Teams, open the **Workflows** app, select **Create**, and choose **Create from blank**.

### Add the trigger

Add the **When a Teams webhook request is received** trigger. Set **Who can trigger the flow** to **Anyone**. The other options need a Microsoft sign-in token, which webhook tools can't send.

### Add the post action

Add the **Post message in a chat or channel** action. Set **Post as** to **Flow bot**, **Post in** to **Channel**, and pick the team and channel. In **Message**, add an expression with the exact value `triggerBody()?['text']`.

### Copy the webhook URL

Save the workflow, then open the trigger and copy the HTTP URL it shows. Treat it as a secret: anyone who has it can post to the channel.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `notify_team_in_teams`                                                                                                                            |
| **Description**      | "Post a message to the team's Teams channel. Use it when a caller asks for a callback, wants to speak to a person, or reports an urgent problem." |
| **Method**           | POST                                                                                                                                              |
| **URL**              | The workflow's webhook URL                                                                                                                        |
| **Body Parameters**  | `text` (string, required): "The message to post: the caller's name, phone number, and what they need."                                            |
| **Assign to agents** | **Receptionist**                                                                                                                                  |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The message appears in the channel. You can also check each run in the Workflows app.

> **Tip**
>
> Each workflow posts to one channel or chat. To post to several, create one workflow and one tool
> for each. A workflow belongs to the person who created it and stops if their account is removed,
> so add a co-owner in Power Automate.

## Troubleshooting

| Problem                                   | What to check                                                                                                                 |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| The workflow runs but posts nothing       | The message expression must be `triggerBody()?['text']`, and the body parameter must be named exactly `text`.                 |
| You started from a webhook alert template | Those templates expect an Adaptive Card. Build the workflow from blank with the **Post message in a chat or channel** action. |
| Requests are rejected with 401            | Set **Who can trigger the flow** to **Anyone**.                                                                               |
| The workflow can't post to the channel    | Private channels aren't supported by this action. Use a standard channel, or a chat.                                          |
| The receptionist never posts              | Make the tool's description name the situations where it should post.                                                         |
