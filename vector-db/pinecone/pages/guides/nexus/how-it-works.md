---
title: "How Nexus works"
source: https://docs.pinecone.io/guides/nexus/how-it-works
path: guides/nexus/how-it-works
---

How Nexus distills curated artifacts for retrieval, then answers with code over a retrieval SDK.

Most RAG systems chop documents into chunks and hope the right ones surface at query time. Pinecone Nexus does the hard work *up front*: it distills your sources into curated artifacts so the information an answer needs is already organized and easy to find, then answers questions by writing code over a retrieval SDK.

At a high level, your data flows through connectors into contexts, tasks curate each context into knowledge, and agents query it through a single KnowQL interface:

<img alt="Pinecone Nexus architecture: your data enters through connectors into a workspace of contexts and tasks, is curated into knowledge in a sandbox, then queried through KnowQL to serve your AI application." />

<img alt="Pinecone Nexus architecture: your data enters through connectors into a workspace of contexts and tasks, is curated into knowledge in a sandbox, then queried through KnowQL to serve your AI application." />

The rest of this page zooms into the two ideas that make that work: curated artifacts for retrieval, and answering with code.

## Curated artifacts

Raw chunks are noisy. The same fact is scattered across pages, counts require reading everything, and relationships are implicit. Curation reorganizes the corpus into artifacts, which are condensed, typed units of knowledge, so retrieval gets a head start.

<img alt="Raw chunks reorganized into curated artifacts" />

<img alt="Raw chunks reorganized into curated artifacts" />

* **Pre-computed, typed knowledge.** Curation produces artifacts by kind: summaries, topics, entities, events, per-doc and per-page units. Each is small, focused, and describes itself, so the right one is easy to retrieve.
* **Structure for exact answers.** Structured artifact types become queryable tables, so "how many" and "list every…" questions get exact answers instead of a guess from prose.
* **Relationships made explicit.** Edge types connect artifacts (who mentions what, what happened when), turning a flat pile of text into a graph you can walk.

## Answering with code

Curated artifacts are only half the story. At query time the model doesn't just stuff chunks into a prompt. It writes Python against a retrieval SDK to gather exactly the evidence it needs, then answers from that.

<img alt="Question to generated retrieval code over artifacts to evidence to answer" />

<img alt="Question to generated retrieval code over artifacts to evidence to answer" />

* **The model orchestrates retrieval.** One turn can read artifacts off disk, run semantic and keyword search, walk the relationship graph, and query structured tables, composing several operations instead of a single top-k lookup.
* **Only evidence enters the prompt.** Raw tool output stays in the code sandbox. Just the distilled evidence the agent selected reaches the model. That keeps context small and answers grounded, and every claim traces to a source.
* **It can iterate.** If the first pass isn't enough, the agent refines its code and searches again, so hard questions get more work, not a worse answer.

## Benefits

Distilling artifacts up front plus writing retrieval code at query time means higher-quality answers on large, messy corpora: exact counts, real relationships, and citations you can trust, without dumping everything into the model's context.
