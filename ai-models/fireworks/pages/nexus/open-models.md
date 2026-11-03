---
title: "Open Models"
source: https://docs.fireworks.ai/nexus/open-models
path: nexus/open-models
---

Use auto, version-tracking aliases, fast tiers, or pinned Fireworks open models in coding workflows.

Use a Fireworks open model directly when you want Fireworks to serve every turn. Choosing a specific open model requires an [Enterprise plan](/nexus/plans). On Pro and Team, use `auto`, which still routes turns to open models.

* Pro and Team requests that name an open model directly, such as `glm-latest` or `kimi-k3`, are refused with HTTP 403. Only `auto` is accepted.
* On Enterprise, Nexus CLI adds the coding-ready catalog to your harness's model picker when you connect it.

## Start with `auto`

`auto` picks a model for each new user turn. Nexus CLI makes it the default in every harness.

```bash wrap theme={null}
nexus claude
```

After you restart Claude Code, **Auto** is the default model in `/model`, and no `--model` flag is required.

In Claude Code, the Opus, Sonnet, and Haiku slots keep Claude's own models, and `/model` also lists **Auto**. Enterprise accounts also see the Fireworks models.

## Choose a family, tier, or version

On Enterprise, use `--model` when you want a specific family, tier, or version:

```bash wrap theme={null}
nexus claude --model glm-latest
```

| Kind | Example IDs | Behavior |
| - | - | - |
| **Latest** | `kimi-latest`, `glm-latest`, `deepseek-flash-latest` | Tracks the current version in the model family |
| **Fast** | `kimi-fast-latest`, `glm-fast-latest` | Favors lower latency at a higher token price |
| **Pinned** | `kimi-k3`, `glm-5p3`, `glm-5p3-flash` | Stays on the named version |

Prefer `*-latest` unless you need a pinned version. Aliases can move to newer models or be retired, so check the [current list](#find-a-model-id) before you hard-code one.

### Current aliases

These are all serverless aliases as of September 27, 2026. Treat this list as a snapshot. The [serverless models endpoint](#find-a-model-id) shows the current set, and `nexus model list` shows the current coding aliases. `deepseek-pro-latest` is retired.

| Alias | Current model | Tier | Input |
| - | - | - | - |
| `kimi-latest` | `kimi-k3` | Standard | Text and images |
| `kimi-fast-latest` | `kimi-k3` | Fast | Text and images |
| `glm-latest` | `glm-5p3` | Standard | Text |
| `glm-fast-latest` | `glm-5p3` | Fast | Text |
| `glm-flash-latest` | `glm-5p3-flash` | Standard | Text and images |
| `deepseek-flash-latest` | `deepseek-v4p1-flash` | Standard | Text and images |
| `minimax-latest` | `minimax-m3` | Standard | Text |
| `qwen-max-latest` | `qwen3p8-max` | Standard | Text and images |

`qwen-max-latest` is not in the coding catalog, so `nexus model list` does not show it.

## Find a model ID

List current models and aliases with Nexus CLI:

```bash wrap theme={null}
nexus model list
nexus model list --search glm
```

Without Nexus CLI, call the serverless models endpoint:

```bash wrap theme={null}
curl "https://api.fireworks.ai/v1/serverless/models?use_cases=coding" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

[Nexus Auto](/nexus/auto) has its own setting for which models it can use.

* The catalog is cached for one hour. `nexus model list --refresh` fetches the latest copy. Offline, `nexus model list` shows the last cached list.
* Each endpoint entry's `aliases` field lists the aliases that point to that model, such as `accounts/fireworks/routers/glm-latest` for `glm-5p3`. Use the last part, `glm-latest`, as the model ID.
* Remove `use_cases=coding` to list every serverless model.

## Check image support

`glm-latest` and `glm-fast-latest` are text-only. If an image reaches a text-only model in Claude Code, use `/rewind`, then switch to a vision-capable model such as Kimi or `glm-5p3-flash`.

* Image support for other aliases depends on the model currently behind each alias. See the Input column in Current aliases above, and check `nexus model list` before sending images.
* In Claude Code, `nexus claude status` marks each model `vision` or `text-only`.
* An image sent to a text-only model in Claude Code can break the session.

## Pricing

Open models bill to your Fireworks account at [Serverless Pricing](/serverless/pricing). Per-session estimates and account usage are in [Usage and Cost](/nexus/metrics). US-only model IDs, the endpoint, and pricing are in [US-only Serverless](/serverless/us-only-serverless#available-models).
