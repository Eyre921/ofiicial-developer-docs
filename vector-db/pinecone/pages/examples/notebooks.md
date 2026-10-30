---
title: "Notebooks"
source: https://docs.pinecone.io/examples/notebooks
path: examples/notebooks
---

Runnable Colab notebooks covering semantic search, lexical search, hybrid search, RAG, embeddings, reranking, and data ingestion with Pinecone.

## Search

## [Full-text search](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/full-text-search.ipynb)

Search typed JSON documents using BM25 scoring, Lucene query syntax, dense vector ranking of images.

Full-text search

BM25

gemini-embedding-2

## [Semantic search](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb)

Implement semantic search over an index with dense vectors to find records that are similar in meaning to a given query.

Integrated embedding

![](/images/examples/huggingface-icon.svg)
Hugging Face Datasets

llama-text-embed-v2

## [Lexical search](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/lexical-search.ipynb)

Implement lexical search over an index of sparse vectors to find records that most exactly match the words or phrases in a query.

Integrated embedding

Integrated reranking

pinecone-sparse-english-v0

bge-reranker-v2-m3

## [Cascading retrieval](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/cascading-retrieval.ipynb)

Implement cascading retrieval (hybrid search with two indexes) to combine the benefits of semantic and lexical search.

Integrated embedding

Standalone reranking

llama-text-embed-v2

pinecone-sparse-english-v0

bge-reranker-v2-m3

## [Reranking search results](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-reranker.ipynb)

Use Pinecone's reranking feature to enhance the accuracy of search results.

Standalone reranking

![](https://cdn.sanity.io/images/vr8gru94/production/40b1d05ee1325e6d9e4886af4e76ff06d844faff-188x188.jpg)
bge-reranker-v2-m3

## Retrieval-augmented generation (RAG)

## [RAG with hybrid search and Claude](https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/traditional-rag/traditional-rag-with-claude-and-hybrid.ipynb)

Implement simple retrieval-augmented generation with hybrid search and Anthropic's Claude models

claude-3-5-haiku-latest

llama-text-embed-v2

pinecone-sparse-english-v0

Dense Indexes

Sparse Indexes

Hybrid Search

## [Agentic RAG with Claude](https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/agentic-rag/agentic-rag-with-claude.ipynb)

Build an agentic RAG pipeline that uses tools to retrieve data from web search and Pinecone semantic search, then generates responses using Anthropic's Claude models

claude-3-5-haiku-latest

llama-text-embed-v2

Dense Indexes

Tool use

## [RAG with LangChain and OpenAI](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-augmentation.ipynb)

Learn how RAG can be used with Pinecone to reduce hallucinations, by grounding responses using our own release notes

![](/images/examples/openai-icon.svg)
gpt-5

![](/images/examples/openai-icon.svg)
text-embedding-3-small

OpenAI

LangChain

## [RAG with LlamaIndex and OpenAI](https://colab.research.google.com/github/pinecone-io/examples/blob/main/learn/generation/llama-index/using-llamaindex-with-pinecone.ipynb)

Load a research paper with LlamaIndex, search it in Pinecone, and evaluate the relevance of the LLM's answers

![](/images/examples/openai-icon.svg)
gpt-4o-mini

![](/images/examples/openai-icon.svg)
text-embedding-3-small

OpenAI

LlamaIndex

## [RAG with cascading retrieval and OpenAI](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb)

Investigate research papers by implementing cascading retrieval, then pass results to OpenAI to generate answers

![](/images/examples/openai-icon.svg)
gpt-4o-mini

llama-text-embed-v2

pinecone-sparse-english-v0

Dense Indexes

Sparse Indexes

Cascading Retrieval

## [Retrieval agent with LangChain and OpenAI](https://colab.research.google.com/github/pinecone-io/examples/blob/main/learn/generation/langchain/handbook/08-langchain-retrieval-agent.ipynb)

Build a conversational agent with memory that decides when to search a Pinecone index for context

![](/images/examples/openai-icon.svg)
gpt-4o-mini

![](/images/examples/openai-icon.svg)
text-embedding-3-small

OpenAI

LangChain

![](/images/examples/huggingface-icon.svg)
Hugging Face Datasets

## [Retrieval Agents with Pinecone Assistant, LangChain and LangGraph](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-agent.ipynb)

Create a study guide generator using agentic retrieval and the Pinecone Assistant Context API

![](/images/examples/openai-icon.svg)
gpt-4o-mini

![](/images/examples/openai-icon.svg)
gpt-4.1

LangChain

LangGraph

Agentic Retrieval

Structured Generation

## Miscellaneous

## [Import from object storage](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-import.ipynb)

Import documents from JSONL files in an Amazon S3 bucket into a document index

Amazon S3
