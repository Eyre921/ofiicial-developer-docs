---
title: "Capsule CRM"
source: https://elevenlabs.io/docs/reception-ai/integrations/capsule-crm.md
path: docs/reception-ai/integrations/capsule-crm
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Capsule CRM

Your receptionist can recognize callers who are already in Capsule, add new callers as contacts, note what each caller wanted, and create a follow-up task for your team. Looking up callers uses a [webhook tool](/docs/reception-ai/integrations/webhooks). Adding contacts, notes, and tasks goes through [Zapier](/docs/reception-ai/integrations/zapier), because Capsule's API needs nested request bodies for those, which webhook tools can't send.

## Look up callers

### Create an API token

In Capsule, open **My Preferences** → **API Authentication Tokens** and generate a new token. Name it, for example `Reception.ai`. The token acts as you, so it can see and change what you can.

> **Warning**
>
> Anyone with the token can read and change your Capsule data. Keep it out of shared documents, and
> delete it in Capsule if it leaks.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_capsule_contact`                                                                                                                   |
| **Description**      | "Find the caller in our CRM by phone number, name, or email. Use it at the start of a call to check whether they're an existing client." |
| **Method**           | GET                                                                                                                                      |
| **URL**              | `https://api.capsulecrm.com/api/v2/parties/search`                                                                                       |
| **Request Headers**  | `Authorization`: `Bearer ` followed by your token                                                                                        |
| **Query Parameters** | `q` (string, required): "The caller's phone number, full name, or email address."                                                        |
| **Assign to agents** | **Receptionist**                                                                                                                         |

Select **Enable**. The search returns the same results as Capsule's own search bar.

## Add contacts, notes, and tasks

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Capsule actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), connect your Capsule CRM account and add the [actions below](#actions). For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action as listed.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call from a number saved on a Capsule contact, then as a new caller who asks for a callback. The new contact, a note, and a task appear in Capsule.

## Actions

### Add the caller

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| **Zapier action**      | **Create Contact**                                      |
| **Set in Zapier**      | The type (Person), the owner, and any tags.             |
| **Let the AI fill in** | First name, last name, phone number, and email address. |
| **Assign to**          | **Client**                                              |

### Log a note

| Field                  | Value                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Zapier action**      | **Add Note to Entity**                                                             |
| **Set in Zapier**      | The kind of record to add the note to: a contact.                                  |
| **Let the AI fill in** | The contact's ID (from `find_capsule_contact` or **Create Contact**) and the note. |
| **Assign to**          | **Client**                                                                         |

### Create a follow-up task

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| **Zapier action**      | **Create Task**                                               |
| **Set in Zapier**      | The team member who handles callbacks.                        |
| **Let the AI fill in** | The description, due date, and the contact the task is about. |
| **Assign to**          | **Client**                                                    |

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) so your receptionist
> searches for the caller first and only creates a contact when no match is found.

## Limitations

* Zapier's Capsule app can't check anyone's availability, so your receptionist can't book meetings in Capsule. Use the follow-up task instead, or Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar).
* Each Zapier action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                         | What to check                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 401 from Capsule                                | Start the header value with `Bearer ` and a space, and check that the token hasn't been deleted.  |
| Known callers aren't found                      | Capsule matches phone numbers as stored. Store numbers in one format, or search by name or email. |
| The receptionist creates duplicate contacts     | Tell it in the lookup tool's description to add a contact only when the caller wasn't found.      |
| A Capsule action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                |
| An action shows **Changed** and isn't used      | You edited it in Zapier. Select **Update** in the **Tools** tab.                                  |
