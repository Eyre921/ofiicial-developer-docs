---
title: "Perplexity with CAMEL-AI"
source: https://docs.perplexity.ai/docs/getting-started/integrations/camel
path: docs/getting-started/integrations/camel
---

Use the Perplexity Search API as a tool inside CAMEL-AI multi-agent systems.

## Overview

CAMEL-AI's `SearchToolkit` ships a `search_perplexity` method that wraps the [Perplexity Search API](/docs/search/quickstart) as a native CAMEL tool. The tool returns ranked web results — title, URL, snippet, and date — so the calling `ChatAgent` can ground its responses on fresh, citable sources.

<Info>
  **CAMEL-AI** is an open-source framework for building communicative multi-agent systems. Learn more at [camel-ai.org](https://www.camel-ai.org).
</Info>

## Installation

```bash theme={null}
pip install camel-ai
```

## API Key Setup

Set your Perplexity API key as an environment variable:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start

Register `search_perplexity` as a tool on a `ChatAgent`:

```python theme={null}
from camel.agents import ChatAgent
from camel.toolkits import FunctionTool, SearchToolkit

agent = ChatAgent(
    system_message=(
        "You are a helpful assistant that can use the Perplexity "
        "search engine to answer questions."
    ),
    tools=[FunctionTool(SearchToolkit().search_perplexity)],
)

response = agent.step(
    input_message="What are the latest developments in multi-agent AI systems?",
    response_format=None,
)
print(response.msgs[0].content)
```

The tool calls `POST https://api.perplexity.ai/search` under the hood and returns the raw API response so the agent can pick which results to cite.

## Configuration

All Search API parameters are supported directly on `search_perplexity`:

```python theme={null}
from camel.toolkits import SearchToolkit

toolkit = SearchToolkit()

results = toolkit.search_perplexity(
    query="AI safety research",
    max_results=5,
    max_tokens_per_page=512,
    country="US",
    search_recency_filter="week",                         # hour | day | week | month | year
    search_domain_filter=["arxiv.org", "-medium.com"],   # prefix with '-' to exclude
    search_language_filter=["en"],
)
```

You can also pass a list of queries for batched search, or use `extra_params` to forward any additional Search API field that isn't yet a first-class argument:

```python theme={null}
results = toolkit.search_perplexity(
    query=["NVIDIA earnings", "AMD earnings"],
    max_results=3,
    extra_params={
        "search_after_date_filter": "1/1/2026",
        "search_before_date_filter": "5/1/2026",
    },
)
```

## Response Shape

`search_perplexity` returns the raw Perplexity Search API response as a `Dict[str, Any]`. On success it contains a `results` list along with `id` and `server_time`:

```python theme={null}
{
    "id": "...",
    "server_time": "...",
    "results": [
        {
            "title": "...",
            "url": "...",
            "snippet": "...",
            "date": "...",          # may be present
            "last_updated": "...",  # may be present
        },
        # ...
    ],
}
```

On failure the response is a dictionary with an `error` key describing the issue (missing API key, HTTP error, or request exception).

## Links & Resources

<CardGroup>
  <Card title="CAMEL-AI Docs" icon="book" href="https://docs.camel-ai.org">
    Build multi-agent systems with CAMEL-AI.
  </Card>

  <Card title="Tool Source" icon="brand-github" href="https://github.com/camel-ai/camel/blob/master/camel/toolkits/search_toolkit.py">
    SearchToolkit.search\_perplexity implementation.
  </Card>

  <Card title="Search API Quickstart" icon="search" href="/docs/search/quickstart">
    Learn more about the underlying Perplexity Search API.
  </Card>

  <Card title="Example Script" icon="code" href="https://github.com/camel-ai/camel/blob/master/examples/toolkits/search_toolkit.py">
    End-to-end CAMEL example using Perplexity search.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [CAMEL-AI documentation](https://docs.camel-ai.org)
* Review our [FAQ](/docs/resources/faq)
