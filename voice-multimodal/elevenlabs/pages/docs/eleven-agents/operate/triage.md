---
title: "Triage"
source: https://elevenlabs.io/docs/eleven-agents/operate/triage.md
path: docs/eleven-agents/operate/triage
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Triage

## Overview

Triage tickets collect problems with an agent's real conversations so you can review and fix them in one place. Each ticket points at the underlying issue and the conversation it came from. Architect surfaces the ticket queue for whichever agent you have open, and can read, comment on, and update tickets when you ask it to.

> **Note**
>
> Triage tickets are about an agent's own performance. They are separate from support tickets that
> an agent opens on behalf of an end user during a conversation.

![Triage queue for an agent](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9fe035e0f67b9c462de2e0260d9f93adfaef42303666b28e4e28e372f4185430/assets/images/agents/triage-queue.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T113218Z&X-Amz-Expires=604800&X-Amz-Signature=ae6ebb0727208bdb8d9e42c81348bfeccece930d7014e2d20dad7686a2f659c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Where tickets come from

* **Flagged issue**: a live agent calls the [flag issue for review](/docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review) tool during a conversation.
* **Manual**: you or a teammate create a ticket by hand for a one-off fix or todo item.
* **Conversation review**: you or a teammate open a ticket while reviewing a transcript.
* **Architect review (coming soon)**: Architect opens a ticket after spotting a recurring pattern across recent conversations.

![Flag issue button on a conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7ddb939cbd0cb690f643ad7051ae29dee94a33f5696f6ff4fe554e9e714afcac/assets/images/agents/triage-manual-flag.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T113218Z&X-Amz-Expires=604800&X-Amz-Signature=4e3fdc7be529b88eca999e9697cf051b9011be09f29363dc24441111ec93c4c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Ticket statuses

| Status      | Meaning                                                           |
| ----------- | ----------------------------------------------------------------- |
| Open        | Not yet reviewed.                                                 |
| In progress | Someone is actively working on it.                                |
| Resolved    | The underlying issue has been addressed.                          |
| Merged      | Grouped with another ticket covering the same underlying problem. |

## Working through the queue with Architect

Ask Architect to help you triage in plain language, for example:

* "Show me the open tickets for this agent."
* "What's the most common issue this week?"
* "Summarize this ticket and suggest a fix."
* "Mark this ticket resolved."

Architect can also propose grouping several tickets that describe the same root cause, so you fix it once instead of ticket by ticket.
