---
title: "Delegate Routine Work to Cheaper Models"
source: https://openrouter.ai/docs/cookbook/building-agents/subagent-server-tool.md
path: docs/cookbook/building-agents/subagent-server-tool
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delegate Routine Work to Cheaper Models

> Use an orchestrator for planning and a cheap subagent worker for each subtask

**Goal:** Add a task-delegation pattern where a large orchestrator model fans out routine subtasks to a smaller, cheaper worker model via the `openrouter:subagent` server tool.

**Outcome:** Your app sends complex tasks to an orchestrator that automatically delegates focused work (summarization, extraction, reformatting, drafting) to a cheap worker, cutting token cost on bulk generation while keeping planning quality high.

> [!TIP]
>
> Want your coding agent to add this workflow to your app? Copy this prompt.

> [!WARNING]
>
> Subagent is a beta server tool. Each delegated task runs a separate model call, so it adds cost and latency per delegation. This recipe keeps the worker model cheap and caps output tokens. Use returned `usage.cost` when present, or estimate spend from the worker model's current pricing before widening the delegation scope.

## Before you start

You need:

* Node.js 20 or newer
* For the TypeScript SDK samples, the `@openrouter/sdk` and `@openrouter/agent` packages (`npm install @openrouter/sdk @openrouter/agent`)
* For the cURL samples, `jq` to parse responses and stream events
* An OpenRouter API key in `OPENROUTER_API_KEY`
* A workflow that already calls OpenRouter (Chat Completions, Responses, or Agent SDK)
* An orchestrator model that supports tool calling (e.g. `~anthropic/claude-opus-latest`). Check the model's capabilities on the [model page](https://openrouter.ai/models) before choosing.
* A cheaper worker model for subtasks (e.g. `~anthropic/claude-haiku-latest`). Browse [model pricing](https://openrouter.ai/models) to find the cheapest model that meets your quality bar.

Tilde-latest aliases like `~anthropic/claude-haiku-latest` auto-resolve to the newest version in that model family. Find available aliases on each model's page at [/models](https://openrouter.ai/models). You can also use exact slugs (e.g. `anthropic/claude-haiku-5.5`) when you need to pin a specific version.

If you're starting a new TypeScript agent, use the [Agent SDK `callModel` API](https://openrouter.ai/docs/sdks/typescript/call-model/overview) for the orchestrator loop. The samples below use the [Responses API](https://openrouter.ai/docs/api_reference/responses/overview.md) so the server-tool request shape is visible, but the delegation pattern works the same way inside an Agent SDK workflow.

Use these references for exact schemas:

* [Subagent server tool](https://openrouter.ai/docs/guides/features/server-tools/subagent.md)
* [Agent SDK `callModel` overview](https://openrouter.ai/docs/sdks/typescript/call-model/overview)
* [Create a response](https://openrouter.ai/docs/api/api-reference/responses/create-a-response.md)
* [TypeScript SDK Responses reference](https://openrouter.ai/docs/client-sdks/typescript/sdks/responses/README.md)

## What you're building

This recipe adds a task-delegation layer to a multi-step workflow.

The orchestrator model receives a complex request and decides how to break it apart. For each piece that doesn't need its full capability, it calls `openrouter:subagent` with a `task_name` and a `task_description`. The worker executes the task and returns its outcome. The orchestrator integrates all outcomes into the final response.

```text lines theme={null}
Complex request
  → orchestrator plans subtasks
  → routine subtask: orchestrator delegates via subagent
  → worker completes task, returns outcome
  → orchestrator integrates outcomes into final answer
```

The cost split: the orchestrator handles planning and integration (small token budget), while the worker handles bulk generation (cheap per token). A request with 3 delegated subtasks on a 50x cheaper worker model can cut total cost by 80%+ on the generation-heavy portions.

**Why server-side delegation instead of two separate API calls?** You could orchestrate client-side: call the big model, parse its plan, call the small model yourself, feed results back. Server-side subagent collapses that into a single request. The orchestrator invokes workers mid-generation without a round-trip to your server, keeps intermediate prompts private within OpenRouter's agentic loop, and can run multiple delegations in one generation pass. Your app makes one call and gets the integrated answer back.

## 1. Add the subagent tool to your request

The minimal setup: one `openrouter:subagent` entry in the `tools` array with the worker model pinned in `parameters`.

```js title="JavaScript" expandable lines theme={null}
const buildDelegationRequest = ({ task, orchestratorModel, workerModel }) => ({
  model: orchestratorModel,
  instructions:
    "You are a senior orchestrator. Break complex tasks into focused subtasks. " +
    "Delegate routine work (summarization, extraction, reformatting, drafting) " +
    "to the subagent. Include all context the worker needs in task_description — " +
    "it cannot see this conversation. Keep planning and integration for yourself.",
  input: task,
  tools: [
    {
      type: "openrouter:subagent",
      parameters: {
        model: workerModel,
      },
    },
  ],
  tool_choice: "auto",
});

const requestBody = buildDelegationRequest({
  task: "Analyze this API changelog. Summarize each section, list all breaking changes, and draft a migration guide.",
  orchestratorModel: "~anthropic/claude-opus-latest",
  workerModel: "~anthropic/claude-haiku-latest",
});
```

```python title="Python" expandable lines theme={null}
import os
import requests

def build_delegation_request(task, orchestrator_model, worker_model):
    return {
        "model": orchestrator_model,
        "instructions": (
            "You are a senior orchestrator. Break complex tasks into focused subtasks. "
            "Delegate routine work (summarization, extraction, reformatting, drafting) "
            "to the subagent. Include all context the worker needs in task_description "
            "- it cannot see this conversation. Keep planning and integration for yourself."
        ),
        "input": task,
        "tools": [
            {
                "type": "openrouter:subagent",
                "parameters": {"model": worker_model},
            }
        ],
        "tool_choice": "auto",
    }

request_body = build_delegation_request(
    task="Analyze this API changelog. Summarize each section, list all breaking changes, and draft a migration guide.",
    orchestrator_model="~anthropic/claude-opus-latest",
    worker_model="~anthropic/claude-haiku-latest",
)
```

```go title="Go" lines theme={null}
type SubagentTool struct {
	Type       string            `json:"type"`
	Parameters map[string]string `json:"parameters"`
}

type DelegationRequest struct {
	Model        string         `json:"model"`
	Instructions string         `json:"instructions"`
	Input        string         `json:"input"`
	Tools        []SubagentTool `json:"tools"`
	ToolChoice   string         `json:"tool_choice"`
}

func buildDelegationRequest(task, orchestratorModel, workerModel string) DelegationRequest {
	return DelegationRequest{
		Model: orchestratorModel,
		Instructions: "You are a senior orchestrator. Break complex tasks into focused subtasks. " +
			"Delegate routine work (summarization, extraction, reformatting, drafting) " +
			"to the subagent. Include all context the worker needs in task_description — " +
			"it cannot see this conversation. Keep planning and integration for yourself.",
		Input: task,
		Tools: []SubagentTool{
			{
				Type:       "openrouter:subagent",
				Parameters: map[string]string{"model": workerModel},
			},
		},
		ToolChoice: "auto",
	}
}

var requestBody = buildDelegationRequest(
	"Analyze this API changelog. Summarize each section, list all breaking changes, and draft a migration guide.",
	"~anthropic/claude-opus-latest",
	"~anthropic/claude-haiku-latest",
)
```

```bash title="cURL" lines theme={null}
REQUEST_BODY=$(cat <<'EOF'
{
  "model": "~anthropic/claude-opus-latest",
  "instructions": "You are a senior orchestrator. Break complex tasks into focused subtasks. Delegate routine work (summarization, extraction, reformatting, drafting) to the subagent. Include all context the worker needs in task_description — it cannot see this conversation. Keep planning and integration for yourself.",
  "input": "Analyze this API changelog. Summarize each section, list all breaking changes, and draft a migration guide.",
  "tools": [
    {
      "type": "openrouter:subagent",
      "parameters": {
        "model": "~anthropic/claude-haiku-latest"
      }
    }
  ],
  "tool_choice": "auto"
}
EOF
)
```

Wire the request body into your app's existing request path. Here's the shape of the call and response parsing:

```typescript title="TypeScript SDK" lines theme={null}
import { OpenRouter } from "@openrouter/sdk";
import { callModel, serverTool } from "@openrouter/agent";

const client = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY });

// The task refers to "this API changelog", so include the changelog text in the input.
const changelog = `## v3.0.0
### Authentication
- BREAKING: API keys must now be sent in the Authorization header; the ?api_key= query parameter is removed.
### Endpoints
- BREAKING: GET /v2/users is removed; use GET /v3/users (paginated with cursor instead of page).
- Added POST /v3/users/bulk for batch creation.
### Responses
- BREAKING: The created field is renamed to created_at and is now an ISO 8601 string.
- Error responses now include a request_id field.
### Rate limits
- Default limit raised from 60 to 120 requests per minute.`;

// callModel uses camelCase options, so map the fetch-shaped body explicitly.
// The subagent is a server tool: OpenRouter runs it, so there is nothing to execute locally.
const result = callModel(client, {
  model: requestBody.model,
  instructions: requestBody.instructions,
  input: `${requestBody.input}\n\n${changelog}`,
  tools: requestBody.tools.map((t) => serverTool(t)),
  toolChoice: "auto",
});

const answer = await result.getText();
```

```js title="JavaScript (fetch)" lines theme={null}
const sendDelegationRequest = async (body) => {
  const response = await fetch("https://openrouter.ai/api/v1/responses", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.OPENROUTER_API_KEY}`,
    },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`OpenRouter ${response.status}: ${text}`);
  }

  return response.json();
};

const result = await sendDelegationRequest(requestBody);
const message = [...result.output].reverse().find((item) => item.type === "message");
const answer = message?.content.find((part) => part.type === "output_text")?.text;
```

```python title="Python" lines theme={null}
def send_delegation_request(body):
    response = requests.post(
        "https://openrouter.ai/api/v1/responses",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        },
        json=body,
    )
    response.raise_for_status()
    return response.json()

