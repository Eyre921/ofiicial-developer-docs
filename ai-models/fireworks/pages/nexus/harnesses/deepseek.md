---
title: "DeepSeek Harness"
source: https://docs.fireworks.ai/nexus/harnesses/deepseek
path: nexus/harnesses/deepseek
---

Connect DeepSeek Harness (dsh) to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

DeepSeek's coding agent (`dsh`) runs named profiles, such as `tui`, `web`, and `headless`, under `$DSH_HOME`, which defaults to `~/.dsh`. Restart `dsh` after changing a profile.

Generally availableOpenAI Chat CompletionsNexus Auto

## Quick start

**1. Install and sign in**

```bash wrap theme={null}
curl -fsSL https://nexus.fireworks.ai/install.sh | bash
```

You need Node.js 22 or later, `git`, and `bash`. On Windows, run the installer from Git Bash. PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks API key (`fw_...`).

Already set up? Skip to step 2.

**2. Connect DeepSeek Harness**

```bash wrap theme={null}
nexus deepseek
nexus deepseek status
```

**3. Restart and pick a model**

Restart `dsh`. It starts on `auto` and goes straight to Fireworks, with no DeepSeek key prompt. To change the default, run `nexus deepseek --model glm-latest`.

> [!TIP]
>
> `nexus deepseek status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** save a key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key), then run `nexus deepseek` again. Nexus CLI adds the saved key to the `fireworks` provider headers. Or connect a [Provider Key](/nexus/provider-keys), which needs nothing saved locally.
* **Environment keys:** Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in `dsh` as usual.

Nexus CLI does not add web search to DeepSeek Harness. See [Web Search](/nexus/web-search).

## Microsoft Foundry

Nexus CLI doesn't connect DeepSeek Harness to Microsoft Foundry. For other options, see [Nexus for Microsoft Foundry](/nexus/microsoft-foundry).

## Troubleshooting

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness. Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

Create the profile folder once, then add a patch to it. Repeat for each profile you use. On `dsh` 0.2 and later, you can put the same patch in `~/.dsh/cordis.patch.yml` instead to cover every profile.

```bash wrap theme={null}
dsh --profile tui --dump-config > /dev/null
```

```yaml ~/.dsh/profiles/tui/cordis.patch.yml theme={null}
- id: llm-pi-ai
  name: "@deepseek-ai/dsh-llm-pi-ai"
  config:
    providers:
      fireworks:
        displayName: Fireworks
        apiKeyEnv: FIREWORKS_API_KEY
        api: openai-completions
        baseURL: https://api.fireworks.ai/inference/v1
        models:
          - id: glm-latest
            name: GLM (Latest)
            reasoning: true
            contextWindow: 1048576
            maxTokens: 131072
- id: agent-default-model
  name: "@deepseek-ai/dsh-agent-default-model"
  config:
    provider: fireworks
    model: glm-latest
```

```bash wrap theme={null}
export FIREWORKS_API_KEY="fw_..."
dsh tui
```

To use Nexus Auto with Anthropic or OpenAI model turns, add `headers` to the provider, such as `x-anthropic-api-key: sk-ant-...`, and use `auto` as the model. The [harness setup](/nexus/auto#nexus-cli) generates the full patch.

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

Nexus CLI writes the `fireworks` provider and default model to three layers, so every `dsh` version picks them up:

* `~/.dsh/settings.yaml`
* `~/.dsh/cordis.patch.yml`, the home-level patch that `dsh` 0.2 and later apply to every profile, including new ones
* Each existing profile's `cordis.patch.yml`, which `dsh` 0.1.7 and later read

Your key goes to `~/.dsh/.credentials.yaml` as `FIREWORKS_API_KEY`.

**\~/.dsh**

**settings.yaml**

**cordis.patch.yml**

**.credentials.yaml**

**profiles/\<profile>**

**cordis.patch.yml**

> **See what Nexus CLI writes**
>
> ```yaml ~/.dsh/settings.yaml theme={null}
> llm-pi-ai:
>   providers:
>     fireworks:
>       displayName: Fireworks
>       apiKeyEnv: FIREWORKS_API_KEY
>       api: openai-completions
>       baseURL: https://api.fireworks.ai/inference/v1
>       headers:
>         x-anthropic-api-key: sk-ant-...
>       models:
>         - id: auto
>           name: Auto
>           reasoning: true
>           input: [text, image]
>           contextWindow: 1048575
>           maxTokens: 131072
> agent-default-model:
>   provider: fireworks
>   model: auto
> ```
>
> ```yaml ~/.dsh/.credentials.yaml theme={null}
> FIREWORKS_API_KEY: fw_...
> ```
>
> The patch files carry the same provider and model as `llm-pi-ai` and `agent-default-model` entries. The `x-anthropic-api-key` and `x-openai-api-key` headers appear only for keys you saved with `nexus auto`. Nexus CLI also adds its own attribution headers.
>
> Every file is saved with mode `0600`. `off` restores each one byte-for-byte from the snapshot under `~/.nexus/deepseek/`, and deletes the ones Nexus CLI created. Use `--config-path` for a `settings.yaml` stored elsewhere. Nexus CLI then keeps the credentials file and patches in that folder.
