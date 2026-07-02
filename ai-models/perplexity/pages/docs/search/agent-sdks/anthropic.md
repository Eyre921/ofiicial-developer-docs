---
title: "Use Search API with the Anthropic SDK"
source: https://docs.perplexity.ai/docs/search/agent-sdks/anthropic
path: docs/search/agent-sdks/anthropic
---

Register Perplexity's Search API as a tool inside the Anthropic Messages API and run the standard tool-use loop with Claude.

## Overview

This guide shows how to expose Perplexity's [Search API](/docs/search/quickstart) to Claude as a tool. The Anthropic Messages API uses a manual tool-use loop: the model emits a `tool_use` block, you execute the tool (in this case, call `client.search.create`), and you send the result back as a `tool_result`. The loop continues until the model returns a final answer.

## Prerequisites

<CodeGroup>
  ```bash Python theme={null}
  pip install anthropic perplexityai
  export ANTHROPIC_API_KEY="your_anthropic_key"
  export PERPLEXITY_API_KEY="your_perplexity_key"
  ```

  ```bash Typescript theme={null}
  npm install @anthropic-ai/sdk @perplexity-ai/perplexity_ai
  export ANTHROPIC_API_KEY="your_anthropic_key"
  export PERPLEXITY_API_KEY="your_perplexity_key"
  ```
</CodeGroup>

## Tool definition

Claude needs a tool description that tells it when and how to call `web_search`. The description below was tuned for Perplexity's Search API; keep it verbatim — the wording of the description and the parameter guidance is what produces good, short, keyword-style queries.

<CodeGroup>
  ```python Python theme={null}
  WEB_SEARCH_TOOL_DESCRIPTION = """\
  Searches the web for current and factual information to answer user queries, returning relevant results with titles, URLs, and content snippets, similar to Google or Bing. Intended for questions about up-to-date or externally verified information beyond your knowledge cutoff. The tool works best with an array of short, keyword-focused queries. Complex queries that require multi-step reasoning are not supported. Time-sensitive queries are supported if the date is included in the query.

  Best practices for using this tool:
  - Limit the number of queries in each request to a maximum of three to maintain efficiency.
  - For multi-entity questions, break them into separate, single-entity queries:
    - Preferred:
      [
        "Brand A protein powder review",
        "Brand B protein powder review"
      ]
    - Not recommended:
      [
        "Brand A vs Brand B protein powder review"
      ]

  - For simple queries, keep each query straightforward and focused:
    - Preferred: ["inflation rate Canada"]
    - Not recommended: ["What is the inflation rate in Canada?"]

  Each query should be short to ensure optimal tool performance. Make sure all provided examples and generated queries follow this guideline."""

  QUERIES_PARAM_DESCRIPTION = (
      "An array of keyword-based search queries. Each query should be short, "
      "as longer queries may reduce performance. Do not provide more than three "
      "queries to maintain efficiency."
  )

  WEB_SEARCH_TOOL = {
      "name": "web_search",
      "description": WEB_SEARCH_TOOL_DESCRIPTION,
      "input_schema": {
          "type": "object",
          "properties": {
              "queries": {
                  "type": "array",
                  "description": QUERIES_PARAM_DESCRIPTION,
                  "items": {"type": "string"},
                  "minItems": 1,
                  "maxItems": 3,
              },
          },
          "required": ["queries"],
      },
  }
  ```

  ```typescript Typescript theme={null}
  const WEB_SEARCH_TOOL_DESCRIPTION = `Searches the web for current and factual information to answer user queries, returning relevant results with titles, URLs, and content snippets, similar to Google or Bing. Intended for questions about up-to-date or externally verified information beyond your knowledge cutoff. The tool works best with an array of short, keyword-focused queries. Complex queries that require multi-step reasoning are not supported. Time-sensitive queries are supported if the date is included in the query.

  Best practices for using this tool:
  - Limit the number of queries in each request to a maximum of three to maintain efficiency.
  - For multi-entity questions, break them into separate, single-entity queries:
    - Preferred:
      [
        "Brand A protein powder review",
        "Brand B protein powder review"
      ]
    - Not recommended:
      [
        "Brand A vs Brand B protein powder review"
      ]

  - For simple queries, keep each query straightforward and focused:
    - Preferred: ["inflation rate Canada"]
    - Not recommended: ["What is the inflation rate in Canada?"]

  Each query should be short to ensure optimal tool performance. Make sure all provided examples and generated queries follow this guideline.`;

  const QUERIES_PARAM_DESCRIPTION =
    "An array of keyword-based search queries. Each query should be short, " +
    "as longer queries may reduce performance. Do not provide more than three " +
    "queries to maintain efficiency.";

  const WEB_SEARCH_TOOL = {
    name: "web_search",
    description: WEB_SEARCH_TOOL_DESCRIPTION,
    input_schema: {
      type: "object" as const,
      properties: {
        queries: {
          type: "array" as const,
          description: QUERIES_PARAM_DESCRIPTION,
          items: { type: "string" as const },
          minItems: 1,
          maxItems: 3,
        },
      },
      required: ["queries"],
    },
  };
  ```
