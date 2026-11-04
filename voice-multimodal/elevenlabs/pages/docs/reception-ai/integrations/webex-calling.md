---
title: "Webex Calling"
source: https://elevenlabs.io/docs/reception-ai/integrations/webex-calling.md
path: docs/reception-ai/integrations/webex-calling
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Webex Calling

Webex Calling has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Webex Calling forwards calls to it. Callers keep dialing your Webex number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

## Before you start

* Webex Calling only forwards a call type that's allowed to be transferred or forwarded. In Control Hub, go to **Management** → **Locations**, select the location, then **Calling** → **Call Handling** → **Outgoing Call Permissions**. Check that **Allow transfer/forwards** is on for the call type of your receptionist's number. It's on for national calls and off for international calls by default. Users and workspaces can override the location's settings.
* Don't add the receptionist under **Sequential Ring** with **Answer confirmation** on. It asks whoever answers to confirm the call, and your receptionist can't press keys.

Then pick one of the setups below.

| Setup                                                   | What happens                                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [Forward a user's calls](#forward-a-users-calls)        | Calls to a user go to the receptionist always, or when unanswered or busy.     |
| [Forward an auto attendant](#forward-an-auto-attendant) | Calls to your main number go to the receptionist always, or during a schedule. |

## Forward a user's calls

### Open call forwarding

In Control Hub, go to **Management** → **Users**, select the user, and open the **Calling** tab. Under **Call handling**, select **Call forwarding**. For a workspace, start from **Management** → **Workspaces** instead.

### Choose when the receptionist answers

Turn on one or more options and enter your receptionist's number:

| Option                                           | When it forwards                                                             |
| ------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Forward all calls**                            | Every call. The user's devices don't ring.                                   |
| **Forward calls when unanswered**                | After the **Number of rings before forwarding** you set.                     |
| **Forward calls when lines are engaged**         | When the user is on a call. You can't turn this on while call waiting is on. |
| **Forward calls if the network is disconnected** | When the user's devices are offline, for example during an internet outage.  |

### Save

Select **Save**.

Users can set the same options themselves in their Webex settings, and changes show up in both places.

## Forward an auto attendant

### Open the auto attendant

In Control Hub, go to **Services** → **Calling** → **Features**. On the **Auto Attendant** card, select **Manage**, then select the auto attendant on your main number.

### Turn on call forwarding

In the **Overview** section, open **Call Forwarding** and turn on the toggle.

### Choose when the receptionist answers

To send every call, select **Always Forward Calls**, enter your receptionist's number, and select **Save**. To send calls only at certain times, select **Selectively Forward Calls** and **Add When to Forward**. Name the rule, pick the business hours schedule and holiday schedule during which the receptionist should answer, and set **Forward To** to your receptionist's number. Leave **Calls From** as **Any Number** and select **Save**.

**When Not to Forward** rules win over **When to Forward** rules, and rules are checked in table order.

> **Tip**
>
> To ring your team before the receptionist without a schedule, forward every call to the
> receptionist and turn on **Who answers first** in Reception.ai. It rings a staff phone first and
> hands the call to the receptionist if nobody answers. The staff phone must be a different number
> from the one callers dial. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** Webex doesn't document which number the receptionist sees on forwarded calls. Check it in your test call. If the receptionist sees your Webex number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Outbound dial digit:** If your dial plan requires an outbound dial digit, include it in the forwarding number, or forwarding to outside numbers stops working.
* **Costs:** Calls forwarded to outside numbers use your PSTN service. Check your Webex Calling plan or PSTN provider for per-minute charges.

## Test it

Call your Webex number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Forwarded calls fail or are rejected                             | Turn on **Allow transfer/forwards** for the receptionist's call type in **Outgoing Call Permissions**, for the location and any user override. Check the outbound dial digit, if your dial plan uses one.                         |
| The receptionist answers, then the call drops                    | The call came through **Sequential Ring** with **Answer confirmation** on. Turn it off, or use call forwarding instead.                                                                                                           |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check which forwarding option or selective rule applies at the time you're testing.                                                                                       |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
