---
title: "Quickstart"
source: https://developers.notion.com/workers/get-started/quickstart
path: workers/get-started/quickstart
---

Create and deploy your first worker in minutes.

Get up and running with Workers in a few steps.

## Prerequisites

> **Node.js**
>
> Version 22 or higher

> **npm**
>
> Version 10 or higher

## Create your first worker

**1. Install the CLI**

**macOS and Linux**

```bash theme={null}
curl -fsSL https://ntn.dev | bash
```

If the installer says it couldn't install the Notion CLI to `/usr/local/bin`, pick a directory you can write to with `NTN_INSTALL_DIR`:

```bash theme={null}
curl -fsSL https://ntn.dev | NTN_INSTALL_DIR="$HOME/.local/bin" bash
```

If that directory isn't on your `PATH`, the installer prints the line to add to your shell startup file.

To inspect the installer before you run it, view the [install script](https://ntn.dev/install.sh).

**Windows**

The install script doesn't support Windows. In PowerShell or Command Prompt, install with WinGet:

```powershell theme={null}
winget install Notion.ntn
```

The WinGet package supports only Windows x64 (x86-64/AMD64). To confirm the package installed, run `winget list --exact --id Notion.ntn`.

**npm**

Use npm on macOS, Linux, or Windows. This requires Node.js 22+ and npm 10+.

```bash theme={null}
npm install --global ntn
```

After you install, restart your terminal so `ntn` is on your `PATH`.

**2. Initialize a new project**

Scaffold a new worker project and enter the directory:

```bash theme={null}
ntn workers new my-worker
cd my-worker
```

**3. Deploy to Notion**

Connect to your Notion workspace and deploy:

```bash theme={null}
ntn workers deploy
```

Follow the prompts to authenticate with your Notion workspace.

**4. Share the worker (optional)**

To let other workspace members use this worker, share it from the [Developer portal](https://www.notion.so/developers/workers). **Can connect** lets members connect the worker to agents, and **Full access** lets them manage, edit, and deploy it. See [sharing workers](/workers/guides/sharing-workers) for more details.

**5. Run the sample tool**

Execute the included sample tool:

```bash theme={null}
ntn workers exec sayHello -d '{"name": "World"}'
```

> [!NOTE]
>
> Run `exec` from the `my-worker` directory after you deploy. The CLI reads the worker ID from `workers.json` in the current directory. From anywhere else, pass `--worker-id`.

## What's in a worker?

The scaffolded project lives in `src/index.ts` and exports a single `Worker` instance:

```typescript src/index.ts theme={null}
import { Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

worker.tool("sayHello", {
  title: "Say Hello",
  description: "Returns a friendly greeting",
  schema: {
    type: "object",
    properties: {
      name: { type: "string" },
    },
    required: ["name"],
    additionalProperties: false,
  },
  execute: ({ name }) => `Hello, ${name}!`,
});
```

## Next steps

> **[Syncs](/workers/guides/syncs)**
>
> Sync external data into Notion databases.

> **[Agent tools](/workers/guides/tools)**
>
> Build custom tools for Notion AI.

> **[Webhooks](/workers/guides/webhooks)**
>
> Receive HTTP events from external services.

> **[OAuth](/workers/guides/oauth)**
>
> Connect to third-party APIs.
