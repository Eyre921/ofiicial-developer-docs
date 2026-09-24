---
title: "Customizing Architect"
source: https://elevenlabs.io/docs/eleven-agents/operate/architect/customization.md
path: docs/eleven-agents/operate/architect/customization
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Customizing Architect

## Overview

Architect's own instructions are fixed, but what it knows about your agent and how you like to work is not. From an agent's **Architect** tab, open **Customization** to manage three things: agent context, your preferences, and a prompt library.

> **Note**
>
> These documents only guide how Architect helps you build the agent. They do not change the agent's
> own runtime behavior or the system prompt it uses with callers.

## Agent context

Every agent has an `agents.md`-style context document that is sent to Architect at the start of every conversation about that agent. Use it to describe the agent's purpose, tone, domain, and any conventions your team follows, so you don't have to repeat that background every time you open a chat.

You can write this document directly, or ask Architect to draft or update it for you. Use the `/setup` slash command to have Architect walk you through creating one from scratch by asking a few clarifying questions.

## Your preferences

Alongside agent context, you have a personal preferences document that is shared across every agent you build, not just one. Use it for standing instructions that apply to you regardless of which agent you're editing, for example how you like changes explained, or when you want to be asked before Architect proceeds.

## Prompt library

Save prompts you use often, then insert them into the composer instead of retyping them. Prompts you save are yours by default; workspace members can also share prompts with their team so everyone starts from the same playbook for common tasks like reviewing triage tickets or writing a new system prompt.