result = send_delegation_request(request_body)
message = next(item for item in reversed(result["output"]) if item["type"] == "message")
answer = next(part["text"] for part in message["content"] if part["type"] == "output_text")
```

```bash title="cURL" lines theme={null}
curl -s https://openrouter.ai/api/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
    "model": "~anthropic/claude-opus-latest",
    "instructions": "You are a senior orchestrator. Delegate routine subtasks to the subagent.",
    "input": "Summarize each section of this changelog and list breaking changes.",
    "tools": [
      {
        "type": "openrouter:subagent",
        "parameters": {"model": "~anthropic/claude-haiku-latest"}
      }
    ],
    "tool_choice": "auto"
  }'
```

```go title="Go" lines theme={null}
// The task refers to "this API changelog", so include the changelog text in the input.
changelog := `## v3.0.0
### Authentication
- BREAKING: API keys must now be sent in the Authorization header; the ?api_key= query parameter is removed.
### Endpoints
- BREAKING: GET /v2/users is removed; use GET /v3/users (paginated with cursor instead of page).
- Added POST /v3/users/bulk for batch creation.
### Responses
- BREAKING: The created field is renamed to created_at and is now an ISO 8601 string.
- Error responses now include a request_id field.
### Rate limits
- Default limit raised from 60 to 120 requests per minute.`

