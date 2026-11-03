---
title: "LLM Gateways"
source: https://docs.fireworks.ai/nexus/llm-gateways
path: nexus/llm-gateways
---

Connect Fireworks to LiteLLM, Portkey, Vercel AI Gateway, Helicone, Keywords AI, AISIX, Requesty, OpenRouter, or Cloudflare AI Gateway

Gateways integrate with Fireworks in two ways. Some connect to your Fireworks account and preserve Fireworks model IDs. Others expose selected Fireworks models through a gateway-managed catalog.

## Check whether your gateway can use Nexus Auto

To call `auto`, your gateway must:

1. Connect to your Fireworks account.
2. Send the `auto` model ID unchanged.
3. Send your Fireworks API key.
4. Provide an Anthropic or OpenAI credential if you want one of those models.

A gateway-managed catalog can use Nexus Auto only when that catalog lists `auto`. Fireworks serving some of the catalog's models does not make `auto` available.

## Connect your Fireworks account

These gateways connect to your Fireworks account and keep Fireworks model IDs: [LiteLLM](https://docs.litellm.ai/docs/providers/fireworks_ai), [Portkey](https://docs.portkey.ai/docs/integrations/llms/fireworks), [Keywords AI](https://keywordsai.mintlify.app/integration/providers/fireworks), [AISIX / API7](https://docs.api7.ai/ai-gateway/providers/fireworks-ai), [Helicone](https://docs.helicone.ai/getting-started/integration-method/fireworks), and [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/).

| Gateway | Fireworks integration | Model naming |
| - | - | - |
| LiteLLM | Native `fireworks_ai` provider | Add `fireworks_ai/` before the full Fireworks path, such as `fireworks_ai/accounts/fireworks/routers/auto` |
| Portkey | Native Fireworks provider with bring your own key (BYOK) | Use the configured provider name, such as `@fireworks-ai/...` |
| Keywords AI | Native Fireworks provider with BYOK | Use Fireworks models through stored or per-request credentials |
| AISIX / API7 | Native `fireworks-ai` provider with OpenAI adapter | Map a gateway alias to a Fireworks model ID |
| Helicone | Fireworks proxy and provider integration | Direct proxy calls preserve Fireworks model IDs |
| Cloudflare AI Gateway | Custom provider, not a native Fireworks provider | Configure the Fireworks inference base URL and a `custom-` provider slug |

## Use a gateway-managed model catalog

[Vercel AI Gateway](https://vercel.com/docs/ai-gateway/models-and-providers/provider-options), [OpenRouter](https://openrouter.ai/provider/fireworks), [Requesty](https://docs.requesty.ai/integrations/opencode), and [Helicone AI Gateway](https://docs.helicone.ai/gateway/overview) expose their own model catalogs. Fireworks may serve a request, but you can call only the models the gateway lists.

| Gateway | Fireworks support |
| - | - |
| Vercel AI Gateway | Native provider slug `fireworks`, including bring your own key for catalog models |
| OpenRouter | Fireworks is an upstream provider for selected OpenRouter models |
| Requesty | Fireworks-prefixed catalog models; newer models may need custom provider configuration |
| Helicone AI Gateway | Fireworks appears in the unified gateway model registry |

## LiteLLM Proxy

Use LiteLLM as a shared gateway for Fireworks serverless models, Nexus Auto, and deployments. Developers call one OpenAI-compatible **chat completions** API, and LiteLLM manages the Fireworks connection and client access.

Closed-model credentials can come from Provider Keys (when enabled for the account), the LiteLLM config, or forwarded client headers. See [Provide closed-model credentials](#provide-closed-model-credentials).

**1. Install LiteLLM Proxy**

You need a [Nexus API key](https://nexus.fireworks.ai/settings/api-keys) (`fw_...`).

```bash wrap theme={null}
pip install "litellm[proxy]"
```

**2. Configure a Fireworks model**

Add each model to `config.yaml`. Keep `model_name` short, and use `fireworks_ai/` plus the full Fireworks path in `litellm_params.model`:

```yaml config.yaml theme={null}
model_list:
  - model_name: glm-latest
    litellm_params:
      model: fireworks_ai/accounts/fireworks/routers/glm-latest
      api_key: os.environ/FIREWORKS_API_KEY
      api_base: https://api.fireworks.ai/inference/v1
```

A short router ID such as `fireworks_ai/auto` returns `404 Model not found`. Use the full path.

| Model | `litellm_params.model` |
| - | - |
| `auto` and `-latest` aliases, such as `glm-latest` | `fireworks_ai/accounts/fireworks/routers/<id>` |
| Pinned models, such as `glm-5p3` | `fireworks_ai/accounts/fireworks/models/<id>` |

Recent LiteLLM versions expand a short ID to `accounts/fireworks/models/<id>`, which is why a short router ID fails. The full path works on every version. See the [LiteLLM Fireworks AI provider docs](https://docs.litellm.ai/docs/providers/fireworks_ai) for dedicated deployments and other options.

**3. Start the proxy**

```bash wrap theme={null}
litellm --config config.yaml
```

**4. Call a model**

If [LiteLLM virtual keys](https://docs.litellm.ai/docs/proxy/virtual_keys) are configured, clients authenticate with a virtual key:

```bash wrap theme={null}
curl http://localhost:4000/chat/completions \
  -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-latest",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

API key layout:

| Key | Who holds it | Used for |
| - | - | - |
| Fireworks API key (`fw_...`) | LiteLLM server (env or secret store) | Upstream Fireworks inference |
| LiteLLM virtual key (if configured) | Each developer or service | Proxy authentication and spend tracking |

## Use Nexus Auto through a gateway

The gateway sends the `auto` model ID and your Fireworks API key to Fireworks. Nexus CLI is not required. For LiteLLM entries, the Portkey model format, and a test request, see [Nexus Auto](/nexus/auto#llm-gateway).

For supported models, see [Nexus Auto](/nexus/auto#supported-models).

### Provide closed-model credentials

`auto` [chooses from the models your credentials allow](/nexus/auto#which-models-auto-can-use):

* With an Anthropic credential, it can also use Anthropic models.
* With an OpenAI credential, it can also use OpenAI models.
* With neither, every turn uses Fireworks open models.

An [Amazon Bedrock](/nexus/provider-keys/bedrock) Provider Key covers a closed model you mapped there.

Provider keys can be stored once in the gateway or connected as Provider Keys, so clients and harnesses don't have to send them:

| Setup | Where the provider key lives | Clients send |
| - | - | - |
| **Provider Keys** | Your Fireworks account | Only their gateway key |
| **Keys in the gateway config** | The gateway's config or secret store | Only their gateway key |
| **Keys from each client** | Each client or harness | Their gateway key and a provider-key header |

> [tab] Provider Keys
>
> An account admin connects the required [Provider Keys](/nexus/provider-keys)
> once from [Settings](https://nexus.fireworks.ai/settings/provider-keys). The
> gateway stores only the Fireworks key. No provider credential passes
> through the gateway.
>
> Every Nexus plan includes Provider Keys. You can also use your own key: save it with `nexus auto`, or send it as a request header.
>
> ```bash wrap theme={null}
> curl http://localhost:4000/chat/completions \
>   -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "model": "auto",
>     "messages": [{"role": "user", "content": "Say pong in one word."}]
>   }'
> ```

> [tab] Keys in the gateway config
>
> Use this option when Provider Keys isn't turned on for your account. The
> gateway adds the provider-key headers to every request for Nexus Auto, so
> clients and harnesses send only their gateway key.
>
> In LiteLLM, add `extra_headers` to the `auto` entry. `os.environ/` reads
> the key from the proxy's environment:
>
> ```yaml config.yaml theme={null}
> model_list:
>   - model_name: auto
>     litellm_params:
>       model: fireworks_ai/accounts/fireworks/routers/auto
>       api_key: os.environ/FIREWORKS_API_KEY
>       api_base: https://api.fireworks.ai/inference/v1
>       extra_headers:
>         x-anthropic-api-key: os.environ/ANTHROPIC_API_KEY
> ```
>
> To give Nexus Auto an OpenAI key too, add
> `x-openai-api-key: os.environ/OPENAI_API_KEY` under `extra_headers`.
>
> For Portkey and other gateways, set the same headers as custom headers on the
> Fireworks provider or integration.

> [tab] Keys from each client
>
> Use this option when each team or user should call closed models with
> their own provider key. The client sends `x-anthropic-api-key`,
> `x-openai-api-key`, or both to the gateway.
>
> LiteLLM does not forward client headers by default. Enable
> [header forwarding](https://docs.litellm.ai/docs/proxy/forward_client_headers)
> in `config.yaml`:
>
> ```yaml theme={null}
> general_settings:
>   forward_client_headers_to_llm_api: true
> ```
>
> ```bash wrap theme={null}
> curl http://localhost:4000/chat/completions \
>   -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
>   -H "Content-Type: application/json" \
>   -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
>   -d '{
>     "model": "auto",
>     "messages": [{"role": "user", "content": "Say pong in one word."}]
>   }'
> ```

A provider-key header sent with a request takes precedence over a Provider Key connected to the account.

> [!WARNING]
>
> Gateways often log request headers. If provider keys travel as headers,
> check that the gateway redacts them in its logs. This applies whether the
> gateway adds the headers or clients send them. Provider Keys keeps provider
> credentials out of the gateway entirely.

LiteLLM returns your `model_name` in the response `model` field, not the model that served the turn. To confirm that closed models are reachable, send a request directly to Fireworks as shown in [Check which model served a turn](/nexus/auto#check-which-model-served-a-turn). For direct API calls, see [APIs and SDKs](/nexus/apis-and-sdks#credentials).
