---
title: "Quickstart: Build a Chat App"
source: https://openrouter.ai/docs/cookbook/get-started/quickstart.md
path: docs/cookbook/get-started/quickstart
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart: Build a Chat App

> Send your first message and stream a response with the OpenRouter SDK

**Goal:** Learn the fundamentals of OpenRouter by building a TypeScript chat app that sends messages and streams responses through OpenRouter.

**Outcome:** A working multi-turn conversation loop that can talk to any of the 600+ models available on the platform by changing a single string.

> [!TIP]
>
> Want to get started faster? Copy this prompt into your coding agent.

## Prerequisites

* **Node.js 18+** installed
* An **OpenRouter API key**. Create one at [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys) or set up a new [Stripe project](https://openrouter.ai/docs/guides/overview/stripe-projects.md)

## 1. Create a project and install the SDK

Set up a new Node.js project and add the OpenRouter client SDK. The SDK is ESM-only, so set the package type to `module`. Install `tsx` so you can run the TypeScript examples directly.

```bash lines theme={null}
mkdir openrouter-chat && cd openrouter-chat
npm init -y
npm pkg set type=module
npm install @openrouter/sdk
npm install --save-dev tsx
```

## 2. Send your first message

Create `chat.ts` with a client instance and a single [Responses API](https://openrouter.ai/docs/api_reference/responses/overview.md) request. The `apiKey` reads from the environment so you never hard-code credentials.

```typescript lines theme={null}
import { OpenRouter } from '@openrouter/sdk';

const client = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const response = await client.responses.send({
  responsesRequest: {
    model: 'google/gemini-3.1-flash-lite',
    input: 'Say hello in one sentence.',
  },
});

if (!('output' in response)) {
  throw new Error('Expected a non-streaming response');
}

const message = [...response.output].reverse().find((item) => item.type === 'message');
const text = message?.content.find((part) => part.type === 'output_text');
console.log(text?.text);
console.log({
  inputTokens: response.usage?.inputTokens,
  outputTokens: response.usage?.outputTokens,
});
```

```python title="Python" lines theme={null}
import os
from openrouter import OpenRouter

with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
    response = client.responses.send(
        model="google/gemini-3.1-flash-lite",
        input="Say hello in one sentence.",
        stream=False,
    )

message = next((item for item in reversed(response.output) if item.type == "message"), None)
text = next((part for part in message.content if part.type == "output_text"), None) if message else None
print(text.text if text else None)
print({
    "input_tokens": response.usage.input_tokens if response.usage else None,
    "output_tokens": response.usage.output_tokens if response.usage else None,
})

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
		"model": "google/gemini-3.1-flash-lite",
		"input": "Say hello in one sentence.",
	})
	req, _ := http.NewRequest("POST", "https://openrouter.ai/api/v1/responses", bytes.NewReader(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENROUTER_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != http.StatusOK {
		log.Fatalf("request failed: %s", res.Status)
	}

	var response struct {
		Output []struct {
			Type    string
			Content []struct{ Type, Text string }
		}
		Usage struct {
			InputTokens  int `json:"input_tokens"`
			OutputTokens int `json:"output_tokens"`
		}
	}
	if err := json.NewDecoder(res.Body).Decode(&response); err != nil {
		log.Fatal(err)
	}

	for i := len(response.Output) - 1; i >= 0; i-- {
		if response.Output[i].Type != "message" {
			continue
		}
		for _, part := range response.Output[i].Content {
			if part.Type == "output_text" {
				fmt.Println(part.Text)
				break
			}
		}
		break
	}
	fmt.Printf("{inputTokens: %d, outputTokens: %d}\n", response.Usage.InputTokens, response.Usage.OutputTokens)
}

```

```bash title="cURL" lines theme={null}
curl -sS https://openrouter.ai/api/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
    "model": "google/gemini-3.1-flash-lite",
    "input": "Say hello in one sentence."
  }' | jq -r '
    ([.output[] | select(.type == "message")] | last | .content[] | select(.type == "output_text") | .text),
    {inputTokens: .usage.input_tokens, outputTokens: .usage.output_tokens}'

```

```text title="Output" theme={null}
Hello, it is a pleasure to meet you!
{
  inputTokens: 6,
  outputTokens: 10,
}
```

Run it with your API key:

```bash lines theme={null}
OPENROUTER_API_KEY=sk-or-v1-... npx tsx chat.ts
```

To run the Python tab instead, install the Python SDK, save the example as `chat.py`, and run it:

```bash lines theme={null}
pip install openrouter
OPENROUTER_API_KEY=sk-or-v1-... python chat.py
```

You should see a single text response printed to the console. The text is in the `output_text` part of the `message` item in `response.output`, and the SDK returns token usage in camelCase fields such as `inputTokens` and `outputTokens`. The `response.output` array follows the same shape as the [Responses API response](https://openrouter.ai/docs/api/api-reference/responses/create-a-response.md). Without `stream: true`, `client.responses.send` is typed to return the full response, so the `'output' in response` check is only a runtime safety guard.

## 3. Stream the response

Streaming returns text as it is generated instead of waiting for the full response. Pass `stream: true` and iterate over the returned event stream. Each `response.output_text.delta` event contains a `delta` with the new text fragment.

```typescript expandable lines theme={null}
import { OpenRouter } from '@openrouter/sdk';

const client = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const stream = await client.responses.send({
  responsesRequest: {
    model: 'google/gemini-3.1-flash-lite',
    input: 'Explain how routers work in three sentences.',
    stream: true,
  },
});

if ('output' in stream) {
  throw new Error('Expected a streaming response');
}

for await (const event of stream) {
  if (event.type === 'response.output_text.delta') {
    process.stdout.write(event.delta);
  }
}
console.log();
```

```python title="Python" lines theme={null}
import os
from openrouter import OpenRouter

with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
    stream = client.responses.send(
        model="google/gemini-3.1-flash-lite",
        input="Explain how routers work in three sentences.",
        stream=True,
    )

    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
    print()

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

func main() {
	body, _ := json.Marshal(map[string]any{
		"model":  "google/gemini-3.1-flash-lite",
		"input":  "Explain how routers work in three sentences.",
		"stream": true,
	})
	req, _ := http.NewRequest("POST", "https://openrouter.ai/api/v1/responses", bytes.NewReader(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENROUTER_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != http.StatusOK {
		log.Fatalf("request failed: %s", res.Status)
	}

	scanner := bufio.NewScanner(res.Body)
	scanner.Buffer(make([]byte, 1024*1024), 1024*1024)
	for scanner.Scan() {
		data, ok := strings.CutPrefix(scanner.Text(), "data: ")
		if !ok || data == "[DONE]" {
			continue
		}
		var event struct{ Type, Delta string }
		if json.Unmarshal([]byte(data), &event) == nil && event.Type == "response.output_text.delta" {
			fmt.Print(event.Delta)
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println()
}

```

```bash title="cURL" lines theme={null}
curl -sSN https://openrouter.ai/api/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
    "model": "google/gemini-3.1-flash-lite",
    "input": "Explain how routers work in three sentences.",
    "stream": true
  }' | jq --unbuffered -Rrj '
    ltrimstr("data: ") | fromjson? | select(.type == "response.output_text.delta") | .delta'
echo
```

```text title="Output" theme={null}
Routers act as traffic directors for data by connecting multiple networks and determining the most efficient path for information to travel between them. When a data packet arrives, the router inspects its destination IP address and consults a stored routing table to decide which network interface should receive it next. By constantly updating these paths, routers ensure that data packets reach their intended destination across the internet or within a local network.
```

Text now prints incrementally. See the [Streaming reference](https://openrouter.ai/docs/api_reference/streaming.md) for the full SSE event format.

## 4. Add multi-turn conversation

Multi-turn works by sending the full conversation history with each request. The model uses all previous turns as context. Append each user input and assistant response to an `input` array of `{ role, content }` items before the next call.

```typescript expandable lines theme={null}
import { OpenRouter } from '@openrouter/sdk';

const client = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const input: { role: 'user' | 'assistant'; content: string }[] = [];

// Each user turn is appended to the history; the model sees all previous turns.
const turns = [
  'My name is Ada. Say hello to me in one sentence.',
  'What is my name?',
];

for (const line of turns) {
  console.log(`You: ${line}`);
  input.push({ role: 'user', content: line });

  const stream = await client.responses.send({
    responsesRequest: {
      model: 'google/gemini-3.1-flash-lite',
      input,
      stream: true,
    },
  });
  if ('output' in stream) {
    throw new Error('Expected a streaming response');
  }

  let response = '';
  let completed = false;
  process.stdout.write('Assistant: ');
  for await (const event of stream) {
    if (event.type === 'response.output_text.delta') {
      process.stdout.write(event.delta);
      response += event.delta;
    }
    if (event.type === 'response.completed') {
      completed = true;
    }
  }
  console.log();

  // A stream that ends with response.failed or response.incomplete leaves a
  // partial answer; keep only completed turns in the history.
  if (completed) {
    input.push({ role: 'assistant', content: response });
  } else {
    input.pop();
    console.log('(The response did not complete, so that turn was not saved.)');
  }
}

```

```python title="Python" lines theme={null}
import os
from openrouter import OpenRouter

input = []

# Each user turn is appended to the history; the model sees all previous turns.
turns = [
    "My name is Ada. Say hello to me in one sentence.",
    "What is my name?",
]

with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as client:
    for line in turns:
        print(f"You: {line}")
        input.append({"role": "user", "content": line})

        stream = client.responses.send(
            model="google/gemini-3.1-flash-lite",
            input=input,
            stream=True,
        )

        response = ""
        completed = False
        print("Assistant: ", end="", flush=True)
        for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
                response += event.delta
            if event.type == "response.completed":
                completed = True
        print()

        # A stream that ends with response.failed or response.incomplete leaves a
        # partial answer; keep only completed turns in the history.
        if completed:
            input.append({"role": "assistant", "content": response})
        else:
            input.pop()
            print("(The response did not complete, so that turn was not saved.)")

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

type message struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

func main() {
	var input []message

	// Each user turn is appended to the history; the model sees all previous turns.
	turns := []string{
		"My name is Ada. Say hello to me in one sentence.",
		"What is my name?",
	}

	for _, line := range turns {
		fmt.Printf("You: %s\n", line)
		input = append(input, message{Role: "user", Content: line})

		body, _ := json.Marshal(map[string]any{
			"model":  "google/gemini-3.1-flash-lite",
			"input":  input,
			"stream": true,
		})
		req, _ := http.NewRequest("POST", "https://openrouter.ai/api/v1/responses", bytes.NewReader(body))
		req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENROUTER_API_KEY"))
		req.Header.Set("Content-Type", "application/json")

		res, err := http.DefaultClient.Do(req)
		if err != nil {
			log.Fatal(err)
		}
		if res.StatusCode != http.StatusOK {
			log.Fatalf("request failed: %s", res.Status)
		}

		var response strings.Builder
		completed := false
		fmt.Print("Assistant: ")
		scanner := bufio.NewScanner(res.Body)
		scanner.Buffer(make([]byte, 1024*1024), 1024*1024)
		for scanner.Scan() {
			data, ok := strings.CutPrefix(scanner.Text(), "data: ")
			if !ok || data == "[DONE]" {
				continue
			}
			var event struct{ Type, Delta string }
			if json.Unmarshal([]byte(data), &event) != nil {
				continue
			}
			switch event.Type {
			case "response.output_text.delta":
				fmt.Print(event.Delta)
				response.WriteString(event.Delta)
			case "response.completed":
				completed = true
			}
		}
		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}
		res.Body.Close()
		fmt.Println()

		// A stream that ends with response.failed or response.incomplete leaves a
		// partial answer; keep only completed turns in the history.
		if completed {
			input = append(input, message{Role: "assistant", Content: response.String()})
		} else {
			input = input[:len(input)-1]
			fmt.Println("(The response did not complete, so that turn was not saved.)")
		}
	}
}

```

```bash title="cURL" lines theme={null}
input='[]'
events=$(mktemp)

# Each user turn is appended to the history; the model sees all previous turns.
for line in 'My name is Ada. Say hello to me in one sentence.' 'What is my name?'; do
  echo "You: $line"
  input=$(jq -c --arg c "$line" '. + [{role: "user", content: $c}]' <<< "$input")

  printf 'Assistant: '
  curl -sSN https://openrouter.ai/api/v1/responses \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -d "$(jq -n --argjson input "$input" \
      '{model: "google/gemini-3.1-flash-lite", input: $input, stream: true}')" \
    | tee "$events" | jq --unbuffered -Rrj '
      ltrimstr("data: ") | fromjson? | select(.type == "response.output_text.delta") | .delta'
  echo

  # A stream that ends with response.failed or response.incomplete leaves a
  # partial answer; keep only completed turns in the history.
  if jq -Rse 'split("\n") | map(ltrimstr("data: ") | fromjson?) | any(.type == "response.completed")' "$events" > /dev/null; then
    reply=$(jq -Rrj 'ltrimstr("data: ") | fromjson? | select(.type == "response.output_text.delta") | .delta' "$events")
    input=$(jq -c --arg c "$reply" '. + [{role: "assistant", content: $c}]' <<< "$input")
  else
    input=$(jq -c '.[:-1]' <<< "$input")
    echo '(The response did not complete, so that turn was not saved.)'
  fi
done

```

```text title="Output" theme={null}
You: My name is Ada. Say hello to me in one sentence.
Assistant: Hello, Ada, it is a pleasure to meet you!
You: What is my name?
Assistant: Your name is Ada.
```

Run the file. It sends the two fixed prompts in `turns` and exits without reading any input. The second answer shows that the model remembers the first turn, because the full `input` array is sent with each request. To chat interactively, replace the `turns` list with lines read from standard input.

## 5. Swap models

OpenRouter gives you access to hundreds of models through one API. Change the `model` string to switch providers, no other code changes needed.

```typescript lines theme={null}
// Use OpenAI's latest chat model
model: 'openai/gpt-chat-latest',

// Use Anthropic Claude Sonnet latest
model: '~anthropic/claude-sonnet-latest',

// Use a free model
model: 'openrouter/free',
```

```go title="Go" lines theme={null}
// Use OpenAI's latest chat model
"model": "openai/gpt-chat-latest",

// Use Anthropic Claude Sonnet latest
// "model": "~anthropic/claude-sonnet-latest",

// Use a free model
// "model": "openrouter/free",
```

```bash title="cURL" lines theme={null}
# Pick one model string; the rest of the request stays the same.
model='openai/gpt-chat-latest'            # OpenAI's latest chat model
# model='~anthropic/claude-sonnet-latest'  # Anthropic Claude Sonnet latest
# model='openrouter/free'                  # A free model

```

Browse all available models at [openrouter.ai/models](https://openrouter.ai/models) or query the [Models API](https://openrouter.ai/docs/api/api-reference/models/list-all-models-and-their-properties.md) programmatically.

## Check your work

* `npx tsx chat.ts` prints a streamed response to the console
* A multi-turn conversation maintains context across turns (ask a follow-up that references a previous answer)
* Changing the `model` string switches to a different provider with no other code changes
* The non-streaming response includes a `usage` object with `inputTokens` and `outputTokens`

## Next steps

* Connect a [coding agent](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration.md) to OpenRouter
* Explore the [Agent SDK](https://openrouter.ai/docs/agent-sdk/overview.md) for built-in multi-turn loops and tool execution

