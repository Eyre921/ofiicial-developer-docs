---
title: "Perplexity with Composio"
source: https://docs.perplexity.ai/docs/getting-started/integrations/composio
path: docs/getting-started/integrations/composio
---

Expose Perplexity's Chat Completions, Agent, Search, and Embeddings APIs as MCP tools or direct API actions for any AI agent framework via Composio.

## Overview

[Composio](https://composio.dev) is a universal tool gateway for AI agents. The Composio Perplexity toolkit exposes the full Perplexity API — Chat Completions, Agent, Search, Embeddings, and async variants — as tools that any agent framework can call through a single MCP URL or direct API integration.

<Info>
  **Composio** handles authentication, secure credential storage, OAuth flows, and tool routing for 1000+ apps. Learn more at [composio.dev](https://composio.dev).
</Info>

The toolkit ships these Perplexity actions:

* **Execute Agent** — `POST /v1/agent` (Agent API responses)
* **Create Chat Completion** — `POST /v1/sonar` (Sonar chat completions)
* **Create Async Chat Completion** — `POST /v1/async/sonar`
* **Get / List Async Chat Completions** — `GET /v1/async/sonar/{id}`, `GET /v1/async/sonar`
* **Perplexity Search (Raw Results)** — `POST /search`
* **Create Embeddings** — `POST /v1/embeddings`
* **Create Contextualized Embeddings** — `POST /v1/contextualizedembeddings`
* **List Models** — `GET /v1/models`

## Prerequisites

* A [Composio account](https://composio.dev) and API key
* A Perplexity API key

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Installation

```bash theme={null}
pip install composio
```

For agent-framework integrations, install your framework SDK alongside Composio (Composio supports Claude Agent SDK, OpenAI Agents SDK, LangChain, LlamaIndex, Mastra, Pydantic AI, AutoGen, CrewAI, Google ADK, and more).

## Quick Start: Tool Router (MCP)

The Tool Router exposes Perplexity as an MCP server your agent can connect to. This works with any MCP-compatible client (Claude Code, Cursor, OpenCode, etc.).

```python theme={null}
from composio import Composio

composio = Composio(api_key="your-composio-api-key")
session = composio.create(user_id="your-user-id")
url = session.mcp.url

print(f"MCP URL: {url}")
```

Wire that URL into your agent's MCP configuration:

```python theme={null}
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

options = ClaudeAgentOptions(
    permission_mode="bypassPermissions",
    mcp_servers={
        "tool_router": {
            "type": "http",
            "url": url,
            "headers": {"x-api-key": "your-composio-api-key"},
        }
    },
    system_prompt="You are a helpful assistant with access to Perplexity tools.",
    max_turns=10,
)

async def main():
    async with ClaudeSDKClient(options=options) as client:
        await client.query("Summarize the latest AI research papers")
        async for message in client.receive_response():
            if hasattr(message, "content"):
                for block in message.content:
                    if hasattr(block, "text"):
                        print(block.text)

asyncio.run(main())
```

## Quick Start: Direct API Actions

You can also execute Perplexity actions directly from Composio without an MCP layer:

```python theme={null}
from composio import Composio

composio = Composio(api_key="your-composio-api-key")

# Connect the user's Perplexity account once
composio.toolkits.authorize(
    user_id="your-user-id",
    toolkit="perplexityai",
)

# Run a Sonar chat completion
result = composio.actions.execute(
    user_id="your-user-id",
    action="PERPLEXITYAI_CREATE_CHAT_COMPLETION",
    params={
        "model": "sonar-pro",
        "messages": [
            {"role": "user", "content": "What are the latest fusion-energy headlines?"}
        ],
    },
)

print(result["data"]["choices"][0]["message"]["content"])
```

## Supported Agent Frameworks

Composio's Perplexity toolkit works with every agent framework Composio supports, including:

* ChatGPT, OpenAI Agents SDK, Codex
* Claude Agents SDK, Claude Code
* Cursor, VS Code, OpenCode
* Google ADK, LangChain, AI SDK, Mastra AI
* LlamaIndex, CrewAI, Pydantic AI, AutoGen

Each framework has a dedicated setup guide in the [Composio Perplexity toolkit](https://composio.dev/toolkits/perplexityai) page.

## Authentication

Composio stores your Perplexity API key securely and injects it into every request. You provide your key once during the toolkit authorization flow — either through the Composio dashboard or programmatically via `composio.toolkits.authorize(...)`. Composio handles token refresh, scope management, and request signing on every call.

## Links & Resources

<CardGroup>
  <Card title="Composio Perplexity Toolkit" icon="toolbox" href="https://composio.dev/toolkits/perplexityai">
    Full toolkit documentation with framework-specific guides.
  </Card>

  <Card title="Composio Docs" icon="book" href="https://docs.composio.dev">
    Composio platform documentation.
  </Card>

  <Card title="Perplexity API Reference" icon="code" href="/api-reference">
    Full Perplexity API reference.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Perplexity models.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [Composio documentation](https://docs.composio.dev)
* Review our [FAQ](/docs/resources/faq)
