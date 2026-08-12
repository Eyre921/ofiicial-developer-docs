---
title: "Netlify Dev: Local Development"
source: https://docs.netlify.com/api-and-cli-guides/cli-guides/local-development.md
path: api-and-cli-guides/cli-guides/local-development
---

---
title: "Local development with Netlify CLI"
description: "Set up and run a local development environment with the CLI (command line interface)."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

The Netlify CLI brings the functionality of your Netlify production environment directly to your local machine through the `dev` command. This CLI functionality is also referred to as Netlify Dev. 

When you use Netlify Dev, the CLI provides a proxy server that includes edge logic for custom headers and redirects, environment variables, and Netlify Functions. It [automatically detects](#project-detection) tools and frameworks like Gatsby, Hugo, Eleventy, Next.js, and more to configure a local development server that mimics the Netlify production environment.

The sections below describe how to get started with Netlify Dev, how project detection and ports work, and how to customize the configuration. 

You can also access the [command reference for `dev`](https://cli.netlify.com/commands/dev) for more information.

## Get started with Netlify Dev

Before you begin, make sure you complete the following if you haven't already:
- [Install](/api-and-cli-guides/cli-guides/get-started-with-cli#installation) the Netlify CLI.
- [Authenticate](/api-and-cli-guides/cli-guides/get-started-with-cli#authentication) with an access token.
- Link your local project to a Netlify `siteID` (also called Project ID in the Netlify UI). To do this:
  - If you're joining an existing project, use [`netlify clone <repo>`](/api-and-cli-guides/cli-guides/get-started-with-cli#clone-a-netlify-site) to clone and link in one command (recommended)
  - If you're setting up a new site, use [`netlify init`](/api-and-cli-guides/cli-guides/get-started-with-cli#continuous-deployment) to set up continuous deployment
  - If you've already cloned a repository manually, use [`netlify link`](/api-and-cli-guides/cli-guides/get-started-with-cli#link-an-existing-local-project) to connect it to a Netlify site

> **Note - Site ID same as Project ID:** Site ID, the API's `site_id`, and the `NETLIFY_SITE_ID` environment variable all hold the same value, which the Netlify UI labels **Project ID**. To find it in the Netlify UI, go to 
### NavigationPath Component:

Project configuration > General > Project information
, and copy the value for **Project ID**. Learn more about [Netlify project identifiers](/api-and-cli-guides/api-guides/get-started-with-api#get-site).

To start a local development server for the build tool you're using, run the following command from the root of your linked repository:

```bash
netlify dev
```

By default, Netlify Dev runs your project using the configuration and [environment variables](/build/environment-variables/overview) set for local development with the Netlify CLI. For environment variables, that means those with values set for `dev` or `all` deploy contexts. You can use the `--context` flag to run your project with a different deploy context's settings and variables.

```bash
netlify dev --context production
```

Note that environment variables apply to all scopes when running `netlify dev`.

To run a shell command within the Netlify Dev environment, use `exec`:

```bash
netlify dev:exec YOUR_SHELL_COMMAND
```

## Project detection

Netlify Dev attempts to detect the site generator or build command that your project uses and run these on your behalf, while adding other development utilities. If you have a JavaScript project, it uses simple heuristics to search for the best `package.json` script to run for you, so you can use the full flexibility of npm scripts.

You also have the option to override framework detection, if needed.

### Collapsible Component:

**'Override framework detection'**

The number of [frameworks that Netlify Dev can detect](https://github.com/netlify/build/tree/main/packages/build-info) is growing but, if the framework you use is not yet supported, you can instruct Netlify Dev to run the project on your behalf. Configure your project's build command, port, and publish directory with the `[dev]` block in your `netlify.toml` file.

```toml
# sample dev block in the toml
# note: each of these fields are optional and should only be used if you need an override
[dev]
  command = "yarn start" # Command to start your dev server
  targetPort = 3000 # The port for your application server, framework, or site generator
  port = 8888 # The port that the Netlify Dev will be accessible on
  publish = "dist" # If you use a _redirect file, provide the path to your static content folder
```

If the CLI detects your project incorrectly or detects multiple frameworks, you can specify a `framework` option to test only one detector against your project.

```toml
[dev]
  framework = "create-react-app" # or "#static" to force a static server
```

Possible values of `framework`:

- `#auto` (default) to check all [available frameworks](https://github.com/netlify/build/tree/main/packages/build-info).
- The ID for one of the available frameworks, as specified in [the `.json` file for that framework](https://github.com/netlify/build/tree/main/packages/build-info) in the Netlify Build repository.
- `#static` for a static file server
- `#custom` to use the `command` option to run an app server and `targetPort` option to connect to it

---

## Project ports

When you use Netlify Dev, you may encounter a few different ports - especially if your project uses a static site generator that has its own dev server, like Gatsby. Keep the following in mind when working with Netlify Dev:

- If your project uses a [framework that we can detect](https://github.com/netlify/build/tree/main/packages/build-info), Netlify Dev will use the framework's conventional ports, so you don't have to supply them yourself. If multiple detectors match your project, we'll ask you to choose.
- If your site generator runs on a specific port, such as port 8000, you need to [specify the port](#specify-custom-ports-for-netlify-dev) when you run `netlify dev`. Netlify Dev will connect to that port and route requests successfully to the site generator along with the rest of the local Netlify environment.
- If you use an unrecognized site generator or framework, or have a server you want Netlify Dev to connect to, you need to [specify the port](#specify-custom-ports-for-netlify-dev) when you run `netlify dev`.

To confirm which port to use for local development with Netlify Dev, search for this box in your console output:

```bash
   ┌────────────────────────────────────────────────────────────────────────┐
   │                                                              │
   │   [Netlify Dev] Server now ready on http://localhost:8888    │
   │                                                              │
   └────────────────────────────────────────────────────────────────────────┘
```

## Configuration

Netlify Dev works without configuration for the majority of users, but you can customize Netlify Dev settings in the `[dev]` section of the Netlify configuration file. The following sections outline some common configuration options. 

For a full list of the available properties, refer to the [Netlify Dev section of our file-based configuration](/build/configure-builds/file-based-configuration#netlify-dev) doc.

### Run an https server for local development

By default, `netlify dev` starts an HTTP server. If you require HTTPS, you can configure a certificate and key file for
use by `netlify dev` in your `netlify.toml`:

```toml
[dev]
  [dev.https]
    certFile = "cert.pem"
    keyFile = "key.pem"
```

### Caution - Self-signed certificates require extra configuration

If you're using a self-signed certificate, you might need to configure your browser to accept it when running on `localhost`. To enable this setting for Chrome, visit `chrome://flags/#allow-insecure-localhost` in your browser.

### Specify custom ports for Netlify Dev

Netlify Dev allows you to specify custom ports using the following parameters as flags or in a Netlify configuration file (`netlify.toml`):

- **`targetPort`**: the port for your application server, framework, or site generator
- **`port`**: the port for the Netlify Dev server that you will open in the browser

Netlify Dev tries to acquire these ports but if they are already in use by another application, it will throw an error and let you know.

```toml
[dev]
  targetPort = 3000
  port = 8888
```

## More Netlify Dev resources

- [Command reference for `dev`](https://cli.netlify.com/commands/dev)
- [Configuration properties for Netlify Dev in `netlify.toml`](/build/configure-builds/file-based-configuration#netlify-dev)
- [Use Netlify CLI with monorepos](/api-and-cli-guides/cli-guides/get-started-with-cli#work-with-monorepos) 
- [Manage Functions with Netlify CLI](/api-and-cli-guides/cli-guides/manage-functions)
