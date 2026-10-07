---
title: "ElevenAgents Architect"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect.md
path: docs/eleven-agents/operate/architect
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenAgents Architect

## Overview

ElevenAgents Architect is the AI assistant built into ElevenAgents. You describe what you want in plain language, and Architect reads your agent's configuration, conversations, and test results, makes the change, and validates it with tests before you decide whether to ship it.

Architect works with the same objects you edit by hand: the system prompt, procedures, workflow, tools, knowledge base, guardrails, tests, branches, and merge proposals. It has no separate hidden configuration. Every change it makes appears in the same draft, diff, and version history as a change you made yourself.

![Architect tab home screen](/docs/_fern-img/ed0d216d50539bce021442606fa5a8b82bd29b1596707571e2247081c399546d.webp)

## What ElevenAgents Architect is for

Architect is most useful for improving an agent you have already deployed. It is built around this loop:

1. **Investigate.** Read real conversations, Spotlight insights, alerts, triage tickets, and failing tests to find what is going wrong and why.
2. **Change.** Edit the prompt, a procedure, a tool, the knowledge base, or guardrails. Agent configuration changes are staged as an unpublished draft, never applied to live callers directly.
3. **Validate.** Write tests and simulations for the change and run them inside the same conversation, before you are asked to ship anything.
4. **Propose.** Hand the change to you for review: you publish the draft, and Architect can open a [merge proposal](/docs/eleven-agents/operate/architect/proposals) for a teammate to approve and suggest a small traffic split to try it on live calls.

Architect also builds new agents from a description, answers product questions, and walks you through the dashboard.

See [How Architect works](/docs/eleven-agents/operate/architect/how-it-works) for a full worked example of this loop, showing each tool Architect calls.

## ElevenAgents Architect and Spotlight

[Spotlight](/docs/eleven-agents/dashboard/spotlight) and Architect do different jobs.

| Product   | Role                  | What it does                                                                                                                                                   |
| --------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spotlight | Observe and recommend | Monitors an agent's conversations and surfaces a weekly summary, suggested investigations, real-time alerts, and configuration recommendations.                |
| Architect | Build and fix         | Investigates a question or a Spotlight finding against the underlying data, changes the agent, writes and runs tests, and prepares the change for your review. |

Spotlight cards hand off to Architect with buttons such as **Analyze with Architect** and **Investigate with Architect**. See [Starting a conversation](/docs/eleven-agents/operate/architect/entry-points#spotlight) for what each hand-off passes in.

## Availability

Architect is in alpha. Some surfaces, such as the per-agent Architect tab and the triage queue, are being rolled out gradually and may not appear in every workspace yet. Architect is free to use during the alpha period, which runs through October 2026. During the alpha, Architect conversations do not count against your workspace's agent minutes or LLM cost. Check the [pricing page](https://elevenlabs.io/pricing) for terms after the alpha ends.

Some limits apply:

* Attaching files in the composer requires a Creator plan or higher.
* An idle Architect session ends after 5 minutes, or 15 minutes on Enterprise plans. You can continue the conversation from chat history.
* Conversation analysis is limited to 100 analyzed conversations per user per minute.

See [Limitations and FAQ](/docs/eleven-agents/operate/architect/faq) for what Architect does not do today.

## Privacy and data retention

> **Warning**
>
> Architect conversations are not covered by Zero Retention Mode (ZRM). Avoid sharing personal or
> sensitive information in messages to Architect.

Your Architect chats are private to you. Teammates cannot open them, even when a chat was started from a shared triage ticket. For details on what ZRM does cover, see [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm).

## Learn more

#### [Starting a conversation](/docs/eleven-agents/operate/architect/entry-points)

Every place you can open Architect, and the context each one passes in.

#### [How ElevenAgents Architect works](/docs/eleven-agents/operate/architect/how-it-works)

What Architect knows, how it investigates, and a worked example of the improvement loop.

#### [What ElevenAgents Architect can change](/docs/eleven-agents/operate/architect/capabilities)

The full list of what Architect can read and edit, and what needs your approval.

#### [Proposals and validation](/docs/eleven-agents/operate/architect/proposals)

How Architect's changes are tested, reviewed, and rolled out.

#### [Permissions, approvals, and drafts](/docs/eleven-agents/operate/architect/authentication)

How Architect acts on your behalf and stages changes safely.

#### [Customizing ElevenAgents Architect](/docs/eleven-agents/operate/architect/customization)

Give Architect durable context about your agent and how you work.

#### [Claude, Cursor, and other AI assistants](/docs/eleven-agents/operate/architect/external-assistants)

Manage agents from outside the ElevenLabs dashboard.

#### [Limitations and FAQ](/docs/eleven-agents/operate/architect/faq)

What Architect does not do yet, and common questions.
