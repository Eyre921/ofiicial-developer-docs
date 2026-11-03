---
title: "Keap"
source: https://elevenlabs.io/docs/reception-ai/integrations/keap.md
path: docs/reception-ai/integrations/keap
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Keap

Your receptionist can recognize callers who are already in Keap, add new callers as contacts, note what each caller wanted, and create a follow-up task for your team. Keap's API stores email addresses and phone numbers as nested lists, which webhook tools can't send, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Keap actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and connect your Keap account. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action as listed.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who asks for a callback. The contact, a note, and a task appear in Keap.

## Actions

### Find the caller

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| **Zapier action**      | **Find Contact**                                            |
| **Set in Zapier**      | **Field**: the field you search by, such as email or phone. |
| **Let the AI fill in** | **Value**: the caller's email address or phone number.      |
| **Assign to**          | **Client**                                                  |

### Add or update the caller

| Field                  | Value                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create or Update Contact**                                                                   |
| **Set in Zapier**      | **Check for Duplicates Using** (for example, email), the lead source, the owner, and any tags. |
| **Let the AI fill in** | First name, last name, email address, and phone number.                                        |
| **Assign to**          | **Client**                                                                                     |

> **Warning**
>
> Don't set the contact's opt-in from a call unless you're sure a spoken yes counts as marketing
> consent where you and your callers are.

### Log a note

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| **Zapier action**      | **Create Note**                                                     |
| **Set in Zapier**      | **Type**, for example a call note.                                  |
| **Let the AI fill in** | **Contact Id** (from the previous action), **Title**, and **Body**. |
| **Assign to**          | **Client**                                                          |

### Create a follow-up task

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| **Zapier action**      | **Create Task**                                               |
| **Set in Zapier**      | **User Id**: the team member who handles callbacks.           |
| **Let the AI fill in** | **Title**, **Due Date**, **Description**, and **Contact Id**. |
| **Assign to**          | **Client**                                                    |

> **Tip**
>
> To start a Keap campaign for new callers, add the **Tag Contact** action with the campaign's tag
> set as a fixed value.

## Limitations

* Zapier's Keap app can't check availability or book appointments, so your receptionist can't schedule meetings in Keap. Use the follow-up task instead, or Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar).
* **Create or Update Contact** only spots duplicates by the field you chose. A caller who gives a new email address may be added twice.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                      | What to check                                                                                 |
| -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| A Keap action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.            |
| An action shows **Changed** and isn't used   | You edited it in Zapier. Select **Update** in the **Tools** tab.                              |
| Known callers aren't found                   | Keap matches values as stored. Search by email, or store phone numbers in one format.         |
| Notes or tasks aren't linked to the caller   | Your receptionist needs the contact ID from **Find Contact** or **Create or Update Contact**. |
