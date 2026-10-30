---
title: "Notion CLI"
source: https://developers.notion.com/cli/get-started/overview
path: cli/get-started/overview
---

Install the Notion CLI and learn the core commands for authentication, Notion Workers, and API requests.

`ntn` is the Notion CLI. Use it to authenticate with Notion, deploy and manage [Notion Workers](/workers/get-started/overview), and make API requests — all from your terminal.

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

Verify the installation:

```bash theme={null}
ntn --version
```

> [!TIP]
>
> See [Installation](/cli/get-started/installation) for update steps and shell completions.

## Authenticate

Log in to connect the CLI to your Notion workspace:

```bash theme={null}
ntn login
```

This opens a browser window where you authorize access. Your credentials are stored securely in your system's keychain. See [Authentication](/cli/get-started/authentication) for more details.

## What you can do

> [card] [Workers](/workers/get-started/overview)
>
> Deploy, manage, and debug Notion Workers.

> [card] [API requests](/cli/guides/api-requests)
>
> Make Notion API requests directly from the terminal.

> [card] [Data sources](/cli/guides/data-sources)
>
> Create, query, and manage data sources from the terminal.

> [card] [File uploads](/cli/guides/file-uploads)
>
> Upload static assets like images and PDFs to Notion.

### Manage Notion Workers

Create, deploy, and operate Workers — small TypeScript programs that extend Notion with syncs, tools, and webhooks:

```bash theme={null}
ntn workers new          # Scaffold a project
ntn workers deploy       # Build and upload
ntn workers list         # List deployed workers
```

See the [Workers guide](/workers/get-started/overview) to get started.

### Make API requests

Make authenticated requests to the Notion API with inline JSON construction and shell completion:

```bash theme={null}
ntn api v1/users                             # GET users
ntn api v1/pages parent[page_id]=abc123      # POST with inline body fields
ntn api v1/pages/abc123 -X PATCH archived:=true  # PATCH with typed assignment
```

See the [API requests guide](/cli/guides/api-requests) for the full inline syntax reference.

### Upload files

Upload static assets like images and PDFs to reference from Notion pages:

```bash theme={null}
ntn files create < photo.png
ntn files create --external-url https://example.com/photo.png
ntn files list
```

See the [file uploads guide](/cli/guides/file-uploads) for details.

## Next steps

> [card] [Installation](/cli/get-started/installation)
>
> Alternative install methods and shell completions.

> [card] [Authentication](/cli/get-started/authentication)
>
> Manage login sessions and credentials.

> [card] [Command reference](/cli/reference/commands)
>
> Full reference for every ntn command.

> [card] [Notion Workers quickstart](/workers/get-started/quickstart)
>
> Create and deploy your first Notion Worker.
