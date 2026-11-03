---
title: "MyCase"
source: https://elevenlabs.io/docs/reception-ai/integrations/mycase.md
path: docs/reception-ai/integrations/mycase
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# MyCase

Your receptionist can recognize callers who are already in MyCase, add new callers as leads, and log every call in MyCase's call log for your team. MyCase's API uses OAuth and is only available on request on its Advanced tier, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Before you start

A MyCase admin user must connect MyCase to Zapier.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the MyCase actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to MyCase as an admin when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller looking for a lawyer. The lead and the call appear in MyCase.

## Actions

### Find the caller

| Field                  | Value                                                                         |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Zapier action**      | **Find Caller**                                                               |
| **Set in Zapier**      | **Search Type**, for example phone number.                                    |
| **Let the AI fill in** | **Search Value**: the caller's phone number, or what the search type expects. |
| **Assign to**          | **Client**                                                                    |

### Add a new lead

| Field                  | Value                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Lead**                                                                                                        |
| **Set in Zapier**      | The referral source, if you track one for phone leads.                                                                 |
| **Let the AI fill in** | First name, last name, cell phone number, email, and lead details (a short, factual summary of what the caller needs). |
| **Assign to**          | **Client**                                                                                                             |

### Log the call

| Field                  | Value                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Zapier action**      | **Create Call**                                                                                              |
| **Set in Zapier**      | **Call For**: the staff member who should follow up. **Resolved**: no, so the call stays open for your team. |
| **Let the AI fill in** | **Caller**, **Caller Phone Number**, **Called At**, and **Message**.                                         |
| **Assign to**          | **Client**                                                                                                   |

> **Tip**
>
> To let your receptionist put consultations on your calendar, add **Create Event** with **Required
> Staff** set to a fixed value. It doesn't check for conflicts, so treat the time as a request and
> have your team confirm it.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's MyCase app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                        | What to check                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| A MyCase action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.              |
| An action shows **Changed** and isn't used     | You edited it in Zapier. Select **Update** in the **Tools** tab.                                |
| Zapier shows a `Forbidden` error               | A MyCase admin user must connect MyCase to Zapier.                                              |
| Known callers aren't found                     | Check the **Search Type** in Zapier, and that phone numbers in MyCase are stored in one format. |
