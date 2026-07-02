---
title: "GLM-5.2 quickstart"
source: https://docs.together.ai/docs/glm-5.2-quickstart
path: docs/glm-5.2-quickstart
---

Get the most out of GLM-5.2 for long-horizon coding and agentic tasks.

GLM-5.2 is Zhipu AI's flagship mixture-of-experts (MoE) model, built for long-horizon coding and agentic work. It holds project-scale context across many steps and completes multi-stage tasks end to end, leading open-source models on benchmarks like FrontierSWE, Terminal-Bench, and SWE-bench Pro.

On Together AI, GLM-5.2 runs in FP4 with a 262K-token context window and up to 128K output tokens. It supports streaming, function calling, structured outputs, and adjustable reasoning effort. Thinking is enabled by default, so you'll receive both reasoning and content tokens.

The model ID is `zai-org/GLM-5.2`. Pricing is \$1.40 per 1M input tokens, \$4.40 per 1M output tokens, and \$0.26 per 1M cached input tokens.

## How to use GLM-5.2

Get started with this model in a few lines of code. Since thinking is on by default, stream the response and handle both the `reasoning` and `content` fields on each delta.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="zai-org/GLM-5.2",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      temperature=1.0,
      top_p=0.95,
      stream=True,
  )

  for chunk in stream:
      if not chunk.choices:
          continue
      delta = chunk.choices[0].delta
      # Stream reasoning and content tokens as they arrive
      print(
          getattr(delta, "reasoning", None) or delta.content or "",
          end="",
          flush=True,
      )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "zai-org/GLM-5.2",
    messages: [
      {
        role: "user",
        content: "What are some fun things to do in New York?",
      },
    ],
    temperature: 1.0,
    top_p: 0.95,
    stream: true,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta;
    // Stream reasoning and content tokens as they arrive
    process.stdout.write(delta?.reasoning || delta?.content || "");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
          "model": "zai-org/GLM-5.2",
          "messages": [
            {"role": "user", "content": "What are some fun things to do in New York?"}
          ],
          "temperature": 1.0,
          "top_p": 0.95,
          "stream": true
       }'
  ```
</CodeGroup>

## Reasoning effort

GLM-5.2 accepts two effort levels through the `reasoning_effort` parameter when thinking is enabled:

* `"high"`: enhanced reasoning. Use for most coding and reasoning tasks.
* `"max"`: deep reasoning, the default. Use for the hardest planning, architecture, and multi-step agentic problems. Set `max_tokens` generously, since `"max"` mode can produce long chains of thought.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="zai-org/GLM-5.2",
      messages=[
          {
              "role": "user",
              "content": "Design a three-tier microservice architecture for a ticketing system.",
          }
      ],
      reasoning_effort="max",
      temperature=1.0,
      top_p=0.95,
      max_tokens=65536,
      stream=True,
  )

  for chunk in stream:
      if not chunk.choices:
          continue
      delta = chunk.choices[0].delta
      # Stream reasoning and content tokens as they arrive
      print(
          getattr(delta, "reasoning", None) or delta.content or "",
          end="",
          flush=True,
      )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "zai-org/GLM-5.2",
    messages: [
      {
        role: "user",
        content:
          "Design a three-tier microservice architecture for a ticketing system.",
      },
    ],
    reasoning_effort: "max",
    temperature: 1.0,
    top_p: 0.95,
    max_tokens: 65536,
    stream: true,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta;
    // Stream reasoning and content tokens as they arrive
    process.stdout.write(delta?.reasoning || delta?.content || "");
  }
  ```
</CodeGroup>

For broader guidance on reasoning controls and prompting, see [Reasoning](/docs/inference/chat/reasoning).

## Thinking modes

GLM-5.2 has thinking enabled by default and supports multiple thinking modes for different scenarios:

