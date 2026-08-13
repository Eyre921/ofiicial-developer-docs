---
title: "LiteLLM"
source: https://docs.fireworks.ai/ecosystem/firerouter/litellm
path: ecosystem/firerouter/litellm
---

Add FireRouter to a LiteLLM Proxy deployment

Add FireRouter to an existing [LiteLLM Proxy](/ecosystem/integrations/litellm) deployment so developers request one model instead of choosing between open and closed-source models on every call.

FireRouter uses bring-your-own-key (BYOK): your Fireworks API key pays for redirected calls, and an Anthropic API key pays for pass-through to Claude Opus 5. See [Authentication](/ecosystem/firerouter/authentication). FireRouter does not store provider keys.

## Prerequisites

* A running LiteLLM Proxy on **v1.95.0** configured for Fireworks (see [LiteLLM integration](/ecosystem/integrations/litellm))
* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* An **Anthropic API key** (`sk-ant-...`) for pass-through

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

Always use the full router resource ID in `litellm_params.model`. LiteLLM rewrites short names like `fireworks_ai/firerouter` to `accounts/fireworks/models/firerouter`, which FireRouter does not recognize.

Set `ANTHROPIC_API_KEY` on the LiteLLM server so pass-through requests include `x-anthropic-api-key` automatically. Developers do not need to send the Anthropic key on each request when it is configured here.

<Note>
  A server-side Anthropic key is shared across all callers of that proxy deployment. If each developer should bring their own Anthropic key, omit `extra_headers` and have clients send `x-anthropic-api-key` on each request instead (see below).
</Note>

Start or restart the proxy with both keys exported:

```bash theme={null}
export FIREWORKS_AI_API_KEY="fw_..."
export ANTHROPIC_API_KEY="sk-ant-..."
litellm --config config.yaml
```

## Call FireRouter

Clients authenticate to LiteLLM with a virtual key:

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

```bash theme={null}
-H "x-routing-preference: 4"
```

See [Routing preferences](/ecosystem/firerouter/routing-preferences) for values `1`–`5`.

## Per-developer Anthropic keys

If each caller should use their own Anthropic key, omit `extra_headers` from the model config and have clients send the header on every request:

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

Enable [client header forwarding](https://docs.litellm.ai/docs/proxy/forward_client_headers) for the `accounts/fireworks/routers/firerouter` model group if your LiteLLM version does not forward `x-` headers by default.

## API key layout

| Key                              | Who holds it                                                     | Used for                                 |
| -------------------------------- | ---------------------------------------------------------------- | ---------------------------------------- |
| Fireworks API key (`fw_...`)     | LiteLLM server                                                   | FireRouter auth and redirected inference |
| LiteLLM virtual key              | Each developer or service                                        | Proxy authentication and spend tracking  |
| Anthropic API key (`sk-ant-...`) | LiteLLM server (`extra_headers`) or each caller (request header) | Claude pass-through billing              |

## Related

* [LiteLLM integration](/ecosystem/integrations/litellm): configure Fireworks models in LiteLLM Proxy
* [Quickstart](/ecosystem/firerouter/quickstart): direct API call examples
* [Authentication](/ecosystem/firerouter/authentication): header reference
* [Routing preferences](/ecosystem/firerouter/routing-preferences): tune cost vs. quality
