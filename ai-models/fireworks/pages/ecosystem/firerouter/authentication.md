---
title: "Authentication"
source: https://docs.fireworks.ai/ecosystem/firerouter/authentication
path: ecosystem/firerouter/authentication
---

BYOK headers and API keys for FireRouter

FireRouter uses a **bring-your-own-key** contract. The service validates your Fireworks key on every request and forwards your provider key only on pass-through legs to closed-source models. FireRouter does not store provider keys server-side.

## Required keys

| Key                              | Header or env                                    | Used for                                           |
| -------------------------------- | ------------------------------------------------ | -------------------------------------------------- |
| Fireworks API key (`fw_...`)     | `Authorization: Bearer` or `X-Fireworks-Api-Key` | FireRouter auth and redirected Fireworks inference |
| Anthropic API key (`sk-ant-...`) | `x-anthropic-api-key`                            | Claude pass-through                                |

The FireRouter model currently routes pass-through requests to **Claude Opus 4.8** (`claude-opus-4-8`), so an Anthropic key is required on every request. This pass-through model is subject to change.

## Fireworks key header

Send your Fireworks API key with either header:

```bash theme={null}
-H "Authorization: Bearer $FIREWORKS_API_KEY"
# or
-H "X-Fireworks-Api-Key: $FIREWORKS_API_KEY"
```

The legacy header `X-FireRouter-Fireworks-Key` is also accepted. New integrations should prefer `X-Fireworks-Api-Key`.

## Anthropic provider key

The canonical header for Anthropic pass-through is:

```bash theme={null}
-H "x-anthropic-api-key: $ANTHROPIC_API_KEY"
```

`x-api-key` and `Authorization: Bearer` are also accepted for Anthropic clients that send credentials that way. For new integrations, prefer `x-anthropic-api-key`.

Example:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "firerouter", "messages": [...]}'
```

## Common errors

| Response                             | Cause                                 | Fix                                                                                           |
| ------------------------------------ | ------------------------------------- | --------------------------------------------------------------------------------------------- |
| `401 Missing Fireworks API key`      | Fireworks key header missing or empty | Set `X-Fireworks-Api-Key` to your `fw_...` key                                                |
| `401 invalid Fireworks API key`      | Key rejected                          | Confirm the key is valid in the [dashboard](https://app.fireworks.ai/settings/users/api-keys) |
| Pass-through fails with provider 401 | Anthropic key missing or wrong header | Send the Anthropic key as `x-anthropic-api-key`                                               |

## Related

* [Quickstart](/ecosystem/firerouter/quickstart): API call examples
* [Claude Code (manual setup)](/ecosystem/firerouter/claude-code): `settings.json` setup
* [Overview](/ecosystem/firerouter/overview): routing model and model ID
