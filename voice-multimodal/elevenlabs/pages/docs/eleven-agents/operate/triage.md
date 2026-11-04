---
title: "Issues"
source: https://elevenlabs.io/docs/eleven-agents/operate/triage.md
path: docs/eleven-agents/operate/triage
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Issues

## Overview

Issues collect problems with an agent's real conversations so you can review and fix them in one place. Each issue describes one problem and, when it came from a conversation, links back to it. Every agent has an **Issues** tab, and a workspace-wide **Issues** page lists the issues across all of your agents. ElevenAgents Architect can read, comment on, and update issues when you ask it to.

> **Note**
>
> Issues are about an agent's own performance. They are separate from support tickets that an agent
> opens on behalf of an end user during a conversation.

![Issues queue for an agent](/docs/_fern-files/_img/9fe035e0f67b9c462de2e0260d9f93adfaef42303666b28e4e28e372f4185430.webp)

## Where issues come from

* **Agent**: a live agent calls the [flag issue for review](/docs/eleven-agents/customization/tools/system-tools/flag-issue-for-review) tool during a conversation.
* **Manual**: you or a teammate create an issue by hand, or ask Architect to open one, for a one-off fix or todo item.
* **Conversation review**: you or a teammate flag an issue while reviewing a transcript.
* **Test run**: you or a teammate create an issue from a test run's results.
* **Architect review (coming soon)**: Architect opens an issue after spotting a recurring pattern across recent conversations.

![Flag issue button on a conversation](/docs/_fern-files/_img/7ddb939cbd0cb690f643ad7051ae29dee94a33f5696f6ff4fe554e9e714afcac.webp)

## Issue statuses

| Status      | Meaning                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------- |
| Pending     | Not yet reviewed.                                                                           |
| In progress | Someone is actively working on it.                                                          |
| Resolved    | The underlying problem has been addressed.                                                  |
| Cancelled   | Closed without a fix, for example because it isn't a real problem or is no longer relevant. |
| Merged      | Grouped with another issue covering the same underlying problem.                            |

## Working through the queue with ElevenAgents Architect

Ask Architect to help you work through issues in plain language, for example:

* "Show me the open issues for this agent."
* "What's the most common issue this week?"
* "Summarize this issue and suggest a fix."
* "Mark this issue resolved."
* "Open an issue to update the refund policy in the knowledge base."

Architect can also propose grouping several issues that describe the same root cause, so you fix it once instead of issue by issue.
