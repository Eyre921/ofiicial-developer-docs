---
title: "Free-form procedures"
source: https://elevenlabs.io/docs/eleven-agents/customization/procedures/free-form-procedures.md
path: docs/eleven-agents/customization/procedures/free-form-procedures
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Free-form procedures

Free-form procedures are currently in Alpha. See details in [Release status](#release-status).

## Overview

A free-form procedure describes one task in plain, natural language. The agent interprets the instructions and adapts the wording and order to the situation. A free-form procedure can call tools (including system tools like ending a call), look up knowledge base documents, and chain to other procedures.

## When to use a free-form procedure

Use a free-form procedure when the agent can adapt wording and order to fit the situation, and you want to author it quickly in plain language. For how it compares to structured procedures, workflows, and the system prompt, see [When to use procedures](/docs/eleven-agents/customization/procedures#when-to-use-procedures).

## Anatomy of a procedure

Here is a refund procedure in the editor:

![Refund procedure
example](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e1264b7a4f94403453087d30ef0894e72d412ba69378e6b8cb1b675e53e887b7/assets/images/conversational-ai/procedures/refund-procedure-example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260813T222303Z&X-Amz-Expires=604800&X-Amz-Signature=4c4d613637097f2eecfa90b8a54102b689e4d2bbc404eaa688ea3532a7f96278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

A procedure has two main parts: a trigger and content. Both can contain inline references to other resources, shown in the screenshot above as tags with wrench icons. Each procedure also has a name shown in the dashboard.

### Name

A short label that identifies the procedure in the dashboard. The name is never sent to the LLM, so it does not affect agent behavior.

### Trigger

A description of when the agent should use this procedure, for example *When the user asks to refund an order*.

Leave the trigger empty only when creating a [sub-procedure](#sub-procedures).

### Content

The body of the procedure, written in markdown. Content describes what the agent should do: ask a question, look up an order, call a tool, or end the call. It can be a numbered sequence of steps to follow, or general guidance for the situation. Each step or guideline can be a single sentence (*Ask the user for their order ID*) or a short paragraph that explains what to do and why.

Use numbered steps for sequential actions and bullet points for requirements or sub-items within a step.

### Inline references

Procedures can reference different kinds of resources inline:

* Tools (e.g. look up an order, charge a card, end the call, transfer to a human)
* Knowledge base documents
* Other procedures

Use inline references whenever a step needs the agent to use a tool, knowledge base document, or another procedure. References auto-attach the resource to the procedure so the agent can use it. Plain prose mentions (like *use the calculator tool here*) also work, but only if the resource is already attached to the agent.

Insert a reference by typing `/` in the trigger or content and choosing the resource from the slash menu. References appear as clickable tags in the editor. Click a tag to open the underlying resource and confirm its configuration.

When writing free-form content through the API, insert references with the following syntax:

```text focus={1-5}
[tool id="tool_abc123"]
[kb id="kb_abc123"]
[procedure id="agtprc_abc123"]
[system_tool id="end_call"]
{{customer_id}}
```

An inline procedure reference must use a procedure from the same agent. See [Limitations](/docs/eleven-agents/customization/procedures#limitations) for agent scope and duplication behavior.

A reference in the trigger lets the procedure fire based on a resource's output, for example *When `get_user` returns tier 'gold'*. A reference in content tells the agent to invoke or consult the resource at that step.

![Slash menu in the procedure editor](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8625ffec0f5584619e6ccb97720fd86f2e8d3cd0061308ad87b57f176e5535e3/assets/images/conversational-ai/procedures/slash-menu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260813T222303Z&X-Amz-Expires=604800&X-Amz-Signature=7c1da6710c4b8b4c82469d087a6f42668215a280d8ce8292bcecad3a8a994b75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If a referenced resource is deleted later, or your account loses access to it, the tag shows as broken. The **Errors** badge at the top of the editor lists these references: *invalid* if the resource no longer exists, or *unavailable* if it exists but your account does not have access. Open the badge to see which step is affected and fix or remove the reference.

![Errors dialog listing invalid
references](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e9ec6b19be2992da80a726883baf53265a5d5b38621373cd7e60375c944674cd/assets/images/conversational-ai/procedures/reference-tags.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260813T222303Z&X-Amz-Expires=604800&X-Amz-Signature=61df9965813a360b82964a53be16633a172181ba88eed1e073f0e9093de25547&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Sub-procedures

A sub-procedure has an empty trigger. The agent can run it only from another procedure that references it.

Use sub-procedures to [share steps](#composing-procedures) within one agent and reduce the number of procedures available at once. Give the entry procedure a trigger, reference related sub-procedures from its content, and leave their triggers empty.

An escalation sub-procedure can hold the steps for handing the conversation to a human. Reference it from the refund and cancellation procedures and leave its trigger empty. The agent can escalate as a step of either procedure, but outside them the sub-procedure stays unavailable.

## Importing from a document

You can bootstrap from an existing standard operating procedure (SOP). Choose **From SOP** in the procedure list **+** menu, then upload a file.

Supported formats: `PDF`, `DOCX`, `TXT`, `MD`, `HTML`, `EPUB`. Files must be 20 MB or smaller.

The importer analyzes the document, identifies up to 10 distinct procedures, and creates a draft for each one with a generated name, trigger, and content. Open each draft to refine it. If your document contains more than 10 SOPs, split it into smaller files before uploading.

![Upload SOP dialog](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/716601fc90dea757e23971e5aabe063e6a66fc0f75878247dc9f1fc3011f5197/assets/images/conversational-ai/procedures/upload-sop.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260813T222303Z&X-Amz-Expires=604800&X-Amz-Signature=b2f74358f559010ab1feb31fda05e574fba46573a7e7258d1ad522fbcf09265c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Manage a free-form procedure

#### Build via the dashboard

Open your agent in the [dashboard](https://elevenlabs.io/app/agents), then select **Procedures**.
Use **+** to create a free-form procedure. Add a trigger and write the instructions in the
content editor, then publish the agent changes.

#### Manage via the API

Free-form procedures store markdown in `content`.

### Prerequisites

* An ElevenLabs API key in the `ELEVENLABS_API_KEY` environment variable.
* The target `agent_id` and `branch_id`. See [Agent versioning](/docs/eleven-agents/operate/versioning) for branch operations.
* Version `2.60.0` or newer of the `elevenlabs` Python package or `@elevenlabs/elevenlabs-js` JavaScript package.

Procedure drafts are [per-user,
per-branch](/docs/eleven-agents/operate/versioning#drafts). Publishing saves your procedure
changes in a new agent version on that branch. Other users' drafts are unaffected.

### Create a draft

```python focus={1,5-15}
from elevenlabs import CreateProcedureRequestModel, ElevenLabs

elevenlabs = ElevenLabs()

procedure = elevenlabs.conversational_ai.agents.procedures.create(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
    request=CreateProcedureRequestModel(
        name="Refund request",
        type="free_form",
        trigger="When the user asks to refund, return, or get money back for an order",
        content="Ask for the order ID, then look it up with [tool id=\"tool_abc123\"].",
    ),
)

print(procedure.procedure_id)
```

```typescript focus={5-15}
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

const procedure = await elevenlabs.conversationalAi.agents.procedures.create(
  "agent_7101k5zvyjhmfg983brhmhkd98n6",
  "agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
  {
    name: "Refund request",
    type: "free_form",
    trigger: "When the user asks to refund, return, or get money back for an order",
    content: "Ask for the order ID, then look it up with [tool id=\"tool_abc123\"].",
  }
);

console.log(procedure.procedureId);
```

```bash focus={1-8}
curl -X POST "https://api.elevenlabs.io/v1/convai/agents/agent_7101k5zvyjhmfg983brhmhkd98n6/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Refund request",
    "type": "free_form",
    "trigger": "When the user asks to refund, return, or get money back for an order",
    "content": "Ask for the order ID, then look it up with [tool id=\"tool_abc123\"]."
  }'
```

The response includes the new `procedure_id`. To update the draft, call
`PATCH /procedures/{procedure_id}/draft` with `name`, `content`, `type`, and an explicit
`trigger`.

Use a non-empty `trigger` for an entry procedure. For a
[sub-procedure](#sub-procedures), use an empty string.

### Publish the changes

Update the agent on the branch to publish your free-form procedure drafts in a new version.
The request needs no body fields; publishing takes the drafts as they are.

```python focus={5-8}
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
)
```

```typescript focus={5-7}
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  branchId: "agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
});
```

```bash focus={1-5}
curl -X PATCH \
  "https://api.elevenlabs.io/v1/convai/agents/agent_7101k5zvyjhmfg983brhmhkd98n6?branch_id=agtbranch_0901k4aafjxxfxt93gd841r7tv5t" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

See [Manage procedures](/docs/eleven-agents/customization/procedures#manage-procedures) for
draft removal and discard behavior, or the
[Procedures API reference](/docs/api-reference/agents/procedures/) for complete endpoint
schemas.

## Best practices

The agent has to pick the right procedure from its trigger and follow the content. More capable
models do this more reliably as the number of procedures grows. See
[Models](/docs/eleven-agents/customization/llm) for options.

Writing procedures well means writing two parts well: a trigger that runs the procedure when it should, and content the agent can follow.

### Writing triggers

#### Keep triggers concrete and disjoint

Overlapping or vague triggers cause the wrong procedure to run. Prefer *When the user asks to
cancel a subscription* over *When the user has a question about their account*.

#### Write from the user's perspective

Describe what the user is asking for, not what the agent should do. Triggers phrased as agent
actions are less reliable.

#### Cover the way users actually ask

A narrow trigger can miss real requests when the user phrases things differently. Include the
variations the user might say. *When the user asks to refund, return, or get money back for an
order* runs more reliably than *When the user requests a refund*.

### Writing content

#### Use imperative form

Write steps as instructions to the agent: *Look up the customer's last order* rather than *You
should look up the customer's last order*. Direct instructions are easier to follow than
suggestions.

#### Explain why a step matters

Reasoning generalizes to edge cases the procedure does not enumerate. A short *because we need
the order ID to issue a refund* helps the agent handle situations the steps did not anticipate.
Avoid all-caps MUSTs and rigid scripts where a one-line explanation would do the same work.

#### Keep each procedure focused on one task

If a procedure starts branching into unrelated outcomes, split it into smaller procedures and
let the agent route between them.

### Composing procedures

#### Extract shared steps into their own procedure

If the same steps show up across multiple procedures (verifying a customer's identity, looking
up an order, escalating to a human), extract them into a dedicated procedure and reference it
from each one that needs it via the slash menu. Maintaining the shared steps in one place keeps
every procedure that uses them consistent.

#### Use sub-procedures for reactive actions

Use a sub-procedure for an action the agent should run only when another procedure requests it,
such as identity verification or escalation. Without a trigger, it does not compete with entry
procedures at conversation start. Fewer trigger choices keep routing focused.

#### Use the system prompt for global behavior

Tone, identity, refusal policies, and guardrails belong in the [system
prompt](/docs/eleven-agents/best-practices/prompting-guide). Put task-specific steps in
procedures.

#### Procedures version with the agent

Procedures are part of the agent's configuration, so they snapshot together when you publish a
new agent version. To roll back to an earlier set of procedures, restore an earlier agent
version. See [Agent versioning](/docs/eleven-agents/operate/versioning).

#### Bootstrap from existing documentation

If your team already has SOPs, use the importer to turn them into drafts and refine from there.

## Release status

Free-form procedures are currently in Alpha. Expect the feature set, dashboard controls, and underlying schema to keep evolving before general availability; some changes may be breaking.
