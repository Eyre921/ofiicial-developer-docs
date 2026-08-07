---
title: "Function calling & tool use"
source: https://docs.together.ai/learn/function-calling-and-tool-use
path: learn/function-calling-and-tool-use
---

The model plans, your code runs the tool. How structured tool calls and agent loops actually work.

**TL;DR:** A model can't actually call functions or APIs to do things in the real world, only output tokens. Instead, you ask the model to output a structured message that says "I want to call this function with these arguments." The software around the LLM is the part that actually runs the call, gets the result, and feeds it back to the model as the next message in the conversation. The model picks things back up from there. Function calling is a structured multi-turn conversation where some of the turns happen to be machine-readable JSON or executable functions instead of natural language. This is the mechanism that every coding agent (Claude Code, Cursor, Codex) and agentic workflow is built on top of.

## The model plans, your code runs the tool

"Function calling" is one of those names that slightly exaggerates: the model can't *actually* execute functions. The model itself has no internet, no shell, no file system, and no way to execute code. It can't run Python, query a database, or call an API on its own. The only thing the model can produce is text.

The cleanest way to think about what's going on is in terms of roles:

* **The model is the planner.** It looks at the conversation, reasons about what should happen next, and either writes a reply to the user or asks for a tool to be run. The model itself can't actually run anything.
* **Your code is the worker.** It sees the model's request, decides whether to honor it, and if so, runs the function, handing the result back as the next message in the conversation.

Completing long, complex tasks takes many turns of reasoning and function calls.

## The loop

One complete tool-using interaction usually looks something like this:

```text theme={null}
USER:       What's the weather in Tokyo right now?

MODEL:      tool_calls: [
              { name: "get_weather",
                arguments: {"city":"Tokyo","units":"celsius"} }
            ]

YOUR CODE:  → fetch https://api.weather.example/v1/Tokyo
            ← { "temp": 12, "conditions": "cloudy" }

TOOL MSG:   { "temp": 12, "conditions": "cloudy" }

MODEL:      It's 12°C and cloudy in Tokyo right now.
```

The model never runs the weather API itself. It asks your code to run it, then waits. Your code runs the API call, and the result becomes a new message in the conversation. The model sees that result and picks up from there to write the final reply.

<ToolLoopDiagram />

## How to tell the model what tools are available

Tools are declared in the API request alongside the messages. Each tool has a name, a description, and a JSON schema for its arguments:

```json theme={null}
[
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the current weather in a city.",
      "parameters": {
        "type": "object",
        "properties": {
          "city":  { "type": "string", "description": "City name" },
          "units": { "type": "string", "enum": ["celsius","fahrenheit"] }
        },
        "required": ["city"]
      }
    }
  }
]
```

The model sees these declarations as part of its prompt. The descriptions you write matter quite a bit, because they are how the model decides which tool is right for a given question. A description like "Get the current weather" is much more useful to the model than something like "Weather function". A useful rule of thumb is to write the description as if you were writing a one-line manual page for another developer.

You can declare as many tools as you want, but more is not always better. With dozens of tools available, the model often starts picking the wrong one or stalling. If you have a lot of capabilities, it usually helps to group them. One `search` tool that takes a query argument tends to work better than twenty narrow tools that each cover a single search type.

<Tip>
  See [Function calling](/docs/inference/function-calling/overview) for the request format and the list of models that support tool calls on Together AI.
</Tip>

## What the model emits

When the model wants to call a tool, the API response includes a `tool_calls` field instead of (or in addition to) a text answer:

```json theme={null}
{
  "role": "assistant",
  "content": null,
  "tool_calls": [
    {
      "id": "call_abc123",
      "type": "function",
      "function": {
        "name": "get_weather",
        "arguments": "{\"city\":\"Tokyo\",\"units\":\"celsius\"}"
      }
    }
  ]
}
```