</CodeGroup>

## Tool handler

The handler is a thin wrapper around `client.search.create`. The Search API natively accepts an array of queries (up to five), so the array Claude emits can be passed straight through.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  perplexity = Perplexity()

  def run_web_search(queries: list[str]) -> str:
      """Call Perplexity Search and format the results for the model."""
      response = perplexity.search.create(query=queries, max_results=5)

      lines = []
      for result in response.results:
          snippet = (result.snippet or "").strip().replace("\n", " ")
          if len(snippet) > 400:
              snippet = snippet[:400] + "…"
          lines.append(f"- {result.title}\n  {result.url}\n  {snippet}")
      return "\n\n".join(lines) if lines else "No results."
  ```

  ```typescript Typescript theme={null}
  import Perplexity from "@perplexity-ai/perplexity_ai";

  const perplexity = new Perplexity();

  async function runWebSearch(queries: string[]): Promise<string> {
    const response = await perplexity.search.create({
      query: queries,
      max_results: 5,
    });

    const lines = response.results.map((r) => {
      const snippet = (r.snippet ?? "").trim().replace(/\n/g, " ");
      const trimmed = snippet.length > 400 ? `${snippet.slice(0, 400)}…` : snippet;
      return `- ${r.title}\n  ${r.url}\n  ${trimmed}`;
    });
    return lines.length ? lines.join("\n\n") : "No results.";
  }
  ```
</CodeGroup>

## Tool-use loop

Anthropic's Messages API hands you a `stop_reason` of `"tool_use"` and one or more `ToolUseBlock` items inside `response.content`. Run each tool call, build a `tool_result` block per call (paired by `tool_use_id`), and send all results back in a single user message. Loop until `stop_reason` is no longer `"tool_use"`.

<CodeGroup>
  ```python Python theme={null}
  import json
  from anthropic import Anthropic

  claude = Anthropic()

  def chat_with_search(user_prompt: str, model: str = "claude-sonnet-4-6") -> str:
      messages = [{"role": "user", "content": user_prompt}]

      while True:
          response = claude.messages.create(
              model=model,
              max_tokens=1024,
              tools=[WEB_SEARCH_TOOL],
              messages=messages,
          )

          if response.stop_reason != "tool_use":
              # Final answer — pull text blocks out of the assistant message.
              return "".join(
                  block.text for block in response.content if block.type == "text"
              )

          # Append the assistant's tool-call turn to history.
          messages.append({"role": "assistant", "content": response.content})

          # Run every tool call in this turn and pair results by tool_use_id.
          tool_results = []
          for block in response.content:
              if block.type != "tool_use":
                  continue
              if block.name == "web_search":
                  output = run_web_search(block.input["queries"])
              else:
                  output = json.dumps({"error": f"unknown tool: {block.name}"})
              tool_results.append({
                  "type": "tool_result",
                  "tool_use_id": block.id,
                  "content": output,
              })

          messages.append({"role": "user", "content": tool_results})


  if __name__ == "__main__":
      answer = chat_with_search(
          "What were the major AI infrastructure announcements this week?"
      )
      print(answer)
  ```

  ```typescript Typescript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const claude = new Anthropic();

  async function chatWithSearch(
    userPrompt: string,
    model = "claude-sonnet-4-6",
  ): Promise<string> {
    const messages: Anthropic.MessageParam[] = [
      { role: "user", content: userPrompt },
    ];

    while (true) {
      const response = await claude.messages.create({
        model,
        max_tokens: 1024,
        tools: [WEB_SEARCH_TOOL],
        messages,
      });

      if (response.stop_reason !== "tool_use") {
        return response.content
          .filter((b): b is Anthropic.TextBlock => b.type === "text")
          .map((b) => b.text)
          .join("");
      }

      messages.push({ role: "assistant", content: response.content });

      const toolResults: Anthropic.ToolResultBlockParam[] = [];
      for (const block of response.content) {
        if (block.type !== "tool_use") continue;
        let output: string;
        if (block.name === "web_search") {
          const input = block.input as { queries: string[] };
          output = await runWebSearch(input.queries);
        } else {
          output = JSON.stringify({ error: `unknown tool: ${block.name}` });
        }
        toolResults.push({
          type: "tool_result",
          tool_use_id: block.id,
          content: output,
        });
      }

      messages.push({ role: "user", content: toolResults });
    }
  }

  (async () => {
    const answer = await chatWithSearch(
      "What were the major AI infrastructure announcements this week?",
    );
    console.log(answer);
  })();
  ```
</CodeGroup>

## Streaming

For streaming responses, use `client.messages.stream(...)` and accumulate `tool_use` blocks from the events. The model emits `input_json_delta` events with partial JSON arguments; the SDK helper accumulates them and exposes the completed `tool_use` block via `stream.get_final_message()` (Python) or `stream.finalMessage()` (TypeScript). The loop structure is otherwise identical to the non-streaming version.

<CodeGroup>
  ```python Python theme={null}
  with claude.messages.stream(
      model="claude-sonnet-4-6",
      max_tokens=1024,
      tools=[WEB_SEARCH_TOOL],
      messages=messages,
  ) as stream:
      for text in stream.text_stream:
          print(text, end="", flush=True)
      final = stream.get_final_message()

  # Inspect final.stop_reason and final.content for tool_use blocks, then
  # resume the loop the same way as in the non-streaming version.
  ```

  ```typescript Typescript theme={null}
  const stream = claude.messages.stream({
    model: "claude-sonnet-4-6",
    max_tokens: 1024,
    tools: [WEB_SEARCH_TOOL],
    messages,
  });

  for await (const chunk of stream) {
    if (chunk.type === "content_block_delta" && chunk.delta.type === "text_delta") {
      process.stdout.write(chunk.delta.text);
    }
  }
  const final = await stream.finalMessage();
  // Inspect final.stop_reason and final.content as in the non-streaming version.
  ```
</CodeGroup>

## Notes

* **Parallel tool calls.** Claude can emit multiple `tool_use` blocks in a single assistant turn. Every block must have a matching `tool_result` in the *same* subsequent user message, paired by `tool_use_id`. To disable, set `tool_choice={"type": "auto", "disable_parallel_tool_use": True}`.
* **Result formatting.** The string returned to `tool_result.content` is what the model reads next. Including the URL alongside the snippet helps the model cite sources when it produces its final answer.
* **Errors.** To signal that a tool call failed, set `"is_error": True` on the `tool_result` block and put a short error message in `content`. The model will see the error and can recover (for example, by reformulating queries).
* **Domains and dates.** Pass `search_domain_filter`, `country`, and other Search API parameters inside `run_web_search` if you want fixed retrieval constraints. See the [Search API quickstart](/docs/search/quickstart) for the full parameter list.

## Next Steps

<CardGroup>
  <Card title="Use with OpenAI SDK" icon="code" href="/docs/search/agent-sdks/openai">
    Wire Search API into the OpenAI Responses API.
  </Card>

  <Card title="Use with Gemini SDK" icon="code" href="/docs/search/agent-sdks/gemini">
    Wire Search API into Google's `google-genai` SDK.
  </Card>

  <Card title="Search API Quickstart" icon="rocket" href="/docs/search/quickstart">
    Full Search API parameter reference.
  </Card>

  <Card title="Search Best Practices" icon="lightbulb" href="/docs/search/best-practices">
    Patterns for production search workloads.
  </Card>
</CardGroup>