* **Interleaved thinking** (default): the model thinks between tool calls and after receiving tool results, interpreting each tool output before deciding what to do next.
* **Preserved thinking**: the model retains reasoning content from previous assistant turns in the context, improving reasoning continuity and cache hit rates. Ideal for coding agents and agentic workflows.
* **Turn-level thinking**: control reasoning on a per-turn basis within the same session. Enable thinking for hard turns, disable it for simple ones.

### Recommended thinking mode by use case

| Scenario                                 | Mode                               | Rationale                                      |
| ---------------------------------------- | ---------------------------------- | ---------------------------------------------- |
| General chat                             | Interleaved thinking (default)     | Step-by-step reasoning between tool calls.     |
| Coding agents (e.g., Claude Code, Codex) | Interleaved and preserved thinking | Retains reasoning across turns for continuity. |
| Simple factual queries                   | Thinking disabled                  | Faster responses, lower cost.                  |

### Disabling thinking

For lightweight tasks where you don't need the model to reason, pass `reasoning={"enabled": False}`. This disables the chain of thought and returns only the final answer.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="zai-org/GLM-5.2",
      messages=[
          {
              "role": "user",
              "content": "What is the capital of France?",
          }
      ],
      reasoning={"enabled": False},
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "zai-org/GLM-5.2",
    messages: [
      {
        role: "user",
        content: "What is the capital of France?",
      },
    ],
    reasoning: { enabled: false },
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

### Preserved thinking

For agentic workflows, enable preserved thinking so the model retains reasoning from previous turns. Set `"clear_thinking": false` in `chat_template_kwargs` to keep reasoning content in context across turns.

```python Python theme={null}
from together import Together

client = Together()

response = client.chat.completions.create(
    model="zai-org/GLM-5.2",
    messages=[
        {
            "role": "user",
            "content": "Refactor this module without changing its public API.",
        }
    ],
    chat_template_kwargs={
        "clear_thinking": False,  # Preserved Thinking
    },
)

print(response.choices[0].message.content)
```

<Info>
  When using preserved thinking, all consecutive `reasoning` blocks must **exactly match the original sequence** generated by the model. Don't reorder or edit these blocks, otherwise performance may degrade and cache hit rates will be affected.
</Info>

## Function calling and streaming tool calls

GLM-5.2 supports tool calling with reasoning interleaved between each step. Define tools in the standard OpenAI-compatible schema and pass them via `tools`.

