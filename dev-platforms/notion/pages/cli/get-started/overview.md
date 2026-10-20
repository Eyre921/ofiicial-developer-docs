---
title: "Notion CLI"
source: https://developers.notion.com/cli/get-started/overview
path: cli/get-started/overview
---

Install the Notion CLI and learn the core commands for authentication, Notion Workers, and API requests.

`ntn` is the Notion CLI. Use it to authenticate with Notion, deploy and manage [Notion Workers](/workers/get-started/overview), and make API requests — all from your terminal.

## Install

```bash theme={null}
curl -fsSL https://ntn.dev | bash
```

Verify the installation:

```bash theme={null}
ntn --version
```

> [!TIP]
>
> See [Installation](/cli/get-started/installation) for more installation options.

## Authenticate

Log in to connect the CLI to your Notion workspace:

```bash theme={null}
ntn login
```

This opens a browser window where you authorize access. Your credentials are stored securely in your system's keychain. See [Authentication](/cli/get-started/authentication) for more details.

## What you can do

> **[Workers](/workers/get-started/overview)**
>
> Deploy, manage, and debug Notion Workers.

> **[API requests](/cli/guides/api-requests)**
>
> Make Notion API requests directly from the terminal.

> **[Data sources](/cli/guides/data-sources)**
>
> Create, query, and manage data sources from the terminal.

> **[File uploads](/cli/guides/file-uploads)**
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

> **[Installation](/cli/get-started/installation)**
>
> Alternative install methods and shell completions.

> **[Authentication](/cli/get-started/authentication)**
>
> Manage login sessions and credentials.

> **[Command reference](/cli/reference/commands)**
>
> Full reference for every ntn command.

> **[Notion Workers quickstart](/workers/get-started/quickstart)**
>
> Create and deploy your first Notion Worker.
