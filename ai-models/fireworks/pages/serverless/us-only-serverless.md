---
title: "US-only Serverless"
source: https://docs.fireworks.ai/serverless/us-only-serverless
path: serverless/us-only-serverless
---

Run Serverless inference exclusively in the US

US-only Serverless serves inference exclusively from the US, making it a good fit for compliance needs.

## Available models

| Model   | `model` ID                              |
| ------- | --------------------------------------- |
| Kimi K3 | `accounts/fireworks/routers/kimi-k3-us` |

## How to use it

Use a US router from the table above as the `model` ID.

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/routers/kimi-k3-us",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

```python theme={null}
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/routers/kimi-k3-us",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)
```

## Pricing

US-only endpoints are priced at a 10% premium to the base model serverless prices. See [Serverless pricing](/serverless/pricing).

## Other regions

For EU-only Serverless, contact [sales](https://fireworks.ai/company/contact-us).

## Related

* [Serverless Serving Paths](/serverless/serving-paths)
* [Serverless pricing](/serverless/pricing)
* [Serverless overview](/serverless/overview)
* [Data Security](/guides/security_compliance/data_security)
