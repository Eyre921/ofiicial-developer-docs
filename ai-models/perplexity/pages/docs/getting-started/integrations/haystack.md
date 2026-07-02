---
title: "Perplexity with Haystack"
source: https://docs.perplexity.ai/docs/getting-started/integrations/haystack
path: docs/getting-started/integrations/haystack
---

Use Perplexity's Agent API, Embeddings API, and grounded Search API in Haystack pipelines.

## Overview

The `perplexity-haystack` package provides Haystack components for Perplexity's Agent API, Embeddings API, and grounded Search API, so you can build retrieval-augmented and agentic pipelines that combine chat, embeddings, and live web search.

<Info>
  **Haystack** is an open-source Python framework by [deepset](https://deepset.ai) for building production-ready LLM applications, including RAG pipelines and agentic workflows. Learn more at [haystack.deepset.ai](https://haystack.deepset.ai).
</Info>

The integration includes:

* **PerplexityChatGenerator** — Chat completions through the [Agent API](/docs/agent-api/quickstart) (OpenAI-compatible).
* **PerplexityTextEmbedder** and **PerplexityDocumentEmbedder** — Embeddings through the [Embeddings API](/docs/embeddings/quickstart).
* **PerplexityWebSearch** — Ranked, grounded web results through the [Search API](/docs/search/quickstart).

## Installation

<Tabs>
  <Tab title="pip">
    ```bash theme={null}
    pip install perplexity-haystack
    ```
  </Tab>

  <Tab title="uv">
    ```bash theme={null}
    uv add perplexity-haystack
    ```
  </Tab>
</Tabs>

## API Key Setup

Set your Perplexity API key as an environment variable:

```python theme={null}
import os

os.environ["PERPLEXITY_API_KEY"] = "your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start: Chat (Agent API)

`PerplexityChatGenerator` is powered by the Perplexity Agent API and defaults to `openai/gpt-5.4`.

```python theme={null}
import os

from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.perplexity import PerplexityChatGenerator

os.environ["PERPLEXITY_API_KEY"] = "your_api_key_here"

client = PerplexityChatGenerator()
response = client.run(
    messages=[ChatMessage.from_user("What are Agentic Pipelines? Be brief.")]
)

print(response["replies"])
```

### Selecting a Model

You can pick any of the supported Agent API models via the `model` parameter:

```python theme={null}
client = PerplexityChatGenerator(model="anthropic/claude-sonnet-4-6")
```

Supported models include `openai/gpt-5.4` (default), `openai/gpt-5.5`, `openai/gpt-4o`, `anthropic/claude-sonnet-4-6`, `xai/grok-4-1`, and `google/gemini-3-flash-preview`. See the [Agent API models page](/docs/agent-api/models) for the full list.

## Quick Start: Embeddings

Embed a single query with `PerplexityTextEmbedder`:

```python theme={null}
import os

from haystack_integrations.components.embedders.perplexity import PerplexityTextEmbedder

os.environ["PERPLEXITY_API_KEY"] = "your_api_key_here"

embedder = PerplexityTextEmbedder()
response = embedder.run(text="What is Haystack by deepset?")

print(response["embedding"])
```

Embed a list of documents with `PerplexityDocumentEmbedder`:

```python theme={null}
from haystack import Document
from haystack_integrations.components.embedders.perplexity import PerplexityDocumentEmbedder

docs = [Document(content="What is Haystack by deepset?")]
result = PerplexityDocumentEmbedder().run(documents=docs)

print(result["documents"][0].embedding)
```

Both embedders default to `pplx-embed-v1-0.6b`. The larger `pplx-embed-v1-4b` model is also available — set it via the `model` parameter.

## Quick Start: Web Search (Search API)

Use `PerplexityWebSearch` to get ranked, grounded web results inside a Haystack pipeline:

```python theme={null}
import os

from haystack.utils import Secret
from haystack_integrations.components.websearch.perplexity import PerplexityWebSearch

os.environ["PERPLEXITY_API_KEY"] = "your_api_key_here"

websearch = PerplexityWebSearch(
    api_key=Secret.from_env_var("PERPLEXITY_API_KEY"),
    top_k=5,
)
result = websearch.run(query="What is Haystack by deepset?")

documents = result["documents"]
links = result["links"]

print(documents)
print(links)
```

## Links & Resources

<CardGroup>
  <Card title="Haystack Integrations" icon="book" href="https://haystack.deepset.ai/integrations/perplexity">
    Catalog entry on haystack.deepset.ai
  </Card>

  <Card title="Source Code" icon="github" href="https://github.com/deepset-ai/haystack-core-integrations/tree/main/integrations/perplexity">
    perplexity-haystack on GitHub
  </Card>

  <Card title="PyPI Package" icon="brand-python" href="https://pypi.org/project/perplexity-haystack">
    View on PyPI
  </Card>

  <Card title="Haystack Docs" icon="book-open" href="https://docs.haystack.deepset.ai">
    Full Haystack documentation
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Check the [Haystack documentation](https://docs.haystack.deepset.ai)
* Open an issue at [haystack-core-integrations](https://github.com/deepset-ai/haystack-core-integrations/issues)
* Review our [FAQ](/docs/resources/faq)
