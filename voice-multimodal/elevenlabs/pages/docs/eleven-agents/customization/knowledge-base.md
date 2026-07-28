---
title: "Knowledge base"
source: https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base.md
path: docs/eleven-agents/customization/knowledge-base
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Knowledge base

A **knowledge base** is a collection of documents that give your agent domain-specific information beyond its pre-trained data. When a document is attached to an agent, the agent can draw on its contents to answer questions accurately and consistently.

To create, edit, and organize documents, see [Manage documents](/docs/eleven-agents/customization/knowledge-base/manage-documents).

## Overview

A well-curated knowledge base gives your agent the information that matters to your use case. Common examples include:

* **Product catalogs**: Specifications, pricing, and availability.
* **Policies**: HR, corporate, or support policies such as returns, benefits, or onboarding.
* **Technical documentation**: Guides and API references for developers.
* **Customer FAQs**: Consistent answers to common questions.

A single document can be attached to multiple agents, so you can maintain shared knowledge in one place.

The agent on this page is configured with full knowledge of ElevenLabs' documentation and sitemap.
Ask it anything about ElevenLabs.

## How your agent uses knowledge

Each document's **usage mode** controls how the agent draws on it, in one of two ways:

* **Full context**: The agent places the document's full text in its system prompt, keeping the whole document available on every turn. Because this consumes context, it works only for documents small enough to fit; larger documents must use RAG instead.
* **Retrieval-Augmented Generation (RAG)**: The document is indexed ahead of time, and at conversation time only the passages most relevant to each user query are retrieved for the agent to use. This lets the agent draw on knowledge bases far larger than the context window. See the [RAG guide](/docs/eleven-agents/customization/knowledge-base/rag) for configuration and limits.

Set each document's usage mode to choose which path the agent takes:

| Usage mode       | Behavior                                                                                               |
| :--------------- | :----------------------------------------------------------------------------------------------------- |
| `auto` (default) | The agent uses RAG when you enable RAG and the document is indexed; otherwise it uses full context.    |
| `prompt`         | The agent always places the document in the prompt, provided it is small enough to fit in the context. |

The agent always accesses folders through RAG and never places them in the prompt, so RAG must be enabled on the agent to use folders.

## Supported file formats

Documents can be created from files, URLs, or text. Uploaded **files** can be in the following formats, up to 20MB per file:

| Format   | Extension |
| :------- | :-------- |
| PDF      | `.pdf`    |
| Word     | `.docx`   |
| Text     | `.txt`    |
| Markdown | `.md`     |
| HTML     | `.html`   |
| EPUB     | `.epub`   |

## Size limits

A document can be used in full context only if its extracted text fits in the prompt, up to roughly 300,000 characters. Larger documents must be used through RAG instead. The total size of documents you can index for RAG depends on your subscription tier; see the [RAG usage limits](/docs/eleven-agents/customization/knowledge-base/rag#usage-limits).

You can check an agent's current knowledge base size from Claude or another MCP client through the [hosted MCP server](/docs/eleven-agents/operate/hosted-mcp).

## Best practices

<h4>
  Content quality
</h4>

Provide clear, well-structured information that is relevant to your agent's purpose.

<h4>
  Size management
</h4>

Break large documents into smaller, focused pieces for better retrieval and processing.

<h4>
  Regular updates
</h4>

Review and refresh your knowledge base so information stays current and accurate.

<h4>
  Identify knowledge gaps
</h4>

Review conversation transcripts to find topics where users struggle to get answers, then add the missing context to the knowledge base.
