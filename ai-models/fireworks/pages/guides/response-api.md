---
title: "Responses API"
source: https://docs.fireworks.ai/guides/response-api
path: guides/response-api
---

Build stateful, tool-using applications on Fireworks with the OpenAI-compatible Responses API.

The Responses API is an OpenAI-compatible endpoint for stateful, tool-using applications. Unlike chat completions, it can store conversation state server-side, execute MCP tools on your behalf, and run long jobs in the background.

<Warning title="Data Retention Policy">
  The Responses API has a different data retention policy than the chat completions endpoint. See [Data Privacy & security](/guides/security_compliance/data_handling#response-api-data-retention).
</Warning>

## Endpoint and authentication

The Responses API is served at `https://api.fireworks.ai/inference/v1/responses`. Authenticate with your Fireworks API key as a bearer token, and set `model` to a Fireworks model resource name.

<CodeGroup>
  ```python OpenAI SDK theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.environ["FIREWORKS_API_KEY"],
  )

  response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="What is the capital of France?",
  )

  print(response.output_text)
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.fireworks.ai/inference/v1/responses \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "accounts/fireworks/models/qwen3-235b-a22b",
      "input": "What is the capital of France?"
    }'
  ```
</CodeGroup>

<Note>
  The OpenAI SDK base URL includes `/v1`; the SDK appends `/responses`. Only `model` and `input` are required.
</Note>

## Streaming

Set `stream=True` to receive semantic events as the response is produced.

```python OpenAI SDK theme={null}
stream = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="Give me 5 interesting facts about the Model Context Protocol.",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

Events follow the OpenAI Responses event vocabulary, including `response.created`, `response.output_text.delta`, `response.output_text.done`, the `response.web_search_call.*` and `response.reasoning_summary_text.*` families, and a terminal `response.completed`.

## Conversation state

By default responses are stored, and you can continue a conversation by referencing the previous response instead of resending the full history.

```python OpenAI SDK theme={null}
first = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="What are the key features of reward-kit?",
)

second = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="How do I install it?",
    previous_response_id=first.id,
)

print(second.output_text)
```

Set `store=False` to opt out of storage. Responses created with `store=False` cannot be referenced by `previous_response_id`, so you must manage history yourself by passing prior turns in `input`.

### Managing stored responses

| Operation           | Endpoint                             |
| ------------------- | ------------------------------------ |
| Retrieve a response | `GET /v1/responses/{response_id}`    |
| List responses      | `GET /v1/responses`                  |
| Delete a response   | `DELETE /v1/responses/{response_id}` |

Listing responses is a Fireworks extension; OpenAI does not offer it.

```bash cURL theme={null}
curl -X DELETE "https://api.fireworks.ai/inference/v1/responses/$RESPONSE_ID" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

<Warning>
  Deletion is permanent. Once a response is deleted it cannot be recovered.
</Warning>

## Tools

Tools fall into two groups, and you can mix them in a single request:

* **Server-executed** (`mcp`, `sse`, `web_search`, `python`) run on Fireworks. The results come back in the output array and the model continues automatically.
* **Client-executed** (`function`, and Codex `namespace`) are returned to you as `function_call` items. You run them and send the results back.

Use `max_tool_calls` to cap the total number of tool calls in a single response.

### MCP servers

Pass an MCP server and Fireworks will discover its tools, call them, and feed the results back to the model.

```python OpenAI SDK theme={null}
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="Summarize the README of modelcontextprotocol/python-sdk.",
    tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}],
)

print(response.output_text)
```

Use `{"type": "sse", "server_url": "..."}` for servers that speak the SSE transport. Server-executed calls appear in `output` as `mcp_call` items.

### Client-side functions

```python OpenAI SDK theme={null}
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="What is the weather in Paris?",
    tools=[{
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    }],
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
```

### Web search

Add the built-in `web_search` tool to let the model search the web. Results appear as `web_search_call` items in the output array.

```python OpenAI SDK theme={null}
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="What happened in AI research this week?",
    tools=[{"type": "web_search"}],
)
```

Web search must be enabled for your account. If it is not, the request fails with a `403`.

### Codex namespace tools

Codex packs MCP tools into `type: "namespace"` wrappers. Fireworks expands these into individual callable tools, exposing them to the model as `<namespace>__<tool>` and splitting the call back into `{namespace, name}` in the response so Codex can dispatch it.

```json theme={null}
{
  "type": "namespace",
  "name": "mcp__jira__",
  "tools": [{ "type": "function", "name": "search", "parameters": {} }]
}
```

Two constraints apply:

* Nested entries must be `function` tools. Other nested types are rejected.
* Flattened names must be unique. If two namespaces collapse to the same flat name, or a flat name collides with a top-level `function` tool, the request is rejected rather than silently mis-dispatched.

The reserved Codex namespaces `multi_tool_use`, `functions`, `web`, and `python` are passed through without expansion.

