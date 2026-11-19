---
title: "Call Model (Typescript)"
source: https://openrouter.ai/docs/agent-sdk/call-model/overview.md
path: docs/agent-sdk/call-model/overview
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Model (Typescript)

> A unified API for calling any LLM with automatic tool execution and multiple consumption patterns

## Why callModel?

* **Items-Based Model**: Built on OpenRouter's Responses API with structured items (messages, tool calls, reasoning) instead of raw message chunks
* **Multiple Consumption Patterns**: Get text, stream responses, or access structured data - all from a single call
* **Automatic Tool Execution**: Define tools with Zod schemas and let the SDK handle execution loops
* **Type Safety**: Full TypeScript inference for tool inputs, outputs, and events
* **Format Compatibility**: Convert to/from OpenAI chat and Anthropic Claude message formats
* **Streaming First**: Built on a reusable stream architecture that supports concurrent consumers

## Quick Start

```typescript lines theme={null}
import { OpenRouter } from '@openrouter/agent';

const openrouter = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const result = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'What is the capital of France?',
});

// Get text (simplest pattern)
const text = await result.getText();
console.log(text); // "The capital of France is Paris."
```

```python title="Python" lines theme={null}
import asyncio
import os
from openrouter_agent import OpenRouter, call_model


async def main() -> None:
    client = OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"])

    result = call_model(
        client,
        {
            "model": "openai/gpt-5-nano",
            "input": "What is the capital of France?",
        },
    )

    # Get text (simplest pattern)
    text = await result.get_text()
    print(text)  # "The capital of France is Paris."


asyncio.run(main())

```

```go title="Go" lines theme={null}
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	body, _ := json.Marshal(map[string]any{
		"model": "openai/gpt-5-nano",
		"input": "What is the capital of France?",
	})

	req, _ := http.NewRequest("POST", "https://openrouter.ai/api/v1/responses", bytes.NewReader(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENROUTER_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		log.Fatalf("unexpected status: %s", resp.Status)
	}

	var result struct {
		Output []struct {
			Type    string `json:"type"`
			Content []struct {
				Type string `json:"type"`
				Text string `json:"text"`
			} `json:"content"`
		} `json:"output"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		log.Fatal(err)
	}

	// Get text (simplest pattern)
	text := ""
	for _, item := range result.Output {
		if item.Type == "message" {
			for _, c := range item.Content {
				if c.Type == "output_text" {
					text += c.Text
				}
			}
		}
	}
	fmt.Println(text) // "The capital of France is Paris."
}

```

```bash title="cURL" lines theme={null}
curl -s https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-5-nano",
    "input": "What is the capital of France?"
  }' | jq -r '[.output[] | select(.type == "message") | .content[] | select(.type == "output_text") | .text] | join("")'

```

```text title="Output" theme={null}
Paris.
```

## Consumption Patterns

callModel returns a `ModelResult` object that provides multiple ways to consume the response:

### Text Methods

```typescript lines theme={null}
// Get just the text content
const text = await result.getText();

// Get the full response with usage data
const response = await result.getResponse();
console.log(response.usage); // { inputTokens, outputTokens, cachedTokens }
```

```python title="Python" lines theme={null}
import asyncio
import os
from openrouter_agent import OpenRouter, call_model


async def main() -> None:
    client = OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"])

    result = call_model(
        client,
        {
            "model": "openai/gpt-5-nano",
            "input": "What is the capital of France?",
        },
    )

    # Get just the text content
    text = await result.get_text()
    print(text)

    # Get the full response with usage data
    response = await result.get_response()
    print(response.usage)  # input_tokens, output_tokens, input_tokens_details.cached_tokens


asyncio.run(main())

```

```go title="Go" lines theme={null}
// Decode the quick start response into a type that also keeps usage.
// resp is the response from the quick start, after its status check.
var result struct {
	Output []struct {
		Type    string `json:"type"`
		Content []struct {
			Type string `json:"type"`
			Text string `json:"text"`
		} `json:"content"`
	} `json:"output"`
	Usage json.RawMessage `json:"usage"`
}
if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
	log.Fatal(err)
}

// Get just the text content
text := ""
for _, item := range result.Output {
	if item.Type == "message" {
		for _, c := range item.Content {
			if c.Type == "output_text" {
				text += c.Text
			}
		}
	}
}
fmt.Println(text)

