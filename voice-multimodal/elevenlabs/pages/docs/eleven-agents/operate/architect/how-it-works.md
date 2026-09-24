---
title: "How Architect works"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/how-it-works.md
path: docs/eleven-agents/operate/architect/how-it-works
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How Architect works

## Overview

An Architect conversation runs as a real-time ElevenAgents conversation, using the same conversational engine that powers the agents you build. When you send a message, Architect decides whether to answer directly or call a tool, then streams its response back, the same way any voice or text agent would.

## What Architect can see

At the start of a conversation, Architect receives context about where you are and what you're working on:

* The page you're on, and, in the Architect tab, which agent you have open.
* That agent's current configuration, workflow, tools, tests, and knowledge base.
* Recent conversation transcripts and open triage tickets for that agent.
* The agent's `agents.md` context and your personal preferences, described in [Customizing Architect](/docs/eleven-agents/operate/architect/customization).

## What Architect can do

Architect's tool calls fall into two groups:

* **Interface tools**: small actions like navigating to a page, clicking a control, highlighting an element, or filling in a form field. These are available everywhere Architect runs.
* **Agent-building tools**: reading and editing an agent's configuration, workflow, procedures, tools, tests, and knowledge base; managing branches; and working the triage ticket queue. These are only available in the Architect tab, on the agent you have open.

Not every tool runs immediately. Changes that affect your agent are gated by an approval step and staged as a draft before anything goes live — see [Authentication, approvals, and drafts](/docs/eleven-agents/operate/architect/authentication) for the full flow.

## Getting Architect's attention

* **@-mentions**: reference a specific agent, tool, test, procedure, or knowledge base topic in your message so Architect knows exactly which resource you mean.
* **Slash commands**: type `/` in the composer to see available commands, including `/setup`, which walks you through writing an agent's initial `agents.md`.
* **Saved prompts**: reuse your own or your team's saved prompts from the prompt library instead of retyping common instructions. See [Customizing Architect](/docs/eleven-agents/operate/architect/customization).

## Proactive suggestions

Architect can offer to help without being asked, for example after a page error, when it notices an empty workflow, or when a batch of conversations looks worth reviewing. These suggestions appear as a prompt you can accept or dismiss; Architect never acts on them without your input.
