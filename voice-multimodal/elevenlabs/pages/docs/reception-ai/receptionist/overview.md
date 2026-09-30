---
title: "Your receptionist"
source: https://elevenlabs.io/docs/reception-ai/receptionist/overview.md
path: docs/reception-ai/receptionist/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Your receptionist

Your AI receptionist is a voice agent that answers inbound phone calls and website conversations on behalf of your business. It speaks naturally, understands context, and performs actions such as booking appointments, taking orders, transferring calls, and taking messages.

## What your receptionist can do

* **Answer calls**: greets callers with your first message, or waits for them to speak if the greeting is empty.
* **Book appointments**: checks availability and books, reschedules, or cancels.
* **Take orders and quote requests**: when [orders](/docs/reception-ai/features/orders) or [quotes](/docs/reception-ai/features/quote-requests) are enabled.
* **Answer questions**: uses your knowledge base and FAQ answers.
* **Take messages**: records callback requests with a priority level.
* **Transfer calls**: routes callers to people on your team based on transfer rules.
* **Speak multiple languages**: switches to the caller's language when it is one of your configured languages.
* **Collect information**: identifies callers and creates or updates client records.

## How it works

When a call comes in:

1. The receptionist greets the caller.
2. It identifies what the caller wants.
3. It follows your rules on every call, and runs a procedure when the caller's request matches one.
4. For bookings, it checks your calendar and offers available slots.
5. If it cannot answer a question, it logs the question in your [FAQ](/docs/reception-ai/knowledge-base/faq) for you to answer.

## The Receptionists page

Open **Receptionists** in the sidebar. The top of the page shows the receptionist's status, its phone numbers, and its languages. Below that, settings are grouped into cards:

| Group              | Cards                                                                                                                             | Details                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Personality**    | Voice, Tone, Greeting                                                                                                             | [Voice and personality](/docs/reception-ai/receptionist/voice-and-personality) |
| **On the call**    | Answering order, Forward an existing number, Transfer to a human, Caller ID on transfers, Verify caller identity, Blocked numbers | [Call handling](/docs/reception-ai/receptionist/call-handling)                 |
| **Instructions**   | Teach your receptionist, Additional instructions                                                                                  | [Rules and procedures](/docs/reception-ai/receptionist/rules-and-procedures)   |
| **How it works**   | Knows your business from, Integrations, Advanced settings                                                                         | [Advanced settings](/docs/reception-ai/receptionist/advanced-settings)         |
| **Communications** | Appointment reminders, Booking confirmations, Staff notifications, Call summaries                                                 | [Notifications and SMS](/docs/reception-ai/features/notifications)             |

Cards marked **Workspace** apply to every receptionist in your workspace, not only the one you are editing.

## Receptionist status

| Status                          | Meaning                                                                 |
| ------------------------------- | ----------------------------------------------------------------------- |
| **Live**                        | Active, has a phone number, and is answering calls                      |
| **Missing phone number**        | Active, but no number is assigned. Add one from the **Phone** tile.     |
| **Waiting for number approval** | The assigned number is held until a regulatory request is approved      |
| **Deactivated**                 | Paused, for example after a plan change. Select **Activate** to resume. |

## Multiple receptionists

You can create more than one receptionist, each with its own voice, rules, procedures, and phone numbers. Use multiple receptionists to:

* Separate departments, such as sales and support
* Serve multiple locations with location-specific knowledge
* Run a separate receptionist per language or brand

To add one, open the receptionist switcher at the top of the page and select **Create a new receptionist**. Settings are copied from the selected receptionist, and you can change them after creation. You can delete a receptionist, but you must keep at least one.

## Configuration review

After you save additional instructions, the greeting, a rule, or a procedure, Reception.ai reviews the text in the background for contradictions and problems. Findings appear as a warning icon in the header. Open it to see **Check your configuration**, then select **Fix with assistant** to have the [business assistant](/docs/reception-ai/features/assistant) propose a fix, or **Got it** to dismiss the finding.
