---
title: "Quickstart"
source: https://docs.fireworks.ai/ecosystem/firerouter/quickstart
path: ecosystem/firerouter/quickstart
---

Make your first FireRouter API call

This guide shows how to call FireRouter directly through the Fireworks inference API. See the [overview](/ecosystem/firerouter/overview) for how routing works and the [authentication](/ecosystem/firerouter/authentication) page for header details.

To use FireRouter in [Claude Code](https://claude.ai/code), see [Claude Code](/ecosystem/firerouter/claude-code).

## Prerequisites

* A [Fireworks API key](https://app.fireworks.ai/settings/users/api-keys) (`fw_...`)
* An **Anthropic API key** (`sk-ant-...`) for pass-through to Claude Opus 4.8

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

Simple prompts are usually redirected to GLM 5.2 on Fireworks. Harder prompts pass through to Claude Opus 4.8 using your Anthropic key.

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

## Verify routing

1. Send a trivial prompt (for example "rename foo to bar"). Expect a fast response routed to the open model.
2. Send a hard reasoning prompt. Expect pass-through to Claude Opus 4.8.
3. Optionally set `x-routing-preference` to bias routing. See [Routing preferences](/ecosystem/firerouter/routing-preferences).

You can also send the Fireworks key as `X-Fireworks-Api-Key` instead of `Authorization: Bearer`. See [Authentication](/ecosystem/firerouter/authentication) for the full header reference.

## Related

* [Overview](/ecosystem/firerouter/overview): model ID and routing pair
* [Authentication](/ecosystem/firerouter/authentication): header reference
* [Routing preferences](/ecosystem/firerouter/routing-preferences): tune cost vs. quality
* [LiteLLM](/ecosystem/firerouter/litellm): add FireRouter to LiteLLM Proxy
* [Claude Code](/ecosystem/firerouter/claude-code): harness setup with `settings.json`
