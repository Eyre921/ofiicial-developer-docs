---
title: "Housecall Pro"
source: https://elevenlabs.io/docs/reception-ai/integrations/housecall-pro.md
path: docs/reception-ai/integrations/housecall-pro
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Housecall Pro

Your receptionist can add a new caller to Housecall Pro as a customer, with their contact details and service address, so your team can schedule the job. Housecall Pro's public API is limited to its MAX plan, while its Zapier integration is available on more plans, so Reception connects through [Zapier](/docs/reception-ai/integrations/zapier).

Zapier's Housecall Pro app has one action, **Create Customer**. Your receptionist can't look up customers, see your schedule, or book jobs in Housecall Pro. Scheduling stays with your team.

## Before you start

Housecall Pro's Zapier integration is available on the Essentials, Essentials+, and MAX plans. Turn it on and get its API key:

1. In Housecall Pro, select the grid icon in the top-right corner to open **My Apps**, then select **Go to App store**.
2. Search for **Zapier**, select **View Details**, and turn on the toggle.
3. Refresh the page. The API key appears on the Zapier app page. Zapier asks for it when you connect Housecall Pro.

> **Warning**
>
> The API key gives access to your Housecall Pro account. Don't share it.

## Set up

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Housecall Pro action

In your Zapier MCP server at [mcp.zapier.com](https://mcp.zapier.com), add the Housecall Pro **Create Customer** action and connect your account with the API key.

| Field                  | Value                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Zapier action**      | **Create Customer**                                                                                             |
| **Set in Zapier**      | **Tag1**, for example `Reception`, so your team can spot new callers. **Notifications enabled**, as you prefer. |
| **Let the AI fill in** | **First name**, **Last name**, **Email**, **Mobile number**, and the service address.                           |
| **Assign to**          | **Client**                                                                                                      |

### Assign the tool

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign **Create Customer** to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) as a new caller who needs a job done. The customer appears in Housecall Pro with your tag.

> **Tip**
>
> Add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures) so your receptionist only
> creates a customer for first-time callers, and takes a message with the job details so your team
> can schedule it.

## Limitations

* Your receptionist can only create customers. It can't find existing customers, create jobs or estimates, or check availability.
* Because there's no lookup, a returning caller can be added twice. Filter by your tag in Housecall Pro to review new customers.
* Each action your receptionist runs uses tasks from your Zapier plan. Zapier currently counts two tasks per successful call; failed calls aren't counted. When the plan runs out, the action stops until it resets.

## Troubleshooting

| Problem                                            | What to check                                                                          |
| -------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Create Customer** doesn't appear in Reception.ai | Select **Refresh tools** on the Zapier integration after adding the action in Zapier.  |
| The action shows **Changed** and isn't used        | You edited it in Zapier. Select **Update** in the **Tools** tab.                       |
| Zapier rejects the API key                         | Check that the Zapier app is still turned on in Housecall Pro, and copy the key again. |
| The Zapier app isn't in the App Store              | Your Housecall Pro plan may not include it. Check your plan.                           |
