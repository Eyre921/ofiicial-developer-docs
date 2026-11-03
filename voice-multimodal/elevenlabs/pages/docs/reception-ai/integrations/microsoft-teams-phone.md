---
title: "Microsoft Teams Phone"
source: https://elevenlabs.io/docs/reception-ai/integrations/microsoft-teams-phone.md
path: docs/reception-ai/integrations/microsoft-teams-phone
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Microsoft Teams Phone

Teams Phone has no direct connection that Reception.ai can use: Direct Routing needs a certified session border controller, and Operator Connect uses trunks managed by your carrier. Instead, you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Teams forwards calls to it. Callers keep dialing your Teams number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

Then pick one of the setups below.

| Setup                                               | What happens                                                                                     |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [Forward a user's calls](#forward-a-users-calls)    | Calls to a user's number go to the receptionist right away, or after the user's Teams rings.     |
| [Route an auto attendant](#route-an-auto-attendant) | Your main number's auto attendant sends business-hours or after-hours calls to the receptionist. |

## Forward a user's calls

### Allow forwarding to outside numbers

In the Teams admin center, go to **Voice** → **Calling policies** and open the policy assigned to the user. Turn on **Call forwarding and simultaneous ringing to external phone numbers** and select **Save**. It's on by default.

### Open the user's call answering rules

Go to **Users** → **Manage users**, select the user, and open the **Voice** tab. If there's no **Voice** tab, the user doesn't have a Teams Phone license.

### Choose when the receptionist answers

Under **Call answering rules**, choose one:

* **Be immediately forwarded** to an external phone number, your receptionist's number. Calls don't ring the user.
* **Ring the user's devices**, then set **If unanswered** to an external phone number, your receptionist's number, and set **Ring for this many seconds before redirecting**.

Select **Save**. Users can also change these rules themselves in Teams settings.

## Route an auto attendant

### Open the auto attendant

In the Teams admin center, go to **Voice** → **Auto attendants** and edit the auto attendant on your main number.

### Route calls to the receptionist

In the **After-hours call flow**, under **Call routing options**, select **Redirect call** → **External phone number** and enter your receptionist's number. Do the same in the **Business-hours call flow** to send every call to the receptionist, or map a menu key to **External phone number**.

### License the resource account

The auto attendant's resource account needs a **Teams Phone Resource Account** license. With Microsoft Calling Plan numbers, it also needs a funded pay-as-you-go Calling Plan license or Communications Credits, or calls to outside numbers fail. With Direct Routing, it needs an online voice routing policy. With Operator Connect, check with your carrier.

> **Note**
>
> Since November 1, 2025, a Calling Plan license on a resource account no longer covers calls to
> outside numbers. If your auto attendant's external transfers stopped working, add pay-as-you-go or
> Communications Credits to its resource account.

## What to know

* **Caller ID:** When an auto attendant transfers a call to an outside number, Calling Plan and Operator Connect numbers show the original caller's number. With Direct Routing, it depends on your session border controller: with P-Asserted-Identity disabled (the default), the caller's number is shown; with it enabled, the resource account's number is shown. If the receptionist sees your Teams number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Costs:** Forwarded calls are outbound calls to the public phone network, billed against your Calling Plan, pay-as-you-go balance, Communications Credits, or carrier.

## Test it

Call your Teams number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                          | What to check                                                                                                                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You can't pick an external phone number in call answering rules  | Turn on **Call forwarding and simultaneous ringing to external phone numbers** in the user's calling policy, and check that the user has a Teams Phone license.                                                                   |
| Auto attendant transfers to the receptionist fail                | Give its resource account a funded pay-as-you-go license or Communications Credits (Calling Plan), or an online voice routing policy (Direct Routing).                                                                            |
| Every call shows your Teams number                               | With Direct Routing, disable P-Asserted-Identity on the session border controller so the caller's number is passed on.                                                                                                            |
| Callers are asked to press a key before the receptionist answers | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
