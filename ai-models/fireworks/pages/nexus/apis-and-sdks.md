---
title: "APIs and SDKs"
source: https://docs.fireworks.ai/nexus/apis-and-sdks
path: nexus/apis-and-sdks
---

Call Fireworks from custom agents, background runners, services, HTTP APIs, and SDKs

The same model ID works on every supported API.

## Compatible APIs

Choose the endpoint your SDK or client already uses:

| API | Base URL to configure | Full endpoint | Typical clients |
| - | - | - | - |
| Anthropic Messages | `https://api.fireworks.ai/inference` | `https://api.fireworks.ai/inference/v1/messages` | Anthropic SDK, Claude Code |
| OpenAI Chat Completions | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/chat/completions` | OpenAI SDK, Fireworks SDK, most gateways and harnesses |
| OpenAI Responses | `https://api.fireworks.ai/inference/v1` | `https://api.fireworks.ai/inference/v1/responses` | OpenAI SDK, Codex |

Anthropic-style clients add `/v1/messages` to the base URL themselves, so their base URL ends at `/inference`.

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

`auto` works the same way on all three APIs. For Nexus Auto examples in cURL and the OpenAI, Anthropic, and Fireworks SDKs, see [Nexus Auto](/nexus/auto#api-and-sdk).

For a Nexus Auto request, the response `model` field [names the model that served the turn](/nexus/auto#check-which-model-served-a-turn), such as `glm-5p3` or `claude-opus-5-5`, not `auto`.

The linked Nexus Auto examples cover Chat Completions, Responses, and Messages, with provider-key headers.

## Credentials

| Credential | How to provide it | When |
| - | - | - |
| Fireworks API key (`fw_...`) | `Authorization` bearer token or `X-Fireworks-Api-Key` header | Every request; bills open-model traffic to your Fireworks account |
| Anthropic | Connect an Anthropic [Provider Key](/nexus/provider-keys) if enabled, or send `x-anthropic-api-key` | You want `auto` to be able to use Anthropic models |
| OpenAI | Connect an OpenAI [Provider Key](/nexus/provider-keys) if enabled, or send `x-openai-api-key` | You want `auto` to be able to use OpenAI models |
| Amazon Bedrock | [Amazon Bedrock](/nexus/provider-keys/bedrock) Provider Key | You want `auto` to use a model you mapped there. Usage bills to your AWS account. |

In every SDK, `api_key` is the Fireworks key. Pass provider keys as extra headers, as shown in [Nexus Auto](/nexus/auto#api-and-sdk).

* An Anthropic or OpenAI key in a request header applies only to that request. A key connected through Provider Keys is available at the account level, so clients and gateways do not need to send it with every call.
* With both credentials, `auto` [can use Anthropic and OpenAI models](/nexus/auto#which-models-auto-can-use) and decides per turn. You can combine an account-level key for one provider with a request header for the other.
* Fireworks also accepts Anthropic credentials in `x-api-key` or `Authorization: Bearer`. One `Authorization` header cannot carry both the Fireworks and Anthropic keys. If it carries the Anthropic key, send the Fireworks key in `X-Fireworks-Api-Key`. Prefer `x-anthropic-api-key` for new integrations.

## Limitations

* With US [data residency](/accounts/data-residency), send Nexus Auto requests to `us.api.fireworks.ai`. Open-model turns run on [US-only Serverless](/serverless/us-only-serverless). Other regions must pin a model served in that region.
* Without an [Anthropic or OpenAI credential](/nexus/auto#provide-anthropic-and-openai-credentials), `auto` uses Fireworks open models.

## Troubleshooting

* **`401`:** the Fireworks key is missing or invalid. Send a valid `fw_...` key with `Authorization: Bearer` or `X-Fireworks-Api-Key`.
* **`404` `Model id not found`:** the model ID is unknown, or the account can't use this router. Check the model ID and your account's access.
* **`400` `no_credential`:** the closed model you named has no provider key. Connect [Provider Keys](/nexus/provider-keys) where available. For Anthropic or OpenAI, you can instead send the provider header.

| Response | Cause | Fix |
| - | - | - |
| Request rejected for data residency | The account's region isn't US, or the request didn't use the region's endpoint | Use `us.api.fireworks.ai` for US. For other regions, pin a model served in that region |
| Upstream provider authentication failure | The provider credential is wrong, revoked, or lacks permission | Check the Anthropic, OpenAI, or Amazon Bedrock credential and its permissions. The status and message come from that provider |

## See also

* [Nexus Auto](/nexus/auto)
* [Provider Keys](/nexus/provider-keys)
* [Effort](/nexus/orchestration-preferences)
* [Routers](/deployments/routers) load-balance traffic across your own Fireworks deployments. They are separate from `auto`, the Nexus Auto model ID.
