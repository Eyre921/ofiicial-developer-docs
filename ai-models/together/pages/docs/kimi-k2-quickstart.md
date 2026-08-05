---
title: "Kimi K2 quickstart"
source: https://docs.together.ai/docs/kimi-k2-quickstart
path: docs/kimi-k2-quickstart
---

How to get the most out of models like Kimi K2.

<Tip>
  Kimi K2-Instruct-0905 has been deprecated. Use [Kimi K2.6](/docs/kimi-k2.6-quickstart) (`moonshotai/Kimi-K2.6`) in Instruct mode instead.
</Tip>

Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model developed by Moonshot AI. It's a 1 trillion total parameter model (32B activated) that is currently the best non-reasoning open source model out there.

It was trained on 15.5 trillion tokens, supports a 256k context window, and excels in agentic tasks, coding, reasoning, and tool use. Even though it's a 1T model, at inference time, the fact that only 32 B parameters are active gives it near‑frontier quality at a fraction of the compute of dense peers.

This quick guide goes over the main use cases for Kimi K2, how to get started with it, when to use it, and prompting tips for getting the most out of this incredible model.

## How to use Kimi K2

Get started with this model in 10 lines of code! The model ID is `moonshotai/Kimi-K2-Instruct-0905` and the pricing is \$1.00 per 1M input tokens and \$3.00 per 1M output tokens.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
      model="moonshotai/Kimi-K2-Instruct-0905",
      messages=[{"role": "user", "content": "Code a hacker news clone"}],
      stream=True,
  )
  for tok in resp:
      print(tok.choices[0].delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [{ role: 'user', content: 'Code a hackernews clone' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

## Use cases

Kimi K2 shines in scenarios requiring autonomous problem-solving – specifically with coding & tool use:

* **Agentic Workflows**: Automate multi-step tasks like booking flights, research, or data analysis using tools/APIs
* **Coding & Debugging**: Solve software engineering tasks (e.g., SWE-bench), generate patches, or debug code
* **Research & Report Generation**: Summarize technical documents, analyze trends, or draft reports using long-context capabilities
* **STEM Problem-Solving**: Tackle advanced math (AIME, MATH), logic puzzles (ZebraLogic), or scientific reasoning
* **Tool Integration**: Build AI agents that interact with APIs (e.g., weather data, databases).

## Prompting tips

| Tip                                                                                                                       | Rationale                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep the system prompt simple** - `"You are Kimi, an AI assistant created by Moonshot AI."` is the recommended default. | Matches the prompt used during instruction tuning.                                                                                       |
| **Temperature ≈ 0.6**                                                                                                     | Calibrated to Kimi-K2-Instruct's RLHF alignment curve. Higher values yield verbosity.                                                    |
| **Leverage native tool calling**                                                                                          | Pass a JSON schema in `tools=[...]` and set `tool_choice="auto"`. Kimi decides when/what to call.                                        |
| **Think in goals, not steps**                                                                                             | Because the model is "agentic", give a *high-level objective* ("Analyze this CSV and write a report"), letting it orchestrate sub-tasks. |
| **Chunk very long contexts**                                                                                              | 256 K is huge, but response speed drops on >100 K inputs. Supply a short executive summary in the final user message to focus the model. |

Much of this information was found in the [Kimi GitHub repo](https://github.com/MoonshotAI/Kimi-K2).

## General Limitations of Kimi K2

The sections above outline various use cases for when to use Kimi K2, but it also has a few situations where it currently isn't the best. The main ones are for latency specific applications like real-time voice agents, it's not the best solution currently due to its speed.

Similarly, if you wanted a quick summary for a long PDF, even though it can handle a good amount of context (256k tokens), its speed is a bit prohibitive if you want to show text quickly to your user as it can get even slower when it is given a lot of context. However, if you're summarizing PDFs async for example or in another scenario where latency isn't a concern, this could be a good model to try.
