---
title: "Conversations"
source: https://elevenlabs.io/docs/reception-ai/features/conversations.md
path: docs/reception-ai/features/conversations
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Conversations

The **Conversations** page collects every interaction your receptionist handles. It has these tabs:

* **Conversations**: every call and website conversation.
* **Messages**: callback requests and voicemails left by callers.
* **Quote requests**: requests for jobs without a fixed price. See [Quote requests](/docs/reception-ai/features/quote-requests).

Questions your receptionist could not answer are collected separately in [FAQ](/docs/reception-ai/knowledge-base/faq).

## Conversations

Each conversation includes the full transcript, the start time, duration, and receptionist, and outcome labels:

| Outcome                     | Meaning                                                   |
| --------------------------- | --------------------------------------------------------- |
| **Appointment**             | A booking was made, or **Cancelled** if one was cancelled |
| **Order**                   | An order was placed or changed                            |
| **Client · New**            | A new client was created                                  |
| **Message**                 | The caller left a message                                 |
| **Question · Needs answer** | The receptionist could not answer a question              |

### Intent and priority

After each conversation, Reception.ai labels it with a short intent, such as "Roof Leak Repair", and a priority:

| Priority      | When it is used                                                                             |
| ------------- | ------------------------------------------------------------------------------------------- |
| **Emergency** | A safety-critical situation is still happening, such as a flood, fire, or medical emergency |
| **Urgent**    | The caller says it is time-sensitive and a missed callback has real consequences            |
| **Normal**    | Everything else                                                                             |

A situation that has already been made safe is urgent or normal, not an emergency.

### Filters

Filter conversations by date, receptionist, outcome (new client, new appointment, message, or unanswered question), status (successful, failed, or unknown), and channel (phone or web).

Review conversations regularly to verify your receptionist's answers and find patterns that suggest new rules, procedures, or knowledge base updates.

## Messages

When a caller wants a callback or asks to leave a message, the receptionist records it with a priority level. Messages come from phone calls and website chat.

Each message shows the caller's words, a short handover note from the receptionist, and the caller's number. Numbers typed in chat are marked as shared by the caller, since they cannot be verified.

Messages are linked to a client automatically when the caller's phone number is usable. From each message you can:

* **Open contact** or **Create contact**
* **View conversation**
* **Mark as read** or **Mark as unread**
* **Delete message**

Filter messages by priority, read state, and date. The **Conversations** item in the sidebar shows the number of unread messages, highlighted in red when any are emergency or urgent.

> **Note**
>
> To stop taking messages, turn off **Messages** in **Settings** → **Features**.
