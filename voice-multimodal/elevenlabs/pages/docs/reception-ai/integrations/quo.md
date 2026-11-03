---
title: "Quo (formerly OpenPhone)"
source: https://elevenlabs.io/docs/reception-ai/integrations/quo.md
path: docs/reception-ai/integrations/quo
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Quo (formerly OpenPhone)

Quo has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and the call flow on your Quo number forwards calls to it. Callers keep dialing your Quo number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview). Quo forwards only to US and Canadian numbers, so use a US or Canadian receptionist number.

Then pick one of the setups below. Each uses a **Forward call** step in your Quo number's call flow.

| Setup                                         | What happens                                                                   |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| [Forward all calls](#forward-all-calls)       | Every call goes straight to the receptionist.                                  |
| [Ring your team first](#ring-your-team-first) | Your team's Quo apps ring first. Unanswered calls go to the receptionist.      |
| [Forward after hours](#forward-after-hours)   | Your team answers during business hours. The receptionist answers after hours. |

## Forward all calls

### Choose Forward all calls

Open the call flow for your Quo number. Select the **Default call flow** dropdown at the top and choose **Forward all calls**.

### Enter the receptionist's number

Enter your receptionist's number and select **Create new call flow**.

### Turn it on

Check the destination, select **Enable this call flow**, and confirm that the **Live** indicator appears.

This call flow can't have other steps. To stop forwarding, select **Default call flow** and then **Enable this call flow**.

## Ring your team first

### Add a Ring users step

In your number's call flow, add a **Ring users** step with the people who should answer first.

### Add a Forward call step after it

Drag a **Forward call** step after **Ring users** and enter your receptionist's number.

## Forward after hours

### Add a Business hours step

Drag a **Business hours** step right after **Incoming call** and set your schedule.

### Route each branch

Add a **Ring users** step for calls during business hours. Add a **Forward call** step for calls after hours, and enter your receptionist's number.

You can also forward a single option of a phone menu to the receptionist.

## What to know

* **Caller ID:** Quo keeps the original caller's number on forwarded calls, so your receptionist can recognize returning callers.
* **Usage:** Quo counts each forwarded call as two call legs, so it counts double toward your usage.
* **No fallback to Quo voicemail:** Once Quo forwards a call, it doesn't return to Quo. Your receptionist handles the call from there.
* **Recording:** Quo can't record or transcribe calls it forwards to an outside number. The receptionist's transcript is in **Inbox**.

## Test it

Call your Quo number from another phone. Check that your receptionist answers, then open **Inbox** and confirm the conversation shows your phone's number. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calls still ring your team or go to Quo voicemail                | Check that the call flow you edited shows **Live**, and that the **Forward call** step is on the branch you're testing (business hours or after hours).                                                                           |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check the number in the **Forward call** step. Quo forwards only to US and Canadian numbers.                                                                              |
| The receptionist doesn't recognize a returning caller            | Check the caller's number in **Inbox**. Callers who hide their number can't be matched.                                                                                                                                           |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
