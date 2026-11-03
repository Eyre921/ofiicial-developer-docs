---
title: "Aircall"
source: https://elevenlabs.io/docs/reception-ai/integrations/aircall.md
path: docs/reception-ai/integrations/aircall
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Aircall

Aircall has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and your Aircall number's Smartflow redirects calls to it. Callers keep dialing your Aircall number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

> **Warning**
>
> Don't use a user's **Forward call to an external number** setting for the receptionist. Aircall
> asks whoever answers a forwarded call to press 1 within 10 seconds, and only Aircall Support can
> turn this off. Your receptionist can't press keys, so those calls fail. Use a Smartflow **Redirect
> to** widget instead, as below.

Then pick one of the setups below. Each uses a **Redirect to** widget in your Aircall number's Smartflow.

| Setup                                         | What happens                                                                  |
| --------------------------------------------- | ----------------------------------------------------------------------------- |
| [Forward all calls](#forward-all-calls)       | Every call goes straight to the receptionist.                                 |
| [Ring your team first](#ring-your-team-first) | Your team rings first. Unanswered calls go to the receptionist.               |
| [Forward after hours](#forward-after-hours)   | Your team answers during opening hours. The receptionist answers after hours. |

## Forward all calls

### Add a Redirect to widget

Open your Aircall number's Smartflow in the Flow editor. Select the **+** icon at the start of the flow and choose **Redirect to**.

### Enter the receptionist's number

In the configuration panel, select **External number** and enter your receptionist's number.

### Publish

Select **Publish**.

## Ring your team first

Add a **Ring to** widget for the users or team who answer first. After it, add a **Redirect to** widget set to **External number** with your receptionist's number, then select **Publish**. Without a widget after **Ring to**, unanswered calls ring once and drop.

## Forward after hours

Add a **Time Rule** widget and set your opening hours as a branch, with the right time zone. On the opening-hours branch, add **Ring to** for your team. On the **At any other time** branch, add **Redirect to** → **External number** with your receptionist's number. Select **Publish**. Use a **Date Rule** widget for holidays.

## What to know

* **The flow ends at Redirect to:** Once Aircall redirects a call to an outside number, no later widget runs. Your receptionist handles the call from there.
* **Reporting and costs:** Aircall places an outbound call to the receptionist, so redirected calls show up as outbound calls in Aircall analytics. Check your Aircall plan for how outbound minutes are billed.
* **Caller ID:** Aircall shows anonymous callers as `+266696687`. Aircall doesn't document which number identified callers show on redirected calls, so check it in your test call. If the receptionist sees your Aircall number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.

## Test it

Call your Aircall number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers, then the call drops                    | The call came through a user's **Forward call to an external number** setting, which needs a press 1. Turn it off and use **Redirect to** in the Smartflow.                                                                       |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check that the Smartflow is published and that the **Redirect to** widget is on the branch you're testing.                                                                |
| After-hours calls still ring your team                           | Check the **Time Rule** time zone and opening hours.                                                                                                                                                                              |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
