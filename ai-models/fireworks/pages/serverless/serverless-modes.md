---
title: "Serverless modes"
source: https://docs.fireworks.ai/serverless/serverless-modes
path: serverless/serverless-modes
---

Compare Standard, Priority, Fast, and Ultra-fast (Preview) serverless modes on Fireworks Serverless to choose the right tradeoff between cost, latency, and throughput.

Fireworks Serverless offers four modes:

* **Standard** is the default mode. No `service_tier` parameter is needed.
* **Priority tier** is for workloads that require higher reliability during peak traffic.
* **Fast** is for workloads that require higher speeds.
* **Ultra-fast** (Preview) for workloads requiring extremely fast end-to-end generation speeds.

## Priority tier

Priority tier is for workloads that require higher reliability during peak traffic periods, at a higher price point. Priority tier is prioritized above Standard traffic and is less likely to be load shed (503 server overloaded).

To use priority tier, set `service_tier` to `"priority"`. Supported on OpenAI-compatible chat completions and on the [Anthropic-compatible](/tools-sdks/anthropic-compatibility) `messages` API:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/glm-5p3",
    "service_tier": "priority",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Priority tier is available on select models. Models and pricing are listed on the [Serverless pricing](/serverless/pricing) page.

## Fast

Fast is a high-speed mode, useful for interactive applications that require fast response speeds, at a higher price point. Fast variants aim for **100+ tokens per second** of generated throughput. It is not a different model and the quality of the model remains the same.

Fast is available for select models. To use Fast, change the `model` ID as listed below.

| Model | `model` ID |
| - | - |
| Kimi K3 Fast | `accounts/fireworks/routers/kimi-k3-fast` |
| GLM 5.3 Fast | `accounts/fireworks/routers/glm-5p3-fast` |

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/routers/kimi-k3-fast",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Pricing is listed on the [Serverless pricing](/serverless/pricing) page.

## Ultra-fast (preview)

Ultra-fast is a high-speed mode, useful for extreme latency sensitive applications that require fast response speeds, at a higher price point. Ultra-fast variants aim for **6-8x generation speed (up to 10x for agentic coding tasks)**. Like fast, it is not a different model and the quality of the model remains the same.

Ultra-fast is in Preview and is available for the models listed below. Our preview modes are under active development and are subject to change quickly. To use Ultra-fast, change the `model` ID as listed below.

| Model | `model` ID |
| - | - |
| Deepseek V4.1 Flash 1017 | `accounts/fireworks/routers/deepseek-v4p1-flash-1017-ultrafast` |

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/routers/deepseek-v4p1-flash-1017-ultrafast",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Pricing is listed on the [Serverless pricing](/serverless/pricing) page.

## Related

* [Serverless overview](/serverless/overview)
* [US-only Serverless](/serverless/us-only-serverless)
* [Serverless quickstart](/getting-started/quickstart)
* [Text models](/guides/querying-text-models)
* [Anthropic compatibility](/tools-sdks/anthropic-compatibility) — `service_tier` is supported on both OpenAI-compatible chat completions and the Anthropic `messages` API.
