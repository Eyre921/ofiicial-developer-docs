---
title: "Models"
source: https://docs.fireworks.ai/ecosystem/fireconnect/models
path: ecosystem/fireconnect/models
---

Switch models in FireConnect harnesses: latest vs fast, smart routers, and US-only endpoints

```bash theme={null}
fireconnect model list --search kimi
fireconnect model list --refresh          # bypass the 1-hour cache
fireconnect <harness> on --model <id>
# Cursor / VS Code: quit the IDE before on, then reopen
# Other harnesses: restart after on
```

`<harness>` is one of: `claude`, `opencode`, `codex`, `chatgpt`, `pi`, `cursor`, `vscode`, `deepseek`.

There is no `model select` command. Always use `on --model`.

```bash theme={null}
fireconnect opencode on --model kimi-fast-latest
fireconnect claude on --model firerouter
fireconnect claude on --interactive              # Claude model mapping wizard
fireconnect claude on --opus glm-fast-latest --sonnet auto-instant
```

Claude Code: `--model` sets **main** only; use slot flags or `--interactive` for the rest. Claude adds `[1m]` on 1M-context models for every slot. Re-running `on` without flags keeps your current mapping.

| Harness                               | Apply the change                                    |
| ------------------------------------- | --------------------------------------------------- |
| Cursor, VS Code                       | **Quit the IDE**, run `on --model`, then reopen     |
| Claude Code                           | New session, or `/exit` then `claude --resume <id>` |
| OpenCode, Codex, Pi, DeepSeek Harness | Restart the CLI after `on`                          |

## Browse the catalog

```bash theme={null}
fireconnect model list
fireconnect model list --search glm
fireconnect model list --json
fireconnect model list --refresh
```

FireConnect fetches coding-tagged serverless models, merges version-tracking aliases (`glm-latest`, `kimi-fast-latest`, …), and lists smart routers (`auto`, `auto-instant`, `firerouter`). Results are **cached for one hour** and work offline — `--refresh` refetches when you need the latest.

## Latest vs Fast

FireConnect short IDs follow the same [Serverless serving paths](/serverless/serving-paths) as the API:

| Kind                       | Example IDs                                                                 | When to use                                                                                                           |
| -------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Latest** (standard path) | `kimi-latest`, `glm-latest`, `deepseek-pro-latest`, `deepseek-flash-latest` | Best price/quality; tracks current model versions                                                                     |
| **Fast**                   | `kimi-fast-latest`, `glm-fast-latest`                                       | Interactive coding where token speed matters. Same model quality as latest, higher \$/token, aims for **100+ tok/s**. |
| **Pinned**                 | `kimi-k3`, `glm-5p2`, `kimi-k3-fast`                                        | Stable ID that does not track new versions.                                                                           |

Prefer `*-latest` / `*-fast-latest` unless you need a pin.

## Which model when

| ID                      | Use when                                                        | Notes                                                                                            |
| ----------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `kimi-fast-latest`      | Default interactive coding; screenshots / UI                    | Vision. Default for single-model harnesses and Claude `fable` on Fire Pass.                      |
| `kimi-latest`           | Strong agentic coding with vision, lower \$/token than Fast     | Vision. Standard path.                                                                           |
| `deepseek-pro-latest`   | Strong text-only coding and reasoning                           | Text-only. Claude `sonnet` default.                                                              |
| `deepseek-flash-latest` | Haiku / subagent / high-volume background work                  | Text-only. Default for Claude `haiku` and `subagent`.                                            |
| `glm-flash-latest`      | Vision-capable GLM for Fable / image tasks                      | Vision. Claude `fable` default on standard keys.                                                 |
| `glm-fast-latest`       | Fast text-only agent loops                                      | Text-only. 1M context.                                                                           |
| `glm-latest`            | Cheaper text-only coding / long context                         | Text-only. Claude `opus` default when FireRouter is not selected.                                |
| `firerouter`            | Auto-route easy work to open models, hard work to Claude Opus 5 | See [FireRouter](/ecosystem/firerouter/overview). Auto-pinned to Claude `opus` on first connect. |
| `auto`                  | Fireworks default open-model mix                                | Preview. Available on every Claude slot.                                                         |
| `auto-instant`          | Latency-first open-model mix                                    | Preview. Available on Claude Sonnet.                                                             |

Also useful from `fireconnect model list`: `minimax-latest` / `qwen-plus-latest` (cheaper vision), `kimi-k2p7-code` / `kimi-k2p7-code-fast` (code-focused Kimi), `glm-5p3` / `glm-5p3-flash`.

<Note>
  The pinned `deepseek-v4-flash` serverless model is deprecated. FireConnect v0.9.3+ migrates existing Claude defaults to `deepseek-flash-latest` on the next `claude on`. Prefer `-latest` aliases so future model upgrades don't require another config change.
</Note>

<Warning>
  GLM and DeepSeek Flash/Pro are **text-only**. Pasting images on those slots in Claude Code can break the session. Recover with `/rewind`, or use a Kimi or GLM Flash ID. See [Claude Code troubleshooting](/ecosystem/fireconnect/claude-code#troubleshooting).
</Warning>

## US-only

For US-only inference (compliance), pass the short US router slug with `on --model`:

| Model              | Short ID           |
| ------------------ | ------------------ |
| Kimi K3 (US)       | `kimi-k3-us`       |
| GLM 5.2 Fast (US)  | `glm-5p2-fast-us`  |
| GLM 5.3 Flash (US) | `glm-5p3-flash-us` |

```bash theme={null}
fireconnect claude on --model kimi-k3-us
fireconnect opencode on --model glm-5p2-fast-us
fireconnect claude on --model glm-5p3-flash-us
```

Beginning September 1, 2026, US-only endpoints launched from that date are priced at a **50% premium** over the matching global row (`glm-5p3-flash-us`). Earlier routers keep their launch rates: `kimi-k3-us` at a 10% premium, `glm-5p2-fast-us` at parity with global GLM 5.2 Fast. Details: [US-only Serverless](/serverless/us-only-serverless).

## Limits

* **Fire Pass** (`fpk_...`): Claude defaults to `kimi-fast-latest`. Catalog is limited. Not on Codex. FireConnect rejects `--model firerouter` with a Fire Pass key on **every** harness; use an `fw_...` account key for FireRouter.
* **Foundry**: pass the Azure deployment name (`FW-GLM-5.2`), not a short ID. Claude Code and DeepSeek Harness do not support Foundry.
* **FireRouter**: standard key only (`fw_...`), not Fire Pass. Cursor / DeepSeek Harness need workspace BYOK for Anthropic pass-through.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Nothing changed after on --model">
    Restart the harness. For Cursor and VS Code, fully quit the IDE **before** running `on`.
  </Accordion>

  <Accordion title="Stuck on FireRouter / Fire Pass">
    FireConnect rejects `--model firerouter` when your stored key is Fire Pass (`fpk_...`), on every harness. Switch to an `fw_...` account key, then run `fireconnect <harness> on --model firerouter` and restart the harness.
  </Accordion>

  <Accordion title="Foundry says the model was not found">
    Pass the Azure **deployment name** (for example `FW-GLM-5.2`), not a serverless short ID.
  </Accordion>

  <Accordion title="Catalog looks stale">
    Run `fireconnect model list --refresh`. Without network, FireConnect keeps showing the last cached catalog instead of clearing it.
  </Accordion>
</AccordionGroup>

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [CLI reference](/ecosystem/fireconnect/cli-reference)
* [Claude Code](/ecosystem/fireconnect/claude-code)
