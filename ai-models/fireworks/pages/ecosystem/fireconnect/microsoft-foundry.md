---
title: "Microsoft Foundry"
source: https://docs.fireworks.ai/ecosystem/fireconnect/microsoft-foundry
path: ecosystem/fireconnect/microsoft-foundry
---

Route OpenCode, Codex, and Pi through Fireworks models deployed in your Azure subscription with FireConnect

FireConnect can route **OpenCode**, **Codex**, and **Pi** through [Fireworks on Microsoft Foundry](/ecosystem/integrations/azure-foundry) instead of the Fireworks gateway. Usage is billed through Azure and counts toward your Microsoft Azure Consumption Commitment (MACC) where applicable.

<Card title="Microsoft Foundry portal setup" icon="microsoft" href="/ecosystem/integrations/azure-foundry">
  Enable Fireworks on Foundry, create a deployment, and find your project endpoint — start here if you have not set up a Foundry resource yet
</Card>

<Note>
  **CLI terminology:** The Foundry provider is `--provider azure` (or `on --azure`). Harness configs display the label **Fireworks on Microsoft Foundry**. Model IDs are your **deployment names** (for example, `FW-GLM-5.1`) — not Fireworks serverless short IDs like `glm-fast-latest`.
</Note>

## Supported harnesses

| Harness     | Azure in FireConnect | Notes                                                                           |
| ----------- | -------------------- | ------------------------------------------------------------------------------- |
| OpenCode    | Yes                  | `fireworks-azure` provider in `opencode.json`                                   |
| Codex       | Yes                  | `fireworks-azure` block in `config.toml`                                        |
| Pi          | Yes                  | `fireworks-azure` provider in `models.json`                                     |
| Claude Code | Not yet              | `claude on` always wires direct Fireworks today                                 |
| Cursor      | Not yet              | `cursor on` always wires direct Fireworks; global `--provider azure` is ignored |
| VS Code     | Not yet              | `vscode on` always wires direct Fireworks today                                 |
| Deep Agents | Not yet              | `deepagents on` always wires direct Fireworks today                             |

FireConnect implements Azure routing for **OpenCode**, **Codex**, and **Pi** today. The other harnesses still route through the Fireworks gateway only — that is a **FireConnect implementation gap**, not a Foundry platform limitation. If you run `fireconnect configure --provider azure` and then `fireconnect cursor on` (or `claude on`, etc.), the harness enables **direct Fireworks** and does not read the global Azure settings.

## Prerequisites

* A Microsoft Foundry resource with at least one Fireworks model deployment (for example, `FW-GLM-5.1` or `FW-MiniMax-M2.5`)
* Your Foundry resource endpoint and Azure API key from the [Microsoft Foundry portal](https://ai.azure.com/)
* OpenCode, Codex, or Pi installed locally
* FireConnect installed (see [Overview — Install](/ecosystem/fireconnect/overview#install))

<Warning>
  Use an **Azure API key** from Foundry — not a Fireworks key (`fw_...`) or Fire Pass key (`fpk_...`). Fire Pass is not supported on the Foundry path.
</Warning>

## Configure once, then enable harnesses

`fireconnect configure` sets the **Foundry provider and endpoint**. It does **not** set your Fireworks API key — use `fireconnect login` for that when routing through the Fireworks gateway.

```bash theme={null}
export AZURE_API_KEY=<your-azure-api-key>

fireconnect configure \
  --provider azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY
```

FireConnect stores a top-level `provider` and `azure` block in `~/.fireconnect/config.json`. After configuring, enable harnesses normally:

```bash theme={null}
fireconnect opencode on --main FW-GLM-5.1
fireconnect codex on --main FW-GLM-5.1
fireconnect pi on --main FW-GLM-5.1
```

If you omit `--main`, FireConnect defaults to `FW-GLM-5.1`.

### Endpoint normalization

Pass your Foundry endpoint to `--base-url`. FireConnect normalizes whatever you paste to the correct OpenAI-compatible base at `https://<resource>.services.ai.azure.com/openai/v1`:

* Bare resource root (`https://<resource>.services.ai.azure.com`)
* Portal **project endpoint** (`.../api/projects/<name>`)
* Foundry **Models** route (`.../models`)
* An already-correct base (`.../openai/v1`)

Find the endpoint in the Microsoft Foundry portal under **Project settings**.

### API key storage

* Pass `--api-key` to write the Azure key into `~/.fireconnect/config.json`
* Or export `AZURE_API_KEY` before `configure` — FireConnect stores an environment reference instead

## One-off Foundry routing

Route a single harness through Foundry without changing global config:

```bash theme={null}
fireconnect opencode on \
  --azure \
  --base-url https://<resource>.services.ai.azure.com \
  --api-key $AZURE_API_KEY \
  --main FW-MiniMax-M2.5
```

If global config already has a Foundry endpoint, `--azure` alone reuses it:

```bash theme={null}
fireconnect opencode on --azure --main FW-GLM-5.1
```

## What each harness writes

Each harness writes a dedicated `fireworks-azure` provider distinct from the Fireworks gateway. `off` restores your original config byte-for-byte.

| Harness  | Config file                                 | Provider ID                    | Notes                                                                            |
| -------- | ------------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------- |
| OpenCode | `~/.config/opencode/opencode.json`          | `fireworks-azure/<deployment>` | `@ai-sdk/openai-compatible` adapter; `options.baseURL` + `options.apiKey`        |
| Codex    | `~/.codex/config.toml`                      | `fireworks-azure`              | `wire_api = "chat"`; bearer or `env_key = "AZURE_API_KEY"`                       |
| Pi       | `~/.pi/agent/models.json` + `settings.json` | `fireworks-azure`              | `openai-completions` provider; key as literal or `$AZURE_API_KEY` in `auth.json` |

`fireconnect <harness> status` reports `azure` as the provider along with the endpoint and deployment name.

<Warning>
  `fireconnect <harness> model list` and `model select` browse the **Fireworks serverless catalog** only. They do not list Foundry deployments. With `--provider azure`, set your deployment with `--main` on `on`.
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
```

Re-running `on` replaces the `fireworks-azure` provider with the normal Fireworks gateway config. You do **not** need to run `off` first.

The Azure endpoint and key remain stored in `~/.fireconnect/config.json` but are unused while `provider` is `fireworks`. They are used again if you run `configure --provider azure` later.

### Remove FireConnect from a harness entirely

Use `off` to restore the config snapshot from **before FireConnect was first enabled** for that harness — your original provider settings, byte-for-byte:

```bash theme={null}
fireconnect pi off
fireconnect opencode off
fireconnect codex off
```

`off` removes the `fireworks-azure` provider from harness config files. It does **not** change the global `provider` field in `~/.fireconnect/config.json`. If `provider` is still `azure`, the next `on` will route through Foundry again unless you run `configure --provider fireworks` first.

Restart the harness after `off` if it is already running.

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
fireconnect opencode status   # provider=azure, base URL, deployment name
fireconnect codex status
fireconnect pi status
```

## Per-harness guides

* [OpenCode](/ecosystem/fireconnect/opencode#fireworks-on-microsoft-foundry)
* [Codex](/ecosystem/fireconnect/codex#fireworks-on-microsoft-foundry)
* [Pi](/ecosystem/fireconnect/pi#fireworks-on-microsoft-foundry)

## Source

FireConnect is open source: [github.com/fw-ai/fireconnect](https://github.com/fw-ai/fireconnect)
