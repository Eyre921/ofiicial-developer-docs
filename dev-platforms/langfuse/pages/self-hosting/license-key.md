---
title: "Enterprise license keys"
source: https://langfuse.com/self-hosting/license-key.md
path: self-hosting/license-key
---

---
title: License keys (self-hosted)
sidebarTitle: License Keys
description: Compare Enterprise and Government features and activate a license key for self-hosted Langfuse.
label: "Version: v4"
---

# License keys

All core Langfuse features and APIs are available in the open-source edition without a license key. Enterprise and Government keys unlock additional features for self-hosted deployments.

## Included features [#included-features]

Both Enterprise and Government include:

- [Project-level roles](/docs/administration/rbac) and [protected prompt labels](/docs/prompt-management/features/prompt-version-control#protected-prompt-labels).
- [Data retention policies](/docs/administration/data-retention) and [server-side data masking](/self-hosting/security/data-masking#server-side-ingestion-masking-ee).
- [Audit logs, including read-access logs](/docs/administration/audit-logs).
- [UI customization](/self-hosting/administration/ui-customization) and [organization creation restrictions](/self-hosting/administration/organization-creators).
- [Organization Management API and SCIM](/docs/administration/scim-and-org-api), plus the [Instance Management API](/self-hosting/administration/instance-management-api).
- [External media storage](/docs/observability/features/multi-modality#external-s3-media) and IAM role authentication for [S3](/docs/api-and-data-platform/features/export-to-blob-storage#iam-role-auth) and [Amazon Bedrock LLM connections](/docs/administration/llm-connection#bedrock-iam-role).

<span id="government" />

Government additionally supports [FIPS mode](/self-hosting/configuration/fips-mode) and sends no telemetry. Enterprise sends limited telemetry for license compliance. See [telemetry details](/self-hosting/security/telemetry).

Compare plans on the [self-hosted pricing page](/pricing-self-host).

## Activate your key [#activating-a-license-key]

Set this environment variable on **both the web and worker containers**, then redeploy:

```bash
LANGFUSE_EE_LICENSE_KEY=<your-license-key>
```

Use the same variable for either key type. Government keys start with `lf_gov_`.

To enable FIPS mode, also complete the [FIPS setup](/self-hosting/configuration/fips-mode#enable-fips-mode).

<span id="faq" />
<span id="how-to-remove-a-license-key" />

Removing a key? See [How do I remove my license key?](/faq/all/remove-license-key) in the [self-hosting FAQ](/self-hosting/troubleshooting-and-faq).

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
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx @langfuse/cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

