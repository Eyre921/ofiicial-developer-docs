---
title: "Custom build extensions"
source: https://trigger.dev/docs/config/extensions/custom
path: docs/config/extensions/custom
---

Customize how your project is built and deployed to Trigger.dev with your own custom build extensions

Build extensions allow you to hook into the build system and customize the build process or the resulting bundle and container image (in the case of deploying). See our [build extension overview](/docs/config/extensions/overview) for more information on how to install and use our built-in extensions. Build extensions can do the following:

* Add additional files to the build
* Add dependencies to the list of externals
* Add esbuild plugins
* Add additional npm dependencies
* Add additional system packages to the image build container
* Add commands to run in the image build container
* Add environment variables to the image build container
* Sync environment variables to your Trigger.dev project

## Creating a build extension

Build extensions are added to your `trigger.config.ts` file, with a required `name` and optional build hook functions. Here's a simple example of a build extension that just logs a message when the build starts:

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

You can also extract that out into a function instead of defining it inline, in which case you will need to import the `BuildExtension` type from the `@trigger.dev/build` package:

<Note>
  You'll need to add the `@trigger.dev/build` package to your `devDependencies` before the below
  code will work. Make sure it's version matches that of the installed `@trigger.dev/sdk` package.
</Note>

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { BuildExtension } from "@trigger.dev/build";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [myExtension()],
  },
});

function myExtension(): BuildExtension {
  return {
    name: "my-extension",
    onBuildStart: async (context) => {
      console.log("Build starting!");
    },
  };
}
```

## Build hooks

### externalsForTarget

This allows the extension to add additional dependencies to the list of externals for the build. This is useful for dependencies that are not included in the bundle, but are expected to be available at runtime.

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [
      {
        name: "my-extension",
        externalsForTarget: async (target) => {
          return ["my-dependency"];
        },
      },
    ],
  },
});
```

### onBuildStart

This hook runs before the build starts. It receives the `BuildContext` object as an argument.

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

If you want to add an esbuild plugin, you must do so in the `onBuildStart` hook. Here's an example of adding a custom esbuild plugin:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [
      {
        name: "my-extension",
        onBuildStart: async (context) => {
          context.registerPlugin({
            name: "my-plugin",
            setup(build) {
              build.onLoad({ filter: /.*/, namespace: "file" }, async (args) => {
                return {
                  contents: "console.log('Hello, world!')",
                  loader: "js",
                };
              });
            },
          });
        },
      },
    ],
  },
});
```

You can use the `BuildContext.target` property to determine if the build is for `dev` or `deploy`:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [
      {
        name: "my-extension",
        onBuildStart: async (context) => {
          if (context.target === "dev") {
            console.log("Building for dev");
          } else {
            console.log("Building for deploy");
          }
        },
      },
    ],
  },
});
```

### onBuildComplete

