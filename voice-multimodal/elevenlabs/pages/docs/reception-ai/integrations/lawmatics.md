---
title: "Lawmatics"
source: https://elevenlabs.io/docs/reception-ai/integrations/lawmatics.md
path: docs/reception-ai/integrations/lawmatics
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Lawmatics

Your receptionist can recognize callers who are already in Lawmatics, open a new matter for each new inquiry, and request a consultation on your calendar. Lawmatics' API uses an OAuth sign-in and needs developer settings that Lawmatics turns on by request, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Lawmatics actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and connect your Lawmatics account. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who wants a consultation. The matter appears in Lawmatics.

## Actions

### Find the caller

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| **Zapier action**      | **Find Contact**                      |
| **Set in Zapier**      | **Search Type**: phone.               |
| **Let the AI fill in** | **Value**: the caller's phone number. |
| **Assign to**          | **Client**                            |

### Open a matter for a new inquiry

In Lawmatics, a new matter is how a potential client enters your intake pipeline. **Create Matter** also records the caller's contact details, so you don't need a separate contact action.

| Field                  | Value                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Matter**                                                                                                   |
| **Set in Zapier**      | Nothing required.                                                                                                   |
| **Let the AI fill in** | **First Name**, **Last Name**, **Email**, **Phone**, **Case Title**, and **Case Blurb** (a short, factual summary). |
| **Assign to**          | **Client**                                                                                                          |

### Request a consultation

| Field                  | Value                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Appointment**                                                                                          |
| **Set in Zapier**      | **All Day**: no. **Attendee Type**: the record type you link appointments to.                                   |
| **Let the AI fill in** | **Attendee ID** (from the previous actions), **Event Name**, **Start Date**, **End Date**, and **Description**. |
| **Assign to**          | **Client**                                                                                                      |

**Create Appointment** doesn't check your calendar for conflicts. Ask your receptionist to offer the time as a request that your team confirms.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's Lawmatics app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                           | What to check                                                                                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| A Lawmatics action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                                            |
| An action shows **Changed** and isn't used        | You edited it in Zapier. Select **Update** in the **Tools** tab.                                                              |
| Known callers aren't found                        | Lawmatics matches phone numbers as stored. Store them in one format, or add a second **Find Contact** that searches by email. |
| Appointments aren't linked to the caller          | Check that **Attendee Type** matches the ID your receptionist passes (contact or matter).                                     |
