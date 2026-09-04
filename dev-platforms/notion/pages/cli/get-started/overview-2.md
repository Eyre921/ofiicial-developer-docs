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

<Tip>
  See [Installation](/cli/get-started/installation) for more installation options.
</Tip>

## Authenticate

Log in to connect the CLI to your Notion workspace:

```bash theme={null}
ntn login
```

This opens a browser window where you authorize access. Your credentials are stored securely in your system's keychain. See [Authentication](/cli/get-started/authentication) for more details.

## What you can do

<CardGroup>
  <Card title="Workers" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/code.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=2601b12ff19455ce6c63331bfbcc62c0" href="/workers/get-started/overview">
    Deploy, manage, and debug Notion Workers.
  </Card>

  <Card title="API requests" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/terminal.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=ed75fe4bd49b0ec0117eeead6adb4e5d" href="/cli/guides/api-requests">
    Make Notion API requests directly from the terminal.
  </Card>

  <Card title="Data sources" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/pathRoundEnds.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=f1b9491091d34c2249a03218696218a3" href="/cli/guides/data-sources">
    Create, query, and manage data sources from the terminal.
  </Card>

  <Card title="File uploads" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/arrowTrayUp.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=3b991e18c85512f06c2d7214acf94f12" href="/cli/guides/file-uploads">
    Upload static assets like images and PDFs to Notion.
  </Card>
</CardGroup>

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

<CardGroup>
  <Card title="Installation" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/arrowTrayDown.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=eb86a4f9408df146015f1c6df83dc97d" href="/cli/get-started/installation">
    Alternative install methods and shell completions.
  </Card>

  <Card title="Authentication" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/personKey.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=e2a4687ab6ed95ea30e5b9879fc17c73" href="/cli/get-started/authentication">
    Manage login sessions and credentials.
  </Card>

  <Card title="Command reference" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/clipboard.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=87e006953ac11c5af23cf0f96d8bfce5" href="/cli/reference/commands">
    Full reference for every ntn command.
  </Card>

  <Card title="Notion Workers quickstart" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/arrowChevronDoubleForward.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=e9dad4152e1d3bf11e6a8404d9504665" href="/workers/get-started/quickstart">
    Create and deploy your first Notion Worker.
  </Card>
</CardGroup>
