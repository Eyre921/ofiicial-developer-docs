---
title: "Workflows as code"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-workflows-as-code.md
path: docs/eleven-agents/customization/agent-workflows-as-code
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Workflows as code

## Overview

A [workflow](/docs/eleven-agents/customization/agent-workflows) is stored as a graph of nodes and edges. Writing that graph by hand means you have to keep edge IDs, `edge_order` lists, and condition objects consistent yourself. The `Workflow` builder in the Python and JavaScript SDKs lets you describe the same graph with chained method calls. It then produces the `workflow` value that `agents.create()` and `agents.update()` already accept.

Use it to:

* Build a workflow in code and review it like any other code change.
* Load an agent's workflow, change one node, and push it back without disturbing the rest of the graph.
* Store workflows as JSON in version control and validate them in CI.

> **Note**
>
> The builder runs entirely in the SDK. It calls no new API endpoints, and anything it builds can be
> opened and edited in the dashboard's visual editor.

## Requirements

* Python: the `elevenlabs` package. The builder is imported from `elevenlabs.agent_workflows`.
* JavaScript: the `@elevenlabs/elevenlabs-js` package. The builder is exported from the package root.

## Build a workflow

The `Workflow` object stands for the start node. Each verb adds a node and returns it, so you can chain the next step from it:

| Python                                 | JavaScript                            | Adds                                                                                     |
| -------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------- |
| `converse(id, prompt, **options)`      | `converse(id, prompt, options?)`      | A subagent node. The agent holds a conversation with `prompt` added to its instructions. |
| `tool(id, tool_ids, **options)`        | `tool(id, toolIds, options?)`         | A dispatch tool node that runs the given tools.                                          |
| `transfer(id, destination, **options)` | `transfer(id, destination, options?)` | A transfer to a phone number, a SIP URI, or another agent.                               |
| `end(id="end")`                        | `end(options?)`                       | An end node. Every `end()` without an ID shares one `"end"` node.                        |

The routing methods decide which edge leads to the next node:

