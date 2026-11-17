---
title: "Nexus architecture"
source: https://docs.pinecone.io/guides/nexus/architecture
path: guides/nexus/architecture
---

Pinecone Nexus curates your sources into typed artifacts, then answers queries by writing code against a retrieval SDK.

Pinecone Nexus curates your sources into artifacts before any query runs, so the information an answer needs is already organized. At query time, the model answers by writing Python against a retrieval SDK.

## Data flow

Your data flows through connectors into contexts. Tasks curate each context into knowledge, and agents query it through a single KnowQL interface.

![The Pinecone Nexus architecture from top to bottom. Your data (docs and wikis, databases, APIs and SaaS, object storage, event streams, code repos) flows through connectors such as Google Drive, Box, Slack, GitHub, Notion, Confluence, and S3 into the Nexus knowledge engine. Inside a workspace, each dataset becomes a context of sources, a manifest, and knowledge, maintained by sandboxed tasks (import, curate, explore, optimize, search). A single KnowQL interface queries it to serve your AI application, from chatbots and Q\&A to search, agents, recommendations, and reporting.](https://mintcdn.com/pinecone/EWF4J3kPxqsT4ELV/images/nexus/nexus-architecture-light.svg?fit=max\&auto=format\&n=EWF4J3kPxqsT4ELV\&q=85\&s=968e4074b4b6b479bab6ebae47fecf73)

## Curated artifacts

In raw chunks, the same fact is scattered across pages, counting anything means reading everything, and relationships between documents are implicit. Curation reorganizes the corpus into artifacts, which are condensed, typed units of knowledge.

![Raw chunks reorganized into curated artifacts](https://mintcdn.com/pinecone/EWF4J3kPxqsT4ELV/images/nexus/how-it-works-1-light.svg?fit=max\&auto=format\&n=EWF4J3kPxqsT4ELV\&q=85\&s=eef0fc626b3d0ce21845757867d5381f)

* **Typed knowledge:** Curation produces summaries, topics, entities, events, glossaries, and per-document and per-page artifacts. Each one is small and describes itself, which makes it easier to retrieve.
* **Structured tables:** Structured artifact types become queryable tables, so "how many" and "list every" questions get exact answers rather than estimates from prose.
* **Relationships:** Typed edges connect artifacts, such as a document to the entities it mentions, so the model can walk the knowledge as a graph.

## Answering with code

At query time, the model [writes Python against a retrieval SDK](/guides/nexus/queries) to gather the evidence it needs, then answers from that evidence.

![Question to generated retrieval code over artifacts to evidence to answer](https://mintcdn.com/pinecone/EWF4J3kPxqsT4ELV/images/nexus/queries-light.svg?fit=max\&auto=format\&n=EWF4J3kPxqsT4ELV\&q=85\&s=fbb7818dc5c26a7ede110869e776d556)

* **Combined operations:** One turn can read artifacts from disk, run semantic and keyword search, walk the graph, and query tables, rather than run a single top-k lookup.
* **Selected evidence:** Search results stay in the sandbox as Python variables, and only what the code prints reaches the model. Every claim in the answer traces to a source.
* **Iteration:** If the first pass doesn't find enough, the model refines its code and searches again, so a hard question gets more steps.
