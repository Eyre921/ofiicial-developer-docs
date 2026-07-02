---
title: "Perplexity with LiteLLM"
source: https://docs.perplexity.ai/docs/getting-started/integrations/litellm
path: docs/getting-started/integrations/litellm
---

Use Perplexity's Sonar models, Agent API, and presets through LiteLLM's unified completion interface — Python SDK and Proxy.

## Overview

[LiteLLM](https://litellm.ai) is a Python SDK and proxy server that gives you a single OpenAI-compatible interface to 100+ LLM providers. Both Perplexity's Sonar models and the [Agent API](/docs/agent-api/quickstart) (with third-party models like GPT-5, Claude, and Gemini routed through Perplexity) are first-class providers in LiteLLM.

<Info>
  **LiteLLM** lets you swap providers without rewriting code, run a self-hosted proxy that fronts every model behind one API key, and track spend, latency, and errors per provider. Learn more at [litellm.ai](https://litellm.ai).
</Info>

## Installation

```bash theme={null}
pip install litellm
```

## API Key Setup

LiteLLM uses two environment variables depending on which Perplexity endpoint you're calling:

```bash theme={null}
# For Sonar chat completions (litellm.completion)
export PERPLEXITYAI_API_KEY="your_api_key_here"

# For Agent API responses (litellm.responses)
export PERPLEXITY_API_KEY="your_api_key_here"
```

In practice, set both to the same key.

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Sonar Chat Completions

Call Perplexity's Sonar models through `litellm.completion` with the `perplexity/` model prefix:

```python theme={null}
from litellm import completion
import os

os.environ["PERPLEXITYAI_API_KEY"] = "your_api_key_here"

response = completion(
    model="perplexity/sonar-pro",
    messages=[
        {"role": "user", "content": "What are the latest fusion breakthroughs?"}
    ],
)

print(response.choices[0].message.content)
```

### Streaming

```python theme={null}
from litellm import completion

response = completion(
    model="perplexity/sonar-pro",
    messages=[{"role": "user", "content": "Explain quantum computing."}],
    stream=True,
)

for chunk in response:
    print(chunk)
```

### Reasoning Effort

For reasoning-capable Sonar models, pass `reasoning_effort` to control depth:

```python theme={null}
response = completion(
    model="perplexity/sonar-reasoning",
    messages=[{"role": "user", "content": "Walk through your reasoning."}],
    reasoning_effort="high",  # "low" | "medium" | "high"
)
```

### Supported Sonar Models

| Model                 | LiteLLM Identifier               |
| --------------------- | -------------------------------- |
| `sonar`               | `perplexity/sonar`               |
| `sonar-pro`           | `perplexity/sonar-pro`           |
| `sonar-reasoning`     | `perplexity/sonar-reasoning`     |
| `sonar-reasoning-pro` | `perplexity/sonar-reasoning-pro` |
| `sonar-deep-research` | `perplexity/sonar-deep-research` |

## Agent API

Use `litellm.responses` to call the [Agent API](/docs/agent-api/quickstart), which routes through Perplexity to third-party models with tool orchestration and presets.

### Presets

```python theme={null}
from litellm import responses
import os

os.environ["PERPLEXITY_API_KEY"] = "your_api_key_here"

response = responses(
    model="perplexity/preset/pro-search",
    input="What are the latest developments in AI?",
    custom_llm_provider="perplexity",
)

print(response.output)
```

Available presets: `fast-search`, `pro-search`, `deep-research`, `advanced-deep-research`.

### Tool Use (`web_search` and `fetch_url`)

```python theme={null}
from litellm import responses

response = responses(
    model="perplexity/openai/gpt-5.2",
    input="Research quantum computing breakthroughs and cite sources.",
    custom_llm_provider="perplexity",
    tools=[
        {"type": "web_search"},
        {"type": "fetch_url"},
    ],
    instructions="Use web_search and fetch_url to gather citations.",
    max_output_tokens=1000,
    temperature=0.7,
)

print(response.output)
```

### Structured Outputs

```python theme={null}
from litellm import responses

response = responses(
    model="perplexity/preset/pro-search",
    input="Extract key facts about the Eiffel Tower.",
    custom_llm_provider="perplexity",
    text={
        "format": {
            "type": "json_schema",
            "name": "facts",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "height_meters": {"type": "number"},
                    "year_built": {"type": "integer"},
                },
                "required": ["name", "height_meters", "year_built"],
            },
            "strict": True,
        }
    },
)
```

### Supported Third-Party Models via Agent API

| Provider   | Models                                                                                                                                                                                                                                              |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI     | `perplexity/openai/gpt-5.5`, `perplexity/openai/gpt-5.4`, `perplexity/openai/gpt-5.4-mini`, `perplexity/openai/gpt-5.2`, `perplexity/openai/gpt-5.1`, `perplexity/openai/gpt-5-mini`                                                                |
| Anthropic  | `perplexity/anthropic/claude-opus-4-7`, `perplexity/anthropic/claude-opus-4-6`, `perplexity/anthropic/claude-sonnet-4-6`, `perplexity/anthropic/claude-opus-4-5`, `perplexity/anthropic/claude-sonnet-4-5`, `perplexity/anthropic/claude-haiku-4-5` |
| Google     | `perplexity/google/gemini-3.1-pro-preview`, `perplexity/google/gemini-3-flash-preview`, `perplexity/google/gemini-3.1-flash-lite`                                                                                                                   |
| xAI        | `perplexity/xai/grok-4.20-non-reasoning`                                                                                                                                                                                                            |
| Perplexity | `perplexity/perplexity/sonar`                                                                                                                                                                                                                       |

See the [Agent API model list](/docs/agent-api/models) for the canonical, up-to-date catalogue.

## LiteLLM Proxy

Run LiteLLM as a self-hosted proxy that fronts Perplexity (and any other provider) behind a single OpenAI-compatible endpoint.

### config.yaml

```yaml theme={null}
model_list:
  - model_name: perplexity-sonar-reasoning
    litellm_params:
      model: perplexity/sonar-reasoning
      api_key: os.environ/PERPLEXITYAI_API_KEY

  - model_name: perplexity-pro-search
    litellm_params:
      model: perplexity/preset/pro-search
      api_key: os.environ/PERPLEXITY_API_KEY
```

### Start the Proxy

```bash theme={null}
litellm --config /path/to/config.yaml
```

### Call the Proxy

```bash theme={null}
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer anything" \
  -d '{
    "model": "perplexity-sonar-reasoning",
    "messages": [{"role": "user", "content": "Who won the World Cup in 2022?"}],
    "reasoning_effort": "high"
  }'
```

## Links & Resources

<CardGroup>
  <Card title="LiteLLM Perplexity Docs" icon="book" href="https://docs.litellm.ai/docs/providers/perplexity">
    Official LiteLLM Perplexity provider docs.
  </Card>

  <Card title="LiteLLM Docs" icon="globe" href="https://docs.litellm.ai">
    Full LiteLLM documentation.
  </Card>

  <Card title="Perplexity Agent API" icon="robot" href="/docs/agent-api/quickstart">
    Agent API reference and presets.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Sonar and Agent API models.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [LiteLLM documentation](https://docs.litellm.ai)
* Review our [FAQ](/docs/resources/faq)
