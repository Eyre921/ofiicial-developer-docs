---
title: "ChatGPT desktop app"
source: https://docs.fireworks.ai/nexus/harnesses/chatgpt
path: nexus/harnesses/chatgpt
---

Connect the ChatGPT desktop app to Fireworks with the Nexus CLI so open models and Nexus Auto appear next to your OpenAI models.

The ChatGPT desktop app and the [Codex CLI](/nexus/harnesses/codex) both read `~/.codex/config.toml`, so connecting one connects the other. **Quit the ChatGPT desktop app and close open Codex sessions before connecting or running `off`.** The app loads its model list only at startup. Nexus CLI waits for both to close, or use `--force` to write anyway.

Generally availableOpenAI ResponsesNexus AutoNative web searchmacOS only

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

**2. Connect the ChatGPT desktop app**

```bash wrap theme={null}
nexus chatgpt
nexus chatgpt status
```

`nexus chatgpt` is the same command as `nexus codex`.

**3. Reopen the app**

Reopen the app. Its model list starts on Nexus Auto (`auto`) and adds the Fireworks models next to the OpenAI models.

> [!TIP]
>
> The model list starts on Nexus Auto (`auto`) and shows the Fireworks models.

## Use Nexus Auto

The app keeps its own ChatGPT sign-in, which pays for OpenAI model turns. Your Fireworks key pays for Fireworks models. See [Who pays for OpenAI model turns](/nexus/harnesses/codex#who-pays-for-openai-model-turns).

## MCP and tools

**MCP servers and plugins** keep working, through Codex's tool search.

Native web search is supported while connected through Nexus CLI. Fireworks runs the search server-side and returns the results, with no MCP server or search service to set up.

## Troubleshooting

Upgrading from an earlier version? See [Upgrading from earlier versions](/nexus/cli#upgrading-from-earlier-versions).

> [!NOTE]
>
> **Threads keep the provider they started on.** A thread started on an
> OpenAI model before you connected stays on OpenAI, even after you pick
> Nexus Auto or a Fireworks model. ChatGPT then shows an error such as
> `The 'auto' model is not supported when using Codex with a ChatGPT account.`
> The error names whichever Fireworks model you picked.
>
> * Start a new thread to use Nexus Auto and Fireworks models.
> * To keep working in the old thread, switch back to an OpenAI model, or run
>   `nexus chatgpt off` and turn it back on when you start a new thread.
> * After `off`, threads started on Fireworks models don't open until you run `nexus chatgpt` again.

> [!NOTE]
>
> Sign-in billing is tested in the Codex CLI. The ChatGPT desktop app is not
> tested yet.

## Manual setup (advanced)

Quit the app, follow the [Codex manual setup](/nexus/harnesses/codex#manual-setup-advanced), then reopen the app and pick the model you set.

## What the Nexus CLI writes

Nexus CLI writes the same `config.toml` and model catalog as for Codex; see [What the Nexus CLI writes](/nexus/harnesses/codex#what-the-nexus-cli-writes).
