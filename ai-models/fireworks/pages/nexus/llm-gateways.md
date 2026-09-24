---
title: "LLM Gateways"
source: https://docs.fireworks.ai/nexus/llm-gateways
path: nexus/llm-gateways
---

Connect Fireworks to LiteLLM, Portkey, Vercel AI Gateway, Helicone, Keywords AI, AISIX, Requesty, OpenRouter, or Cloudflare AI Gateway

Gateways integrate with Fireworks in two ways. Some connect to your Fireworks account and preserve Fireworks model IDs. Others expose selected Fireworks models through a gateway-managed catalog.

## Connect your Fireworks account

| Gateway                                                                                               | Fireworks integration                              | Model naming                                                             |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------ |
| [LiteLLM](https://docs.litellm.ai/docs/providers/fireworks_ai)                                        | Native `fireworks_ai` provider                     | Add `fireworks_ai/` before the Fireworks model ID                        |
| [Portkey](https://docs.portkey.ai/docs/integrations/llms/fireworks)                                   | Native Fireworks provider with BYOK                | Use the configured provider name, such as `@fireworks-ai/...`            |
| [Keywords AI](https://keywordsai.mintlify.app/integration/providers/fireworks)                        | Native Fireworks provider with BYOK                | Use Fireworks models through stored or per-request credentials           |
| [AISIX / API7](https://docs.api7.ai/ai-gateway/providers/fireworks-ai)                                | Native `fireworks-ai` provider with OpenAI adapter | Map a gateway alias to a Fireworks model ID                              |
| [Helicone](https://docs.helicone.ai/getting-started/integration-method/fireworks)                     | Fireworks proxy and provider integration           | Direct proxy calls preserve Fireworks model IDs                          |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/) | Custom provider, not a native Fireworks provider   | Configure the Fireworks inference base URL and a `custom-` provider slug |

## Use a gateway-managed model catalog

These gateways expose their own model catalogs. Fireworks may serve a request, but you are not connecting an arbitrary Fireworks model ID.

| Gateway                                                                                       | Fireworks support                                                                      |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Vercel AI Gateway](https://vercel.com/docs/ai-gateway/models-and-providers/provider-options) | Native provider slug `fireworks`, including BYOK for catalog models                    |
| [OpenRouter](https://openrouter.ai/provider/fireworks)                                        | Fireworks is an upstream provider for selected OpenRouter models                       |
| [Requesty](https://docs.requesty.ai/integrations/opencode)                                    | Fireworks-prefixed catalog models; newer models may need custom provider configuration |
| [Helicone AI Gateway](https://docs.helicone.ai/gateway/overview)                              | Fireworks appears in the unified gateway model registry                                |

<Note>
  Gateway catalogs do not necessarily expose `firerouter/...` IDs. Verify that
  the gateway preserves the exact Fireworks model ID and forwards any provider
  headers you require.
</Note>

## LiteLLM Proxy

Use LiteLLM as a shared gateway for Fireworks serverless models, model routers, and deployments. Developers call one OpenAI-compatible **chat completions** API. You manage provider credentials and access control on the LiteLLM server.

### Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* LiteLLM Proxy installed:

```bash wrap theme={null}
pip install "litellm[proxy]"
```

### Configure Fireworks models

Add each model you want to expose to `config.yaml`. In `litellm_params.model`, prefix the Fireworks model ID with `fireworks_ai/`. For example, `firerouter/opus` becomes `fireworks_ai/firerouter/opus`.

```yaml theme={null}
model_list:
  - model_name: accounts/fireworks/models/glm-5p2
    litellm_params:
      model: fireworks_ai/accounts/fireworks/models/glm-5p2
      api_key: os.environ/FIREWORKS_AI_API_KEY
      api_base: https://api.fireworks.ai/inference/v1

  - model_name: firerouter/opus
    litellm_params:
      model: fireworks_ai/firerouter/opus
      api_key: os.environ/FIREWORKS_AI_API_KEY
      api_base: https://api.fireworks.ai/inference/v1
```

See the [LiteLLM Fireworks AI provider docs](https://docs.litellm.ai/docs/providers/fireworks_ai) for dedicated deployments and other options.

### Start the proxy

```bash wrap theme={null}
export FIREWORKS_AI_API_KEY="$FIREWORKS_API_KEY"
litellm --config config.yaml
```

### Call a model

If [LiteLLM virtual keys](https://docs.litellm.ai/docs/proxy/virtual_keys) are configured, clients authenticate with a virtual key:

```bash wrap theme={null}
curl http://localhost:4000/chat/completions \
  -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "firerouter/opus",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

### API key layout

| Key                                 | Who holds it                         | Used for                                |
| ----------------------------------- | ------------------------------------ | --------------------------------------- |
| Fireworks API key (`fw_...`)        | LiteLLM server (env or secret store) | Upstream Fireworks inference            |
| LiteLLM virtual key (if configured) | Each developer or service            | Proxy authentication and spend tracking |

### Model routers

Account-level Provider Keys determine whether closed models are eligible. An Anthropic key covers bare `firerouter` and routes containing a Claude family alias or Anthropic model ID. An OpenAI key covers routes containing Astra or another OpenAI model. For credentials on direct API calls, see [APIs and SDKs](/nexus/apis-and-sdks#credentials).
