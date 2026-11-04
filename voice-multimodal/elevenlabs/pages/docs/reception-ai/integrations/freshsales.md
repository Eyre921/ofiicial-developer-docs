---
title: "Freshsales"
source: https://elevenlabs.io/docs/reception-ai/integrations/freshsales.md
path: docs/reception-ai/integrations/freshsales
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Freshsales

Your receptionist can recognize callers who are already in Freshsales, add new callers as contacts, note what each caller wanted, and create a follow-up task for your team. Reception connects through [Zapier](/docs/reception-ai/integrations/zapier). Freshsales' API can only look contacts up by name or email, not by phone number, and it needs nested request bodies to create records, which webhook tools can't send.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Freshsales actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) from the **Freshsales Suite** app and connect your Freshsales account. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action as listed.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who asks for a callback. The contact, a note, and a task appear in Freshsales.

## Actions

### Find the caller

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| **Zapier action**      | **Find Contact by Unique Fields**                   |
| **Set in Zapier**      | The field to search by: the phone number.           |
| **Let the AI fill in** | The value to search for: the caller's phone number. |
| **Assign to**          | **Client**                                          |

### Add the caller

| Field                  | Value                                                                |
| ---------------------- | -------------------------------------------------------------------- |
| **Zapier action**      | **Create Contact**                                                   |
| **Set in Zapier**      | The sales owner, the lead source, the lifecycle stage, and any tags. |
| **Let the AI fill in** | First name, last name, mobile number, and email address.             |
| **Assign to**          | **Client**                                                           |

### Log a note

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| **Zapier action**      | **Add Note**                                                  |
| **Set in Zapier**      | The module: Contact.                                          |
| **Let the AI fill in** | The contact ID (from the previous actions) and the note text. |
| **Assign to**          | **Client**                                                    |

### Create a follow-up task

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| **Zapier action**      | **Create Task**                                           |
| **Set in Zapier**      | The module (Contact) and the owner who handles callbacks. |
| **Let the AI fill in** | The title, due date, description, and contact ID.         |
| **Assign to**          | **Client**                                                |

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) so your receptionist
> searches for the caller first and only creates a contact when no match is found.

## Limitations

* Freshsales doesn't allow two contacts with the same mobile number or email address, so **Create Contact** fails for a caller who is already saved. Your receptionist should search first.
* Zapier's Freshsales app can't check anyone's availability, so your receptionist can't safely book meetings in Freshsales. Use the follow-up task instead, or Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                            | What to check                                                                                        |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| A Freshsales action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                   |
| An action shows **Changed** and isn't used         | You edited it in Zapier. Select **Update** in the **Tools** tab.                                     |
| Known callers aren't found                         | Freshsales matches phone numbers as stored. Store numbers in one format, or also search by email.    |
| Creating a contact fails                           | The caller may already be saved with that mobile number or email. Search for them first.             |
| Notes or tasks aren't linked to the caller         | Your receptionist needs the contact ID from **Find Contact by Unique Fields** or **Create Contact**. |