// Get the full response with usage data
fmt.Println(string(result.Usage)) // { input_tokens, output_tokens, input_tokens_details: { cached_tokens } }
```

```bash title="cURL" lines theme={null}
response=$(curl -s https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-5-nano", "input": "What is the capital of France?"}')

# Get just the text content
text=$(jq -r '[.output[] | select(.type == "message") | .content[] | select(.type == "output_text") | .text] | join("")' <<<"$response")
echo "$text"

# Get the full response with usage data
jq '.usage' <<<"$response" # { input_tokens, output_tokens, ... }

```

```text title="Output" theme={null}
Paris. If you’d like more details about Paris (history, landmarks, etc.), I can share them.
input_tokens=13 input_tokens_details=InputTokensDetails(cached_tokens=0, cache_write_tokens=Unset()) output_tokens=141 output_tokens_details=OutputTokensDetails(reasoning_tokens=64) total_tokens=154 cost=5.705e-05 cost_details=UsageCostDetails(upstream_inference_input_cost=6.5e-07, upstream_inference_output_cost=5.64e-05, upstream_inference_cost=5.705e-05) is_byok=False server_tool_use_details=Unset()
```

### Streaming Methods

```typescript lines theme={null}
// Stream text deltas
for await (const delta of result.getTextStream()) {
  process.stdout.write(delta);
}

// Stream reasoning (for reasoning models)
for await (const delta of result.getReasoningStream()) {
  console.log('Reasoning:', delta);
}

// Stream complete items by ID (recommended)
for await (const item of result.getItemsStream()) {
  console.log('Item update:', item.type, item.id);
}

// Stream all events (including tool preliminary results)
for await (const event of result.getFullResponsesStream()) {
  console.log('Event:', event.type);
}
```

```python title="Python" lines theme={null}
import asyncio
import os
from openrouter_agent import OpenRouter, call_model


async def main() -> None:
    client = OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"])

    result = call_model(
        client,
        {
            "model": "openai/gpt-5-nano",
            "input": "What is the capital of France?",
        },
    )

    # Stream text deltas
    async for delta in result.get_text_stream():
        print(delta, end="", flush=True)
    print()

    # Stream reasoning (for reasoning models)
    async for delta in result.get_reasoning_stream():
        print("Reasoning:", delta)

    # Stream complete items by ID (recommended)
    async for item in result.get_items_stream():
        print("Item update:", item.type, item.id)

    # Stream all events (including tool preliminary results)
    # Agent events (e.g. turn.start) are dicts; API events are typed models
    async for event in result.get_full_responses_stream():
        event_type = event["type"] if isinstance(event, dict) else event.type
        print("Event:", event_type)


asyncio.run(main())

```

```go title="Go" lines theme={null}
package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

type Event struct {
	Type  string `json:"type"`
	Delta string `json:"delta"`
	Item  *struct {
		Type string `json:"type"`
		ID   string `json:"id"`
	} `json:"item"`
}

func main() {
	// Set "stream" to true to receive server-sent events
	body, _ := json.Marshal(map[string]any{
		"model":  "openai/gpt-5-nano",
		"input":  "What is the capital of France?",
		"stream": true,
	})

	req, _ := http.NewRequest("POST", "https://openrouter.ai/api/v1/responses", bytes.NewReader(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENROUTER_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		log.Fatalf("unexpected status: %s", resp.Status)
	}

	// Each event arrives as a "data: {json}" line; handle it as soon as it is read
	scanner := bufio.NewScanner(resp.Body)
	scanner.Buffer(make([]byte, 0, 64*1024), 1024*1024)
	for scanner.Scan() {
		data, ok := strings.CutPrefix(scanner.Text(), "data: ")
		if !ok || data == "[DONE]" {
			continue
		}

		var e Event
		if err := json.Unmarshal([]byte(data), &e); err != nil {
			log.Fatal(err)
		}

		switch e.Type {
		case "response.output_text.delta":
			fmt.Print(e.Delta)
		case "response.reasoning_text.delta": // reasoning models only
			fmt.Println("Reasoning:", e.Delta)
		}

		if e.Item != nil {
			fmt.Fprintln(os.Stderr, "Item update:", e.Item.Type, e.Item.ID)
		}
		fmt.Fprintln(os.Stderr, "Event:", e.Type)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println()
}
```

```text title="Output" theme={null}
Paris
Item update: reasoning rs_06f1215a9189bd99016afcb5617d4887d1a74a3eb14886de2d
Item update: message msg_tmp_6h9qz4yakan
Event: turn.start
Event: response.created
Event: response.in_progress
Event: response.output_item.added
Event: response.output_item.done
Event: response.output_item.added
Event: response.content_part.added
Event: response.output_text.delta
Event: response.output_text.done
Event: response.content_part.done
Event: response.output_item.done
Event: response.completed
Event: turn.end
```

### Tool Methods

```typescript lines theme={null}
// Get all tool calls from the response
const toolCalls = await result.getToolCalls();

// Stream tool calls as they complete
for await (const toolCall of result.getToolCallsStream()) {
  console.log(`Tool: ${toolCall.name}`, toolCall.arguments);
}

// Stream tool deltas and preliminary results
for await (const event of result.getToolStream()) {
  if (event.type === 'delta') {
    process.stdout.write(event.content);
  } else if (event.type === 'preliminary_result') {
    console.log('Progress:', event.result);
  }
}
```

```python title="Python" lines theme={null}
import asyncio
import json
import os
from pydantic import BaseModel
from openrouter_agent import OpenRouter, call_model, tool


class WeatherInput(BaseModel):
    location: str


class WeatherOutput(BaseModel):
    temperature: int
    condition: str
    location: str


async def main() -> None:
    client = OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"])

    weather_tool = tool(
        name="get_weather",
        description="Get the current weather for a location",
        input_schema=WeatherInput,
        output_schema=WeatherOutput,
        execute=lambda params, ctx: WeatherOutput(
            temperature=72, condition="sunny", location=params.location
        ),
    )

    result = call_model(
        client,
        {
            "model": "openai/gpt-5-nano",
            "input": "What is the weather in San Francisco?",
            "tools": [weather_tool],
        },
    )

    # Get all tool calls from the response
    tool_calls = await result.get_tool_calls()

    # Stream tool calls as they complete
    async for tool_call in result.get_tool_calls_stream():
        print(f"Tool: {tool_call.name}", tool_call.arguments)

    # Stream tool deltas and preliminary results
    async for event in result.get_tool_stream():
        if event["type"] == "delta":
            print(event["content"], end="", flush=True)
        elif event["type"] == "preliminary_result":
            print("Progress:", event["result"])
    print()

    print(
        "Tool calls:",
        json.dumps(
            [
                {"id": c.id, "name": c.name, "arguments": c.arguments}
                for c in tool_calls
            ],
            indent=2,
            default=str,
        ),
    )
    print("Final text:", await result.get_text())


asyncio.run(main())

```

```go title="Go" lines theme={null}
// Describe the tool in the request body, then send it as in the quick start.
// Over raw HTTP the API returns the function call; running the tool is up to your code.
body, _ := json.Marshal(map[string]any{
	"model": "openai/gpt-5-nano",
	"input": "What is the weather in San Francisco?",
	"tools": []map[string]any{{
		"type":        "function",
		"name":        "get_weather",
		"description": "Get the current weather for a location",
		"parameters": map[string]any{
			"type":       "object",
			"properties": map[string]any{"location": map[string]any{"type": "string"}},
			"required":   []string{"location"},
		},
	}},
})

// Decode the response into a type that keeps the function call fields
type OutputItem struct {
	Type      string `json:"type"`
	Name      string `json:"name"`
	Arguments string `json:"arguments"`
}
var result struct {
	Output []OutputItem `json:"output"`
}
if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
	log.Fatal(err)
}

// Get all tool calls from the response
for _, item := range result.Output {
	if item.Type == "function_call" {
		fmt.Println("Tool:", item.Name, item.Arguments)
	}
}
```

The Go tab is a fragment: it replaces the request body and the decoding step of the Go quick start, and reads tool calls from a non-streaming response. To stream them over raw HTTP, set `"stream": true` and read events as in the Go streaming example above: a `response.output_item.done` event whose item has type `function_call` carries a completed tool call, and `response.function_call_arguments.delta` events carry argument deltas.

```text title="Output" theme={null}
Tool: get_weather {'location': 'San Francisco'}
Tool: get_weather {'location': 'San Francisco'}
{"location":"San Francisco"}
Tool calls: [
  {
    "id": "call_4Q3SfQPSSX1rPLH4Iq7idUM7",
    "name": "get_weather",
    "arguments": {
      "location": "San Francisco"
    }
  }
]
Final text: Currently in San Francisco: sunny, about 72°F. Want a forecast or more details (humidity, wind, etc.)?
```

## Input Formats

callModel accepts multiple input formats:

```typescript lines theme={null}
// Simple string
const result1 = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: 'Hello!',
});

