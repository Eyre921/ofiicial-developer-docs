---
title: "Microsoft Foundry"
source: https://docs.fireworks.ai/ecosystem/fireconnect/microsoft-foundry
path: ecosystem/fireconnect/microsoft-foundry
---

Route FireConnect harnesses through Fireworks models deployed in your Azure subscription

FireConnect can route supported harnesses through [Fireworks on Microsoft Foundry](/ecosystem/integrations/azure-foundry) instead of the Fireworks gateway. Usage is billed through Azure and counts toward your Microsoft Azure Consumption Commitment (MACC) where applicable.

<Card title="Microsoft Foundry portal setup" icon="microsoft" href="/ecosystem/integrations/azure-foundry">
  Enable Fireworks on Foundry, create a deployment, and find your project endpoint. Start here if you have not set up a Foundry resource yet.
</Card>

<Note>
  **CLI terminology:** The Foundry provider is `--provider azure` (or `on --azure`). Harness configs display the label **Fireworks on Microsoft Foundry**. With Foundry, `--model` is the model you deployed in Azure (for example, `FW-GLM-5.2`), not a Fireworks serverless short ID like `glm-fast-latest`.
</Note>

## Supported harnesses

| Harness          | Azure in FireConnect | Notes                                                         |
| ---------------- | -------------------- | ------------------------------------------------------------- |
| OpenCode         | Yes                  | `fireworks-azure` provider in `opencode.json`                 |
| Codex            | Yes                  | `fireworks-azure` block in `config.toml`                      |
| Pi               | Yes                  | `fireworks-azure` provider in `models.json`                   |
| Cursor           | Yes                  | OpenAI BYOK override pointed at Foundry                       |
| VS Code          | Yes                  | Custom chat-completions endpoint in `chatLanguageModels.json` |
| DeepSeek Harness | No                   | `deepseek on` always uses the direct Fireworks gateway        |
| Claude Code      | Not yet              | `claude on` always wires direct Fireworks today               |

OpenCode, Codex, Pi, Cursor, and VS Code support Foundry routing in FireConnect v0.9.0+. Claude Code and DeepSeek Harness do not.

## Prerequisites

