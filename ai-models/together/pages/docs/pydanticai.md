---
title: "PydanticAI"
source: https://docs.together.ai/docs/pydanticai
path: docs/pydanticai
---

Using PydanticAI with Together

PydanticAI is an agent framework created by the Pydantic team to simplify building production-grade generative AI applications. It brings the ergonomic design philosophy of FastAPI to AI agent development, offering a familiar and type-safe approach to working with language models.

## Installing libraries

<CodeGroup>
  ```shell Shell theme={null}
  pip install pydantic-ai
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

<CodeGroup>
  ```python Python theme={null}
  from pydantic_ai import Agent
  from pydantic_ai.models.openai import OpenAIModel
  from pydantic_ai.providers.openai import OpenAIProvider

  # Connect PydanticAI to LLMs on Together
  model = OpenAIModel(
      "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      provider=OpenAIProvider(
          base_url="https://api.together.ai/v1",
          api_key=os.environ.get("TOGETHER_API_KEY"),
      ),
  )

  # Setup the agent
  agent = Agent(
      model,
      system_prompt="Be concise, reply with one sentence.",
  )

  result = agent.run_sync('Where does "hello world" come from?')
  print(result.data)
  ```
</CodeGroup>

### Output

```
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
```

## Next Steps

<Info>
  ### PydanticAI - Together AI Notebook

  Learn more about building agents using PydanticAI with Together AI in our [notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/PydanticAI/PydanticAI_Agents.ipynb).
</Info>
