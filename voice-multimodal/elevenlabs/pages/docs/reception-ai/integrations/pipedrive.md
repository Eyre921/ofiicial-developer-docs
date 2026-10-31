---
title: "Pipedrive"
source: https://elevenlabs.io/docs/reception-ai/integrations/pipedrive.md
path: docs/reception-ai/integrations/pipedrive
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Pipedrive

With the [webhook tools](/docs/reception-ai/integrations/webhooks) below, your receptionist can recognize callers who are already in Pipedrive, open a deal for a new opportunity, and schedule a follow-up call for your team.

## Before you start

In Pipedrive, open **Personal preferences** → **API** and copy your API token. Every tool below sends it in the `x-api-token` request header. The tools act as you, so use the token of a user who can see the right pipeline.

## Create the tools

For each tool, go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and set **Assign to agents** to **Receptionist**.

### Find a caller

| Field                | Value                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_pipedrive_person`                                                                                                         |
| **Description**      | "Find the caller in our CRM by phone number or name. Use it at the start of a call about a sale, a quote, or an existing deal." |
| **Method**           | GET                                                                                                                             |
| **URL**              | `https://api.pipedrive.com/api/v2/persons/search`                                                                               |
| **Request Headers**  | `x-api-token`: your API token                                                                                                   |
| **Query Parameters** | `term` (string, required): "The caller's phone number or full name, at least 2 characters."                                     |

### Open a deal

| Field               | Value                                                                                                                                                                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `create_pipedrive_deal`                                                                                                                                                                                                                                  |
| **Description**     | "Open a deal when a caller wants a quote or wants to buy. Include the caller's name in the title."                                                                                                                                                       |
| **Method**          | POST                                                                                                                                                                                                                                                     |
| **URL**             | `https://api.pipedrive.com/api/v2/deals`                                                                                                                                                                                                                 |
| **Request Headers** | `x-api-token`: your API token                                                                                                                                                                                                                            |
| **Body Parameters** | `title` (string, required): "Short title with the caller's name and what they want."  `person_id` (number): "The id from `find_pipedrive_person`. Leave it out if the caller wasn't found."  `value` (number): "The deal value, if the caller gave one." |

### Schedule a follow-up

| Field               | Value                                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `create_pipedrive_followup`                                                                                                                                                                                                                                                                                                                                       |
| **Description**     | "Schedule a call back from the team whenever you promise the caller a follow-up."                                                                                                                                                                                                                                                                                 |
| **Method**          | POST                                                                                                                                                                                                                                                                                                                                                              |
| **URL**             | `https://api.pipedrive.com/api/v2/activities`                                                                                                                                                                                                                                                                                                                     |
| **Request Headers** | `x-api-token`: your API token                                                                                                                                                                                                                                                                                                                                     |
| **Body Parameters** | `subject` (string, required): "For example: Call back Jane Doe about a kitchen quote."  `type` (string, required): "Always the exact value `call`."  `due_date` (string, required): "The follow-up date as YYYY-MM-DD."  `note` (string, required): "The caller's name, phone number, and what they need."  `deal_id` (number): "The deal id, if you opened one." |

Select **Enable** on each tool, then [test your receptionist](/docs/reception-ai/receptionist/testing) with a call that asks for a quote.

## Limitations

Webhook tools send flat values, and Pipedrive stores a person's phone numbers as a nested list. So these tools can't create a new contact with a phone number. The follow-up's note keeps the caller's number instead. To create contacts, use Pipedrive's **Create Person** action through [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                    | What to check                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------- |
| 401 from Pipedrive         | The header must be named `x-api-token` and hold a current token.                                        |
| Known callers aren't found | Pipedrive matches phone numbers as stored. Store numbers in one format, or search by name as well.      |
| The follow-up has no type  | `call` must be an activity type in your Pipedrive account. Check **Company settings** → **Activities**. |
