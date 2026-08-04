---
title: "Models"
source: https://docs.fireworks.ai/ecosystem/fireconnect/models
path: ecosystem/fireconnect/models
---

Switch models in FireConnect harnesses: latest vs fast, when to pick each ID, and US-only routers

```bash theme={null}
fireconnect model list --search kimi
fireconnect <harness> on --model <id>
# Cursor / VS Code: quit the IDE before on, then reopen
# Other harnesses: restart after on
```

`<harness>` is one of: `claude`, `opencode`, `codex`, `pi`, `cursor`, `vscode`, `deepagents`.

There is no `model select` command. Always use `on --model`.

```bash theme={null}
fireconnect opencode on --model kimi-fast-latest
fireconnect claude on --model firerouter
fireconnect claude on --interactive              # Claude: map all six slots
fireconnect claude on --opus glm-fast-latest --sonnet glm-fast-latest
```

Claude Code: `--model` sets **main** only; use `--opus`, `--sonnet`, `--haiku`, `--fable`, `--subagent`, or `--interactive` for the rest. Other harnesses take one `--model` for the default. Re-running `on` without `--model` keeps your current choice.

| Harness                          | Apply the change                                    |
| -------------------------------- | --------------------------------------------------- |
| Cursor, VS Code                  | **Quit the IDE**, run `on --model`, then reopen     |
| Claude Code                      | New session, or `/exit` then `claude --resume <id>` |
| OpenCode, Codex, Pi, Deep Agents | Restart the CLI after `on`                          |

## Latest vs Fast

FireConnect short IDs follow the same [Serverless serving paths](/serverless/serving-paths) as the API:

| Kind                       | Example IDs                           | When to use                                                                                                           |
| -------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Latest** (standard path) | `kimi-latest`, `glm-latest`           | Best price/quality. Version-tracking routers that move to the current model automatically.                            |
| **Fast**                   | `kimi-fast-latest`, `glm-fast-latest` | Interactive coding where token speed matters. Same model quality as latest, higher \$/token, aims for **100+ tok/s**. |
| **Pinned**                 | `kimi-k3`, `glm-5p2`, `kimi-k3-fast`  | Stable ID that does not track new versions.                                                                           |

Prefer `*-latest` / `*-fast-latest` unless you need a pin. Browse live IDs and prices with `fireconnect model list`.

## Which model when

| ID                  | Use when                                                          | Notes                                                  |
| ------------------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| `kimi-fast-latest`  | Default interactive coding; screenshots / UI                      | Vision. Default for most harnesses and Claude `fable`. |
| `kimi-latest`       | Strong agentic coding with vision, lower \$/token than Fast       | Vision. Standard path.                                 |
| `glm-fast-latest`   | Fast text-only agent loops (Claude `opus` / `sonnet` defaults)    | Text-only. 1M context.                                 |
| `glm-latest`        | Cheaper text-only coding / long context                           | Text-only. Same family as Fast at standard price.      |
| `deepseek-v4-flash` | Haiku / subagent / high-volume background work                    | Text-only. Lowest cost in the coding catalog.          |
| `firerouter`        | Auto-route easy work to open models, hard work to Claude Opus 4.8 | See [FireRouter](/ecosystem/firerouter/overview).      |

Also useful from `fireconnect model list`: `minimax-latest` / `qwen-plus-latest` (cheaper vision), `deepseek-v4-pro` (stronger text coding than Flash), `kimi-k2p7-code` / `kimi-k2p7-code-fast` (code-focused Kimi).

<Warning>
  GLM and DeepSeek Flash/Pro are **text-only**. Pasting images on those slots in Claude Code can break the session. Recover with `/rewind`, or use a Kimi ID. See [Claude Code troubleshooting](/ecosystem/fireconnect/claude-code#troubleshooting).
</Warning>

## US-only

For US-only inference (compliance), pass the **full router path** with `on --model`. FireConnect does not yet expand the short US slugs to routers (unknown short IDs map to `accounts/fireworks/models/...`, which is wrong for these endpoints).

| Model             | Full ID                                      |
| ----------------- | -------------------------------------------- |
| Kimi K3 (US)      | `accounts/fireworks/routers/kimi-k3-us`      |
| GLM 5.2 Fast (US) | `accounts/fireworks/routers/glm-5p2-fast-us` |

```bash theme={null}
fireconnect claude on --model accounts/fireworks/routers/kimi-k3-us
fireconnect opencode on --model accounts/fireworks/routers/glm-5p2-fast-us
```

US-only endpoints are a **10% premium** except GLM 5.2 Fast US (same price as global Fast). Details: [US-only Serverless](/serverless/us-only-serverless).

## Limits

* **Fire Pass** (`fpk_...`): Claude defaults to `kimi-fast-latest`. Catalog is limited. Not on Codex. FireConnect rejects `--model firerouter` with a Fire Pass key on **every** harness; use an `fw_...` account key for FireRouter.
* **Foundry**: pass the Azure deployment name (`FW-GLM-5.2`), not a short ID. Claude Code does not support Foundry.
* **FireRouter**: standard key only (`fw_...`), not Fire Pass. Cursor / Deep Agents need workspace BYOK.

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
</AccordionGroup>

## See also

* [FireConnect overview](/ecosystem/fireconnect/overview)
* [CLI reference](/ecosystem/fireconnect/cli-reference)
* [Harness guides](/ecosystem/fireconnect/claude-code)
