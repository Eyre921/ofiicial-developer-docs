---
title: "n8n"
source: https://docs.pinecone.io/integrations/n8n
path: integrations/n8n
---

Connect Pinecone and n8n to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

n8n is a workflow automation platform that combines AI capabilities with business process automation, giving technical teams the flexibility of code with the speed of no-code. Integrate Pinecone Vector Database or Pinecone Assistant nodes directly into your automation pipelines to build powerful AI workflows with vector search and retrieval.

Released under a fair-code license, n8n can be self-hosted and is supported by a vibrant community of developers and builders. Use the visual builder for quick wins and add custom Javascript or Python where you need more control.

## Two ways to use Pinecone in n8n

**[Pinecone Vector Store integration on n8n](https://n8n.io/integrations/pinecone-vector-store/)** — Use this for full control over RAG pipelines. Provides direct access to Pinecone's vector database so you can choose embedding models, customize chunking, and control search (semantic, lexical, or hybrid). Ideal for wiring up custom nodes for each step and tuning everything to specific use cases. See the [Pinecone Vector Store integration on n8n](https://n8n.io/integrations/pinecone-vector-store/) for node docs, supported modes (insert, retrieve, update), and workflow templates.

**[Pinecone Assistant integration on n8n](https://n8n.io/integrations/pinecone-assistant/)** — Use this for managed RAG with minimal setup. Upload files (PDF, DOCX, TXT, JSON, Markdown), connect any data source, and get production-ready knowledge retrieval. One node handles chunking, embedding, vector search, query planning, and reranking. Ideal for building AI workflows that need trusted, grounded context without configuring pipelines. See the [Pinecone Assistant integration on n8n](https://n8n.io/integrations/pinecone-assistant/) for installation and workflow templates.

The quickstart below uses the **Pinecone Assistant** node.

<PrimarySecondaryCTA />

## Getting started (Pinecone Assistant)

Follow our [complete Assistant quickstart guide](/guides/assistant/quickstart/n8n-quickstart) to:

* Install the Pinecone Assistant node in n8n
* Get your API keys
* Create your first assistant
* Import a ready-to-use workflow template
* Start chatting with your documents