| Python                                | JavaScript                       | Creates                                                                                                                                                    |
| ------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `when(condition)`                     | `when(condition)`                | A conditional edge. A string is an LLM condition; an `Expr` is an expression.                                                                              |
| `on_success()` / `on_failure()`       | `onSuccess()` / `onFailure()`    | An edge from a tool node, taken when the tool call succeeds or fails.                                                                                      |
| `on_result(success=..., failure=...)` | `onResult({ success, failure })` | Both tool result edges at once.                                                                                                                            |
| `go_to(node)`                         | `goTo(node)`                     | An edge to a node that already exists, for merges and loops.                                                                                               |
| `up()`                                | `up()`                           | No edge. Returns the node the current one was chained from, to keep chaining from it. See [Write a workflow as one chain](#write-a-workflow-as-one-chain). |

Verbs called directly on the workflow branch from the start node with an unconditional edge. This example routes callers to an order lookup, retries identification if the lookup fails, and transfers VIP or frustrated callers:

```python
from elevenlabs import ElevenLabs
from elevenlabs.agent_workflows import Destination, Expr, Workflow

elevenlabs = ElevenLabs()

wf = Workflow()

triage = wf.converse("triage", "Greet the caller and find out why they're calling")
identify = triage.when("Caller wants to check an order").converse(
    "identify", "Ask for the order number and the email on the account"
)

lookup = identify.when("Caller gave an order number").tool("lookup_order", ["tool_get_order"])
lookup.on_result(
    success=lambda ok: ok.converse("resolve", "Explain the order status")
        .when("Caller is satisfied")
        .end(),
    failure=lambda failed: failed.go_to(identify),
)

triage.when(Expr.variable("tier").eq("gold")).transfer("vip", Destination.agent("agent_vip"))
triage.when("Caller wants a human").transfer("human", Destination.phone("+15551234567"))

elevenlabs.conversational_ai.agents.update("agent_id", workflow=wf.build())

```

```typescript
import { Destination, ElevenLabsClient, Expr, Workflow } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

const wf = new Workflow();

const triage = wf.converse("triage", "Greet the caller and find out why they're calling");
const identify = triage
  .when("Caller wants to check an order")
  .converse("identify", "Ask for the order number and the email on the account");

const lookup = identify
  .when("Caller gave an order number")
  .tool("lookup_order", ["tool_get_order"]);
lookup.onResult({
  success: (ok) =>
    ok.converse("resolve", "Explain the order status").when("Caller is satisfied").end(),
  failure: (failed) => failed.goTo(identify),
});

triage.when(Expr.variable("tier").eq("gold")).transfer("vip", Destination.agent("agent_vip"));
triage.when("Caller wants a human").transfer("human", Destination.phone("+15551234567"));

await elevenlabs.conversationalAi.agents.update("agent_id", { workflow: wf.build() });
```

`build()` validates the whole graph and returns the request model. It also:

* Gives the start node the ID `start_node`, which the API requires.
* Generates edge IDs in the form `source__target`.
* Fills in each node's `edge_order` in the order you added the edges.
* Positions any node that has no position, so the graph is laid out left to right in the visual editor.

### Write a workflow as one chain

`up()` returns the node the current one was chained from, so you can describe a whole workflow in one expression instead of keeping each node in a variable. Inside a single chain, use `go_to()` / `goTo()` with a node ID, because there is no variable to pass:

```python

wf = Workflow()
(
    wf.converse("triage", "Find out why the customer is calling")
    .when("Caller gave an order number")
    .tool("lookup_order", ["tool_get_order"])
    .on_result(
        success=lambda ok: ok.converse("resolve", "Explain the order status").when("Customer is satisfied").end(),
        failure=lambda failed: failed.go_to("triage"),
    )
    .up()
    .when(Expr.variable("tier").eq("gold"))
    .transfer("vip", Destination.agent("agent_vip_desk"))
)

elevenlabs.conversational_ai.agents.update("agent_id", workflow=wf.build())

```

```typescript
const wf = new Workflow();
wf.converse("triage", "Find out why the customer is calling")
  .when("Caller gave an order number")
  .tool("lookup_order", ["tool_get_order"])
  .onResult({
    success: (ok) =>
      ok.converse("resolve", "Explain the order status").when("Customer is satisfied").end(),
    failure: (failed) => failed.goTo("triage"),
  })
  .up()
  .when(Expr.variable("tier").eq("gold"))
  .transfer("vip", Destination.agent("agent_vip_desk"));

await elevenlabs.conversationalAi.agents.update("agent_id", { workflow: wf.build() });
```

For a node handle from `wf.node(id)`, `up()` returns the node the first edge into it comes from. For the start node, it returns the start node.

### Node options

Optional settings go in keyword arguments in Python and in a trailing options object in JavaScript. Their names match the node's fields in the API:

| Node       | Python                                                                                         | JavaScript                                                                              |
| ---------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `converse` | `label`, `tool_ids`, `knowledge_base`, `conversation_config`, `entry_behavior`                 | `label`, `toolIds`, `knowledgeBase`, `conversationConfig`, `entryBehavior`              |
| `tool`     | `schema_overrides`                                                                             | `schemaOverrides`                                                                       |
| `transfer` | `transfer_type`, `custom_sip_headers`, `post_dial_digits`, `delay_ms`, `transfer_message`, ... | `transferType`, `customSipHeaders`, `postDialDigits`, `delayMs`, `transferMessage`, ... |
| `end`      | `id`                                                                                           | `id`                                                                                    |

Every verb also accepts `position` if you want to place the node yourself. `Workflow(prevent_subagent_loops=True)` in Python, or `new Workflow({ preventSubagentLoops: true })` in JavaScript, stops the conversation from re-entering a subagent it has already visited.

```python
triage = wf.converse(
    "triage",
    "Greet the caller and find out why they're calling",
    label="Triage",
    tool_ids=["tool_crm_search"],
    entry_behavior="generate_immediately",
)

triage.when("Caller is a VIP").transfer(
    "vip_desk",
    Destination.agent("agent_vip_concierge"),
    transfer_message="Connecting you to our VIP team",
    delay_ms=500,
)

identify.when("Caller refuses to share details").end(id="abandoned")
```

```typescript
const triage = wf.converse("triage", "Greet the caller and find out why they're calling", {
  label: "Triage",
  toolIds: ["tool_crm_search"],
  entryBehavior: "generate_immediately",
});

triage.when("Caller is a VIP").transfer("vip_desk", Destination.agent("agent_vip_concierge"), {
  transferMessage: "Connecting you to our VIP team",
  delayMs: 500,
});

identify.when("Caller refuses to share details").end({ id: "abandoned" });
```

### Transfer destinations

| Python                             | JavaScript                        | Transfers to                              |
| ---------------------------------- | --------------------------------- | ----------------------------------------- |
| `Destination.phone(number)`        | `Destination.phone(number)`       | A phone number                            |
| `Destination.phone_variable(name)` | `Destination.phoneVariable(name)` | A phone number held in a dynamic variable |
| `Destination.sip(uri)`             | `Destination.sip(uri)`            | A SIP URI                                 |
| `Destination.sip_variable(name)`   | `Destination.sipVariable(name)`   | A SIP URI held in a dynamic variable      |
| `Destination.agent(agent_id)`      | `Destination.agent(agentId)`      | Another agent                             |

## Conditions

`when()` takes a plain string, a `Condition`, or an `Expr`:

* A string is an LLM condition: the LLM decides whether it holds.
* `Condition.llm(text, label=...)` is the same, with a label shown on the edge in the visual editor. Use `Condition.expr(expr, label=...)` to label an expression.
* An `Expr` is evaluated against [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables), without calling the LLM.

Build expressions from `Expr.variable(name)` and `Expr.literal(value)`. Compare them with `eq`, `neq`, `gt`, `gte`, `lt` and `lte`, and do arithmetic with `add`, `sub`, `mul` and `div`. Combine them with `all_of` / `allOf`, `any_of` / `anyOf` and `if_else` / `ifElse`. Plain values are wrapped in `Expr.literal()` for you. `Expr.llm(description)` asks the LLM to extract a value from the conversation; pass `type` and `enum` to get a string, a number, or one of a fixed set instead of a boolean.

```python
from elevenlabs.agent_workflows import Condition, Expr

is_vip = Expr.any_of(
    Expr.variable("tier").eq("gold"),
    Expr.all_of(Expr.variable("orders").gte(10), Expr.variable("churn_risk").eq(True)),
)
triage.when(Condition.expr(is_vip, label="VIP")).transfer("vip_desk", Destination.agent("agent_vip"))

big_refund = Expr.variable("unit_price").mul(Expr.variable("quantity")).gt(500)
resolve.when(big_refund).transfer("finance", Destination.phone("+15551234567"))

score = Expr.llm("How satisfied the caller sounds, from 1 to 5", type="integer")
resolve.when(score.lte(2)).converse("recovery", "Apologize and offer a discount code")
```

```typescript
import { Condition, Expr } from "@elevenlabs/elevenlabs-js";

const isVip = Expr.anyOf(
  Expr.variable("tier").eq("gold"),
  Expr.allOf(Expr.variable("orders").gte(10), Expr.variable("churn_risk").eq(true))
);

triage
  .when(Condition.expr(isVip, { label: "VIP" }))
  .transfer("vip_desk", Destination.agent("agent_vip"));

const bigRefund = Expr.variable("unit_price").mul(Expr.variable("quantity")).gt(500);
resolve.when(bigRefund).transfer("finance", Destination.phone("+15551234567"));

const score = Expr.llm("How satisfied the caller sounds, from 1 to 5", { type: "integer" });
resolve.when(score.lte(2)).converse("recovery", "Apologize and offer a discount code");
```

## Loops and backward edges

The API allows one edge between any two nodes, in either direction. To let the conversation return the way it came, give the edge a backward condition with `back`:

```python
faq = triage.when("Caller has a general question", back="Question answered").converse(
    "faq", "Answer using the FAQ knowledge base"
)
```

```typescript
const faq = triage
  .when("Caller has a general question", { back: "Question answered" })
  .converse("faq", "Answer using the FAQ knowledge base");
```

`go_to()` / `goTo()` handles the common case for you. When the target node already has an edge leading here, the new edge becomes that edge's backward condition. In the first example, `failed.go_to(identify)` is sent as the backward condition of the `identify` → `lookup_order` edge. Any other second edge between the same two nodes, and any edge from a node to itself, fails validation.

## Edit an existing agent

`Workflow.from_agent()` / `Workflow.fromAgent()` loads the workflow of an agent returned by `agents.get()`. Node IDs, edge IDs, editor positions and edge order are kept, so pushing it back only changes what you changed.

| Python                                  | JavaScript                             | Does                                                               |
| --------------------------------------- | -------------------------------------- | ------------------------------------------------------------------ |
| `wf.node(id)`                           | `wf.node(id)`                          | Returns a handle to an existing node, to edit it or chain from it. |
| `node.update(**fields)`                 | `node.update(fields)`                  | Changes a node's prompt, tools, destination or options.            |
| `wf.insert_between(source, target, fn)` | `wf.insertBetween(source, target, fn)` | Splices new nodes into an existing edge, keeping its condition.    |
| `wf.remove(id)`                         | `wf.remove(id)`                        | Removes a node and every edge to or from it.                       |

`insert_between()` / `insertBetween()` passes your function a branch that carries the replaced edge's condition. The function returns the last node it added, which is then connected to the original target. The method returns that node, or `None` / `undefined` if there is no edge between the two nodes.

```python

agent = elevenlabs.conversational_ai.agents.get("agent_id")
wf = Workflow.from_agent(agent)

wf.node("resolve").update(prompt="Explain the status, then offer a discount code")

verify = wf.insert_between(
    "identify",
    "lookup_order",
    lambda start: start.converse("verify", "Verify the caller's identity with a one-time code"),
)

if verify is not None:
    verify.when("Caller can't verify").end(id="unverified")

wf.remove("vip")

elevenlabs.conversational_ai.agents.update("agent_id", workflow=wf.build())
```

```typescript
const agent = await elevenlabs.conversationalAi.agents.get("agent_id");
const wf = Workflow.fromAgent(agent);

wf.node("resolve").update({ prompt: "Explain the status, then offer a discount code" });

const verify = wf.insertBetween("identify", "lookup_order", (start) =>
  start.converse("verify", "Verify the caller's identity with a one-time code")
);

verify?.when("Caller can't verify").end({ id: "unverified" });

wf.remove("vip");

await elevenlabs.conversationalAi.agents.update("agent_id", { workflow: wf.build() });
```

## Store workflows in version control

`to_json_string()` / `toJSONString()` writes the workflow in the API's wire format: snake_case keys, sorted at every level, with 2-space indentation. It's the same shape the REST API and the [CLI](/docs/eleven-agents/operate/cli) use, and both SDKs write byte-for-byte identical files for the same workflow, so diffs stay small. `Workflow.from_json()` / `Workflow.fromJSON()` reads it back, and also accepts a full agent config with a `workflow` key, such as a file in the CLI's `agent_configs/` directory.

```python
from pathlib import Path

from elevenlabs.agent_workflows import Workflow

Path("workflows/support.json").write_text(wf.to_json_string())

stored = Workflow.from_json(Path("workflows/support.json").read_text())
from_cli = Workflow.from_json(Path("agent_configs/support.json").read_text())
```

```typescript
import { Workflow } from "@elevenlabs/elevenlabs-js";
import { readFile, writeFile } from "node:fs/promises";

await writeFile("workflows/support.json", wf.toJSONString());

const stored = Workflow.fromJSON(await readFile("workflows/support.json", "utf8"));
const fromCli = Workflow.fromJSON(await readFile("agent_configs/support.json", "utf8"));
```

A typical setup:

#### Seed the file

Load the agent with `from_agent()` / `fromAgent()` and write it out, or pull it with `elevenlabs
    agents pull`.

#### Edit

Change the JSON directly, or load it with `from_json()` / `fromJSON()` and edit it with the
builder in a script.

#### Validate in CI

Run `Workflow.from_json(file).build()` / `Workflow.fromJSON(file).build()` on every pull
request, and post `elevenlabs agents workflow diagram <file> --format mermaid-md` as a comment so
reviewers can see the graph.

#### Deploy on merge

Push the built workflow with `agents.update()`.

## Visualize a workflow

The [CLI](/docs/eleven-agents/operate/cli) draws a workflow file as a flowchart, so you can check what your code built without opening the dashboard. It accepts a bare workflow file written by `to_json_string()` / `toJSONString()`, or an agent config with a `workflow` key:

```bash
elevenlabs agents workflow diagram workflows/support.json
```

By default it draws boxes and arrows in the terminal, with each edge condition numbered on its edge and written out in a legend underneath. Use `--format mermaid` to print [Mermaid](https://mermaid.js.org/) source instead, or `--format mermaid-md` to wrap it in a fenced code block that GitHub renders, for example in a pull request comment:

```bash
elevenlabs agents workflow diagram workflows/support.json --format mermaid-md
```

The command reads local files only, so it needs no API key and can run in CI.

## Validation

Chained calls never fail on their own. `build()`, `to_json()` / `toJSON()` and `to_json_string()` / `toJSONString()` check the whole graph and raise or throw a single `WorkflowValidationError` whose `issues` list every problem, each with a `code`, a `message` and the `node_id` / `nodeId` it concerns.

```python
from elevenlabs.agent_workflows import WorkflowValidationError

try:
    workflow = wf.build(on_warning=lambda issue: print("warning:", issue.message))
except WorkflowValidationError as err:
    for issue in err.issues:
        print(issue.code, issue.message)
```

```typescript
import { WorkflowValidationError } from "@elevenlabs/elevenlabs-js";

try {
  const workflow = wf.build({ onWarning: (issue) => console.warn(issue.message) });
} catch (err) {
  if (err instanceof WorkflowValidationError) {
    for (const issue of err.issues) console.error(issue.code, issue.message);
  } else {
    throw err;
  }
}
```

Errors include:

* Two edges between the same pair of nodes, or an edge from a node to itself.
* An edge into the start node, or out of an end node.
* An edge from a tool node that isn't a success or failure edge, or a success or failure edge from any other kind of node.
* Two nodes with the same ID, or an edge to a node that doesn't exist.

Nodes that can't be reached from the start node are reported as warnings, through `on_warning` / `onWarning`, and don't stop the build.

## Node types newer than your SDK

A workflow loaded from the API or from a file can contain node types that your SDK version doesn't know yet. They round-trip through `from_json()` / `fromJSON()` and `to_json_string()` / `toJSONString()` unchanged, and `build()` reports each one as a warning. The typed request model can't carry them, so upgrade the SDK, or send the wire format directly:

```python
elevenlabs.conversational_ai.agents.update(
    "agent_id",
    request_options={"additional_body_parameters": {"workflow": wf.to_json()}},
)
```

```typescript
await elevenlabs.conversationalAi.agents.update(
  "agent_id",
  {},
  { additionalBodyParameters: { workflow: wf.toJSON() } }
);
```
