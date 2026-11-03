---
title: "Clio"
source: https://elevenlabs.io/docs/reception-ai/integrations/clio.md
path: docs/reception-ai/integrations/clio
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Clio

Your receptionist can recognize callers who are already in Clio, add new callers as contacts, log each call as a communication, and create a follow-up task for an attorney or assistant. Clio's API only accepts OAuth sign-ins, which Reception's connectors don't support, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

> **Note**
>
> Zapier's Clio app works with Clio Manage. It doesn't add leads to a Clio Grow inbox.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Clio actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Clio when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller with a legal question. The contact, the call, and a task appear in Clio.

## Actions

### Find the caller

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| **Zapier action**      | **Find Person Contact**                                      |
| **Set in Zapier**      | Nothing.                                                     |
| **Let the AI fill in** | **Search Value**: the caller's name, phone number, or email. |
| **Assign to**          | **Client**                                                   |

### Add a new caller

| Field                  | Value                                                                   |
| ---------------------- | ----------------------------------------------------------------------- |
| **Zapier action**      | **Create Person Contact**                                               |
| **Set in Zapier**      | Nothing.                                                                |
| **Let the AI fill in** | **First name**, **Last name**, **Phone Number**, and **Email Address**. |
| **Assign to**          | **Client**                                                              |

### Log the call

| Field                  | Value                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Communication**                                                                             |
| **Set in Zapier**      | **Type of Communication**: phone.                                                                    |
| **Let the AI fill in** | **Subject**, **Body** (who called, their number, and what they need), and **Date of Communication**. |
| **Assign to**          | **Client**                                                                                           |

### Create a follow-up task

| Field                  | Value                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Task**                                                                    |
| **Set in Zapier**      | **Type of Assignee** and the assignee, **Task Priority**, and **Notify Assignee**. |
| **Let the AI fill in** | **Name**, **Description**, and **Task Due Date**.                                  |
| **Assign to**          | **Client**                                                                         |

> **Note**
>
> Opening a matter usually comes after a conflict check, so this guide leaves **Create Matter** to
> your team.

> **Tip**
>
> To let your receptionist put consultations on the firm's calendar, add **Create Calendar Entry**
> with **Calendar** set to a fixed value. It doesn't check for conflicts, so agree on the time with
> the caller as a request and have your team confirm it.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's Clio app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                      | What to check                                                                                 |
| -------------------------------------------- | --------------------------------------------------------------------------------------------- |
| A Clio action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.            |
| An action shows **Changed** and isn't used   | You edited it in Zapier. Select **Update** in the **Tools** tab.                              |
| Leads don't reach Clio Grow                  | Zapier's Clio app writes to Clio Manage. Check the contact under **Contacts** in Clio Manage. |
| Returning callers are added twice            | Add a procedure so your receptionist runs **Find Person Contact** before creating a contact.  |
