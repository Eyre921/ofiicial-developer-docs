---
title: "Workiz"
source: https://elevenlabs.io/docs/reception-ai/integrations/workiz.md
path: docs/reception-ai/integrations/workiz
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Workiz

Your receptionist can add a caller to Workiz as a new lead, with their contact details, service address, and what they need, so your team can follow up and schedule the work. Workiz's API expects its secret inside the request body, where webhook tools would expose it to the AI, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

Zapier's Workiz app can create leads and jobs, but it can't look up clients or check your schedule.

## Before you start

Zapier connects to Workiz with your API token and API secret, which need the Developer API add-on:

1. In Workiz, select **Feature Center** in the navigation bar.
2. Under **Add-ons**, select **Developer API** and turn on the toggle.
3. Open the **Developer** page and copy your API token and API secret. Zapier asks for both when you connect Workiz.

If you can't see the **Feature Center** or the **Developer** page, ask your account admin to turn on the **Account Settings** permission for your user type in **Roles & Permissions**.

> **Warning**
>
> The API token and secret give access to your Workiz account. Store them safely and don't share
> them.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Workiz action

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the Workiz **Create Lead** action and connect your account. Zapier's fields aren't in the same order as on the Workiz **Developer** page, so paste the token and the secret into the matching fields.

| Field                  | Value                                                                                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Lead**                                                                                                                                             |
| **Set in Zapier**      | The job source, for example `Reception`. It must already exist as an ad source in Workiz.                                                                   |
| **Let the AI fill in** | First and last name, phone, email, the service address, and the lead notes: what the caller needs, when they're available, and anything else they told you. |
| **Assign to**          | **Client**                                                                                                                                                  |

### Assign the tool

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign **Create Lead** to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a repair. The lead appears in Workiz with your job source.

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) telling your receptionist
> to ask for the full address with the ZIP code and a 10-digit phone number before it creates the
> lead.

## Limitations

* Your receptionist can't find existing clients, so a returning caller can be added as a new lead. Filter by your job source in Workiz to review new leads.
* Zapier's Workiz app can't check your schedule. **Create Job** books a job at a set time and needs a job type, so leave it to your team unless you want callers' preferred times to go straight onto your calendar.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the action stops until it resets.

## Troubleshooting

| Problem                                        | What to check                                                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Create Lead** doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding the action in Zapier.                             |
| The action shows **Changed** and isn't used    | You edited it in Zapier. Select **Update** in the **Tools** tab.                                                  |
| Zapier says authentication failed              | The token and secret may be in the wrong fields, or no longer valid. Copy them again from the **Developer** page. |
| Field validation error from Workiz             | The job source must match an ad source in Workiz exactly. Phone numbers need 10 digits and ZIP codes 5.           |
