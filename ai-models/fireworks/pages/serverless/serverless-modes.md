---
title: "Serverless Modes"
source: https://docs.fireworks.ai/serverless/serverless-modes
path: serverless/serverless-modes
---

Compare Standard, Priority, and Fast serverless modes on Fireworks Serverless to choose the right tradeoff between cost, latency, and throughput.

Fireworks Serverless offers three modes:

* **Standard** is the default mode. No `service_tier` parameter is needed.
* **Priority tier** is for workloads that require higher reliability during peak traffic.
* **Fast** is for workloads that require higher speeds.
* **Ultrafast** (Private Preview) for workloads requiring extremely fast end-to-end generation speeds.

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

## Ultrafast (Private Preview)

Ultrafast is a high-speed mode, useful for extreme latency sensitive applications that require fast response speeds, at a higher price point. Ultrafast variants aim for **1500+ tokens per second** of generated throughput for agentic coding tasks. It is not a different model and the quality of the model remains the same.

Ultrafast is in Private Preview and is available for the models listed below. To get access to Ultrafast please reach out to the team [here](https://share-na2.hsforms.com/19_8Sm5zPQ7aUh1W2FuLDygqbom7). Once access is granted, change the `model` ID as listed below.

<table>
  <colgroup>
    <col />

    <col />
  </colgroup>

  <thead>
    <tr>
      <th>Model</th>
      <th>`model` ID</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Deepseek V4.1 Flash 1017</td>
      <td>`accounts/fireworks/models/deepseek-v4p1-flash-ultrafast`</td>
    </tr>
  </tbody>
</table>

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/routers/deepseek-v4p1-flash-ultrafast",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

## Related

* [Serverless overview](/serverless/overview)
* [US-only Serverless](/serverless/us-only-serverless)
* [Serverless quickstart](/getting-started/quickstart)
* [Text models](/guides/querying-text-models)
* [Anthropic compatibility](/tools-sdks/anthropic-compatibility) — `service_tier` is supported on both OpenAI-compatible chat completions and the Anthropic `messages` API.
