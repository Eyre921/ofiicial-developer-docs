---
title: "VS Code"
source: https://docs.fireworks.ai/nexus/harnesses/vscode
path: nexus/harnesses/vscode
---

Add Fireworks models and Nexus Auto to GitHub Copilot Chat in VS Code with the Nexus CLI or manual setup.

You need Copilot **Pro or Enterprise**.

Support summary:

* API the harness speaks to Fireworks: OpenAI Chat Completions
* Nexus Auto: Supported
* Native web search: Not added by Nexus. See [Web search](/nexus/auto#web-search).

Nexus CLI adds a **Fireworks** provider to GitHub Copilot Chat's custom endpoints.

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

**2. Quit VS Code**

**Quit VS Code before you connect or run `off`.** A running VS Code overwrites the change from memory. If it's open, Nexus CLI waits until you quit.

`--force` writes anyway, which isn't recommended.

**3. Connect VS Code**

```bash wrap theme={null}
nexus vscode
```

Nexus Auto is the default model. To pick another one, run `nexus vscode --model <id>`, such as `--model glm-latest`.

`nexus vscode status` shows the provider, where the key comes from, and the configured model.

**4. Restart and pick a model**

Restart VS Code, then pick a model under **Other Models → Fireworks** in Copilot Chat.

![VS Code Chat model picker showing the Fireworks provider with Auto selected and DeepSeek, GLM, and Kimi models](https://mintcdn.com/fireworksai/qp-9FYlGs5qTS-0n/images/nexus/vscode-chat-model-picker.png?fit=max\&auto=format\&n=qp-9FYlGs5qTS-0n\&q=85\&s=6a7d65116a2dc1e0d534856c6c394a7c)

VS Code Chat after Nexus CLI, with Auto selected under Fireworks (Enterprise account)

To restore your original settings, quit VS Code and run `nexus vscode off`.

## Use Nexus Auto

* **Anthropic and OpenAI model turns** need a [Provider Key](/nexus/provider-keys) from your admin.
* `glm-latest` and `glm-fast-latest` are text-only, and `glm-flash-latest` supports images.

- Instead of a Provider Key, a developer can save their own key with `nexus auto --anthropic-api-key` or `--openai-api-key` (each prompts for the key) and run `nexus vscode` again. Nexus CLI adds the saved key to the `auto` model's `requestHeaders` only. A Provider Key needs nothing saved locally.
- Nexus CLI never sends `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` from your environment.
- Nexus Auto (`auto`) is supported on the Chat Completions API.
- Manual setup sends `x-anthropic-api-key` and `x-openai-api-key` headers itself. See [Manual setup (advanced)](#manual-setup-advanced).

## MCP and tools

* Nexus CLI doesn't change your MCP servers.
* Nexus CLI doesn't add [web search](/nexus/auto#web-search) to VS Code.

## Troubleshooting

* **401 errors after you rotate your key:** quit VS Code, then run `nexus login`. It saves the new key into every connected harness that keeps its own copy, including VS Code.

Fixes for issues that affect every harness are in [Nexus Auto troubleshooting](/nexus/auto#troubleshooting).

## Manual setup (advanced)

In Copilot Chat, open **Language Models**, click **+ Add Models...**, and choose **Custom Endpoint**. Use `https://api.fireworks.ai/inference/v1`, your Fireworks key, and a model ID such as `glm-latest`.

Step-by-step screenshots are in [GitHub Copilot](/ecosystem/integrations/github-copilot). Without the Nexus CLI, you take over [the tasks it otherwise performs](/nexus/manual-setup#what-changes-without-the-nexus-cli), such as undo and updates.

## What the Nexus CLI writes

Files: `chatLanguageModels.json` and `state.vscdb`.

```json chatLanguageModels.json theme={null}
[
  {
    "name": "Fireworks",
    "vendor": "customendpoint",
    "apiType": "chat-completions",
    "apiKey": "${input:chat.lm.secret.fw-...}",
    "models": [
      {
        "id": "auto",
        "name": "Auto",
        "url": "https://api.fireworks.ai/inference",
        "maxInputTokens": 1048575,
        "maxOutputTokens": 131072,
        "vision": true,
        "toolCalling": true,
        "requestHeaders": { "x-anthropic-api-key": "sk-ant-..." }
      }
    ]
  }
]
```

* The `x-anthropic-api-key` and `x-openai-api-key` headers appear only on the `auto` row, and only for keys you saved with `nexus auto`. Nexus CLI also adds its own attribution headers to every row.
* The key is not in `chatLanguageModels.json`. It is stored in `state.vscdb` under a `chat.lm.secret.fw-*` ID, encrypted with Electron `safeStorage`. On Linux, encryption needs `libsecret`. Without it, VS Code only obfuscates the key and Nexus CLI warns you.
* If only VS Code Insiders is installed, Nexus CLI uses its `Code - Insiders` folder instead.
* `off` restores `chatLanguageModels.json` byte-for-byte and deletes the secret. Providers you set up yourself are untouched.
* Use `--vscode-path` for a non-default `chatLanguageModels.json`. Nexus CLI then uses the `state.vscdb` next to it.

| Platform | `chatLanguageModels.json` | `state.vscdb` |
| - | - | - |
| Linux | `~/.config/Code/User/` | `~/.config/Code/User/globalStorage/` |
| macOS | `~/Library/Application Support/Code/User/` | `~/Library/Application Support/Code/User/globalStorage/` |
| Windows | `%APPDATA%\Code\User\` | `%APPDATA%\Code\User\globalStorage\` |
