---
title: "Multi-domain routing"
source: https://docs.pinecone.io/guides/marketplace/multi-domain-routing
path: guides/marketplace/multi-domain-routing
---

How KAT routes queries across multiple knowledge bases in a Pinecone Marketplace deployment.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

A multi-domain deployment has more than one knowledge base. Each knowledge base represents a domain, such as HR policies, product documentation, or contracts. The Knowledge Agent Toolkit (KAT) routes every query to the right knowledge bases at runtime so the end user gets a single coherent answer.

For an introduction, see [KAT overview](/guides/marketplace/kat-overview).

## How routing decisions are made

When an end user asks a question, KAT:

1. Extracts intent and any slot values from the query.
2. Looks up each knowledge base's [manifest](/guides/marketplace/kat-overview#manifests) to determine which domains can answer.
3. Picks one or more knowledge bases to query based on relevance and required slots.
4. Issues retrieval calls in parallel.
5. Synthesizes a single answer from the results, with citations.

If no knowledge base can answer the question, KAT returns `OUT_OF_SCOPE`. If a needed slot is missing, KAT returns `ASK_SLOT`.

## Designing knowledge bases for routing

Routing works best when knowledge bases have non-overlapping scope. Some practical guidance:

* Group documents by domain, not by source. A single knowledge base can mix sources from one domain; a single source can be split across knowledge bases if needed.
* Give each knowledge base a name and description that reflects its scope.
* Re-run introspection after major content changes so the manifest stays accurate.

## When to use which strategy

For what each strategy does, see [KAT overview](/guides/marketplace/kat-overview#execution-modes). The table below is selection guidance.

| Strategy                  | Use it when                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| `full` KAT                | You have multiple domains and want disambiguation, slot filling, and consistent synthesis. |
| `disambiguation_only` KAT | You want KAT's routing but want Pinecone Assistant to handle synthesis.                    |
| `single`                  | You have one knowledge base and want minimal overhead.                                     |
| `fan_out`                 | Domains overlap and you want every knowledge base to weigh in on every query.              |
| `llm_classify`            | You want lightweight classification without the full KAT pipeline.                         |

## Mixing knowledge bases of different sizes

Knowledge bases do not need to be the same size. KAT uses manifests, not document counts, to make routing decisions. A small knowledge base with a focused scope routes just as cleanly as a large one with broad coverage.

## Observability

The deployment dashboard logs every routing decision with the outcome (`CALL_KB`, `ASK_SLOT`, `BLOCKED`, or `OUT_OF_SCOPE`) and the knowledge bases queried. Use this to identify questions that consistently land on the wrong knowledge base or get refused unexpectedly. See [Analytics and event logs](/guides/marketplace/analytics-and-event-logs).
