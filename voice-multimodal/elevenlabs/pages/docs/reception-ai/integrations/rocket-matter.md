---
title: "Rocket Matter"
source: https://elevenlabs.io/docs/reception-ai/integrations/rocket-matter.md
path: docs/reception-ai/integrations/rocket-matter
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Rocket Matter

Your receptionist can add new callers as contacts in Rocket Matter, with a short note on what they need, and create a follow-up task for an attorney or assistant. Reception connects to Rocket Matter through [Zapier](/docs/reception-ai/integrations/zapier), which handles the Rocket Matter sign-in.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Rocket Matter actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Rocket Matter when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Add a procedure for returning callers

Zapier's Rocket Matter app can't search contacts. Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to ask whether the caller is already a client, and to create a contact only for new callers.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller looking for a lawyer. The contact and a task appear in Rocket Matter.

## Actions

### Add a new caller

| Field                  | Value                                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Contact**                                                                                                                                   |
| **Set in Zapier**      | **Contact Type**: the type you use for potential clients. It must match a type set up in Rocket Matter.                                              |
| **Let the AI fill in** | **Contact Name** (first and last name), **Contact Email**, **Cell Phone Number**, and **Notes** (a short, factual summary of what the caller needs). |
| **Assign to**          | **Client**                                                                                                                                           |

### Create a follow-up task

| Field                  | Value                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Task**                                                                                            |
| **Set in Zapier**      | **Primary Assignee**: the team member who handles callbacks. **Choose the Priority**, for example Medium.  |
| **Let the AI fill in** | **Task name**, **Task Description** (who called, their number, and what they need), and **Task Due Date**. |
| **Assign to**          | **Client**                                                                                                 |

> **Note**
>
> Opening a matter usually comes after a conflict check, so this guide leaves **Create Matter** to
> your team.

> **Tip**
>
> To let your receptionist put consultations on the firm's calendar, add **Create Event** and let
> the AI fill in the event name, start and end times, and description. It doesn't check for
> conflicts, so agree on the time with the caller as a request and have your team confirm it.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's Rocket Matter app has no search actions, so your receptionist can't recognize callers who are already in Rocket Matter or look up their matters.
* Tasks and notes link to a matter by its file number, and new callers don't have one yet. Tasks for new callers aren't linked to a matter or contact.
* Zapier's Rocket Matter app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                               | What to check                                                                                   |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| A Rocket Matter action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.              |
| An action shows **Changed** and isn't used            | You edited it in Zapier. Select **Update** in the **Tools** tab.                                |
| **Create Contact** fails                              | Check that **Contact Type** matches a type set up in Rocket Matter exactly.                     |
| Returning callers are added twice                     | Check the procedure that tells your receptionist to ask whether the caller is already a client. |
| Tasks go to the wrong person                          | Set **Primary Assignee** to the team member's full name or login, as Rocket Matter shows it.    |
