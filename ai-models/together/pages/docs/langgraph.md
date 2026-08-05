---
title: "LangGraph"
source: https://docs.together.ai/docs/langgraph
path: docs/langgraph
---

Using LangGraph with Together AI

LangGraph is an OSS library for building stateful, multi-actor applications with LLMs, specifically designed for agent and multi-agent workflows. The framework supports critical agent architecture features including persistent memory across conversations and human-in-the-loop capabilities through checkpointed states.

## Installing libraries

<CodeGroup>
  ```shell Python theme={null}
    pip install -U langgraph langchain-together
  ```

  ```shell Typescript theme={null}
    pnpm add @langchain/langgraph @langchain/core  @langchain/community
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

In this simple example you augment an LLM with a calculator tool!

<CodeGroup>
  ```python Python theme={null}
  import os
  from langchain_together import ChatTogether

  llm = ChatTogether(
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      api_key=os.getenv("TOGETHER_API_KEY"),
  )


  # Define a tool
  def multiply(a: int, b: int) -> int:
      return a * b


  # Augment the LLM with tools
  llm_with_tools = llm.bind_tools([multiply])

  # Invoke the LLM with input that triggers the tool call
  msg = llm_with_tools.invoke("What is 2 times 3?")

  # Get the tool call
  msg.tool_calls
  ```

  ```typescript Typescript theme={null}
  import { ChatTogetherAI } from "@langchain/community/chat_models/togetherai";

  const llm = new ChatTogetherAI({
      model: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      apiKey: process.env.TOGETHER_API_KEY,
  });

  // Define a tool
  const multiply = {
      name: "multiply",
      description: "Multiply two numbers",
      schema: {
          type: "function",
          function: {
              name: "multiply",
              description: "Multiply two numbers",
              parameters: {
                  type: "object",
                  properties: {
                      a: { type: "number" },
                      b: { type: "number" },
                  },
                  required: ["a", "b"],
              },
          },
      },
  };

  // Augment the LLM with tools
  const llmWithTools = llm.bindTools([multiply]);

  // Invoke the LLM with input that triggers the tool call
  const msg = await llmWithTools.invoke("What is 2 times 3?");

  // Get the tool call
  console.log(msg.tool_calls);
  ```
</CodeGroup>

## Next steps

<Info>
  ### LangGraph - Together AI Notebook

  Learn more about building agents using LangGraph with Together AI in these notebooks:

  * [Agentic RAG Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/Agentic_RAG_LangGraph.ipynb)
  * [Planning Agent Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/LangGraph_Planning_Agent.ipynb)
</Info>
