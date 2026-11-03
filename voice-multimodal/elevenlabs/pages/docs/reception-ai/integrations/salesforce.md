---
title: "Salesforce"
source: https://elevenlabs.io/docs/reception-ai/integrations/salesforce.md
path: docs/reception-ai/integrations/salesforce
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Salesforce

Your receptionist can recognize callers who are already in Salesforce, add new callers as leads, and create a follow-up task for your team. Salesforce's API and its hosted MCP server only accept OAuth sign-ins, which Reception's connectors don't support, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Before you start

* Salesforce is a premium app on Zapier, so you need a paid Zapier plan.
* Zapier works with Sales Cloud and Service Cloud, including Essentials. Your org needs My Domain set up, and a Salesforce admin may need to approve Zapier before you can connect.
* Connect Zapier as a Salesforce user who can read and create leads, contacts, and tasks.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Salesforce actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and connect your Salesforce account. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action as listed.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who wants a quote. A lead and a follow-up task appear in Salesforce.

## Actions

### Find the caller

| Field                  | Value                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Zapier action**      | **Find Record**                                                                    |
| **Set in Zapier**      | **Salesforce Object**: Contact (or Lead). **Field to Search By**: the phone field. |
| **Let the AI fill in** | **Search Value**: the caller's phone number.                                       |
| **Assign to**          | **Client**                                                                         |

Add a second **Find Record** action with **Salesforce Object** set to Lead if you want to search both contacts and leads.

### Create a lead

| Field                  | Value                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Lead**                                                                                                |
| **Set in Zapier**      | **Lead Source** (for example, Phone), **Lead Status**, and the owner.                                          |
| **Let the AI fill in** | **First Name**, **Last Name**, **Company**, **Phone**, **Email**, and **Description** (what the caller wants). |
| **Assign to**          | **Client**                                                                                                     |

Salesforce requires a company on every lead. If the caller is a private person, tell your receptionist to use their full name as the company.

### Create a follow-up task

| Field                  | Value                                                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Record**                                                                                                         |
| **Set in Zapier**      | **Salesforce Object**: Task. The assignee, **Status**, and **Priority**.                                                  |
| **Let the AI fill in** | **Subject**, the due date, the comments (caller's name, number, and request), and the contact or lead ID from the search. |
| **Assign to**          | **Client**                                                                                                                |

### Run a report

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| **Zapier action**      | **Run Report**                                               |
| **Set in Zapier**      | The report, for example this week's new leads.               |
| **Let the AI fill in** | Nothing, unless you want to let it set the report's filters. |
| **Assign to**          | **Assistant**                                                |

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) so your receptionist
> searches for the caller first and only creates a lead when no match is found.

## Limitations

* Zapier's Salesforce app can't check anyone's availability, so your receptionist can't book meetings in Salesforce. Use the follow-up task instead, or Reception's own booking with [Google Calendar](/docs/reception-ai/integrations/google-calendar).
* **Find Record** returns one match. Callers who share a phone number may be matched to the wrong record.
* Each action call counts against your Salesforce org's API request limits.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                            | What to check                                                                                     |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| A Salesforce action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                |
| An action shows **Changed** and isn't used         | You edited it in Zapier. Select **Update** in the **Tools** tab.                                  |
| Known callers aren't found                         | Salesforce matches phone numbers as stored. Store numbers in one format, or also search by email. |
| Creating a lead fails                              | Check that **Last Name** and **Company** are filled, and any fields your org has made required.   |
| Zapier can't connect to Salesforce                 | Ask your Salesforce admin to approve Zapier in your org and check that My Domain is set up.       |
