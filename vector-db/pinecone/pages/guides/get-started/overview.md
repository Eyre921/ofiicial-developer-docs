---
title: "Pinecone Database"
source: https://docs.pinecone.io/guides/get-started/overview
path: guides/get-started/overview
---

Pinecone Database is a search engine for AI agents and applications. It serves full-text, semantic, and sparse-vector search and retrieval from one index.

Pinecone Database powers retrieval for AI agents and applications, including search, recommendations, and long-term memory. You build on one API, the [Documents API](/guides/get-started/documents-api). You write JSON documents with your own field names, and the index schema declares how each searchable field is indexed, whether for full-text search, for embedding by Pinecone, or as a dense or sparse vector you bring. Any other field is stored as metadata you can filter on, so one index can serve whichever retrieval approach a query calls for.

## Get started

> [card] [Quickstart](/guides/get-started/quickstart)
>
> Pick a search path and run your first search in minutes

> [card] [AI coding tools](/integrations/ai-coding-tools)
>
> Use Pinecone with Claude Code, Codex, Cursor, and other agentic tools

> [card] [MCP server](/guides/agents/mcp-server)
>
> Connect any MCP-compatible agent to Pinecone for search and index management

## What you can do

With Pinecone Database, you can:

* Find exact IDs, codes, and phrases with [full-text search](/guides/search/full-text-search), which ranks with BM25, accepts Lucene query syntax, and lets you set stemming, stop words, and n-grams per field.
* Serve full-text search, [semantic search](/guides/search/semantic-search), [sparse-vector search](/guides/search/sparse-vector-search), and [hybrid search](/guides/search/hybrid-search) from one index. To choose an approach, see [Search overview](/guides/search/search-overview).
* Upsert and query with text instead of vectors. With [integrated embedding](/guides/indexes/index-data-overview#integrated-embedding), Pinecone generates the vectors from your text server-side.
* Narrow results with [metadata filters](/guides/search/filter-by-metadata), then [rerank](/guides/search/rerank-results) them for relevance.
* Keep each tenant's data separate within one index by using [namespaces](/guides/data/implement-multitenancy).
* Scale reads for sustained, high query volumes with [dedicated read nodes](/guides/optimize/dedicated-read-nodes/overview).
* On the Standard and Enterprise plans, [convert a legacy index](/guides/indexes/convert-an-index) to a document index without reloading your data. For the code changes, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).
* Run in production by [backing up](/guides/indexes/backups-overview) your indexes and deploying in your own cloud account with [Bring Your Own Cloud (BYOC)](/guides/production/bring-your-own-cloud).

## Learn

> [card] [Documents API](/guides/get-started/documents-api)
>
> One schema for your text, vectors, and metadata, searched through one API

> [card] [Key terms](/guides/get-started/key-terms)
>
> Organizations, projects, indexes, namespaces, documents, and records

> [card] [Data modeling](/guides/indexes/data-modeling)
>
> Design the fields your index needs for the searches you'll run

> [card] [Search overview](/guides/search/search-overview)
>
> Compare search types and choose the right approach for each query

## Resources

> [card] [API reference](/reference)
>
> Details about the Pinecone APIs, SDKs, and architecture

> [card] [Examples](/examples)
>
> Notebooks and sample apps with common AI patterns

> [card] [Models](/models/overview)
>
> Embedding and reranking models hosted by Pinecone

> [card] [Integrations](/integrations/overview)
>
> Third-party integrations for LangChain, LlamaIndex, and more

> [card] [Troubleshooting](/admin/support/contact-support)
>
> Common errors, account help, and how to contact support

> [card] [Changelog](/release-notes)
>
> What's new in Pinecone

## Other Pinecone products

> [card] [Pinecone Assistant](/guides/assistant/overview)
>
> A managed service for RAG chat and agent applications grounded in your data

> [card] [Pinecone Nexus](/guides/nexus/overview)
>
> The knowledge engine for agents, serving grounded, cited answers in one call
