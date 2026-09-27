---
title: "LLM Gateways"
source: https://docs.fireworks.ai/nexus/llm-gateways
path: nexus/llm-gateways
---

Connect Fireworks to LiteLLM, Portkey, Vercel AI Gateway, Helicone, Keywords AI, AISIX, Requesty, OpenRouter, or Cloudflare AI Gateway

Gateways integrate with Fireworks in two ways. Some connect to your Fireworks account and preserve Fireworks model IDs. Others expose selected Fireworks models through a gateway-managed catalog.

## Check whether your gateway can use FireRouter

To call a model router such as `firerouter/opus`, your gateway must:

1. Connect to your Fireworks account.
2. Preserve the exact `firerouter/...` model ID.
3. Send your Fireworks API key.
4. Provide any Anthropic or OpenAI credential the route requires.

A gateway-managed catalog can use a FireRouter model only when that catalog lists the router ID. Fireworks serving some of the catalog's models does not make arbitrary `firerouter/...` IDs available.

## Connect your Fireworks account

| Gateway                                                                                               | Fireworks integration                                    | Model naming                                                                                                          |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [LiteLLM](https://docs.litellm.ai/docs/providers/fireworks_ai)                                        | Native `fireworks_ai` provider                           | Add `fireworks_ai/` before the full Fireworks path, such as `fireworks_ai/accounts/fireworks/routers/firerouter/opus` |
| [Portkey](https://docs.portkey.ai/docs/integrations/llms/fireworks)                                   | Native Fireworks provider with bring your own key (BYOK) | Use the configured provider name, such as `@fireworks-ai/...`                                                         |
| [Keywords AI](https://keywordsai.mintlify.app/integration/providers/fireworks)                        | Native Fireworks provider with BYOK                      | Use Fireworks models through stored or per-request credentials                                                        |
| [AISIX / API7](https://docs.api7.ai/ai-gateway/providers/fireworks-ai)                                | Native `fireworks-ai` provider with OpenAI adapter       | Map a gateway alias to a Fireworks model ID                                                                           |
| [Helicone](https://docs.helicone.ai/getting-started/integration-method/fireworks)                     | Fireworks proxy and provider integration                 | Direct proxy calls preserve Fireworks model IDs                                                                       |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/) | Custom provider, not a native Fireworks provider         | Configure the Fireworks inference base URL and a `custom-` provider slug                                              |

## Use a gateway-managed model catalog

These gateways expose their own model catalogs. Fireworks may serve a request, but you are not connecting an arbitrary Fireworks model ID.

| Gateway                                                                                       | Fireworks support                                                                      |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Vercel AI Gateway](https://vercel.com/docs/ai-gateway/models-and-providers/provider-options) | Native provider slug `fireworks`, including bring your own key for catalog models      |
| [OpenRouter](https://openrouter.ai/provider/fireworks)                                        | Fireworks is an upstream provider for selected OpenRouter models                       |
| [Requesty](https://docs.requesty.ai/integrations/opencode)                                    | Fireworks-prefixed catalog models; newer models may need custom provider configuration |
| [Helicone AI Gateway](https://docs.helicone.ai/gateway/overview)                              | Fireworks appears in the unified gateway model registry                                |

## LiteLLM Proxy

Use LiteLLM as a shared gateway for Fireworks serverless models, model routers, and deployments. Developers call one OpenAI-compatible **chat completions** API. LiteLLM manages the Fireworks connection and client access. Closed-model credentials can come from Fireworks Provider Keys, when enabled for the account, or from forwarded client headers.

### Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* LiteLLM Proxy installed:

```bash wrap theme={null}
pip install "litellm[proxy]"
```

### Configure a Fireworks model

Add each model you want to expose to `config.yaml`. Keep the client-facing `model_name` short. In `litellm_params.model`, use `fireworks_ai/` followed by the full Fireworks path:

| Model                                                                             | `litellm_params.model`                         |
| --------------------------------------------------------------------------------- | ---------------------------------------------- |
| Routers, `auto`, and `-latest` aliases, such as `firerouter/opus` or `glm-latest` | `fireworks_ai/accounts/fireworks/routers/<id>` |
| Pinned models, such as `glm-5p3`                                                  | `fireworks_ai/accounts/fireworks/models/<id>`  |

Recent LiteLLM versions expand a short ID to `accounts/fireworks/models/<id>`, so a short router ID such as `fireworks_ai/firerouter/opus` returns `404 Model not found`. The full path works on every version.

```yaml theme={null}
model_list:
  - model_name: glm-latest
    litellm_params:
      model: fireworks_ai/accounts/fireworks/routers/glm-latest
      api_key: os.environ/FIREWORKS_API_KEY
      api_base: https://api.fireworks.ai/inference/v1
```

See the [LiteLLM Fireworks AI provider docs](https://docs.litellm.ai/docs/providers/fireworks_ai) for dedicated deployments and other options.

### Start the proxy

```bash wrap theme={null}
litellm --config config.yaml
```

### Call a model

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

### API key layout

| Key                                 | Who holds it                         | Used for                                |
| ----------------------------------- | ------------------------------------ | --------------------------------------- |
| Fireworks API key (`fw_...`)        | LiteLLM server (env or secret store) | Upstream Fireworks inference            |
| LiteLLM virtual key (if configured) | Each developer or service            | Proxy authentication and spend tracking |

## Use FireRouter through a gateway

The gateway sends the exact `firerouter/...` model ID and your Fireworks API key to Fireworks. You do not need FireConnect. For router IDs and supported models, see [FireRouter](/nexus/firerouter#supported-models).

<Card title="Set up FireRouter in LiteLLM or Portkey" icon="shuffle" href="/nexus/firerouter/setup#llm-gateway">
  Router entries for LiteLLM, the Portkey model format, and a test request.
</Card>

### Provide closed-model credentials

A route containing a Claude model needs an Anthropic credential. A route containing a GPT model needs an OpenAI credential. A route containing both needs credentials for both providers. An [Amazon Bedrock](/nexus/provider-keys/bedrock) Provider Key covers routes that include a model you mapped there. Without a credential, FireRouter [leaves that closed model out](/nexus/firerouter#what-happens-without-a-closed-model-credential) and serves the turn with open models.

You do not need to pass provider keys from each client or harness. Store them in the gateway once, or connect them as Provider Keys:

| Setup                          | Where the provider key lives         | Clients send                                |
| ------------------------------ | ------------------------------------ | ------------------------------------------- |
| **Provider Keys**              | Your Fireworks account               | Only their gateway key                      |
| **Keys in the gateway config** | The gateway's config or secret store | Only their gateway key                      |
| **Keys from each client**      | Each client or harness               | Their gateway key and a provider-key header |

<Tabs>
  <Tab title="Provider Keys">
    An account admin connects the required [Provider Keys](/nexus/provider-keys)
    once from [Settings](https://app.fireworks.ai/settings/provider-keys). The
    gateway stores only the Fireworks key. No provider credential passes
    through the gateway.

    Provider Keys is not yet available on every account. See
    [Provider Keys](/nexus/provider-keys) to request it.

    ```bash wrap theme={null}
    curl http://localhost:4000/chat/completions \
      -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "firerouter/opus",
        "messages": [{"role": "user", "content": "Say pong in one word."}]
      }'
    ```
  </Tab>

  <Tab title="Keys in the gateway config">
    Use this option when Provider Keys is not enabled for your account. The
    gateway adds the provider-key headers to every request for a router, so
    clients and harnesses send only their gateway key.

    In LiteLLM, add `extra_headers` to each router entry. `os.environ/` reads
    the key from the proxy's environment:

    ```yaml config.yaml theme={null}
    model_list:
      - model_name: firerouter/opus
        litellm_params:
          model: fireworks_ai/accounts/fireworks/routers/firerouter/opus
          api_key: os.environ/FIREWORKS_API_KEY
          api_base: https://api.fireworks.ai/inference/v1
          extra_headers:
            x-anthropic-api-key: os.environ/ANTHROPIC_API_KEY

      - model_name: firerouter/opus/astra
        litellm_params:
          model: fireworks_ai/accounts/fireworks/routers/firerouter/opus/astra
          api_key: os.environ/FIREWORKS_API_KEY
          api_base: https://api.fireworks.ai/inference/v1
          extra_headers:
            x-anthropic-api-key: os.environ/ANTHROPIC_API_KEY
            x-openai-api-key: os.environ/OPENAI_API_KEY
    ```

    Clients call `firerouter/opus` with only their LiteLLM virtual key. For
    Portkey and other gateways, set the same headers as custom headers on the
    Fireworks provider or integration.
  </Tab>

  <Tab title="Keys from each client">
    Use this option when each team or user should call closed models with
    their own provider key. The client sends `x-anthropic-api-key`,
    `x-openai-api-key`, or both to the gateway.

    LiteLLM does not forward client headers by default. Enable forwarding in
    `config.yaml`:

    ```yaml theme={null}
    general_settings:
      forward_client_headers_to_llm_api: true
    ```

    ```bash wrap theme={null}
    curl http://localhost:4000/chat/completions \
      -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
      -H "Content-Type: application/json" \
      -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
      -d '{
        "model": "firerouter/opus",
        "messages": [{"role": "user", "content": "Say pong in one word."}]
      }'
    ```

    See [Forward client headers](https://docs.litellm.ai/docs/proxy/forward_client_headers)
    in the LiteLLM docs.
  </Tab>
</Tabs>

A provider-key header sent with a request takes precedence over a Provider Key connected to the account.

<Warning>
  Gateways often log request headers. If provider keys travel as headers,
  whether added by the gateway or sent by clients, check that the gateway
  redacts them in its logs. Provider Keys keeps provider credentials out of
  the gateway entirely.
</Warning>

LiteLLM returns your `model_name` in the response `model` field, not the model that served the turn. To confirm that closed models are reachable, send a request directly to Fireworks as shown in [Verify routing](/nexus/firerouter#verify-routing). For direct API calls, see [APIs and SDKs](/nexus/apis-and-sdks#credentials).
