---
title: "Grasshopper"
source: https://elevenlabs.io/docs/reception-ai/integrations/grasshopper.md
path: docs/reception-ai/integrations/grasshopper
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Grasshopper

Grasshopper has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, which you add as a forwarding number on a Grasshopper extension. Callers keep dialing your Grasshopper number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

Then pick one of the setups below.

| Setup                                         | What happens                                                                  |
| --------------------------------------------- | ----------------------------------------------------------------------------- |
| [Forward all calls](#forward-all-calls)       | Every call to the extension goes straight to the receptionist.                |
| [Ring your team first](#ring-your-team-first) | Your own phone rings first. Unanswered calls go to the receptionist.          |
| [Forward after hours](#forward-after-hours)   | Your phone rings during business hours. The receptionist answers after hours. |

## Forward all calls

### Add the receptionist as a forwarding number

In Grasshopper, go to **Extensions** and select **Edit** next to the extension that answers your number. Select **Add a forwarding number** and enter your receptionist's number.

### Connect calls without screening

Set **How should Grasshopper handle calls to this number?** to **Calls will connect to you as soon as you pick up** (Direct Connect).

### Show the caller's number

Under **Options**, set **When a call is forwarded to me, show the caller ID of:** to **The caller**.

### Remove other forwarding numbers

Remove or turn off the extension's other forwarding numbers so only the receptionist rings.

> **Warning**
>
> With call screening or call announce on, Grasshopper asks whoever answers to press 1 to accept the
> call. Your receptionist can't press keys, so those calls fail. Always use Direct Connect for the
> receptionist's forwarding number.

## Ring your team first

Add your own phone and the receptionist as forwarding numbers on the same extension, with your phone listed first. Under **Options**, choose to call your forwarding numbers **in order**, and set **Ring for…** on your own phone to how long it should ring before Grasshopper moves on to the receptionist.

Grasshopper's True Solo plan allows one forwarding number per extension, so this setup needs another plan. Other plans allow up to 15 forwarding numbers per extension.

## Forward after hours

Each forwarding number has a schedule. On the receptionist's forwarding number, set **When do you want this number to receive calls** to the hours outside your business hours, and set your own phone's forwarding number to your business hours.

## What to know

* **Caller ID:** With **The caller** selected, your receptionist sees the caller's number and can recognize returning callers. If the receptionist sees your Grasshopper number instead, every call looks like it comes from the same number, and returning callers can't be recognized by their number.
* **Changes take a few minutes:** Forwarding changes can take up to five minutes to apply.

## Test it

Call your Grasshopper number from another phone. Check that your receptionist answers right away, then open **Inbox** and confirm the conversation shows your phone's number. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The call connects, then drops or goes to Grasshopper voicemail   | Call screening or call announce is on for the receptionist's forwarding number. Switch it to **Calls will connect to you as soon as you pick up**.                                                                                |
| Every call shows your Grasshopper number                         | Set **When a call is forwarded to me, show the caller ID of:** to **The caller** on the receptionist's forwarding number.                                                                                                         |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check the forwarding number's schedule and ring order, and wait a few minutes after changes.                                                                              |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
