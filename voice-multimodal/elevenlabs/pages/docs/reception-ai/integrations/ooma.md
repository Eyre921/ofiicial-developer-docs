---
title: "Ooma"
source: https://elevenlabs.io/docs/reception-ai/integrations/ooma.md
path: docs/reception-ai/integrations/ooma
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Ooma

Ooma Office has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Ooma forwards calls to it. Callers keep dialing your Ooma number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview). Ooma doesn't forward to international numbers, so use a receptionist number in your own country.

> **Warning**
>
> Leave **Require key press on answer** off wherever you enter the receptionist's number. It asks
> whoever answers to press 1 before the call connects, and your receptionist can't press keys. Some
> forwarding guides tell you to turn it on, which makes every forwarded call fail.

Then pick one of the setups below.

| Setup                                                        | What happens                                                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| [Forward an extension's calls](#forward-an-extensions-calls) | Every call to the extension goes to the receptionist, or only when its devices are offline. |
| [Use a shared external line](#use-a-shared-external-line)    | Your virtual receptionist, a ring group, or a call queue sends calls to the receptionist.   |

## Forward an extension's calls

### Open call handling

Sign in to the Ooma Office End User Portal at office.ooma.com and open **Call Handling** on the **Settings** page. In the Ooma Office desktop app, select your name, then **Settings** → **Devices**.

### Forward every call

Set **When a call comes in** to **Forward it immediately**, and set **Forward to** to **My Forwarding number**.

### Enter the receptionist's number

In the popup, enter your receptionist's number. Under **Show**, choose the original caller's number so the receptionist can recognize callers. Leave **Require key press on answer** off. Select **Save** in the popup, then save your settings.

To forward only when the extension's devices are offline, for example during an internet outage, turn on **When all devices are offline, send calls to Forwarding number** instead, and enter the receptionist's number the same way.

> **Note**
>
> From an Ooma Office desk phone, you can also dial `*72`, wait for the prompt, then dial your
> receptionist's number followed by `#`. Dial `*74` to turn forwarding on or off. Star codes don't
> show the **Require key press on answer** option, so check it in the End User Portal afterward.

## Use a shared external line

A shared external line lets your virtual receptionist, a ring group, or a call queue send calls to an outside number. It requires Ooma Office Pro Plus, and each account can have one.

### Add the line

As an administrator, sign in to office.ooma.com and open the **Settings** page. From the **ADD** menu, select **Shared External Line**.

### Enter the receptionist's number

Enter a name and your receptionist's number. Leave **Required key press on answer** off, then select **Save**.

### Route calls to it

The line now appears as a destination in your other extensions' call handling. Choose it in your virtual receptionist's menu or after-hours handling, in a ring group or call queue, or as where a user's calls go when nobody answers.

> **Tip**
>
> To ring your team before the receptionist without Pro Plus, forward every call to the receptionist
> and turn on **Who answers first** in Reception.ai. It rings a staff phone first and hands the call
> to the receptionist if nobody answers. The staff phone must be a different number from the one
> callers dial. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** Extension forwarding lets you show the original caller's number or your Ooma number. Ooma doesn't document caller ID for shared external lines, so check it in your test call. If the receptionist sees your Ooma number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Forwarding takes over:** With **Forward it immediately**, only the receptionist's number rings. Your extension's devices don't ring.

## Test it

Call your Ooma number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                            | What to check                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers, then the call drops or goes to voicemail | **Require key press on answer** is on for the forwarding number or the shared external line. Turn it off.                                                                                                                         |
| **Shared External Line** is missing from the **ADD** menu          | Shared external lines need Ooma Office Pro Plus, and you can add only one per account.                                                                                                                                            |
| Calls never reach the receptionist                                 | Call the receptionist's number directly. If that works, check that your call handling is saved and that forwarding wasn't turned off with `*74`.                                                                                  |
| Callers are asked to press a key before the receptionist answers   | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
