---
title: "OpenCode"
source: https://langfuse.com/integrations/developer-tools/opencode-gateway.md
path: integrations/developer-tools/opencode-gateway
---

---
title: "OpenCode with the Langfuse AI Gateway"
sidebarTitle: OpenCode (gateway)
seoTitle: "Trace OpenCode with the Langfuse AI Gateway (beta)"
description: Route OpenCode's Anthropic and OpenAI providers through the Langfuse AI Gateway to trace every model call, tool call, token, and cost.
logo: /images/integrations/opencode_icon.svg
logoAppearance: multicolor
category: Integrations
---

# OpenCode with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

**Requires** OpenCode 2.0 or later and an `ANTHROPIC` and/or `OPENAI` provider connection. Verified with OpenCode 2.0.25.

  For tracing OpenCode without the gateway, see the [OpenCode integration](/integrations/developer-tools/opencode).

**Start with Langfuse** [Sign up](/cloud)

## Setup [#setup]

<Steps>

### Create a gateway API key [#create-a-key]

Create a gateway API key under **AI Gateway → Gateway keys**. See [API keys](/docs/gateway/features/api-keys#create-a-key).

Export it in the shell you start OpenCode from:

```sh
export LANGFUSE_GATEWAY_KEY="<your-gateway-key>"
```

To keep the setup across sessions, add the `export` lines to `~/.zshrc`.

### Configure the providers [#configure-the-providers]

Use `opencode.json` in the project root or `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/<model-id>",
  "small_model": "anthropic/<small-model-id>",
  "providers": {
    "anthropic": {
      "settings": {
        "baseURL": "https://gateway.cloud.langfuse.com/anthropic/v1",
        "apiKey": "{env:LANGFUSE_GATEWAY_KEY}"
      },
      "headers": {
        "langfuse-tags": "opencode,<team>",
        "langfuse-environment": "local",
        "langfuse-metadata": "repo:<repo>"
      }
    },
    "openai": {
      "settings": {
        "baseURL": "https://gateway.cloud.langfuse.com/openai/v1",
        "apiKey": "{env:LANGFUSE_GATEWAY_KEY}"
      },
      "headers": {
        "langfuse-tags": "opencode,<team>",
        "langfuse-environment": "local"
      }
    }
  }
}
```

- Replace `<model-id>` and `<small-model-id>` with model IDs from [`/models`](/docs/gateway/get-started/first-request#list-models). OpenCode uses `small_model` for titles, so a small, fast model works best.
- The Anthropic `baseURL` **includes `/v1`**, because OpenCode appends only `/messages`. Claude Code and Pi are the opposite.
- The built-in OpenAI provider uses the Responses API. OpenAI-compatible providers that use Chat Completions are supported by the gateway but have not been verified with OpenCode.
- To set a session per run, add `"langfuse-session-id": "{env:LF_SESSION}"`. An unset variable sends an empty value, which is ignored.
- Headers apply to every call from that provider, including title generation and subagents. See [request headers](/docs/gateway/features/tracing#request-headers).

  OpenCode continues to use stored account connections when you override the
  built-in `anthropic` or `openai` provider. Remove those connections before
  using this configuration, or configure the gateway under a separate provider
  ID as shown below.

#### Keep existing account connections [#keep-existing-account-connections]

To keep your existing OpenCode account connections, configure the gateway as a separate provider and declare each model manually. For example:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "langfuse/<model-id>",
  "providers": {
    "langfuse": {
      "package": "@opencode/ai/providers/openai-compatible/responses",
      "settings": {
        "baseURL": "https://gateway.cloud.langfuse.com/openai/v1",
        "apiKey": "{env:LANGFUSE_GATEWAY_KEY}"
      },
      "headers": {
        "langfuse-tags": "opencode,<team>",
        "langfuse-environment": "local"
      },
      "models": {
        "<model-id>": {}
      }
    }
  }
}
```

Add every model you want to use to `models`, then select it as `langfuse/<model-id>`.

### Verify [#verify]

Run a prompt:

```sh
opencode run "Reply with exactly: pong"
```

If OpenCode replies, it runs through the gateway.

</Steps>

## Turn grouping (experimental, optional) [#turn-grouping]

  Experimental. This plugin works with the current gateway but is not an
  official, published package yet.

With the stock `anthropic` and `openai` providers, every model call is its own trace. A small [plugin](https://opencode.ai/docs/plugins/) can send OpenCode's user message ID as the turn key, which the gateway already understands. Save it as `.opencode/plugin/langfuse-turn.ts` in your project or as `~/.config/opencode/plugin/langfuse-turn.ts`:

```ts
import type { Plugin } from "@opencode-ai/plugin";

export const LangfuseTurn: Plugin = async () => ({
  "chat.headers": async (input, output) => {
    output.headers["x-opencode-request"] = input.message.id;
  },
});
```

- All model calls of a prompt, including retries and parallel tool calls, land in one trace. The title call joins the first turn.
- Subagents (`task` tool) get their own trace, because they have their own session and user message.
- Auto-compaction and a message typed while the agent is busy start a new trace.

## Troubleshooting and FAQ [#troubleshooting-and-faq]

### How do I tell title calls apart from agent steps? [#title-calls]

Title calls have the same session, trace name, and generation name as agent steps. Tell them apart by the small model and zero tools. Some title calls are stored as `WARNING` "Client cancelled the response", because OpenCode aborts them.

### Why do subagents get their own session? [#subagent-sessions]

OpenCode starts a new session for subagents (`task` tool). The parent session ID is stored in `agent.parent_session_id`.

### OpenCode fails with UnknownError: Unexpected server error [#unknown-error]

The model is missing from OpenCode's catalog, so OpenCode fails locally and sends nothing. Declare the model under `providers.<id>.models`.

### OpenCode ignores the gateway provider [#stored-connections]

Stored OpenCode account connections take precedence when you override the built-in providers. Remove the existing `anthropic` and `openai` connections, or use a separate provider ID and declare its models explicitly.

### OpenCode still uses an old key [#service-restart]

OpenCode's background service keeps the environment variables from when it started. After exporting or changing `LANGFUSE_GATEWAY_KEY`, run `opencode service restart` before retrying.

### Why does a wrong model ID show six ERROR generations? [#six-errors]

OpenCode retries OpenAI `404` errors up to six times with backoff.

[Ask another question](/docs/ask-ai)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/developer-tools/opencode-gateway.md`.

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

