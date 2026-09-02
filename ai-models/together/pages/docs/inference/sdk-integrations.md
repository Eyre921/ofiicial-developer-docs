---
title: "Third-party integrations"
source: https://docs.together.ai/docs/inference/sdk-integrations
path: docs/inference/sdk-integrations
---

Use Together AI models through partner SDKs and integrations.

The Together AI API is [OpenAI-compatible](/docs/inference/openai-compatibility), so most third-party SDKs work by pointing them at `https://api.together.ai/v1` and supplying your [Together API key](/docs/api-keys-authentication). The integrations below ship dedicated Together support, with first-class clients, helpers, or providers.

For agent frameworks (CrewAI, LangGraph, DSPy, PydanticAI, AutoGen, Agno, Composio), see the dedicated pages under [Framework integrations](/docs/agent-integrations).

## Hugging Face

Use Together AI as a provider for [Hugging Face Inference](https://huggingface.co/docs/huggingface_hub/guides/inference) clients:

<CodeGroup>
  ```bash Python theme={null}
  pip install "huggingface_hub>=0.29.0"
  ```

  ```bash TypeScript theme={null}
  npm install @huggingface/inference
  ```
</CodeGroup>

<CodeGroup>
  ```python Python theme={null}
  from huggingface_hub import InferenceClient

  client = InferenceClient(
      provider="together",
      api_key="<your_api_key>",  # HF token or Together API key
  )

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-V4-Pro-0813",
      messages=[{"role": "user", "content": "What is the capital of France?"}],
      max_tokens=500,
  )

  print(completion.choices[0].message)
  ```

  ```typescript TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  const client = new HfInference("<your_api_key>");

  const chatCompletion = await client.chatCompletion({
    model: "deepseek-ai/DeepSeek-V4-Pro-0813",
    messages: [{ role: "user", content: "What is the capital of France?" }],
    provider: "together",
    max_tokens: 500,
  });

  console.log(chatCompletion.choices[0].message);
  ```
</CodeGroup>

See the [Together AI Hugging Face guide](https://docs.together.ai/docs/quickstart-using-hugging-face-inference) for more details.

## Vercel AI SDK

The [Vercel AI SDK](https://sdk.vercel.ai/) is a TypeScript library for building AI-powered applications. The `@ai-sdk/togetherai` provider gives you native access to Together AI models.

```bash Shell theme={null}
npm i ai @ai-sdk/togetherai
```

```typescript TypeScript theme={null}
import { togetherai } from "@ai-sdk/togetherai";
import { generateText } from "ai";

const { text } = await generateText({
  model: togetherai("moonshotai/Kimi-K3"),
  prompt: "Write a vegetarian lasagna recipe for 4 people.",
});

console.log(text);
```

See the [Together AI Vercel AI SDK guide](https://docs.together.ai/docs/using-together-with-vercels-ai-sdk) for details on streaming, tool use, and structured outputs.

## LangChain

[LangChain](https://www.langchain.com/) is a framework for building context-aware, reasoning applications powered by LLMs. The `langchain-together` package provides chat models and embeddings.

```bash Shell theme={null}
pip install --upgrade langchain-together
```

```python Python theme={null}
from langchain_together import ChatTogether

chat = ChatTogether(model="meta-llama/Llama-3.3-70B-Instruct-Turbo")

for chunk in chat.stream("Tell me fun things to do in NYC"):
    print(chunk.content, end="", flush=True)
```

For RAG patterns with LangChain plus Together embeddings, see [RAG integrations](/docs/inference/embeddings/rag) and the [LangChain provider docs](https://python.langchain.com/docs/integrations/providers/together/).

## LlamaIndex

[LlamaIndex](https://www.llamaindex.ai/) is a data framework for connecting custom data sources to LLMs. Together AI works with LlamaIndex through the `OpenAILike` LLM and dedicated embedding classes.

```bash Shell theme={null}
pip install llama-index
```

```python Python theme={null}
import os
from llama_index.llms import OpenAILike

llm = OpenAILike(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    api_base="https://api.together.ai/v1",
    api_key=os.environ["TOGETHER_API_KEY"],
    is_chat_model=True,
    is_function_calling_model=True,
    temperature=0.1,
)

response = llm.complete("Explain large language models in 500 words.")
print(response)
```

For RAG patterns, see [RAG integrations](/docs/inference/embeddings/rag), the [LlamaIndex Together LLM docs](https://docs.llamaindex.ai/en/stable/examples/llm/together/), and the [LlamaIndex Together embeddings docs](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/together/).

## Helicone

[Helicone](https://www.helicone.ai/) is an open-source LLM observability platform. Route Together requests through Helicone's gateway by overriding `base_url` and adding the auth header.

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together(
      api_key=os.environ["TOGETHER_API_KEY"],
      base_url="https://together.hconeai.com/v1",
      default_headers={
          "Helicone-Auth": f"Bearer {os.environ['HELICONE_API_KEY']}",
      },
  )

  stream = client.chat.completions.create(
      model="Qwen/Qwen3.5-9B",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      if chunk.choices:
          print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: "https://together.hconeai.com/v1",
    defaultHeaders: {
      "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
    },
  });

  const stream = await client.chat.completions.create({
    model: "Qwen/Qwen3.5-9B",
    messages: [
      { role: "user", content: "What are some fun things to do in New York?" },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
  }
  ```

  ```bash cURL theme={null}
  curl https://together.hconeai.com/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Qwen/Qwen3.5-9B",
      "messages": [
        {"role": "user", "content": "What are some fun things to do in New York?"}
      ],
      "stream": true
    }'
  ```
</CodeGroup>

## Agent frameworks

Each framework below has a dedicated guide with installation, model selection, and runnable examples:

* [CrewAI](/docs/crewai): Open-source orchestration for multi-agent workflows.
* [LangGraph](/docs/langgraph): Stateful, multi-actor applications built on LangChain.
* [DSPy](/docs/dspy): Modular AI systems written in code instead of prompt strings.
* [PydanticAI](/docs/pydanticai): Typed agent framework from the Pydantic team.
* [AutoGen (AG2)](/docs/autogen): Conversational multi-agent systems.
* [Agno](/docs/agno): Open-source library for multimodal agents.
* [Composio](/docs/composio): Tool-use platform for connecting agents to external services.

## Vector stores and RAG

For Pinecone, MongoDB, Pixeltable, and other vector-store integrations, see [RAG integrations](/docs/inference/embeddings/rag).
