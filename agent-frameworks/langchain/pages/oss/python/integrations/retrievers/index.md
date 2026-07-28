---
title: "Retriever integrations"
source: https://docs.langchain.com/oss/python/integrations/retrievers/index
path: oss/python/integrations/retrievers/index
---

Integrate with retrievers using LangChain Python.

A [retriever](/oss/python/deepagents/retrieval#building-blocks) is an interface that returns documents given an unstructured query.
It is more general than a vector store.
A retriever does not need to be able to store documents, only to return (or retrieve) them.
Retrievers can be created from vector stores, but are also broad enough to include other sources.

Retrievers accept a string query as input and return a list of [`Document`](https://reference.langchain.com/python/langchain-core/documents/base/Document) objects as output.

Note that all [vector stores](/oss/python/integrations/vectorstores) can be cast to retrievers. Refer to the vector store [integration docs](/oss/python/integrations/vectorstores/) for available vector stores.
This page lists custom retrievers, implemented via subclassing BaseRetriever.

## Bring-your-own documents

The below retrievers allow you to index and search a custom corpus of documents.

| Retriever                                                                                | Self-host | Cloud offering | Package                                                                                                                                    |
| ---------------------------------------------------------------------------------------- | --------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [`AmazonKnowledgeBasesRetriever`](/oss/python/integrations/retrievers/bedrock)           | ❌         | ✅              | [`langchain-aws`](https://reference.langchain.com/python/langchain-aws/retrievers/bedrock/AmazonKnowledgeBasesRetriever)                   |
| [`ElasticsearchRetriever`](/oss/python/integrations/retrievers/elasticsearch_retriever)  | ✅         | ✅              | [`langchain-elasticsearch`](https://reference.langchain.com/python/langchain-elasticsearch/retrievers/ElasticsearchRetriever)              |
| [`NVIDIARAGRetriever`](/oss/python/integrations/retrievers/nvidia)                       | ✅         | ❌              | [`langchain-nvidia-ai-endpoints`](https://reference.langchain.com/python/langchain-nvidia-ai-endpoints/retrievers/NVIDIARAGRetriever)      |
| [`VertexAISearchRetriever`](/oss/python/integrations/retrievers/google_vertex_ai_search) | ❌         | ✅              | [`langchain-google-community`](https://reference.langchain.com/python/langchain-google-community/vertex_ai_search/VertexAISearchRetriever) |

## External index

The below retrievers will search over an external index (e.g., constructed from Internet data or similar).

| Retriever                                                                            | Source                                                                                             | Package                                                                                                                    |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [`ParallelSearchRetriever`](/oss/python/integrations/retrievers/parallel)            | Internet search via the [Parallel Search API](https://docs.parallel.ai/search/search-quickstart)   | [`langchain-parallel`](https://reference.langchain.com/python/langchain-parallel/retrievers/ParallelSearchRetriever)       |
| [`PerplexitySearchRetriever`](/oss/python/integrations/retrievers/perplexity_search) | Internet search via the [Perplexity Search API](https://docs.perplexity.ai/docs/search/quickstart) | [`langchain-perplexity`](https://reference.langchain.com/python/langchain-perplexity/retrievers/PerplexitySearchRetriever) |
| [`YouRetriever`](/oss/python/integrations/retrievers/you-retriever)                  | Internet search                                                                                    | [`langchain-youdotcom`](https://pypi.org/project/langchain-youdotcom/)                                                     |

## All retrievers

<Columns>
  <Card title="AgentMail" icon="link" href="/oss/python/integrations/retrievers/agentmail" />

  <Card title="Bedrock (Knowledge Bases)" icon="link" href="/oss/python/integrations/retrievers/bedrock" />

  <Card title="Box" icon="link" href="/oss/python/integrations/retrievers/box" />

  <Card title="Cognee" icon="link" href="/oss/python/integrations/retrievers/cognee" />

  <Card title="Cohere reranker" icon="link" href="/oss/python/integrations/retrievers/cohere-reranker" />

  <Card title="Cohere RAG" icon="link" href="/oss/python/integrations/retrievers/cohere" />

  <Card title="Contextual AI Reranker" icon="link" href="/oss/python/integrations/retrievers/contextual" />

  <Card title="Dappier" icon="link" href="/oss/python/integrations/retrievers/dappier" />

  <Card title="Elasticsearch" icon="link" href="/oss/python/integrations/retrievers/elasticsearch_retriever" />

  <Card title="Egnyte" icon="link" href="/oss/python/integrations/retrievers/egnyte" />

  <Card title="Galaxia" icon="link" href="/oss/python/integrations/retrievers/galaxia-retriever" />

  <Card title="Google Drive" icon="link" href="/oss/python/integrations/retrievers/google_drive" />

  <Card title="Google Vertex AI Search" icon="link" href="/oss/python/integrations/retrievers/google_vertex_ai_search" />

  <Card title="Graph RAG" icon="link" href="/oss/python/integrations/retrievers/graph_rag" />

  <Card title="GreenNode" icon="link" href="/oss/python/integrations/retrievers/greennode_reranker" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/python/integrations/retrievers/ibm_watsonx_ranker" />

  <Card title="IMAP" icon="link" href="/oss/python/integrations/retrievers/imap" />

  <Card title="Kinetica Vectorstore" icon="link" href="/oss/python/integrations/retrievers/kinetica" />

  <Card title="LinkupSearchRetriever" icon="link" href="/oss/python/integrations/retrievers/linkup_search" />

  <Card title="Nebius" icon="link" href="/oss/python/integrations/retrievers/nebius" />

  <Card title="Nimble Extract" icon="link" href="/oss/python/integrations/retrievers/nimble_extract" />

  <Card title="Nimble Search" icon="link" href="/oss/python/integrations/retrievers/nimble_search" />

  <Card title="NVIDIA RAG Blueprint" icon="link" href="/oss/python/integrations/retrievers/nvidia" />

  <Card title="Parallel Search" icon="link" href="/oss/python/integrations/retrievers/parallel" />

  <Card title="Permit" icon="link" href="/oss/python/integrations/retrievers/permit" />

  <Card title="Perigon" icon="link" href="/oss/python/integrations/retrievers/perigon" />

  <Card title="Perplexity Search" icon="link" href="/oss/python/integrations/retrievers/perplexity_search" />

  <Card title="Pinecone Rerank" icon="link" href="/oss/python/integrations/retrievers/pinecone_rerank" />

  <Card title="RAGatouille" icon="link" href="/oss/python/integrations/retrievers/ragatouille" />

  <Card title="Sourcey" icon="link" href="/oss/python/integrations/retrievers/sourcey" />

  <Card title="SpiceDB" icon="link" href="/oss/python/integrations/retrievers/spicedb" />

  <Card title="ValyuContext" icon="link" href="/oss/python/integrations/retrievers/valyu" />

  <Card title="Vectorize" icon="link" href="/oss/python/integrations/retrievers/vectorize" />

  <Card title="You.com" icon="link" href="/oss/python/integrations/retrievers/you-retriever" />

  <Card title="Zotero" icon="link" href="/oss/python/integrations/retrievers/zotero" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/retrievers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
