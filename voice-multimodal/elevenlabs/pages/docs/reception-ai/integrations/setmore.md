---
title: "Setmore"
source: https://elevenlabs.io/docs/reception-ai/integrations/setmore.md
path: docs/reception-ai/integrations/setmore
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Setmore

Your receptionist can add a caller to Setmore as a contact and create an appointment for a time the caller asks for. Setmore's API needs a Pro plan, approval from Setmore, and access tokens that expire and must be refreshed, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

> **Note**
>
> Zapier's Setmore app can't check open times or look up existing appointments, so your receptionist
> can't offer free slots. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar),
> [Calendly](/docs/reception-ai/integrations/calendly), or
> [Cal.com](/docs/reception-ai/integrations/cal-com).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Setmore actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) from the **Setmore Appointments** app and sign in to Setmore when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking for an appointment. Check which staff calendar and service the appointment lands on in Setmore.

## Actions

### Create an appointment

| Field                  | Value                                                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Appointment**                                                                                                                             |
| **Set in Zapier**      | Nothing required.                                                                                                                                  |
| **Let the AI fill in** | **First Name**, **Last Name**, **Customer Email**, **Customer Mobile**, **Start Date**, **End Date**, and **Notes** (what the appointment is for). |
| **Assign to**          | **Client**                                                                                                                                         |

Setmore requires the customer's email for every appointment, so your receptionist must ask for it. Ask it to spell the address back to the caller.

### Add a contact

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| **Zapier action**      | **Create Contact**                                                     |
| **Set in Zapier**      | Nothing.                                                               |
| **Let the AI fill in** | **First Name**, **Last Name**, **Email**, **Phone**, and **Comments**. |
| **Assign to**          | **Client**                                                             |

Use it for callers who want to be added to your customer list without booking.

## Limitations

* Your receptionist can't check availability, find existing appointments, or reschedule or cancel them.
* Zapier's **Create Appointment** has no staff or service field. Check in your first test which staff member and service Setmore uses, and tell your team to adjust appointments that need someone else.
* Zapier's Setmore app has no search, so a returning caller can be added twice.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                         | What to check                                                                                  |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| A Setmore action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.             |
| An action shows **Changed** and isn't used      | You edited it in Zapier. Select **Update** in the **Tools** tab.                               |
| **Create Appointment** fails                    | Check that the caller gave an email address and that the start time is a full date and time.   |
| Appointments land at the wrong time             | Check the time zone in your Setmore settings, and ask your receptionist to read the time back. |
