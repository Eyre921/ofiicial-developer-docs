---
title: "Phone.com"
source: https://elevenlabs.io/docs/reception-ai/integrations/phone-com.md
path: docs/reception-ai/integrations/phone-com
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Phone.com

Phone.com has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Phone.com forwards calls to it. Callers keep dialing your Phone.com number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

> **Warning**
>
> Leave **Call Screening** off on the forward to your receptionist. With screening on, whoever
> answers must press 1 to connect the call, and your receptionist can't press keys.

Phone.com has two admin consoles. Follow the one your account uses.

| Setup                                                         | What happens                                                                                           |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [Forward in My.Phone.com](#forward-in-myphonecom)             | Every call to the number, or every call outside your business hours, goes to the receptionist.         |
| [Forward in the Control Panel](#forward-in-the-control-panel) | Call handling rules forward calls during a schedule, or after an extension rings, to the receptionist. |

## Forward in My.Phone.com

You need to be a Phone.com administrator.

### Open the number

Sign in to My.Phone.com. Select **Administration** → **Numbers**, then select **edit** next to your number.

### Forward to the receptionist

Under **Call handling**, choose **Forward to a Number** and enter your receptionist's number.

### Check the forwarding options

Select the pen icon next to the number. Set **Caller ID to Display** to the caller's number, leave **Voice Tag** empty, and leave **Call Screening** off. Then select **Save**.

To send only calls outside your hours, set your hours under **Administration** → **Business Hours**. Then edit your main number, choose **Main company number**, and set **After hours** to forward to your receptionist's number. Holidays and lunch breaks follow **After hours** unless you turn off **Same as after hours**.

## Forward in the Control Panel

### Open the number's rules

Sign in to Control.Phone.com. Hover over **Configure**, select **Manage Numbers**, and select **Edit** next to your number. Next to **Number Action**, select **Edit**.

### Add a forward

Set **Select Operation** to **Forward Call** and enter your receptionist's number. To forward only at certain times, change **All Calls** to **Received During** and pick a schedule (create one with **Configure** → **Add a Schedule**), then add a second rule for all other calls.

### Ring your team first (optional)

Make the first action a **Forward Call** to your extension with a ring duration. Select **Add Next Action** and add a **Forward Call** to your receptionist's number.

### Check the forwarding options

Select **Adv** next to the forward to your receptionist. Set **Caller ID to Show Me** to **Caller's ID**, leave **Voice Tag** empty, and leave **Call Screening** off. Select **Save Rule Settings**.

Rules set on an extension (**Configure** → **Manage Users & Extensions** → **Call Handling Rules**) work the same way and apply to calls that reach that extension.

> **Tip**
>
> You can also forward every call to the receptionist and turn on **Who answers first** in
> Reception.ai. It rings a staff phone first and hands the call to the receptionist if nobody
> answers. The staff phone must be a different number from the one callers dial. See [Who answers first](/docs/reception-ai/receptionist/call-handling#who-answers-first).

## What to know

* **Caller ID:** Phone.com lets you show the caller's number or your Phone.com number on forwarded calls. Choose the caller's number, or every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Voice tag:** A voice tag is read aloud to whoever answers before the call connects. Your receptionist would hear it as the start of the call, so leave it empty.
* **Costs:** Check your Phone.com plan for how forwarded minutes are billed.

## Test it

Call your Phone.com number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm the conversation shows your phone's number. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                            | What to check                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers, then the call drops or goes to voicemail | **Call Screening** is on for the forward to your receptionist. Turn it off.                                                                                                                                                       |
| The receptionist's greeting talks over a message                   | A **Voice Tag** is set on the forward. Clear it.                                                                                                                                                                                  |
| Calls never reach the receptionist                                 | Call the receptionist's number directly. If that works, check the rule or business-hours section that applies at the time you're testing. Holiday schedules must be in place at least 24 hours ahead.                             |
| Callers are asked to press a key before the receptionist answers   | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
