---
title: "Use Search API with the OpenAI SDK"
source: https://docs.perplexity.ai/docs/search/agent-sdks/openai
path: docs/search/agent-sdks/openai
---

Register Perplexity's Search API as a function tool inside the OpenAI Responses API and run the standard tool-call loop with GPT models.

## Overview

This guide shows how to expose Perplexity's [Search API](/docs/search/quickstart) to an OpenAI model as a function tool. The Responses API uses a manual tool-call loop: the model emits a `function_call` item with a `call_id`, you execute the tool (in this case, call `client.search.create`), and you send the result back as a `function_call_output` item paired by `call_id`. The loop continues until the response no longer contains pending function calls.

<Info>
  This page uses the **Responses API** (`client.responses.create`), the newer OpenAI surface. The tool shape is flat (`{type: "function", name, description, parameters, strict}`) — different from the legacy `chat.completions` function-calling shape that nests under `function: {…}`.
</Info>

## Prerequisites

<CodeGroup>
  ```bash Python theme={null}
  pip install openai perplexityai
  export OPENAI_API_KEY="your_openai_key"
  export PERPLEXITY_API_KEY="your_perplexity_key"
  ```

  ```bash Typescript theme={null}
  npm install openai @perplexity-ai/perplexity_ai
  export OPENAI_API_KEY="your_openai_key"
  export PERPLEXITY_API_KEY="your_perplexity_key"
  ```
</CodeGroup>

## Tool definition

