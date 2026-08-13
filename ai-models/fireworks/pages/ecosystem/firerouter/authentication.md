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
| Anthropic API key (`sk-ant-...`) | `x-anthropic-api-key`                            | Calls to Claude models                             |
| OpenAI API key (`sk-...`)        | `x-openai-api-key`                               | Calls to OpenAI models                             |

The default `firerouter` model uses **Claude Opus 5** as its primary model, so every request requires an Anthropic key. FireRouter fails closed when the primary model's credential is missing; it does not silently restrict the route to Fireworks models.

For a model-specific [FireRouter slug](/ecosystem/firerouter/overview#choose-different-models), the first model's credential is required. Later models are eligible only when their credentials are present. Slugs that contain only Fireworks models need no additional provider key beyond the Fireworks API key.

## Fireworks key header

Send your Fireworks API key with either header:

```bash theme={null}
-H "Authorization: Bearer $FIREWORKS_API_KEY"
# or
-H "X-Fireworks-Api-Key: $FIREWORKS_API_KEY"
```

`X-FireRouter-Fireworks-Key` is also accepted. New integrations should prefer `X-Fireworks-Api-Key`.

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

## OpenAI provider key

When the selected FireRouter slug includes an OpenAI model, send your OpenAI API key as:

```bash theme={null}
-H "x-openai-api-key: $OPENAI_API_KEY"
```

Do not put the OpenAI provider key in the OpenAI client's `api_key` field. That field supplies the `Authorization` header used to authenticate to the Fireworks gateway, so it must contain your Fireworks API key. Pass the OpenAI provider key as a custom header:

```python theme={null}
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/inference/v1",
    default_headers={"x-openai-api-key": os.environ["OPENAI_API_KEY"]},
)
```

## Common errors

| Response                        | Cause                                                        | Fix                                                                                           |
| ------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `401 Missing Fireworks API key` | Fireworks key header missing or empty                        | Set `X-Fireworks-Api-Key` to your `fw_...` key                                                |
| `401 invalid Fireworks API key` | Key rejected                                                 | Confirm the key is valid in the [dashboard](https://app.fireworks.ai/settings/users/api-keys) |
| `400` with `no_credential`      | Required provider key missing or sent under the wrong header | Send the key under the provider-specific header                                               |
| Provider `401`                  | Provider key is invalid                                      | Check the key sent as `x-anthropic-api-key` or `x-openai-api-key`                             |

## Related

* [Quickstart](/ecosystem/firerouter/quickstart): API call examples
* [Claude Code (manual setup)](/ecosystem/firerouter/claude-code): `settings.json` setup
* [Overview](/ecosystem/firerouter/overview): routing model and model ID
