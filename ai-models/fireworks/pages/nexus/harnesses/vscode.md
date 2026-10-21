---
title: "VS Code"
source: https://docs.fireworks.ai/nexus/harnesses/vscode
path: nexus/harnesses/vscode
---

Add Fireworks models and Nexus Auto to GitHub Copilot Chat in VS Code with the Nexus CLI or manual setup.

Nexus CLI adds a **Fireworks** provider to GitHub Copilot Chat's custom endpoints. This requires Copilot **Pro or Enterprise**.

PreviewOpenAI Chat CompletionsNexus Auto

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

**2. Quit VS Code**

**Quit VS Code before connecting or running `off`.**

**3. Connect VS Code**

```bash wrap theme={null}
nexus vscode
nexus vscode status
```

**4. Restart and pick a model**

Restart VS Code, then pick a model under **Other Models → Fireworks** in Copilot Chat. `glm-latest` and `glm-fast-latest` are text-only; `glm-flash-latest` supports images.

![VS Code Chat model picker showing the Fireworks provider with Auto selected and DeepSeek, GLM, and Kimi models](https://mintcdn.com/fireworksai/qp-9FYlGs5qTS-0n/images/nexus/vscode-chat-model-picker.png?fit=max\&auto=format\&n=qp-9FYlGs5qTS-0n\&q=85\&s=6a7d65116a2dc1e0d534856c6c394a7c)

> [!TIP]
>
> `nexus vscode status` shows the provider, where the key comes from, and the configured model.

## Use Nexus Auto

Nexus Auto (`auto`) is supported on the Chat Completions API.

* **Anthropic and OpenAI model turns:** connect an Anthropic or OpenAI [Provider Key](/nexus/provider-keys). Nexus CLI doesn't send local keys on `auto`.
* **Manual setup:** send `x-anthropic-api-key` and `x-openai-api-key` headers yourself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

Nexus CLI doesn't touch MCP. Set up servers in VS Code as usual.

Nexus CLI does not add web search to VS Code. See [Web Search](/nexus/web-search).

## Troubleshooting

See [Nexus Auto](/nexus/auto#troubleshooting) for issues that affect every harness.

## Manual setup (advanced)

In Copilot Chat, open **Language Models**, click **+ Add Models...**, and choose **Custom Endpoint**. Use `https://api.fireworks.ai/inference/v1`, your Fireworks key, and a model ID such as `glm-latest`.

Follow the step-by-step screenshots in [GitHub Copilot](/ecosystem/integrations/github-copilot).

See [what changes without the Nexus CLI](/nexus/manual-setup#what-changes-without-the-nexus-cli).

## What the Nexus CLI writes

> **See what Nexus CLI writes**
>
> ```json chatLanguageModels.json theme={null}
> [
>   {
>     "name": "Fireworks",
>     "vendor": "customendpoint",
>     "apiType": "chat-completions",
>     "apiKey": "${input:chat.lm.secret.fw-...}",
>     "models": [
>       {
>         "id": "auto",
>         "name": "Auto",
>         "url": "https://api.fireworks.ai/inference",
>         "maxInputTokens": 1048575,
>         "maxOutputTokens": 131072,
>         "vision": true,
>         "toolCalling": true
>       }
>     ]
>   }
> ]
> ```
>
> The key is stored separately in `state.vscdb`, encrypted with Electron `safeStorage`. On Linux, encryption needs `libsecret`; without it, VS Code only obfuscates the key and Nexus CLI warns you.
>
> | Platform | `chatLanguageModels.json` | `state.vscdb` |
> | - | - | - |
> | Linux | `~/.config/Code/User/` | `~/.config/Code/User/globalStorage/` |
> | macOS | `~/Library/Application Support/Code/User/` | `~/Library/Application Support/Code/User/globalStorage/` |
> | Windows | `%APPDATA%\Code\User\` | `%APPDATA%\Code\User\globalStorage\` |
