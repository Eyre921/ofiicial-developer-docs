---
title: "FireConnect"
source: https://docs.fireworks.ai/ecosystem/fireconnect/overview
path: ecosystem/fireconnect/overview
---

Point Claude Code, Cursor IDE, Codex, Copilot, and the rest at Fireworks with one FireConnect command

[FireConnect](https://github.com/fw-ai/fireconnect) is an open-source CLI that connects your existing coding harness to Fireworks. Install it, sign in once, then run one command for each harness you use. You do not need to host another service.

<Tip>
  Start with [Quick start](#quick-start). Then review the setup details for your app in [Coding Harnesses](/ecosystem/fireconnect/harnesses). To choose a router, see [FireRouter](/ecosystem/firerouter/overview).
</Tip>

## Quick start

**1. Install from Bash** (Node.js 18 or later):

```bash wrap theme={null}
curl -fsSL https://fireconnect.fireworks.ai/install.sh | bash
```

Alternative installer:

```bash wrap theme={null}
curl -fsSL \
  https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh \
  | bash
```

**2. Sign in** (browser flow, or paste a Fireworks key):

```bash wrap theme={null}
fireconnect login
```

**3. Connect** (example: Claude Code):

```bash wrap theme={null}
fireconnect claude
```

**4. Restart the harness, then check:**

```bash wrap theme={null}
fireconnect claude status
```

`status` shows the configured model and which Fireworks models appear in the picker.

Replace `claude` with a supported harness name from [Coding Harnesses](/ecosystem/fireconnect/harnesses). `cursor` means **Cursor IDE** only; Cursor CLI is not supported.

<Note>
  **Windows:** run the install command from Git Bash. PowerShell breaks the install script line endings.
</Note>

## In Claude Code

When you select FireRouter in Claude Code, the header shows the active profile:

<Frame>
  <img alt="Claude Code startup header showing FireRouter and Claude Enterprise" />
</Frame>

Open `/model` to choose FireRouter, an open-model router, or a Fireworks model:

<Frame>
  <img alt="Claude Code model picker with FireRouter selected and Auto, DeepSeek, GLM, Kimi, and MiniMax options" />
</Frame>

## Connect and restore

* **Connect** rewrites the harness config to call Fireworks and saves a snapshot under `~/.fireconnect/`.
* **`off`** restores file-based harnesses from that snapshot byte-for-byte. For IDE databases, it removes the settings and models FireConnect added.
* **Sign-in credentials and harness configurations are stored separately.** `fireconnect login` saves your credential through FireConnect's secret store. If a harness requires the key in its own configuration, FireConnect copies it there and restricts the file permissions. Run `fireconnect status` to see the active storage backend without revealing the key.

## Choose a model

Connecting registers coding-ready Fireworks models, including `auto`. Use `--model` only when you want to add or select an explicit model:

```bash wrap theme={null}
fireconnect claude --model glm-latest
```

See [FireRouter](/ecosystem/firerouter/overview) for router behavior. See [Coding Harnesses](/ecosystem/fireconnect/harnesses) for app-specific restart rules. See [Harness Compatibility](/nexus/harness-compatibility) for credentials and explicit model changes. See [Open Models](/nexus/open-models) for aliases, fast tiers, and pinned versions.

## Upgrade and uninstall

For upgrade and uninstall commands, see the [CLI Reference](/nexus/cli-reference).
