---
title: "Crew Studio"
source: https://docs.crewai.com/v1.15.7/en/enterprise/features/crew-studio
path: v1.15.7/en/enterprise/features/crew-studio
---

Build new automations with AI assistance, a visual editor, and integrated testing.

## Overview

Crew Studio is an interactive, AI‑assisted workspace for creating new automations from scratch using natural language and a visual workflow editor.

<Frame>
  <img alt="Crew Studio Overview" />
</Frame>

## Prompt‑based Creation

* Describe the automation you want; the AI generates agents, tasks, and tools.
* Use voice input via the microphone icon if preferred.
* Start from built‑in prompts for common use cases.

<Frame>
  <img alt="Prompt Builder" />
</Frame>

## Visual Editor

The canvas reflects the workflow as nodes and edges with three supporting panels that allow you to configure the workflow easily without writing code; a.k.a. "**vibe coding AI Agents**".

You can use the drag-and-drop functionality to add agents, tasks, and tools to the canvas or you can use the chat section to build the agents. Both approaches share state and can be used interchangeably.

* **AI Thoughts (left)**: streaming reasoning as the workflow is designed
* **Canvas (center)**: agents and tasks as connected nodes
* **Resources (right)**: drag‑and‑drop components (agents, tasks, tools)

<Frame>
  <img alt="Visual Canvas" />
</Frame>

## Execution & Debugging

Switch to the <b>Execution</b> view to run and observe the workflow:

* Event timeline
* Detailed logs (Details, Messages, Raw Data)
* Local test runs before publishing

<Frame>
  <img alt="Execution View" />
</Frame>

## Publish & Export

* <b>Publish</b> to deploy a live automation
* <b>Download</b> source as a ZIP for local development or customization

<Frame>
  <img alt="Publish & Download" />
</Frame>

Once published, you can view the automation details and have the **Options** dropdown menu to `chat with this crew`, `Export React Component` and `Export as MCP`.

<Frame>
  <img alt="Published Automation" />
</Frame>

## Best Practices

* Iterate quickly in Studio; publish only when stable
* Keep tools constrained to minimum permissions needed
* Use Traces to validate behavior and performance

## Related

<CardGroup>
  <Card title="Enable Crew Studio" href="/en/enterprise/guides/enable-crew-studio" icon="palette">
    Enable Crew Studio.
  </Card>

  <Card title="Build a Crew" href="/en/enterprise/guides/build-crew" icon="paintbrush">
    Build a Crew.
  </Card>

  <Card title="Deploy a Crew" href="/en/enterprise/guides/deploy-crew" icon="rocket">
    Deploy a Crew from GitHub or ZIP file.
  </Card>

  <Card title="Export a React Component" href="/en/enterprise/guides/react-component-export" icon="download">
    Export a React Component.
  </Card>
</CardGroup>
