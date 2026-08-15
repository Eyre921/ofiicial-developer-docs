---
title: "LangDB Integration"
source: https://docs.crewai.com/v1.15.16/en/observability/langdb
path: v1.15.16/en/observability/langdb
---

Govern, secure, and optimize your CrewAI workflows with LangDB AI Gateway—access 350+ models, automatic routing, cost optimization, and full observability.

# Introduction

[LangDB AI Gateway](https://langdb.ai) provides OpenAI-compatible APIs to connect with multiple Large Language Models and serves as an observability platform that makes it effortless to trace CrewAI workflows end-to-end while providing access to 350+ language models. With a single `init()` call, all agent interactions, task executions, and LLM calls are captured, providing comprehensive observability and production-ready AI infrastructure for your applications.

<Frame>
  <img alt="LangDB CrewAI trace example" />
</Frame>

**Checkout:** [View the live trace example](https://app.langdb.ai/sharing/threads/3becbfed-a1be-ae84-ea3c-4942867a3e22)

## Features

### AI Gateway Capabilities

* **Access to 350+ LLMs**: Connect to all major language models through a single integration
* **Virtual Models**: Create custom model configurations with specific parameters and routing rules
* **Virtual MCP**: Enable compatibility and integration with MCP (Model Context Protocol) systems for enhanced agent communication
* **Guardrails**: Implement safety measures and compliance controls for agent behavior

### Observability & Tracing

* **Automatic Tracing**: Single `init()` call captures all CrewAI interactions
* **End-to-End Visibility**: Monitor agent workflows from start to finish
* **Tool Usage Tracking**: Track which tools agents use and their outcomes
* **Model Call Monitoring**: Detailed insights into LLM interactions
* **Performance Analytics**: Monitor latency, token usage, and costs
* **Debugging Support**: Step-through execution for troubleshooting
* **Real-time Monitoring**: Live traces and metrics dashboard

## Setup Instructions

<Steps>
  <Step title="Install LangDB">
    Install the LangDB client with CrewAI feature flag:

    ```bash theme={null}
    pip install 'pylangdb[crewai]'
    ```
  </Step>

  <Step title="Set Environment Variables">
    Configure your LangDB credentials:

    ```bash theme={null}
    export LANGDB_API_KEY="<your_langdb_api_key>"
    export LANGDB_PROJECT_ID="<your_langdb_project_id>"
    export LANGDB_API_BASE_URL='https://api.us-east-1.langdb.ai'
    ```
  </Step>

  <Step title="Initialize Tracing">
    Import and initialize LangDB before configuring your CrewAI code:

    ```python theme={null}
    from pylangdb.crewai import init
    # Initialize LangDB
    init()
    ```
  </Step>

  <Step title="Configure CrewAI with LangDB">
    Set up your LLM with LangDB headers:

    ```python theme={null}
    from crewai import Agent, Task, Crew, LLM
    import os

    # Configure LLM with LangDB headers
    llm = LLM(
        model="openai/gpt-4o", # Replace with the model you want to use
        api_key=os.getenv("LANGDB_API_KEY"),
        base_url=os.getenv("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.getenv("LANGDB_PROJECT_ID")}
    )
    ```
  </Step>
</Steps>

## Quick Start Example

Here's a simple example to get you started with LangDB and CrewAI:

```python theme={null}
import os
from pylangdb.crewai import init
from crewai import Agent, Task, Crew, LLM

# Initialize LangDB before any CrewAI imports
init()

def create_llm(model):
    return LLM(
        model=model,
        api_key=os.environ.get("LANGDB_API_KEY"),
        base_url=os.environ.get("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.environ.get("LANGDB_PROJECT_ID")}
    )

# Define your agent
researcher = Agent(
    role="Research Specialist",
    goal="Research topics thoroughly",
    backstory="Expert researcher with skills in finding information",
    llm=create_llm("openai/gpt-4o"), # Replace with the model you want to use
    verbose=True
)

# Create a task
task = Task(
    description="Research the given topic and provide a comprehensive summary",
    agent=researcher,
    expected_output="Detailed research summary with key findings"
)

# Create and run the crew
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
print(result)
```

## Complete Example: Research and Planning Agent

This comprehensive example demonstrates a multi-agent workflow with research and planning capabilities.

### Prerequisites

```bash theme={null}
pip install crewai 'pylangdb[crewai]' crewai_tools setuptools python-dotenv
```

### Environment Setup

```bash theme={null}
# LangDB credentials
export LANGDB_API_KEY="<your_langdb_api_key>"
export LANGDB_PROJECT_ID="<your_langdb_project_id>"
export LANGDB_API_BASE_URL='https://api.us-east-1.langdb.ai'

# Additional API keys (optional)
export SERPER_API_KEY="<your_serper_api_key>"  # For web search capabilities
```

### Complete Implementation

```python theme={null}
#!/usr/bin/env python3

import os
import sys
from pylangdb.crewai import init
init()  # Initialize LangDB before any CrewAI imports
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

load_dotenv()

def create_llm(model):
    return LLM(
        model=model,
        api_key=os.environ.get("LANGDB_API_KEY"),
        base_url=os.environ.get("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.environ.get("LANGDB_PROJECT_ID")}
    )

class ResearchPlanningCrew:
    def researcher(self) -> Agent:
        return Agent(
            role="Research Specialist",
            goal="Research topics thoroughly and compile comprehensive information",
            backstory="Expert researcher with skills in finding and analyzing information from various sources",
            tools=[SerperDevTool()],
            llm=create_llm("openai/gpt-4o"),
            verbose=True
        )
    
    def planner(self) -> Agent:
        return Agent(
            role="Strategic Planner",
            goal="Create actionable plans based on research findings",
            backstory="Strategic planner who breaks down complex challenges into executable plans",
            reasoning=True,
            max_reasoning_attempts=3,
            llm=create_llm("openai/anthropic/claude-3.7-sonnet"),
            verbose=True
        )
    
    def research_task(self) -> Task:
        return Task(
            description="Research the topic thoroughly and compile comprehensive information",
            agent=self.researcher(),
            expected_output="Comprehensive research report with key findings and insights"
        )
    
    def planning_task(self) -> Task:
        return Task(
            description="Create a strategic plan based on the research findings",
            agent=self.planner(),
            expected_output="Strategic execution plan with phases, goals, and actionable steps",
            context=[self.research_task()]
        )
    
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.planner()],
            tasks=[self.research_task(), self.planning_task()],
            verbose=True,
            process=Process.sequential
        )

def main():
        topic = sys.argv[1] if len(sys.argv) > 1 else "Artificial Intelligence in Healthcare"
        
        crew_instance = ResearchPlanningCrew()
        
        # Update task descriptions with the specific topic
        crew_instance.research_task().description = f"Research {topic} thoroughly and compile comprehensive information"
    crew_instance.planning_task().description = f"Create a strategic plan for {topic} based on the research findings"
    
    result = crew_instance.crew().kickoff()
    print(result)

if __name__ == "__main__":
    main()
```

### Running the # CrewAI Documentation
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
