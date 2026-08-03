---
title: "Overview"
source: https://docs.fireworks.ai/ecosystem/firerouter/overview
path: ecosystem/firerouter/overview
---

Route LLM requests between closed-source and open models with FireRouter

FireRouter is a managed routing service for **any LLM workload**. Request the FireRouter model through the [Fireworks inference API](/tools-sdks/openai-compatibility), and FireRouter scores each turn to decide whether it can be served by a cheaper Fireworks open model or should pass through to a closed-source model.

The result is lower cost on simpler requests without giving up closed-source quality on harder ones.

<Note>
  FireRouter is in **research preview**. APIs, routing behavior, and the models in the routing pair may change. This documentation is updated to reflect the current configuration.
</Note>

## When to use FireRouter

Use FireRouter when you want **automatic cost optimization** without picking a different model per request:

* You want closed-source quality (for example Claude Opus) on hard prompts but do not need it on every call.
* Many of your requests are straightforward (summaries, formatting, simple Q\&A) and can be served by a Fireworks open model.
* You are fine sending both a Fireworks API key and a provider API key on each request.

## How it works

FireRouter scores each request independently and picks one of two paths:

| Path             | When                                      | What runs                                           | Billing                           |
| ---------------- | ----------------------------------------- | --------------------------------------------------- | --------------------------------- |
| **Redirect**     | Simple or low-complexity work             | A Fireworks open model (for example GLM 5.2)        | Your Fireworks API key            |
| **Pass-through** | Hard reasoning, judgment, or long context | A closed-source model (for example Claude Opus 4.8) | Your provider API key (Anthropic) |

FireRouter uses a bring-your-own-key (BYOK) model:

* Your **Fireworks API key** authenticates to FireRouter and pays for redirected calls.
* Your **provider API key** pays for pass-through calls to closed-source models.

FireRouter never stores your provider keys server-side. You send them on each request.

## FireConnect

The easiest way to use FireRouter in coding harnesses is [FireConnect](/ecosystem/fireconnect/overview). As of FireConnect **v0.9.0**, select FireRouter like any other model:

```bash theme={null}
fireconnect login
fireconnect claude on --model firerouter
```

See the [FireConnect overview: Harness support](/ecosystem/fireconnect/overview#harness-support) for which harnesses support FireRouter, and [FireConnect + FireRouter](/ecosystem/fireconnect/overview#firerouter) for quick enable steps. Per-harness guides (Claude Code slot flags, Codex Anthropic env, routing preference) live on each harness page.

Upgrade FireConnect before enabling FireRouter on an older install. See [Upgrade FireConnect](/ecosystem/fireconnect/overview#upgrade-fireconnect).

Pass `--anthropic-api-key sk-ant-...` on `on`, or store a key once with `fireconnect configure --anthropic-api-key sk-ant-...`. Without an Anthropic key, FireRouter still redirects to open models but cannot pass through to Claude Opus 4.8. See [Authentication](/ecosystem/firerouter/authentication).

Cursor does not support FireRouter through FireConnect.

## Endpoint

FireRouter is available through the Fireworks inference API:

```text theme={null}
https://api.fireworks.ai/inference/v1
```

Common API paths:

| Wire format        | Path                                                     |
| ------------------ | -------------------------------------------------------- |
| Chat Completions   | `https://api.fireworks.ai/inference/v1/chat/completions` |
| Anthropic Messages | `https://api.fireworks.ai/inference/v1/messages`         |

## Model ID

FireRouter is a first-party model on the Fireworks provider. Use `firerouter` in the `model` field:

```text theme={null}
firerouter
```

These longer forms are also accepted:

```text theme={null}
fireworks/firerouter
accounts/fireworks/routers/firerouter
```

For [LiteLLM](/ecosystem/firerouter/litellm), use the full router path in `litellm_params.model`.

FireRouter routes each request between a configured closed-source model and a Fireworks open model. You do not pick the target model per request; FireRouter decides based on request complexity.

### Current routing pair

The FireRouter model currently routes between:

| Role                         | Model                                   |
| ---------------------------- | --------------------------------------- |
| Pass-through (closed-source) | **Claude Opus 4.8** (`claude-opus-4-8`) |
| Redirect (open)              | **GLM 5.2** (`glm-5p2`)                 |

These models are subject to change as FireRouter is updated. This page reflects the current configuration.

Because the pass-through target is Claude Opus 4.8, you must supply an Anthropic API key. See [Authentication](/ecosystem/firerouter/authentication).

## Client integrations

| Integration                                                     | When to use                                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [FireConnect](/ecosystem/fireconnect/overview)                  | One-command setup for Claude Code, OpenCode, Codex, Pi, and VS Code (recommended) |
| [Quickstart](/ecosystem/firerouter/quickstart)                  | Direct HTTP calls (curl, OpenAI SDK, any OpenAI-compatible client)                |
| [Claude Code (manual setup)](/ecosystem/firerouter/claude-code) | Manual `settings.json` setup                                                      |
| [LiteLLM](/ecosystem/firerouter/litellm)                        | Add FireRouter to a LiteLLM Proxy deployment                                      |

## What FireRouter is not

* **Not a deployment router.** FireRouter is different from [deployment routers](/deployments/routers), which load-balance traffic across your own Fireworks deployments.
* **Not request-sticky.** Each request is scored independently.

## Next steps

<CardGroup>
  <Card title="FireConnect" icon="plug" href="/ecosystem/fireconnect/overview">
    Enable FireRouter with one command
  </Card>

  <Card title="Quickstart" icon="rocket" href="/ecosystem/firerouter/quickstart">
    Make your first API call
  </Card>

  <Card title="Claude Code (manual)" icon="terminal" href="/ecosystem/firerouter/claude-code">
    Edit settings.json for FireRouter in Claude Code
  </Card>

  <Card title="Authentication" icon="key" href="/ecosystem/firerouter/authentication">
    BYOK headers and API key requirements
  </Card>

  <Card title="Routing preferences" icon="sliders" href="/ecosystem/firerouter/routing-preferences">
    Tune the quality vs. savings dial
  </Card>

  <Card title="LiteLLM" icon="server" href="/ecosystem/firerouter/litellm">
    Add FireRouter to LiteLLM Proxy
  </Card>
</CardGroup>