To stream tool calls, set `stream=True`. The model emits tool call parameters incrementally, so concatenate the `arguments` fragments from each delta to rebuild the full call. Together does not use a separate `tool_stream` parameter.

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current weather conditions for a city.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City name, e.g. Beijing, Shanghai.",
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
                  "required": ["location"],
              },
          },
      }
  ]

  stream = client.chat.completions.create(
      model="zai-org/GLM-5.2",
      messages=[{"role": "user", "content": "What's the weather in Beijing?"}],
      tools=tools,
      stream=True,
  )

  final_tool_calls = {}

  for chunk in stream:
      if not chunk.choices:
          continue
      delta = chunk.choices[0].delta

      # Reassemble streamed tool calls by index
      if delta.tool_calls:
          for tool_call in delta.tool_calls:
              idx = tool_call.index
              if idx not in final_tool_calls:
                  final_tool_calls[idx] = tool_call
              else:
                  final_tool_calls[
                      idx
                  ].function.arguments += tool_call.function.arguments

  for idx, tool_call in final_tool_calls.items():
      print(f"{tool_call.function.name}: {tool_call.function.arguments}")
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const tools = [
    {
      type: "function" as const,
      function: {
        name: "get_weather",
        description: "Get current weather conditions for a city.",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "City name, e.g. Beijing, Shanghai.",
            },
            unit: { type: "string", enum: ["celsius", "fahrenheit"] },
          },
          required: ["location"],
        },
      },
    },
  ];

  const stream = await together.chat.completions.create({
    model: "zai-org/GLM-5.2",
    messages: [{ role: "user", content: "What's the weather in Beijing?" }],
    tools,
    stream: true,
  });

  const finalToolCalls: Record<number, { name: string; arguments: string }> = {};

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta;
    if (!delta?.tool_calls) continue;

    for (const toolCall of delta.tool_calls) {
      const idx = toolCall.index;
      if (!(idx in finalToolCalls)) {
        finalToolCalls[idx] = {
          name: toolCall.function?.name ?? "",
          arguments: toolCall.function?.arguments ?? "",
        };
      } else {
        finalToolCalls[idx].arguments += toolCall.function?.arguments ?? "";
      }
    }
  }

  for (const idx in finalToolCalls) {
    const call = finalToolCalls[idx];
    console.log(`${call.name}: ${call.arguments}`);
  }
  ```
</CodeGroup>

## Structured outputs

GLM-5.2 supports structured outputs. Pass a JSON schema through `response_format` to constrain the response to a fixed shape.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="zai-org/GLM-5.2",
      messages=[
          {
              "role": "user",
              "content": "Extract the person: John is 30 years old.",
          }
      ],
      response_format={
          "type": "json_schema",
          "json_schema": {
              "name": "person",
              "schema": {
                  "type": "object",
                  "properties": {
                      "name": {"type": "string"},
                      "age": {"type": "integer"},
                  },
                  "required": ["name", "age"],
              },
          },
      },
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "zai-org/GLM-5.2",
    messages: [
      { role: "user", content: "Extract the person: John is 30 years old." },
    ],
    response_format: {
      type: "json_schema",
      json_schema: {
        name: "person",
        schema: {
          type: "object",
          properties: {
            name: { type: "string" },
            age: { type: "integer" },
          },
          required: ["name", "age"],
        },
      },
    },
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Use cases

GLM-5.2 is strongest in scenarios that require deep reasoning and autonomous, multi-step execution:

* **Project-level codebase work:** Hold an entire codebase in a single reasoning workflow, retaining module boundaries, API contracts, and architectural constraints.
* **Long-horizon refactoring:** Run cross-file, multi-step engineering tasks end to end, from planning through verification.
* **Production-grade standards:** Follow team engineering standards (lint rules, build commands, commit conventions) consistently across long sessions.
* **Coding and debugging:** Solve complex software engineering tasks, generate patches, and debug intricate issues across large codebases.
* **Front-end and design:** Build polished UIs from a prompt or mockup, producing clean component code and well-structured layouts with strong attention to visual detail.
* **Tool orchestration:** Chain multiple tool calls with reasoning between steps, making finer-grained decisions based on intermediate results.
* **Research reproduction:** Turn a paper's architecture, loss functions, and data pipelines into a runnable project with consistency across files.

## Usage tips

| Tip                                             | Rationale                                                                                                                           |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Temperature = 1.0, top\_p = 0.95**            | Recommended defaults. Adjust only one of the two, not both at once.                                                                 |
| **Think in goals, not steps**                   | GLM-5.2 is agentic. Give high-level objectives and let it orchestrate sub-tasks and tool calls.                                     |
| **Use `reasoning_effort="max"` for hard tasks** | Deep reasoning for complex planning, architecture, and multi-step agentic problems.                                                 |
| **Use preserved thinking for agents**           | Set `"clear_thinking": false` in `chat_template_kwargs` for coding agents to maintain reasoning continuity.                         |
| **Return reasoning content faithfully**         | When using preserved thinking, return the unmodified `reasoning` from previous turns back to the API.                               |
| **Use turn-level thinking to save cost**        | Disable thinking on simple turns and enable it on complex turns within the same session.                                            |
| **Set generous max tokens**                     | GLM-5.2 supports up to 128K output tokens. Raise `max_tokens` for deep reasoning, and keep it lower for short agentic turns.        |
| **State constraints explicitly**                | For engineering tasks, spell out hard constraints (no new dependencies, no API changes, run the tests) so the model holds the line. |
