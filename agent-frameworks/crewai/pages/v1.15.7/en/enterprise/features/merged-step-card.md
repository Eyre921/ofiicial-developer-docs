---
title: "One Card per Step"
source: https://docs.crewai.com/v1.15.7/en/enterprise/features/merged-step-card
path: v1.15.7/en/enterprise/features/merged-step-card
---

Each step on the Studio canvas is a single card that combines the task and the agent that performs it.

## Overview

On the Studio canvas, each step of work is represented by a **single card**. The card combines two things that used to live in separate nodes:

* **The task** — what to do (name, description, expected output, and response format).
* **The agent** — who does it (the assigned agent, its model, and its tools).

An agent isn't an independent participant in your workflow — it's an attribute of the task: *which agent performs this work.* Putting the task and its agent on one card makes that relationship explicit and turns your automation into a single, left-to-right chain of work units that's easier to read at a glance.

<Frame>
  <img alt="Merged step cards on the canvas" />
</Frame>

## On the canvas

Each collapsed card shows:

* The **task name and description** at the top.
* A **footer summarizing the assigned agent** — avatar, name, model, and tools.

There's no separate agent node and no vertical agent → task edge. Your steps connect directly to one another in the order they run.

## In the editor

Open a card to edit it. The expanded view is the same card in a detailed state — not a different screen — organized into two clearly labeled sections.

<Frame>
  <img alt="Expanded step editor" />
</Frame>

### The task — what to do

Open by default, since this is what you usually edit:

* **Name**
* **Description**
* **Expected Output**
* **Response Format** — surfaced here because it controls exactly what downstream steps (such as routing) read from this step.

### The agent — who does it

The assigned agent is shown as a summary — **name, model, and tools inline**. Its deeper configuration is preserved behind two disclosures:

* **Role, goal & backstory**
* **Agent settings** — reasoning, max reasoning attempts, allow delegation, max iterations, and LLM settings.

<Tip>
  An agent's full configuration — Role, Goal, Backstory, Model, Tools, LLM Settings, and the complete Agent Settings block — lives behind the **Role, goal & backstory** and **Agent settings** disclosures, organized by how often you edit it.
</Tip>

## Swapping vs. editing the agent

There are two distinct ways to work with the agent on a card, and they do different things:

* **Swap** reassigns *which* agent performs this task. Use the **Swap** control to pick a different agent from this project, choose one from your Agent Repository, or create a new agent. This is scoped to the task.
* **Editing** the agent — opening **Role, goal & backstory** or **Agent settings** — changes the agent *itself*.

<Frame>
  <img alt="Swap agent panel" />
</Frame>

<Warning>
  **Agents are reusable and shared.** The same agent can perform more than one task across your project. Editing an agent's role, backstory, or settings updates that agent **everywhere it's used** — not just on the card you opened. If you want a change to apply to only one step, **Swap** in a different agent instead of editing the shared one.
</Warning>

## Related

<CardGroup>
  <Card title="Crew Studio" href="/en/enterprise/features/crew-studio" icon="pencil">
    Build automations with AI assistance and a visual editor.
  </Card>

  <Card title="Agent Repositories" href="/en/enterprise/features/agent-repositories" icon="users">
    Manage and reuse agents across your automations.
  </Card>
</CardGroup>
