---
title: "Inbox"
source: https://elevenlabs.io/docs/reception-ai/features/inbox.md
path: docs/reception-ai/features/inbox
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Inbox

**Inbox** in the sidebar collects every interaction your receptionist handles. It has four views:

* **All conversations**: every call and website chat, except spam.
* **Needs attention**: open messages, quote requests, and caller questions, and calls marked urgent or emergency. See [Quote requests](/docs/reception-ai/features/quote-requests).
* **Done**: conversations and items you have finished, such as messages marked done, converted quote requests, and answered questions.
* **Spam**: calls marked as spam. The view shows how many there are, and a dot when one is unread.

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

### Caller details

A phone call shows the caller's number, or **Not shared** when there is none. If the number does not belong to a client yet, select **Save as contact**. If several clients share the number, select **Choose client** and pick who the call was with.

### Done and spam

Select **Done** on an open conversation to move it to the **Done** view, and **Reopen** to bring it back. A conversation also leaves **Done** when something in it is reopened.

Select **Spam** to move a call to the **Spam** view. Spam calls show **Spam** as their status and never appear in **Needs attention** or **Done**. If a call was marked as spam by mistake, open it in the **Spam** view and select **Not spam**.

On a spam call, select **Block** next to the caller's number to block it. The reason is set to **Spam**.

If your business is in the US and spam protection is off, **All conversations** and **Spam** show a **Keep spam calls out** banner, which you can dismiss. Select **Turn on spam protection** to switch it on. See [Call handling](/docs/reception-ai/receptionist/call-handling#verify-caller-identity).

### Intent and priority

After each conversation, Reception.ai labels it with a short intent, such as "Roof Leak Repair", and a priority:

| Priority      | When it is used                                                                             |
| ------------- | ------------------------------------------------------------------------------------------- |
| **Emergency** | A safety-critical situation is still happening, such as a flood, fire, or medical emergency |
| **Urgent**    | The caller says it is time-sensitive and a missed callback has real consequences            |
| **Normal**    | Everything else                                                                             |

A situation that has already been made safe is urgent or normal, not an emergency. Messages from sales pitches, vendors, recruiters, robocalls, and payment demands are normal, however pressing they sound.

A call's priority is never lower than the priority of the messages left on it, unless the call is spam.

Review conversations regularly to verify your receptionist's answers and find patterns that suggest new rules, procedures, or knowledge base updates.

### Search

The list has a **Search** field with the placeholder **Name, phone, topic or summary**. A search is ignored until it contains two letters, numbers, or underscores in a row, and it can be up to 100 characters. A phone number can include spaces, dots, dashes, or brackets.

Search matches the conversation title and summary when those are kept, a client's name or phone, the name, phone, and text of messages and quote requests, and questions the receptionist saved. It also matches the number a call came from, even when that caller is not a saved client. Titles, messages, quote requests, and clients each contribute their 500 most recent matches.

When nothing matches, the list shows **No results**.

**More actions** includes **Mark all as read**. It is unavailable in **Done**, while a search is active, and when the view has nothing unread.

## Messages

When a caller wants a callback or asks to leave a message, the receptionist records it with a priority level. Messages come from phone calls and website chat. If the caller adds details or changes something later in the same call, the receptionist updates that message instead of leaving a second one.

Each message shows the caller's words, a short handover note from the receptionist, and the caller's number. Numbers typed in chat are marked as shared by the caller, since they cannot be verified.

Once the caller wants something passed on and the receptionist knows what it is about, it saves the message then, before asking for anything still missing. It uses the number on the call when there is one, and the caller's name as heard, and does not ask the caller to spell their name. A number given without a country code is treated as a local number in the business's country, or as a US number when **Country** is not set.

A new phone message with no number the caller gave stores the number the call came from, so you can call back. A withheld or shared carrier number is not stored. Updating a message does not replace a number the caller gave with the calling number.

Messages are linked to a client automatically when the caller's phone number is usable. From each message you can:

* Select the client's name to open their record, or **Save contact** if the caller is not a client yet.
* Select **Mark done** when you have handled it, or **Reopen** to bring it back to **Needs attention**.

The **Inbox** item in the sidebar shows the number of unread messages, highlighted in red when any are emergency or urgent.

## Call privacy

**Settings** → **Privacy** opens **Call privacy**. These settings only affect phone call recordings and transcripts. Your clients, appointments, notes, and interaction history are always saved, and these options never delete them.

| Setting                                    | Default                                                     |
| ------------------------------------------ | ----------------------------------------------------------- |
| **Store call recordings**                  | On. When off, only the written transcript is kept.          |
| **Auto-delete calls after a fixed period** | Off. Recordings and transcripts stay until you delete them. |

Turning auto-delete on shows **Days to keep calls**, starting at 30. Set it to 0 and the label reads **Deleted soon after the call ends**. **Delete call transcripts** and **Delete call recordings** appear when auto-delete is on and the number of days is greater than 0. **Apply to past calls too** appears only when you change how long calls are kept. When it is off, only new calls follow the new period.

Changing these settings requires an active Premium plan. On any other plan, including the free trial, settings you already saved stay as they are. A change is refused with: "Privacy settings are available on the Premium plan. Upgrade to Premium to change them."
