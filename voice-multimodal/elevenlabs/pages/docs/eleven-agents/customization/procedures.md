---
title: "Procedures"
source: https://elevenlabs.io/docs/eleven-agents/customization/procedures.md
path: docs/eleven-agents/customization/procedures
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Procedures

## Overview

A procedure contains instructions for one specific task. Each procedure has a trigger that describes when it applies and content that describes what to do. When a conversation matches the trigger, the agent loads the procedure.

Use procedures when your agent needs to handle many distinct tasks. One example use case is a customer support agent, where each procedure covers one type of request: refunds, identity verification, account recovery, or connection troubleshooting.

![Procedures tab in the agent
dashboard](/docs/_fern-files/_img/38b190b7a08cb9e628da309a86c5e4b315eabccf238a41d5d3a6c2646aba11af.webp)

## Procedure types

There are two kinds of procedures:

* **[Free-form procedures](/docs/eleven-agents/customization/procedures/free-form-procedures)** are written as natural-language instructions the agent interprets and adapts to the situation.
* **[Structured procedures](/docs/eleven-agents/customization/procedures/structured-procedures)** are an ordered list of typed steps the agent runs the same way every time.

You can use both kinds on the same agent. The agent picks the relevant procedure from its trigger, regardless of type.

> **Tip**
>
> Procedures can call each other. A free-form procedure calls another procedure with an [inline reference](/docs/eleven-agents/customization/procedures/free-form-procedures#inline-references),
> and a structured procedure calls another structured procedure with a
> [Sub-procedure](/docs/eleven-agents/customization/procedures/structured-procedures#sub-procedure)
> step. A common pattern is to keep open-ended handling in a free-form procedure and hand off the
> parts that must run the same way every time to a structured one.

An agent can have procedures, a [workflow](/docs/eleven-agents/customization/agent-workflows), or both. When both are present, every procedure is available from every point in the workflow; a procedure cannot be limited to specific workflow nodes. Most agents are built around one approach or the other, but the two compose.

## When to use procedures

Every agent has a [system prompt](/docs/eleven-agents/best-practices/prompting-guide). Procedures and [workflows](/docs/eleven-agents/customization/agent-workflows) are two ways to add structure on top, and an agent can use both. Choose a starting point based on how much the conversation can vary.

| Requirement                                        | Use                                                                                        | Why                                                                                                                                                        |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simple proof of concept agent                      | System prompt only                                                                         | Fastest to set up and iterate on, but a single prompt gets unwieldy as the agent grows in scope.                                                           |
| Task where the agent can adapt wording and order   | [Free-form procedure](/docs/eleven-agents/customization/procedures/free-form-procedures)   | Keeps the whole conversation in one LLM's context, so the agent adapts wording and order and can follow unexpected turns. Uses more of the context window. |
| Task whose steps must run the same way every time  | [Structured procedure](/docs/eleven-agents/customization/procedures/structured-procedures) | Each step runs in the order you set, the same way every time, and you author it as a short list of steps.                                                  |
| Full control over complex branching and edge cases | [Workflow](/docs/eleven-agents/customization/agent-workflows)                              | Runs as a graph of subagents you design and connect yourself, with full control over branching and the model each step uses.                               |

Free-form procedures are the default choice. They are the fastest to write, they read like a document so non-technical teams can own them, and the agent can recover when a conversation goes off script. Reach for a structured procedure when the cost of a skipped or reordered step is high, such as authentication, escalation, or a financial transaction. Reach for a workflow when you need routing logic or per-step model control that neither procedure type offers.

## Manage procedures

The dashboard is the recommended way to author procedures. Use the CLI or the API to manage procedures programmatically or integrate them into deployment tooling.

#### Build via the dashboard

Open your agent in the [dashboard](https://elevenlabs.io/app/agents), then select **Procedures**.
Use **+** to create a free-form or structured procedure. Procedures can be grouped into folders
from the same menu. See
[Free-form procedures](/docs/eleven-agents/customization/procedures/free-form-procedures)
and
[Structured procedures](/docs/eleven-agents/customization/procedures/structured-procedures)
for authoring guidance.

#### Manage via the CLI

The [ElevenLabs CLI](/docs/eleven-agents/operate/cli) manages procedures with the
`elevenlabs agents procedures` command group. Set `ELEVENLABS_API_KEY` in your environment
first.

```bash
# List the procedures on a branch
elevenlabs agents procedures list \
  --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 \
  --branch-id agtbranch_0901k4aafjxxfxt93gd841r7tv5t

# Create a procedure
elevenlabs agents procedures create \
  --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 \
  --branch-id agtbranch_0901k4aafjxxfxt93gd841r7tv5t \
  --json '{"name": "Refund request", "type": "free_form", "trigger": "When the user asks to refund an order", "content": "Ask for the order ID."}'

# Publish every changed procedure draft on the branch
elevenlabs agents update \
  --agent-id agent_7101k5zvyjhmfg983brhmhkd98n6 \
  --branch-id agtbranch_0901k4aafjxxfxt93gd841r7tv5t \
  --json '{"version_description": "Publish refund procedure"}'
```

Use `elevenlabs agents procedures drafts` to read, update, or discard a draft, and
`elevenlabs agents procedures remove` to stage a removal. Add `--schema` to any command to see
its input and output contract.

#### Manage via the API

Procedure drafts follow the [agent versioning lifecycle](/docs/eleven-agents/operate/versioning#drafts). They are per-user, per-branch, so each
team member has separate drafts on each branch. Publishing saves your procedure changes in a new
immutable agent version on that branch. Other users' drafts are unaffected.

Agent configuration responses include procedure metadata such as IDs, names, types, and
triggers, but not procedure bodies or drafts. Use the procedure endpoints to read and edit the
full content. All procedure endpoints are nested under
`/v1/convai/agents/{agent_id}/branches/{branch_id}`.

### Create or update a draft

Create a procedure with `POST /procedures`. Update it with
`PATCH /procedures/{procedure_id}/draft`, including `name`, `content`, `type`, and `trigger`
in every request. The `type` must match the procedure's existing type.

Use `GET /procedures/{procedure_id}/draft` to read unpublished changes. If you have no draft,
the endpoint returns the published version.

### Publish the changes

Publish the drafts by creating a new agent version with
[Update agent](/docs/api-reference/agents/update). One request publishes every changed
procedure draft on the branch, for both procedure types. Turning a structured procedure's
steps into the form the agent executes is called compiling. The platform compiles every
structured procedure when the agent draft is saved or the agent is published; authors never
compile anything themselves. Both operations validate every structured procedure and return
any errors. If validation passes, the agent configuration is saved or published.

Follow the type-specific instructions for
[free-form procedures](/docs/eleven-agents/customization/procedures/free-form-procedures#manage-a-free-form-procedure)
or
[structured procedures](/docs/eleven-agents/customization/procedures/structured-procedures#manage-a-structured-procedure).

### Discard or remove a procedure

`DELETE /procedures/{procedure_id}/draft` discards unpublished edits and restores the
published version. If the procedure has never been published, this deletes it.

`DELETE /procedures/{procedure_id}` stages removal of a published procedure. Publish the
change using the same flow.

See the [Procedures API reference](/docs/api-reference/agents/procedures/) for complete endpoint
schemas.

## Choose procedures per conversation

By default, every conversation can use all of the agent's procedures, and the agent loads a procedure only after the conversation matches its trigger. Your application often knows more before the conversation starts: who the user is, which region they are in, or what they called about. Pass procedure IDs in the conversation initiation client data to use that knowledge. You decide which procedures the agent can use, and which ones it follows from the first turn.

| Field                 | What it does                                                                                                                    | Why use it                                                                                                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `procedure_ids`       | Limits the conversation to these procedures. An empty array disables all of the agent's procedures.                             | Give each user only the procedures that apply to them, for example hide account procedures from a user who has not signed in. Also use it when procedures have similar triggers that you cannot avoid, such as one refund procedure per region. Pass only the user's region, so the agent cannot follow another region's procedure. |
| `start_procedure_ids` | Starts these free-form procedures with the conversation, so the agent follows them from the first turn. Accepts up to five IDs. | Reply faster when you already know the user's task, for example from an IVR menu choice, the page that hosts the widget, or CRM data.                                                                                                                                                                                               |

A procedure in `start_procedure_ids` is already loaded when the user first speaks, so the agent skips the LLM call that would load it. Any active procedure stays in the prompt on every turn, whether the agent or your application started it. A started procedure that the conversation never needs still adds its content to every turn, so start only the procedures the conversation is likely to use.

### Allow procedure selection

The **Procedures** override is off by default. Enable it on each agent that should accept procedure IDs from the client.

#### Dashboard

Open your agent in the [dashboard](https://elevenlabs.io/app/agents), select the **Security** tab, and enable the **Procedures** override.

#### CLI

Pull the agent configuration:

```bash
elevenlabs agents pull --agent "<agent-name>"
```

In `agent_configs/<agent-name>.json`, set `platform_settings.overrides.enable_procedure_ids_from_client` to `true`:

```json
{
  "platform_settings": {
    "overrides": {
      "enable_procedure_ids_from_client": true
    }
  }
}
```

Push the change:

```bash
elevenlabs agents push --agent "<agent-name>"
```

#### SDK

```python
import os

from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    platform_settings={
        "overrides": {
            "enable_procedure_ids_from_client": True,
        },
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient({ apiKey: process.env.ELEVENLABS_API_KEY });

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  platformSettings: {
    overrides: {
      enableProcedureIdsFromClient: true,
    },
  },
});
```

### Pass the IDs when the conversation starts

> **Warning**
>
> If the agent does not have the **Procedures** override enabled, or an ID is invalid, the
> conversation fails to start.

Get procedure IDs from [List procedures](/docs/api-reference/agents/procedures/list). Add `procedure_ids`, `start_procedure_ids`, or both to the conversation initiation client data:

**`Conversation initiation payload`**

```json title="Conversation initiation payload"
{
  "type": "conversation_initiation_client_data",
  "procedure_ids": [
    "agtprc_4101k8f3w2pqv6xs9mhdr0tz7n3b",
    "agtprc_2301k8f3xq9zfa7tkrqs6m4bdn5e",
    "agtprc_7801k8f3yt4mfzh2xbq9d0vcpw1r"
  ],
  "start_procedure_ids": ["agtprc_4101k8f3w2pqv6xs9mhdr0tz7n3b"]
}
```

The agent starts the conversation with the first procedure already running. It can still start the other two when the conversation matches their triggers.

> **Note**
>
> The Python and JavaScript conversation SDKs do not send `procedure_ids` or `start_procedure_ids`.
> To use these fields, send the initiation message over the
> [WebSocket](/docs/eleven-agents/libraries/web-sockets) yourself.

Both fields follow these rules:

* Each ID in `procedure_ids` must belong to the agent. If a selected procedure calls sub-procedures, include the sub-procedures too.
* Each ID in `start_procedure_ids` must be a free-form procedure. When you also pass `procedure_ids`, each ID must also be in that list.
* `procedure_ids` applies only to the agent the conversation starts with. It does not apply after an [agent transfer](/docs/eleven-agents/customization/tools/system-tools/agent-transfer).
* Started procedures count toward the five active procedures in [Limitations](#limitations). The conversation history records each one as a `start_procedure` tool call.

## Limitations

* A procedure's content is capped at 50,000 characters.
* The agent keeps the five most recently started procedures in context. When more have been started in one conversation, the content, inline tools, and knowledge base documents of the oldest free-form procedures drop out of the prompt. Keep procedures focused and use sub-procedures so that few are active at once.
* You cannot change a procedure's type after creating it. To convert between free-form and structured, create a new procedure and update any references to it.
* Procedures belong to one agent. They cannot be shared across agents or stored as workspace-level resources.
* Duplicating an agent copies its procedures instead of sharing them. The copies receive new procedure IDs, so references in the duplicated agent must use those new IDs.
* Procedures cannot be limited to specific workflow nodes. When an agent has both, every procedure is available from every node.
* Structured procedures cannot reference knowledge base documents.
