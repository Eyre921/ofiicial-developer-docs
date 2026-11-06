---
title: "GitHub Copilot"
source: https://langfuse.com/integrations/developer-tools/github-copilot-gateway.md
path: integrations/developer-tools/github-copilot-gateway
---

---
title: "GitHub Copilot with the Langfuse AI Gateway"
sidebarTitle: GitHub Copilot (gateway)
seoTitle: "Trace GitHub Copilot CLI and the GitHub Copilot app with the Langfuse AI Gateway (beta)"
description: Route GitHub Copilot CLI and the GitHub Copilot app through the Langfuse AI Gateway to trace every model call, tool call, token, and cost.
logo: /images/integrations/github_copilot_icon.svg
logoAppearance: dark
category: Integrations
---

# GitHub Copilot with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

Both Copilot surfaces support bring-your-own-key (BYOK) model providers. Only those models go through the gateway. GitHub-hosted models in the same picker are not traced.

  For tracing GitHub Copilot without the gateway, see the [GitHub Copilot integration](/integrations/developer-tools/github-copilot).

- [Copilot CLI](#cli): `ANTHROPIC` or `OPENAI` provider credential.
- [GitHub Copilot app](#app): `OPENAI` provider credential. BYOK in the app is in public preview.

**Start with Langfuse** [Sign up](/cloud)

## Copilot CLI [#cli]

<Steps>

### Create a gateway API key [#cli-create-a-key]

Create a gateway API key under **Organization settings → AI Gateway → Gateway keys**. See [API keys](/docs/gateway/features/api-keys#create-a-key).

### Point Copilot CLI at the gateway [#cli-configure]

Copilot CLI reads its BYOK provider from environment variables. See GitHub's [BYOK guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models).

**Anthropic route**

```sh
export COPILOT_PROVIDER_BASE_URL="https://gateway.cloud.langfuse.com/anthropic"
export COPILOT_PROVIDER_TYPE="anthropic"
export COPILOT_PROVIDER_API_KEY="<your-gateway-key>"
export COPILOT_MODEL="<model-id>"   # an Anthropic model ID from /models
copilot
```

**OpenAI route**

```sh
export COPILOT_PROVIDER_BASE_URL="https://gateway.cloud.langfuse.com/openai/v1"
export COPILOT_PROVIDER_TYPE="openai"
export COPILOT_PROVIDER_WIRE_API="responses"
export COPILOT_PROVIDER_API_KEY="<your-gateway-key>"
export COPILOT_MODEL="<model-id>"   # an OpenAI model ID from /models
copilot
```

To keep the setup across sessions, add the `export` lines to `~/.zshrc`.

- The Anthropic base URL has **no** `/v1`. The OpenAI base URL **includes** `/v1`.
- Set `COPILOT_PROVIDER_WIRE_API="responses"` on the OpenAI route. Copilot defaults to `completions` ([Chat Completions](/docs/gateway/features/rest-api#routes)), which has not been verified with Copilot.
- If `~/.copilot/providers.json` (or the file in `COPILOT_PROVIDERS_CONFIG`) already lists providers or models, it takes precedence and these variables have no effect.
- Copilot CLI cannot send custom headers to a BYOK provider, so [request headers](/docs/gateway/features/tracing#request-headers) such as `langfuse-tags` cannot be set. Use [key metadata](/docs/gateway/features/api-keys#key-metadata) instead.

### Verify [#cli-verify]

Send a prompt in `copilot`. If Copilot replies, it runs through the gateway.

</Steps>

## GitHub Copilot app [#app]

<Steps>

### Create a gateway API key [#app-create-a-key]

Create a gateway API key under **Organization settings → AI Gateway → Gateway keys**. See [API keys](/docs/gateway/features/api-keys#create-a-key).

### Add the gateway as a model provider [#app-configure]

See GitHub's [guide to adding models to the Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/add-llm-models).

1. Open **Settings → Model providers**, select **Add provider**, then choose **Custom endpoint**.
2. Set **Display name** to `Langfuse`.
3. Set **Base URL** to `https://gateway.cloud.langfuse.com/openai/v1`.
4. Set **Wire API** to `responses`. With `completions`, requests to OpenAI's GPT-5 models fail.
5. Paste your gateway key as **API key**. The app stores it in your OS keychain.
6. Optional: add [request headers](/docs/gateway/features/tracing#request-headers) under **Custom headers**, for example:

   ```json
   {
     "langfuse-tags": "github-copilot,<team>"
   }
   ```

7. Select **Add provider**. The models of your `OPENAI` provider credential appear in the model picker alongside the GitHub-hosted models. Select one to start a session.

### Verify [#app-verify]

Select a gateway model and send a prompt. If Copilot replies, it runs through the gateway.

</Steps>

## Troubleshooting and FAQ [#troubleshooting-and-faq]

### Why does every call have its own trace without a session? [#no-session]

The gateway does not infer a session or turn from Copilot requests. In the app, set `langfuse-session-id` under **Custom headers** to group calls into one session.

### Can the Copilot app use the Anthropic route? [#anthropic-route]

No. The Anthropic route is CLI only. The app's custom endpoint speaks the OpenAI API only.

[Ask another question](/docs/ask-ai)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/developer-tools/github-copilot-gateway.md`.

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

