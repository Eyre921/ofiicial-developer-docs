---
title: "Pinecone Database"
source: https://docs.pinecone.io/guides/get-started/overview
path: guides/get-started/overview
---

Pinecone Database is a search engine for AI agents and applications, built for semantic search, knowledge retrieval, and long-term memory at scale.

Pinecone Database powers retrieval for AI agents and applications, including search, recommendations, and long-term memory. Each index has a schema that declares the fields you need, such as full-text-search fields, dense vectors, and sparse vectors, so one index can serve whichever retrieval approach a query calls for.

## Get started

> **[Quickstart](/guides/get-started/quickstart)**
>
> Pick a search path and run your first search in minutes

> **[AI coding tools](/integrations/ai-coding-tools)**
>
> Use Pinecone with Claude Code, Codex, Cursor, and other agentic tools

> **[MCP server](/guides/operations/mcp-server)**
>
> Connect any MCP-compatible agent to Pinecone for search and index management

## What you can do

With Pinecone Database, you can:

* Serve [full-text search](/guides/search/full-text-search), [semantic search](/guides/search/semantic-search), [sparse-vector search](/guides/search/lexical-search), and [hybrid search](/guides/search/hybrid-search) from one index. To choose an approach, see [Search overview](/guides/search/search-overview).
* Upsert and query with text instead of vectors. With [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding), Pinecone generates the vectors from your text server-side.
* Narrow results with [metadata filters](/guides/search/filter-by-metadata), then [rerank](/guides/search/rerank-results) them for relevance.
* Keep each tenant's data separate within one index by using [namespaces](/guides/index-data/implement-multitenancy).
* Scale reads for sustained, high query volumes with [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview).
* Run in production by [backing up](/guides/manage-data/backups-overview) your indexes and deploying in your own cloud account with [Bring Your Own Cloud (BYOC)](/guides/production/bring-your-own-cloud).

## Learn

> **[Key terms](/guides/core-concepts/key-terms)**
>
> Organizations, projects, indexes, namespaces, documents, and records

> **[Data modeling](/guides/index-data/data-modeling)**
>
> Design the fields your index needs for the searches you'll run

> **[Search overview](/guides/search/search-overview)**
>
> Compare search types and choose the right approach for each query

## Resources

> **[API reference](/reference)**
>
> Details about the Pinecone APIs, SDKs, and architecture

> **[Examples](/examples)**
>
> Notebooks and sample apps with common AI patterns

> **[Models](/models/overview)**
>
> Embedding and reranking models hosted by Pinecone

> **[Integrations](/integrations/overview)**
>
> Third-party integrations for LangChain, LlamaIndex, and more

> **[Troubleshooting](/admin/support/contact-support)**
>
> Common errors, account help, and how to contact support

> **[Changelog](/release-notes)**
>
> What's new in Pinecone

## Other Pinecone products

> **[Pinecone Assistant](/guides/assistant/overview)**
>
> A managed service for RAG chat and agent applications grounded in your data

> **[Pinecone Nexus](/guides/nexus/overview)**
>
> The knowledge engine for agents, serving grounded, cited answers in one call