requestBody.Input = requestBody.Input + "\n\n" + changelog

// The subagent is a server tool: OpenRouter runs it, so there is nothing to execute locally.
body, err := json.Marshal(requestBody)
if err != nil {
	log.Fatal(err)
}
req, err := http.NewRequest("POST", "https://openrouter.ai/api/v1/responses", bytes.NewReader(body))
if err != nil {
	log.Fatal(err)
}
req.Header.Set("Authorization", "Bearer "+os.Getenv("OPENROUTER_API_KEY"))
req.Header.Set("Content-Type", "application/json")

resp, err := http.DefaultClient.Do(req)
if err != nil {
	log.Fatal(err)
}
defer resp.Body.Close()
if resp.StatusCode != http.StatusOK {
	b, _ := io.ReadAll(resp.Body)
	log.Fatalf("%s: %s", resp.Status, b)
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

answer := ""
for _, item := range result.Output {
	if item.Type != "message" {
		continue
	}
	for _, c := range item.Content {
		if c.Type == "output_text" {
			answer += c.Text
		}
	}
}
fmt.Println(answer)
```

The response follows the standard [Responses API format](https://openrouter.ai/docs/api_reference/responses/overview.md). Server tools resolve server-side: the orchestrator's subagent calls happen inside OpenRouter's agentic loop, and you don't execute them. The response `output` records each delegation as an `openrouter:subagent` item, followed by a `message` item whose `output_text` part holds the final integrated answer. The `usage` object reflects the combined token spend per [Server tools: Usage Tracking](https://openrouter.ai/docs/guides/features/server-tools.md#usage-tracking).

The orchestrator decides whether and when to delegate. Each delegation passes two arguments:

* `task_name`: a short label (e.g. `summarize-breaking-changes`)
* `task_description`: everything the worker needs, including all context, inputs, and the expected output format

The worker sees only `task_description`. It has no access to the parent conversation, so the orchestrator must be explicit about what it wants back.

## 2. Read the tool result

On success, the subagent returns a JSON result with the worker's output:

```json lines theme={null}
{
  "status": "ok",
  "model": "anthropic/claude-haiku-5.5",
  "task_name": "summarize-breaking-changes",
  "outcome": "Breaking changes in v3.0:\n1. Removed deprecated /v1/legacy endpoint..."
}
```

On failure:

```json lines theme={null}
{
  "status": "error",
  "task_name": "summarize-breaking-changes",
  "error": "Subagent call failed: ..."
}
```

In the response `output`, each delegation appears as an `openrouter:subagent` item with the worker's model, the task, and its outcome:

```json lines theme={null}
{
  "type": "openrouter:subagent",
  "id": "st_tmp_dgy29rn5qvk",
  "status": "completed",
  "model": "anthropic/claude-haiku-5.5",
  "task_name": "summarize-breaking-changes",
  "task_description": "Summarize the breaking changes in this changelog...",
  "outcome": "Breaking changes in v3.0:\n1. Removed deprecated /v1/legacy endpoint...",
  "call_id": "call_xvWTB916fUfn6eNGQfvbvhod"
}
```

The orchestrator receives the result as a tool response and continues generating. It can delegate more tasks, integrate outcomes it already has, or finish the response. Subagent calls are capped per request (see the [reference page](https://openrouter.ai/docs/guides/features/server-tools/subagent.md) for current limits).

## 3. Give the worker its own tools

When a subtask needs external data, pass server tools to the worker. The worker runs as a mini agent over those tools before producing its outcome.

```js expandable lines theme={null}
const requestBody = {
  model: "~anthropic/claude-opus-latest",
  input: "Research competitors mentioned in our Q2 report and draft a competitive analysis.",
  tools: [
    {
      type: "openrouter:subagent",
      parameters: {
        model: "~anthropic/claude-haiku-latest",
        instructions:
          "You are a research assistant. Use web search to find current data. " +
          "Return structured findings with sources.",
        tools: [
          { type: "openrouter:web_search" },
          { type: "openrouter:web_fetch" },
        ],
      },
    },
  ],
};
```

```python title="Python" lines theme={null}
# Include the report text so the worker has the competitor names to research.
q2_report = """Q2 Report (excerpt)
Company: Acme Observability, a SaaS monitoring platform for mid-market engineering teams.
Competitive landscape: We lost deals this quarter mainly to Datadog and New Relic,
and Grafana Labs is increasingly showing up in open-source-leaning accounts."""

request_body = {
    "model": "~anthropic/claude-opus-latest",
    "input": (
        "Research competitors mentioned in our Q2 report and draft a competitive analysis.\n\n"
        + q2_report
    ),
    "tools": [
        {
            "type": "openrouter:subagent",
            "parameters": {
                "model": "~anthropic/claude-haiku-latest",
                "instructions": (
                    "You are a research assistant. Use web search to find current data. "
                    "Return structured findings with sources."
                ),
                "tools": [
                    {"type": "openrouter:web_search"},
                    {"type": "openrouter:web_fetch"},
                ],
            },
        },
    ],
}
```

```go title="Go" lines theme={null}
// The task refers to "our Q2 report", so include the relevant report text in the input.
q2Report := `Q2 Report excerpt (Competitive landscape):
Our main competitors this quarter were Notion, Coda, and Airtable.
- Notion launched new AI features and continued to grow in the SMB segment.
- Coda pushed its enterprise offering with new admin controls.
- Airtable shifted focus toward enterprise app-building.
Our product: a collaborative docs-and-database workspace for mid-market teams.`

requestBody := map[string]any{
	"model": "~anthropic/claude-opus-latest",
	"input": "Research competitors mentioned in our Q2 report and draft a competitive analysis.\n\n" + q2Report,
	"tools": []map[string]any{
		{
			"type": "openrouter:subagent",
			"parameters": map[string]any{
				"model": "~anthropic/claude-haiku-latest",
				"instructions": "You are a research assistant. Use web search to find current data. " +
					"Return structured findings with sources.",
				"tools": []map[string]any{
					{"type": "openrouter:web_search"},
					{"type": "openrouter:web_fetch"},
				},
			},
		},
	},
}
```

```bash title="cURL" lines theme={null}
REQUEST_BODY='{
  "model": "~anthropic/claude-opus-latest",
  "input": "Research the competitors mentioned in this Q2 report excerpt and draft a short competitive analysis.\n\nQ2 report excerpt: We sell a team documentation and wiki product to mid-size software companies. This quarter we lost several enterprise deals to Notion and Coda, and Atlassian Confluence introduced more aggressive pricing for teams under 100 seats.",
  "tools": [
    {
      "type": "openrouter:subagent",
      "parameters": {
        "model": "~anthropic/claude-haiku-latest",
        "instructions": "You are a research assistant. Use web search to find current data. Return structured findings with sources.",
        "tools": [
          {"type": "openrouter:web_search"},
          {"type": "openrouter:web_fetch"}
        ]
      }
    }
  ]
}'
```

The worker's tool use happens inside the subagent call. Only its final text is returned to the orchestrator. The orchestrator never sees the worker's intermediate tool calls or search results, just the finished outcome.

Two constraints on nested tools:

* Only OpenRouter server tools work (e.g. `openrouter:web_search`, `openrouter:web_fetch`, `openrouter:datetime`). Function tools placed in the nested `tools` array are rejected with a `400`. On the Responses API, the subagent can additionally inherit top-level function tools (experimental). See [Inheriting Client Function Tools](https://openrouter.ai/docs/guides/features/server-tools/subagent.md#inheriting-client-function-tools).
* The subagent tool can't list itself. Recursion guards prevent the worker from re-entering the subagent.

## 4. Tune the worker for cost and quality

The subagent's `parameters` let you control how the worker generates. Use them to keep cost predictable.

```js lines theme={null}
const tools = [
  {
    type: "openrouter:subagent",
    parameters: {
      model: "~anthropic/claude-haiku-latest",
      instructions:
        "Complete the task exactly as described. Be concise and structured.",
      max_completion_tokens: 1024,
      temperature: 0.2,
      reasoning: { effort: "low" },
    },
  },
];
```

```python title="Python" lines theme={null}
tools = [
    {
        "type": "openrouter:subagent",
        "parameters": {
            "model": "~anthropic/claude-haiku-latest",
            "instructions": "Complete the task exactly as described. Be concise and structured.",
            "max_completion_tokens": 1024,
            "temperature": 0.2,
            "reasoning": {"effort": "low"},
        },
    },
]
```

```go title="Go" lines theme={null}
tools := []map[string]any{
	{
		"type": "openrouter:subagent",
		"parameters": map[string]any{
			"model":                 "~anthropic/claude-haiku-latest",
			"instructions":          "Complete the task exactly as described. Be concise and structured.",
			"max_completion_tokens": 1024,
			"temperature":           0.2,
			"reasoning":             map[string]any{"effort": "low"},
		},
	},
}
```

```bash title="cURL" lines theme={null}
TOOLS='[
  {
    "type": "openrouter:subagent",
    "parameters": {
      "model": "~anthropic/claude-haiku-latest",
      "instructions": "Complete the task exactly as described. Be concise and structured.",
      "max_completion_tokens": 1024,
      "temperature": 0.2,
      "reasoning": {"effort": "low"}
    }
  }
]'
```

| Parameter | What it controls |
| - | - |
| `model` | The worker model. Pick the cheapest model that can handle the subtask quality you need. |
| `max_completion_tokens` | Output token ceiling (including reasoning). Prevents runaway generation on open-ended tasks. |
| `temperature` | Lower values for deterministic extraction, higher for creative drafting. Range 0 to 2. |
| `reasoning` | `effort` controls reasoning depth. Set to `"low"` for fast, cheap tasks. `max_tokens` sets the upper bound for the worker's reasoning tokens. |
| `instructions` | System prompt for the worker. Shape its output format and behavior. |
| `max_tool_calls` | Range 1 to 25. Ceiling on the worker's own tool-calling loop. |

The full parameter reference is at [Subagent server tool](https://openrouter.ai/docs/guides/features/server-tools/subagent.md).

> [!NOTE]
>
> Subagent works with both non-streaming and streaming requests. With streaming (`stream: true`), the server sends SSE comment lines as heartbeats while workers execute. Text deltas resume once the orchestrator continues generating. The `response.completed` event includes the aggregated `usage` object. See [Server tools overview](https://openrouter.ai/docs/guides/features/server-tools.md) for how server tool usage appears in the response.

With `stream: true`, expect this pattern in the SSE stream:

```text lines theme={null}
data: {"type":"response.output_item.added","item":{"type":"openrouter:subagent",...}}
:                            ← heartbeat comments during worker execution
data: {"type":"response.output_item.done","item":{"type":"openrouter:subagent","outcome":"...",...}}
data: {"type":"response.output_text.delta","delta":"Here"}
data: {"type":"response.output_text.delta","delta":"'s the summary:"}
...text deltas...
data: {"type":"response.completed","response":{...,"usage":{...}}}  ← aggregated usage
data: [DONE]
```

Most SSE client libraries ignore comment lines (lines starting with `:`) automatically. Here's a minimal consumer:

```js expandable lines theme={null}
const response = await fetch("https://openrouter.ai/api/v1/responses", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.OPENROUTER_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    ...buildDelegationRequest({
      task: "Summarize this document...",
      orchestratorModel: "~anthropic/claude-sonnet-latest",
      workerModel: "~anthropic/claude-haiku-latest",
    }),
    stream: true,
  }),
});

