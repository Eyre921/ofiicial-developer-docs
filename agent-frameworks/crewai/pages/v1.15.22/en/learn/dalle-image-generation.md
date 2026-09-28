---
title: "Image Generation with DALL-E"
source: https://docs.crewai.com/v1.15.22/en/learn/dalle-image-generation
path: v1.15.22/en/learn/dalle-image-generation
---

Learn how to use DALL-E for AI-powered image generation in your CrewAI projects

CrewAI supports integration with OpenAI's DALL-E, allowing your AI agents to generate images as part of their tasks. This guide will walk you through how to set up and use the DALL-E tool in your CrewAI projects.

## Prerequisites

* crewAI installed (latest version)
* OpenAI API key with access to DALL-E

## Setting Up the DALL-E Tool

<Steps>
  <Step title="Import the DALL-E tool">
    ```python theme={null}
    from crewai_tools import DallETool
    ```
  </Step>

  <Step title="Add the DALL-E tool to your agent configuration">
    ```python theme={null}
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), DallETool()],  # Add DallETool to the list of tools
            allow_delegation=False,
            verbose=True
        )
    ```
  </Step>
</Steps>

## Using the DALL-E Tool

Once you've added the DALL-E tool to your agent, it can generate images based on text prompts. The tool will return a URL to the generated image, which can be used in the agent's output or passed to other agents for further processing.

### Example Agent Configuration

```yaml theme={null}
role: >
    LinkedIn Profile Senior Data Researcher
goal: >
    Uncover detailed LinkedIn profiles based on provided name {name} and domain {domain}
    Generate a Dall-e image based on domain {domain}
backstory: >
    You're a seasoned researcher with a knack for uncovering the most relevant LinkedIn profiles.
    Known for your ability to navigate LinkedIn efficiently, you excel at gathering and presenting
    professional information clearly and concisely.
```

### Expected Output

The agent with the DALL-E tool will be able to generate the image and provide a URL in its response. You can then download the image.

<Frame>
  <img alt="DALL-E Image" />
</Frame>

## Best Practices

1. **Be# CrewAI Documentation
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
