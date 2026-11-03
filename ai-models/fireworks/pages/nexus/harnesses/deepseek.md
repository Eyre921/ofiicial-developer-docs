---
title: "DeepSeek Harness"
source: https://docs.fireworks.ai/nexus/harnesses/deepseek
path: nexus/harnesses/deepseek
---

Connect DeepSeek Harness (dsh) to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

Support summary:

* API the harness speaks to Fireworks: OpenAI Chat Completions
* Nexus Auto: Supported
* Native web search: Not added by Nexus. See [Web search](/nexus/auto#web-search).

`dsh` runs named profiles, such as `tui`, `web`, and `headless`, under `$DSH_HOME`, which defaults to `~/.dsh`. Restart `dsh` after changing a profile.

Plan access: Pro and Team don't include general access to open models. They use Nexus Auto (`auto`) along with their own Claude or ChatGPT models, and Nexus Auto still sends turns to open models. Enterprise accounts also get general access to open models on Fireworks serverless. See [Plans and Accounts](/nexus/plans).

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

If the Nexus CLI is already installed and signed in, skip to step 2.

**2. Connect DeepSeek Harness**

```bash wrap theme={null}
nexus deepseek
```

Nexus Auto is the default model. To pick another one, run `nexus deepseek --model <id>`, such as `--model glm-latest`.

`nexus deepseek status` shows the provider, where the key comes from, and the configured model.

**3. Restart dsh**

Restart `dsh`. It connects to Fireworks without prompting for a DeepSeek key.

To restore your original settings, run `nexus deepseek off`.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin.

- Instead of a Provider Key, a developer can save their own key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key) and run `nexus deepseek` again. Nexus CLI adds the saved key to the `fireworks` provider headers. A Provider Key needs nothing saved locally.
- Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
- Nexus Auto (`auto`) is supported on the Chat Completions API.
- Manual setup sends `x-anthropic-api-key` and `x-openai-api-key` headers itself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* Nexus CLI doesn't add [web search](/nexus/auto#web-search) to DeepSeek Harness.

## Troubleshooting

Fixes for issues that affect every harness are in [Nexus Auto troubleshooting](/nexus/auto#troubleshooting).

* Upgrading from an earlier version: see [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

Create the profile folder once, then add a patch to it. Repeat for each profile you use.

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

Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

* On `dsh` 0.2 and later, you can put the same patch in `~/.dsh/cordis.patch.yml` instead to cover every profile.
* To use Nexus Auto with Anthropic or OpenAI model turns, add `headers` to the provider, such as `x-anthropic-api-key: sk-ant-...`, and use `auto` as the model. The [harness setup](/nexus/auto#nexus-cli) generates the full patch.

## What the Nexus CLI writes

Nexus CLI writes the `fireworks` provider and default model to three layers, so every `dsh` version picks them up:

* `~/.dsh/settings.yaml`
* `~/.dsh/cordis.patch.yml`, the home-level patch that `dsh` 0.2 and later apply to every profile, including new ones
* Each existing profile's `cordis.patch.yml` (`~/.dsh/profiles/<profile>/cordis.patch.yml`), which `dsh` 0.1.7 and later read

Your key goes to `~/.dsh/.credentials.yaml` as `FIREWORKS_API_KEY`.

```yaml ~/.dsh/settings.yaml theme={null}
llm-pi-ai:
  providers:
    fireworks:
      displayName: Fireworks
      apiKeyEnv: FIREWORKS_API_KEY
      api: openai-completions
      baseURL: https://api.fireworks.ai/inference/v1
      headers:
        x-anthropic-api-key: sk-ant-...
      models:
        - id: auto
          name: Auto
          reasoning: true
          input: [text, image]
          contextWindow: 1048575
          maxTokens: 131072
agent-default-model:
  provider: fireworks
  model: auto
```

```yaml ~/.dsh/.credentials.yaml theme={null}
FIREWORKS_API_KEY: fw_...
```

* The patch files carry the same provider and model as `llm-pi-ai` and `agent-default-model` entries.
* The `x-anthropic-api-key` and `x-openai-api-key` headers appear only for keys you saved with `nexus auto`. Nexus CLI also adds its own attribution headers.
* Every file is saved with mode `0600`.
* `off` restores each one byte-for-byte from the snapshot under `~/.nexus/deepseek/`, and deletes the ones Nexus CLI created.
* Use `--config-path` for a `settings.yaml` stored elsewhere. Nexus CLI then keeps the credentials file and patches in that folder.