const reader = response.body.getReader();
const decoder = new TextDecoder();
let buffer = "";
let completed = false;

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  buffer += decoder.decode(value, { stream: true });

  const lines = buffer.split("\n");
  buffer = lines.pop(); // keep incomplete line in buffer

  let streamDone = false;
  for (const line of lines) {
    if (line.startsWith(":")) continue; // heartbeat comment
    if (!line.startsWith("data: ")) continue;
    const payload = line.slice(6);
    if (payload === "[DONE]") { streamDone = true; break; }
    let event;
    try { event = JSON.parse(payload); } catch { continue; }
    if (event.type === "response.failed") {
      throw new Error(event.response.error?.message ?? "Delegation failed");
    }
    if (event.type === "response.incomplete") {
      throw new Error(
        `Delegation incomplete: ${event.response.incomplete_details?.reason ?? "unknown reason"}`,
      );
    }
    if (event.type === "error") throw new Error(event.message);
    if (event.type === "response.output_text.delta") process.stdout.write(event.delta);
    if (event.type === "response.completed") completed = true;
  }
  if (streamDone) break;
}
// A clean end of stream without response.completed means the summary is partial.
if (!completed) throw new Error("Stream ended before response.completed");
```

```python title="Python" lines theme={null}
import json
import os

import requests

