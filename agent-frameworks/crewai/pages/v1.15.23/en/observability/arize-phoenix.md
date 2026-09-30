---
title: "Arize Phoenix"
source: https://docs.crewai.com/v1.15.23/en/observability/arize-phoenix
path: v1.15.23/en/observability/arize-phoenix
---

Arize Phoenix integration for CrewAI with OpenTelemetry and OpenInference

# Arize Phoenix Integration

This guide demonstrates how to integrate **Arize Phoenix** with **CrewAI** using OpenTelemetry via the [OpenInference](https://github.com/openinference/openinference) SDK. By the end of this guide, you will be able to trace your CrewAI agents and debug agent behavior.

> **What is Arize Phoenix?** [Arize Phoenix](https://arize.com/phoenix/) is the open-source observability and evaluation option from [Arize AI](https://arize.com/?utm_source=crewai-docs\&utm_medium=partner\&utm_campaign=partner-docs\&utm_content=observability-arize-phoenix). Use Phoenix when you want to run locally or self-host. Use [Arize AX](https://arize.com/products/ax/) for a managed cloud or enterprise self-hosted platform for production AI systems.

[![Watch a Video Demo of Our Integration with Phoenix](https://storage.googleapis.com/arize-assets/fixtures/setup_crewai.png)](https://www.youtube.com/watch?v=Yc5q3l6F7Ww)

## Get Started

We'll walk through a simple example of using CrewAI and integrating it with Arize Phoenix via OpenTelemetry using OpenInference.

You can also access this guide on [Google Colab](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/tracing/crewai_tracing_tutorial.ipynb).

### Step 1: Install Dependencies

```bash theme={null}
pip install openinference-instrumentation-crewai crewai crewai-tools arize-phoenix-otel
```

### Step 2: Set Up Environment Variables

Configure your Phoenix API key and OpenTelemetry endpoint to send traces to Phoenix. The same setup works with a local or self-hosted Phoenix endpoint by changing the collector URL.

You can get your free Serper API key [here](https://serper.dev/).

```python theme={null}
import os
from getpass import getpass

# Get your Phoenix API key
PHOENIX_API_KEY = getpass("🔑 Enter your Phoenix API key: ")

# Get API keys for services
OPENAI_API_KEY = getpass("🔑 Enter your OpenAI API key: ")
SERPER_API_KEY = getpass("🔑 Enter your Serper API key: ")

# Set environment variables
os.environ["PHOENIX_CLIENT_H# CrewAI Documentation
Source: https://docs.crewai.com/index

Build collaborative AI agents, crews, and flows — production ready from day one.

<div>
  <img alt="CrewAI" />

  <div>
    <h1>Ship multi‑agent systems with confidence</h1>

    <p>
      Design agents, orchestrate crews, and automate flows with guardrails, memory, knowledge, and observability baked in.
    </p>
  </div>

  <div>
    <a href="/en/quickstart">
      Get started
    </a>

    <button type="button">
      Copy agent setup prompt
    </button>

    <a href="/guides/coding-tools/build-with-ai">
      Coding-agent guide
    </a>

    <a href="/en/api-reference/introduction">
      API Reference
    </a>
  </div>
</div>

<div />

## Get started

<CardGroup>
  <Card title="Introduction" href="/en/introduction" icon="sparkles">
    Overview of CrewAI concepts, architecture, and what you can build with agents, crews, and flows.
  </Card>

  <Card title="Installation" href="/en/installation" icon="wrench">
    Install via `uv`, configure API keys, and set up the CLI for local development.
  </Card>

  <Card title="Quickstart" href="/en/quickstart" icon="rocket">
    Spin up your first crew in minutes. Learn the core runtime, project layout, and dev loop.
  </Card>
</CardGroup>

## Build the basics

<CardGroup>
  <Card title="Agents" href="/en/concepts/agents" icon="users">
    Compose agents with tools, memory, knowledge, and structured outputs using Pydantic. Includes templates and best practices.
  </Card>

  <Card title="Flows" href="/en/concepts/flows" icon="arrow-progress">
    Orchestrate start/listen/router steps, manage state, persist execution, and resume long-running workflows.
  </Card>

  <Card title="Tasks & Processes" href="/en/concepts/tasks" icon="check">
    Define sequential, hierarchical, or hybrid processes with guardrails, callbacks, and human-in-the-loop triggers.
  </Card>
</CardGroup>

## Enterprise journey

<CardGroup>
  <Card title="Deploy automations" href="https://docs-platform.crewai.com/platform/en/features/automations" icon="server">
    Manage environments, redeploy safely, and monitor live runs directly from the Enterprise console.
  </Card>

  <Card title="Triggers & Flows" href="https://docs-platform.crewai.com/platform/en/guides/automation-triggers" icon="bolt">
    Connect Gmail, Slack, Salesforce, and more. Pass trigger payloads into crews and flows automatically.
  </Card>

  <Card title="Team management" href="https://docs-platform.crewai.com/platform/en/guides/team-management" icon="users-gear">
    Invite teammates, configure RBAC, and control access to production automations.
  </Card>
</CardGroup>

## What’s new

<CardGroup>
  <Card title="Triggers overview" href="https://docs-platform.crewai.com/platform/en/guides/automation-triggers" icon="sparkles">
    Unified overview for Gmail, Drive, Outlook, Teams, OneDrive, HubSpot, and more — now with sample payloads and crews.
  </Card>

  <Card title="Integration tools" href="/en/tools/integration/overview" icon="plug">
    Call existing CrewAI automations or Amazon Bedrock Agents directly from your crews using the updated integration toolkit.
  </Card>
</CardGroup>

<Callout title="Explore real-world patterns" icon="github">
  Browse the <a href="/en/examples/cookbooks">examples and cookbooks</a> for end-to-end reference implementations across agents, flows, and enterprise automations.
</Callout>

## Stay connected

<CardGroup>
  <Card title="Star us on GitHub" href="https://github.com/crewAIInc/crewAI" icon="star">
    If CrewAI helps you ship faster, give us a star and share your builds with the community.
  </Card>

  <Card title="Join the community" href="https://community.crewai.com" icon="comments">
    Ask questions, showcase workflows, and request features alongside other builders.
  </Card>
</CardGroup>
