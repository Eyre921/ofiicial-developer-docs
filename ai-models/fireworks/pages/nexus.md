---
title: "Overview"
source: https://docs.fireworks.ai/nexus
path: nexus
---

Fireworks Nexus connects coding harnesses, apps, and LLM gateways to open models and FireRouter, with usage visibility and per-user spend caps.

Coding agents start at [Nexus](/nexus). Use the [Quickstart](/nexus/quickstart) for harnesses, custom agents, APIs, SDKs, and LLM gateways. Use [FireRouter](/nexus/firerouter) for model routers, the supported model list, composition, closed-model credentials, and pricing. Prefer short model IDs such as `firerouter/opus`. In LiteLLM `litellm_params.model`, use `fireworks_ai/accounts/fireworks/routers/firerouter/opus`. Family names such as `opus` track the latest evaluated family version.

New to Nexus? Start with the [Quickstart](/nexus/quickstart). For the product overview, see the [Nexus product page](https://fireworks.ai/nexus).

> **[Quickstart](/nexus/quickstart)**
>
> Connect your first harness, app, or gateway.

> **[FireConnect](/nexus/fireconnect)**
>
> One command to route a coding harness through Fireworks.

> **[FireRouter](/nexus/firerouter)**
>
> One model ID that picks a model for each turn.

## How Nexus fits together

Connection and model choice are independent. Bring a coding tool, application, or LLM gateway. Then call a Fireworks model directly, or let FireRouter choose one for each new user turn.

```mermaid theme={null}
flowchart LR
  H[Coding harnesses] --> FC[FireConnect]
  A[Apps and agents] --> API[Fireworks API]
  G[LLM gateways] --> API
  FC --> API
  API --> OM[Open models]
  API --> FR[FireRouter]
  FR --> OM
  FR --> CM[Claude and GPT models<br/>on your provider account]
```

**1. Connect**

[FireConnect](/nexus/fireconnect) for coding harnesses, [APIs and SDKs](/nexus/apis-and-sdks) for your own code, or [LLM Gateways](/nexus/llm-gateways) for LiteLLM, Portkey, and others. Prefer not to install FireConnect? Every harness has [manual setup](/nexus/harnesses).

**2. Choose models**

Select [Open Models](/nexus/open-models) directly, or let [FireRouter](/nexus/firerouter) pick one for each user turn.

**3. Add closed models**

FireRouter calls Claude and GPT models on your own Anthropic, OpenAI, or Amazon Bedrock account. Connect [Provider Keys](/nexus/provider-keys) once where available, or send the key with each request.

**4. Operate**

[Usage and Cost](/nexus/metrics) shows Claude Code session estimates and dashboard usage for Fireworks models. [Spend Limits](/nexus/usage-limits) caps supported Fireworks serverless usage.