response = requests.post(
    "https://openrouter.ai/api/v1/responses",
    headers={
        "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "model": "~anthropic/claude-sonnet-latest",
        "input": "Summarize this document: OpenRouter provides a unified API for hundreds of AI models, with automatic fallbacks, provider routing, and usage-based pricing.",
        "tools": [
            {
                "type": "openrouter:subagent",
                "parameters": {
                    "model": "~anthropic/claude-haiku-latest",
                    "instructions": "Complete the task exactly as described. Be concise and structured.",
                },
            },
        ],
        "stream": True,
    },
    stream=True,
)
response.raise_for_status()

completed = False
for raw in response.iter_lines(decode_unicode=True):
    if not raw or raw.startswith(":"):  # skip blanks and heartbeat comments
        continue
    if not raw.startswith("data: "):
        continue
    payload = raw[6:]
    if payload == "[DONE]":
        break
    try:
        event = json.loads(payload)
    except json.JSONDecodeError:
        continue
    if event.get("type") == "response.failed":
        error = event["response"].get("error") or {}
        raise RuntimeError(error.get("message", "Delegation failed"))
    if event.get("type") == "response.incomplete":
        details = event["response"].get("incomplete_details") or {}
        raise RuntimeError(f"Delegation incomplete: {details.get('reason', 'unknown reason')}")
    if event.get("type") == "error":
        raise RuntimeError(event.get("message"))
    if event.get("type") == "response.output_text.delta":
        print(event["delta"], end="", flush=True)
    if event.get("type") == "response.completed":
        completed = True
