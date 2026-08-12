---
title: "Configure operating parameters"
source: https://docs.pinecone.io/guides/marketplace/configure-operating-parameters
path: guides/marketplace/configure-operating-parameters
---

Tune the system prompt, starter prompts, and response style of a Pinecone Marketplace knowledge application through operating parameter settings.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Operating parameters control how a knowledge application responds. They are set initially by the [template](/guides/marketplace/templates-overview) and can be overridden at any time from the deployment dashboard.

## System prompt

The system prompt sets the application's voice, tone, and high-level instructions. Each template ships with a system prompt tuned for its vertical. Use the system prompt to:

* Define the application's persona and tone.
* Constrain what topics the application will engage with.
* Specify formatting preferences, such as bullet lists or short paragraphs.

<Tip>
  Keep the system prompt focused. Use [KAT guardrails](/guides/marketplace/kat-overview#guardrails-and-scope) for hard policy rules and the system prompt for tone and style.
</Tip>

## Starter prompts

Starter prompts are the suggestions end users see in the empty state of the consumer interface. Marketplace generates starter prompts automatically on publish based on the connected sources, and you can edit or replace them.

## Response style

Configure response defaults such as:

* **Length**: short, medium, or long.
* **Citations**: required, preferred, or optional.
* **Refusal behavior**: how the application phrases out-of-scope refusals.

## Suggested follow-ups

Enable suggested follow-ups so that the consumer interface offers next questions after each answer. Suggested follow-ups are generated from the response and the connected sources.

## Routing strategy

Choose how queries are routed across knowledge bases. The available strategies and execution modes (`full`, `disambiguation_only`, `single`, `fan_out`, `llm_classify`) are defined in [Knowledge Agent Toolkit (KAT) overview](/guides/marketplace/kat-overview); for selection guidance, see [Multi-domain routing](/guides/marketplace/multi-domain-routing).

## Apply changes

Edits to operating parameters create a new building version. Publish the version to send the changes to end users. See [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).
