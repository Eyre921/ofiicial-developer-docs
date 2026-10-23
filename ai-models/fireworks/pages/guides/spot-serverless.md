---
title: "Spot Serverless"
source: https://docs.fireworks.ai/guides/spot-serverless
path: guides/spot-serverless
---

Use lower-cost, best-effort serverless inference and fall back to Standard

Spot is a separate serverless offering for workloads that can tolerate temporary capacity limits. It uses the same OpenAI-compatible API as Standard and costs 30% less.

Use Spot for background, batch, and other cost-sensitive traffic that can wait through a retry or move to Standard.

> [!WARNING]
>
> Spot is best-effort. It has no availability or throughput guarantee, and available throughput can fall to zero.

Select Spot with its model identifier. `service_tier` does not select Spot.

## Models

| Model | Spot model identifier | Standard model identifier |
| - | - | - |
| GLM-5.3 | `accounts/fireworks/models/glm-5p3-spot` | `accounts/fireworks/models/glm-5p3` |
| Kimi K3 | `accounts/fireworks/models/kimi-k3-spot` | `accounts/fireworks/models/kimi-k3` |
| DeepSeek V4.1 Flash | `accounts/fireworks/models/deepseek-v4p1-flash-spot` | `accounts/fireworks/models/deepseek-v4p1-flash` |
| DeepSeek V4.1 Flash 1017 | `accounts/fireworks/models/deepseek-v4p1-flash-1017-spot` | `accounts/fireworks/models/deepseek-v4p1-flash-1017` |

## Make a request

**Python (Fireworks SDK)**

```python theme={null}
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/kimi-k3-spot",
  messages=[{"role": "user", "content": "Explain mixture-of-experts models."}]
)

print(response.choices[0].message.content)
```

**Python (OpenAI SDK)**

```python theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k3-spot",
    messages=[{
        "role": "user",
        "content": "Explain mixture-of-experts models."
    }]
)

print(response.choices[0].message.content)
```

**JavaScript**

```javascript theme={null}
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k3-spot",
  messages: [
    {
      role: "user",
      content: "Explain mixture-of-experts models.",
    },
  ],
});

console.log(response.choices[0].message.content);
```

**curl**

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k3-spot",
    "messages": [
      {
        "role": "user",
        "content": "Explain mixture-of-experts models."
      }
    ]
  }'
```

## Pricing

Prices are USD per 1 million tokens. Each Spot rate is 30% below the Standard rate for the same model. A request that falls back to Standard is billed at the Standard rate.

| Model | Tier | Cached input | Uncached input | Output |
| - | - | - | - | - |
| GLM-5.3 | Standard | \$0.26 | \$1.40 | \$4.40 |
| GLM-5.3 | Spot | \$0.182 | \$0.98 | \$3.08 |
| Kimi K3 | Standard | \$0.30 | \$3.00 | \$15.00 |
| Kimi K3 | Spot | \$0.21 | \$2.10 | \$10.50 |
| DeepSeek V4.1 Flash | Standard | \$0.006 | \$0.30 | \$1.20 |
| DeepSeek V4.1 Flash | Spot | \$0.0042 | \$0.21 | \$0.84 |
| DeepSeek V4.1 Flash 1017 | Standard | \$0.006 | \$0.30 | \$1.20 |
| DeepSeek V4.1 Flash 1017 | Spot | \$0.0042 | \$0.21 | \$0.84 |

## Availability, retries, and fallback

When no serving capacity is available, the API returns `503`. A rate limit returns `429`. Honor the `Retry-After` header when the response includes one. The Fireworks Python SDK retries these errors automatically, up to 2 times by default. Fireworks does not fall back to Standard. See [Reliability and Error Handling](/guides/reliability) for timeouts and backoff patterns.

If Spot is still unavailable after those retries, send the same request to the Standard model identifier:

```python theme={null}
from fireworks import Fireworks, InternalServerError, RateLimitError

client = Fireworks()
messages = [{"role": "user", "content": "Explain mixture-of-experts models."}]

try:
    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k3-spot",
        messages=messages,
    )
except (RateLimitError, InternalServerError):
    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k3",
        messages=messages,
    )

print(response.choices[0].message.content)
```

For a streaming request, fall back only if it fails before the stream starts. Replaying a stream that has already produced output can duplicate that output.
