---
title: "Filevine"
source: https://elevenlabs.io/docs/reception-ai/integrations/filevine.md
path: docs/reception-ai/integrations/filevine
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Filevine

Your receptionist can find a caller in Filevine or add them as a new contact, and open an intake project for a new inquiry. Filevine's API needs a token that expires after a short time, which Reception's connectors can't renew, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

> **Note**
>
> Zapier's Filevine app works with Filevine contacts and projects. It has no action for Lead Docket,
> so it can't add leads to your Lead Docket intake.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Filevine actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and connect your Filevine account when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller looking for a lawyer. The contact and an intake project appear in Filevine.

## Actions

### Find or add the caller

| Field                  | Value                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Zapier action**      | **Find or Create Contact**                                                                             |
| **Set in Zapier**      | **Field**: the contact field to search by, for example phone. **Contact Types**: the type for callers. |
| **Let the AI fill in** | The search value, first name, last name, **Phone Numbers**, and **Email Addresses**.                   |
| **Assign to**          | **Client**                                                                                             |

### Open an intake project

| Field                  | Value                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Zapier action**      | **Create Project**                                                                                     |
| **Set in Zapier**      | **Project Type**: the project type you use for intake.                                                 |
| **Let the AI fill in** | **Contact** (from the previous action), the project name, and the incident date if the caller has one. |
| **Assign to**          | **Client**                                                                                             |

> **Note**
>
> If your firm runs a conflict check before opening a project, leave **Create Project** out and let
> your team open projects from the call summary.

> **Warning**
>
> Add a [rule](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to
> take down the caller's details and never give legal advice.

## Limitations

* Zapier's Filevine app has no action for notes or tasks, so your receptionist can't log the call or assign a follow-up in Filevine. Your team gets the details from Reception's [post-call summaries](/docs/reception-ai/features/notifications).
* Zapier's Filevine app can't check availability, so your receptionist can't offer open times. For real-time booking, use Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar), [Calendly](/docs/reception-ai/integrations/calendly), or [Cal.com](/docs/reception-ai/integrations/cal-com).
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                          | What to check                                                                                    |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| A Filevine action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.               |
| An action shows **Changed** and isn't used       | You edited it in Zapier. Select **Update** in the **Tools** tab.                                 |
| Returning callers are added twice                | Filevine matches values as stored. Store phone numbers in one format, or set **Field** to email. |
| Projects aren't linked to the caller             | Your receptionist needs the contact from **Find or Create Contact**. Run it first.               |
| Leads don't reach Lead Docket                    | Zapier's Filevine app writes to Filevine projects. Check the project list in Filevine.           |
