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
dashboard](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/38b190b7a08cb9e628da309a86c5e4b315eabccf238a41d5d3a6c2646aba11af/assets/images/conversational-ai/procedures/procedures-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261006T231212Z&X-Amz-Expires=604800&X-Amz-Signature=22a07c09f01510cb66e8ea9a8ca27492ac0b679f7b1036f631d0a9348ef1fcda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
procedure draft on the branch, for both procedure types. If the branch has structured
procedures, the publish validates and compiles them (turns their steps into the form the
agent executes) and returns any errors. If validation passes, the agent configuration is
published. You do not compile anything yourself.

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

## Limitations

* A procedure's content is capped at 50,000 characters.
* The agent keeps the five most recently started procedures in context. When more have been started in one conversation, the content, inline tools, and knowledge base documents of the oldest free-form procedures drop out of the prompt. Keep procedures focused and use sub-procedures so that few are active at once.
* You cannot change a procedure's type after creating it. To convert between free-form and structured, create a new procedure and update any references to it.
* Procedures belong to one agent. They cannot be shared across agents or stored as workspace-level resources.
* Duplicating an agent copies its procedures instead of sharing them. The copies receive new procedure IDs, so references in the duplicated agent must use those new IDs.
* Procedures cannot be limited to specific workflow nodes. When an agent has both, every procedure is available from every node.
* Structured procedures cannot reference knowledge base documents.