// Message array (OpenResponses format)
const result2 = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  input: [
    { role: 'user', content: 'Hello!' },
  ],
});

// With system instructions
const result3 = openrouter.callModel({
  model: 'openai/gpt-5-nano',
  instructions: 'You are a helpful assistant.',
  input: 'Hello!',
});
```

```python title="Python" lines theme={null}
# Simple string
result1 = call_model(client, {
    "model": "openai/gpt-5-nano",
    "input": "Hello!",
})

# Message array (OpenResponses format)
result2 = call_model(client, {
    "model": "openai/gpt-5-nano",
    "input": [
        {"role": "user", "content": "Hello!"},
    ],
})

# With system instructions
result3 = call_model(client, {
    "model": "openai/gpt-5-nano",
    "instructions": "You are a helpful assistant.",
    "input": "Hello!",
})

```

```go title="Go" lines theme={null}
// Each map is a request body: pass it to json.Marshal in place of the body in the quick start.

// Simple string
input1 := map[string]any{
	"model": "openai/gpt-5-nano",
	"input": "Hello!",
}

// Message array (OpenResponses format)
input2 := map[string]any{
	"model": "openai/gpt-5-nano",
	"input": []map[string]any{
		{"role": "user", "content": "Hello!"},
	},
}

// With system instructions
input3 := map[string]any{
	"model":        "openai/gpt-5-nano",
	"instructions": "You are a helpful assistant.",
	"input":        "Hello!",
}
```

```bash title="cURL" lines theme={null}
# Simple string
result1=$(curl -s https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-5-nano", "input": "Hello!"}')

# Message array (OpenResponses format)
result2=$(curl -s https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-5-nano", "input": [{"role": "user", "content": "Hello!"}]}')

# With system instructions
result3=$(curl -s https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-5-nano", "instructions": "You are a helpful assistant.", "input": "Hello!"}')
```

## What's Next?

Explore the guides to learn more about specific features:

* **[Working with Items](https://openrouter.ai/docs/agent-sdk/call-model/items.md)** - Understand the items-based streaming paradigm
* **[Text Generation](https://openrouter.ai/docs/agent-sdk/call-model/text-generation.md)** - Input formats, model selection, and response handling
* **[Streaming](https://openrouter.ai/docs/agent-sdk/call-model/streaming.md)** - All streaming methods and patterns
* **[Tools](https://openrouter.ai/docs/agent-sdk/call-model/tools.md)** - Creating typed tools with Zod schemas and multi-turn orchestration
* **[Lifecycle Hooks](https://openrouter.ai/docs/agent-sdk/call-model/lifecycle-hooks.md)** - Observe and control tools, prompts, approvals, sessions, and model calls
* **[nextTurnParams](https://openrouter.ai/docs/agent-sdk/call-model/next-turn-params.md)** - Tool-driven context injection for skills and plugins
* **[Message Formats](https://openrouter.ai/docs/agent-sdk/call-model/message-formats.md)** - Converting to/from OpenAI and Claude formats
* **[Dynamic Parameters](https://openrouter.ai/docs/agent-sdk/call-model/dynamic-parameters.md)** - Async functions for adaptive behavior
* **[Stop Conditions](https://openrouter.ai/docs/agent-sdk/call-model/stop-conditions.md)** - Intelligent execution control
* **[API Reference](https://openrouter.ai/docs/agent-sdk/call-model/api-reference.md)** - Complete type definitions and method signatures

### Example Tools

Ready-to-use tool implementations:

* **[Weather Tool](https://openrouter.ai/docs/agent-sdk/call-model/examples/weather-tool.md)** - Basic API integration
* **[Skills Loader](https://openrouter.ai/docs/agent-sdk/call-model/examples/skills-loader.md)** - Claude Code skills pattern

