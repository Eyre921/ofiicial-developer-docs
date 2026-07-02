---
title: "Agno"
source: https://docs.together.ai/docs/agno
path: docs/agno
---

Using Agno with Together AI

Agno is an open-source library for creating multimodal agents. It supports interactions with text, images, audio, and video while remaining model-agnostic, allowing you to use any model in the Together AI library with our integration.

## Install libraries

```bash theme={null}
pip install -U agno duckduckgo-search
```

## Authentication

Set your `TOGETHER_API_KEY` environment variable.

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

Below is a simple agent with access to web search.

<CodeGroup>
  ```python Python theme={null}
  from agno.agent import Agent
  from agno.models.together import Together
  from agno.tools.duckduckgo import DuckDuckGoTools

  agent = Agent(
      model=Together(id="Qwen/Qwen3.5-9B"),
      tools=[DuckDuckGoTools()],
      markdown=True,
  )
  agent.print_response("What's happening in New York?", stream=True)
  ```
</CodeGroup>

## Next steps

<Info>
  ### Agno - Together AI Cookbook

  Explore our in-depth [Agno Cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Agno/Agents_Agno.ipynb)
</Info>
