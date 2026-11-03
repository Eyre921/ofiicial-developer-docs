---
title: "Zendesk"
source: https://elevenlabs.io/docs/reception-ai/integrations/zendesk.md
path: docs/reception-ai/integrations/zendesk
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Zendesk

Your receptionist can recognize callers who are already in Zendesk, open a ticket when a caller reports a problem, and add the caller's update to an existing ticket. Zendesk's API expects ticket fields nested inside a `ticket` object, which webhook tools can't send, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Zendesk actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Zendesk when Zapier asks. Connect as an agent with access to the groups your receptionist should file tickets in. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a caller reporting a problem. The ticket appears in Zendesk.

## Actions

### Find the caller

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| **Zapier action**      | **Find a User**                                               |
| **Set in Zapier**      | Nothing.                                                      |
| **Let the AI fill in** | **Query**: the caller's email address, phone number, or name. |
| **Assign to**          | **Client**                                                    |

### Open a ticket

| Field                  | Value                                                                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Ticket**                                                                                                                                       |
| **Set in Zapier**      | **Group**, **Priority**, **Tags** (for example, `phone`), and **Should the first Comment be public?**.                                                  |
| **Let the AI fill in** | **Subject**, **First Comment/Description** (the problem, the caller's phone number, and steps they tried), **Requester Name**, and **Requester Email**. |
| **Assign to**          | **Client**                                                                                                                                              |

The ticket has no phone field, so tell your receptionist to put the caller's number in the description.

> **Warning**
>
> If the first comment is public and the caller gives an email address, Zendesk's default triggers
> can email the ticket to that address. Ask your receptionist to spell the address back before
> creating the ticket.

### Add an update to a ticket

| Field                  | Value                                                                             |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Zapier action**      | **Add Comment to Ticket**                                                         |
| **Set in Zapier**      | **Should the Comment be public?**: no, so updates from calls stay internal notes. |
| **Let the AI fill in** | **Ticket** (the number the caller gives) and **Comment body**.                    |
| **Assign to**          | **Client**                                                                        |

> **Tip**
>
> For callers with no email address, add **Create User** so your receptionist can save their name
> and phone number in Zendesk.

## Limitations

* Your receptionist can't read a ticket's status or history back to callers with these actions. It adds updates; your agents reply.
* **Find a User** returns one match. Callers who share a phone number or name may be matched to the wrong user.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                         | What to check                                                                                      |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| A Zendesk action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                 |
| An action shows **Changed** and isn't used      | You edited it in Zapier. Select **Update** in the **Tools** tab.                                   |
| Tickets land in the wrong group                 | Check the fixed **Group**, and that the connected agent belongs to it.                             |
| Comments fail on a ticket                       | Check the ticket number, and that the ticket isn't closed. Closed tickets can't take new comments. |
| Callers get unexpected emails                   | Set **Should the first Comment be public?** to no, or check your Zendesk triggers.                 |
