---
title: "Pinecone Nexus"
source: https://docs.pinecone.io/guides/nexus/overview
path: guides/nexus/overview
---

Pinecone Nexus is the knowledge engine for agents. It compiles your data into queryable knowledge once, then serves grounded, cited answers on every call.

You point Nexus at your sources and curate them into a context. Agents then query that context with a single call and get back a structured, grounded answer with citations, instead of re-assembling context from raw chunks on every request.

Traditional RAG hands an agent ranked chunks and leaves it to search, stitch, and re-search. Nexus does that work once, upstream, so agents spend their budget on reasoning instead of re-orienting.

> [card] [Quickstart](/guides/nexus/quickstart)
>
> Prepare your first context, then query it

> [card] [Key concepts](/guides/nexus/concepts)
>
> Contexts, manifests, artifacts, sessions, and the Query API

> [card] [How Nexus works](/guides/nexus/how-it-works)
>
> Curated artifacts for retrieval, then answers composed over a retrieval SDK

> [card] [Context design](/guides/nexus/context-design)
>
> How a context's manifest turns your sources into queryable knowledge

> [card] [Bring Your Own Cloud](/guides/nexus/byoc/overview)
>
> Deploy Nexus in your own cloud account

> [card] [MCP server](/guides/nexus/mcp-server)
>
> Query your contexts from any MCP client

## What you can do

With Pinecone Nexus, you can:

* Turn raw sources into queryable knowledge. Upload documents or connect a data source, then curate them into a searchable context, without building a chunking pipeline or an eval set by hand.
* Get an answer in one call. Agents issue a KnowQL query (`ask` plus `scope`, optionally a typed `shape`) and get back a grounded, cited answer. Each query is a turn, and multi-turn conversations are sessions.
* Query across domains. A single query can span multiple contexts, so your knowledge forms a graph of contexts instead of one large index.
* Keep answers grounded and scoped. Every answer carries citations, and access is scoped to your Pinecone project.

## Why Nexus

The most expensive part of an agent is knowledge acquisition. Agents built on raw retrieval burn tokens re-orienting on every call and loop through retrieve, evaluate, and re-retrieve cycles. Nexus compiles the knowledge once and serves it on every call:

* It's cheaper than agentic RAG. The expensive work happens once at curation time instead of on every query, so agents spend far fewer tokens.
* It's faster than a retrieval loop. A single query replaces the multi-step retrieve, evaluate, and re-retrieve cycle.
* Its answers are trusted and grounded. Each answer carries citations and is scoped to your Pinecone project, with Pinecone Database running underneath.

## What Nexus is not

Nexus is sometimes confused with other kinds of AI tools. Here's how it differs:

* Nexus isn't a vector database. Pinecone Database sits underneath Nexus as its retrieval layer, and Nexus is the engine layer above it.
* Nexus isn't RAG. RAG returns ranked chunks for a human to read, while Nexus compiles typed, grounded artifacts for agents and returns answers.
* Nexus isn't an agent framework. Your agent sends Nexus a query, gets back an answer, and decides what to do with it.

## Resources

> [card] [API reference](/reference/api/nexus/introduction)
>
> Details about the Nexus control plane and data plane APIs

> [card] [Changelog](/release-notes)
>
> What's new in Pinecone

## Other Pinecone products

> [card] [Pinecone Database](/guides/get-started/overview)
>
> The retrieval foundation, bringing full-text and semantic search with metadata filtering into one managed database

> [card] [Pinecone Assistant](/guides/assistant/overview)
>
> A managed service for RAG chat and agent applications grounded in your data
