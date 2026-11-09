---
title: "Set up the gateway as an admin"
source: https://langfuse.com/docs/gateway/get-started/admin-setup.md
path: docs/gateway/get-started/admin-setup
---

---
title: Set up Gateway as an admin
seoTitle: "Set up the Langfuse AI Gateway for your team (beta)"
description: Set up the Langfuse AI Gateway for an organization. Choose the ingestion project and ingestion mode, add provider credentials, choose models, give your team access, and issue gateway API keys.
---

# Set up Gateway as an admin

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

This page walks through how to set up the AI Gateway for your organization. Read [Core concepts](/docs/gateway/concepts) first to understand how the gateway works. If you want to use the gateway with your coding agent/AI app as a user, go to [Send your first request](/docs/gateway/get-started/first-request).

_**Self-hosting Langfuse?** The gateway is a separate service that runs next to Langfuse. See [Self-hosting the AI Gateway](/self-hosting/configuration/ai-gateway)._

## Setup steps [#setup-steps]

This guide helps you set up Langfuse Gateway as an admin.

<Steps>

### Configure the gateway [#configure-the-gateway]

Go to **AI Gateway → Overview** and choose:

- the **project**, where the gateway records generations
- the [ingestion mode](/docs/gateway/features/tracing#ingestion-modes): `FULL` (input and output) or `USAGE` (usage and cost only, the default). Self-hosted deployments also offer `NONE` (route without recording).

  ![Gateway setup page with the first step, choosing between the Full and Usage ingestion modes and the project to record in](/images/docs/ai-gateway/setup-ingestion-mode.png)

### Add provider credentials [#add-provider-connections]

On the same page, select **Add credential** and add [API keys](/docs/gateway/concepts#credential-types) for model providers you’d like to use. The credential's **name** becomes the prefix of its [model IDs](/docs/gateway/features/models#model-ids).

  ![Add provider credential dialog with the provider, name, and secret key fields](/images/docs/ai-gateway/setup-add-provider-credential.png)

  Provider credentials are separate from project [LLM
  connections](/docs/administration/llm-connection), which power the Playground
  and LLM-as-a-Judge.

### Configure allowed models (optional) [#choose-models]

By default, a credential allows every model the provider offers, including models the provider publishes later. To restrict a credential to selected models, turn models off on its models page. See [Model management](/docs/gateway/features/models#manage-models).

### Give your team access [#give-your-team-access]

Use **Notify your team** to email teammates. People who are not in the organization yet are invited with the AI Gateway role: they can call the gateway, manage their own keys, and see [analytics](/docs/gateway/features/analytics) of their own usage, but can't see any projects. This role suits people who only need to call models, for example developers who use the gateway for their coding agent.

  You can change anyone's role later in the organization's members settings,
  for example to let them see their traces in the ingestion project. See [roles
  and permissions](/docs/administration/rbac) for what each role can do.

</Steps>

## Not seeing what you expected? [#not-seeing-what-you-expected]

- [Why can't I open AI Gateway pages like Providers & Models or Gateway keys?](/faq/all/ai-gateway-pages-missing)

[Ask another question](/docs/ask-ai)

## Next steps [#next-steps]

- [Enable users to start using Gateway](/docs/gateway/get-started/first-request)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/gateway/get-started/admin-setup.md`.

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

