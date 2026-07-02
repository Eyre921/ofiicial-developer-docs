---
title: "Configure layouts"
source: https://docs.pinecone.io/guides/marketplace/configure-layouts
path: guides/marketplace/configure-layouts
---

Choose the consumer layout for a Pinecone Marketplace knowledge application.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

A layout is the high-level shape of the consumer interface. Marketplace provides four layouts. Each [template](/guides/marketplace/templates-overview) suggests a default layout, which you can override.

## Chat

A conversational thread with a single input box. Each turn shows the question, the answer with inline citations, and any rendered components. Suggested follow-ups appear after each answer.

Best for:

* Open-ended Q\&A across documents.
* Long-running conversations where context carries between turns.

Templates that recommend chat: Customer Support, HR Benefits, Onboarding and Training, Local Government Citizen Engagement.

## Search

A query box with ranked results, source previews, and an "answer" panel that summarizes the top matches with citations.

Best for:

* Finding a specific clause, document, or passage.
* Domains where the end user wants to scan multiple results before drilling in.

Templates that recommend search: Legal Document Search, Financial Filings Analyzer.

## Structured

Form-style inputs that guide the end user to provide the information needed for a structured answer, such as a comparison table or a coverage matrix.

Best for:

* Repeatable, parameterized tasks such as deal sizing or coverage lookups.
* Workflows where end users want a consistent output shape every time.

Templates that recommend structured: Deal Desk.

## Hybrid

Chat plus a persistent structured panel. The chat handles open-ended questions, and the panel shows visual components such as comparison tables, timelines, or coverage matrices that update as the conversation progresses.

Best for:

* Workflows that mix exploration with reference output.
* Sales, legal, or research tasks where the end user wants both an answer and a working surface.

Templates that recommend hybrid: Sales Enablement, Event Management.

## Switching layouts

You can change a deployment's layout from the dashboard. Switching layouts creates a new building version and may require you to enable or disable specific [components](/guides/marketplace/configure-components). Publish the new version to apply the change.
