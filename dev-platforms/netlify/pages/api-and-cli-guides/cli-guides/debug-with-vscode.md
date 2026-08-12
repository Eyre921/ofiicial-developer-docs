---
title: "VS Code Netlify CLI Debugging"
source: https://docs.netlify.com/api-and-cli-guides/cli-guides/debug-with-vscode.md
path: api-and-cli-guides/cli-guides/debug-with-vscode
---

---
title: "Debug with VS Code and Netlify CLI"
description: "Learn how to debug projects with Netlify CLI and VS Code."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

You can use the VS Code debugger while you run your project with the Netlify CLI. This document outlines how to configure VS Code and how to launch the debugger.

## Create a configuration file

Create a `launch.json` file under a `.vscode` directory in your project with the following content.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "netlify dev",
      "type": "node",
      "request": "launch",
      "skipFiles": ["<node_internals>/**"],
      "outFiles": ["${workspaceFolder}/.netlify/functions-serve/**/*.js"],
      "program": "${workspaceFolder}/node_modules/.bin/netlify",
      "args": ["dev"],
      "console": "integratedTerminal",
      "env": { "BROWSER": "none" },
      "serverReadyAction": {
        "pattern": "Server now ready on (https?://[\\w:.-]+)",
        "uriFormat": "%s",
        "action": "debugWithChrome"
      }
    },
    {
      "name": "netlify functions:serve",
      "type": "node",
      "request": "launch",
      "skipFiles": ["<node_internals>/**"],
      "outFiles": ["${workspaceFolder}/.netlify/functions-serve/**/*.js"],
      "program": "${workspaceFolder}/node_modules/.bin/netlify",
      "args": ["functions:serve"],
      "console": "integratedTerminal"
    }
  ]
}
```

## Launch the debugger

After you create the configuration file, launch the debugger:

1. Select `Run and Debug` from the VS Code sidebar. To reduce noise, we recommend that you deactivate `Caught Exceptions`.
2. In the top menu, select the command to run - either `netlify dev` or `netlify functions:serve`
3. Run the debugger.

If you select `netlify dev`, the CLI will start a local development environment and open a browser with the site URL. If you select `netlify functions:serve`, the CLI will start a [standalone Netlify Functions server](/api-and-cli-guides/cli-guides/manage-functions#serve-functions-with-a-standalone-server-locally).

### Debug functions

Use the `--inspect` Node.js option to debug functions. Visit [managing functions](/api-and-cli-guides/cli-guides/manage-functions#debug-functions-locally) for more information.
