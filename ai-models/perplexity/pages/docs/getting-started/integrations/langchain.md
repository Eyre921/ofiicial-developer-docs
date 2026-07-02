---
title: "Perplexity with LangChain"
source: https://docs.perplexity.ai/docs/getting-started/integrations/langchain
path: docs/getting-started/integrations/langchain
---

Use Perplexity's chat models and search tool in your LangChain applications (Python and JavaScript).

## Overview

LangChain provides first-class integrations for Perplexity in both Python (`langchain-perplexity`) and JavaScript/TypeScript (`@langchain/community`). Both packages let you build LLM applications with real-time web search, citations, and Perplexity's Pro Search reasoning.

<Info>
  **LangChain** is a popular Python framework for building applications powered by large language models. It provides composable components for chains, agents, and retrieval-augmented generation (RAG). Learn more at [langchain.com](https://www.langchain.com).
</Info>

The integration includes:

* **ChatPerplexity** - Chat model with Pro Search, streaming, and search controls
* **PerplexitySearchRetriever** - Retriever for RAG applications
* **PerplexitySearchResults** - Tool for LangChain agents

## Installation

<Tabs>
  <Tab title="pip">
    ```bash theme={null}
    pip install langchain-perplexity
    ```
  </Tab>

  <Tab title="uv">
    ```bash theme={null}
    uv add langchain-perplexity
    ```
  </Tab>
</Tabs>

## API Key Setup

Set your Perplexity API key as an environment variable:

```python theme={null}
import os

os.environ["PERPLEXITY_API_KEY"] = "your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Quick Start: Chat Models

Use `ChatPerplexity` for conversational AI with web search:

```python theme={null}
from langchain_perplexity import ChatPerplexity

chat = ChatPerplexity(model="sonar")

response = chat.invoke("What breakthroughs in fusion energy have been announced this year?")
print(response.content)
```

### Pro Search

Enable multi-step reasoning with Pro Search:

```python theme={null}
from langchain_perplexity import ChatPerplexity, WebSearchOptions

chat = ChatPerplexity(
    model="sonar-pro",
    web_search_options=WebSearchOptions(search_type="pro")
)

response = chat.invoke("How does the electoral college work?")

# Access reasoning steps
if reasoning := response.additional_kwargs.get("reasoning_steps"):
    for step in reasoning:
        print(f"Thought: {step['thought']}")
```

### Search Controls

Filter search results by domain, recency, or date:

```python theme={null}
chat = ChatPerplexity(
    model="sonar",
    search_domain_filter=["wikipedia.org", "nature.com"],
    search_recency_filter="month",
    return_images=True
)

response = chat.invoke("Solar system planets")

# Access citations and images
print("Citations:", response.additional_kwargs.get("citations", []))
print("Images:", response.additional_kwargs.get("images", []))
```

### Streaming

```python theme={null}
for chunk in chat.stream("Explain quantum computing"):
    print(chunk.content, end="", flush=True)
```

## Quick Start: Retriever

Use `PerplexitySearchRetriever` for RAG applications:

```python theme={null}
from langchain_perplexity import PerplexitySearchRetriever

retriever = PerplexitySearchRetriever(k=5)

docs = retriever.invoke("What is nuclear fusion?")

for doc in docs:
    print(f"Title: {doc.metadata['title']}")
    print(f"URL: {doc.metadata['url']}")
    print(f"Content: {doc.page_content[:200]}...")
    print("---")
```

### RAG Chain Example

```python theme={null}
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_perplexity import ChatPerplexity, PerplexitySearchRetriever

llm = ChatPerplexity(model="sonar")
retriever = PerplexitySearchRetriever(k=3)

template = """Answer based on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

answer = rag_chain.invoke("What is the current status of ITER?")
print(answer)
```

## Quick Start: Tool

Use `PerplexitySearchResults` with LangChain agents:

```python theme={null}
from langchain_perplexity import PerplexitySearchResults

tool = PerplexitySearchResults()

results = tool.invoke("LangChain framework")

for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['snippet'][:100]}...")
    print("---")
```

### Agent Example

```python theme={null}
from langchain.chat_models import init_chat_model
from langchain_perplexity import PerplexitySearchResults
from langgraph.prebuilt import create_react_agent

model = init_chat_model(model="gpt-4o", model_provider="openai")
search_tool = PerplexitySearchResults()

agent = create_react_agent(model, [search_tool])

for step in agent.stream(
    {"messages": [("user", "What are the latest LangChain releases?")]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
```

## JavaScript / TypeScript

The JavaScript integration ships in the [`@langchain/community`](https://www.npmjs.com/package/@langchain/community) package as `ChatPerplexity`. It is an OpenAI-compatible chat model that talks to `https://api.perplexity.ai`.

### Installation

<Tabs>
  <Tab title="npm">
    ```bash theme={null}
    npm install @langchain/community @langchain/core
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash theme={null}
    pnpm add @langchain/community @langchain/core
    ```
  </Tab>

  <Tab title="yarn">
    ```bash theme={null}
    yarn add @langchain/community @langchain/core
    ```
  </Tab>
</Tabs>

### API Key Setup

Set `PERPLEXITY_API_KEY` in your environment, or pass `apiKey` directly to the constructor:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

### Quick Start

```ts theme={null}
import { ChatPerplexity } from "@langchain/community/chat_models/perplexity";

const llm = new ChatPerplexity({
  model: "sonar",
  temperature: 0,
  maxRetries: 2,
});

const aiMsg = await llm.invoke([
  {
    role: "system",
    content: "You are a helpful assistant that answers with web-grounded citations.",
  },
  { role: "user", content: "What breakthroughs in fusion energy were announced this year?" },
]);

console.log(aiMsg.content);

// Citations and other metadata
console.log(aiMsg.additional_kwargs.citations);
```

### Streaming

```ts theme={null}
const stream = await llm.stream("Explain quantum computing in two paragraphs.");
for await (const chunk of stream) {
  process.stdout.write(chunk.content as string);
}
```

### Chaining with Prompts

```ts theme={null}
import { ChatPromptTemplate } from "@langchain/core/prompts";

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "You translate English into {language}."],
  ["human", "{input}"],
]);

const chain = prompt.pipe(llm);
const res = await chain.invoke({
  language: "French",
  input: "I love programming.",
});
console.log(res.content);
```

See the [LangChain JS Perplexity docs](https://docs.langchain.com/oss/javascript/integrations/chat/perplexity) for the full API surface.

## Available Models

The integration supports all Perplexity models:

| Model                 | Description                               |
| --------------------- | ----------------------------------------- |
| `sonar`               | Fast, cost-effective search model         |
| `sonar-pro`           | Advanced model with Pro Search support    |
| `sonar-reasoning-pro` | Advanced reasoning capabilities           |
| `sonar-deep-research` | Deep research with comprehensive analysis |

See the full list of models on our [models page](/docs/sonar/models).

## Links & Resources

<CardGroup>
  <Card title="LangChain Docs" icon="book" href="https://docs.langchain.com/oss/python/integrations/providers/perplexity">
    Full LangChain integration documentation
  </Card>

  <Card title="ChatPerplexity" icon="message" href="https://docs.langchain.com/oss/python/integrations/chat/perplexity">
    Detailed chat model documentation
  </Card>

  <Card title="Retriever Docs" icon="search" href="https://docs.langchain.com/oss/python/integrations/retrievers/perplexity">
    PerplexitySearchRetriever documentation
  </Card>

  <Card title="Tool Docs" icon="wrench" href="https://docs.langchain.com/oss/python/integrations/tools/perplexity">
    PerplexitySearchResults documentation
  </Card>

  <Card title="PyPI Package" icon="brand-python" href="https://pypi.org/project/langchain-perplexity/">
    View on PyPI
  </Card>

  <Card title="API Reference" icon="code-circle" href="https://python.langchain.com/api_reference/perplexity/">
    LangChain API reference
  </Card>

  <Card title="LangChain JS Docs" icon="js" href="https://docs.langchain.com/oss/javascript/integrations/chat/perplexity">
    ChatPerplexity for JavaScript / TypeScript
  </Card>

  <Card title="npm Package" icon="npm" href="https://www.npmjs.com/package/@langchain/community">
    @langchain/community on npm
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Check the [LangChain documentation](https://docs.langchain.com)
* Review our [FAQ](/docs/resources/faq)
