---
title: "Open Models"
source: https://docs.fireworks.ai/nexus/open-models
path: nexus/open-models
---

Use auto, version-tracking aliases, fast tiers, or pinned Fireworks open models in coding workflows.

Use a Fireworks open model directly when you want Fireworks to serve every turn. FireConnect automatically registers the coding-ready catalog when you connect a harness.

## Start with `auto`

`auto` chooses from frontier open models for each new user turn. It is the default on a standard Fireworks key.

Use `auto-instant` when you want a latency-first open-model mix. If fast models are disabled by model governance, use `auto`.

```bash wrap theme={null}
fireconnect claude
```

Restart Claude Code, open `/model`, and select **Auto**. No `--model` flag is required.

## Choose a family, tier, or version

Use `--model` only when you want a specific family, tier, or version:

```bash wrap theme={null}
fireconnect claude --model glm-latest
```

| Kind       | Example IDs                                        | Behavior                                       |
| ---------- | -------------------------------------------------- | ---------------------------------------------- |
| **Latest** | `kimi-latest`, `glm-latest`, `deepseek-pro-latest` | Tracks the current version in the model family |
| **Fast**   | `kimi-fast-latest`, `glm-fast-latest`              | Favors lower latency at a higher token price   |
| **Pinned** | `kimi-k3`, `glm-5p3`, `glm-5p3-flash`              | Stays on the named version                     |

Prefer `*-latest` unless you need a pinned version.

## Find a model ID

```bash wrap theme={null}
fireconnect model list
fireconnect model list --search glm
fireconnect model list --refresh
```

The catalog is cached for one hour. `--refresh` fetches the latest copy.

## Check image support

`glm-latest` and `glm-fast-latest` are text-only. Image support for other aliases depends on the model currently behind each alias. Check `fireconnect model list` before sending images.

If an image reaches a text-only model in Claude Code, use `/rewind` or switch to a vision-capable model such as Kimi or `glm-5p3-flash`.

## Use US-only models

Use the current model IDs, endpoint, and pricing guidance from [US-only Serverless](/serverless/us-only-serverless#available-models).

## Pricing

Open models bill to your Fireworks account at [Serverless Pricing](/serverless/pricing). For per-session estimates and account usage, see [Usage and Cost](/nexus/metrics).
