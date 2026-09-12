---
title: "Quickstart"
source: https://docs.fireworks.ai/ecosystem/firerouter/quickstart
path: ecosystem/firerouter/quickstart
---

Make your first FireRouter API call

This guide shows how to call FireRouter directly through the Fireworks inference API. See the [overview](/ecosystem/firerouter/overview) for how routing works and the [authentication](/ecosystem/firerouter/authentication) page for header details.

For coding harnesses, use [FireConnect](/ecosystem/fireconnect/overview): `fireconnect <harness> on --model firerouter`. Claude Code supports Main plus named aliases; see [Claude Code — FireRouter](/ecosystem/fireconnect/claude-code#choose-where-firerouter-is-used) to configure each slot explicitly. For manual `settings.json` setup, see [Claude Code (manual setup)](/ecosystem/firerouter/claude-code).

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* Optional **Anthropic credentials** to make Claude Opus 5 eligible — an API key (`sk-ant-...`) for direct HTTP calls, or your existing Claude Code login when using [FireConnect](/ecosystem/fireconnect/claude-code#firerouter). Without them, FireRouter can still use eligible Fireworks-hosted models.

Fire Pass keys (`fpk_...`) and accounts with data residency enabled cannot use FireRouter. See [Availability limitations](/ecosystem/firerouter/overview#availability-limitations).

## Chat Completions

Send a request to the [Chat Completions](/tools-sdks/openai-compatibility) endpoint with the FireRouter model ID:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "firerouter",
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

With the default `firerouter` model ID, simple prompts are more likely to use GLM 5.3 (`glm-5p3`) on Fireworks. Harder prompts are more likely to use Claude Opus 5 (`claude-opus-5`) when Anthropic credentials are available. Routing is policy-driven; prompt difficulty alone does not guarantee either result for an individual request.

To use a different model combination, replace `firerouter` with one of the [model-specific FireRouter slugs](/ecosystem/firerouter/overview#choose-different-models).

If the selected slug includes an OpenAI model, send its key as `-H "x-openai-api-key: $OPENAI_API_KEY"`. See [Authentication](/ecosystem/firerouter/authentication).

## Anthropic Messages

For clients that speak the Anthropic Messages API:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/messages \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "firerouter",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Say pong in one word."}]
  }'
```

## Observe routing

Send both a simple prompt and a harder reasoning prompt, then inspect the `model` field in each response. It names the backend that served the request (for example `glm-5p3` or `claude-opus-5`), not `firerouter`. Simple prompts are more likely to use the Fireworks model and harder prompts are more likely to use the primary model, but neither result is guaranteed for an individual request. Use `x-routing-preference` to bias the decision. See [Routing preferences](/ecosystem/firerouter/routing-preferences).

You can also send the Fireworks key as `X-Fireworks-Api-Key` instead of `Authorization: Bearer`. See [Authentication](/ecosystem/firerouter/authentication) for the full header reference.

## Related

* [Overview](/ecosystem/firerouter/overview): model ID and routing pair
* [Authentication](/ecosystem/firerouter/authentication): header reference
* [Routing preferences](/ecosystem/firerouter/routing-preferences): tune cost vs. quality
* [LiteLLM](/ecosystem/firerouter/litellm): add FireRouter to LiteLLM Proxy
* [Claude Code (manual setup)](/ecosystem/firerouter/claude-code): edit `settings.json` directly
