---
title: "Pinecone Nexus"
source: https://docs.pinecone.io/guides/nexus/overview
path: guides/nexus/overview
---

Pinecone Nexus is the knowledge engine for agents. It compiles your data into queryable knowledge once, then serves grounded, cited answers to agents on every call.

You point Nexus at your sources and curate them into a context. Agents then query that context with a single call and get back a structured, grounded answer with citations, instead of re-assembling context from raw chunks on every request.

Traditional RAG hands an agent ranked chunks and leaves it to search, stitch, and re-search. Nexus does that work once, upstream, so agents spend their budget on reasoning instead of re-orienting.

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/guides/nexus/quickstart">
    Prepare your first context, then query it.
  </Card>

  <Card title="Key concepts" icon="book" href="/guides/nexus/concepts">
    Contexts, manifests, artifacts, sessions, and the Query API.
  </Card>

  <Card title="How Nexus works" icon="lightbulb" href="/guides/nexus/how-it-works">
    Curated artifacts for retrieval, then answers composed over a retrieval SDK.
  </Card>

  <Card title="Bring Your Own Cloud" icon="cloud" href="/guides/nexus/byoc/overview">
    Deploy Nexus in your own cloud account.
  </Card>
</CardGroup>

## What you can do

* **Turn raw sources into queryable knowledge.** Upload documents or connect a data source, then curate them into a searchable context. There is no chunking pipeline or eval set to hand-build.
* **Ask in one call.** Agents issue a KnowQL query (`ask` plus `scope`, optionally a typed `shape`) and get back a grounded, cited answer. One query is a turn. Multi-turn conversations are sessions.
* **Compose across domains.** A single query can span multiple contexts, so knowledge is a graph of contexts rather than one monolithic index.
* **Keep answers grounded and scoped.** Answers carry citations, and access is scoped to your Pinecone project.

## Why Nexus

The most expensive part of an agent is not reasoning. It is knowledge acquisition. Agents built on raw retrieval burn tokens re-orienting on every call and loop through retrieve, evaluate, and re-retrieve cycles. Nexus compiles the knowledge once and serves it on every call:

* **Cheaper than agentic RAG.** The expensive work happens once at curation time, not per query, so agents spend far fewer tokens.
* **Faster than a retrieval loop.** A single query replaces the multi-step retrieve, evaluate, and re-retrieve cycle.
* **Trusted, grounded answers.** Each one carries citations and is scoped to your Pinecone project, running on the Pinecone Database underneath.

## What Nexus is not

* **Not a vector database.** The Pinecone Database sits *underneath* Nexus as the retrieval substrate. Nexus is the engine layer above it.
* **Not RAG.** RAG returns ranked chunks for a human to read. Nexus compiles typed, grounded artifacts purpose-built for agents and returns answers.
* **Not an agent framework.** Nexus is knowledge infrastructure: query in, answer out. Your agent decides what to do with the answer.
