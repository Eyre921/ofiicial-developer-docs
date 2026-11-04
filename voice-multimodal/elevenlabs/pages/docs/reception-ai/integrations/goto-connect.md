---
title: "GoTo Connect"
source: https://elevenlabs.io/docs/reception-ai/integrations/goto-connect.md
path: docs/reception-ai/integrations/goto-connect
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# GoTo Connect

GoTo Connect has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and GoTo Connect forwards calls to it. Callers keep dialing your GoTo Connect number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

Then pick one of the setups below.

| Setup                                            | What happens                                                                      |
| ------------------------------------------------ | --------------------------------------------------------------------------------- |
| [Forward a line's calls](#forward-a-lines-calls) | A line rings first. Unanswered calls go to the receptionist, or every call does.  |
| [Route the main number](#route-the-main-number)  | The main number's dial plan sends every call, or calls outside your hours, to it. |

## Forward a line's calls

Use **Find Me/Follow Me** on the line that callers reach.

### Open Find Me/Follow Me

In the GoTo app on desktop or web, select your profile picture, then **Settings** → **Find me follow me**. On mobile, open the menu, then **Phone** → **Find Me, Follow Me**.

### Choose when the receptionist answers

To ring your line first, keep it as the first ring step and set **No answer, send to** to **External** with your receptionist's number. To send every call to the receptionist, make its number the only ring step.

### Turn off Confirm pick-up

Make sure call screening is not set to **Confirm pick-up** for the receptionist's number. It asks whoever answers to accept the call, and your receptionist can't press keys.

### Pass the caller's number

Turn on **Pass-through Caller ID** so the receptionist sees the caller's number instead of your line's external caller ID. Then select **Save**.

Find Me/Follow Me applies when the line is dialed directly, when a call is transferred to it, and when a **Line & Voicemail** dial plan node sends calls to it. A **Simple Dial** node, or another user's Find Me/Follow Me ring step, ignores it.

## Route the main number

An admin can send the main number's calls to the receptionist in the dial plan editor.

### Open the dial plan

In the GoTo Admin portal, select **Dial Plans** and open the dial plan your main number uses, or select **Add Dial Plan** to create one.

### Add an External Number node

Add an **External Number** node and enter your receptionist's number. To send only calls outside your hours, add a **Schedule** node first and connect its closed branch to the **External Number** node. Keep your team on the open branch.

### Save and assign the number

Select **Save**. If you created a new dial plan, go to **Phone Numbers**, select the pencil icon next to your number, and choose the dial plan under **Route to**.

> **Tip**
>
> To ring your team before the receptionist without a schedule, route every call to the receptionist
> and turn on **Who answers first** in Reception.ai. It rings a staff phone first and hands the call
> to the receptionist if nobody answers. The staff phone must be a different number from the one
> callers dial. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** On Find Me/Follow Me, **Pass-through Caller ID** controls whether the receptionist sees the caller's number or your line's external caller ID. If an admin turned on caller ID blocking for the line, callers stay blocked when forwarded. GoTo doesn't document caller ID for the **External Number** node, so check it in your test call. If the receptionist sees your GoTo number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Costs:** Check your GoTo Connect plan for how calls forwarded to outside numbers are billed.

## Test it

Call your GoTo Connect number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers, then the call moves on or drops        | **Confirm pick-up** is on for the receptionist's ring step. Turn it off.                                                                                                                                                          |
| Find Me/Follow Me changes have no effect                         | The main number's dial plan reaches the line through a **Simple Dial** node, which ignores Find Me/Follow Me. Use a **Line & Voicemail** node, or route with an **External Number** node.                                         |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check the dial plan branch or ring step for the hours you're testing, and that you saved your changes.                                                                    |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
