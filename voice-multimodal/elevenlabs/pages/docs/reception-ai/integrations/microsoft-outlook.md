---
title: "Microsoft Outlook"
source: https://elevenlabs.io/docs/reception-ai/integrations/microsoft-outlook.md
path: docs/reception-ai/integrations/microsoft-outlook
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Microsoft Outlook

Your receptionist can see what's already on your Outlook calendar, add an event for an appointment it has agreed with a caller, and email your team a message from a call. Microsoft's calendar and mail API (Microsoft Graph) only accepts OAuth sign-ins, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

> **Note**
>
> This isn't the same as Reception's built-in booking. Your receptionist reads a list of events, not
> your open slots, and nothing stops two callers from taking the same time. Use it to log
> appointments and send emails. For real-time booking based on availability, use Reception's own
> booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar),
> [Calendly](/docs/reception-ai/integrations/calendly), or
> [Cal.com](/docs/reception-ai/integrations/cal-com).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Outlook actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) from the **Microsoft Outlook** app and sign in to your Microsoft account when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action as listed.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking for an appointment tomorrow, then leaving a message. The event appears in your calendar and the email arrives.

## Actions

### Check the calendar

| Field                  | Value                                                                      |
| ---------------------- | -------------------------------------------------------------------------- |
| **Zapier action**      | **Get Calendar Events in Date Range**                                      |
| **Set in Zapier**      | **Calendar**.                                                              |
| **Let the AI fill in** | **Start Date & Time** and **End Date & Time** of the day the caller wants. |
| **Assign to**          | **Client** and **Assistant**                                               |

Your receptionist sees each event's details, including its subject. Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling it to only tell callers whether a time is free, and never what's on the calendar. Assigned to the **Assistant**, the same action answers questions like "What's on my calendar tomorrow?".

### Add an event

| Field                  | Value                                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Event**                                                                                                      |
| **Set in Zapier**      | **Calendar**, and **Show me as Free or Busy** set to busy.                                                            |
| **Let the AI fill in** | **Subject**, **Start Date & Time**, **End Date & Time**, and **Description** (the caller's name, number, and reason). |
| **Assign to**          | **Client**                                                                                                            |

Leave **Attendees** empty unless you want Outlook to send the caller a meeting invitation. If you do let the AI fill it in, ask your receptionist to spell the email address back first.

### Email your team

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| **Zapier action**      | **Send Email**                                                    |
| **Set in Zapier**      | **To Email(s)**: your team's address. **Body Format**: text.      |
| **Let the AI fill in** | **Subject** and **Body**: the caller's name, number, and message. |
| **Assign to**          | **Client**                                                        |

> **Warning**
>
> Keep **To Email(s)** fixed. If the AI fills it in, a caller could get your receptionist to send
> email from your account to any address.

## Limitations

* Your receptionist can't see open slots, business hours, or buffers, only existing events. Two callers can book the same time if both calls happen before either event is created.
* Your receptionist can't move or cancel events.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                          | What to check                                                                                  |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| An Outlook action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.             |
| An action shows **Changed** and isn't used       | You edited it in Zapier. Select **Update** in the **Tools** tab.                               |
| Events land at the wrong time                    | Check the time zone of your Outlook calendar, and ask your receptionist to read the time back. |
| The calendar looks empty                         | Check that **Calendar** is set to the calendar you use for appointments.                       |
