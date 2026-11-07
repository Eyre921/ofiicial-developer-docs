---
title: "Context snippets overview"
source: https://docs.pinecone.io/guides/assistant/context-snippets-overview
path: guides/assistant/context-snippets-overview
---

Learn how Pinecone Assistant retrieves context snippets with relevancy scores and references for RAG applications and agentic workflows.

You can [retrieve the context snippets](/guides/assistant/retrieve-context-snippets) that Pinecone Assistant uses to generate its responses. This data includes relevant chunks, relevancy scores, and references.

## Use cases

Retrieve context snippets to:

* Understand what relevant data snippets Pinecone Assistant provides to the LLM for chat generation.
* Use the retrieved snippets with your own LLM.
* Use the retrieved snippets with your own RAG application or agentic workflow.

## SDK support

The Pinecone [Python SDK](/reference/sdks/python/overview) and [Node.js SDK](/reference/sdks/node/overview) can [retrieve context snippets](/reference/api/latest/assistant/context_assistant).

## Pricing

Context retrieval usage is [measured in tokens](/guides/assistant/pricing-and-limits#token-usage), similar to Pinecone Assistant. See [Pricing](https://www.pinecone.io/pricing/) for up-to-date pricing information.

> [!NOTE]
>
> Pricing updates specific to context retrieval will be made as the feature becomes generally available.
