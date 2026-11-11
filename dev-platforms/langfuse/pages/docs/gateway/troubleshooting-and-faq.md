---
title: "Troubleshooting and FAQ"
source: https://langfuse.com/docs/gateway/troubleshooting-and-faq.md
path: docs/gateway/troubleshooting-and-faq
---

---
title: Troubleshooting and FAQ
seoTitle: "Langfuse AI Gateway troubleshooting (beta)"
description: Fix common Langfuse AI Gateway errors and review the known limitations of the beta.
---

# Troubleshooting and FAQ

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

This page addresses frequently asked questions and common troubleshooting topics for the Langfuse AI Gateway.

If you don't find a solution to your issue here, try using [Ask AI](/docs/ask-ai) for instant answers. For bug reports, please open a ticket on [GitHub Issues](/issues). For general questions or support, visit our [support page](/support).

## FAQ

- [Can I self-host the gateway?](/faq/all/ai-gateway-self-hosting)
- [Can I use the gateway in USAGE mode and still set users and tags?](/faq/all/ai-gateway-usage-mode-headers)
- [Can I use the gateway together with the Langfuse SDK?](/faq/all/ai-gateway-with-sdk)
- [Does the gateway change my requests?](/faq/all/ai-gateway-request-changes)
- [How do I report an AI Gateway issue?](/faq/all/ai-gateway-report-issue)
- [How do I troubleshoot AI Gateway errors?](/faq/all/ai-gateway-error-codes)
- [How is gateway usage billed?](/faq/all/ai-gateway-pricing)
- [What are the known limitations of the AI Gateway beta?](/faq/all/ai-gateway-known-limitations)
- [Which provider API keys are used?](/faq/all/ai-gateway-provider-credentials)
- [Why can't I open AI Gateway pages like Providers & Models or Gateway keys?](/faq/all/ai-gateway-pages-missing)

[Ask another question](/docs/ask-ai)

## GitHub Discussions

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/gateway/troubleshooting-and-faq.md`.

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

