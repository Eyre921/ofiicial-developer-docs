---
title: "DeepSeek Harness"
source: https://docs.fireworks.ai/nexus/harnesses/deepseek
path: nexus/harnesses/deepseek
---

Connect DeepSeek Harness (dsh) to Fireworks models and Nexus Auto with the Nexus CLI or manual setup.

DeepSeek's coding agent (`dsh`) runs named profiles, such as `tui`, `web`, and `headless`, under `$DSH_HOME`, which defaults to `~/.dsh`. Restart `dsh` after changing a profile.

Generally availableOpenAI Chat CompletionsNexus Auto with manual setup

## Quick start

**1. Install and sign in**

```bash wrap theme={null}
curl -fsSL https://nexus.fireworks.ai/install.sh | bash
```

Requires Node.js 18 or later, `git`, and `bash`. On Windows, run it from Git Bash; PowerShell breaks the script's line endings.

```bash wrap theme={null}
nexus login
```

Sign in with your browser, or paste a Fireworks key.

Already set up? Skip to step 2.

**2. Connect DeepSeek Harness**

```bash wrap theme={null}
nexus deepseek
nexus deepseek status
```

**3. Restart dsh**

Restart `dsh`. It starts on `auto` and goes straight to Fireworks, with no DeepSeek key prompt.

> [!TIP]
>
> `nexus deepseek status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus CLI can add `auto`, but it does not send provider keys from `dsh`. For turns on Anthropic or OpenAI models, connect a [Provider Key](/nexus/provider-keys) or use [manual setup](#manual-setup-advanced) to send `x-anthropic-api-key` and `x-openai-api-key` headers.

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in `dsh` as usual.

Nexus CLI does not add web search to DeepSeek Harness. See [Web Search](/nexus/web-search).

## Troubleshooting

Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

Create the profile folder once, then add a patch to it. Repeat for each profile you use.

```bash wrap theme={null}
dsh --profile tui --dump-config > /dev/null
```

```yaml ~/.dsh/profiles/tui/cordis.patch.yml theme={null}
- id: llm-pi-ai
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

Nexus CLI adds a `fireworks` provider to `~/.dsh/settings.yaml` and to each existing profile's `cordis.patch.yml`, which `dsh` 0.1.7 and later read. `off` restores both from the snapshot under `~/.nexus/deepseek/`.

**\~/.dsh**

**settings.yaml**

**.credentials.yaml**

**profiles/\<profile>**

**cordis.patch.yml**
