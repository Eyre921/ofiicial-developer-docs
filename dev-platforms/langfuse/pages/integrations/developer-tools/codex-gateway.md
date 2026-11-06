---
title: "Codex"
source: https://langfuse.com/integrations/developer-tools/codex-gateway.md
path: integrations/developer-tools/codex-gateway
---

---
title: "Codex with the Langfuse AI Gateway"
sidebarTitle: Codex (gateway)
seoTitle: "Trace OpenAI Codex with the Langfuse AI Gateway (beta)"
description: Route the OpenAI Codex CLI through the Langfuse AI Gateway to trace every turn, model round, tool call, token, and cost.
logo: /images/integrations/openai_icon.svg
logoAppearance: dark
category: Integrations
---

# Codex with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

**Requires** Codex CLI 0.157 or later and an `OPENAI` provider credential. Verified with Codex 0.157.0.

  For tracing Codex without the gateway, see the [Codex integration](/integrations/developer-tools/codex).

**Start with Langfuse** [Sign up](/cloud)

## Setup [#setup]

<Steps>

### Create a gateway API key [#create-a-key]

Create a gateway API key under **Organization settings → AI Gateway → Gateway keys**. See [API keys](/docs/gateway/features/api-keys#create-a-key).

### Export the gateway key [#export-the-key]

Codex reads the key from this variable when it starts:

```sh
 export LANGFUSE_GATEWAY_KEY="<your-gateway-key>"
```

The leading space keeps the key out of shell history if your shell ignores commands that start with a space. To keep the setup across sessions, add the `export` lines to `~/.zshrc`.

### Add the gateway provider [#add-the-provider]

Add this to `~/.codex/config.toml` (`$CODEX_HOME/config.toml` if you set `CODEX_HOME`). Put `model_provider` next to your other top-level keys, before any `[table]` section, and the `[model_providers.langfuse]` table after them:

```toml filename="~/.codex/config.toml"
model_provider = "langfuse"

[model_providers.langfuse]
name = "Langfuse AI Gateway"
base_url = "https://gateway.cloud.langfuse.com/openai/v1"
env_key = "LANGFUSE_GATEWAY_KEY"   # sent as Authorization: Bearer
wire_api = "responses"
```

To pick a model, add `model = "<model-id>"` next to `model_provider`, using an ID from [`/models`](/docs/gateway/get-started/first-request#list-models). To add tags or other headers, use `http_headers`. See [request headers](/docs/gateway/features/tracing#request-headers).

### Start Codex [#start-codex]

```sh
codex
```

Each turn appears in Langfuse as one trace.

</Steps>

## Turn grouping [#turn-grouping]

Codex sends its own turn ID, so the gateway groups all model rounds of a turn into one trace named `codex`, with no extra setup. Each model round is an `openai.responses` generation, and the session is `codex:<thread id>`.

- The trace's input and output are copied from the turn's **last** round.
- Compaction calls appear in the same trace with `agent.request_kind=compaction`.

## Troubleshooting and FAQ [#troubleshooting-and-faq]

### Codex still uses old credentials after a change [#old-credentials]

Restart the Codex app-server daemon with `codex app-server daemon restart`. The daemon can keep using credentials loaded before the change until it restarts.

### Why is the input missing on long sessions? [#missing-input]

Codex sends `store: false` and replays the **whole conversation** on every round. Each generation's input is the full history, so long sessions can exceed the 5 MiB input capture limit, and the input is then dropped. See [known limitations](/faq/all/ai-gateway-known-limitations).

### A model fails with a 400 error [#model-400]

A global `model_reasoning_effort` makes non-reasoning models fail with a `400`. Some small models reject Codex's `tool_search` tool.

### Why does a trace contain several generations for one call? [#retries]

Codex retries failed requests (`request_max_retries`, `stream_max_retries`). Each retry is its own generation in the same trace.

### Why do cancelled or failed calls show high cost? [#inflated-cost]

As of November 6, 2026, Langfuse no longer tokenizes request or response text to fill missing usage. Older generations may still show inflated costs estimated from that text. For new writes, calls without provider usage or submitted cost have empty usage and cost breakdowns; historical estimates are not bulk-rewritten. See [token and cost tracking](/docs/observability/features/token-and-cost-tracking#troubleshooting).

### Can I use websocket features? [#websockets]

No. Keep websocket features off for this provider. The gateway serves HTTP server-sent events only.

### Why can't Codex generate images through the gateway? [#image-generation]

Codex offers its built-in `image_gen` tool only when the model provider is OpenAI itself, so it hides the tool for the gateway provider. Codex may then suggest the `imagegen` skill's CLI fallback instead. Support for custom providers in Codex is tracked in [openai/codex#24465](https://github.com/openai/codex/issues/24465).

  The `imagegen` CLI fallback calls OpenAI directly with `OPENAI_API_KEY`, so
  those calls bypass the gateway and are not traced in Langfuse. The gateway
  does not serve the OpenAI Images API (`/images/generations`, `/images/edits`)
  yet either; see [supported endpoints](/docs/gateway/features/rest-api#routes).

[Ask another question](/docs/ask-ai)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/developer-tools/codex-gateway.md`.

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

