---
title: "Smokeball"
source: https://elevenlabs.io/docs/reception-ai/integrations/smokeball.md
path: docs/reception-ai/integrations/smokeball
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Smokeball

Your receptionist can recognize callers who are already in Smokeball, add new callers as contacts and leads, and create a follow-up task for your team. Smokeball's API uses OAuth and requires registering as a Smokeball partner, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Smokeball actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions). When Zapier asks, confirm your Smokeball region and sign in with your Smokeball username and password. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller looking for a lawyer. The contact, the lead, and a task appear in Smokeball.

## Actions

### Find the caller

| Field                  | Value                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Find Contact**                                                                               |
| **Set in Zapier**      | Nothing.                                                                                       |
| **Let the AI fill in** | **Contact number (mobile, home or work)**, and **Name** or **Email** if the caller gives them. |
| **Assign to**          | **Client**                                                                                     |

### Add a new caller

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| **Zapier action**      | **Create Person Contact**                                    |
| **Set in Zapier**      | Nothing required.                                            |
| **Let the AI fill in** | The caller's first name, last name, phone number, and email. |
| **Assign to**          | **Client**                                                   |

### Add a new lead

In Smokeball, a lead is a potential matter. Your team converts it to a matter once the firm takes the case.

| Field                  | Value                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Lead**                                                                                                                                 |
| **Set in Zapier**      | **Lead Type**: the type you use for phone inquiries. **Person Responsible**: the staff member who handles new inquiries.                        |
| **Let the AI fill in** | **Description** (a short, factual summary of what the caller needs), and the caller's contact if Zapier shows a client field for the lead type. |
| **Assign to**          | **Client**                                                                                                                                      |

### Create a follow-up task

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Task**                                                                         |
| **Set in Zapier**      | **Created By** and **Assignees**: the staff member who handles callbacks.               |
| **Let the AI fill in** | **Name**, **Details** (who called, their number, and what they need), and **Due Date**. |
| **Assign to**          | **Client**                                                                              |

> **Note**
>
> Opening a matter usually comes after a conflict check, so this guide leaves **Create Matter** to
> your team.

> **Tip**
>
> To let your receptionist put consultations on the firm's calendar, add **Create Calendar Event**
> with **Organizer** and **Attendees** set to fixed values. It doesn't check for conflicts, so agree
> on the time with the caller as a request and have your team confirm it.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's Smokeball app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                           | What to check                                                                               |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| A Smokeball action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.          |
| An action shows **Changed** and isn't used        | You edited it in Zapier. Select **Update** in the **Tools** tab.                            |
| Zapier can't connect to Smokeball                 | Check that you chose the region your firm's Smokeball account is in.                        |
| Returning callers are added twice                 | Add a procedure so your receptionist runs **Find Contact** before creating a contact.       |
| Known callers aren't found                        | Check that phone numbers in Smokeball are stored in one format, or search by email instead. |
