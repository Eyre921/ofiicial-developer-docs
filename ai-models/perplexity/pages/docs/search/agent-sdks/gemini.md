---
title: "Use Search API with the Google Gemini SDK"
source: https://docs.perplexity.ai/docs/search/agent-sdks/gemini
path: docs/search/agent-sdks/gemini
---

Register Perplexity's Search API as a function tool inside Google's google-genai SDK and run the tool-call loop with Gemini models.

## Overview

This guide shows how to expose Perplexity's [Search API](/docs/search/quickstart) to Gemini as a function tool through Google's `google-genai` SDK. The model emits a `functionCall` part with `name` and `args`, you execute the tool (in this case, call `client.search.create`), and you send the result back as a `functionResponse` part. The loop continues until the model returns a final text response.

<Info>
  The Python SDK can run the tool-call loop **automatically** if you pass a Python callable directly to `tools=[...]` — the SDK introspects the signature and invokes your function. This page uses the **manual** loop so the pattern matches the [Anthropic](/docs/search/agent-sdks/anthropic) and [OpenAI](/docs/search/agent-sdks/openai) integration pages and so you keep explicit control over the call. The auto-loop variant is shown in [Notes](#notes).
</Info>

## Prerequisites

<CodeGroup>
  ```bash Python theme={null}
  pip install google-genai perplexityai
  export GEMINI_API_KEY="your_gemini_key"
  export PERPLEXITY_API_KEY="your_perplexity_key"
  ```

  ```bash Typescript theme={null}
  npm install @google/genai @perplexity-ai/perplexity_ai
  export GEMINI_API_KEY="your_gemini_key"
  export PERPLEXITY_API_KEY="your_perplexity_key"
  ```
</CodeGroup>

## Tool definition

Gemini accepts a `Tool` containing one or more `FunctionDeclaration` objects. Each declaration takes a `name`, `description`, and a JSON Schema for parameters. The description below was tuned for Perplexity's Search API; keep it verbatim — the wording is what produces good, short, keyword-style queries.

<CodeGroup>
  ```python Python theme={null}
  from google.genai import types

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

  WEB_SEARCH_FUNCTION = types.FunctionDeclaration(
      name="web_search",
      description=WEB_SEARCH_TOOL_DESCRIPTION,
      parameters_json_schema={
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
  )

  WEB_SEARCH_TOOL = types.Tool(function_declarations=[WEB_SEARCH_FUNCTION])
  ```

  ```typescript Typescript theme={null}
  import { Type } from "@google/genai";
  import type { FunctionDeclaration, Tool } from "@google/genai";

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

  const WEB_SEARCH_FUNCTION: FunctionDeclaration = {
    name: "web_search",
    description: WEB_SEARCH_TOOL_DESCRIPTION,
    parametersJsonSchema: {
      type: "object",
      properties: {
        queries: {
          type: "array",
          description: QUERIES_PARAM_DESCRIPTION,
          items: { type: "string" },
          minItems: 1,
          maxItems: 3,
        },
      },
      required: ["queries"],
    },
  };

  const WEB_SEARCH_TOOL: Tool = {
    functionDeclarations: [WEB_SEARCH_FUNCTION],
  };
  ```
</CodeGroup>

## Tool handler

The handler is a thin wrapper around `client.search.create`. The Search API natively accepts an array of queries (up to five), so the array Gemini emits can be passed straight through.

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

## Tool-call loop

Disable the automatic loop with `AutomaticFunctionCallingConfig(disable=True)` (Python) — the JS SDK doesn't auto-loop in core APIs to begin with. Then walk `response.function_calls`, execute each call, and send the model a follow-up `Content` array that contains the original `function_call` parts and the matching `function_response` parts.

<CodeGroup>
  ```python Python theme={null}
  import json
  from google import genai
  from google.genai import types

  gemini = genai.Client()

  def chat_with_search(user_prompt: str, model: str = "gemini-2.5-flash") -> str:
      contents: list[types.Content] = [
          types.Content(
              role="user",
              parts=[types.Part.from_text(text=user_prompt)],
          ),
      ]

      config = types.GenerateContentConfig(
          tools=[WEB_SEARCH_TOOL],
          automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
      )

      while True:
          response = gemini.models.generate_content(
              model=model,
              contents=contents,
              config=config,
          )

          function_calls = response.function_calls or []

          if not function_calls:
              return response.text

          # Persist the assistant's function_call parts.
          contents.append(response.candidates[0].content)

          # Run each function call and pair results by name (Gemini matches
          # function_response → function_call positionally within the turn).
          response_parts: list[types.Part] = []
          for call in function_calls:
              if call.name == "web_search":
                  queries = call.args.get("queries", [])
                  output = run_web_search(queries)
                  result = {"result": output}
              else:
                  result = {"error": f"unknown tool: {call.name}"}
              response_parts.append(
                  types.Part.from_function_response(name=call.name, response=result)
              )

          contents.append(types.Content(role="user", parts=response_parts))


  if __name__ == "__main__":
      answer = chat_with_search(
          "What were the major AI infrastructure announcements this week?"
      )
      print(answer)
  ```

  ```typescript Typescript theme={null}
  import { GoogleGenAI, type Content, type Part } from "@google/genai";

  const gemini = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

  async function chatWithSearch(
    userPrompt: string,
    model = "gemini-2.5-flash",
  ): Promise<string> {
    const contents: Content[] = [
      { role: "user", parts: [{ text: userPrompt }] },
    ];

    while (true) {
      const response = await gemini.models.generateContent({
        model,
        contents,
        config: { tools: [WEB_SEARCH_TOOL] },
      });

      const functionCalls = response.functionCalls ?? [];

      if (functionCalls.length === 0) {
        return response.text ?? "";
      }

      // Persist the assistant's function_call parts.
      const candidate = response.candidates?.[0];
      if (candidate?.content) {
        contents.push(candidate.content);
      }

      const responseParts: Part[] = [];
      for (const call of functionCalls) {
        let result: Record<string, unknown>;
        if (call.name === "web_search") {
          const queries = (call.args?.queries as string[]) ?? [];
          result = { result: await runWebSearch(queries) };
        } else {
          result = { error: `unknown tool: ${call.name}` };
        }
        responseParts.push({
          functionResponse: { name: call.name!, response: result },
        });
      }

      contents.push({ role: "user", parts: responseParts });
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

For streaming, use `generate_content_stream` (Python) or `generateContentStream` (TypeScript). A single `functionCall` part can be split across stream chunks, so accumulate parts before invoking your handler. The loop structure is otherwise identical to the non-streaming version.

<CodeGroup>
  ```python Python theme={null}
  for chunk in gemini.models.generate_content_stream(
      model="gemini-2.5-flash",
      contents=contents,
      config=config,
  ):
      if chunk.text:
          print(chunk.text, end="", flush=True)
      # Accumulate function-call parts across chunks before executing.
  ```

  ```typescript Typescript theme={null}
  const stream = await gemini.models.generateContentStream({
    model: "gemini-2.5-flash",
    contents,
    config: { tools: [WEB_SEARCH_TOOL] },
  });

  for await (const chunk of stream) {
    if (chunk.text) process.stdout.write(chunk.text);
    // Accumulate function-call parts across chunks before executing.
  }
  ```
</CodeGroup>

## Notes

* **Automatic loop (Python only).** The Python SDK can run the tool-call loop for you. Pass a Python callable directly and the SDK will introspect its signature, invoke it, and feed the result back to the model — no manual loop, no `Content` plumbing.

  ```python theme={null}
  def web_search(queries: list[str]) -> str:
      """<paste the verbatim WEB_SEARCH_TOOL_DESCRIPTION here as the docstring>"""
      return run_web_search(queries)

  response = gemini.models.generate_content(
      model="gemini-2.5-flash",
      contents="What were the major AI infrastructure announcements this week?",
      config=types.GenerateContentConfig(tools=[web_search]),
  )
  print(response.text)
  ```

  The auto-loop depth caps at 10 by default — raise it via `AutomaticFunctionCallingConfig(maximum_remote_calls=N)` for long research chains. Auto-mode is convenient but trades visibility for terseness: errors surface through exceptions rather than tool-result content the model can recover from.
* **Parallel calls.** Gemini can emit multiple `function_call` parts in a single response. Build one `function_response` part per call (matched by `name` plus the call's position within the turn) and put them all in one follow-up `Content`.
* **Pair `function_call` and `function_response`.** Both turns must be present in the next `generate_content` call — the model needs to see its own `function_call` part alongside your `function_response` part. Dropping either side produces "missing function response" errors.
* **Domains and dates.** Pass `search_domain_filter`, `country`, and other Search API parameters inside `run_web_search` if you want fixed retrieval constraints. See the [Search API quickstart](/docs/search/quickstart) for the full parameter list.

## Next Steps

<CardGroup>
  <Card title="Use with Anthropic SDK" icon="code" href="/docs/search/agent-sdks/anthropic">
    Wire Search API into the Anthropic Messages API.
  </Card>

  <Card title="Use with OpenAI SDK" icon="code" href="/docs/search/agent-sdks/openai">
    Wire Search API into the OpenAI Responses API.
  </Card>

  <Card title="Search API Quickstart" icon="rocket" href="/docs/search/quickstart">
    Full Search API parameter reference.
  </Card>

  <Card title="Search Best Practices" icon="lightbulb" href="/docs/search/best-practices">
    Patterns for production search workloads.
  </Card>
</CardGroup>
