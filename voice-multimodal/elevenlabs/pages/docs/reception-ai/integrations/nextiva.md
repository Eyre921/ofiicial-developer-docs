---
title: "Nextiva"
source: https://elevenlabs.io/docs/reception-ai/integrations/nextiva.md
path: docs/reception-ai/integrations/nextiva
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Nextiva

Nextiva has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Nextiva forwards calls to it. Callers keep dialing your Nextiva number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

Then pick one of the setups below. Menu names differ between Nextiva's platforms, so follow the one your account uses.

| Setup                                            | What happens                                                                                 |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| [Forward a user's calls](#forward-a-users-calls) | Calls to a user go to the receptionist always, or when unanswered, busy, or unreachable.     |
| [Route a call flow](#route-a-call-flow)          | Your main number's call flow sends after-hours calls, or a menu option, to the receptionist. |

## Forward a user's calls

### Open the user's forwarding settings

In the Nextiva voice portal, select **Users**, hover over the user, and choose **Actions** → **Voice Settings** → **Forwarding**. In Nextiva NEXT, open the user with **Edit user** and go to **Calling** → **Forwarding**.

### Choose when the receptionist answers

Turn on one or more rules and enter your receptionist's number:

| Rule                                   | When it forwards                                                            |
| -------------------------------------- | --------------------------------------------------------------------------- |
| Always (**Forward all calls** in NEXT) | Every direct call. It overrides the other rules.                            |
| **Call forwarding (unanswered)**       | After the number of rings you pick.                                         |
| Busy                                   | When the user is on a call with call waiting off, or has Do Not Disturb on. |
| Not reachable                          | When the user's devices are offline, for example during an internet outage. |

### Save

Select **Save**.

User forwarding rules apply only to calls made directly to the user. Calls the user gets from a call center or call group aren't forwarded.

## Route a call flow

### Open the call flow

Select **Voice**, open the **Call Flows** tab, and open the call flow on your main number (or select **Create New Call Flow** → **Start From Scratch**).

### Add business hours

Add a **Schedules** node with your hours and holidays. Calls outside your hours follow the closed branch.

### Send calls to the receptionist

On the closed branch, add a **Transfer Out** node and enter your receptionist's 10-digit number. To send callers who choose a menu option instead, add **Transfer Out** to that option of a **Phone Menu** node.

### Go live

Every branch must end in a terminating node, such as **Transfer Out** or voicemail. Select **Go Live** and confirm.

## What to know

* **Caller ID:** By default, Nextiva shows the original caller's number on blind transfers to outside numbers, and Nextiva Support can change this on request. Nextiva doesn't document caller ID for forwarded calls, so check it in your test call. If the receptionist sees your Nextiva number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **US and Canada:** **Transfer Out** takes a 10-digit number, so use a US or Canadian receptionist number.

## Test it

Call your Nextiva number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm the conversation shows your phone's number. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The unanswered or busy rule doesn't forward                      | Turn off the always rule, which overrides the others, and check that no selective forwarding rules are active.                                                                                                                    |
| Calls from a call group or call center aren't forwarded          | User forwarding rules don't apply to those calls. Route them with a call flow instead.                                                                                                                                            |
| The call flow won't go live                                      | Every branch needs a terminating node. **Transfer Out** can't point at the call flow's own number or extension.                                                                                                                   |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
