---
title: "n8n"
source: https://docs.pinecone.io/integrations/n8n
path: integrations/n8n
---

Use the Pinecone Vector Store and Pinecone Assistant nodes in n8n to build RAG pipelines, semantic search, and no-code AI automations with 400+ apps.

n8n is a workflow automation platform that combines AI capabilities with business process automation. Add the Pinecone Vector Store or Pinecone Assistant nodes to your automation pipelines to build AI workflows with vector search and retrieval.

Released under a fair-code license, n8n can be self-hosted and is supported by a community of developers and builders. Use the visual builder for simple workflows and add custom JavaScript or Python where you need more control.

## Two ways to use Pinecone in n8n

Use the Pinecone Vector Store node for full control over RAG pipelines. It gives you direct access to Pinecone Database, so you can choose embedding models, customize chunking, and control search (semantic, lexical, or hybrid). It works well for wiring up custom nodes for each step and tuning everything to a specific use case. See the [Pinecone Vector Store integration on n8n](https://n8n.io/integrations/pinecone-vector-store/) for node docs, supported modes (insert, retrieve, update), and workflow templates.

Use the Pinecone Assistant node for managed RAG with minimal setup. Upload files (PDF, DOCX, TXT, JSON, Markdown), connect any data source, and get knowledge retrieval that's ready for production. One node handles chunking, embedding, vector search, query planning, and reranking. It works well for AI workflows that need trusted, grounded context without configuring pipelines. See the [Pinecone Assistant integration on n8n](https://n8n.io/integrations/pinecone-assistant/) for installation and workflow templates.

The following quickstart uses the **Pinecone Assistant** node.

<PrimarySecondaryCTA />

## Getting started (Pinecone Assistant)

Follow the [complete Pinecone Assistant quickstart guide](/guides/assistant/quickstart/n8n-quickstart) to do the following:

* Install the Pinecone Assistant node in n8n
* Get your API keys
* Create your first assistant
* Import a ready-to-use workflow template
* Start chatting with your documents

You can also use the [n8n skill](/integrations/ai-coding-tools) to build n8n workflows in AI coding tools like Claude Code and Cursor.
