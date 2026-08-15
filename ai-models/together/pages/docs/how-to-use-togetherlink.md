---
title: "Configure Claude Code, Codex, and ChatGPT with Together AI models"
source: https://docs.together.ai/docs/how-to-use-togetherlink
path: docs/how-to-use-togetherlink
---

Use TogetherLink to run Claude Code, Codex CLI, ChatGPT Desktop, Pi Code, and OpenCode with models hosted by Together AI.

TogetherLink is an open-source tool that lets you run your existing local coding tools against models hosted by Together AI. Instead of configuring each tool's provider settings by hand, you launch it through TogetherLink and it wires everything up for you.

## Requirements

* A [Together AI API key](https://api.together.ai/settings/projects/~current/api-keys).
* The coding tool you want to use, already installed on your machine. TogetherLink does not install the underlying tool for you.

## Get started

Install TogetherLink with the one-line installer. The installer will also install [Bun](https://bun.sh) if it is not already present:

```bash theme={null}
curl -fsSL https://togetherlink.vercel.app/install.sh | sh
```

Launch the interactive selector to pick a tool:

```bash theme={null}
togetherlink
```

If no Together AI API key is already configured or available through your environment, the interactive launcher automatically opens the API-key configuration flow so you can provide one.

Or run a tool directly. `tclaude`, `tcodex`, `tpi`, and `topencode` are installed as standalone shortcuts:

| Command                 | Shortcut    | Notes                                                                            |
| ----------------------- | ----------- | -------------------------------------------------------------------------------- |
| `togetherlink claude`   | `tclaude`   | Claude Code                                                                      |
| `togetherlink codex`    | `tcodex`    | Codex                                                                            |
| `togetherlink pi`       | `tpi`       | Pi Code                                                                          |
| `togetherlink opencode` | `topencode` | OpenCode                                                                         |
| `togetherlink chatgpt`  | None        | ChatGPT Desktop (alpha). `togetherlink codex-app` is a backward-compatible alias |

`togetherlink chatgpt` is only available as a `togetherlink` subcommand. There is no standalone shortcut.

## Configure your API key

Run the built-in configuration command to store your Together AI API key:

```bash theme={null}
togetherlink configure
```

`togetherlink configure` also optionally asks for an [Exa](https://exa.ai) API key, which enables web search inside Claude Code.

<Tip>
  You can also skip `configure` by exporting `TOGETHER_API_KEY` in your shell environment. TogetherLink will pick it up automatically.
</Tip>

## How it works

TogetherLink launches the selected coding tool configured to use compatible models hosted by Together AI. How that configuration is applied depends on the tool:

* **Claude Code and Codex** route through a shared local translation proxy daemon managed by TogetherLink. Their normal configuration files remain unchanged.
* **OpenCode and Pi Code** receive temporary per-run configuration. Their normal configuration files remain unchanged. Pi Code may write temporary files during a run.
* **ChatGPT Desktop (alpha)** is different: `togetherlink chatgpt` persistently modifies ChatGPT Desktop's configuration so it points at Together AI, and those changes remain in place until you revert them.

To restore ChatGPT Desktop's original configuration, run:

```bash theme={null}
togetherlink chatgpt --restore
```

The installed TogetherLink CLI periodically checks for updates. When an update is installed, the next invocation uses the new version.

## Learn more

* [TogetherLink](https://togetherlink.vercel.app)
* [TogetherLink on GitHub](https://github.com/Nutlope/togetherlink)
* [Together AI models](https://www.together.ai/models)
