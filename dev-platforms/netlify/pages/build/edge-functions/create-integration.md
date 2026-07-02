---
title: "Edge Functions Integrations"
source: https://docs.netlify.com/build/edge-functions/create-integration.md
path: build/edge-functions/create-integration
---

---
title: "Create an Edge Functions integration"
description: "Framework authors can integrate a framework with Edge Functions by dynamically generating edge function files and declarations with the build process."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

It's possible for frameworks and other tools to dynamically create edge function files and declarations through integrations with the build process. For inspiration, you can explore the [framework-specific examples](/build/edge-functions/overview#use-cases) on the Edge Functions overview. The examples highlight different use cases for developing build-generated edge functions.

### Tip - Not a framework author? Create edge functions using the Netlify SDK

If you want to build a tool or integration that is unrelated to a framework, we recommend using the [Netlify SDK](https://developers.netlify.com/sdk/get-started/introduction/) instead. You can develop an extension that [injects edge functions](https://developers.netlify.com/sdk/edge-functions/overview/) during the build step for a site and take advantage of the other functionality and features that come with the Netlify SDK. Learn more about [extending Netlify](/extend/develop-and-share/overview#general-extensions).

This page will help you learn how to integrate your framework with Edge Functions by generating edge function files and declarations. If your framework's build process uses Vite, then you can use [the Netlify Edge Functions Vite plugin](https://github.com/netlify/vite-plugin-netlify-edge/) to generate a catch-all edge function file and declaration to serve all requests.

## Generate function files

To generate edge function files, a framework emits one function file per edge function under `.netlify/edge-functions`. Build-generated edge function files go in this internal directory so as to not interfere with user-created files.

The generated function must be compatible with the [Deno](https://deno.land/) runtime. This means the following:
- Imports of Node built-in modules must be prefixed with `node:`, for example `- All npm modules must be bundled in the function or changed to use URL imports. You can make a URL - The generated file should use ES Modules format.
- If your bundler supports build targets, it should target `browser` or `worker`.

## Generate declarations

The framework must generate declarations either inline in the function files or in a manifest file at `.netlify/edge-functions/manifest.json`. The manifest file is a JSON object with the same structure as the [`edge_functions` object from `netlify.toml`](/build/edge-functions/declarations#declare-edge-functions-in-netlify-toml).

### Caution - Avoid collisions between integrations

If you expect your integration to be used in conjunction with other integrations, avoid overwriting declarations from other integrations and be mindful about declaration order.

Declarations for build-generated edge functions support additional properties not available to user-created edge functions. Which additional properties are supported depends on whether the function is declared inline or in `manifest.json`.

|  Build-generated property   |Supported inline|Supported in `manifest.json`|
|-----------------------------|:--------------:|:--------------------------:|
| `generator`                 |**&check;**     |**&check;**                 |
| `name`                      |**&check;**     |**&check;**                 |
| `import_map`                |                |**&check;**                 |
| `version`                   |                |**&check;**                 |

These additional properties are for the following purposes:
- `generator` is an optional property for noting the integration that generated the edge function. Setting this for your integration helps Netlify's observability; this does not affect the user experience. We recommend using a value with a format of `@integration-name/plugin-name@1.2.3`, where the plugin version is included at the end.
- `name` is an optional property that allows you to set a display name for the function that appears in the Netlify UI.
- `import_map` is an optional property for specifying the path to an import map file. If this path is relative, it will be resolved in relation to the manifest file itself. The `manifest.json` declaration example below uses an import map found at `.netlify/edge-functions/import_map.json`, for example:
   ```json
    {
      "imports": {
        "example": "https://example.com",
        "netlify:edge": "this will be ignored, netlify: is a reserved prefix"
      }
    }
   ```
   Note that any imports prefixed with `netlify:` are reserved, and may be overridden by built-in definitions.
- `version` is a required metadata property for `manifest.json` that tracks the version of the manifest format being used. Set this to `1` as demonstrated in the `manifest.json` example below. 

Here are examples of build-generated declarations:

### Tabs Component:

<TabItem label="inline">
```ts
import type { IntegrationsConfig } from "@netlify/edge-functions";

export default async () => new Response("Hello, world!", {
		headers: {
			'cache-control': 'public, s-maxage=3600'
		}
	});

export const config: IntegrationsConfig = {
  path: "/hello",
  generator: "@cool-framework/nice-plugin@1.0.0",
  name: "greeting",
  cache: "manual",
  onError: "bypass"
};
```
</TabItem>

<TabItem label="manifest.json">
```json
{
  "functions": [
    {
      "path": "/admin",
      "function": "auth",
      "generator": "@cool-framework/nice-plugin@1.0.0",
      "name": "/admin auth handler",
      "onError": "/unavailable"
    },
    {
      "pattern": "^/dashboard(?:/([^/#\\?]+?))[/#\\?]?$",
      "function": "auth",
      "name": "/dashboard/* auth handler"
    },
    {
      "path": "/blog/*",
      "excludedPath": "/blog/img/*",
      "function": "rewriter",
      "cache": "manual",
      "onError": "bypass",
    },
    {
      "pattern": "/products/(.*)",
      "excludedPattern": "/products/things/(.*)",
      "function": "highlight"
    }
  ],
  "import_map": "./import_map.json",
  "version": 1
}
```
</TabItem>

## Contact us

If you'd like to create an Edge Functions integration for a framework or other developer tool, we encourage you to let us know by reaching out through our [technology partner program](https://www.netlify.com/partners/technology/) so we can help you.

We welcome your feedback on building integrations with this feature. Visit our [Forums](https://answers.netlify.com/categories) to join the conversation about Edge Functions.

