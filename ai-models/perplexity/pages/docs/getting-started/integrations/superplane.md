---
title: "Perplexity with SuperPlane"
source: https://docs.perplexity.ai/docs/getting-started/integrations/superplane
path: docs/getting-started/integrations/superplane
---

Run Perplexity agents inside SuperPlane workflows — research, synthesis, and analysis steps with web search, URL fetching, and source citations.

## Overview

[SuperPlane](https://superplane.com) is an open-source DevOps control plane for long-lived, event-driven workflows. It exposes Perplexity as a native **component** on the canvas — drop a Perplexity node into any workflow and it runs a Perplexity agent with web search and URL fetching, then emits the response and source citations as a payload for downstream nodes.

<Info>
  **SuperPlane** models workflows as event-driven canvases: nodes emit payloads, downstream nodes subscribe to them, and the runtime tracks every run with full observability. Learn more at [superplane.com](https://superplane.com).
</Info>

## Component: Perplexity

The Perplexity component runs a Perplexity AI agent as a workflow step. Use it for research, synthesis, automated analysis, and content generation grounded in real-time web sources.

### Action

| Action        | Description                                                              |
| ------------- | ------------------------------------------------------------------------ |
| **Run Agent** | Run a Perplexity AI agent with web search and URL fetching capabilities. |

### Configuration

| Parameter        | Description                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Preset**       | Agent preset to use: `fast-search`, `pro-search`, `deep-research`, or `advanced-deep-research`. When set, `Model` is ignored. |
| **Model**        | Model identifier to use when no preset is specified (e.g., `sonar-pro`).                                                      |
| **Input**        | The prompt or question for the agent. Supports SuperPlane [expressions](https://docs.superplane.com/concepts/expressions).    |
| **Instructions** | Optional system-level instructions for the agent.                                                                             |
| **Web Search**   | Enable the `web_search` tool (default: `true`).                                                                               |
| **Fetch URL**    | Enable the `fetch_url` tool (default: `true`).                                                                                |

### Output Payload

The component emits a payload with these fields downstream nodes can access via expressions:

| Field       | Description                           |
| ----------- | ------------------------------------- |
| `text`      | The generated text response.          |
| `citations` | Source citations from web results.    |
| `model`     | The specific model used for this run. |
| `usage`     | Token and cost usage information.     |

## API Key Setup

Configure the Perplexity integration in SuperPlane with your API key. Open your canvas's **Integrations** settings, add a Perplexity integration, and paste your key.

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Quick Start

A minimal workflow that asks Perplexity a question whenever a manual run is triggered:

<Steps>
  <Step title="Add a Manual Run trigger">
    Drop a **Manual Run** node onto the canvas — this is the workflow's entry point.
  </Step>

  <Step title="Add a Perplexity node">
    Click **+ Components**, choose **Perplexity → Run Agent**, and drag it onto the canvas. Connect **Manual Run → Perplexity**.
  </Step>

  <Step title="Configure the agent">
    In the Perplexity node:

    * **Preset**: `pro-search`
    * **Input**: `What is the latest news on nuclear fusion?`
    * **Web Search**: enabled
    * **Fetch URL**: enabled
  </Step>

  <Step title="Run">
    Click **Run** on the Manual Run node. The Perplexity node emits a payload with `text`, `citations`, `model`, and `usage`.
  </Step>
</Steps>

## Reading the Response Downstream

Use SuperPlane expressions to pipe the Perplexity output into the next node — for example, a Slack message or a database write:

```
Research result: {{ $['Perplexity'].data.text }}

Sources:
{{ $['Perplexity'].data.citations }}
```

In condition fields (If / Filter), write expressions without `{{ }}`:

```
$['Perplexity'].data.usage.total_tokens > 1000
```

## Use Cases

* **Incident triage** — when an alert fires, run a Perplexity research step to gather background on a vendor, library, or CVE before paging on-call.
* **Release notes synthesis** — turn raw GitHub commit diffs into customer-facing release notes with citations.
* **Competitive monitoring** — schedule a daily canvas that queries Perplexity for industry news and posts a summary to a Slack channel.
* **Document grounding** — feed a Perplexity run's output into a downstream component that updates a Notion page or knowledge base.

## Links & Resources

<CardGroup>
  <Card title="SuperPlane Perplexity Component" icon="book" href="https://docs.superplane.com/components/perplexity">
    Official component documentation.
  </Card>

  <Card title="SuperPlane Docs" icon="globe" href="https://docs.superplane.com">
    Full SuperPlane documentation.
  </Card>

  <Card title="Perplexity Agent API" icon="robot" href="/docs/agent-api/quickstart">
    How the Perplexity agent layer works.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Sonar models.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [SuperPlane documentation](https://docs.superplane.com)
* Review our [FAQ](/docs/resources/faq)
