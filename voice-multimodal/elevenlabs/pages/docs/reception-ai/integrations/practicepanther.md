---
title: "PracticePanther"
source: https://elevenlabs.io/docs/reception-ai/integrations/practicepanther.md
path: docs/reception-ai/integrations/practicepanther
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# PracticePanther

Your receptionist can find a caller in PracticePanther or add them as a new contact, log the call, and create a follow-up task for your team. PracticePanther's API uses OAuth and is only available on request, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the PracticePanther actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to PracticePanther when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who asks for a consultation. The contact, the call log, and a task appear in PracticePanther.

## Actions

### Find or add the caller

| Field                  | Value                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Zapier action**      | **Find or Create Contact**                                                                                               |
| **Set in Zapier**      | **User**: the team member new contacts are assigned to. **Tags**, for example `Reception`.                               |
| **Let the AI fill in** | **Search Text** (the caller's name, email, or phone number), **First Name**, **Last Name**, **Email**, and **Mobile #**. |
| **Assign to**          | **Client**                                                                                                               |

### Log the call

| Field                  | Value                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| **Zapier action**      | **Create Call Log**                                                                              |
| **Set in Zapier**      | **User** and **Direction** (inbound).                                                            |
| **Let the AI fill in** | **Contact** (from the previous action), **Subject**, **Date/Time**, **Duration**, and **Notes**. |
| **Assign to**          | **Client**                                                                                       |

### Create a follow-up task

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| **Zapier action**      | **Create Task**                                        |
| **Set in Zapier**      | **User**: the team member who handles callbacks.       |
| **Let the AI fill in** | **Contact**, **Subject**, **Notes**, and **Due Date**. |
| **Assign to**          | **Client**                                             |

### Open a matter

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| **Zapier action**      | **Create Matter**                                           |
| **Set in Zapier**      | **Status**: the status you use for new inquiries. **User**. |
| **Let the AI fill in** | **Contact**, **Matter Name**, and **Notes**.                |
| **Assign to**          | **Client**                                                  |

> **Note**
>
> If your firm runs a conflict check before opening a matter, leave **Create Matter** out and let
> your team open matters from the follow-up task.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's PracticePanther app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                                 | What to check                                                                                   |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| A PracticePanther action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.              |
| An action shows **Changed** and isn't used              | You edited it in Zapier. Select **Update** in the **Tools** tab.                                |
| Returning callers are added twice                       | PracticePanther matches values as stored. Ask your receptionist to search by email when it can. |
| Call logs or tasks aren't linked to the caller          | Your receptionist needs the contact from **Find or Create Contact**. Run it first.              |
