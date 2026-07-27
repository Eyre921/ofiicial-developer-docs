---
title: "Serverless Serving Paths"
source: https://docs.fireworks.ai/serverless/serving-paths
path: serverless/serving-paths
---

Standard, Priority, and Fast serving paths on Fireworks Serverless

Fireworks Serverless offers three serving paths:

* **Standard** is the default serving path. No `service_tier` parameter is needed.
* **Priority tier** is for workloads that require higher reliability during peak traffic.
* **Fast** is for workloads that require higher speeds.

## Priority tier

Priority tier is for workloads that require higher reliability during peak traffic periods, at a higher price point. Priority tier is prioritized above Standard traffic and is less likely to be load shed (503 server overloaded).

To use priority tier, set `service_tier` to `"priority"`. Supported on OpenAI-compatible chat completions and on the [Anthropic-compatible](/tools-sdks/anthropic-compatibility) `messages` API:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/glm-5p2",
    "service_tier": "priority",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Priority tier is available on select models. Models and pricing are listed on the [Serverless pricing](/serverless/pricing) page.

## Fast

Fast is a high-speed serving path, useful for interactive applications that require fast response speeds, at a higher price point. Fast variants aim for **100+ tokens per second** of generated throughput. It is not a different model and the quality of the model remains the same.

Fast is available for select models. To use Fast, change the `model` ID as listed below.

| Model          | `model` ID                                  |
| -------------- | ------------------------------------------- |
| Kimi K2.6 Fast | `accounts/fireworks/routers/kimi-k2p6-fast` |
| GLM 5.2 Fast   | `accounts/fireworks/routers/glm-5p2-fast`   |
| GLM 5.1 Fast   | `accounts/fireworks/routers/glm-5p1-fast`   |

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/routers/kimi-k2p7-code-fast",
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
