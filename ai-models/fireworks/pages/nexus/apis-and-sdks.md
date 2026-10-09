---
title: "APIs and SDKs"
source: https://docs.fireworks.ai/nexus/apis-and-sdks
path: nexus/apis-and-sdks
---

Call Fireworks from custom agents, background runners, services, HTTP APIs, and SDKs

Call Fireworks from custom agents, background jobs, or services with curl, the OpenAI SDK, the Anthropic SDK, or the Fireworks SDK. Send requests to `https://api.fireworks.ai/inference` and use the same model ID across each supported API.

## Compatible APIs

Choose the endpoint your SDK or client already uses:

| API format | Endpoint | Typical clients |
| - | - | - |
| **Chat completions** (OpenAI-style) | `POST /v1/chat/completions` | OpenAI SDK, most LLM gateways |
| **Messages** (Anthropic-style) | `POST /v1/messages` | Anthropic SDK |
| **Responses** (OpenAI-style) | `POST /v1/responses` | OpenAI Responses API clients |

For client setup, see [OpenAI compatibility](/tools-sdks/openai-compatibility), [Anthropic compatibility](/tools-sdks/anthropic-compatibility), or the [Responses API](/guides/response-api).

## Call the API

Send your Fireworks key and any model ID:

```bash wrap theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-latest",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

Router IDs such as `firerouter/opus` work the same way on all three APIs.

<Card title="FireRouter examples for every API and SDK" icon="code" href="/nexus/firerouter/setup#api-and-sdk">
  cURL, OpenAI, Anthropic, and Fireworks SDK examples for Chat Completions,
  Responses, and Messages, with provider-key headers.
</Card>

## Read the serving model

For a router request, the response `model` field names the model that served the turn, such as `glm-5p3` or `claude-opus-5-5`, not the router ID you sent. See [Verify routing](/nexus/firerouter#verify-routing).

## Credentials

| Credential | How to provide it | When |
| - | - | - |
| Fireworks API key (`fw_...`) | `Authorization` bearer token or `X-Fireworks-Api-Key` header | Every request; bills open-model traffic to your Fireworks account |
| Anthropic | Connect an Anthropic [Provider Key](/nexus/provider-keys) if enabled, or send `x-anthropic-api-key` Any route containing a Claude family alias or Anthropic model ID. Bare `firerouter` needs an Anthropic or an OpenAI credential | |
| OpenAI | Connect an OpenAI [Provider Key](/nexus/provider-keys) if enabled, or send `x-openai-api-key` | Any route containing Astra or another OpenAI model |
| Amazon Bedrock | [Amazon Bedrock](/nexus/provider-keys/bedrock) Provider Key | A route that includes one of your mapped models. Usage bills to your AWS account. |

An Anthropic or OpenAI key in a request header applies only to that request. A key connected through Provider Keys is available at the account level, so clients and gateways do not need to send it with every call.

A route containing both providers needs both credentials. You can combine an account-level key for one provider with a request header for the other.

Fireworks also accepts Anthropic credentials in `x-api-key` or `Authorization: Bearer`. One `Authorization` header cannot carry both the Fireworks and Anthropic keys. If it carries the Anthropic key, send the Fireworks key in `X-Fireworks-Api-Key`. Prefer `x-anthropic-api-key` for new integrations.

In every SDK, `api_key` is the Fireworks key. Pass provider keys as extra headers, as shown in [FireRouter Setup](/nexus/firerouter/setup#api-and-sdk).

## Limitations

* Accounts with data residency enabled must use a residency-compatible pinned serverless model. Other model-router requests are rejected.
* Model routers are not available through Microsoft Foundry.
* See [What happens without a closed-model credential](/nexus/firerouter#what-happens-without-a-closed-model-credential).

## Errors

| Response | Cause | Fix |
| - | - | - |
| `401` | Fireworks key is missing or invalid | Send a valid `fw_...` key with `Authorization: Bearer` or `X-Fireworks-Api-Key` |
| Request rejected for data residency | The requested route is not residency-compatible | Pin a residency-compatible serverless model |
| `404` `Model id not found` | Unknown id, or the account cannot use this router | Check the model id and account access |
| `400` `no_credential` | The closed model you named has no provider key | Connect [Provider Keys](/nexus/provider-keys) where available. For Anthropic or OpenAI, you can instead send the provider header. |
| Upstream provider authentication failure | The provider credential is wrong, revoked, or lacks permission | Check the Anthropic, OpenAI, or Amazon Bedrock credential and its permissions; exact status and message come from that provider |

## Model routers and deployment routers

A `firerouter/...` id is a model router. [Routers](/deployments/routers) load-balance traffic across your own Fireworks deployments.

## See also

* [FireRouter](/nexus/firerouter)
* [Provider Keys](/nexus/provider-keys)
* [Routing Preferences](/nexus/routing-preferences)
