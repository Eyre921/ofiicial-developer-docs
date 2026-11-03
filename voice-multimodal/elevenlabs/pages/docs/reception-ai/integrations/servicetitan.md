---
title: "ServiceTitan"
source: https://elevenlabs.io/docs/reception-ai/integrations/servicetitan.md
path: docs/reception-ai/integrations/servicetitan
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ServiceTitan

Your receptionist can look up callers in ServiceTitan, send new work as a booking for your call takers to review, and tell existing customers when their next appointment is. ServiceTitan's API exchanges a client ID and secret for short-lived tokens and also needs an app key, which webhook tools can't do, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

## Before you start

ServiceTitan's Zapier integration is in open beta, and ServiceTitan provides it as is. To connect it:

1. A ServiceTitan administrator submits ServiceTitan's Zapier registration form. ServiceTitan contacts you with next steps.
2. In ServiceTitan, go to **Settings** → **Integrations** → **API Application Access**, select **Connect New App**, and choose **Zapier 3.0.X**.
3. Review the scopes, choose a **Booking Provider** option, and select **Allow Access**.
4. Generate a client secret and copy it, along with the client ID and your tenant ID.

> **Warning**
>
> The client secret gives access to your ServiceTitan data. Store it safely and don't share it.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the ServiceTitan actions

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the [actions below](#actions) from the **ServiceTitan (3.0.X)** app. To connect, enter your tenant ID, client ID, and client secret, and choose the production environment. For each field, either set a fixed value or let the AI fill it in, as listed.

### Assign the tools

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign each action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a repair. The booking appears in ServiceTitan for your team to review.

## Actions

### Find the caller

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| **Zapier action**      | **Search Customers**                         |
| **Set in Zapier**      | Nothing.                                     |
| **Let the AI fill in** | **Phone** (the caller's number) or **Name**. |
| **Assign to**          | **Client**                                   |

### Send a booking

A booking is the safest way to send new work. Your call takers review it in ServiceTitan and turn it into a job, so your receptionist never books over your dispatch board.

| Field                  | Value                                                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Booking**                                                                                                                                                                                       |
| **Set in Zapier**      | **Booking Provider**, **Source** (for example, `Reception`), and optionally **Business Unit**, **Job Type**, and **Campaign**.                                                                           |
| **Let the AI fill in** | **Name**, **Summary** (the problem, the caller's phone number, and when they're available), **Is First Time Client**, the service address, **Start** (the caller's preferred time), and **External Id**. |
| **Assign to**          | **Client**                                                                                                                                                                                               |

**External Id** must be unique for every booking. Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist to use the caller's phone number followed by the current date and time.

### Check a customer's appointments

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| **Zapier action**      | **Search Appointments**                     |
| **Set in Zapier**      | Nothing.                                    |
| **Let the AI fill in** | **Customer Id**, from **Search Customers**. |
| **Assign to**          | **Client**                                  |

## Limitations

* Zapier's ServiceTitan app can't check capacity or technician availability, so the time on a booking is the caller's preference, not a confirmed slot.
* **Create Job** and **Create Appointment** need IDs for the location, business unit, job type, and campaign, and book straight onto your schedule. Leave them to your call takers.
* The integration is in open beta and ServiceTitan doesn't officially support it.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the actions stop until it resets.

## Troubleshooting

| Problem                                              | What to check                                                                                                  |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| A ServiceTitan action doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                             |
| An action shows **Changed** and isn't used           | You edited it in Zapier. Select **Update** in the **Tools** tab.                                               |
| Zapier can't connect to ServiceTitan                 | Check that your registration was approved, and that you used a 3.0.X client ID and secret, not an old API key. |
| `UniqueConstraint` error on a booking                | **External Id** repeated an earlier booking. Make sure it includes the date and time.                          |
| Known customers aren't found                         | Try the caller's name as well as their phone number.                                                           |