This hook runs after the build completes. It receives the `BuildContext` object and a `BuildManifest` object as arguments. This is where you can add in one or more `BuildLayer`'s to the context.

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "my-project",
  build: {
    extensions: [
      {
        name: "my-extension",
        onBuildComplete: async (context, manifest) => {
          context.addLayer({
            id: "more-dependencies",
            dependencies,
          });
        },
      },
    ],
  },
});
```

See the [addLayer](#addlayer) documentation for more information on how to use `addLayer`.

## BuildTarget

Can either be `dev` or `deploy`, matching the CLI command name that is being run.

```sh theme={"theme":"css-variables"}
npx trigger.dev@latest dev # BuildTarget is "dev"
npx trigger.dev@latest deploy # BuildTarget is "deploy"
```

## BuildContext

### addLayer()

<ParamField type="BuildLayer">
  The layer to add to the build context. See the [BuildLayer](#buildlayer) documentation for more
  information.
</ParamField>

### registerPlugin()

<ParamField type="esbuild.Plugin">
  The esbuild plugin to register.
</ParamField>

<ParamField type="object">
  <Expandable title="properties">
    <ResponseField name="target" type="BuildTarget">
      An optional target to register the plugin for. If not provided, the plugin will be registered
      for all targets.
    </ResponseField>

    <ResponseField name="placement" type="first | last">
      An optional placement for the plugin. If not provided, the plugin will be registered in place.
      This allows you to control the order of plugins.
    </ResponseField>
  </Expandable>
</ParamField>

### resolvePath()

Resolves a path relative to the project's working directory.

<ParamField type="string">
  The path to resolve.
</ParamField>

```ts theme={"theme":"css-variables"}
const resolvedPath = context.resolvePath("my-other-dependency");
```

### properties

<ParamField type="BuildTarget">
  The target of the build, either `dev` or `deploy`.
</ParamField>

<ParamField type="ResolvedConfig">
  <Expandable title="properties">
    <ResponseField name="runtime" type="string">
      The runtime of the project (either node or bun)
    </ResponseField>

    <ResponseField name="project" type="string">
      The project ref
    </ResponseField>

    <ResponseField name="dirs" type="string[]">
      The trigger directories to search for tasks
    </ResponseField>

    <ResponseField name="build" type="object">
      The build configuration object
    </ResponseField>

    <ResponseField name="workingDir" type="string">
      The working directory of the project
    </ResponseField>

    <ResponseField name="workspaceDir" type="string">
      The root workspace directory of the project
    </ResponseField>

    <ResponseField name="packageJsonPath" type="string">
      The path to the package.json file
    </ResponseField>

    <ResponseField name="lockfilePath" type="string">
      The path to the lockfile (package-lock.json, yarn.lock, or pnpm-lock.yaml)
    </ResponseField>

    <ResponseField name="configFile" type="string">
      The path to the trigger.config.ts file
    </ResponseField>

    <ResponseField name="tsconfigPath" type="string">
      The path to the tsconfig.json file
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField type="BuildLogger">
  A logger object that can be used to log messages to the console.
</ParamField>

## BuildLayer

<ParamField type="string">
  A unique identifier for the layer.
</ParamField>

<ParamField type="string[]">
  An array of commands to run in the image build container.

  ```ts theme={"theme":"css-variables"}
  commands: ["echo 'Hello, world!'"];
  ```

  These commands are run after packages have been installed and the code copied into the container in the "build" stage of the Dockerfile. This means you cannot install system packages in these commands because they won't be available in the final stage. To do that, please use the `pkgs` property of the `image` object.
</ParamField>

<ParamField type="object">
  <Expandable title="properties">
    <ResponseField name="pkgs" type="string[]">
      An array of system packages to install in the image build container.
    </ResponseField>

    <ResponseField name="instructions" type="string[]">
      An array of instructions to add to the Dockerfile.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField type="object">
  <Expandable title="properties">
    <ResponseField name="env" type="Record<string, string>">
      Environment variables to add to the image build container, but only during the "build" stage
      of the Dockerfile. This is where you'd put environment variables that are needed when running
      any of the commands in the `commands` array.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField type="object">
  <Expandable title="properties">
    <ResponseField name="env" type="Record<string, string>">
      Environment variables that should sync to the Trigger.dev project, which will then be avalable
      in your tasks at runtime. Importantly, these are NOT added to the image build container, but
      are instead added to the Trigger.dev project and stored securely.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField type="Record<string, string>">
  An object of dependencies to add to the build. The key is the package name and the value is the
  version.

  ```ts theme={"theme":"css-variables"}
  dependencies: {
    "my-dependency": "^1.0.0",
  };
  ```
</ParamField>

### examples

Add a command that will echo the value of an environment variable:

```ts theme={"theme":"css-variables"}
context.addLayer({
  id: "my-layer",
  commands: [`echo $MY_ENV_VAR`],
  build: {
    env: {
      MY_ENV_VAR: "Hello, world!",
    },
  },
});
```

## Troubleshooting

When creating a build extension, you may run into issues with the build process. One thing that can help is turning on `debug` logging when running either `dev` or `deploy`:

```sh theme={"theme":"css-variables"}
npx trigger.dev@latest dev --log-level debug
npx trigger.dev@latest deploy --log-level debug
```

Another helpful tool is the `--dry-run` flag on the `deploy` command, which will bundle your project and generate the Containerfile (e.g. the Dockerfile) without actually deploying it. This can help you see what the final image will look like and debug any issues with the build process.

```sh theme={"theme":"css-variables"}
npx trigger.dev@latest deploy --dry-run
```

You should also take a look at our built in extensions for inspiration on how to create your own. You can find them in in [the source code here](https://github.com/triggerdotdev/trigger.dev/tree/main/packages/build/src/extensions).
