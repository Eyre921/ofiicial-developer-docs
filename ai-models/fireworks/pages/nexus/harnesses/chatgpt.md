---
title: "ChatGPT desktop app"
source: https://docs.fireworks.ai/nexus/harnesses/chatgpt
path: nexus/harnesses/chatgpt
---

Connect the ChatGPT desktop app to Fireworks with the Nexus CLI so Nexus Auto appears next to your ChatGPT models.

The app keeps your ChatGPT sign-in for OpenAI model turns. ChatGPT in a browser at chatgpt.com isn't supported.

The app and the [Codex CLI](/nexus/harnesses/codex) share `~/.codex/config.toml`, so connecting one connects the other.

Support summary:

* API the harness speaks to Fireworks: OpenAI Responses
* Nexus Auto: Supported
* Native web search: Supported. Fireworks runs the harness's native web search server-side, with any Fireworks model. See [Web search](/nexus/auto#web-search).

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

**2. Connect the ChatGPT desktop app**

Quit the ChatGPT desktop app and close open Codex sessions, then run:

```bash wrap theme={null}
nexus chatgpt
```

* Quit them before `off` too. The app loads its model list only at startup. Nexus CLI waits for both to close. `--force` writes anyway, which isn't recommended.
* `nexus chatgpt` is the same command as `nexus codex`.
* `nexus chatgpt status` shows the current connection.

**3. Reopen the app and pick Auto**

Reopen the app. Nexus Auto appears along with your ChatGPT models.

![ChatGPT desktop model picker showing GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna, then Auto selected](https://mintcdn.com/fireworksai/zB7PRUO6m5X1UU4P/images/nexus/chatgpt-model-picker.png?fit=max\&auto=format\&n=zB7PRUO6m5X1UU4P\&q=85\&s=0efa047327f69172969a2f5e3b81dc99)

ChatGPT desktop after Nexus CLI, with Auto selected

Nexus Auto's model ID is `auto`. Enterprise accounts also get general access to open models on Fireworks serverless.

To restore your original settings, run `nexus chatgpt off`.

## Use Nexus Auto

* **Fireworks model turns** use your Fireworks key.
* **OpenAI model turns** use your ChatGPT sign-in, and [the same billing rules as Codex](/nexus/harnesses/codex#who-pays-for-openai-model-turns) apply.

## MCP and tools

* MCP servers, plugins, and ChatGPT connectors are unchanged.
* Native web search is supported. Fireworks runs the search server-side, so no search MCP server is required.

- MCP servers and plugins load through Codex's tool search. ChatGPT connectors keep working because the app keeps your ChatGPT sign-in.
- Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results. No search service is needed.

## Troubleshooting

* **`The 'auto' model is not supported when using Codex with a ChatGPT account`:** the thread started on an OpenAI model before you connected, and threads keep the provider they started on. Start a new thread to use Nexus Auto and Fireworks models.

- The error names whichever Fireworks model you picked, so it can say a Fireworks model ID instead of `'auto'`. It appears even after you pick Nexus Auto or a Fireworks model in the old thread.
- To keep working in the old thread, switch back to an OpenAI model, or run `nexus chatgpt off` and turn it back on when you start a new thread.
- After `off`, threads started on Fireworks models don't open until you run `nexus chatgpt` again.
- Upgrading from an earlier version: see [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

## Manual setup (advanced)

Quit the app, follow the [Codex manual setup](/nexus/harnesses/codex#manual-setup-advanced), then reopen the app and pick the model you set.

## What the Nexus CLI writes

Nexus CLI writes the same `config.toml` and model catalog as for Codex. See [What the Nexus CLI writes](/nexus/harnesses/codex#what-the-nexus-cli-writes).
