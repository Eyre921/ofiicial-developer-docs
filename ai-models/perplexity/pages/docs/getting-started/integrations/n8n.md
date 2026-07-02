---
title: "Perplexity with n8n"
source: https://docs.perplexity.ai/docs/getting-started/integrations/n8n
path: docs/getting-started/integrations/n8n
---

Add real-time web search, AI agents, and embeddings to your n8n workflows using the native Perplexity node.

## Overview

n8n ships a native **Perplexity node** with full API coverage — Chat Completions, Agent, Search, and Embeddings — all configurable from the visual canvas. Models load dynamically from the API, so the dropdown always reflects the latest options.

<Info>
  **n8n** is a node-based workflow automation platform. It supports both self-hosted and cloud deployments — all examples below work in either. If you're self-hosting, make sure your instance can reach `api.perplexity.ai` outbound. Learn more at [n8n.io](https://n8n.io).
</Info>

The node supports four resources:

* **Chat Completion** — Sonar models with built-in web search, citations, and search controls
* **Agent** — Third-party models (OpenAI, Anthropic, Google, xAI) with tool-calling and structured output
* **Search** — Raw ranked web results for your own processing
* **Embeddings** — Vector generation for RAG and retrieval pipelines

## Prerequisites

* n8n 2.14.0+ (cloud at [app.n8n.cloud](https://app.n8n.cloud) or self-hosted)
* A Perplexity API key

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/settings/api">
  Generate your Perplexity API key from the console.
</Card>

## Credential Setup

<Steps>
  <Step title="Open Credentials">
    In n8n, go to **Settings → Credentials → Add credential**.
  </Step>

  <Step title="Select Perplexity">
    Search for **Perplexity API** and select it.
  </Step>

  <Step title="Add Your Key">
    Paste your API key and save. The node will reference this credential automatically.
  </Step>
</Steps>

<img alt="Perplexity credential setup" />

***

## Chat Completion

Use Sonar models with built-in web search. This is the most common starting point — send a question, get a grounded answer with citations.

Add a **Perplexity** node, set **Resource** to `Chat Completion`, and choose a model:

| Parameter        | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| **Model**        | `sonar`, `sonar-pro`, `sonar-reasoning-pro`, or `sonar-deep-research`          |
| **User Message** | The question or prompt — supports n8n expressions like `={{ $json.question }}` |

<img alt="Chat Completion node configuration" />

### Search Controls

The node exposes Perplexity's full search filtering in the **Options** section:

<img alt="Search controls and additional parameters" />

### Extracting Citations

The response includes a `citations` array of source URLs. Use a **Code** node after the Perplexity node to format them:

```javascript theme={null}
const response = $input.first().json;
const content = response.choices[0].message.content;
const citations = response.citations ?? [];

return [{
  answer: citations.length > 0
    ? `${content}\n\nSources:\n${citations.map((c, i) => `[${i + 1}] ${c}`).join('\n')}`
    : content,
  citations
}];
```

***

## Agent

Use the Agent resource to route through third-party models (OpenAI, Anthropic, Google, xAI) with Perplexity's `web_search` and `fetch_url` tools.

Set **Resource** to `Agent` and configure:

| Parameter               | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| **Model**               | Any model from the dynamic dropdown (e.g., `openai/gpt-5.5`, `anthropic/claude-sonnet-4-6`) |
| **Input**               | Your prompt — supports n8n expressions                                                      |
| **Tools**               | Select `web_search`, `fetch_url`, or both                                                   |
| **System Instructions** | Optional system prompt for the agent                                                        |
| **Response Format**     | Optional JSON schema for structured output                                                  |

<img alt="Agent resource configuration" />

***

## Search

Get raw ranked web results without LLM processing. Set **Resource** to `Search`:

| Parameter         | Description                                 |
| ----------------- | ------------------------------------------- |
| **Query**         | The search query — supports n8n expressions |
| **Recency**       | `day`, `week`, `month`, or `year`           |
| **Domain Filter** | Limit to specific domains                   |
| **Language**      | ISO 639-1 language code                     |
| **Country**       | Two-letter country code                     |

Each result includes `title`, `url`, `snippet`, and `date`.

<img alt="Search resource results" />

***

## Embeddings

Generate vectors for RAG and retrieval pipelines. Set **Resource** to `Embeddings`:

| Parameter | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| **Model** | `pplx-embed-v1-4b` (2560 dims) or `pplx-embed-v1-0.6b` (1024 dims) |
| **Input** | Text to embed — supports n8n expressions                           |

The node also supports contextual embeddings via `POST /v1/contextualizedembeddings` for document-chunk-aware vectors.

<img alt="Embeddings resource configuration" />

***

## Error Handling

Use n8n's **Error Trigger** workflow or the built-in **Retry on Fail** setting (node settings → Retry on Fail) to handle transient errors:

* **429 Too Many Requests** — add a **Wait** node with exponential backoff before retrying
* **401 Unauthorized** — verify your Perplexity API credential is saved correctly
* **500 errors** — enable Retry on Fail in the node settings

## Links & Resources

<CardGroup>
  <Card title="n8n Docs" icon="book" href="https://docs.n8n.io">
    Official n8n documentation
  </Card>

  <Card title="n8n Community" icon="users" href="https://community.n8n.io">
    Templates, workflows, and community support
  </Card>

  <Card title="Perplexity API Reference" icon="code" href="/api-reference">
    Full API reference
  </Card>

  <Card title="Sonar Models" icon="sparkles" href="/docs/sonar/models">
    Available models and capabilities
  </Card>
</CardGroup>
