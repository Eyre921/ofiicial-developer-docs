---
title: "Perplexity with AG2"
source: https://docs.perplexity.ai/docs/getting-started/integrations/ag2
path: docs/getting-started/integrations/ag2
---

Use the Perplexity Search API as a tool inside AG2 (AutoGen) agents.

## Overview

AG2 ships a `PerplexitySearchToolkit` that wraps the [Perplexity Search API](/docs/search/quickstart) as a native AG2 tool. The tool returns ranked web results — title, URL, snippet, and date — without generating an LLM answer, which keeps token usage minimal and lets the calling agent decide how to consume them.

<Info>
  **AG2** (formerly AutoGen) is an open-source framework for building multi-agent conversational AI systems. Learn more at [ag2.ai](https://ag2.ai).
</Info>

## Installation

```bash theme={null}
pip install "ag2[perplexity]"
```

## API Key Setup

Set your Perplexity API key as an environment variable, or pass it to the toolkit constructor:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start

Register `PerplexitySearchToolkit` with an AG2 `Agent`:

```python theme={null}
from autogen.beta import Agent
from autogen.beta.tools.search import PerplexitySearchToolkit

toolkit = PerplexitySearchToolkit()
search = toolkit.search()

agent = Agent(
    "researcher",
    prompt="Answer using fresh information from the web.",
    tools=[search],
)

await agent.ask("What were the top tech announcements this week?")
```

The tool calls the Perplexity Search API under the hood and returns structured `PerplexitySearchResult` objects.

## Configuration

All search parameters are passed to `toolkit.search()` and forwarded to the Search API:

```python theme={null}
from autogen.beta.tools.search import PerplexitySearchToolkit

toolkit = PerplexitySearchToolkit()
search = toolkit.search(
    max_results=5,
    max_tokens_per_page=512,
    search_domain_filter=["arxiv.org", "-medium.com"],  # prefix with '-' to exclude
    search_recency_filter="week",                         # hour | day | week | month | year
    search_after_date_filter="1/1/2025",
    search_before_date_filter="12/31/2025",
)
```

You can also pass any parameter as an AG2 `Variable` so it can be resolved from the conversation context at runtime:

```python theme={null}
from autogen.beta import Variable
from autogen.beta.tools.search import PerplexitySearchToolkit

toolkit = PerplexitySearchToolkit()
search = toolkit.search(
    max_results=Variable("user_max"),
    search_recency_filter=Variable(),  # resolved from the variable named after the parameter
)
```

## Response Shape

Each call returns a `PerplexitySearchResponse` with the original query and a list of `PerplexitySearchResult` items:

```python theme={null}
@dataclass(slots=True)
class PerplexitySearchResult:
    title: str
    url: str
    snippet: str | None = None
    date: str | None = None

@dataclass(slots=True)
class PerplexitySearchResponse:
    query: str
    results: list[PerplexitySearchResult]
    content: str | None = None
    citations: list[str]
    images: list[PerplexityImageMeta]
```

## Links & Resources

<CardGroup>
  <Card title="AG2 Docs" icon="book" href="https://docs.ag2.ai">
    Build multi-agent systems with AG2.
  </Card>

  <Card title="Tool Source" icon="brand-github" href="https://github.com/ag2ai/ag2/blob/main/autogen/beta/tools/search/perplexity.py">
    PerplexitySearchToolkit implementation.
  </Card>

  <Card title="Search API Quickstart" icon="search" href="/docs/search/quickstart">
    Learn more about the underlying Perplexity Search API.
  </Card>

  <Card title="Common Toolkits" icon="toolbox" href="https://docs.ag2.ai/docs/beta/tools/common_toolkits">
    Browse all built-in AG2 tools.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [AG2 documentation](https://docs.ag2.ai)
* Review our [FAQ](/docs/resources/faq)
