---
title: "Service Fusion"
source: https://elevenlabs.io/docs/reception-ai/integrations/service-fusion.md
path: docs/reception-ai/integrations/service-fusion
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Service Fusion

Your receptionist can add a new caller to Service Fusion as a customer, then create an unscheduled job with the details of the work, or a calendar task so your team calls them back. Service Fusion's API uses OAuth access tokens that expire after an hour, which webhook tools can't renew, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Before you start

* Service Fusion's Zapier integration and API are only available on the Pro plan.
* Zapier asks you to sign in to Service Fusion when you connect it. Sign in as a user who will stay active.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Service Fusion actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Service Fusion when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a repair. The customer and the job appear in Service Fusion.

## Actions

### Add the caller

| Field                  | Value                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Customer**                                                                                                                      |
| **Set in Zapier**      | The referral source, for example `Reception`, if it exists in Service Fusion.                                                            |
| **Let the AI fill in** | **Customer Name** (the caller's full name or business name), first and last name, email, phone, the service address, and a private note. |
| **Assign to**          | **Client**                                                                                                                               |

### Create a job

| Field                  | Value                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Job**                                                                                                                                                      |
| **Set in Zapier**      | **Status**, for example `Unscheduled`, so your dispatcher schedules the job. Optionally the job category and source.                                                |
| **Let the AI fill in** | **Customer Name** (as used in **Create Customer**), the service address, and the description: what the caller needs, when they're available, and how to reach them. |
| **Assign to**          | **Client**                                                                                                                                                          |

Leave the start date and assigned techs empty, so your receptionist never books over your schedule.

### Ask for a callback

| Field                  | Value                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Zapier action**      | **Create Calendar Task**                                                                                           |
| **Set in Zapier**      | The task type, and the user the task is assigned to.                                                               |
| **Let the AI fill in** | The start date (today's date) and the description: the caller's name, phone number, and why they want a call back. |
| **Assign to**          | **Client**                                                                                                         |

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) for new work: add the
> caller, then create the job. For anything else, create a callback task.

## Limitations

* Zapier's Service Fusion app can't search customers, so your receptionist can't recognize returning callers. A returning caller who books new work can be added twice.
* Your receptionist can't check technician availability or book a time. The job holds the caller's preferred time in its description, and your team schedules it.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                                | What to check                                                                                   |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| A Service Fusion action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.              |
| An action shows **Changed** and isn't used             | You edited it in Zapier. Select **Update** in the **Tools** tab.                                |
| Zapier can't connect to Service Fusion                 | Check that your account is on the Pro plan, and that the user you signed in as is still active. |
| A job isn't linked to the new customer                 | **Customer Name** in **Create Job** must match the name used in **Create Customer** exactly.    |
| **Create Job** fails on the status                     | **Status** must be one of the job statuses in your Service Fusion account.                      |