The Responses API takes a flat tool object: `type`, `name`, `description`, `parameters` (JSON Schema), and optional `strict`. The description below was tuned for Perplexity's Search API; keep it verbatim — the wording is what produces good, short, keyword-style queries.

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
      "type": "function",
      "name": "web_search",
      "description": WEB_SEARCH_TOOL_DESCRIPTION,
      "strict": True,
      "parameters": {
          "type": "object",
          "additionalProperties": False,
          "properties": {
              "queries": {
                  "type": "array",
                  "description": QUERIES_PARAM_DESCRIPTION,
                  "items": {"type": "string"},
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
    type: "function" as const,
    name: "web_search",
    description: WEB_SEARCH_TOOL_DESCRIPTION,
    strict: true,
    parameters: {
      type: "object" as const,
      additionalProperties: false,
      properties: {
        queries: {
          type: "array" as const,
          description: QUERIES_PARAM_DESCRIPTION,
          items: { type: "string" as const },
        },
      },
      required: ["queries"],
    },
  };
  ```
</CodeGroup>

<Warning>
  **Strict mode constraints.** When `strict: true`, the JSON Schema must set `additionalProperties: false` and list every property in `required`. OpenAI rejects `maxItems`/`minItems` and similar constraints in strict mode — enforce the "max three queries" guidance through the description, then truncate defensively in your handler.
</Warning>

## Tool handler

The handler is a thin wrapper around `client.search.create`. The Search API natively accepts an array of queries, so the array the model emits can be passed straight through.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  perplexity = Perplexity()

  def run_web_search(queries: list[str]) -> str:
      """Call Perplexity Search and format the results for the model."""
      # Defensive cap — the description asks for ≤3, but trust nothing.
      queries = queries[:3]

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
    const capped = queries.slice(0, 3);

    const response = await perplexity.search.create({
      query: capped,
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

## Tool-call loop

The Responses API returns `response.output` as a flat list of items. Walk it for items whose `type` is `"function_call"`, execute each call, and append a paired `function_call_output` item to the running `input` array. Re-call `responses.create` until the response has no more function calls.

<CodeGroup>
  ```python Python theme={null}
  import json
  from openai import OpenAI

  openai_client = OpenAI()

  def chat_with_search(user_prompt: str, model: str = "gpt-5.5") -> str:
      # The Responses API's `input` is an ordered list of items; we append
      # function_call_output items to it as the loop progresses.
      input_items: list[dict] = [{"role": "user", "content": user_prompt}]

      while True:
          response = openai_client.responses.create(
              model=model,
              input=input_items,
              tools=[WEB_SEARCH_TOOL],
          )

          function_calls = [
              item for item in response.output if item.type == "function_call"
          ]

          if not function_calls:
              return response.output_text

          # Persist the assistant's function_call items in the conversation.
          for item in response.output:
              input_items.append(item.model_dump())

          # Run each function call and append a paired function_call_output.
          for call in function_calls:
              args = json.loads(call.arguments)
              if call.name == "web_search":
                  output = run_web_search(args["queries"])
              else:
                  output = json.dumps({"error": f"unknown tool: {call.name}"})
              input_items.append({
                  "type": "function_call_output",
                  "call_id": call.call_id,
                  "output": output,
              })


  if __name__ == "__main__":
      answer = chat_with_search(
          "What were the major AI infrastructure announcements this week?"
      )
      print(answer)
  ```

  ```typescript Typescript theme={null}
  import OpenAI from "openai";

  const openaiClient = new OpenAI();

  async function chatWithSearch(
    userPrompt: string,
    model = "gpt-5.5",
  ): Promise<string> {
    const inputItems: OpenAI.Responses.ResponseInputItem[] = [
      { role: "user", content: userPrompt },
    ];

    while (true) {
      const response = await openaiClient.responses.create({
        model,
        input: inputItems,
        tools: [WEB_SEARCH_TOOL],
      });

      const functionCalls = response.output.filter(
        (item): item is OpenAI.Responses.ResponseFunctionToolCall =>
          item.type === "function_call",
      );

      if (functionCalls.length === 0) {
        return response.output_text;
      }

      // Persist the assistant's function_call items in the conversation.
      inputItems.push(...response.output);

      for (const call of functionCalls) {
        const args = JSON.parse(call.arguments) as { queries: string[] };
        let output: string;
        if (call.name === "web_search") {
          output = await runWebSearch(args.queries);
        } else {
          output = JSON.stringify({ error: `unknown tool: ${call.name}` });
        }
        inputItems.push({
          type: "function_call_output",
          call_id: call.call_id,
          output,
        });
      }
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

For streaming, use `client.responses.stream(...)`. The SDK emits typed events: `response.output_item.added` when a `function_call` item starts, `response.function_call_arguments.delta` for each chunk of the arguments JSON, and `response.function_call_arguments.done` when the argument string is complete. The loop structure is otherwise identical to the non-streaming version.

<CodeGroup>
  ```python Python theme={null}
  with openai_client.responses.stream(
      model="gpt-5.5",
      input=input_items,
      tools=[WEB_SEARCH_TOOL],
  ) as stream:
      for event in stream:
          if event.type == "response.output_text.delta":
              print(event.delta, end="", flush=True)
      final = stream.get_final_response()

  # Inspect final.output for function_call items, then resume the loop the
  # same way as in the non-streaming version.
  ```

  ```typescript Typescript theme={null}
  const stream = openaiClient.responses.stream({
    model: "gpt-5.5",
    input: inputItems,
    tools: [WEB_SEARCH_TOOL],
  });

  for await (const event of stream) {
    if (event.type === "response.output_text.delta") {
      process.stdout.write(event.delta);
    }
  }
  const final = await stream.finalResponse();
  // Inspect final.output for function_call items as in the non-streaming version.
  ```
</CodeGroup>

## Notes

* **`call_id` pairs requests with results.** Every `function_call_output` item must include the originating `call_id`. Multiple parallel function calls in one assistant turn each get their own paired output.
* **Server-side state.** Instead of resending the whole `input` array on each turn, you can pass `previous_response_id=<id>` and only append new items. This is useful for long agent loops.
* **`output_text` shortcut.** `response.output_text` flattens the assistant text content for you. If you need granular access (annotations, segments), iterate `response.output` and pull `output_text` blocks out of the message item.
* **Domains and dates.** Pass `search_domain_filter`, `country`, and other Search API parameters inside `run_web_search` if you want fixed retrieval constraints. See the [Search API quickstart](/docs/search/quickstart) for the full parameter list.

## Next Steps

<CardGroup>
  <Card title="Use with Anthropic SDK" icon="code" href="/docs/search/agent-sdks/anthropic">
    Wire Search API into the Anthropic Messages API.
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
