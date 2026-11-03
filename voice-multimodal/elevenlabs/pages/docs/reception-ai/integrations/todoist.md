---
title: "Todoist"
source: https://elevenlabs.io/docs/reception-ai/integrations/todoist.md
path: docs/reception-ai/integrations/todoist
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Todoist

Your receptionist can add a task to Todoist when a caller asks for a callback, a quote, or anything else to follow up on. A [webhook tool](/docs/reception-ai/integrations/webhooks) creates the task through Todoist's API.

## Before you start

### Copy your API token

In Todoist, open **Settings** → **Integrations** → **Developer** and copy your **API token**. It gives full access to your Todoist account, so treat it as a secret.

### Find the project ID

Open the project in the Todoist web app. The ID is the last part of the URL, after the final dash: in `app.todoist.com/app/project/callbacks-6Jf8VQXxpwv56VQ7`, it's `6Jf8VQXxpwv56VQ7`. Skip this to add tasks to your Inbox.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `create_todoist_task`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Description**      | "Create a task for the team whenever you promise the caller a follow-up, or the caller asks for something the team must handle."                                                                                                                                                                                                                                                                                                                            |
| **Method**           | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **URL**              | `https://api.todoist.com/api/v1/tasks`                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your API token                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Body Parameters**  | `content` (string, required): "Short title with the caller's name and what they need, for example: Call back Jane Doe about a quote."  `description` (string, required): "The caller's name, phone number, and the details of their request."  `due_string` (string): "When to follow up, in plain English, for example: tomorrow at 10am. Leave it out if the caller didn't say."  `project_id` (string, required): "Always the exact value `PROJECT_ID`." |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Replace `PROJECT_ID` with your project ID, or remove `project_id` to add tasks to your Inbox.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback tomorrow. The task appears in the project with a due date.

## Troubleshooting

| Problem                              | What to check                                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Todoist returns 401                  | The header value must be `Bearer ` followed by the token. Copy it again if you reset it.                                             |
| Todoist returns 400 or 404           | Check the project ID, and that the URL is `https://api.todoist.com/api/v1/tasks`. Older guides use the previous `/rest/v2/` address. |
| Tasks have the wrong due date        | Todoist reads `due_string` in your account's time zone. Check it under **Settings** → **General**.                                   |
| The receptionist never creates tasks | Make the tool's description name the situations where it should create one.                                                          |
