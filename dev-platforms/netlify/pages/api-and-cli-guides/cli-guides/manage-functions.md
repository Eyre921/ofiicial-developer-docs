---
title: "Netlify CLI: Manage Functions"
source: https://docs.netlify.com/api-and-cli-guides/cli-guides/manage-functions.md
path: api-and-cli-guides/cli-guides/manage-functions
---

---
title: "Manage functions with Netlify CLI"
description: "With the CLI, you can create, run, and test your serverless functions locally."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

The Netlify CLI offers the ability to create, serve, and test Netlify Functions locally. Once you create a serverless function, you have the option to invoke the function in a local development environment using Netlify Dev, or to invoke the functions with a local standalone server.

To learn about all of the options available, review the [command reference for functions](https://cli.netlify.com/commands/functions).

## Create serverless functions with Netlify Dev

Netlify can create serverless functions for you locally as part of Netlify Functions with the `functions:create` command:

```bash
netlify functions:create
```

Follow the CLI prompts to select from a number of function templates that are available to get you started. You can also add your own utility functions to suit your project development needs.

```bash
# Create a new function from one of the available templates offered
# when prompted
$ netlify functions:create

# Create a new function with a given name using either of the
# following options
$ netlify functions:create hello-world
$ netlify functions:create --name hello-world

# Create a new function by cloning a template from a remote url
# organised with dependencies installed into a subdirectory
$ netlify functions:create hello-world --url https://my-remote-template-URL
```

### Note

Git ignore the <code>node_modules</code> folder</span>">
If your functions have `node_modules` in each function folder, make sure to add them to your `.gitignore` file. Don't forget to add bash scripts to install the dependencies for production.

#### Deploy unbundled function folders

When a function has `node_modules` in its own folder, these packages need to be installed during deployment. The Netlify build system does not recursively install dependencies for your function folders but you can write `prebuild` or `postinstall` bash scripts to install them for production.

## Invoke functions while running Netlify Dev

Use `netlify dev` to start a local development environment and Netlify Dev will run the functions as they would run in the Netlify production environment.

To get started, configure the [functions directory in your `netlify.toml`](/build/configure-builds/file-based-configuration#sample-netlify-toml-file) and then run `netlify dev`.

The functions will be accessible at `http://localhost:8888/.netlify/functions/function-name` in the browser. Accessing the function through the browser simulates a `GET` request but you can also use `netlify functions:invoke` to test other requests. For example, the CLI also models POST requests.

You can use `netlify functions: list` to get a list of all detected functions.

If you run functions in your local environment with Netlify Dev, you can then test sending payloads of data or authentication payloads:

```bash
netlify functions:invoke # we will prompt you at each step
netlify functions:invoke myfunction # invoke a specific function
netlify functions:invoke --name myfunction # invoke a specific function

# sending payloads
netlify functions:invoke myfunction --payload '{"count": 1}'
netlify functions:invoke myfunction --querystring "count=1"
netlify functions:invoke myfunction --payload "./pathTo.json"
```

There are special cases for [event-triggered functions](/build/functions/trigger-on-events) that will also provide mock data for testing. This makes it possible to manually test event-triggered functions locally and improves the development experience.

## Serve functions with a standalone server locally

While Netlify Dev will simulate the Netlify production environment, it can be useful to simulate Netlify Functions in a standalone server instead. If you serve functions with a standalone server, you can debug functions without the overhead of starting a framework server.

To start a functions server locally, run `netlify functions:serve`. Your function will be available at `http://localhost:9999/.netlify/functions/<function-name>`

If you configure a functions directory, the server will serve functions from that directory. If not, the server will serve functions from `netlify/functions`. The default port for the functions server is `9999`.

To override these settings, use the `--functions` and `--port` flags:

```sh
netlify functions:serve --functions <path-to-dir> --port <port>
```

You can also configure the settings in a `netlify.toml`, under the `dev` block:

```toml
[dev]
  functions = "netlify-functions"
  functionsPort = 7000
```

## Debug functions locally

Netlify CLI uses [Lambda-local](https://github.com/ashiina/lambda-local) to simulate serverless functions. Since the CLI invokes functions in the same process as the functions server, you can debug functions by inspecting the functions server process.

To debug, set the `--inspect` Node.js option when starting the functions server:

- On Windows, run `cmd /V /C "set NODE_OPTIONS=--inspect && netlify functions:serve"`
- On Mac/Linux, run `NODE_OPTIONS=--inspect netlify functions:serve`

Then, attach any Node.js debugger to the CLI process to debug your functions. To learn how to debug with Visual Studio Code while running the Netlify CLI, review [Debug with VS Code](/api-and-cli-guides/cli-guides/debug-with-vscode).
