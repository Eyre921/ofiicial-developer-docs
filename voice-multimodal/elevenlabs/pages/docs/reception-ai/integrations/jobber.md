---
title: "Jobber"
source: https://elevenlabs.io/docs/reception-ai/integrations/jobber.md
path: docs/reception-ai/integrations/jobber
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Jobber

Your receptionist can find a caller in Jobber or add them as a new client, then create a request for the work they need, with the call details as a note. Jobber's API only works with OAuth apps, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Before you start

* Jobber's Zapier integration is available on the Connect, Grow, and Plus plans.
* Connect Zapier as a Jobber team member who will stay active. If that team member is deactivated, the Zapier connection stops working.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Jobber actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) and sign in to Jobber when Zapier asks. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a quote. The client and the request appear in Jobber.

## Actions

### Find or add the caller

| Field                  | Value                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Find or Create Client**                                                                                                   |
| **Set in Zapier**      | Nothing.                                                                                                                    |
| **Let the AI fill in** | **Client Search Term** (the caller's name or email), first and last name, email address, phone number, and service address. |
| **Assign to**          | **Client**                                                                                                                  |

If you only want your receptionist to recognize existing clients, add **Find Client** instead.

### Create a request

| Field                  | Value                                                                             |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Request**                                                                |
| **Set in Zapier**      | Nothing.                                                                          |
| **Let the AI fill in** | **Client** (from the previous action) and **Title**, a short summary of the work. |
| **Assign to**          | **Client**                                                                        |

### Add the call details

| Field                  | Value                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Add Note to Request**                                                                                                         |
| **Set in Zapier**      | Nothing.                                                                                                                        |
| **Let the AI fill in** | **Request ID** (from **Create Request**) and **Message**: what the caller needs, when they're available, and how to reach them. |
| **Assign to**          | **Client**                                                                                                                      |

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) for new work: find or add
> the caller, create the request, then add the note.

## Limitations

* Zapier's Jobber app can't read your schedule or book visits. Your receptionist collects the request, and your team schedules it in Jobber.
* **Create Request** always uses the client's first property. For clients with several properties, ask your receptionist to put the service address in the note.
* Zapier's Jobber search matches a name, email address, or company name, so ask returning callers for one of those.
* **Create Job** and **Create Quote** need line items, so leave them to your team.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                        | What to check                                                                               |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------- |
| A Jobber action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.          |
| An action shows **Changed** and isn't used     | You edited it in Zapier. Select **Update** in the **Tools** tab.                            |
| Returning callers are added twice              | Ask callers for the name or email on their account, and use it as the search term.          |
| Zapier says the Jobber connection expired      | The team member who connected Jobber may have been deactivated. Reconnect Jobber in Zapier. |
