---
title: "Dialpad"
source: https://elevenlabs.io/docs/reception-ai/integrations/dialpad.md
path: docs/reception-ai/integrations/dialpad
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dialpad

Dialpad has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and your Dialpad main line (or a department) routes calls to it. Callers keep dialing your Dialpad number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

> **Warning**
>
> Don't add the receptionist as a personal forwarding number under **Your Devices**. Dialpad asks
> whoever answers a forwarded call to press 1, both to verify the number and on calls answered
> within a few seconds, and this prompt can't be fully turned off. Your receptionist can't press
> keys, so those calls fail. Route calls from the main line instead, as below.

## Allow routing to outside numbers

A Dialpad company admin must allow calls to be routed to numbers outside Dialpad. Go to **My Company** → **Company Settings** and turn on IVR forwarding to external numbers. To send a main line's fallback straight to an outside number, without a menu, contact Dialpad Support to enable external fallback for your account.

## Route main line calls to the receptionist

### Open call routing

Open your main line (or the department or contact center that owns the number). Under **Business hours and call routing**, select **Call Routing** → **Edit Call Routing**.

### Choose when the receptionist answers

Under **Fallback Options**, send calls that nobody answers to your receptionist's number. Set this for business hours so your team rings first, and for after hours so the receptionist answers every call outside your hours.

### Or add a menu option

If external fallback isn't enabled, choose the automated response menu as the fallback and add an option that forwards to your receptionist's number. Press **Enter** after typing the number.

> **Tip**
>
> To ring your team before the receptionist without a Dialpad menu, route every call to the
> receptionist and turn on **Who answers first** in Reception.ai. It rings a staff phone first and
> hands the call to the receptionist if nobody answers. The staff phone must be a different number
> from the one callers dial. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** Dialpad places a new outbound call to the receptionist and bridges it with the caller. Check which number the receptionist sees in your test call. If it's your Dialpad number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Costs:** Forwarded calls are outbound calls from Dialpad. Dialpad charges usage for calls forwarded to international numbers; check your plan for other per-minute charges.

## Test it

Call your Dialpad number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers but hears "press 1" and the call drops  | The call came through a personal forwarding number. Remove the receptionist from **Your Devices** and route from the main line instead.                                                                                           |
| You can't pick an outside number in call routing                 | Turn on IVR forwarding to external numbers in **Company Settings**, or ask Dialpad Support to enable external fallback.                                                                                                           |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check the main line's routing for the hours you're testing.                                                                                                               |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
