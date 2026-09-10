---
title: "Enterprise license keys"
source: https://langfuse.com/self-hosting/license-key.md
path: self-hosting/license-key
---

---
title: Enterprise License Key (self-hosted)
sidebarTitle: License Key (EE)
description: Learn how to activate a license key for your self-hosted Langfuse deployment.
label: "Version: v4"
---

# Enterprise License Key

All core Langfuse features and APIs are available in Langfuse OSS (MIT licensed) without any limits.

When running Langfuse self-hosted, you use the same deployment infrastructure as Langfuse Cloud. There are no scalability limitations between the different versions.

Some additional Enterprise features require a license key:

- [Project-level RBAC Roles](/docs/rbac)
- [Protected Prompt Labels](/docs/prompt-management/features/prompt-version-control#protected-prompt-labels)
- [Data Retention Policies](/docs/data-retention)
- [Audit Logs](/changelog/2025-01-21-audit-logs)
- [Server-Side Data Masking](/self-hosting/security/data-masking#server-side-ingestion-masking-ee)
- [UI Customization](/self-hosting/administration/ui-customization)
- [Organization Creators](/self-hosting/administration/organization-creators)
- [Org Management API and SCIM](/docs/administration/scim-and-org-api)
- [Instance Management API](/self-hosting/administration/instance-management-api)

See [pricing page](/pricing-self-host) for more details on Langfuse Enterprise.

## Activating a License Key

After purchasing a license key, you can activate it by adding the following environment variable to your Langfuse deployment (both langfuse containers):

```bash
LANGFUSE_EE_LICENSE_KEY=<your-license-key>
```

Enterprise self-hosted deployments use limited telemetry for license compliance.
See the [telemetry documentation](/self-hosting/security/telemetry) for the exact fields that are collected.

## Questions?

If you have any questions about licensing, please [contact us](/support).

---

If you experience any issues when self-hosting Langfuse, please:

1. Check out [Troubleshooting & FAQ](/self-hosting/troubleshooting-and-faq) page.
2. Use [Ask AI](/docs/ask-ai) to get instant answers to your questions.
3. Ask the maintainers on [GitHub Discussions](/gh-support).
4. Create a bug report or feature request on [GitHub](/issues).

  Enterprise-grade support is available when self-hosting Langfuse. Learn more on
  our [pricing page](/pricing-self-host).

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/self-hosting/license-key.md`.

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
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx langfuse-cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

