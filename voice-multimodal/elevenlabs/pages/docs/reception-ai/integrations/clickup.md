---
title: "ClickUp"
source: https://elevenlabs.io/docs/reception-ai/integrations/clickup.md
path: docs/reception-ai/integrations/clickup
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ClickUp

Your receptionist can create a ClickUp task for your team when a caller asks for a callback, a quote, or anything else to follow up on. A [webhook tool](/docs/reception-ai/integrations/webhooks) adds the task to one list.

## Before you start

### Create a personal API token

In ClickUp, select your avatar, open **Settings** → **Apps**, and under **API Token** select **Generate**. The token starts with `pk_`. It acts as you and never expires, so treat it as a secret. Consider generating it from an account that only has access to the list.

### Find the list ID

Open the list in your browser. The number after `/li/` in the URL is the list ID.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `create_clickup_task`                                                                                                                                                                                                                                                                                                                             |
| **Description**      | "Create a task for the team whenever you promise the caller a follow-up, or the caller asks for something the team must handle."                                                                                                                                                                                                                  |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                              |
| **URL**              | `https://api.clickup.com/api/v2/list/LIST_ID/task`                                                                                                                                                                                                                                                                                                |
| **Request Headers**  | `Authorization`: your token, with no `Bearer` in front                                                                                                                                                                                                                                                                                            |
| **Body Parameters**  | `name` (string, required): "Short title with the caller's name and what they need, for example: Call back Jane Doe about a quote."  `description` (string, required): "The caller's name, phone number, and the details of their request."  `priority` (number): "1 for urgent, 2 for high, 3 for normal, 4 for low. Use 1 only for emergencies." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                  |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The task appears in the list.

The tool leaves out due dates and assignees. ClickUp takes due dates as Unix timestamps in milliseconds, which your receptionist can't reliably work out on a call, and assignees as a list of user IDs, which webhook tools can't send. Use a ClickUp automation on the list to assign new tasks and set a due date, or route the task through [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                              | What to check                                                                             |
| ------------------------------------ | ----------------------------------------------------------------------------------------- |
| ClickUp returns 401                  | The header must be `Authorization` with the `pk_` token alone, without `Bearer`.          |
| ClickUp returns 404 or a list error  | Check the list ID in the URL, and that the token's user can see the list.                 |
| The task has no priority             | Priority must be a number from 1 to 4. Leave it out if the caller's request isn't urgent. |
| The receptionist never creates tasks | Make the tool's description name the situations where it should create one.               |
