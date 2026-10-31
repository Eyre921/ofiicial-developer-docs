---
title: "Asana"
source: https://elevenlabs.io/docs/reception-ai/integrations/asana.md
path: docs/reception-ai/integrations/asana
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Asana

Your receptionist can turn a caller's request into an Asana task for your team, and tell a caller where a job stands. Creating tasks goes through [Zapier](/docs/reception-ai/integrations/zapier), because Asana's API expects task fields nested inside a `data` object that webhook tools can't send. Reading tasks uses a [webhook tool](/docs/reception-ai/integrations/webhooks).

## Create tasks

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Asana action

In your Zapier MCP server, add the Asana **Create Task** action and connect your Asana account. Set the workspace and project to fixed values, and let the AI fill in the task name, notes, and due date.

### Assign the tool

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign the Asana action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a callback. The task appears in the project.

## Check a project's open tasks

### Create a personal access token

In Asana, open **My settings** → **Apps** → **Manage Developer Apps**, and create a personal access token. The token can see everything you can, so consider creating it from an account that only has access to the project.

### Find the project ID

Open the project in your browser. The long number after `/project/` in the URL is the project ID.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `list_open_jobs`                                                                                                                                              |
| **Description**      | "List the open jobs in our project. Use it when a caller asks about the status of their job."                                                                 |
| **Method**           | GET                                                                                                                                                           |
| **URL**              | `https://app.asana.com/api/1.0/projects/PROJECT_ID/tasks`                                                                                                     |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your token                                                                                                             |
| **Query Parameters** | `completed_since` (string, required): "Always the exact value `now`."  `opt_fields` (string, required): "Always the exact value `name,due_on,assignee.name`." |
| **Assign to agents** | **Receptionist**                                                                                                                                              |

Select **Enable**.

`completed_since=now` makes Asana return only incomplete tasks. Name tasks after the customer, so your receptionist can find the caller's task in the list.

## Troubleshooting

| Problem                                         | What to check                                                                                    |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| The Asana action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.               |
| 401 on the task list                            | The header must be `Bearer ` followed by a current token.                                        |
| 404 on the task list                            | Check the project ID, and that the token's account can see the project.                          |
| Asana says the result is too large              | Very large projects need pagination, which the tool doesn't do. Keep the project to active jobs. |
