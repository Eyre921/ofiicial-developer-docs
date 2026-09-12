---
title: "LiteLLM"
source: https://docs.fireworks.ai/ecosystem/firerouter/litellm
path: ecosystem/firerouter/litellm
---

Add FireRouter to a LiteLLM Proxy deployment

Add FireRouter to an existing [LiteLLM Proxy](/ecosystem/integrations/litellm) deployment so developers request one model instead of choosing between open and closed-source models on every call.

Your Fireworks API key authenticates FireRouter and pays for Fireworks-hosted calls. An Anthropic credential makes Claude Opus 5 eligible and pays for that provider's calls. Provider keys sent on individual requests are not persisted by FireRouter. See [Authentication](/ecosystem/firerouter/authentication).

## Prerequisites

* A running LiteLLM Proxy on **v1.98.0** configured for Fireworks (see [LiteLLM integration](/ecosystem/integrations/litellm))
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* Optional: an **Anthropic API key** (`sk-ant-...`) to make Claude Opus 5 eligible for the default `firerouter` slug. It is not needed for a Fireworks-only slug or when workspace BYOK is provisioned.

## Add FireRouter to `config.yaml`

```yaml theme={null}
model_list:
  - model_name: accounts/fireworks/routers/firerouter
    litellm_params:
      model: fireworks_ai/accounts/fireworks/routers/firerouter
      api_key: os.environ/FIREWORKS_AI_API_KEY
      extra_headers:
        x-anthropic-api-key: os.environ/ANTHROPIC_API_KEY
```

Use a router-qualified ID in `litellm_params.model`, such as `fireworks_ai/routers/firerouter` or the full `fireworks_ai/accounts/fireworks/routers/firerouter` shown above. Do not use bare `fireworks_ai/firerouter`, which LiteLLM interprets as a model rather than a router.

Set `ANTHROPIC_API_KEY` on the LiteLLM server when you want pass-through requests to include `x-anthropic-api-key` automatically. Developers do not need to send the Anthropic key on each request when it is configured here. Omit `extra_headers` for Fireworks-only routing or workspace BYOK.

<Note>
  A server-side Anthropic key is shared across all callers of that proxy deployment. If each developer should bring their own Anthropic key, omit `extra_headers` and have clients send `x-anthropic-api-key` on each request instead (see below).
</Note>

For server-managed Anthropic credentials, start or restart the proxy with both keys exported:

```bash theme={null}
export FIREWORKS_AI_API_KEY="fw_..."
export ANTHROPIC_API_KEY="sk-ant-..."
litellm --config config.yaml
```

## Call FireRouter

If LiteLLM virtual keys are configured, clients authenticate to LiteLLM with a virtual key:

```bash theme={null}
curl http://localhost:4000/chat/completions \
  -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/fireworks/routers/firerouter",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

Optional routing preference:

```yaml theme={null}
litellm_settings:
  model_group_settings:
    forward_client_headers_to_llm_api:
      - accounts/fireworks/routers/firerouter
```

```text theme={null}
-H "x-routing-preference: 4"
```

See [Routing preferences](/ecosystem/firerouter/routing-preferences) for values `1`–`5`.

## Per-developer Anthropic keys

If each caller should use their own Anthropic key, omit `extra_headers` from the model config, enable the header-forwarding configuration above, and have clients send the header on every request:

```bash theme={null}
curl http://localhost:4000/chat/completions \
  -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/fireworks/routers/firerouter",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

See [client header forwarding](https://docs.litellm.ai/docs/proxy/forward_client_headers) for configuration details.

## API key layout

| Key                                 | Who holds it                                                               | Used for                                                      |
| ----------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Fireworks API key (`fw_...`)        | LiteLLM server                                                             | FireRouter auth and redirected inference                      |
| LiteLLM virtual key (if configured) | Each developer or service                                                  | Proxy authentication and spend tracking                       |
| Anthropic API key (`sk-ant-...`)    | Optional: LiteLLM server (`extra_headers`) or each caller (request header) | Makes Claude models eligible and pays for Claude pass-through |

## Related

* [LiteLLM integration](/ecosystem/integrations/litellm): configure Fireworks models in LiteLLM Proxy
* [Quickstart](/ecosystem/firerouter/quickstart): direct API call examples
* [Authentication](/ecosystem/firerouter/authentication): header reference
* [Routing preferences](/ecosystem/firerouter/routing-preferences): tune cost vs. quality
