---
title: "Perplexity with LiveKit Agents"
source: https://docs.perplexity.ai/docs/getting-started/integrations/livekit
path: docs/getting-started/integrations/livekit
---

Use Perplexity models as the LLM brain of a LiveKit voice agent.

## Overview

The `livekit-plugins-perplexity` package wraps Perplexity's OpenAI-compatible chat completions endpoint at `https://api.perplexity.ai` so it can be used as a drop-in LLM for [LiveKit Agents](https://docs.livekit.io/agents/).

<Info>
  **LiveKit Agents** is an open-source framework for building realtime voice and multimodal AI agents. The Perplexity plugin lets a voice agent answer with web-grounded, citation-backed responses. Learn more at [livekit.io](https://livekit.io).
</Info>

## Installation

```bash theme={null}
pip install "livekit-agents[perplexity]"
```

## API Key Setup

Set your Perplexity API key as an environment variable, or pass it directly to the constructor:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://console.perplexity.ai">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start

Use `perplexity.LLM` anywhere a LiveKit Agent expects an LLM:

```python theme={null}
from livekit.agents import Agent, AgentSession
from livekit.plugins import perplexity, openai, silero

session = AgentSession(
    llm=perplexity.LLM(model="sonar-pro"),
    stt=openai.STT(),
    tts=openai.TTS(),
    vad=silero.VAD.load(),
)

agent = Agent(
    instructions="You are a helpful voice assistant. Use web search to answer with up-to-date information.",
)

# Run the session inside your LiveKit room entrypoint
```

The plugin reuses the OpenAI plugin's chat completions transport with `base_url="https://api.perplexity.ai"` and forwards an `X-Pplx-Integration` attribution header on every outgoing request.

## Configuration

`perplexity.LLM` accepts the same options as the underlying OpenAI-compatible client:

```python theme={null}
from livekit.plugins import perplexity

llm = perplexity.LLM(
    model="sonar-pro",
    api_key="...",            # falls back to PERPLEXITY_API_KEY
    temperature=0.2,
    top_p=0.9,
    parallel_tool_calls=True,
)
```

## Available Models

The plugin works with any model exposed through the Perplexity Agent API. `sonar-pro` is the default. See the full list on our [models page](/docs/sonar/models).

## Links & Resources

<CardGroup>
  <Card title="LiveKit Agents Docs" icon="book" href="https://docs.livekit.io/agents/">
    Build realtime voice and multimodal agents with LiveKit.
  </Card>

  <Card title="Perplexity Plugin Source" icon="brand-github" href="https://github.com/livekit/agents/tree/main/livekit-plugins/livekit-plugins-perplexity">
    Plugin source in the livekit/agents monorepo.
  </Card>

  <Card title="PyPI Package" icon="brand-python" href="https://pypi.org/project/livekit-plugins-perplexity/">
    View on PyPI.
  </Card>

  <Card title="Agent API Quickstart" icon="bolt" href="/docs/agent-api/quickstart">
    Learn more about the OpenAI-compatible Perplexity Agent API.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [LiveKit Agents documentation](https://docs.livekit.io/agents/)
* Review our [FAQ](/docs/resources/faq)
