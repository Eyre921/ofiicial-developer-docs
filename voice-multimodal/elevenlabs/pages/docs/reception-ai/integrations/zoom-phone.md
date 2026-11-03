---
title: "Zoom Phone"
source: https://elevenlabs.io/docs/reception-ai/integrations/zoom-phone.md
path: docs/reception-ai/integrations/zoom-phone
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Zoom Phone

Zoom Phone has no direct connection to Reception.ai, so you connect it with call forwarding. Your receptionist answers on its own Reception.ai number, and Zoom Phone forwards calls to it. Callers keep dialing your Zoom Phone number.

First, go to **Receptionists**, select the **Phone** tile, and get a number. See [Phone numbers](/docs/reception-ai/phone-numbers/overview).

## Before you start

* Zoom Phone forwards to outside numbers only from a user, call queue, or auto receptionist that has a direct number (DID). A user with only an extension can't forward calls externally.
* Your admin may lock forwarding settings (shown with a lock icon). If you can't change a setting below, ask your Zoom admin.
* Calls forwarded to outside numbers can be billed by usage, depending on your Zoom Phone plan.

Then pick one of the setups below.

| Setup                                               | What happens                                                                               |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [Forward a user's calls](#forward-a-users-calls)    | The user's Zoom apps ring first. Unanswered and closed-hours calls go to the receptionist. |
| [Forward the main number](#forward-the-main-number) | An auto receptionist sends every call, or only closed-hours calls, to the receptionist.    |

## Forward a user's calls

### Open call handling

In the Zoom web portal, open **Zoom Phone** → **Settings**. Admins can go to **Admin Center** → **Product configuration** → **Phone system** → **Users & Rooms**, select the user, and open **User Settings**. Under **Business Hours**, select **Edit** next to **Call Handling**.

### Choose when the receptionist answers

Set **When a call is not answered** to **Forward to External Contacts** and add your receptionist's number with **Add Phone Number**. Choose the right country or region, since some countries share a country code. The user's Zoom apps ring first, and unanswered calls go to the receptionist.

### Turn off press 1

Clear **Require to press 1 before connecting the call** on the receptionist's number. It's on by default, and your receptionist can't press keys.

### Set closed hours

Repeat these steps under **Closed Hours** so the receptionist answers outside business hours. Break and holiday hours have their own call handling sections.

> **Note**
>
> Users can also set **Forward to External Contacts** in the Zoom Workplace app under **Settings** →
> **Phone** → **Voicemail and forwarding**. In the app, this option has to be enabled by Zoom
> Support first.

## Forward the main number

An auto receptionist can route closed-hours calls, or any routing step, to an outside number. Routing to a raw **Phone Number** requires a direct number on the auto receptionist. If your account has a directory of external contacts, you can add the receptionist as an external contact and route to it instead.

### Open the auto receptionist

In the Zoom web portal, go to **Admin Center** → **Product configuration** → **Phone system** → **Auto Receptionists**, select it, and open the **Profile** tab.

### Route closed hours to the receptionist

Under **Closed Hours**, edit the routing and send calls to your receptionist's number. Do the same under **Business Hours** to send every call to the receptionist.

## What to know

* **Caller ID:** Zoom doesn't document which number the receptionist sees on forwarded calls. Check it in your test call. If the receptionist sees your Zoom number instead of the caller's, every call looks like it comes from the same number, and your receptionist can't recognize returning callers by their number.
* **Call queues:** The press 1 requirement can't be turned off for call queue calls, so don't forward a call queue to the receptionist.

## Test it

Call your Zoom Phone number from another phone at a time when the routing you set applies. Check that your receptionist answers, then open **Inbox** and confirm which caller number the conversation shows. See [Testing](/docs/reception-ai/receptionist/testing).

## Troubleshooting

| Problem                                                            | What to check                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The receptionist answers, then the call drops or goes to voicemail | **Require to press 1 before connecting the call** is still on for the receptionist's number. Clear it. Call queue calls always require it.                                                                                        |
| **Forward to External Contacts** or **Phone Number** is missing    | The user or auto receptionist needs a direct number, and your admin may have locked the option. In the Workplace app, Zoom Support must enable it.                                                                                |
| Calls never reach the receptionist                                 | Call the receptionist's number directly. If that works, check the call handling for the hours you're testing (business, closed, break, or holiday).                                                                               |
| Callers are asked to press a key before the receptionist answers   | [Spam protection](/docs/reception-ai/receptionist/call-handling#verify-caller-identity) asks callers whose number isn't verified to press a key. Forwarded calls can arrive unverified. Turn it off if this affects real callers. |
