---
title: "Call handling"
source: https://elevenlabs.io/docs/reception-ai/receptionist/call-handling.md
path: docs/reception-ai/receptionist/call-handling
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Call handling

The **On the call** group on the Receptionists page controls what happens during a phone call: who picks up first, when calls are transferred to your team, how callers are verified, and which numbers are blocked.

## Answering order

**Answering order** decides who answers inbound calls first. It applies to every receptionist in your workspace.

| Option                           | Behavior                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| **Receptionist first** (default) | The AI receptionist answers immediately. Best for full 24/7 coverage.                 |
| **Staff first**                  | Your staff phone rings first. If nobody answers in time, the receptionist takes over. |

When **Staff first** is selected, configure:

| Setting                          | Description                                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Staff phone number**           | The number to ring first                                                                                    |
| **Maximum ring time**            | How long to ring before the receptionist answers: 10, 15 (default), 20, or 30 seconds                       |
| **Ring music**                   | What the caller hears while waiting: soft rock (default), ambient, classical, electronica, rock, or guitars |
| **Staff connection message**     | Spoken to the caller while staff is ringing (up to 200 characters)                                          |
| **Receptionist connect message** | Spoken when staff does not answer and the receptionist takes over (up to 200 characters)                    |
| **Staff answering hours**        | When staff first is active, with a timezone. Outside these hours, the receptionist answers directly.        |

> **Note**
>
> Staff first places an outbound call to your staff phone. It is available for US businesses, and
> for any business whose receptionist uses only numbers from your own Twilio account or SIP trunk.
> See [Bring your own number](/docs/reception-ai/phone-numbers/bring-your-own-number).

## Forward an existing number

To keep your current business line, forward calls you don't answer to your receptionist's number. Forwarding is set up with your phone carrier and works independently of the answering order.

Open **Forward an existing number**, choose the country of the phone you will forward from, and dial the codes shown. For most mobile carriers:

| When                             | Code             |
| -------------------------------- | ---------------- |
| You don't answer                 | `**61*<number>#` |
| Your line is busy                | `**67*<number>#` |
| Your phone is off or unreachable | `**62*<number>#` |
| Turn off all forwarding          | `##002#`         |

Some carriers, such as Verizon in the US, use star codes instead (`*71` for busy or unanswered calls, `*72` for all calls). The dialog shows the right codes for your country.

> **Note**
>
> Your carrier controls how many rings pass before forwarding, and may charge for forwarded calls.
> Landlines and internet phone systems are configured through your provider's settings instead.

## Transfer to a human

Transfer rules let your receptionist connect callers to specific people or departments based on what the caller says. You can create up to **100 transfer rules** per receptionist.

Each rule has:

* **Label**: a short name (1–200 characters).
* **Phone number**: where to transfer the call.
* **When to transfer**: the condition, in plain English (1–2,000 characters).
* **Digits to dial after connecting** (optional): keypad tones to play once the destination answers, for example to reach an extension. Use `0`–`9`, `*`, `#`, `w` for a 0.5-second pause, and `W` for a 1-second pause, up to 50 characters. This field appears when **Allow playing touch tones** is on in [Advanced settings](/docs/reception-ai/receptionist/advanced-settings).

### Example transfer rules

| Label           | When to transfer                                          | Phone number        |
| --------------- | --------------------------------------------------------- | ------------------- |
| Owner           | Caller asks to speak with the owner or manager            | Owner's mobile      |
| Billing         | Caller has questions about billing, payments, or invoices | Finance line        |
| Emergency       | Caller describes an emergency                             | Emergency contact   |
| Specific person | Caller asks for Sarah by name                             | Sarah's direct line |

### Transfer availability and limits

* Transfers work on phone calls only, not on web conversations.
* Transfers are available for US businesses, and for any business whose receptionist uses only numbers from your own Twilio account or SIP trunk.
* Transferring to a number outside your business's country requires your own Twilio number or a paid plan.
* During the free trial, you can add or edit up to 10 transfer rules per day.

## Caller ID on transfers

By default, the person receiving a transferred call sees the caller's own number. This is a blind transfer: the call is handed over directly.

Turn on **Show your business number instead** to show your business number. The person receiving the call then hears a summary of the conversation before being connected, and the caller hears hold music while they wait.

This option is available when all of the receptionist's numbers are Twilio numbers.

## Verify caller identity

Protect client data by requiring callers to prove who they are before the receptionist reads or changes their records.

| Setting                        | Default | Behavior                                                                                                                                                                 |
| ------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Secure mode**                | Off     | The receptionist only looks up or changes a client's details when the caller's number matches the one on file. Clients created during the same conversation are trusted. |
| **Identity verification tool** | Off     | The receptionist can send a one-time code to the client's email or phone number on file and ask the caller to read it back.                                              |

With secure mode on, callers from an unknown number and website visitors must pass verification before accessing their records. Codes are sent by email by default. Sending by SMS requires an SMS-capable Twilio number. See [Notifications and SMS](/docs/reception-ai/features/notifications).

## Blocked numbers

Block phone numbers from reaching your receptionist. Blocked callers are rejected immediately. The block list applies to every receptionist in your workspace.

When blocking a number, you can add:

* **Reason**: a note for your team.
* **Block until**: an expiry date. Leave empty to block permanently.

You can also block a number from a conversation or a client profile.
