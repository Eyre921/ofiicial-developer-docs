---
title: "Perplexity with Agno"
source: https://docs.perplexity.ai/docs/getting-started/integrations/agno
path: docs/getting-started/integrations/agno
---

Use Perplexity's web-grounded models inside Agno agents and teams.

## Overview

[Agno](https://docs.agno.com) is an open-source Python framework for building agents, teams, and workflows with first-class support for 40+ model providers. Agno ships a native `Perplexity` model class so you can drop Perplexity's web-grounded Sonar models into any Agno `Agent` with a single import.

<Info>
  **Agno** provides a unified `Agent` abstraction, a tools system, and a multi-agent team/workflow runtime. Learn more at [agno.com](https://agno.com).
</Info>

## Installation

```bash theme={null}
pip install agno openai
```

The `Perplexity` model extends Agno's OpenAI-compatible interface, so the `openai` SDK is required as a transitive dependency.

## API Key Setup

Set your Perplexity API key as an environment variable:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Quick Start

```python theme={null}
from agno.agent import Agent
from agno.models.perplexity import Perplexity

agent = Agent(
    model=Perplexity(id="sonar-pro"),
    markdown=True,
)

agent.print_response("What launched at the latest Perplexity event?")
```

The default model is `sonar`. Pass any [Perplexity model id](/docs/sonar/models) via the `id` parameter — `sonar`, `sonar-pro`, `sonar-reasoning`, `sonar-reasoning-pro`, or `sonar-deep-research`.

## Parameters

The `Perplexity` model accepts the standard OpenAI parameters plus a few Perplexity-specific options:

| Parameter               | Type              | Default                        | Description                                        |
| ----------------------- | ----------------- | ------------------------------ | -------------------------------------------------- |
| `id`                    | `str`             | `"sonar"`                      | Perplexity model id                                |
| `api_key`               | `Optional[str]`   | `None`                         | Falls back to `PERPLEXITY_API_KEY`                 |
| `base_url`              | `str`             | `"https://api.perplexity.ai/"` | API base URL                                       |
| `max_tokens`            | `int`             | `1024`                         | Maximum tokens to generate                         |
| `top_k`                 | `Optional[float]` | `None`                         | Top-K sampling                                     |
| `retries`               | `int`             | `0`                            | Retry attempts before raising `ModelProviderError` |
| `delay_between_retries` | `int`             | `1`                            | Seconds between retries                            |
| `exponential_backoff`   | `bool`            | `False`                        | Double the delay on each retry                     |

All OpenAI-compatible parameters (`temperature`, `top_p`, `frequency_penalty`, etc.) are also supported.

## Structured Output

```python theme={null}
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.perplexity import Perplexity

class Summary(BaseModel):
    headline: str
    bullets: list[str]

agent = Agent(
    model=Perplexity(id="sonar-pro"),
    response_model=Summary,
)

result = agent.run("Summarize this week's top AI research papers.")
print(result.content.headline)
for bullet in result.content.bullets:
    print(f"- {bullet}")
```

## Streaming

```python theme={null}
from agno.agent import Agent
from agno.models.perplexity import Perplexity

agent = Agent(model=Perplexity(id="sonar"))

for chunk in agent.run("Explain quantum entanglement", stream=True):
    print(chunk.content, end="", flush=True)
```

## Notes on Tool Calling

Perplexity models support tool calling through Agno, but Sonar models do not natively expose function-calling in the same first-class way as some other providers. Tool use through `Perplexity` may be less reliable than with `OpenAIChat` or `Claude`. For agent workflows that need rich tool orchestration on top of Perplexity-grounded answers, consider routing through the [Agent API](/docs/agent-api/quickstart) with `web_search` and `fetch_url` tools.

## Links & Resources

<CardGroup>
  <Card title="Agno Perplexity Docs" icon="book" href="https://docs.agno.com/models/providers/native/perplexity/overview">
    Official Agno Perplexity provider documentation.
  </Card>

  <Card title="Agno API Reference" icon="code" href="https://docs.agno.com/reference/models/perplexity">
    Full parameter reference for the `Perplexity` model.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Perplexity models and capabilities.
  </Card>

  <Card title="Agno Docs" icon="globe" href="https://docs.agno.com">
    Learn more about agents, teams, and workflows in Agno.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [Agno documentation](https://docs.agno.com)
* Review our [FAQ](/docs/resources/faq)
