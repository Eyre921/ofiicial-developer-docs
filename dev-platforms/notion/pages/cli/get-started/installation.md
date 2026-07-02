---
title: "Installation"
source: https://developers.notion.com/cli/get-started/installation
path: cli/get-started/installation
---

Install the Notion CLI on your machine.

## Install via script (recommended)

The recommended way to install `ntn` on macOS and Linux:

```bash theme={null}
curl -fsSL https://ntn.dev | bash
```

To update:

```bash theme={null}
ntn update
```

## Install via npm

Use macOS, Linux, or Windows to install:

```bash theme={null}
npm install --global ntn
```

To update:

```bash theme={null}
npm update --global ntn
```

<Note>
  Requires Node.js 22+ and npm 10+.
</Note>

## Install via Winget (Windows)

In PowerShell or Command Prompt, including either shell in Windows Terminal:

```powershell theme={null}
winget install Notion.ntn
```

You can also confirm the WinGet package:

```powershell theme={null}
winget list --exact --id Notion.ntn
```

Restart your terminal to verify.

To update:

```powershell theme={null}
winget upgrade Notion.ntn
```

<Note>
  We currently only support Windows x64 (x86-64/AMD64)
</Note>

## Verify installation

```bash theme={null}
ntn --version
```

## Shell completions

Enable tab completions for your shell:

```bash theme={null}
ntn completions bash  # or fish, zsh, powershell, elvish
```

## Building from source

Clone the repository and use [mise](https://mise.jdx.dev/) to build a local debug binary installed as `ntnd`:

```bash theme={null}
git clone https://github.com/makenotion/cli.git
cd cli
mise build
```

See the [CLI README](https://github.com/makenotion/cli/blob/main/README.md#building-from-source) for `mise watch` and other development workflows.

## Next steps

<CardGroup>
  <Card title="Authentication" icon="lock" href="/cli/get-started/authentication">
    Log in to your Notion workspace.
  </Card>

  <Card title="Workers quickstart" icon="rocket" href="/workers/get-started/quickstart">
    Create and deploy your first Notion Worker.
  </Card>
</CardGroup>