<Note>
  `defer_loading` has no effect on the Responses API — there is no tool-search protocol here, so deferred tools are exposed to the model eagerly. Deferred tool loading *is* supported on the [Anthropic-compatible Messages API](/tools-sdks/anthropic-compatibility#tool-search-and-deferred-tool-loading).
</Note>

## Reasoning

Set `reasoning.effort` to control how much the model thinks. Reasoning appears in the output array as `reasoning` items with `summary_text` parts.

```python OpenAI SDK theme={null}
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="Prove that the square root of 2 is irrational.",
    reasoning={"effort": "high"},
)
```

`reasoning.summary` is not configurable — summaries are always included when the model produces reasoning content.

## Structured output

Constrain output to a JSON schema with `text.format`:

```python OpenAI SDK theme={null}
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="Extract the city and country from: 'The Eiffel Tower is in Paris, France.'",
    text={
        "format": {
            "type": "json_schema",
            "name": "location",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "country": {"type": "string"},
                },
                "required": ["city", "country"],
            },
        }
    },
)
```

`{"type": "json_object"}` is also supported for unconstrained JSON. See [Structured outputs](/structured-responses/structured-output-grammar-based) for schema guidance.

## Background mode

For long-running work, set `background=True`. The request returns immediately with `status: "queued"`, and you poll for completion.

```python OpenAI SDK theme={null}
import time

response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="Write a detailed migration plan for our monolith.",
    background=True,
)

while response.status in ("queued", "in_progress"):
    time.sleep(2)
    response = client.responses.retrieve(response.id)

print(response.output_text)
```

Cancel an in-flight background response with `POST /v1/responses/{response_id}/cancel`. Cancellation is idempotent: responses still running move to `cancelling` and finalize as `cancelled`, while already-terminal responses are returned unchanged with a `200`.

Two limits apply:

* `background=True` cannot be combined with `stream=True`. Choose polling or streaming.
* Not every model supports background mode. Unsupported models fail with `model_not_supported_for_background`.

## Logprobs

Set `top_logprobs` and request `include=["message.output_text.logprobs"]` to get token log probabilities attached to `output_text` content parts. `message.output_text.logprobs` is the only supported `include` value.

## Errors

Errors use the OpenAI Responses error envelope:

```json theme={null}
{
  "error": {
    "type": "invalid_request_error",
    "code": "model_not_supported_for_background",
    "message": "Model ... is not supported for background mode.",
    "param": null
  }
}
```

Status codes are preserved from the underlying inference call, so a `429` stays a `429` and client SDK retry logic behaves normally. In streaming and background requests — where an error cannot be raised as an HTTP status after the response has begun — the error is embedded in the response object or emitted as an SSE error event instead.

See [Inference error codes](/guides/inference-error-codes) for the shared status-code catalog.

## Compatibility with OpenAI

Supported request fields: `model`, `input`, `instructions`, `stream`, `store`, `previous_response_id`, `background`, `include`, `tools`, `tool_choice`, `parallel_tool_calls`, `max_tool_calls`, `max_output_tokens`, `metadata`, `reasoning`, `text`, `temperature`, `top_p`, `top_logprobs`, `truncation`, `user`, and `prompt_cache_key`.

Not currently supported:

| Feature                                                     | Status                                  |
| ----------------------------------------------------------- | --------------------------------------- |
| `code_interpreter`, `file_search`, `image_generation` tools | Not supported                           |
| `refusal` content parts                                     | Not supported                           |
| `GET /v1/responses/{id}/input_items`                        | Not supported                           |
| `background` + `stream` together                            | Not supported                           |
| `include` values other than `message.output_text.logprobs`  | Not supported                           |
| `reasoning.summary` configuration                           | Always on when reasoning content exists |

For the full request and response schema, see the [Responses API reference](/api-reference/post-responses).

## Use with Codex

Configure Codex to use Fireworks by adding a provider to `~/.codex/config.toml`:

```toml theme={null}
model = "accounts/fireworks/models/qwen3-235b-a22b"
model_provider = "fireworks"

[model_providers.fireworks]
name = "Fireworks"
base_url = "https://api.fireworks.ai/inference/v1"
env_key = "FIREWORKS_API_KEY"
wire_api = "responses"
```

Set `wire_api = "responses"` so Codex targets this endpoint rather than chat completions, and export `FIREWORKS_API_KEY` in your shell.

### Troubleshooting

| Symptom                                                    | Cause and fix                                                                                                                                 |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `404` "Model not found, inaccessible, and/or not deployed" | `model` is not a Fireworks model resource name, or it is not deployed to your account. Use the full `accounts/<account>/models/<model>` form. |
| MCP tools never get called                                 | The namespace wrapper was rejected or its nested entries are not `function` tools. Check the error body for the offending namespace.          |
| Ambiguous flattened tool name                              | Two namespaces expand to the same `<namespace>__<tool>` name. Rename one of the MCP servers.                                                  |
| `400` combining background and streaming                   | Codex requested both. Disable one.                                                                                                            |

## Cookbook examples

<CardGroup>
  <Card title="MCP examples" href="https://github.com/fw-ai/cookbook/blob/main/archived/learn/response-api/fireworks_mcp_examples.ipynb" icon="plug">
    Calling MCP servers from the Responses API
  </Card>

  <Card title="Continuing conversations" href="https://github.com/fw-ai/cookbook/blob/main/archived/learn/response-api/fireworks_previous_response_cookbook.ipynb" icon="comments">
    Using `previous_response_id`
  </Card>

  <Card title="Streaming" href="https://github.com/fw-ai/cookbook/blob/main/archived/learn/response-api/fireworks_streaming_example.ipynb" icon="bolt">
    Streaming responses end to end
  </Card>

  <Card title="Stateless requests" href="https://github.com/fw-ai/cookbook/blob/main/archived/learn/response-api/mcp_server_with_store_false_argument.ipynb" icon="database">
    Using `store=false`
  </Card>
</CardGroup>
