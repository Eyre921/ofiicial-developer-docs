---
title: "Square Appointments"
source: https://elevenlabs.io/docs/reception-ai/integrations/square-appointments.md
path: docs/reception-ai/integrations/square-appointments
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Square Appointments

Your receptionist can find a caller in Square or add them as a customer, then create an appointment in Square Appointments for a time the caller asks for. Square's booking API expects nested objects that webhook tools can't send, and Square's MCP server requires an OAuth sign-in, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

> **Note**
>
> Zapier's Square app can't check open times, so your receptionist can't offer free slots or tell
> whether a time is taken. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar),
> [Calendly](/docs/reception-ai/integrations/calendly), or
> [Cal.com](/docs/reception-ai/integrations/cal-com).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Square actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Square when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who asks for an appointment. The customer and the appointment appear in Square.

## Actions

### Find the caller

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| **Zapier action**      | **Find Customer**                                            |
| **Set in Zapier**      | Nothing.                                                     |
| **Let the AI fill in** | **Phone Number** (the caller's number) or the email address. |
| **Assign to**          | **Client**                                                   |

### Add a new caller

| Field                  | Value                                                           |
| ---------------------- | --------------------------------------------------------------- |
| **Zapier action**      | **Create Customer**                                             |
| **Set in Zapier**      | Nothing.                                                        |
| **Let the AI fill in** | **First Name**, **Last Name**, phone number, and email address. |
| **Assign to**          | **Client**                                                      |

### Create an appointment

| Field                  | Value                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Appointment**                                                                                           |
| **Set in Zapier**      | **Location** and **Team Member ID**. **Appointment Service ID**, if you offer one service.                       |
| **Let the AI fill in** | **Customer ID** (from **Find Customer** or **Create Customer**), **Date and Time of Appointment**, and **Note**. |
| **Assign to**          | **Client**                                                                                                       |

If you offer several services, also add **Find Service** with **Location** set to a fixed value, and let the AI fill in **Appointment Service ID** from its result.

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) for bookings: find or add
> the caller, agree on a time, read the date and time back, then create the appointment.

## Limitations

* Your receptionist can't check availability. It books the time the caller asks for without seeing your calendar.
* With **Team Member ID** fixed, every appointment goes to the same team member. Your receptionist can't choose between staff.
* Your receptionist can't reschedule or cancel appointments.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                        | What to check                                                                                 |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| A Square action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.            |
| An action shows **Changed** and isn't used     | You edited it in Zapier. Select **Update** in the **Tools** tab.                              |
| **Create Appointment** fails                   | Check that the team member is bookable at the location and offers the service.                |
| Appointments land at the wrong time            | Check the time zone of your Square location, and ask your receptionist to read the time back. |
| Returning callers are added twice              | Add a procedure so your receptionist runs **Find Customer** before **Create Customer**.       |
