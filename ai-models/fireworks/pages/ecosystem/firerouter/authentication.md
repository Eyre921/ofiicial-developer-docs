---
title: "Authentication"
source: https://docs.fireworks.ai/ecosystem/firerouter/authentication
path: ecosystem/firerouter/authentication
---

BYOK headers and API keys for FireRouter

Every request is authenticated with a Fireworks API key. Provider credentials sent on individual requests are forwarded only to the selected provider and are not persisted by FireRouter. If workspace BYOK is provisioned on your Fireworks account, Fireworks stores the provider credential in your workspace and supplies it server-side. Contact the Fireworks team to enable workspace BYOK.

## Credentials

| Credential                   | Header or env                                      | When it is needed                                  |
| ---------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| Fireworks API key (`fw_...`) | `Authorization: Bearer` or `X-Fireworks-Api-Key`   | FireRouter auth and redirected Fireworks inference |
| Anthropic credential         | `x-anthropic-api-key`, or auth sent by Claude Code | To make Claude models eligible                     |
| OpenAI API key (`sk-...`)    | `x-openai-api-key`                                 | To make OpenAI models eligible                     |

FireRouter requires a standard Fireworks API key (`fw_...`). Fire Pass keys (`fpk_...`) are not supported.

The default `firerouter` model uses **Claude Opus 5** as its primary model. Anthropic credentials make that pass-through leg eligible. Without them, FireRouter removes Claude Opus 5 from the candidate pool and can still serve an eligible Fireworks-hosted model such as GLM 5.3.

For a model-specific [FireRouter slug](/ecosystem/firerouter/overview#choose-different-models), each provider-hosted member is eligible only when its credential is available. A request pinned directly to a provider-hosted model fails with `no_credential` when that credential is unavailable. Slugs containing only Fireworks-hosted models need no additional provider key.

## Claude Code with FireConnect

When Claude Code is routed through [FireConnect](/ecosystem/fireconnect/claude-code#firerouter), Anthropic auth usually comes from **Claude Code itself**, not a separate FireConnect prompt:

| Source                                               | Works for FireRouter pass-through?                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------- |
| Claude subscription login                            | Yes                                                                 |
| Browser OAuth (`/login` in Claude Code)              | Yes                                                                 |
| `ANTHROPIC_API_KEY` in Claude Code settings or env   | Yes                                                                 |
| `--anthropic-api-key` on `fireconnect claude on`     | Yes                                                                 |
| `fireconnect configure --anthropic-api-key`          | Yes                                                                 |
| Workspace BYOK provisioned on your Fireworks account | Yes (server-side; requires Fireworks team enablement; no local key) |

FireConnect does not prompt for Anthropic credentials during Claude Code setup. Claude Code attaches its existing Anthropic login at request time. For direct HTTP calls, send `x-anthropic-api-key` when you want Claude models to be eligible; omit it to route only among eligible Fireworks-hosted members.

## Fireworks key header

Send your Fireworks API key with either header:

```text theme={null}
-H "Authorization: Bearer $FIREWORKS_API_KEY"
# or
-H "X-Fireworks-Api-Key: $FIREWORKS_API_KEY"
```

## Anthropic provider key

The canonical header for Anthropic pass-through is:

```text theme={null}
-H "x-anthropic-api-key: $ANTHROPIC_API_KEY"
```

`x-api-key` and `Authorization: Bearer` are also accepted as Anthropic credentials. If either carries the Anthropic credential, send the Fireworks key separately as `X-Fireworks-Api-Key`; one `Authorization` header cannot carry both credentials. New integrations should prefer `x-anthropic-api-key`.

Example:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "x-anthropic-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"firerouter","messages":[{"role":"user","content":"Say pong."}]}'
```

## OpenAI provider key

When the selected FireRouter slug includes an OpenAI model, send your OpenAI API key as:

```text theme={null}
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

| Response                                         | Cause                                                                                 | Fix                                                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `401` with `You must provide an API key`         | Fireworks key header missing or empty                                                 | Send `Authorization: Bearer $FIREWORKS_API_KEY` or `X-Fireworks-Api-Key`                             |
| `401` with `The API key you provided is invalid` | Gateway rejected the key                                                              | Confirm a valid `fw_...` key in the [dashboard](https://app.fireworks.ai/settings/users/api-keys)    |
| `403` with Fire Pass authorization error         | A Fire Pass key (`fpk_...`) was used                                                  | Use a standard Fireworks API key (`fw_...`)                                                          |
| `403` with data residency error                  | Data residency is enabled on the Fireworks account                                    | Use a residency-compatible pinned serverless model                                                   |
| `404` with `Model id not found`                  | Unknown model ID, FireRouter access denial, or model entitlement denial               | Confirm the model ID and account access; contact Fireworks if you expect access                      |
| `400` with `no_credential`                       | A pinned provider model or preference `1` requires an unavailable provider credential | Send the provider credential, choose a route with another eligible member, or use preference `2`–`5` |
| Provider `401`                                   | Provider key is invalid                                                               | Check the key sent as `x-anthropic-api-key` or `x-openai-api-key`                                    |

## Related

* [Quickstart](/ecosystem/firerouter/quickstart): API call examples
* [Claude Code (manual setup)](/ecosystem/firerouter/claude-code): `settings.json` setup
* [Overview](/ecosystem/firerouter/overview): routing model and model ID