print()
# A clean end of stream without response.completed means the summary is partial.
if not completed:
    raise RuntimeError("Stream ended before response.completed")

```

```go title="Go" lines theme={null}
package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

func main() {
	body, _ := json.Marshal(map[string]any{
		"model": "~anthropic/claude-sonnet-latest",
		"input": "Summarize this document: OpenRouter provides a unified API for hundreds of AI models, with automatic fallbacks, provider routing, and usage-based pricing.",
		"tools": []map[string]any{
			{
				"type": "openrouter:subagent",
				"parameters": map[string]any{
					"model":        "~anthropic/claude-haiku-latest",
					"instructions": "Complete the task exactly as described. Be concise and structured.",
				},
			},
		},
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
		detail, _ := io.ReadAll(resp.Body)
		log.Fatalf("request failed: %s: %s", resp.Status, detail)
	}

	completed := false
	scanner := bufio.NewScanner(resp.Body)
	scanner.Buffer(make([]byte, 1024*1024), 16*1024*1024)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, ":") || !strings.HasPrefix(line, "data: ") {
			continue // heartbeat comment or non-data line
		}
		payload := strings.TrimPrefix(line, "data: ")
		if payload == "[DONE]" {
			break
		}
		var event struct {
			Type     string `json:"type"`
			Delta    string `json:"delta"`
			Message  string `json:"message"`
			Response struct {
				Error             *struct{ Message string } `json:"error"`
				IncompleteDetails *struct{ Reason string }  `json:"incomplete_details"`
			} `json:"response"`
		}
		if json.Unmarshal([]byte(payload), &event) != nil {
			continue
		}
		switch event.Type {
		case "response.failed":
			msg := "Delegation failed"
			if event.Response.Error != nil {
				msg = event.Response.Error.Message
			}
			log.Fatal(msg)
		case "response.incomplete":
			reason := "unknown reason"
			if event.Response.IncompleteDetails != nil {
				reason = event.Response.IncompleteDetails.Reason
			}
			log.Fatal("Delegation incomplete: " + reason)
		case "error":
			log.Fatal(event.Message)
		case "response.output_text.delta":
			fmt.Print(event.Delta)
		case "response.completed":
			completed = true
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println()
	// A clean end of stream without response.completed means the summary is partial.
	if !completed {
		log.Fatal("stream ended before response.completed")
	}
}

```

```bash title="cURL" lines theme={null}
set -o pipefail # a rejected request or a failed stream fails the whole pipeline
command -v jq >/dev/null || { echo "This script needs jq to parse stream events" >&2; exit 1; }

curl -sSfN https://openrouter.ai/api/v1/responses \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "~anthropic/claude-sonnet-latest",
    "input": "Summarize this document: OpenRouter provides a unified API for hundreds of AI models, with automatic fallbacks, provider routing, and usage-based pricing.",
    "tools": [
      {
        "type": "openrouter:subagent",
        "parameters": {
          "model": "~anthropic/claude-haiku-latest",
          "instructions": "Complete the task exactly as described. Be concise and structured."
        }
      }
    ],
    "stream": true
  }' | {
  completed=0
  while IFS= read -r line; do
    line="${line%$'\r'}"
    case "$line" in
      :*) continue ;;                # heartbeat comment
      "data: [DONE]") break ;;
      "data: "*) payload="${line#data: }" ;;
      *) continue ;;
    esac
    type=$(jq -r '.type' <<<"$payload" 2>/dev/null) || continue
    case "$type" in
      response.failed)
        echo "Delegation failed: $(jq -r '.response.error.message // "unknown"' <<<"$payload")" >&2; exit 1 ;;
      response.incomplete)
        echo "Delegation incomplete: $(jq -r '.response.incomplete_details.reason // "unknown reason"' <<<"$payload")" >&2; exit 1 ;;
      error)
        echo "$(jq -r '.message' <<<"$payload")" >&2; exit 1 ;;
      response.output_text.delta)
        jq -j '.delta' <<<"$payload" ;;
      response.completed) completed=1 ;;
    esac
  done
  echo
  # A clean end of stream without response.completed means the summary is partial.
  [ "$completed" = 1 ] || { echo "Stream ended before response.completed" >&2; exit 1; }
}