Two things worth noticing here. The arguments come back as a JSON string, not as an already-parsed object. You parse the string yourself, and you should also validate it, because the model can hallucinate fields or incorrect types. Each call also has an `id`. When you send the results back to the model, you include the same `id` so the model knows which call the result belongs to. This matters when the model emits multiple parallel tool calls in a single turn.

After your code has run the tool, you send the result back as a new message with `role: "tool"`:

```json theme={null}
{
  "role": "tool",
  "tool_call_id": "call_abc123",
  "content": "{\"temp\":12,\"conditions\":\"cloudy\"}"
}
```

Then you call the model again with the full message history. The model sees the tool result and produces the next message, which is either another tool call or the final answer to the user.

## Multi-step agent loops

Real tasks can rarely be completed with a single tool call. A coding agent task like "fix the failing test in `auth.py`" unfolds across many rounds:

1. The model calls `read_file("auth.py")` and `read_file("test_auth.py")`.
2. Your code returns the file contents.
3. The model calls `run_tests("test_auth.py")` to see the failure.
4. Your code returns the failure output.
5. The model reasons about the bug, then calls `edit_file("auth.py", ...)`.
6. Your code applies the edit and returns confirmation.
7. The model re-runs the tests to verify.
8. Your code returns the passing test output.
9. The model writes a final summary message to the user.

This sequence is what people typically call an **agent loop,** and is the basic underlying process for coding agents like Claude Code. Your application keeps calling the model in a loop, and each time it does, it passes in the full message history plus any new tool results. The loop continues until the model decides it is done, which is the point at which it produces a normal text reply with no tool calls in it.

There are two important guardrails for any agent loop:

* **Step limit:** Cap the number of times the loop will iterate before giving up. Models can sometimes spiral into tool-call loops if they get confused. A ceiling of 20–50 steps is reasonable for most tasks, but coding agents often go higher.
* **Tool authorization:** A tool request is not authorization. Even when the model asks for a tool to be run, your code does not have to comply. For anything irreversible (sending money, deleting data, force-pushing to main), your code should require human confirmation before honoring the call.

<Info>
  The **Model Context Protocol (MCP)** has emerged as the standard way to expose tools to any compatible model without redeclaring them per-provider. Tools live as standalone MCP servers, and any MCP-aware model can pick them up via a single connection. Most production coding agents and chat clients now speak MCP, which means you can write a tool once and use it from Claude, ChatGPT, Cursor, and others without changes.
</Info>

## How it goes wrong

There are five common ways tool use breaks in practice:

* **Hallucinated arguments:** The model produces arguments that do not match the schema. There might be a missing field, a wrong type, or a city that does not actually exist. You should always validate the arguments before executing the call, rather than blindly trusting what the model produces.
* **Tool-call loops:** The model keeps calling the same tool with slightly different arguments and getting back the same kind of answer. The common cause is a tool result that is vague or unhelpful, which leads the model to think it didn't get what it asked for. The fix is to make tool outputs explicit ("Found 0 results matching 'cat photos' uploaded after 2024-01-01") or to set a step limit on the loop.
* **Picked the wrong tool:** Two tools have overlapping descriptions and the model picks the wrong one. The fix is to disambiguate the descriptions or merge the two tools into one.
* **Skipped a tool when it should have used one:** The model answers from its training knowledge when fresh data was needed. The fix is to strengthen the system prompt with something like "Always use `lookup_price` before quoting a price".
* **Parallel calls when serial was intended:** Modern models often emit multiple tool calls in a single turn. Make sure your executor can handle them in parallel and that it matches results back to calls using the `id` field.

## Next steps

<CardGroup>
  <Card title="Structured outputs & JSON mode" icon="braces" href="/learn/structured-outputs">
    The same constrained-decoding plumbing, but for non-tool outputs.
  </Card>

  <Card title="Context engineering" icon="messages" href="/learn/prompt-engineering">
    How the system prompt steers tool selection.
  </Card>

  <Card title="Context windows" icon="layout-board" href="/learn/context-windows">
    Agent loops grow the message history fast.
  </Card>
</CardGroup>
