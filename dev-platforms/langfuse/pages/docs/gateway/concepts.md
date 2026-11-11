---
title: "Concepts"
source: https://langfuse.com/docs/gateway/concepts.md
path: docs/gateway/concepts
---

---
title: Concepts
seoTitle: "How the Langfuse AI Gateway works (beta)"
description: How the Langfuse AI Gateway routes model calls, which keys and connections are involved, how a request reaches a model, and how each call becomes a Langfuse trace.
---

# Core concepts

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

This page explains how the gateway works: what happens to a request, which keys and settings are involved, and how a model call becomes a trace. To start using it, see [Set up the gateway](/docs/gateway/get-started/admin-setup) for admins or [Send your first request](/docs/gateway/get-started/first-request) for developers.

## Components, architecture and request flow [#architecture]

The gateway serves as a layer between the user's AI requests and the model providers. Users authenticate with the AI gateway and pass on request content. The AI gateway routes the request to the correct model provider, executes the API call, and returns the result back to the user.

Figure: AI Gateway architecture.

1. A coding agent or AI application authenticates with a gateway key and sends the model name and URL along with the request body to the AI gateway, which runs in Langfuse.
2. The AI gateway authorizes the user with the gateway key and maps the model name and URL to a valid model provider request.
3. The AI gateway sends the API request to the external model provider (OpenAI, Anthropic) and returns the response to the client.
4. Langfuse tracing captures the request data, with different tracing options.

On Langfuse Cloud, Langfuse runs the gateway in the EU, US, JP, and HIPAA regions, each with its own [gateway host](/docs/gateway/features/rest-api#gateway-hosts). Gateway traces are stored in your organization's Langfuse region. Requests are forwarded to your model providers and processed under your agreement with them.

On self-hosted Langfuse, the gateway is a separate service that you deploy next to your instance. See [Self-hosting the AI Gateway](/self-hosting/configuration/ai-gateway).

### Keys and connections [#credential-types]

The gateway uses three types of keys. Clients hold user keys or service account keys, and only the gateway holds the provider API keys:

| Key type                                                                           | Origin                                          | Scope                                                                    | Provided by |
| ---------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ | ----------- |
| [Provider API key](/docs/gateway/get-started/admin-setup#add-provider-connections) | Model provider, for example OpenAI or Anthropic | Held only by the gateway. Clients never see it.                          | Owner/admin |
| [User key](/docs/gateway/features/api-keys#key-types)                              | AI Gateway                                      | Scoped to one user. Stops working when the user leaves the organization. | User        |
| [Service account key](/docs/gateway/features/api-keys#key-types)                   | AI Gateway                                      | Scoped to a CI or shared service. Not linked to an individual user.      | Owner/admin |

Because clients only hold gateway keys, you can rotate a provider key without changing any client, and revoke one person's access without affecting anyone else.

The gateway calls the provider with your own provider API keys, so the provider bills model usage to your provider account. Langfuse counts each recorded generation as a [billable unit](/docs/administration/billable-units).

### Model and key routing [#routing]

An organization can add several provider connections, including more than one per provider.

**The URL path decides which API format the gateway expects.** Requests look exactly like requests to the provider. Only the base URL and the key change:

- `/openai/v1/responses` uses the OpenAI Responses API.
- `/openai/v1/chat/completions` uses the OpenAI Chat Completions API.
- `/anthropic/v1/messages` uses the Anthropic Messages API.

  The gateway doesn't convert one API format into the other, so a client that
  uses the OpenAI API can only call models from providers that support it, see
  [supported providers](/docs/gateway/features/models#supported-providers).

**The model ID decides the connection.** Each model ID starts with the name of a connection, in the form `<connection>:<model>`. For example, `openai-prod:<model>` calls `<model>` with the connection named `openai-prod`.

  Some coding agents send the provider's model names without a prefix, which
  also works for OpenAI and Anthropic models. See [model
  IDs](/docs/gateway/features/models#model-ids).

  By default, a connection allows every model the provider offers. Admins can
  turn models off per connection, see [Models and
  providers](/docs/gateway/features/models).

## Tracing [#tracing]

You can enable tracing of the LLM calls in a couple of different tiers (see [Tracing](/docs/gateway/features/tracing) for more details):

| Mode                      | Recorded                                                                                                                                                                                                        |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FULL`                    | Everything `USAGE` records, plus the full input (system prompt, tool definitions, messages, tool calls and results) and the streamed output (text, reasoning or thinking, and tool calls with parsed arguments) |
| `USAGE` (default)         | The model, token usage, cost, and latency, without input or output                                                                                                                                              |
| `NONE` (self-hosted only) | Nothing. The gateway only routes requests.                                                                                                                                                                      |

After the response, the gateway records the call as a generation in Langfuse asynchronously. See [how Langfuse captures data](/docs/observability/data-model#how-langfuse-captures-data) for more.

### Tracing context around the LLM call [#tracing-context]

The gateway only sees model calls. It doesn't see what your app does around them, for example retrieval or tool execution. To trace those steps, instrument your app with the [Langfuse SDK](/docs/observability/sdk/overview). To combine both, send the `traceparent` header of your current span with the request, and the gateway records its generation inside your trace. See [trace context and baggage](/docs/gateway/features/tracing#trace-context).

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/gateway/concepts.md`.

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