```

```text title="Output" theme={null}
The document says that OpenRouter offers one API for accessing hundreds of AI models. It includes three main features:

- **Automatic fallbacks:** if a model or provider fails, requests can be rerouted.
- **Provider routing:** requests can be directed to different providers.
- **Usage-based pricing:** you pay for what you use.
```

## 5. Log delegation routing, not task content

Add telemetry where your app already records model calls. Log the routing decision and cost, not the content.

Log:

* `orchestrator_model`
* `worker_model`
* `did_enable_delegation` (whether you configured the subagent tool on this request)
* `status` (and `incomplete_details.reason` when the response is incomplete)
* `usage.input_tokens`, `usage.output_tokens`, `usage.total_tokens`, and `usage.cost` when returned
* route or feature name, such as `delegated_analysis`

Do not log:

* API keys
* cookies
* full task descriptions
* full worker outcomes
* user content (unless your product already has an explicit retention policy)

The `usage` object in the response reflects the combined token spend of the orchestrator plus all worker calls, per [Server tools: Usage Tracking](https://openrouter.ai/docs/guides/features/server-tools.md#usage-tracking). You don't need to track inner costs separately.

```js lines theme={null}
const logDelegation = (response, context) => {
  const usage = response.usage ?? {};
  return {
    orchestrator_model: context.orchestratorModel,
    worker_model: context.workerModel,
    did_enable_delegation: true,
    status: response.status,
    incomplete_reason: response.incomplete_details?.reason,
    usage_input_tokens: usage.input_tokens,
    usage_output_tokens: usage.output_tokens,
    usage_total_tokens: usage.total_tokens,
    usage_cost: usage.cost,
    route: "delegated_analysis",
  };
};
```

```python title="Python" lines theme={null}
def log_delegation(response, context):
    usage = response.get("usage") or {}
    return {
        "orchestrator_model": context["orchestrator_model"],
        "worker_model": context["worker_model"],
        "did_enable_delegation": True,
        "status": response.get("status"),
        "incomplete_reason": (response.get("incomplete_details") or {}).get("reason"),
        "usage_input_tokens": usage.get("input_tokens"),
        "usage_output_tokens": usage.get("output_tokens"),
        "usage_total_tokens": usage.get("total_tokens"),
        "usage_cost": usage.get("cost"),
        "route": "delegated_analysis",
    }

