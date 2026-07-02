---
title: "Kimi K2 Thinking quickstart"
source: https://docs.together.ai/docs/kimi-k2-thinking-quickstart
path: docs/kimi-k2-thinking-quickstart
---

How to get the most out of reasoning models like Kimi K2 Thinking.

<Tip>
  Kimi K2 Thinking has been deprecated. We recommend using [Kimi K2.6](/docs/kimi-k2.6-quickstart) with thinking mode enabled instead for reasoning tasks.
</Tip>

Kimi K2 Thinking is a state-of-the-art reasoning model developed by Moonshot AI. It's a 1 trillion total parameter model (32B activated) that represents the latest, most capable version of open-source thinking models. Built on the foundation of Kimi K2, it's designed as a thinking agent that reasons step-by-step while dynamically invoking tools.

The model sets a new state-of-the-art on benchmarks like Humanity's Last Exam (HLE), BrowseComp, and others by dramatically scaling multi-step reasoning depth and maintaining stable tool-use across 200–300 sequential calls. Trained on 15.5 trillion tokens with a 256k context window, it excels in complex reasoning tasks, agentic workflows, coding, and tool use.

Unlike standard models, Kimi K2 Thinking outputs both a `reasoning` field (containing its chain-of-thought process) and a `content` field (containing the final answer), allowing you to see how it thinks through problems. In this quick guide, we'll go over the main use cases for Kimi K2 Thinking, how to get started with it, when to use it, and prompting tips for getting the most out of this incredible reasoning model.

## How to use Kimi K2 Thinking

Get started with this model in just a few lines of code! The model ID is `moonshotai/Kimi-K2-Thinking` and the pricing is \$1.20 per 1M input tokens and \$4.00 per 1M output tokens.

Since this is a reasoning model that produces both reasoning tokens and content tokens, you'll want to handle both fields in the streaming response:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  stream = client.chat.completions.create(
      model="moonshotai/Kimi-K2-Thinking",
      messages=[
          {
              "role": "user",
              "content": "Which number is bigger, 9.11 or 9.9? Think carefully.",
          }
      ],
      stream=True,
      max_tokens=500,
  )

  for chunk in stream:
      if chunk.choices:
          delta = chunk.choices[0].delta

          # Show reasoning tokens if present
          if hasattr(delta, "reasoning") and delta.reasoning:
              print(delta.reasoning, end="", flush=True)

          # Show content tokens if present
          if hasattr(delta, "content") and delta.content:
              print(delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai"
  import type { ChatCompletionChunk } from "together-ai/resources/chat/completions"

  const together = new Together()

  const stream = await together.chat.completions.stream({
    model: "moonshotai/Kimi-K2-Thinking",
    messages: [
      { role: "user", content: "What are some fun things to do in New York?" },
    ],
    max_tokens: 500,
  } as any)

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta as ChatCompletionChunk.Choice.Delta & {
      reasoning?: string
    }

    // Show reasoning tokens if present
    if (delta?.reasoning) process.stdout.write(delta.reasoning)

    // Show content tokens if present
    if (delta?.content) process.stdout.write(delta.content)
  }
  ```
</CodeGroup>

## Use cases

Kimi K2 Thinking excels in scenarios requiring deep reasoning, strategic thinking, and complex problem-solving:

* **Complex Reasoning Tasks**: Tackle advanced mathematical problems (AIME25, HMMT25, IMO-AnswerBench), scientific reasoning (GPQA), and logic puzzles that require multi-step analysis
* **Agentic Search & Research**: Automate research workflows using tools and APIs, with stable performance across 200–300 sequential tool invocations (BrowseComp, Seal-0, FinSearchComp)
* **Coding with Deep Analysis**: Solve complex software engineering tasks (SWE-bench, Multi-SWE-bench) that require understanding large codebases, generating patches, and debugging intricate issues
* **Long-Horizon Agentic Workflows**: Build autonomous agents that maintain coherent goal-directed behavior across extended sequences of tool calls, research tasks, and multi-step problem solving
* **Strategic Planning**: Create detailed plans for complex projects, analyze trade-offs, and orchestrate multi-stage workflows that require reasoning through dependencies and constraints
* **Document Analysis & Pattern Recognition**: Process and analyze extensive unstructured documents, identify connections across multiple sources, and extract precise information from large volumes of data

## Prompting tips

| Tip                                                                                                                       | Rationale                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep the system prompt simple** - `"You are Kimi, an AI assistant created by Moonshot AI."` is the recommended default. | Matches the prompt used during instruction tuning.                                                                                                      |
| **Temperature = 1.0**                                                                                                     | The recommended temperature for Kimi-K2-Thinking; calibrated for optimal reasoning performance.                                                         |
| **Leverage native tool calling**                                                                                          | Pass a JSON schema in `tools=[...]`; set `tool_choice="auto"`. Kimi decides when/what to call, maintaining stability across 200-300 calls.              |
| **Think in goals, not steps**                                                                                             | Because the model is "agentic", give a *high-level objective* ("Analyze this data and write a comprehensive report"), letting it orchestrate sub-tasks. |
| **Manage context for very long inputs**                                                                                   | 256 K is huge, but response speed drops on >100 K inputs; supply a short executive summary in the final user message to focus the model.                |
| **Allow adequate reasoning space**                                                                                        | The model generates both reasoning and content tokens; ensure your `max_tokens` parameter accommodates both for complex problems.                       |

Much of this information was found in the [Kimi GitHub repo](https://github.com/MoonshotAI/Kimi-K2) and the [Kimi K2 Thinking model card](https://huggingface.co/moonshotai/Kimi-K2-Thinking).

## General Limitations of Kimi K2 Thinking

We've outlined various use cases for when to use Kimi K2 Thinking, but it also has a few situations where it currently isn't the best choice:

* **Latency-sensitive applications**: Due to the reasoning process, this model generates more tokens and takes longer than non-reasoning models. For real-time voice agents or applications requiring instant responses, consider the regular Kimi K2 or other faster models.

* **Simple, direct tasks**: For straightforward tasks that don't require deep reasoning (e.g., simple classification, basic text generation), the regular Kimi K2 or other non-reasoning models will be faster and more cost-effective.

* **Cost-sensitive high-volume use cases**: At \$4.00 per 1M output tokens (vs \$3.00 for regular K2), the additional reasoning tokens can increase costs. If you're processing many simple queries where reasoning isn't needed, consider alternatives.

However, for complex problems requiring strategic thinking, multi-step reasoning, or long-horizon agentic workflows, Kimi K2 Thinking provides exceptional value through its transparent reasoning process and superior problem-solving capabilities.
