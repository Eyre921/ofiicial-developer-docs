---
title: "Overview"
source: https://langfuse.com/docs/gateway/overview.md
path: docs/gateway/overview
---

---
title: Overview
seoTitle: "Langfuse AI Gateway (beta)"
description: Send OpenAI and Anthropic API calls through Langfuse to trace every model call, keep provider keys in one place, and track cost, with no SDK or code changes.
---

# AI Gateway

  **Beta.** The **Langfuse AI Gateway** is in public beta and can still change.

Figure: AI Gateway overview.

1. A coding agent or AI application sends a request to the AI gateway, which runs in Langfuse.
2. The AI gateway authorizes the user with the gateway key and maps the model name and URL to a valid model provider request.
3. The AI gateway calls the external model provider (OpenAI, Anthropic) and returns the response to the client.
4. Langfuse tracing captures the request data, with different tracing options.

AI is being used in many different areas of a company, with engineers using coding agents, often dozens of AI apps running in production, internally or externally. Companies need to keep visibility and control over rising AI usage, answering questions like:

- Who in our organization uses which models?
- What do we use it for?
- What does it cost?
- Is it secure?
- How can we optimize it?

The **Langfuse AI Gateway** is a central entry point to govern all AI traffic, easy to host, adopt, and enforce. It can log all requests natively in Langfuse to analyze and make decisions based on AI usage.

If you have feedback, questions, or feature requests, please [share them on GitHub](https://github.com/orgs/langfuse/discussions/19686).

  ![Gateway analytics page showing total cost, requests, tokens, cost over time, and cost and requests per user](/images/docs/ai-gateway/analytics.png)

## What the Langfuse AI Gateway can do

Most gateways tell you what AI costs. Because every call through the **Langfuse AI Gateway** becomes a full Langfuse trace, it's more powerful than that.

- **See your spend.** Cost and usage for every call land in one [AI spend dashboard](/docs/gateway/features/analytics), by model and provider.
- **Know who spends it.** Every [key](/docs/gateway/features/api-keys) belongs to a person or service and can carry a team or cost center, so AI spend breaks down the way your company is organized.
- **Understand what it's spent on.** Each call can be logged as a [complete trace](/docs/gateway/features/tracing). You can see what an application or a team actually did with a model, and use the same search, evaluations, and annotation you already use in Langfuse. Or simply ask [Halo](/docs/api-and-data-platform/features/halo): "What does this team use Claude Code for?"
- **Control model usage.** [Approve models](/docs/gateway/features/models) centrally, so expensive or unvetted ones don't creep in unnoticed.
- **Incrementally adopt deeper tracing.** Enforce logging every model call by mandating the gateway, and allow teams to incrementally add more detail (for example, tool call executions of complex agents) to AI traces in Langfuse via [OpenTelemetry](/integrations/native/opentelemetry) or one of our 50+ [integrations](/integrations). OpenTelemetry distributed tracing merges these traces within Langfuse.
- **Use Langfuse as memory for agents.** All data in Langfuse is available via [MCP](/docs/api-and-data-platform/features/mcp-server) and the [CLI](/docs/api-and-data-platform/features/cli), so you can give agents access to search all AI requests they made in the past, which is the foundation for self-improvement loops.
- **Export metrics and raw logs to a [data lake](/docs/api-and-data-platform/features/export-to-blob-storage).** This enables any custom downstream process in finance and data teams.

## Roadmap [#roadmap]

This is only the beginning. We have a strong roadmap for the AI Gateway to help govern AI usage:

- **Cost:** hard spend caps
- **Reliability:** fallbacks between providers
- **Safety:** guardrails, PII redaction
- **Access:** user provisioning (SCIM)
- **More providers:** Vertex, Google AI Studio, and custom providers that support the gateway's API formats
- **Model routing:** automatically pick the best model for the task

If you are interested in being a design partner on one of these, [reach out to us](/talk-to-us).

## Getting Started [#getting-started]

Depending on your role, you're likely looking to:

- [set up the gateway for your organization](/docs/gateway/get-started/admin-setup) (admin)
- [start using your organization's gateway to send your LLM calls](/docs/gateway/get-started/first-request) (user)

For more information on how the gateway, keys, and model routing fit together, read [Core Concepts](/docs/gateway/concepts).

**Start with Langfuse** [Sign up](/cloud)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/gateway/overview.md`.

### Querying these docs

If the answer is not on this page, query the documentation instead of guessing:

- **Semantic search** across all Langfuse docs, returning an answer with the relevant pages and excerpts. Ask a specific, self-contained question:

  ```bash
  curl -sG "https://langfuse.com/api/search-docs" --data-urlencode "query=How do I trace a LangGraph agent?"
  ```

- **Index of every page**: <https://langfuse.com/llms.txt>, with per-section indexes [llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), and [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt).

### Before writing Langfuse code

- **Install the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill).** It encodes Langfuse's own best practices for instrumentation, prompt management, and evaluation, and materially improves results.
- **Read [What does a good trace look like?](https://langfuse.com/docs/observability/best-practices.md)** before instrumenting an application.
- **Verify endpoints, parameters, and response fields** against the [API reference](https://api.reference.langfuse.com) instead of inferring them from code examples.
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx @langfuse/cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

