---
title: "Neatlogs Integration"
source: https://docs.crewai.com/v1.15.14/en/observability/neatlogs
path: v1.15.14/en/observability/neatlogs
---

Understand, debug, and share your CrewAI agent runs

# Introduction

Neatlogs helps you **see what your agent did**, **why**, and **share it**.

It captures every step: thoughts, tool calls, responses, evaluations. No raw logs. Just clear, structured traces. Great for debugging and collaboration.

## Why use Neatlogs?

CrewAI agents use multiple tools and reasoning steps. When something goes wrong, you need context — not just errors.

Neatlogs lets you:

* Follow the full decision path
* Add feedback directly on steps
* Chat with the trace using AI assistant
* Share runs publicly for feedback
* Turn insights into tasks

All in one place.

Manage your traces effortlessly

<img alt="Traces" />

<img alt="Trace Response" />

The best UX to view a CrewAI trace. Post comments anywhere you want. Use AI to debug.

<img alt="Trace Details" />

<img alt="Ai Chat Bot With A Trace" />

<img alt="Comments Drawer" />

## Core Features

* **Trace Viewer**: Track thoughts, tools, and decisions in sequence
* **Inline Comments**: Tag teammates on any trace step
* **Feedback & Evaluation**: Mark outputs as correct or incorrect
* **Error Highlighting**: Automatic flagging of API/tool failures
* **Task Conversion**: Convert comments into assigned tasks
* **Ask the Trace (AI)**: Chat with your trace using Neatlogs AI bot
* **Public Sharing**: Publish trace links to your community

## Quick Setup with CrewAI

<Steps>
  <Step title="Sign Up & Get API Key">
    Visit [neatlogs.com](https://neatlogs.com/?utm_source=crewAI-docs), create a project, copy the API key.
  </Step>

  <Step title="Install SDK">
    ```bash theme={null}
    pip install neatlogs
    ```

    (Latest version 0.8.0, Python 3.8+; MIT license)
  </Step>

  <Step title="Initialize Neatlogs">
    Before starting Crew agents, add:

    ```python theme={null}
    import neatlogs
    neatlogs.init("YOUR_PROJECT_API_KEY")
    ```

    Agents run as usual. Neatlogs captures everything automatically.
  </Step>
</Steps>

## Under the Hood

According to GitHub, Neatlogs:

* Captures thoughts, tool calls, responses, errors, and token stats
* Supports AI-powered task generation and robust evaluation workflows

All with just two lines of code.

## Watch It Work

### 🔍 Full Demo (4 min)

<iframe title="NeatLogs overview" />

### ⚙️ CrewAI Integration (30 s)

<iframe title="Loom video player" />

## Links & Support

* 📘 [Neatlogs Docs](https://docs.neatlogs.com/)
* 🔐 [Dashboard & API Key](https://app.neatlogs.com/)
* 🐦 [Follow on Twitter](https://twitter.com/neatlogs)
* 📧 Contact: [hello@neatlogs.com](mailto:hello@neatlogs.com)
* 🛠 [GitHub SDK](https://github.com/NeatLogs/neatlogs)

## TL;DR

With just:

```bash theme={null}
pip install neatlogs

import neatlogs
neatlogs.init("YOUR_API_KEY")

You can now capture, understand, share, and act on your CrewAI agent runs in seconds.
No setup overhead. Full trace transparency. Full team collaboration.
```
