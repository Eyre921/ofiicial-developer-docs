---
title: "Free-form procedures"
source: https://elevenlabs.io/docs/eleven-agents/customization/procedures/free-form-procedures.md
path: docs/eleven-agents/customization/procedures/free-form-procedures
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Free-form procedures

## Overview

A free-form procedure describes one task in plain, natural language. The agent interprets the instructions and adapts the wording and order to the situation. A free-form procedure can call tools (including system tools like ending a call), look up knowledge base documents, and chain to other procedures.

## When to use a free-form procedure

Use a free-form procedure when the agent can adapt wording and order to fit the situation, and you want to author it quickly in plain language. For how it compares to structured procedures, workflows, and the system prompt, see [When to use procedures](/docs/eleven-agents/customization/procedures#when-to-use-procedures).

## Anatomy of a procedure

Here is a refund procedure in the editor:

![Refund procedure
example](/docs/_fern-img/e1264b7a4f94403453087d30ef0894e72d412ba69378e6b8cb1b675e53e887b7.webp)

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

![Slash menu in the procedure editor](/docs/_fern-img/8625ffec0f5584619e6ccb97720fd86f2e8d3cd0061308ad87b57f176e5535e3.webp)

If a referenced resource is deleted later, or your account loses access to it, the tag shows as broken. The **Errors** badge at the top of the editor lists these references: *invalid* if the resource no longer exists, or *unavailable* if it exists but your account does not have access. Open the badge to see which step is affected and fix or remove the reference.

![Errors dialog listing invalid
references](/docs/_fern-img/e9ec6b19be2992da80a726883baf53265a5d5b38621373cd7e60375c944674cd.webp)

## Sub-procedures

A sub-procedure has an empty trigger. The agent can run it only from another procedure that references it.

Use sub-procedures to [share steps](#composing-procedures) within one agent and reduce the number of procedures available at once. Give the entry procedure a trigger, reference related sub-procedures from its content, and leave their triggers empty.

An escalation sub-procedure can hold the steps for handing the conversation to a human. Reference it from the refund and cancellation procedures and leave its trigger empty. The agent can escalate as a step of either procedure, but outside them the sub-procedure stays unavailable.

## Importing from a document

You can bootstrap from an existing standard operating procedure (SOP). Choose **From SOP** in the procedure list **+** menu, then upload a file.

Supported formats: `PDF`, `DOCX`, `TXT`, `MD`, `HTML`, `EPUB`. Files must be 20 MB or smaller.

The importer analyzes the document, identifies up to 10 distinct procedures, and creates a draft for each one with a generated name, trigger, and content. Open each draft to refine it. If your document contains more than 10 SOPs, split it into smaller files before uploading.

![Upload SOP dialog](/docs/_fern-img/716601fc90dea757e23971e5aabe063e6a66fc0f75878247dc9f1fc3011f5197.webp)

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

Procedure drafts are [per-user, per-branch](/docs/eleven-agents/operate/versioning#drafts). Publishing saves your procedure
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

> **Tip**
>
> The agent has to pick the right procedure from its trigger and follow the content. More capable
> models do this more reliably as the number of procedures grows. See
> [Models](/docs/eleven-agents/customization/llm) for options.

Writing procedures well means writing two parts well: a trigger that runs the procedure when it should, and content the agent can follow.

### Iterating on a procedure

We recommend starting small and using [agent tests](/docs/eleven-agents/customization/agent-testing) to check each change before you make the next one.

#### Write a short procedure

Write a trigger and short content. Expand the content only when a test shows that the agent
needs more instructions.

#### Add trigger tests

Create simulation tests for requests that should start the procedure and for similar requests
that should not. Most failures come from the trigger, so write more of these than full
simulations.

#### Add a full simulation

Create a simulation test that runs the whole procedure and checks the outcome.

#### Run the tests and fix failures

When a test fails, fix the trigger or the content, then rerun every test.

> **Tip**
>
> To iterate on a trigger quickly, create a simulation test whose [chat history](/docs/eleven-agents/customization/agent-testing#simulation-testing) ends with the user's
> request, and set **Maximum conversation turns** to `1`. The agent replies once, which is enough to
> show whether the request starts the right procedure, and each run stays short. Write the success
> criteria as *The agent started the refund procedure*. Without chat history, an agent with a first
> message spends the only turn on its greeting and the test checks nothing.

When a test or a live conversation fails, look for the class of mistake behind it. If the agent said something wrong, adding *Don't say that* fixes one conversation. Search past conversations for similar failures and write one instruction that covers all of them. The cause can also be in the knowledge base or the agent configuration. [Architect](/docs/eleven-agents/operate/architect) can do this search: open the failed conversation, select **Architect**, and ask it to find similar failures and propose a fix. Architect can also turn the conversation into a test.

### Writing triggers

#### Keep triggers concrete and disjoint

Overlapping or vague triggers cause the wrong procedure to run. Prefer *When the user asks to
cancel a subscription* over *When the user has a question about their account*.

#### Write from the user's perspective

Describe what the user is asking for, not what the agent should do. Triggers phrased as agent
actions are less reliable. Prefer *When the user asks to cancel their subscription* over *Cancel
the user's subscription*.

#### Cover the way users actually ask

A narrow trigger can miss real requests when the user phrases things differently. Include the
variations the user might say. *When the user asks to refund, return, or get money back for an
order* runs more reliably than *When the user requests a refund*. [Search past conversations](/docs/eleven-agents/customization/agent-analysis/smart-search) to find how users
phrase the request.

#### Hand off between related procedures

Users sometimes change their request partway through a procedure, and the trigger alone may not
start the right one. For a switch you see often in past conversations, add an inline reference
to the other procedure in the first procedure's content. For example, write *If the user wants a
refund instead of an exchange, run* followed by an inline reference to the refund procedure. If
most procedures need a hand-off, make the triggers more distinct instead.

### Writing content

#### Use imperative form

Write steps as instructions to the agent: *Look up the customer's last order* rather than *You
should look up the customer's last order*. Direct instructions are easier to follow than
suggestions.

#### Explain why a step matters

Reasoning generalizes to edge cases the procedure does not enumerate. A short *because we need
the order ID to issue a refund* helps the agent handle situations the steps did not anticipate.
Avoid all-caps MUSTs and rigid scripts where a one-line explanation would do the same work.

#### Say what to do instead of what to avoid

Describe the behavior you want. *If you can't find the order, ask the user to confirm the order
ID* works better than *Don't make up order details*. For mistakes with a high cost, add a
[guardrail](/docs/eleven-agents/best-practices/guardrails) as well.

#### Use steps when order matters

Numbered steps help when the agent must do things in a fixed order. For judgment calls, a few
sentences of guidance often work better, especially with more capable models.

#### Keep facts in the knowledge base

A procedure describes what the agent should do in a situation. Specific information, such as
prices, plan details, or opening hours, belongs in the [knowledge base](/docs/eleven-agents/customization/knowledge-base). Reference the document from the
procedure that needs it. For example, instead of listing every plan's price in the procedure,
write *Quote the price from* followed by an inline reference to a pricing document.

### Composing procedures

#### Write one procedure per situation

If one situation is split across several narrow procedures, the agent has more triggers to
choose from and starts the wrong one more often. If two procedures would start on the same
request, merge them. Content longer than about 3,000 characters usually covers more than one
situation.

#### Extract shared steps into a sub-procedure

If the same steps show up across multiple procedures (verifying a customer's identity, looking
up an order, escalating to a human), extract them into a [sub-procedure](#sub-procedures) and
reference it from each one that needs it via the slash menu. Maintaining the shared steps in one
place keeps every procedure that uses them consistent.

#### Use sub-procedures for reactive actions

Use a sub-procedure for an action the agent should run only when another procedure requests it,
such as identity verification or escalation. Without a trigger, it does not compete with entry
procedures at conversation start. Fewer trigger choices keep routing focused.

#### Reference tools from the procedure that uses them

Reference a tool from the procedure that uses it instead of attaching it to the whole agent. The
tool then stays out of unrelated conversations. In a free-form procedure, the tool is available
only while the procedure is one of the five most recently started, so mention the tool's task in
the trigger too, for example *or when you need to look up an order*. See
[Limitations](/docs/eleven-agents/customization/procedures#limitations).

#### Use the system prompt for global behavior

Tone, identity, refusal policies, and guardrails belong in the [system prompt](/docs/eleven-agents/best-practices/prompting-guide). Put task-specific steps in
procedures.

#### Procedures version with the agent

Procedures are part of the agent's configuration, so they snapshot together when you publish a
new agent version. To roll back to an earlier set of procedures, restore an earlier agent
version. See [Agent versioning](/docs/eleven-agents/operate/versioning).

#### Bootstrap from existing documentation

If your team already has SOPs, use the importer to turn them into drafts and refine from there.
