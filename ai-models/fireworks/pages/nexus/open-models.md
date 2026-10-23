---
title: "Open Models"
source: https://docs.fireworks.ai/nexus/open-models
path: nexus/open-models
---

Use auto, version-tracking aliases, fast tiers, or pinned Fireworks open models in coding workflows.

Use a Fireworks open model directly when you want Fireworks to serve every turn. When you connect a harness, Nexus CLI adds the coding-ready catalog to its model picker.

## Start with `auto`

`auto` picks a model for each new user turn. Nexus CLI makes it the default in every harness. In Claude Code, the Opus, Sonnet, and Haiku slots keep Claude's own models, and `/model` also lists **Auto** and the Fireworks models.

```bash wrap theme={null}
nexus claude
```

Restart Claude Code. **Auto** is the default model in `/model`, so you don't need a `--model` flag.

## Choose a family, tier, or version

Use `--model` only when you want a specific family, tier, or version:

```bash wrap theme={null}
nexus claude --model glm-latest
```

| Kind | Example IDs | Behavior |
| - | - | - |
| **Latest** | `kimi-latest`, `glm-latest`, `deepseek-flash-latest` | Tracks the current version in the model family |
| **Fast** | `kimi-fast-latest`, `glm-fast-latest` | Favors lower latency at a higher token price |
| **Pinned** | `kimi-k3`, `glm-5p3`, `glm-5p3-flash` | Stays on the named version |

Prefer `*-latest` unless you need a pinned version.

### Current aliases

These are all serverless aliases as of September 27, 2026. Aliases can move to newer models or be retired, so treat this list as a snapshot. The [serverless models endpoint](#find-a-model-id) shows the current set, and `nexus model list` shows the current coding aliases.

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

> [!NOTE]
>
> Aliases may change as Fireworks adds and retires models. For example,
> `deepseek-pro-latest` is retired. Check the current list before you
> hard-code an alias, as shown in [Find a model ID](#find-a-model-id).

## Find a model ID

List current models and aliases with Nexus CLI:

```bash wrap theme={null}
nexus model list
nexus model list --search glm
nexus model list --refresh
```

The catalog is cached for one hour. `--refresh` fetches the latest copy. Offline, `nexus model list` shows the last cached list.

Without Nexus CLI, call the serverless models endpoint:

```bash wrap theme={null}
curl "https://api.fireworks.ai/v1/serverless/models?use_cases=coding" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

Each entry's `aliases` field lists the aliases that point to that model, such as `accounts/fireworks/routers/glm-latest` for `glm-5p3`. Use the last part, `glm-latest`, as the model ID. Remove `use_cases=coding` to list every serverless model.

To control which models Nexus Auto can use, see [Nexus Auto](/nexus/auto).

## Check image support

`glm-latest` and `glm-fast-latest` are text-only. Image support for other aliases depends on the model currently behind each alias. See the Input column in [Current aliases](#current-aliases), and check `nexus model list` before sending images. In Claude Code, `nexus claude status` marks each model `vision` or `text-only`.

If an image reaches a text-only model in Claude Code, the session can break. Use `/rewind`, then switch to a vision-capable model such as Kimi or `glm-5p3-flash`.

## Use US-only models

Use the current model IDs, endpoint, and pricing guidance from [US-only Serverless](/serverless/us-only-serverless#available-models).

## Pricing

Open models bill to your Fireworks account at [Serverless Pricing](/serverless/pricing). For per-session estimates and account usage, see [Usage and Cost](/nexus/metrics).
