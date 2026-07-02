---
title: "Perplexity with AnythingLLM"
source: https://docs.perplexity.ai/docs/getting-started/integrations/anythingllm
path: docs/getting-started/integrations/anythingllm
---

Use Perplexity as the LLM provider in AnythingLLM for grounded, citation-backed chat over your documents and workspaces.

## Overview

[AnythingLLM](https://anythingllm.com) is an all-in-one AI productivity app that turns any document, resource, or piece of content into context for LLM-powered chat. It supports both desktop and self-hosted deployments and works with dozens of LLM providers — including Perplexity as a first-class cloud provider, giving every workspace access to web-grounded answers with citations.

<Info>
  **AnythingLLM** is built and maintained by Mintplex Labs. It supports per-workspace LLM configuration, so you can use Perplexity in one workspace and a different provider in another. Learn more at [anythingllm.com](https://anythingllm.com).
</Info>

## Setup

<Steps>
  <Step title="Get your API key">
    Generate a Perplexity API key from the [API portal](https://www.perplexity.ai/account/api/keys).

    <Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
      Generate your Perplexity API key.
    </Card>
  </Step>

  <Step title="Open LLM settings">
    In AnythingLLM, go to **Settings → LLM Preference**.
  </Step>

  <Step title="Select Perplexity AI">
    Choose **Perplexity AI** from the provider list and paste your API key.
  </Step>

  <Step title="Choose a model">
    Once your key is entered, the **Chat Model Selection** dropdown automatically populates with available Perplexity models. Pick the model you want (e.g., `sonar-pro`) and save.
  </Step>
</Steps>

## System vs. Workspace Models

AnythingLLM lets you scope LLM choice at two levels:

* **System LLM** — The default provider used for every workspace and agent.
* **Workspace LLM** — Per-workspace override that takes precedence when chatting inside that workspace.

You can mix providers freely. For example, set Anthropic as your system default and use Perplexity in a specific workspace where you need real-time web grounding for research-heavy chats.

To override per workspace: open the workspace, go to **Workspace Settings → Chat Settings → Workspace LLM Provider**, and select **Perplexity AI** with the model you want.

## Available Models

All Perplexity models supported by the API are available to AnythingLLM users — the model dropdown populates dynamically once your API key is validated. Recommended models:

* `sonar` — fast, cost-effective web-grounded chat
* `sonar-pro` — advanced reasoning with broader citation depth
* `sonar-reasoning-pro` — multi-step reasoning with search

See the full list of [Perplexity models and capabilities](/docs/sonar/models).

## Use Cases

Pairing Perplexity with AnythingLLM gives you:

* **Live web answers inside document workflows** — your workspace can answer questions about uploaded PDFs and the open web in the same chat.
* **Citation-grounded retrieval** — Perplexity returns source URLs you can audit alongside your retrieval-augmented context.
* **No-RAG fallback for current events** — when documents don't contain the answer, the model can reach for live web context automatically.

## Agent Configuration

When using AnythingLLM's [AI agents](https://docs.anythingllm.com/agent/setup), you can configure Perplexity as the agent's LLM in the workspace's **Agent Configuration** menu. This is useful for agents that need to chain web research with skills like web browsing, document Q\&A, or external API calls.

## Links & Resources

<CardGroup>
  <Card title="AnythingLLM Perplexity Docs" icon="book" href="https://docs.anythingllm.com/setup/llm-configuration/cloud/perplexity-ai">
    Official AnythingLLM setup guide for Perplexity AI.
  </Card>

  <Card title="AnythingLLM Docs" icon="globe" href="https://docs.anythingllm.com">
    Full AnythingLLM documentation.
  </Card>

  <Card title="Perplexity API Reference" icon="code" href="/api-reference">
    Full Perplexity API reference.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Sonar models and capabilities.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [AnythingLLM documentation](https://docs.anythingllm.com)
* Review our [FAQ](/docs/resources/faq)
