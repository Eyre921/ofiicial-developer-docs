---
title: "Overview"
source: https://upstash.com/docs/workflow/agents/overview
path: docs/workflow/agents/overview
---

The **Agents API** of Upstash Workflow enables you to:
* Execute an individual agent or facilitate collaboration among multiple agents.
* Integrate any tool compatible with AI SDK or LangChain.
* Reliably invoke agents without concerns about timeouts or transient errors.
* Unlike mainstream agent frameworks, we prioritize debuggability and extensibility.

To get started, you can refer to the [Getting Started page](/docs/workflow/agents/getting-started). For more details about the features, you can refer to [the Features page](/docs/workflow/agents/features).

<Note>
  This feature is not yet available in
  [workflow-py](https://github.com/upstash/workflow-py). See our
  [Roadmap](/docs/workflow/roadmap) for feature parity plans and
  [Changelog](/docs/workflow/changelog) for updates.
</Note>

## Agent Patterns

If you're interested, you can also explore our rich examples that showcase how various patterns can be built using the Agents API:

<CardGroup cols={2}>
  <Card title="Prompt Chaining" icon="link" href="/workflow/agents/patterns/prompt-chaining">
    Sequential LLM calls where each output becomes the input for the next, enabling structured reasoning and step-by-step task completion.
  </Card>
  <Card title="Evaluator-optimizer" icon="arrows-rotate" href="/workflow/agents/patterns/evaluator-optimizer">
    A feedback loop where LLM outputs are evaluated and refined iteratively to improve accuracy and relevance.
  </Card>
  <Card title="Parallelization" icon="arrows-to-dot" href="/workflow/agents/patterns/parallelization">
    Distribute tasks across multiple LLMs and aggregate the results for efficient handling of complex or large-scale operations.
  </Card>
  <Card title="Orchestrator-workers" icon="sparkles" href="/workflow/agents/patterns/orchestrator-workers">
    A central orchestrator directs multiple worker LLMs to complete subtasks and synthesize their outputs for complex operations.
  </Card>
</CardGroup>

## Real World Examples

Practical implementations demonstrating how to use our Agents API in production scenarios. These examples provide ready-to-use templates for common use cases.

<CardGroup cols={2}>
  <Card
    title="Browser Automation"
    icon="globe"
    href="https://github.com/upstash/workflow-js/blob/main/examples/agents/app/agentic-browser-search/route.ts"
  >
    Autonomous web navigation and interaction system for content extraction and
    form handling.
  </Card>
  <Card
    title="Email Analyzer"
    icon="envelope"
    href="https://github.com/upstash/workflow-js/blob/main/examples/agents/app/email-analyzer/route.ts"
  >
    Intelligent email processing system for content analysis, classification,
    and automated responses.
  </Card>
  <Card
    title="Social Media Manager"
    icon="share-nodes"
    href="https://github.com/upstash/workflow-js/blob/main/examples/agents-instagram-post-generator"
  >
    Multi-platform social media management system for content moderation and
    engagement automation.
  </Card>
</CardGroup>
