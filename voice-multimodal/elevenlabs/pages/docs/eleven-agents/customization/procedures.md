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
dashboard](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/38b190b7a08cb9e628da309a86c5e4b315eabccf238a41d5d3a6c2646aba11af/assets/images/conversational-ai/procedures/procedures-overview.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260825%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260825T200601Z&X-Amz-Expires=604800&X-Amz-Signature=699fce7ad65bc09160a05990245ad730671f07c8efea8ba9b1aa92f13c156e09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Procedure types

There are two kinds of procedures:

* **[Free-form procedures](/docs/eleven-agents/customization/procedures/free-form-procedures)** are written as natural-language instructions the agent interprets and adapts to the situation.
* **[Structured procedures](/docs/eleven-agents/customization/procedures/structured-procedures)** are an ordered list of typed steps the agent runs the same way every time.

You can use both kinds, alongside [workflows](/docs/eleven-agents/customization/agent-workflows), on the same agent. The agent picks the relevant procedure from its trigger, regardless of type.

## When to use procedures

Every agent has a [system prompt](/docs/eleven-agents/best-practices/prompting-guide). Procedures and [workflows](/docs/eleven-agents/customization/agent-workflows) are two alternative ways to add structure on top. Pick based on how much the conversation can vary.

| Requirement                                        | Use                                                                                        | Why                                                                                                                                                        |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simple proof of concept agent                      | System prompt only                                                                         | Fastest to set up and iterate on, but a single prompt gets unwieldy as the agent grows in scope.                                                           |
| Task where the agent can adapt wording and order   | [Free-form procedure](/docs/eleven-agents/customization/procedures/free-form-procedures)   | Keeps the whole conversation in one LLM's context, so the agent adapts wording and order and can follow unexpected turns. Uses more of the context window. |
| Task whose steps must run the same way every time  | [Structured procedure](/docs/eleven-agents/customization/procedures/structured-procedures) | Each step runs in the order you set, the same way every time, and you author it as a short list of steps.                                                  |
| Full control over complex branching and edge cases | [Workflow](/docs/eleven-agents/customization/agent-workflows)                              | Runs as a graph of subagents you design and connect yourself, with full control over branching and the model each step uses.                               |

## Manage procedures

The dashboard is the recommended way to build procedures. Use the API to manage procedures
programmatically or integrate them into deployment tooling.

The ElevenLabs CLI does not currently support managing procedures.

#### Build via the dashboard

Open your agent in the [dashboard](https://elevenlabs.io/app/agents), then select **Procedures**.
Use **+** to create a free-form or structured procedure. See
[Free-form procedures](/docs/eleven-agents/customization/procedures/free-form-procedures)
and
[Structured procedures](/docs/eleven-agents/customization/procedures/structured-procedures)
for authoring guidance.

#### Manage via the API

Procedure drafts follow the [agent versioning
lifecycle](/docs/eleven-agents/operate/versioning#drafts). They are per-user, per-branch, so each
team member has separate drafts on each branch. Publishing saves your procedure changes in a new
immutable agent version on that branch. Other users' drafts are unaffected.

Agent configuration responses include procedure metadata such as IDs, names, types, and
triggers, but not procedure bodies or drafts. Use the procedure endpoints to read and edit the
full content. All procedure endpoints are nested under
`/v1/convai/agents/{agent_id}/branches/{branch_id}`.

### Create or update a draft

Create a procedure with `POST /procedures`. Update it with
`PATCH /procedures/{procedure_id}/draft`, including `name`, `content`, `type`, and `trigger`
in every request.

Use `GET /procedures/{procedure_id}/draft` to read unpublished changes. If you have no draft,
the endpoint returns the published version.

### Publish the changes

Publish the draft by creating a new agent version. Free-form procedures can be published
directly. For structured procedures, call `/procedures/compile` to generate a workflow first.

Follow the type-specific instructions for
[free-form procedures](/docs/eleven-agents/customization/procedures/free-form-procedures#manage-a-free-form-procedure)
or
[structured procedures](/docs/eleven-agents/customization/procedures/structured-procedures#manage-a-structured-procedure).

### Discard or remove a procedure

`DELETE /procedures/{procedure_id}/draft` discards unpublished edits and restores the
published version. If the procedure has never been published, this deletes it.

`DELETE /procedures/{procedure_id}` stages removal of a published procedure. Publish the
change using the same type-specific flow.

See the [Procedures API reference](/docs/api-reference/agents/procedures/) for complete endpoint
schemas.

## Limitations

* A procedure's content is capped at 50,000 characters.
* You cannot change a procedure's type after creating it.
* Procedures belong to one agent. They cannot be shared across agents or stored as workspace-level resources.
* Duplicating an agent copies its procedures instead of sharing them. The copies receive new procedure IDs, so references in the duplicated agent must use those new IDs.
* Structured procedures cannot reference knowledge base documents.
