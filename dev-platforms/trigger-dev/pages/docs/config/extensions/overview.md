---
title: "Build extensions"
source: https://trigger.dev/docs/config/extensions/overview
path: docs/config/extensions/overview
---

Customize how your project is built and deployed to Trigger.dev with build extensions

Build extensions allow you to hook into the build system and customize the build process or the resulting bundle and container image (in the case of deploying).

You can use pre-built extensions by installing the `@trigger.dev/build` package into your `devDependencies`, or you can create your own.

Build extensions are added to your `trigger.config.ts` file under the `build.extensions` property:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [
      {
        name: "my-extension",
        onBuildStart: async (context) => {
          console.log("Build starting!");
        },
      },
    ],
  },
});
```

If you are using a pre-built extension, you can import it from the `@trigger.dev/build` package:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { ffmpeg } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [ffmpeg()],
  },
});
```

## Built-in extensions

Trigger.dev provides a set of built-in extensions that you can use to customize how your project is built and deployed. These extensions are available out of the box and can be configured in your `trigger.config.ts` file.

| Extension                                                                 | Description                                                                    |
| :------------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| [prismaExtension](/docs/config/extensions/prismaExtension)                     | Using prisma in your Trigger.dev tasks                                         |
| [pythonExtension](/docs/config/extensions/pythonExtension)                     | Execute Python scripts in your project                                         |
| [puppeteer](/docs/config/extensions/puppeteer)                                 | Use Puppeteer in your Trigger.dev tasks                                        |
| [ffmpeg](/docs/config/extensions/ffmpeg)                                       | Use FFmpeg in your Trigger.dev tasks                                           |
| [aptGet](/docs/config/extensions/aptGet)                                       | Install system packages in your build image                                    |
| [additionalFiles](/docs/config/extensions/additionalFiles)                     | Copy additional files to your build image                                      |
| [additionalPackages](/docs/config/extensions/additionalPackages)               | Install additional npm packages in your build image                            |
| [syncEnvVars](/docs/config/extensions/syncEnvVars)                             | Automatically sync environment variables from external services to Trigger.dev |
| [syncVercelEnvVars](/docs/config/extensions/syncEnvVars#syncVercelEnvVars)     | Automatically sync environment variables from Vercel to Trigger.dev            |
| [syncSupabaseEnvVars](/docs/config/extensions/syncEnvVars#syncSupabaseEnvVars) | Automatically sync environment variables from Supabase to Trigger.dev          |
| [esbuildPlugin](/docs/config/extensions/esbuildPlugin)                         | Add existing or custom esbuild extensions to customize your build process      |
| [emitDecoratorMetadata](/docs/config/extensions/emitDecoratorMetadata)         | Enable `emitDecoratorMetadata` in your TypeScript build                        |
| [audioWaveform](/docs/config/extensions/audioWaveform)                         | Add Audio Waveform to your build image                                         |

## Custom extensions

If one of the built-in extensions doesn't meet your needs, you can create your own custom extension. See our [guide on creating custom build extensions](/docs/config/extensions/custom) for more information.
