---
title: "Installation"
source: https://developers.notion.com/cli/get-started/installation
path: cli/get-started/installation
---

Install the Notion CLI on your machine.

## Install

> [tab] macOS and Linux
>
> ```bash theme={null}
> curl -fsSL https://ntn.dev | bash
> ```
>
> If the installer says it couldn't install the Notion CLI to `/usr/local/bin`, pick a directory you can write to with `NTN_INSTALL_DIR`:
>
> ```bash theme={null}
> curl -fsSL https://ntn.dev | NTN_INSTALL_DIR="$HOME/.local/bin" bash
> ```
>
> If that directory isn't on your `PATH`, the installer prints the line to add to your shell startup file.
>
> To inspect the installer before you run it, view the [install script](https://ntn.dev/install.sh).

> [tab] Windows
>
> The install script doesn't support Windows. In PowerShell or Command Prompt, install with WinGet:
>
> ```powershell theme={null}
> winget install Notion.ntn
> ```
>
> The WinGet package supports only Windows x64 (x86-64/AMD64). To confirm the package installed, run `winget list --exact --id Notion.ntn`.

> [tab] npm
>
> Use npm on macOS, Linux, or Windows. This requires Node.js 22+ and npm 10+.
>
> ```bash theme={null}
> npm install --global ntn
> ```

After you install, restart your terminal so `ntn` is on your `PATH`.

## Verify installation

```bash theme={null}
ntn --version
```

## Update

If you used the install script, run:

```bash theme={null}
ntn update
```

If you used WinGet, run:

```powershell theme={null}
winget upgrade Notion.ntn
```

If you used npm, run:

```bash theme={null}
npm update --global ntn
```

## Shell completions

`ntn completions <shell>` prints a completion script to stdout. It supports `bash`, `zsh`, `fish`, `powershell`, and `elvish`.

To load completions in bash, add this line to `~/.bashrc`:

```bash theme={null}
source <(ntn completions bash)
```

To load completions in zsh, add this line to `~/.zshrc` after `compinit` runs:

```zsh theme={null}
source <(ntn completions zsh)
```

For fish, PowerShell, or elvish, run `ntn completions fish`, `ntn completions powershell`, or `ntn completions elvish`. Load its output the way your shell loads other completion scripts.

## Next steps

> [card] [Authentication](/cli/get-started/authentication)
>
> Log in to your Notion workspace.

> [card] [Workers quickstart](/workers/get-started/quickstart)
>
> Create and deploy your first Notion Worker.