```

```go title="Go" lines theme={null}
type DelegationContext struct {
	OrchestratorModel string
	WorkerModel       string
}

func logDelegation(response map[string]any, ctx DelegationContext) map[string]any {
	usage, _ := response["usage"].(map[string]any)
	entry := map[string]any{
		"orchestrator_model":    ctx.OrchestratorModel,
		"worker_model":          ctx.WorkerModel,
		"did_enable_delegation": true,
		"status":                response["status"],
		"usage_input_tokens":    usage["input_tokens"],
		"usage_output_tokens":   usage["output_tokens"],
		"usage_total_tokens":    usage["total_tokens"],
		"usage_cost":            usage["cost"],
		"route":                 "delegated_analysis",
	}
	if d, ok := response["incomplete_details"].(map[string]any); ok && d["reason"] != nil {
		entry["incomplete_reason"] = d["reason"]
	}
	return entry
}
```

```bash title="cURL" lines theme={null}
log_delegation() {
  local response="$1" orchestrator_model="$2" worker_model="$3"
  jq --arg orchestrator_model "$orchestrator_model" --arg worker_model "$worker_model" '{
    orchestrator_model: $orchestrator_model,
    worker_model: $worker_model,
    did_enable_delegation: true,
    status: .status,
    incomplete_reason: .incomplete_details.reason,
    usage_input_tokens: .usage.input_tokens,
    usage_output_tokens: .usage.output_tokens,
    usage_total_tokens: .usage.total_tokens,
    usage_cost: .usage.cost,
    route: "delegated_analysis"
  } | with_entries(select(.value != null))' <<<"$response"
}
```

## Next steps

* Read the [Subagent reference](https://openrouter.ai/docs/guides/features/server-tools/subagent.md) for exact parameters, recursion guards, worker tool constraints, and invocation caps.
* Pair subagent with [Advisor](https://openrouter.ai/docs/cookbook/building-agents/advisor-server-tool.md) for a two-tier pattern: cheap worker for routine tasks, strong advisor for uncertain decisions.
* Give the worker [Web Search](https://openrouter.ai/docs/guides/features/server-tools/web-search.md) when subtasks need current data.
* Add [Response Caching](https://openrouter.ai/docs/guides/features/response-caching.md) for repeated orchestrator prefixes across similar tasks.
* Use [Fusion](https://openrouter.ai/docs/guides/features/server-tools/fusion.md) when subtasks need multi-model deliberation instead of single-worker execution.
* Browse the [Model list](https://openrouter.ai/models) to compare worker model pricing and find the cheapest model that meets your subtask quality bar.
* Add [Structured Outputs](https://openrouter.ai/docs/structured-outputs.md) to the orchestrator request when you need the final answer in a specific JSON schema.

