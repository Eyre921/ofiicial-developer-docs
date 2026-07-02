---
title: "Perplexity with Mastra"
source: https://docs.perplexity.ai/docs/getting-started/integrations/mastra
path: docs/getting-started/integrations/mastra
---

Use Perplexity models, the Agent API, and the Search API in your Mastra agents and tools.

## Overview

[Mastra](https://mastra.ai) is an open-source TypeScript framework for building AI agents and workflows. It ships first-class Perplexity integrations through its model router and tool system, so you can wire Perplexity into a Mastra `Agent` with a single string identifier or expose the Search API as a Mastra-compatible tool.

<Info>
  **Mastra** provides a unified `Agent` interface, a model router, and a tools/MCP system for orchestrating LLM workflows. Learn more at [mastra.ai](https://mastra.ai).
</Info>

The Mastra ecosystem provides three Perplexity integrations:

* **Perplexity model provider** — Use Perplexity's web-grounded models in a Mastra `Agent`.
* **Perplexity Agent provider** — Use the [Agent API](/docs/agent-api/quickstart) (OpenAI-compatible `/chat/completions`) through Mastra.
* **Perplexity Search tool** — Expose the [Search API](/docs/search/quickstart) as a Mastra tool for ranked web results.

## API Key Setup

All three integrations read your Perplexity API key from the environment:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

The Search tool also accepts `PPLX_API_KEY` as a fallback.

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate your API key from the Perplexity dashboard.
</Card>

## Perplexity Model Provider

Use Perplexity's web-grounded models inside a Mastra `Agent` through the model router.

```bash theme={null}
npm install @mastra/core
```

```ts theme={null}
import { Agent } from "@mastra/core/agent";

const agent = new Agent({
  id: "research-agent",
  name: "Research Agent",
  instructions: "Answer questions with up-to-date information from the web.",
  model: "perplexity/sonar",
});

const result = await agent.generate("What launched at the latest Perplexity event?");
console.log(result.text);
```

The agent supports both `agent.generate(...)` and `agent.stream(...)`. For the full list of Perplexity models available through the router, see the [Mastra Perplexity provider docs](https://mastra.ai/models/providers/perplexity).

## Perplexity Agent Provider

The Agent provider routes through Perplexity's OpenAI-compatible `/chat/completions` endpoint, giving you access to third-party models served by the [Agent API](/docs/agent-api/quickstart).

```ts theme={null}
import { Agent } from "@mastra/core/agent";

const agent = new Agent({
  id: "agent-api",
  name: "Agent API",
  instructions: "Use the best available model for the task.",
  model: "perplexity-agent/<model-id>",
});
```

For finer control — for example, custom headers or a pinned base URL — pass an object instead of a string:

```ts theme={null}
const agent = new Agent({
  id: "agent-api",
  name: "Agent API",
  instructions: "Use the best available model for the task.",
  model: {
    id: "perplexity-agent/<model-id>",
    url: "https://api.perplexity.ai/v1",
    apiKey: process.env.PERPLEXITY_API_KEY,
  },
});
```

See the [Mastra Perplexity Agent provider docs](https://mastra.ai/models/providers/perplexity-agent) for the full list of supported models and configuration options.

## Perplexity Search Tool

The `@mastra/perplexity` package wraps the [Search API](/docs/search/quickstart) as a Mastra-compatible tool. Use this when you want raw ranked web results — for chat completions or agentic workflows, prefer the model or Agent provider above.

```bash theme={null}
npm install @mastra/perplexity zod
```

```ts theme={null}
import { createPerplexitySearchTool } from "@mastra/perplexity";

const searchTool = createPerplexitySearchTool({
  apiKey: process.env.PERPLEXITY_API_KEY,
});

const results = await searchTool.execute({
  context: {
    query: "Latest advances in nuclear fusion",
    maxResults: 5,
    searchRecencyFilter: "month",
  },
});

for (const result of results) {
  console.log(result.title, result.url);
}
```

The tool ID is `perplexity-search` and supported input parameters include `query`, `maxResults`, `searchDomainFilter`, `searchRecencyFilter`, `searchAfterDateFilter`, and `searchBeforeDateFilter`. Each result includes `title`, `url`, `snippet`, and an optional `date`.

To register multiple Perplexity tools at once, use `createPerplexityTools(config?)`. See the [Mastra Perplexity tool reference](https://mastra.ai/reference/tools/perplexity) for the full schema.

## Links & Resources

<CardGroup>
  <Card title="Perplexity Model Provider" icon="cube" href="https://mastra.ai/models/providers/perplexity">
    Use Perplexity models in a Mastra `Agent`.
  </Card>

  <Card title="Perplexity Agent Provider" icon="robot" href="https://mastra.ai/models/providers/perplexity-agent">
    Use the Perplexity Agent API through Mastra.
  </Card>

  <Card title="Perplexity Search Tool" icon="search" href="https://mastra.ai/reference/tools/perplexity">
    Wrap the Perplexity Search API as a Mastra tool.
  </Card>

  <Card title="Mastra Docs" icon="book" href="https://mastra.ai/docs">
    Learn more about agents, tools, and workflows in Mastra.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [Mastra documentation](https://mastra.ai/docs)
* Review our [FAQ](/docs/resources/faq)