* A Microsoft Foundry resource with at least one Fireworks model deployment (for example, `FW-GLM-5.2` or `FW-MiniMax-M2.5`)
* Your Foundry resource endpoint and Azure API key from the [Microsoft Foundry portal](https://ai.azure.com/)
* A supported harness installed locally
* FireConnect v0.9.0+ (see [Overview: Install](/ecosystem/fireconnect/overview#install))

<Warning>
  Use an **Azure API key** from Foundry, not a Fireworks key (`fw_...`) or Fire Pass key (`fpk_...`). Fire Pass is not supported on the Foundry path.
</Warning>

## Configure once, then enable harnesses

`fireconnect configure` sets the **Foundry provider and endpoint**. It does **not** set your Fireworks API key. Use `fireconnect login` for that when routing through the Fireworks gateway.

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY
```

FireConnect stores a top-level `provider` and `azure` block in `~/.fireconnect/config.json`. After configuring, enable harnesses normally:

```bash theme={null}
fireconnect opencode on --model FW-GLM-5.2
fireconnect codex on --model FW-GLM-5.2
fireconnect pi on --model FW-GLM-5.2
fireconnect cursor on --model FW-GLM-5.2
fireconnect vscode on --model FW-GLM-5.2
```

If you omit `--model`, FireConnect defaults to `FW-GLM-5.2`.

<Warning>
  **Cursor and VS Code:** fully quit the IDE before `on` or `off`. FireConnect writes SQLite state. In an interactive terminal it waits for you to quit; pass `--force` to write anyway.
</Warning>

### Endpoint normalization

Pass your Foundry endpoint to `--base-url`. FireConnect normalizes whatever you paste to the correct OpenAI-compatible base at `https://<resource>.services.ai.azure.com/openai/v1`:

* Bare resource root (`https://<resource>.services.ai.azure.com`)
* Portal **project endpoint** (`.../api/projects/<name>`)
* Foundry **Models** route (`.../models`)
* An already-correct base (`.../openai/v1`)

Find the endpoint in the Microsoft Foundry portal under **Project settings**.

### API key storage

* Pass `--api-key` to write the Azure key into `~/.fireconnect/config.json`
* Or export `AZURE_API_KEY` before `configure`. FireConnect stores an environment reference instead.

## One-off Foundry routing

Route a single harness through Foundry without changing global config:

```bash theme={null}
fireconnect opencode on \
  --azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --model FW-MiniMax-M2.5
```

If global config already has a Foundry endpoint, `--azure` alone reuses it:

```bash theme={null}
fireconnect cursor on --azure --model FW-GLM-5.2
```

## What each harness writes

Each harness writes a dedicated Foundry config distinct from the Fireworks gateway. `off` restores your original config byte-for-byte.

| Harness  | Config file                                 | Provider ID                  | Notes                                                                            |
| -------- | ------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------- |
| OpenCode | `~/.config/opencode/opencode.json`          | `fireworks-azure/FW-GLM-5.2` | `@ai-sdk/openai-compatible` adapter; `options.baseURL` + `options.apiKey`        |
| Codex    | `~/.codex/config.toml`                      | `fireworks-azure`            | `wire_api = "chat"`; bearer or `env_key = "AZURE_API_KEY"`                       |
| Pi       | `~/.pi/agent/models.json` + `settings.json` | `fireworks-azure`            | `openai-completions` provider; key as literal or `$AZURE_API_KEY` in `auth.json` |
| Cursor   | `state.vscdb`                               | Foundry deployment name      | OpenAI BYOK base URL + Azure key; one deployment in the picker                   |
| VS Code  | `chatLanguageModels.json` + `state.vscdb`   | Foundry deployment name      | Chat-completions endpoint; Azure key in secret storage                           |

`fireconnect <harness> status` reports `azure` as the provider along with the endpoint and model.

<Warning>
  `fireconnect model list` browses the **Fireworks serverless catalog** only. It does not list Foundry deployments. With `--provider azure`, set your model with `--model` on `on`.
</Warning>

## Turn off Foundry routing

There are two ways to stop using Microsoft Foundry, depending on what you want next.

### Switch back to direct Fireworks

Use this when you want to keep FireConnect enabled but route through the Fireworks gateway again instead of your Foundry deployment.

<Warning>
  While `~/.fireconnect/config.json` has `provider: azure`, running `fireconnect <harness> on` **without** `--azure` still routes through Foundry. Change the global provider first.
</Warning>

```bash theme={null}
fireconnect configure --provider fireworks

fireconnect login                    # if you have not signed in yet
fireconnect opencode on
fireconnect codex on
fireconnect pi on
fireconnect cursor on
fireconnect vscode on
```

Re-running `on` replaces the Foundry config with the normal Fireworks gateway config. You do **not** need to run `off` first.

The Azure endpoint and key remain stored in `~/.fireconnect/config.json` but are unused while `provider` is `fireworks`. They are used again if you run `configure --provider azure` later.

### Remove FireConnect from a harness entirely

Use `off` to restore the config snapshot from **before FireConnect was first enabled** for that harness. Your original provider settings are restored byte-for-byte:

```bash theme={null}
fireconnect pi off
fireconnect opencode off
fireconnect codex off
fireconnect cursor off
fireconnect vscode off
```

`off` removes Foundry wiring from harness config files. It does **not** change the global `provider` field in `~/.fireconnect/config.json`. If `provider` is still `azure`, the next `on` will route through Foundry again unless you run `configure --provider fireworks` first.

Restart the harness after `off` if it is already running. For Cursor and VS Code, quit the IDE before `off`.

### Remove FireConnect everywhere

```bash theme={null}
fireconnect uninstall
```

Disables all harnesses, restores every backup, and removes the CLI.

| Goal                                        | Commands                                                                     |
| ------------------------------------------- | ---------------------------------------------------------------------------- |
| Stop Foundry, keep FireConnect on Fireworks | `fireconnect configure --provider fireworks` then `fireconnect <harness> on` |
| Undo FireConnect for one harness            | `fireconnect <harness> off`                                                  |
| Undo FireConnect on all harnesses           | `fireconnect uninstall`                                                      |

## Verify routing

```bash theme={null}
fireconnect opencode status   # provider=azure, base URL, model
fireconnect codex status
fireconnect pi status
fireconnect cursor status
fireconnect vscode status
```

## Per-harness guides

* [OpenCode](/ecosystem/fireconnect/opencode#fireworks-on-microsoft-foundry)
* [Codex](/ecosystem/fireconnect/codex#fireworks-on-microsoft-foundry)
* [Pi](/ecosystem/fireconnect/pi#fireworks-on-microsoft-foundry)
* [Cursor](/ecosystem/fireconnect/cursor#fireworks-on-microsoft-foundry)
* [VS Code](/ecosystem/fireconnect/vscode#fireworks-on-microsoft-foundry)

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
