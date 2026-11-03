---
title: "Google Voice"
source: https://elevenlabs.io/docs/reception-ai/integrations/google-voice.md
path: docs/reception-ai/integrations/google-voice
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Google Voice

Google Voice has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Google Voice forwards calls to it. Callers keep dialing your Google Voice number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

Then pick one of the setups below.

| Setup                                                            | What happens                                                                                          |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [Forward from a ring group](#forward-from-a-ring-group)          | Google Workspace only. The group rings first; unanswered or after-hours calls go to the receptionist. |
| [Link the receptionist's number](#link-the-receptionists-number) | Calls to your own Google Voice number ring the receptionist along with your devices.                  |

## Forward from a ring group

Ring groups need a Google Voice Standard or Premier subscription, and setting one up needs the Google Voice Admin role.

### Open the ring group

In the Google Admin console, go to **Menu** → **Apps** → **Google Workspace** → **Google Voice** → **Ring groups**, and open or create the ring group for your business number.

### Forward unanswered calls

Under **Configure call handling**, set **Unanswered calls** to **Forward the caller**. Set **Forward type** to **Phone number** and enter your receptionist's number. For a number outside the US, choose the country or region first. Unanswered calls are forwarded after 30 seconds.

### Forward after-hours calls

Select **Edit Working Hours**, set **Opening hours** to **Customized hours**, and add holiday closures if needed. Set **After hours action** to **Forward the caller**, with **Forward type** **Phone number** and your receptionist's number.

An auto attendant can also send callers to another phone number, during open hours from a menu option or after hours.

## Link the receptionist's number

Use this for a Google Voice number assigned to you. Linked numbers ring together with your Google Voice apps, so the receptionist usually answers first.

### Turn off call screening

On [voice.google.com](https://voice.google.com), open **Settings** → **Calls** and turn off **Screen Calls**. With screening on, whoever answers has to press 1 to accept the call, and your receptionist can't press keys.

### Show the caller's number

In the same section, turn off **Show my Google Voice number as caller ID when forwarding calls**, so the receptionist sees the caller's number.

### Add the linked number

Under **Account** → **Linked numbers**, select **New linked number** and enter your receptionist's number. Choose **Verify by phone**, then **Call**. Your receptionist answers Google's verification call: open the conversation in Reception.ai's **Inbox**, find the code in the transcript, and enter it in Google Voice.

### Check forwarding is on

Under **Settings** → **Calls** → **Incoming calls**, make sure the receptionist's number is turned on under **Call forwarding**.

> **Note**
>
> Linked numbers aren't available to SIP Link users, and your Google Workspace admin may restrict
> them. To ring your own devices before the receptionist, turn on **Who answers first** in
> Reception.ai instead, with a staff phone that isn't your Google Voice number. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** For linked numbers, the **Show my Google Voice number as caller ID when forwarding calls** setting controls it: off shows the caller's number. Google doesn't document which number ring-group forwards show, so check it in your test call. If the receptionist sees your Google Voice number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.

## Test it

Call your Google Voice number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers, then the call goes to voicemail        | **Screen Calls** is on. Turn it off under **Settings** → **Calls**.                                                                                                                                                               |
| Every call shows your Google Voice number                        | Turn off **Show my Google Voice number as caller ID when forwarding calls**.                                                                                                                                                      |
| No verification code in the transcript                           | Retry **Verify by phone** and check the newest conversation in **Inbox**. If the code still isn't there, use a ring group instead.                                                                                                |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check the ring group's **Unanswered calls** and working hours, or that the linked number is on under **Call forwarding**.                                                 |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
