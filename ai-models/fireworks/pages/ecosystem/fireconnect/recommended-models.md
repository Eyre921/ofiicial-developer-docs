---
title: "Recommended models"
source: https://docs.fireworks.ai/ecosystem/fireconnect/recommended-models
path: ecosystem/fireconnect/recommended-models
---

Serverless model short IDs and Fire Pass defaults for FireConnect

Browse live pricing and availability with `fireconnect model list`, then apply a choice with `fireconnect <harness> on --model <id>` or slot flags such as `--sonnet`.

```bash theme={null}
fireconnect model list --search glm
fireconnect claude on --model glm-fast-latest --sonnet kimi-fast-latest
```

## Serverless short IDs

These IDs apply to **direct Fireworks routing** and expand to full Fireworks paths automatically. With [Microsoft Foundry](/ecosystem/fireconnect/microsoft-foundry), pass your Foundry model instead (for example, `FW-GLM-5.2`) via `--model`.

| Short ID            | Best for                      | Notes                                                                                                                                                                            |
| ------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `glm-latest`        | All-around use, agentic tasks | Version-tracking router; strong reasoning, 1M context.                                                                                                                           |
| `glm-fast-latest`   | Latency-sensitive agentic use | Default for `main`, `opus`, and `fable` slots in Claude Code. Version-tracking router on the high-speed Fast serving path (100+ tok/s), at a higher per-token price. 1M context. |
| `glm-5p2-fast`      | Latency-sensitive agentic use | Same as `glm-fast-latest` but pinned to GLM 5.2 rather than version-tracking. 1M context.                                                                                        |
| `kimi-fast-latest`  | General use (lighter)         | Default `sonnet` slot in Claude Code. Fast Kimi variant with vision support.                                                                                                     |
| `glm-5p1`           | General use (lighter)         | Pinned GLM 5.1; use with `--sonnet glm-5p1` if you prefer it over the default.                                                                                                   |
| `deepseek-v4-flash` | Background / fast tasks       | Default `haiku` and `subagent` slots in Claude Code. Lowest latency.                                                                                                             |
| `firerouter`        | Automatic cost routing        | Sends simple work to open models and hard work to Claude Opus 4.8. See [FireRouter](/ecosystem/firerouter/overview).                                                             |

## Fire Pass keys

Fire Pass keys (`fpk_...`) default all slots to `glm-fast-latest`. The model browser shows Fire Pass-supported routers: `glm-latest`, `glm-fast-latest`, `glm-5p2-fast`, `kimi-fast-latest`, and `kimi-k2p7-code-fast`.

Fire Pass works with direct Fireworks routing only. Fire Pass keys are not supported on Codex, Microsoft Foundry, or `--model firerouter` in FireConnect (on any harness).

<Warning>
  Codex does not support Fire Pass keys yet. Use a standard Fireworks API key (`fw_...`) with Codex.
</Warning>

## Per-harness defaults

Claude Code uses multi-slot aliases (`main`, `opus`, `sonnet`, `haiku`, `fable`, `subagent`). See [Claude Code](/ecosystem/fireconnect/claude-code#default-model-mapping) for the full mapping table.

Other harnesses set a single default model on `on`. Pass `--model <id>` to override.

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [CLI reference](/ecosystem/fireconnect/cli-reference)
* [Side-by-side demo](/ecosystem/fireconnect/demo)
