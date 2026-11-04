---
title: "Copper"
source: https://elevenlabs.io/docs/reception-ai/integrations/copper.md
path: docs/reception-ai/integrations/copper
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Copper

Your receptionist can recognize callers who are already in Copper, add new callers as leads, note what each caller wanted, and create a follow-up task for your team. Looking up callers and creating tasks use [webhook tools](/docs/reception-ai/integrations/webhooks). Adding leads and notes goes through [Zapier](/docs/reception-ai/integrations/zapier), because Copper stores phone numbers and note links as nested data that webhook tools can't send.

## Before you start

In Copper, open **System settings** → **API Keys** and select **Generate API key**. Label it, for example `Reception.ai`. The key acts as you, so it can see and change what you can.

Every webhook tool below sends these request headers:

| Header             | Value                                          |
| ------------------ | ---------------------------------------------- |
| `X-PW-AccessToken` | your API key                                   |
| `X-PW-Application` | `developer_api`                                |
| `X-PW-UserEmail`   | the email address of the user who made the key |

> **Warning**
>
> Anyone with the API key and your email address can read and change your Copper data. Keep the key
> out of shared documents, and delete it in Copper if it leaks.

## Create the webhook tools

For each tool, go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and set **Assign to agents** to **Receptionist**. Copper's search endpoints use POST with the search in the body.

### Find a contact

| Field               | Value                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `find_copper_person`                                                                                                   |
| **Description**     | "Find the caller among our contacts by phone number. Use it at the start of a call to check whether they're a client." |
| **Method**          | POST                                                                                                                   |
| **URL**             | `https://api.copper.com/developer_api/v1/people/search`                                                                |
| **Request Headers** | The headers from [Before you start](#before-you-start)                                                                 |
| **Body Parameters** | `phone_number` (string, required): "The caller's phone number."                                                        |

### Find a lead

| Field               | Value                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------ |
| **Name**            | `find_copper_lead`                                                                         |
| **Description**     | "Find the caller among our leads by phone number. Use it when the caller isn't a contact." |
| **Method**          | POST                                                                                       |
| **URL**             | `https://api.copper.com/developer_api/v1/leads/search`                                     |
| **Request Headers** | The headers from [Before you start](#before-you-start)                                     |
| **Body Parameters** | `phone_number` (string, required): "The caller's phone number."                            |

### Create a follow-up task

| Field               | Value                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `create_copper_task`                                                                                                                                                      |
| **Description**     | "Create a task for the team whenever you promise the caller a call back."                                                                                                 |
| **Method**          | POST                                                                                                                                                                      |
| **URL**             | `https://api.copper.com/developer_api/v1/tasks`                                                                                                                           |
| **Request Headers** | The headers from [Before you start](#before-you-start)                                                                                                                    |
| **Body Parameters** | `name` (string, required): "For example: Call back Jane Doe about a kitchen quote."  `details` (string, required): "The caller's name, phone number, and what they need." |

Select **Enable** on each tool.

## Add leads and notes

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Copper actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), connect your Copper account and add these actions:

* **Create Lead**: set the owner and lead source as fixed values, and let the AI fill in the caller's name, phone number, email address, and what they want.
* **Create Activity**: set the activity type to a note, and let the AI fill in the person or lead found by the search tools and what the caller needed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign both Copper actions to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call from a number saved on a Copper contact, then from a new number that asks for a callback. The new caller appears as a lead, and the task appears in Copper.

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) so your receptionist
> searches contacts and leads first, and only creates a lead when neither search finds the caller.

## Limitations

* Webhook tools send flat values, and Copper links a task to a person or lead with a nested value. So tasks from `create_copper_task` aren't linked to the caller's record; the task's details keep the caller's name and number instead.
* Copper takes due dates as Unix timestamps, which the AI can't reliably work out, so `create_copper_task` leaves the due date empty.
* To link tasks to the caller or set a due date, use Copper's **Create Task** action through Zapier instead of the webhook tool.
* Each Zapier action your receptionist runs uses tasks from your Zapier plan. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                    | What to check                                                                                                                      |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| 401 or 403 from Copper                     | Check all three headers. `X-PW-UserEmail` must be the email of the user who generated the key.                                     |
| Known callers aren't found                 | Copper matches phone numbers as stored. Store numbers in one format, and check that the caller is a person or lead, not a company. |
| The receptionist creates duplicate leads   | Tell it in the search tools' descriptions to create a lead only when the caller wasn't found.                                      |
| A Copper action doesn't appear             | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                                                 |
| An action shows **Changed** and isn't used | You edited it in Zapier. Select **Update** in the **Tools** tab.                                                                   |
