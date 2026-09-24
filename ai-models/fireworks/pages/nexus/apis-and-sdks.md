---
title: "APIs and SDKs"
source: https://docs.fireworks.ai/nexus/apis-and-sdks
path: nexus/apis-and-sdks
---

Call Fireworks from custom agents, background runners, services, HTTP APIs, and SDKs

Call Fireworks from custom agents, background jobs, or services with curl, the OpenAI SDK, or the Anthropic SDK. Send requests to `https://api.fireworks.ai/inference` and use the same model ID across each supported wire API.

## Compatible APIs

Choose the endpoint your SDK or client already uses:

| Wire API                            | Endpoint                    | Typical clients               |
| ----------------------------------- | --------------------------- | ----------------------------- |
| **Chat completions** (OpenAI-style) | `POST /v1/chat/completions` | OpenAI SDK, most LLM gateways |
| **Messages** (Anthropic-style)      | `POST /v1/messages`         | Anthropic SDK                 |
| **Responses** (OpenAI-style)        | `POST /v1/responses`        | OpenAI Responses API clients  |

For client setup, see [OpenAI compatibility](/tools-sdks/openai-compatibility), [Anthropic compatibility](/tools-sdks/anthropic-compatibility), or the [Responses API](/guides/response-api).

## Call the API

### Chat completions

Most direct API clients use chat completions:

```bash wrap theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "firerouter/opus",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

If your account has an Anthropic Provider Key, that request can use Claude Opus. Otherwise, add `-H "x-anthropic-api-key: $ANTHROPIC_API_KEY"` to the request. To use Astra, set `"model": "firerouter/astra"` and connect an OpenAI Provider Key or send `x-openai-api-key`.

### Messages (Anthropic-style)

Anthropic Messages clients use the same model id on `/v1/messages`:

```bash wrap theme={null}
curl https://api.fireworks.ai/inference/v1/messages \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "firerouter/opus",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

### Responses (OpenAI-style)

OpenAI Responses clients send `input` to `/v1/responses`:

```bash wrap theme={null}
curl https://api.fireworks.ai/inference/v1/responses \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "firerouter/opus",
    "input": "Say pong in one word."
  }'
```

Router IDs and provider credentials work the same way across all three APIs. If the account has no Anthropic Provider Key, add `-H "x-anthropic-api-key: $ANTHROPIC_API_KEY"`.

## Read the serving model

For a router request, the response `model` field identifies the model that served the request, such as `glm-5p3`, `claude-opus-5-5`, or `gpt-6-astra`. It does not repeat the router ID you sent.

Easy prompts tend to stay on the open model. Harder prompts tend to use the family named in the router ID. Neither result is guaranteed for a single request. Continue sending the short router slug, such as `firerouter/opus`.

## Credentials

| Credential                   | How to provide it                                               | When                                                                                   |
| ---------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Fireworks API key (`fw_...`) | `Authorization` bearer token or `X-Fireworks-Api-Key` header    | Every request; bills open-model traffic to your Fireworks account                      |
| Anthropic                    | [Provider Keys](/nexus/provider-keys), or `x-anthropic-api-key` | Bare `firerouter`, or any route containing a Claude family alias or Anthropic model ID |
| OpenAI                       | Provider Keys, or `x-openai-api-key`                            | Any route containing Astra or another OpenAI model                                     |

A provider key in a request header applies only to that request. A key connected through Provider Keys is available at the account level, so clients and gateways do not need to send it with every call.

Fireworks also accepts Anthropic credentials in `x-api-key` or `Authorization: Bearer`. One `Authorization` header cannot carry both the Fireworks and Anthropic keys. If it carries the Anthropic key, send the Fireworks key in `X-Fireworks-Api-Key`. Prefer `x-anthropic-api-key` for new integrations.

For an OpenAI SDK pointed at Fireworks, `api_key` is the Fireworks key. Pass the OpenAI provider key as a header:

```python wrap theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/inference/v1",
    default_headers={"x-openai-api-key": os.environ["OPENAI_API_KEY"]},
)
```

Drop `default_headers` when an OpenAI Provider Key is already connected.

## Limitations

* Accounts with data residency enabled must use a residency-compatible pinned serverless model. Other model-router requests are rejected.
* Model routers are not available through Microsoft Foundry.

## Errors

| Response                                 | Cause                                             | Fix                                                                                 |
| ---------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `401`                                    | Fireworks key is missing or invalid               | Send a valid `fw_...` key with `Authorization: Bearer` or `X-Fireworks-Api-Key`     |
| Request rejected for data residency      | The requested route is not residency-compatible   | Pin a residency-compatible serverless model                                         |
| `404` `Model id not found`               | Unknown id, or the account cannot use this router | Check the model id and account access                                               |
| `400` `no_credential`                    | The closed model you named has no provider key    | Connect [Provider Keys](/nexus/provider-keys), or send the provider header          |
| Upstream provider authentication failure | The provider key is wrong or revoked              | Check the Anthropic or OpenAI key; exact status and message come from that provider |

## Model routers and deployment routers

A `firerouter/...` id is a model router. [Routers](/deployments/routers) load-balance traffic across your own Fireworks deployments.

## See also

* [FireRouter](/nexus/firerouter)
* [Provider Keys](/nexus/provider-keys)
* [Routing Preferences](/nexus/routing-preferences)
