---
title: "Knowledge Agent Toolkit (KAT) overview"
source: https://docs.pinecone.io/guides/marketplace/kat-overview
path: guides/marketplace/kat-overview
---

How the Knowledge Agent Toolkit (KAT) orchestrates multi-domain Pinecone Marketplace apps with manifests, disambiguation, slot filling, and guardrails.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Knowledge Agent Toolkit (KAT) is the orchestration layer in Pinecone Marketplace. KAT turns one or more knowledge bases into a coherent multi-domain knowledge application by handling intent extraction, slot filling, multi-domain routing, disambiguation, and guardrails.

KAT is required for any deployment with more than one knowledge base. Single-knowledge-base deployments can use simpler routing strategies.

## What KAT does

For every end-user query, KAT:

1. **Extracts intent**: identifies what the end user is trying to accomplish.
2. **Fills slots**: identifies missing context, such as a region or a product line, and asks the end user for it when needed.
3. **Routes**: picks the right knowledge bases to query based on auto-generated [manifests](#manifests).
4. **Applies guardrails**: blocks queries that violate policy and refuses out-of-scope queries.
5. **Synthesizes a response** (in `full` mode) or hands off to Pinecone Assistant for synthesis (in `disambiguation_only` mode).

## Outcomes

Every KAT decision resolves to one of four outcomes:

| Outcome        | What it means                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `CALL_KB`      | Route the query to one or more specific knowledge bases.                                                                        |
| `ASK_SLOT`     | Ask the end user for missing context before answering. See [Disambiguation and slot filling](#disambiguation-and-slot-filling). |
| `BLOCKED`      | Refuse the query because it violates a guardrail. See [Guardrails and scope](#guardrails-and-scope).                            |
| `OUT_OF_SCOPE` | Refuse the query and list what the application can help with instead. See [Guardrails and scope](#guardrails-and-scope).        |

## Execution modes

KAT supports two execution modes:

* **`full`**: KAT runs the complete pipeline, including disambiguation, slot filling, knowledge-base selection, and answer synthesis. Best for multi-domain deployments where consistent orchestration matters.
* **`disambiguation_only`**: KAT routes and disambiguates, then delegates synthesis to Pinecone Assistant. Best when you want KAT's routing intelligence with Pinecone Assistant's response style.

## Strategies for single-knowledge-base deployments

If a deployment has only one knowledge base, you can choose a simpler strategy instead of `full` KAT:

| Strategy       | Behavior                                                           |
| -------------- | ------------------------------------------------------------------ |
| `single`       | Route every query to the only knowledge base.                      |
| `fan_out`      | Query every knowledge base in parallel and merge results.          |
| `llm_classify` | An LLM classifies the query and picks the relevant knowledge base. |

You can change the strategy from the deployment dashboard. See [Configure operating parameters](/guides/marketplace/configure-operating-parameters). For selection guidance across all strategies, see [Multi-domain routing](/guides/marketplace/multi-domain-routing).

## Manifests

A manifest is an automatically generated description of what a knowledge base can answer, what is in scope, and what is out of scope. Manifests are central to how KAT routes queries, disambiguates, and refuses out-of-scope questions.

### Why manifests exist

Without a manifest, KAT would have to retrieve from every knowledge base on every query to discover whether it can answer. With manifests, KAT can pick the right knowledge base before retrieving, refuse out-of-scope questions cleanly instead of producing low-confidence answers, and ask for missing slots only when they would change the answer.

### How a manifest is built

Manifests are built through **progressive introspection**. After publish, Marketplace probes each knowledge base with sampled questions and uses the responses to construct the manifest. Introspection covers the high-level topics the knowledge base can answer, the kinds of questions that are clearly in or out of scope, required slots that change the answer, and suggested starter prompts for the consumer interface.

Introspection runs on initial publish, on republish after major content changes, and when you trigger a manual rebuild from the deployment dashboard.

### Reviewing a manifest

The deployment dashboard shows each knowledge base's current manifest. You can see what KAT considers in scope and out of scope, the slots KAT will ask about, and the starter prompts generated from the content.

Manifests are generated automatically; you do not author them by hand. If a manifest does not match expectations, the right move is usually to adjust the knowledge base content, names, or descriptions and republish.

### Manifests and routing accuracy

Routing quality depends on manifest quality. Two practical guidelines:

* Keep knowledge bases focused. Broad, sprawling knowledge bases produce vague manifests and weaker routing.
* Re-run introspection after large content changes so the manifest stays in sync with reality.

## Disambiguation and slot filling

KAT is built around the assumption that not every question can be answered from the question alone. When information is missing or the question maps to more than one domain, KAT either asks the end user for clarification or routes intelligently based on prior turns.

### Disambiguation

When a question could be answered by multiple knowledge bases, or when an answer would change depending on missing context, KAT pauses to clarify. Disambiguation can take two forms:

* **Domain disambiguation**: KAT asks the end user which knowledge domain they meant.
* **Slot disambiguation**: KAT asks the end user for a specific value, such as a region or a product line.

In both cases, the consumer interface renders the prompt as a clarifying question. Once the end user responds, KAT proceeds with the original query plus the new context.

### Slots

A slot is a named piece of context KAT needs to answer correctly. Common examples include region or location, plan tier or product line, effective date, and user role or persona. Slots can be:

* **Required**: KAT will not answer without the value. Missing required slots produce `ASK_SLOT`.
* **Optional**: KAT will use the slot if available and proceed without it otherwise.

The connected templates and configuration determine which slots are defined. You can review and adjust slots from the deployment dashboard.

### AgentContext and multi-turn behavior

KAT tracks slots and selected knowledge bases across turns through `AgentContext`. End users do not have to repeat themselves; once a value is set in the conversation, KAT carries it forward. `AgentContext` is per-conversation, so starting a new conversation resets context.

KAT only asks for clarification when it would meaningfully change the answer. If two knowledge bases return the same content, or if the missing slot does not affect routing, KAT proceeds without asking.

### Tuning disambiguation

If end users see too many clarifying questions, tighten manifests so domains have less overlap, reduce the number of required slots in the deployment configuration, or improve knowledge base names and descriptions so KAT picks correctly without asking.

If end users see too few clarifying questions and answers are inconsistent, add required slots for context that meaningfully changes the answer, or split an overly broad knowledge base into focused domains.

## Guardrails and scope

A knowledge application should be honest about what it can and cannot answer. KAT enforces two kinds of refusal: **out-of-scope** and **blocked**.

### Out-of-scope refusals

A query is out of scope when no knowledge base in the deployment has the information to answer it. KAT returns `OUT_OF_SCOPE` and the consumer interface shows a refusal that lists what the application can help with instead.

Examples of out-of-scope behavior:

* An HR Benefits application is asked about a competitor's product features.
* A Customer Support application for one product is asked about a different product line.
* A Legal Document Search application is asked for general legal advice.

Out-of-scope refusals are derived from the [manifests](#manifests) KAT builds for each knowledge base. Improving manifests usually improves out-of-scope accuracy.

### Blocked queries

A query is blocked when it violates a guardrail. KAT returns `BLOCKED` and the consumer interface shows a refusal explaining that the request cannot be processed.

Guardrails include refusing to produce content that violates the application's defined scope, refusing to surface content that has been excluded from the knowledge base by the operator, and refusing to return content for which the end user lacks authorization.

You configure scope and exclusion rules from the deployment dashboard.

### Citations and grounding

Every answer is grounded in retrieved content and includes citations. If KAT cannot ground an answer, it refuses rather than producing unsupported content. This is the most important guardrail in the system. For end-user-facing detail on how citations work, see [Understand answers](/guides/marketplace/end-user/citations).

### Tuning the balance

If the application refuses too often, add or expand knowledge bases to cover the missing topics, re-run introspection so manifests reflect new content, or loosen scope rules where appropriate.

If the application answers things it should not, tighten scope rules, split overly broad knowledge bases into focused domains, or add explicit exclusion rules for topics the application must not discuss.

### Observability

Every refusal is logged with the outcome (`BLOCKED` or `OUT_OF_SCOPE`) and the originating query. Use the deployment dashboard to identify questions that should be answered but are being refused, and the other way around. See [Analytics and event logs](/guides/marketplace/analytics-and-event-logs).
