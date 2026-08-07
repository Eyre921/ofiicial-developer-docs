---
title: "LiteLLM"
source: https://docs.fireworks.ai/ecosystem/integrations/litellm
path: ecosystem/integrations/litellm
---

Configure Fireworks models in LiteLLM Proxy

Use [LiteLLM Proxy](https://docs.litellm.ai/docs/proxy/quick_start) as a shared gateway for Fireworks serverless models, router endpoints, and deployments. LiteLLM exposes a single OpenAI-compatible API to your developers while you manage provider credentials and access control on the server.

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* LiteLLM v1.95.0 installed (`pip install "litellm[proxy]==1.95.0"`)

## Configure Fireworks models

Create a `config.yaml` with one entry per model you want to expose. Use the `fireworks_ai/` provider prefix and the **full** Fireworks model or router ID:

<Note>
  Always use full resource paths (for example `accounts/fireworks/models/glm-5p2` or `accounts/fireworks/routers/firerouter`). LiteLLM rewrites short names to `accounts/fireworks/models/...`, which breaks router endpoints like FireRouter.
</Note>

```yaml theme={null}
model_list:
  - model_name: accounts/fireworks/models/glm-5p2
    litellm_params:
      model: fireworks_ai/accounts/fireworks/models/glm-5p2
      api_key: os.environ/FIREWORKS_AI_API_KEY

  - model_name: accounts/fireworks/routers/kimi-k2p6-turbo
    litellm_params:
      model: fireworks_ai/accounts/fireworks/routers/kimi-k2p6-turbo
      api_key: os.environ/FIREWORKS_AI_API_KEY
```

LiteLLM sends requests to `https://api.fireworks.ai/inference/v1` by default. See the [LiteLLM Fireworks AI provider docs](https://docs.litellm.ai/docs/providers/fireworks_ai) for direct-route deployments and other options.

## Start the proxy

```bash theme={null}
export FIREWORKS_AI_API_KEY="fw_..."
litellm --config config.yaml
```

## Call a model

Clients authenticate to LiteLLM with a [virtual key](https://docs.litellm.ai/docs/proxy/virtual_keys):

```bash theme={null}
curl http://localhost:4000/chat/completions \
  -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/fireworks/models/glm-5p2",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

## API key layout

| Key                          | Who holds it                         | Used for                                |
| ---------------------------- | ------------------------------------ | --------------------------------------- |
| Fireworks API key (`fw_...`) | LiteLLM server (env or secret store) | Upstream Fireworks inference            |
| LiteLLM virtual key          | Each developer or service            | Proxy authentication and spend tracking |

A common pattern is one Fireworks service-account API key on the LiteLLM server, with per-developer virtual keys for access control and attribution.

## FireRouter

To add automatic routing between closed-source and open models, register [FireRouter](/ecosystem/firerouter/overview) in the same `model_list`. FireRouter requires an Anthropic API key for pass-through. See [FireRouter with LiteLLM](/ecosystem/firerouter/litellm).

## Related

* [LiteLLM Proxy quick start](https://docs.litellm.ai/docs/proxy/quick_start)
* [LiteLLM Fireworks AI provider](https://docs.litellm.ai/docs/providers/fireworks_ai)
* [FireRouter](/ecosystem/firerouter/overview): managed routing between open and closed-source models
* [OpenAI compatibility](/tools-sdks/openai-compatibility): Fireworks inference API reference
