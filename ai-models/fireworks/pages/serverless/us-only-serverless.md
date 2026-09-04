---
title: "US-only Serverless"
source: https://docs.fireworks.ai/serverless/us-only-serverless
path: serverless/us-only-serverless
---

Run Serverless inference exclusively in the US

US-only Serverless serves inference exclusively from the US, making it a good fit for compliance needs.

## Available models

| Model                    | `model` ID                                             |
| ------------------------ | ------------------------------------------------------ |
| Kimi K3                  | `accounts/fireworks/routers/kimi-k3-us`                |
| DeepSeek V4 Flash (0731) | `accounts/fireworks/routers/deepseek-v4-flash-0731-us` |
| GLM 5.2                  | `accounts/fireworks/routers/glm-5p2-us`                |
| GLM 5.2 Fast             | `accounts/fireworks/routers/glm-5p2-fast-us`           |
| GLM 5.3                  | `accounts/fireworks/routers/glm-5p3-us`                |
| GLM 5.3 Flash            | `accounts/fireworks/routers/glm-5p3-flash-us`          |

## How to use it

Call `https://us.api.fireworks.ai` and pass one of the US model IDs from the table above as `model`.

```bash theme={null}
curl https://us.api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/routers/kimi-k3-us",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

```python theme={null}
from fireworks import Fireworks

client = Fireworks(base_url="https://us.api.fireworks.ai/inference")

response = client.chat.completions.create(
    model="accounts/fireworks/routers/kimi-k3-us",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)
```

To require this for every request on your account, see [Data residency](/accounts/data-residency).

## Pricing

Beginning September 1, 2026, launched US-only models are priced at a 50% premium to the base model serverless prices. Kimi K3 US already includes this premium, while GLM 5.2 Fast US is an exception and matches global GLM 5.2 Fast pricing. See [Serverless pricing](/serverless/pricing).

## Other regions

For EU-only Serverless, contact [sales](https://fireworks.ai/company/contact-us).

## Related

* [Serverless Serving Paths](/serverless/serving-paths)
* [Serverless pricing](/serverless/pricing)
* [Serverless overview](/serverless/overview)
* [Data Security](/guides/security_compliance/data_security)
