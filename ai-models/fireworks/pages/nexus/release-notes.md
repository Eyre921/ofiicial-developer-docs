---
title: "Release Notes"
source: https://docs.fireworks.ai/nexus/release-notes
path: nexus/release-notes
---

What's new in each Nexus CLI release: new harnesses and commands, fixes, and what was deprecated or removed.

Nexus CLI releases are listed newest first. To update, run:

```bash wrap theme={null}
nexus update
```

Then restart your harnesses so they load the new settings.

* Run `nexus --version` to see which version you have.
* For every deprecated or removed command in one table, see [Deprecated and removed](/nexus/cli-reference#deprecated-and-removed).
* Versions before 0.10.0 shipped as FireConnect, with the `fireconnect` command, and Nexus Auto was called FireRouter. Their notes use today's command names. See [Upgrading from FireConnect](/nexus/cli#upgrading-from-fireconnect).

**0.10.1**

October 22, 2026

**New**

* **Bring your own Anthropic and OpenAI keys to Nexus Auto** with `nexus auto`.
* **`nexus auto` shows every key**, both your saved keys and your account's Provider Keys.
* **`nexus status` lists installed harnesses** as well as connected ones.
* **`nexus update` updates Nexus CLI.**

**Improved**

* Connecting a harness that isn't installed stops and writes nothing.
* Claude Code: the Artifact tool, `/model` picker, and status line work better.
* Nexus CLI prompts for keychain access less often.
* Sign-in no longer tells account members that they aren't members.
* `nexus logout` also clears the Anthropic and OpenAI keys saved on this machine.
* `nexus update` no longer modifies a `~/.nexus` directory that Nexus CLI didn't create.
* The installer now requires Node.js 22 or later.

**Deprecated and removed**

* Removed `nexus claude live`.
* Removed the Anthropic and OpenAI key flags from harness commands.
* Deprecated `nexus harnesses` in favor of `nexus status`.
* Deprecated the Anthropic and OpenAI key flags on `nexus configure`.

- Bring your own keys: run `nexus auto --anthropic-api-key` or `nexus auto --openai-api-key`. Each prompts for the key, so it stays out of your shell history. Then run your harness command again. See [Nexus Auto](/nexus/auto#nexus-cli).
- `nexus auto` shows the keys saved on this machine next to the [Provider Keys](/nexus/provider-keys) on your Fireworks account. Provider Keys work in every harness, and a key saved on your machine wins for its provider.
- `nexus upgrade` still works.
- Uninstalled harness: connect stops with an explanation. Pass `--skip-install-check` if the tool lives somewhere Nexus CLI doesn't look.
- Claude Code: the Artifact tool shows up, a Claude Code older than 2.1.242 gets a warning instead of an empty `/model` picker, and the status line names the model that served the latest turn. Run `nexus claude` again to refresh the picker.
- Keychain: Nexus CLI reads your keychain only when a command needs your key.
- Safer updates: if `~/.nexus` wasn't created by Nexus CLI, `nexus update` stops before changing anything.
- `nexus claude live` replacement: the Claude Code status line shows the model and spend on every turn, and `nexus claude usage` gives the full breakdown.
- Removed `--anthropic-api-key` and `--openai-api-key` from harness commands such as `nexus opencode`. Save keys with `nexus auto` instead.
- Deprecated `--anthropic-api-key`, `--openai-api-key`, and `--unset` on `nexus configure`. Use the same flags on `nexus auto`.

**0.10.0**

October 20, 2026

**New**

* **FireConnect is now Nexus CLI.** The command is `nexus`, and your harnesses, key, and settings carry over.
* **FireRouter is now Nexus Auto**, with the model ID `auto` in every harness.
* **Keep Nexus Auto on Fireworks models** with `nexus auto --providers fireworks`.
* **[Claude Desktop](/nexus/harnesses/claude-desktop) runs on Linux** as well as macOS.

**Deprecated and removed**

* Removed FireRouter models and the `auto-instant` mix.
* Deprecated `FIRECONNECT_*` environment variables.
* Deprecated `--routing-preference`.

- Rename: your data moves from `~/.fireconnect` to `~/.nexus`. The old path stays as a link. Try `nexus status`.
- The update moves every harness on a FireRouter route to `auto`.
- `nexus auto --providers fireworks` is global, and `nexus auto --reset` restores the default. See [Nexus Auto](/nexus/auto#which-models-auto-can-use).
- Removed models: `firerouter`, `firerouter/...`, and `auto-instant`. Picking one fails and points you to `auto`.
- `FIRECONNECT_*` variables still work. Rename them to `NEXUS_*` in your scripts and shell profile.
- `--routing-preference` has no effect. Set [effort](/nexus/orchestration-preferences) in your harness instead.

**0.9.9**

October 12, 2026

**New**

* **[Codex](/nexus/harnesses/codex) starts on FireRouter (now Nexus Auto)**, and OpenAI turns use your own sign-in.
* **MCP servers and ChatGPT app connectors work in Codex.**
* **Rotating your Fireworks key no longer breaks connected harnesses.**
* **OpenCode v2 lists your Fireworks models.**

**Fixed**

* OpenCode's `/models` no longer lists models twice.
* Claude Desktop works behind TLS-inspecting corporate proxies.
* Node.js from fnm no longer goes missing in new shells.
* When the model catalog can't load, you see the gateway's actual error.

**Deprecated and removed**

* Removed `--anthropic-api-key` from `nexus claude`.

- Codex OpenAI sign-in: run `codex login` with ChatGPT or an OpenAI key. Easy turns stay on open models, and the OpenAI models your sign-in offers sit above the Fireworks catalog in `/model`.
- Codex MCP servers and ChatGPT app connectors: their tools now reach the model.
- Key rotation: `nexus login` saves the new key into every connected harness, VS Code included, even when you're already signed in.
- OpenCode v2: when `opencode.json` uses the v2 `providers` map, Nexus CLI writes Fireworks there too.
- OpenCode duplicate models: for example `glm-latest`.
- Claude Desktop proxy fix covers proxies such as Zscaler. Run `nexus claude-desktop on` again to pick it up.
- fnm fix: the CLI could stop finding Node in new shells. Re-run the installer once to fix it.
- Anthropic turns in Claude Code use Claude Code's own sign-in.

**0.9.8**

October 4, 2026

**New**

* **Claude Desktop runs on Fireworks** with `nexus claude-desktop on`.
* **Pin Claude Code tiers** to open models, such as for subagents.
* **FireRouter (now Nexus Auto) can use OpenAI models** with your own OpenAI key.
* **New Anthropic and OpenAI models show real prices.**
* **`nexus models`** is a shortcut for `nexus model list`.

**Fixed**

* `nexus claude --model <id>` now makes the model your default.
* Codex auto-review runs on the model you picked.
* `--model` on a first Codex connection keeps the full catalog.
* DeepSeek Harness 0.1.7 and later skip the DeepSeek key prompt.

If you use Codex auto-review or DeepSeek Harness, run `nexus codex` or `nexus deepseek` once after updating.

* Claude Desktop (macOS): sends Chat, Cowork, and Code through Fireworks, starting on `auto`. `off` puts your previous setup back exactly as it was.
* Tier pinning keeps Claude as your main model and hands subagents to an open model: `nexus claude --sonnet deepseek-flash-latest --subagent deepseek-flash-latest`. Pass `native` to release a slot.
* FireRouter with OpenAI: Cursor IDE, the Copilot harnesses, and DeepSeek Harness can pick it too.
* Prices appear as soon as models.dev lists them. Prices come from a cached snapshot, so session estimates still work offline.
* `nexus claude --model <id>` also adds the model to `/model`.
* Codex auto-review previously denied every approval.
* DeepSeek Harness 0.1.7 and later go straight to Fireworks.

**0.9.7**

September 21, 2026

**New**

* **GitHub Copilot works with Fireworks.** `nexus copilot-app` connects the desktop app, and `nexus copilot-cli` connects the CLI.
* **Claude Code keeps its own tier models.**
* **Every other harness starts on `auto`.**
* **Claude Code gets native [web search](/nexus/auto#web-search) and fetch.**
* **Codex web search works again.**

**Improved**

* The built-in Explore agent follows your session model again.
* Connecting again refreshes the picker.
* Codex compacts long sessions so they can continue.
* GLM 5.3 models unlock the max reasoning effort.

**Removed**

* The `fireworks-websearch` MCP server.

- Copilot: your own models stay, and `off` removes only what Nexus CLI added.
- Claude Code tiers: the Fireworks catalog joins the `/model` picker instead of replacing slots.
- Claude Code web search and fetch are served by Fireworks.
- Explore agent previously always used Opus.
- Refreshing the picker: retired models go, new ones arrive, and pricing updates.
- Codex compacts at 80% of the context window.
- The update removes `fireworks-websearch` and leaves your own MCP servers alone.

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

* **Session cost in Claude Code.** A [status line](/nexus/metrics) shows which models ran and what they cost.
* **Support for the [ChatGPT desktop app](/nexus/harnesses/chatgpt).**
* **Pick a model for each Claude Code slot** in the setup wizard.
* **Faster `nexus model list`.**

**Improved**

* MCP tool search works through the Fireworks gateway again.
* `nexus claude demo` and the status line use the same prices.
* The update repairs missing dependencies.
* Better key storage on Linux over SSH or WSL.
* `nexus claude status` shows every slot.
* GLM 5.3 and GLM 5.3 Flash are in the catalog.

- Status line: costs at Fireworks rates plus your cache savings. If you already have a status line, Nexus CLI leaves it alone.
- ChatGPT: `nexus chatgpt` and `nexus codex` share one config, so one command connects both.
- `nexus model list`: results are cached for an hour, work offline, and show when they were last updated. `--refresh` pulls the latest.
- Demo and status line numbers now match.
- Repairing dependencies lets a partial install recover.
- Linux over SSH or WSL: keys go to an encrypted file, with timeouts on keyring and network calls.
- `nexus claude status` includes defaults you never set.

**0.9.4**

August 20, 2026

**Improved**

* `nexus claude demo` estimates cost more accurately.
* Connecting and disconnecting Cursor IDE is more reliable.
* `nexus uninstall` restores one harness at a time and waits for open IDEs to quit.

**0.9.3**

August 18, 2026

**New**

* **Claude Code can use Anthropic and Fireworks models side by side.**
* **`nexus claude demo`** races two live Claude Code sessions side by side.
* **[DeepSeek Harness](/nexus/harnesses/deepseek) replaces Deep Agents.** Connect it with `nexus deepseek`.

**Fixed**

* `nexus status` no longer reports "All off" while models are connected.
* OpenCode shows the cost of each model.

**Deprecated**

* `nexus demo`, replaced by `nexus claude demo`.

**0.9.2**

August 9, 2026

**New**

* **VS Code uses the Chat Completions API** for better compatibility.
* **Cursor IDE's picker hides the built-in models** while connected.
* **A live session cost meter for Claude Code**, now opened with `nexus claude usage`.

**Fixed**

* Kimi K3 lists its 1M-token context window.
* On Linux, quit detection ignores VS Code's Electron helper processes.

**0.9.1**

August 1, 2026

**New**

* **Claude Code stays connected** when you reinstall or update.
* **Update in place.** When a newer version is available, interactive terminals offer to update.
* **Claude Code model choices persist** across sessions, with a guided setup.

**Improved**

* More reliable setup for Cursor IDE, OpenCode, and VS Code.
* Clearer Claude Code model defaults and catalog labels.

- Update prompt: answer No to snooze for a day.
- Catalog labels include Kimi K3 naming and pricing.

**0.9.0**

July 26, 2026

**New**

* **`nexus model list`** shows the coding model catalog in one place.
* **FireRouter (now Nexus Auto) works like any other model** through `--model`.
* **Claude Code usage reports** show session tokens and estimated Fireworks cost.

**Improved**

* Sign-in supports enterprise SSO and stores your key securely.
* Your own settings, headers, and model selections are kept when you connect and disconnect.
* More reliable Windows installs and error messages.

- `nexus model list` covers standard and fast options across model families.
