---
title: "Release Notes"
source: https://docs.fireworks.ai/nexus/release-notes
path: nexus/release-notes
---

What's new in each Nexus CLI release: new harnesses and commands, fixes, and what was deprecated or removed.

What changed in each Nexus CLI release, newest first. To update, run:

```bash wrap theme={null}
nexus update
```

Restart your harnesses afterward so they load the new settings. Run `nexus --version` to see which version you have. For every deprecated or removed command in one table, see [Deprecated and removed](/nexus/cli-reference#deprecated-and-removed).

> [!NOTE]
>
> Versions before 0.10.0 shipped as FireConnect, with the `fireconnect` command, and Nexus Auto was called FireRouter. Their notes use today's command names. See [Upgrading from FireConnect](/nexus/cli#upgrading-from-fireconnect).

**0.10.1**

October 22, 2026

**New**

* **Bring your own Anthropic and OpenAI keys to Nexus Auto.** Run `nexus auto --anthropic-api-key` or `nexus auto --openai-api-key`. Each prompts for the key, so it stays out of your shell history. Then run your harness command again. See [Nexus Auto](/nexus/auto#nexus-cli).
* **Every key in one place.** `nexus auto` shows the keys saved on this machine next to the [Provider Keys](/nexus/provider-keys) on your Fireworks account. Provider Keys work in every harness, and a key saved on your machine wins for its provider.
* **`nexus status` lists installed harnesses**, not just connected ones.
* **`nexus update` updates Nexus CLI.** `nexus upgrade` still works.

**Improved**

* Connecting a harness that isn't installed now stops with an explanation and writes nothing. Pass `--skip-install-check` if the tool lives somewhere Nexus CLI doesn't look.
* Claude Code: the Artifact tool shows up, a Claude Code older than 2.1.242 gets a warning instead of an empty `/model` picker, and the status line names the model that served the latest turn. Run `nexus claude` again to refresh the picker.
* Fewer keychain prompts. Nexus CLI reads your keychain only when a command needs your key.
* Sign-in no longer tells account members that they aren't members.
* `nexus logout` also clears the Anthropic and OpenAI keys saved on this machine.
* Safer updates: if `~/.nexus` wasn't created by Nexus CLI, `nexus update` stops before changing anything.
* The installer now requires Node.js 22 or later.

**Deprecated and removed**

* Removed `nexus claude live`. The Claude Code status line shows the model and spend on every turn, and `nexus claude usage` gives the full breakdown.
* Removed `--anthropic-api-key` and `--openai-api-key` from harness commands such as `nexus opencode`. Save keys with `nexus auto` instead.
* Deprecated `nexus harnesses`. Use `nexus status`.
* Deprecated `--anthropic-api-key`, `--openai-api-key`, and `--unset` on `nexus configure`. Use the same flags on `nexus auto`.

**0.10.0**

October 20, 2026

**New**

* **FireConnect is now Nexus CLI.** The command is `nexus`, and your data moves from `~/.fireconnect` to `~/.nexus`. The old path stays as a link. Your harnesses, key, and settings carry over. Try `nexus status`.
* **FireRouter is now Nexus Auto.** Use `auto` everywhere. The update moves every harness on a FireRouter route to `auto`.
* **Keep Nexus Auto on Fireworks models** with `nexus auto --providers fireworks`. The setting is global, and `nexus auto --reset` restores the default. See [Nexus Auto](/nexus/auto#which-models-auto-can-use).
* **Claude Desktop runs on Linux** as well as macOS. See [Claude Desktop](/nexus/harnesses/claude-desktop).

**Deprecated and removed**

* Removed FireRouter models (`firerouter`, `firerouter/...`) and the `auto-instant` mix. Picking one fails and points you to `auto`.
* Deprecated `FIRECONNECT_*` environment variables. They still work. Rename them to `NEXUS_*` in your scripts and shell profile.
* Deprecated `--routing-preference`. It has no effect. Set [effort](/nexus/orchestration-preferences) in your harness instead.

**0.9.9**

October 12, 2026

**New**

* **Codex starts on FireRouter (now Nexus Auto), and OpenAI turns use your own sign-in.** Run `codex login` with ChatGPT or an OpenAI key. Easy turns stay on open models, and the OpenAI models your sign-in offers sit above the Fireworks catalog in `/model`. See [Codex](/nexus/harnesses/codex).
* **MCP servers and ChatGPT app connectors work in Codex.** Their tools now reach the model.
* **Rotate your Fireworks key without breaking a harness.** `nexus login` saves the new key into every connected harness, VS Code included, even when you're already signed in.
* **OpenCode v2 lists your Fireworks models.** When `opencode.json` uses the v2 `providers` map, Nexus CLI writes Fireworks there too.

**Fixed**

* OpenCode's `/models` no longer lists models such as `glm-latest` twice.
* Claude Desktop works behind TLS-inspecting corporate proxies such as Zscaler. Run `nexus claude-desktop on` again to pick it up.
* With Node.js from fnm, the CLI could stop finding Node in new shells. Re-run the installer once to fix it.
* When the model catalog can't load, you see the gateway's actual error.

**Deprecated and removed**

* Removed `--anthropic-api-key` from `nexus claude`. Anthropic turns in Claude Code use Claude Code's own sign-in.
* Removed Codex on Microsoft Foundry, because Codex CLI 0.160 dropped the only API Foundry offers. Run `nexus configure --provider fireworks`, then `nexus codex`. OpenCode, Pi, Cursor IDE, and VS Code still support Foundry.

**0.9.8**

October 4, 2026

**New**

* **Claude Desktop runs on Fireworks.** On macOS, `nexus claude-desktop on` sends Chat, Cowork, and Code through Fireworks, starting on `auto`. `off` puts your previous setup back exactly as it was.
* **Pin Claude Code tiers.** Keep Claude as your main model and hand subagents to an open model: `nexus claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest`. Pass `native` to release a slot.
* **FireRouter (now Nexus Auto) can use OpenAI models** with your own OpenAI key. Cursor IDE, the Copilot harnesses, and DeepSeek Harness can pick it too.
* **New Anthropic and OpenAI models show real prices** as soon as models.dev lists them. Prices come from a cached snapshot, so session estimates still work offline.
* **`nexus models`** is a shortcut for `nexus model list`.

**Fixed**

* `nexus claude --model <id>` now makes the model your default and adds it to `/model`.
* Codex auto-review runs on the model you picked, instead of denying every approval.
* `--model` on a first Codex connection keeps the full catalog in the picker.
* DeepSeek Harness 0.1.7 and later go straight to Fireworks, with no DeepSeek key prompt.

Using Codex auto-review or DeepSeek Harness? Run `nexus codex` or `nexus deepseek` once after updating.

**0.9.7**

September 21, 2026

**New**

* **GitHub Copilot works with Fireworks.** `nexus copilot-app` connects the desktop app, and `nexus copilot-cli` connects the CLI. Your own models stay, and `off` removes only what Nexus CLI added.
* **Claude Code keeps its own tier models.** The Fireworks catalog joins the `/model` picker instead of replacing slots.
* **Every other harness starts on `auto`.**
* **Native web search and fetch in Claude Code**, served by Fireworks. See [Web Search](/nexus/web-search).
* **Codex web search works again.**

**Improved**

* The built-in Explore agent follows your session model again, instead of always using Opus.
* Connecting again refreshes the picker: retired models go, new ones arrive, and pricing updates.
* Codex compacts at 80% of the context window, so long sessions keep going.
* GLM 5.3 models unlock the max reasoning effort.

**Removed**

* The `fireworks-websearch` MCP server. The update removes it and leaves your own MCP servers alone.

**0.9.6**

September 3, 2026

**Fixed**

* Codex 0.153 works with Fireworks again.
* The status line and session meter name each model once, instead of listing it twice.
* Claude Fable 5.1 pricing is in estimates and `nexus model list`.
* A routed subagent slot keeps its `[1m]` tag.
* `nexus model list` lines up prices across models.
* `nexus claude demo` turns off your own MCP servers so they can't skew the race.

**0.9.5**

August 31, 2026

**New**

* **Session cost in Claude Code.** A status line shows which models ran, what they cost at Fireworks rates, and your cache savings. If you already have a status line, Nexus CLI leaves it alone. See [Usage and Cost](/nexus/metrics).
* **ChatGPT desktop app support.** `nexus chatgpt` and `nexus codex` share one config, so one command connects both. See [ChatGPT Desktop](/nexus/harnesses/chatgpt).
* **Pick a model for each Claude Code slot** in the setup wizard.
* **Faster `nexus model list`.** Results are cached for an hour, work offline, and show when they were last updated. `--refresh` pulls the latest.

**Improved**

* MCP tool search works through the Fireworks gateway again.
* `nexus claude demo` and the status line use the same prices, so their numbers match.
* The update repairs missing dependencies, so a partial install recovers.
* On Linux over SSH or WSL, keys go to an encrypted file, with timeouts on keyring and network calls.
* `nexus claude status` shows every slot, including defaults you never set.
* GLM 5.3 and GLM 5.3 Flash are in the catalog.

**0.9.4**

August 20, 2026

**Improved**

* `nexus claude demo` estimates cost more accurately.
* Connecting and disconnecting Cursor IDE is more reliable.
* `nexus uninstall` restores one harness at a time and waits for open IDEs to quit.

**0.9.3**

August 18, 2026

**New**

* **Anthropic and Fireworks models side by side in Claude Code.** Mix them freely.
* **`nexus claude demo`** races two live Claude Code sessions side by side.
* **DeepSeek Harness** replaces Deep Agents: `nexus deepseek`. See [DeepSeek Harness](/nexus/harnesses/deepseek).

**Fixed**

* `nexus status` no longer reports "All off" while models are connected.
* OpenCode shows the cost of each model.

**Deprecated**

* `nexus demo`. Use `nexus claude demo`.

**0.9.2**

August 9, 2026

**New**

* **VS Code uses the Chat Completions API** for better compatibility.
* **Cursor IDE's picker hides the built-in models** while connected.
* **A live session cost meter for Claude Code.** Today it opens with `nexus claude usage`.

**Fixed**

* Kimi K3 lists its 1M-token context window.
* On Linux, quit detection ignores VS Code's Electron helper processes.

**0.9.1**

August 1, 2026

**New**

* **Claude Code stays connected** when you reinstall or update.
* **Update in place.** When a newer version is out, interactive terminals offer to update. Answer No to snooze for a day.
* **Claude Code model choices persist** across sessions, with a guided setup.

**Improved**

* More reliable setup for Cursor IDE, OpenCode, and VS Code.
* Clearer Claude Code model defaults and catalog labels, including Kimi K3 naming and pricing.

**0.9.0**

July 26, 2026

**New**

* **`nexus model list`** shows the coding model catalog in one place, with standard and fast options across model families.
* **FireRouter (now Nexus Auto) works like any other model** through `--model`.
* **Claude Code usage reports** show session tokens and estimated Fireworks cost.

**Improved**

* Sign-in supports enterprise SSO and stores your key securely.
* Your own settings, headers, and model selections are kept when you connect and disconnect.
* More reliable Microsoft Foundry endpoints, Windows installs, and error messages.
