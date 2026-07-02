---
title: "Examples Overview"
source: https://docs.perplexity.ai/docs/cookbook/examples/README
path: docs/cookbook/examples/readme
---

Runnable projects covering the Agent API, Search API, and Embeddings API

# Examples Overview

Ready-to-run projects that demonstrate real-world use cases across every Perplexity API. Each example includes complete setup instructions and working code.

## Choosing the Right Example

| If you want to...                     | Use this example                                                                    | API                    | Language           |
| ------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------- | ------------------ |
| Conduct deep web research             | [Agent Research Assistant](/docs/cookbook/examples/agent-research-assistant/README) | Agent API              | Python, TypeScript |
| Compare models across providers       | [Model Comparison](/docs/cookbook/examples/model-comparison/README)                 | Agent API              | Python             |
| Monitor news topics in real time      | [Search News Monitor](/docs/cookbook/examples/search-news-monitor/README)           | Search API             | Python, TypeScript |
| Build a document Q\&A system          | [Document Q\&A](/docs/cookbook/examples/document-qa/README)                         | Embeddings + Agent API | Python             |
| Build a TypeScript CLI agent          | [TypeScript Agent CLI](/docs/cookbook/examples/typescript-agent-cli/README)         | Agent API              | TypeScript         |
| Analyze images with web context       | [Image Analysis](/docs/cookbook/examples/image-analysis/README)                     | Agent API              | Python, TypeScript |
| Ask questions about uploaded files    | [File Attachment Q\&A](/docs/cookbook/examples/file-attachment-qa/README)           | Agent API              | Python             |
| Search SEC filings for financial data | [SEC Filing Search](/docs/cookbook/examples/sec-filing-search/README)               | Agent API              | Python             |
| Run code and build a PDF in a sandbox | [Competitor Buzz Tracker](/docs/cookbook/examples/competitor-buzz-tracker/README)   | Agent API              | Python             |
| Source candidates for a hiring brief  | [Talent Sourcer](/docs/cookbook/examples/talent-sourcer/README)                     | Agent API              | Python             |

## By API

### Agent API

<CardGroup>
  <Card title="Agent Research Assistant" icon="magnifying-glass" href="/docs/cookbook/examples/agent-research-assistant/README">
    Deep web research using the `deep-research` preset with structured report output.
  </Card>

  <Card title="Model Comparison" icon="chart-bar" href="/docs/cookbook/examples/model-comparison/README">
    Compare responses from 5 providers side-by-side — quality, latency, and cost.
  </Card>

  <Card title="TypeScript Agent CLI" icon="terminal" href="/docs/cookbook/examples/typescript-agent-cli/README">
    Interactive TypeScript CLI with streaming, model selection, and web search.
  </Card>

  <Card title="Image Analysis" icon="image" href="/docs/cookbook/examples/image-analysis/README">
    Vision + web search for context-enriched image analysis.
  </Card>

  <Card title="File Attachment Q&A" icon="file-lines" href="/docs/cookbook/examples/file-attachment-qa/README">
    Upload documents and ask questions about them with optional web search enrichment.
  </Card>

  <Card title="Competitor Buzz Tracker" icon="chart-line" href="/docs/cookbook/examples/competitor-buzz-tracker/README">
    Two chained agent requests: the sandbox searches and counts each brand's share of voice, then renders a downloadable bar-chart PDF.
  </Card>

  <Card title="Talent Sourcer" icon="users" href="/docs/cookbook/examples/talent-sourcer/README">
    Wide search in a sandbox: source engineers by skill, location, and tenure, verify each, and rank them with their GitHub and profile links into an HTML shortlist.
  </Card>
</CardGroup>

### Search API

<CardGroup>
  <Card title="Search News Monitor" icon="newspaper" href="/docs/cookbook/examples/search-news-monitor/README">
    Multi-topic news monitoring with domain filtering and recency control.
  </Card>

  <Card title="SEC Filing Search" icon="file-invoice" href="/docs/cookbook/examples/sec-filing-search/README">
    Search SEC.gov and EDGAR for financial filings with structured data extraction.
  </Card>
</CardGroup>

### Embeddings API

<CardGroup>
  <Card title="Document Q&A" icon="file-lines" href="/docs/cookbook/examples/document-qa/README">
    Self-contained RAG system with contextualized embeddings and Agent API answer generation.
  </Card>
</CardGroup>

## API Key Setup

All examples require a Perplexity API key. Set it as an environment variable:

```bash theme={null}
export PERPLEXITY_API_KEY="your-api-key-here"
```

<Tip>
  Get your API key at [perplexity.ai/account/api](https://perplexity.ai/account/api).
</Tip>

## Common Requirements

* **Python 3.9+** or **Node.js 18+** (depending on the example)
* **Perplexity API Key**
* **Internet connection** for API calls

Additional requirements vary by example and are listed in each project's documentation.

## Contributing

Found a bug or want to add an example? See our [Contributing Guidelines](https://github.com/ppl-ai/api-cookbook/blob/main/CONTRIBUTING.md).
