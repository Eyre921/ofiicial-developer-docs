---
title: "Structured procedures"
source: https://elevenlabs.io/docs/eleven-agents/customization/procedures/structured-procedures.md
path: docs/eleven-agents/customization/procedures/structured-procedures
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Structured procedures

Structured procedures are currently in Alpha. See details in [Release status](#release-status).

## Overview

A structured procedure is a [procedure](/docs/eleven-agents/customization/procedures) that runs a fixed sequence of steps. A [free-form procedure](/docs/eleven-agents/customization/procedures/free-form-procedures) is natural-language guidance the agent interprets and adapts to the situation. A structured procedure is an ordered list of typed steps the agent runs in order every time the procedure applies.

Use a structured procedure when specific steps must happen the same way on every call: verifying a caller's identity, escalating a ticket, or taking a payment. You author it as a short list of plain-language steps.

Like every procedure, a structured procedure has a trigger that describes when it applies. When a conversation matches the trigger, the agent runs the procedure's steps in order, then returns to the rest of the conversation.

![Structured procedure
editor](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bc996f67b2afad8f1de5abe8febcf8af3766b4f098627b0ae60e0456b3c2703b/assets/images/conversational-ai/procedures/structured-procedure-example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260806%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260806T205829Z&X-Amz-Expires=604800&X-Amz-Signature=7a5ff3231ae92fe63b3662d34326c713caddee89309a0dda00bcc9f5b9278fec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## When to use a structured procedure

Use a structured procedure when specific steps must run the same way every time, but you still want to author quickly in plain steps. For how it compares to free-form procedures, workflows, and the system prompt, see [When to use procedures](/docs/eleven-agents/customization/procedures#when-to-use-procedures).

## Anatomy of a structured procedure

A structured procedure has three parts: a name, a trigger, and an ordered list of steps.

### Name

A short label that identifies the procedure in the dashboard. The name is never sent to the LLM, so it does not affect agent behavior.

### Trigger

A plain-language description of when the agent should run this procedure, for example *When the user asks to refund an order*. The agent compares the user's intent against each procedure's trigger and runs the matching one, so triggers should be concrete and distinct. A trigger works the same way as for any procedure; see [Writing triggers](/docs/eleven-agents/customization/procedures/free-form-procedures#writing-triggers).

### Steps

The procedure body is an ordered list of typed steps. There are multiple step types, and you combine them to describe the task.

| Step              | What it does                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| **Ask**           | Requests information from the user and waits for an appropriate response.        |
| **Tell**          | Has the agent generate a message in its own words from an instruction.           |
| **Say**           | Has the agent speak an exact message word for word.                              |
| **Tool**          | Calls a specific tool or API.                                                    |
| **If**            | Selects the first matching if/else-if arm, or an optional else arm.              |
| **Sub-procedure** | Runs another structured procedure, then returns to the next step.                |
| **System tool**   | Performs a built-in system action. Currently, only ending the call is supported. |
| **Retry**         | Reattempts a failed tool call. Available only inside tool failure handling.      |

![Structured procedure step type
menu](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/14976a6b9979d21fd7c77541a49e7475f8aa0764af4940746d3390804e7c4598/assets/images/conversational-ai/procedures/step_type_menu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260806%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260806T205829Z&X-Amz-Expires=604800&X-Amz-Signature=dccde69aad9139428238d6cdb8fb8c1f991605ef4fd5cd8286293dbaa5b92f2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## API step reference

Structured procedure `content` is a JSON-encoded document containing a `steps` array. Each step is an object identified by its `type`.

### Ask

An Ask step instructs the agent to request information and wait until the user provides an appropriate response.

* API type: `ask`
* `instruction`: Required, non-empty string.

```json focus={1-4}
{
  "type": "ask",
  "instruction": "Ask the user for their order ID."
}
```

### Tell

A Tell step instructs the agent to generate a single message in its own words. Unlike Ask, it does not wait for a user response before continuing.

* API type: `tell`
* `instruction`: Required, non-empty string.

```json focus={1-4}
{
  "type": "tell",
  "instruction": "Explain that the refund normally takes five to ten business days."
}
```

### Say

A Say step speaks the supplied text exactly as written.

* API type: `say`
* `message`: Required, non-empty string.

```json focus={1-4}
{
  "type": "say",
  "message": "Your refund has been submitted."
}
```

### If, else if, and else

An If step contains one or more ordered conditional arms. The first matching arm runs. The optional `fallback` array acts as the else arm.

* API type: `branch`
* `branches`: Required, non-empty list of conditional arms.
* `fallback`: Optional list of else steps.
* Each arm requires a `condition` and a non-empty `steps` list.

```json focus={1-23}
{
  "type": "branch",
  "branches": [
    {
      "condition": {
        "type": "llm",
        "condition": "The user is on an annual plan."
      },
      "steps": [
        {
          "type": "say",
          "message": "Your annual plan is eligible for a prorated refund."
        }
      ]
    }
  ],
  "fallback": [
    {
      "type": "tell",
      "instruction": "Explain that the account's plan could not be determined."
    }
  ]
}
```

This behaves like if/else-if/else:

1. Conditions are evaluated in order.
2. The first matching arm runs.
3. If no condition matches, `fallback` runs.
4. After an arm finishes, the procedure rejoins the main sequence.

The example above uses a natural-language condition. Conditions can also use workflow expressions:

```json focus={1-14}
{
  "type": "expression",
  "expression": {
    "type": "eq_operator",
    "left": {
      "type": "dynamic_variable",
      "name": "plan_tier"
    },
    "right": {
      "type": "string_literal",
      "value": "annual"
    }
  }
}
```

All arms in one If step must use the same condition type: either `llm` or `expression`.

An If step may be the first procedure step. However:

* If steps cannot be nested.
* Two If steps cannot be placed consecutively.
* An expression condition cannot directly follow an Ask step. Use an LLM condition to evaluate a user's free-text response.

### Tool

A Tool step calls a specific tool.

* API type: `tool_call`
* `tool_id`: Required, non-empty tool ID.
* `tool_name`: Required tool name.
* `instruction`: Optional instruction describing how to call the tool.
* `on_failure`: Optional failure handler.

```json focus={1-6}
{
  "type": "tool_call",
  "tool_id": "tool_abc123",
  "tool_name": "lookup_order",
  "instruction": "Look up the order using the order ID provided by the user."
}
```

Without `on_failure`, a failed tool call stops the procedure. Add `on_failure` to handle specific failures, retry the tool, or continue with fallback steps.

* `branches`: Optional list of ordered conditions. The first matching branch runs.
* `fallback`: Required, non-empty list of steps. It runs when no branch matches.

```json focus={1-13}
{
  "type": "tool_call",
  "tool_id": "tool_abc123",
  "tool_name": "lookup_order",
  "on_failure": {
    "fallback": [
      {
        "type": "tell",
        "instruction": "Explain that the order could not be retrieved and offer to connect the user with support."
      }
    ]
  }
}
```

Failure-handler branches may contain Ask, Tell, Say, Sub-procedure, System tool, and Retry steps. They cannot contain Tool or If steps. All conditional branches in one failure handler must use the same condition type.

### Retry

A Retry step reattempts the Tool step whose failure handler contains it.

* API type: `retry`
* `max_retries`: Optional integer from 1 through 3. Defaults to 1.
* The value counts reattempts after the original tool call.
* Retry is valid only inside `on_failure`.
* Retry must be the final step in its failure-handler branch because subsequent steps would be unreachable.
* If all attempts fail, the procedure stops.

```json focus={1-4}
{
  "type": "retry",
  "max_retries": 2
}
```

### Sub-procedure

A Sub-procedure step runs another structured procedure. When it finishes, execution returns to the step after the Sub-procedure step.

* API type: `sub_procedure`
* `procedure_id`: Required, non-empty procedure ID.
* The target must exist on the same agent.
* The target must be a structured procedure.
* A procedure cannot invoke itself.

```json focus={1-4}
{
  "type": "sub_procedure",
  "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3"
}
```

### System tool

A System tool step performs a built-in system action.

* API type: `system_tool`
* `system_tool_name`: Required system-tool name.
* Currently, only `end_call` is supported. More system tools may be added later.
* Because `end_call` is terminal, it must be the final step in its containing sequence or branch.

```json focus={1-4}
{
  "type": "system_tool",
  "system_tool_name": "end_call"
}
```

## Complete API example

This example handles an order cancellation based on shipment status. It retries a failed tool call, invokes another structured procedure, then ends the call.

```json maxLines=30
{
  "trigger": "When the user asks to cancel an order and request a refund.",
  "steps": [
    {
      "type": "ask",
      "instruction": "Ask the user for their order ID."
    },
    {
      "type": "branch",
      "branches": [
        {
          "condition": {
            "type": "llm",
            "condition": "The user says the order has already shipped."
          },
          "steps": [
            {
              "type": "tell",
              "instruction": "Explain that shipped orders must be returned before they can be refunded."
            }
          ]
        },
        {
          "condition": {
            "type": "llm",
            "condition": "The user says the order has not shipped."
          },
          "steps": [
            {
              "type": "tool_call",
              "tool_id": "tool_abc123",
              "tool_name": "cancel_order",
              "instruction": "Cancel the order using the order ID provided by the user.",
              "on_failure": {
                "fallback": [
                  {
                    "type": "retry",
                    "max_retries": 2
                  }
                ]
              }
            }
          ]
        }
      ],
      "fallback": [
        {
          "type": "ask",
          "instruction": "Ask whether the order has already shipped."
        }
      ]
    },
    {
      "type": "sub_procedure",
      "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3"
    },
    {
      "type": "say",
      "message": "Thank you for contacting us. Goodbye."
    },
    {
      "type": "system_tool",
      "system_tool_name": "end_call"
    }
  ]
}
```

## How a structured procedure runs

When the user's request matches a procedure's trigger during a conversation, the agent enters the procedure and runs its steps in order, the same way every time. While inside the procedure, the agent focuses on those steps; when it reaches the end, it returns to where it left off in the conversation.

If a Tool step fails and does not define `on_failure`, the procedure stops without running the remaining steps. When `on_failure` is configured, the procedure runs the first matching failure branch or its required fallback. A handled failure continues to the next procedure step unless the selected handler retries the tool, ends the call, or invokes another terminal path.

## Manage a structured procedure

#### Build via the dashboard

Open your agent in the [dashboard](https://elevenlabs.io/app/agents), then select **Procedures**.
Use **+** to create a structured procedure. Add a trigger, select a type for each step, and
publish the agent changes.

#### Manage via the API

API and SDK payloads use `type: "deterministic"` for structured procedures. Their `content` is
a JSON-encoded document. The `/procedures/compile` endpoint generates workflow nodes from this
document.

### Prerequisites

* An ElevenLabs API key in the `ELEVENLABS_API_KEY` environment variable.
* The target `agent_id` and `branch_id`. See [Agent versioning](/docs/eleven-agents/operate/versioning) for branch operations.
* Version `2.60.0` or newer of the `elevenlabs` Python package or `@elevenlabs/elevenlabs-js` JavaScript package.
* `curl` and `jq` for the REST examples.

API edits are private to your user on the selected branch until you publish a new agent version.

### Create or update a draft

Create a structured procedure with `POST /procedures` and set `type` to `deterministic`.
Update an existing procedure with `PATCH /procedures/{procedure_id}/draft`, as shown below.

Include `trigger` as a top-level field and repeat the same value inside the structured
document, keeping the two in sync. JSON-encode the document in `content` rather than sending a
nested object.

```python focus={6-19}
import json
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.procedures.drafts.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
    procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
    name="Refund request",
    type="deterministic",
    trigger="When the user asks to refund an order",
    content=json.dumps(
        {
            "trigger": "When the user asks to refund an order",
            "steps": [{"type": "ask", "instruction": "Ask for the order ID."}],
        }
    ),
)
```

```typescript focus={5-18}
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.procedures.drafts.update(
  "agent_7101k5zvyjhmfg983brhmhkd98n6",
  "agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
  "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
  {
    name: "Refund request",
    type: "deterministic",
    trigger: "When the user asks to refund an order",
    content: JSON.stringify({
      trigger: "When the user asks to refund an order",
      steps: [{ type: "ask", instruction: "Ask for the order ID." }],
    }),
  }
);
```

```bash focus={1-9}
curl -X PATCH "https://api.elevenlabs.io/v1/convai/agents/agent_7101k5zvyjhmfg983brhmhkd98n6/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Refund request",
    "type": "deterministic",
    "trigger": "When the user asks to refund an order",
    "content": "{\"trigger\":\"When the user asks to refund an order\",\"steps\":[{\"type\":\"ask\",\"instruction\":\"Ask for the order ID.\"}]}"
  }'
```

Saving a structured draft does not validate or regenerate its workflow. Before publishing
changes or after merging agent branches, call `/procedures/compile` and publish the exact
workflow it returns. Otherwise, the workflow can contain stale, missing, duplicated, or
orphaned procedure nodes. The dashboard handles this automatically.

### Generate and publish the workflow

`/procedures/compile` validates the structured drafts and returns a workflow. A validation
failure returns `400` with `errors` keyed by procedure ID. Fix the reported drafts, then call
the endpoint again.

Removing the last remaining structured procedure does not remove its workflow nodes until you
regenerate the workflow.

After merging agent branches, regenerate the workflow on the target branch even if no
procedure drafts changed. A merge combines existing workflow nodes by ID, while each generated
workflow uses new node IDs. Regeneration removes duplicated or orphaned nodes.

Pass the returned `workflow` to [Update agent](/docs/api-reference/agents/update). This
publishes the drafts and generated nodes in the same agent version.

```python focus={3-12}
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

compiled = elevenlabs.conversational_ai.agents.procedures.compile(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
)

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
    workflow=compiled.workflow,
)
```

```typescript focus={5-14}
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

const compiled = await elevenlabs.conversationalAi.agents.procedures.compile(
  "agent_7101k5zvyjhmfg983brhmhkd98n6",
  "agtbranch_0901k4aafjxxfxt93gd841r7tv5t"
);

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  branchId: "agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
  workflow: compiled.workflow,
});
```

```bash focus={1-11,13-17}
set -euo pipefail

COMPILE_RESPONSE=$(curl -fsS -X POST \
  "https://api.elevenlabs.io/v1/convai/agents/agent_7101k5zvyjhmfg983brhmhkd98n6/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/compile" \
  -H "xi-api-key: $ELEVENLABS_API_KEY")

COMPILED_WORKFLOW=$(printf "%s" "$COMPILE_RESPONSE" | jq -ce '.workflow')
PUBLISH_BODY=$(jq -n \
  --argjson workflow "$COMPILED_WORKFLOW" \
  '{workflow: $workflow}')

curl -X PATCH \
  "https://api.elevenlabs.io/v1/convai/agents/agent_7101k5zvyjhmfg983brhmhkd98n6?branch_id=agtbranch_0901k4aafjxxfxt93gd841r7tv5t" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$PUBLISH_BODY"
```

See [Manage procedures](/docs/eleven-agents/customization/procedures#manage-procedures) for
draft removal and discard behavior, or the
[Procedures API reference](/docs/api-reference/agents/procedures/) for complete endpoint
schemas.

## Best practices

Each step type already enforces its own behavior, so you rarely need to spell it out. Write the
intent of each step and let the step type do the rest. The guidance below covers the cases worth
getting right.

### Writing steps

#### Let Ask steps wait for the user

An Ask step does not advance until it has asked your question and received an appropriate
answer. You do not need a follow-up step to check that the information was collected; the Ask
step guarantees it before moving on.

#### Keep Tool steps to the tool call

A Tool step only runs the tool; the agent cannot speak or make a decision during it. To talk to
the user or branch on what the tool returned, put that in a separate step before or after the
Tool step.

#### Choose Tell for phrasing, Say for exact words

Use a Tell step when the agent should compose the message itself, and a Say step when the
wording must be verbatim. Both deliver exactly one message, so there is no need to instruct a
step to send a single message.

### Composing procedures

The general guidance for composing procedures applies to structured procedures too — see [Composing procedures](/docs/eleven-agents/customization/procedures/free-form-procedures#composing-procedures) on the Free-form procedures page.

One pattern is specific to mixing types: a free-form procedure can reference a structured one. Keep open-ended handling in a free-form procedure and delegate the parts that must run the same way every time, such as identity verification or escalation, to a structured procedure.

## Limitations

* If steps cannot be nested, and two If steps cannot be placed back to back.

### Model provider support

Structured procedures force internal tool calls when entering a sub-procedure and completing a procedure. Major OpenAI, Anthropic, Gemini, and Grok model families support forced tool choice. Other models or custom providers may not guarantee it, which can make sub-procedure transitions or procedure completion less reliable. Verify forced tool-choice support when using another model provider.

See [Procedures](/docs/eleven-agents/customization/procedures#limitations) for limits that apply to all procedures, including the content size cap and how structured procedures differ from free-form ones.

## Release status

Structured procedures are currently in Alpha. Expect the step types, conditions, dashboard controls, and underlying schema to keep evolving before general availability; some changes may be breaking.
