---
title: "Vonage Business Communications"
source: https://elevenlabs.io/docs/reception-ai/integrations/vonage.md
path: docs/reception-ai/integrations/vonage
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Vonage Business Communications

Vonage Business Communications has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Vonage forwards calls to it. Callers keep dialing your Vonage number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

Then pick one of the setups below.

| Setup                                                                           | What happens                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Forward an extension](#forward-an-extension)                                   | Every call to the extension goes to the receptionist.                           |
| [Forward from the Virtual Receptionist](#forward-from-the-virtual-receptionist) | After-hours calls, or callers who choose a menu option, go to the receptionist. |

## Forward an extension

### Open the extension's call forwarding

In the Vonage Admin Portal, select **Phone System** → **Extensions**. Hover over the extension, select the **Pencil** icon, and select **Call Forwarding**.

### Forward to the receptionist

Turn on **Forward Calls** and select **Send To Ext. or Number**. Under **Forward All My Calls To**, select **Add New Number** and enter your receptionist's number.

### Pass the caller's number

Under **Use Caller ID**, select **Originating Caller ID**, then select **Save**.

Users can set the same forwarding at app.vonage.com under their avatar → **Settings** → **Call Forwarding** → **Forward All Calls**.

## Forward from the Virtual Receptionist

### Open the schedule

In the Admin Portal, open the **Virtual Receptionist** page, hover over your Virtual Receptionist, and select the **Pencil** icon. Open **Schedules and Call Flows**.

### Forward after-hours calls

Next to **After Hours Schedule**, select the three dots → **Edit**. On the **Call Flow** tab, choose **Forward Calls to External Number**, select the country code, and enter your receptionist's number. Keep **Originating Caller ID** selected.

### Or forward a menu option

To send callers who press a key to the receptionist, edit your business-hours schedule. On the **Call Flow** tab, select **Play a List of Options**, choose **Forward to number** for the key, and enter your receptionist's number with **Originating Caller ID**.

### Save

Select **Save**, then **Done**, then **Save**.

After-hours routing applies only if your main schedule isn't set to **All Day**. Use **Specify Hours and Dates** for your business hours.

> **Tip**
>
> To ring your team before the receptionist, forward all calls to the receptionist and turn on **Who
> answers first** in Reception.ai. It rings a staff phone first and hands the call to the
> receptionist if nobody answers. The staff phone must be a different number from the one callers
> dial. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** With **Originating Caller ID**, your receptionist sees the caller's number and can recognize returning callers. With **Number on Account**, every call looks like it comes from your Vonage number, and returning callers can't be recognized by their number.
* **Costs:** Vonage charges extra for calls forwarded to numbers outside your plan's coverage area. Its Virtual Receptionist guide lists a per-minute charge for calls forwarded to an outside line, with higher international rates.

## Test it

Call your Vonage number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm the conversation shows your phone's number. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Every call shows your Vonage number                              | Set **Use Caller ID** to **Originating Caller ID** on the forwarding rule or Virtual Receptionist option.                                                                                                                         |
| After-hours calls don't reach the receptionist                   | Make sure your main schedule isn't set to **All Day**, and that the **After Hours Schedule** forwards to the receptionist's number.                                                                                               |
| Calls never reach the receptionist                               | Call the receptionist's number directly. If that works, check that **Forward Calls** is on and the number is saved under **Forward All My Calls To**.                                                                             |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
