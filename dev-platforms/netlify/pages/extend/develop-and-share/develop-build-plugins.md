---
title: "Netlify Build Plugins"
source: https://docs.netlify.com/extend/develop-and-share/develop-build-plugins.md
path: extend/develop-and-share/develop-build-plugins
---

---
title: "Develop Build Plugins"
description: "Learn how to create your own build plugin for our platform. Hook into different events during the build-deploy lifecycle to expand your site's capabilities."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

In addition to [installing plugins](/extend/install-and-use/build-plugins#install-a-plugin) written by others, you can create your own. To learn how, check out the detailed reference information below and our [Build Plugin template](https://github.com/netlify/build-plugin-template).

### Note - Start here

A new way to build deep integrations and extensions is here.

Visit the [Netlify SDK docs](https://developers.netlify.com/sdk/) to learn about new tools and options for extending and integrating with Netlify. With the SDK, you can make an extension that interacts with more parts of the Netlify platform than a build plugin can. This new toolset also provides a streamlined experience for both developers and users.

While you can also create build plugins with TypeScript, this document currently demonstrates how to create build plugins with JavaScript.

## ES modules

If you plan to use JavaScript, we recommend building new plugins with [ES modules](https://nodejs.org/api/packages.html) (ESM) but the examples below also include CommonJS (CJS) syntax for older plugins.

To use ESM, Node.js requires `"type": "module"` in your plugin's `package.json` file.

## Plug into events

Build Plugins run JavaScript or TypeScript code in response to different events happening during the build-deploy lifecycle.

For example, the `onPreBuild` event handler runs before your build command. The `onPostBuild` event handler runs
after your site build has completed. The following event handlers are currently available:

- **`onPreBuild`:** runs before the build command is executed.
- **`onBuild`:** runs directly after the build command is executed and before Functions bundling.
- **`onPostBuild`:** runs after the build command completes; after `onBuild` tasks and Functions bundling are executed; and before the deploy stage. This is when file-based uploads for Netlify Blobs occur. Can be used to prevent a build from being deployed.
- **`onError`:** runs when an error occurs in the build or deploy stage, failing the build. Can't be used to prevent a build from being deployed.
- **`onSuccess`:** runs when the deploy succeeds. Can't be used to prevent a build from being deployed.
- **`onEnd`:** runs after completion of the deploy stage, regardless of build error or success; is useful for resources cleanup. Can't be used to prevent a build from being deployed.

There are also event handlers that are available when running [`netlify dev`](/api-and-cli-guides/cli-guides/local-development#get-started-with-netlify-dev):

- **`onPreDev`:** runs before `onDev`.
- **`onDev`:** runs directly before the dev command.

## Anatomy of a plugin

A plugin consists of two files:

- A `manifest.yml` file in the package root with the plugin's name at minimum:

  ```yml
  # manifest.yml

  name: netlify-plugin-hello-world
  ```

- A JavaScript or TypeScript object that hooks onto a build event. For example, in JavaScript:

### Tabs Component:

<TabItem label="ES modules">
  ``` js
  // index.js

  export const onPreBuild = function() {
    console.log("Hello world from onPreBuild event!");
  }
  ```
  </TabItem>

  <TabItem label="Common JS">
  ``` js
  // index.js

  module.exports = {
    onPreBuild: () => {
      console.log("Hello world from onPreBuild event!");
    },
  }
  ```
  </TabItem>

The plugin defined above will output `Hello world from onPreBuild event!` right before the site's build command is run.

The `index.js` file runs in a regular Node.js environment and can use any
[Node.js core methods](https://nodejs.org/api/) and [modules](https://www.npmjs.com/).
Environment variables, redirects, headers, and build configuration can be accessed and modified with [`netlifyConfig`](#netlifyconfig).

Store both files together in a single folder. You can store this folder with your site code to run as a [local plugin](#local-plugins), or you can [publish the plugin](/extend/develop-and-share/share-build-plugins#publish-to-npm) to npm.

> **Note - Use a compatible Node.js version:** For optimum compatibility while developing or running plugins, we recommend using the [default version](/build/configure-builds/available-software-at-build-time/) of Node.js installed by Netlify. However, you can also [specify a different version](/build/configure-builds/manage-dependencies/#node-js-and-javascript) for your project's setup, if needed.

## Local plugins

You can run your own custom plugins from within your site repository without publishing to npm. To do this, save your plugin `index.js` and `manifest.yml` files into a folder in the repository. Then, using the [file-based installation](/extend/install-and-use/build-plugins#file-based-installation) method, specify the absolute path to your plugin folder in the `package` field.

The following example installs a local plugin stored in `/plugins/netlify-plugin-hello-world`:

```toml
# netlify.toml

[[plugins]]
package = "/plugins/netlify-plugin-hello-world"
```

### Tip - Take care with formatting

Each plugin you add to the `netlify.toml` file must have its own `[[plugins]]` line. For a local plugin, the `package` value must start with `.` or `/`.

With a local plugin declared, you can verify it's loading correctly by using the [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli) to [run the build locally](/api-and-cli-guides/cli-guides/get-started-with-cli#run-builds-locally).

## Plugin values

When a plugin runs, it can receive certain data:
 - [constants](#constants): values generated by the plugin event
 - [inputs](#inputs): values configured by the plugin user
 - [netlifyConfig](#netlifyconfig) : the site's Netlify configuration
 - [packageJson](#packagejson): the contents of the site's `package.json` file
 - [environment variables](#environment-variables): values available in the Netlify build environment

### `constants`

Each event handler includes a `constants` key.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ constants }) {
  console.log(constants);
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: ({ constants }) => {
    console.log(constants);
  },
}
```
</TabItem>

The `constants` key contains the following values:

- **`CONFIG_PATH`:** path to the Netlify configuration file. `undefined` if none was used.
- **`PUBLISH_DIR`:** directory that contains the deploy-ready HTML files and assets generated by the build. Its value is
  always defined, but the target might not have been created yet.
- **`FUNCTIONS_SRC`:** directory where function source code lives. `undefined` if no `netlify/functions` directory exists in the base directory and if not specified by the user.
- **`FUNCTIONS_DIST`:** directory where built serverless functions are placed before deployment. Its value is always
  defined, but the target might not have been created yet.
- **`IS_LOCAL`:** boolean indicating whether the build was [run locally](/api-and-cli-guides/cli-guides/get-started-with-cli#run-builds-locally) or on Netlify.
- **`NETLIFY_BUILD_VERSION`:** version of Netlify Build as a `major.minor.patch` string.
- **`SITE_ID`:** Netlify site ID.

Along with these constants, plugins can also access any of the [environment variables](#environment-variables) that are available in the build environment.

### `inputs`

If your plugin requires additional values from the user, you can specify these requirements in an `inputs` array in the plugin's [`manifest.yml` file](#anatomy-of-a-plugin):

```yml
# manifest.yml

name: netlify-plugin-lighthouse
inputs:
  - name: output_path
    description: Path to save the generated HTML Lighthouse report
  - name: fail_deploy_on_score_thresholds
    description: Fail deploy if minimum threshold scores are not met
  - name: thresholds
    description: Key value mapping of thresholds that will fail the build when not passed
```

When you or a user install the plugin, the input names are used as keys with user-supplied values in the site
`netlify.toml` file:

```toml
# netlify.toml

[[plugins]]
package = "./plugins/netlify-plugin-lighthouse"

  [plugins.inputs]
    output_path = "reports/lighthouse.html"
    fail_deploy_on_score_thresholds = "true"

  [plugins.inputs.thresholds]
    performance = 0.9
    accessibility = 0.9
    best-practices = 0.9
    seo = 0.9
    pwa = 0.9
```

These `inputs` values are passed into the plugin when the event handlers are being executed.

To access them in your plugin code you can use the following pattern:

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ inputs }) {
  console.log(inputs.output_path);
  console.log(inputs.thresholds);
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: ({ inputs }) => {
    console.log(inputs.output_path);
    console.log(inputs.thresholds);
  },
}
```
</TabItem>

### Caution - Plugin inputs cannot be set through the Netlify UI

Currently, users cannot set inputs when [installing plugins from the Netlify UI](/extend/install-and-use/build-plugins#ui-installation). If you would like your plugin to be listed under 
### NavigationPath Component:

Project configuration > Build & deploy > Build plugins
, we recommend setting [zero-config defaults](https://github.com/netlify/plugins/blob/main/docs/guidelines.md) where possible, falling back to accepting values from [build environment variables](/build/configure-builds/environment-variables) if needed.

#### Input validation

Plugin inputs can be validated using the `inputs` property in the plugin `manifest.yml` file:

```yml
# manifest.yml

name: netlify-plugin-lighthouse
inputs:
  - name: output_path
    required: false
    description: Path to save the generated HTML Lighthouse report
    default: "reports/lighthouse.html"
  - name: fail_deploy_on_score_thresholds
    required: false
    description: Fail deploy if minimum threshold scores are not met
  - name: thresholds
    required: false
    description: Key value mapping of thresholds that will fail the build when not passed
```

The `inputs` property is an array of objects with the following members:

- **`name` `{string}`:** name of the input. Required.
- **`description` `{string}`:** description of the input.
- **`required` `{boolean}`**
- **`default` `{any}`:** default value.

### Tip

inputs</code>&nbsp;for validation">
We recommended using the `inputs` property to validate your plugin inputs and assign default values. This works more consistently and efficiently than coding your own validation inside event handlers.

### `netlifyConfig`

When an event handler executes, a site's Netlify configuration is normalized by [@netlify/config](https://github.com/netlify/build/tree/main/packages/config) and passed as a `netlifyConfig` object. Normalization includes applying context-specific or branch-specific settings and combining settings from `netlify.toml` with build settings configured in the Netlify UI.

After normalization, plugins can access and modify most `netlifyConfig` properties during a site's build. These include redirects, headers, and build configuration. If a site doesn't use `netlify.toml` or build settings selections in the Netlify UI, `netlifyConfig` and its properties contain default build settings.

Here's a list of modifiable properties:

- **`redirects`:** array of [redirects](/manage/routing/redirects/overview) with their modifiable options
- **`headers`:** array of [headers](/manage/routing/headers) with their modifiable options
- **`functions`:** object with options for modifying [functions](/build/configure-builds/file-based-configuration#functions)
- **`functions.directory`:** string that includes the path to a site's [functions directory](/build/functions/configuration#directory)
- **`edge_functions`:** array of [edge functions](/build/edge-functions/overview) with their modifiable options
- **`build.command`:** string that includes a site's [build command](/build/configure-builds/overview#definitions)
- **`build.environment`:** object that contains a subset of a site's [environment variables](#environment-variables)
- **`build.edge_functions`:** string that includes the path to a site's [edge functions directory](/build/edge-functions/optional-configuration#edge-functions-directory)
- **`build.processing`:** object that includes options for [post processing](/build/configure-builds/file-based-configuration#post-processing) HTML

And here's a plugin code sample that modifies several of the above properties.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ netlifyConfig }) {
  const newCommand = `node YOUR_SCRIPT.js`;

  // Run a script after the build command
  netlifyConfig.build.command = netlifyConfig.build.command
    ? `${netlifyConfig.build.command} && ${newCommand}`
    : newCommand;

  // Modify build command's environment variables
  netlifyConfig.build.environment.DATABASE_URI = getDatabaseUri();

  // Add redirects
  netlifyConfig.redirects.push({
    from: "/ORIGIN_PATH",
    to: "/DESTINATION_PATH",
  });

  // Add headers
  netlifyConfig.headers.push({
    for: "/YOUR_PATH",
    values: { YOUR_HEADER_NAME: "YOUR_HEADER_VALUE" },
  });

  // Add edge functions
  netlifyConfig.edge_functions
    ? netlifyConfig.edge_functions.push({ path: '/YOUR_PATH', function: 'YOUR_EDGE_FUNCTION' })
    : (netlifyConfig.edge_functions = [{ path: '/YOUR_PATH', function: 'YOUR_EDGE_FUNCTION' }])
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild({ netlifyConfig }) {
    const newCommand = `node YOUR_SCRIPT.js`;

    // Run a script after the build command
    netlifyConfig.build.command = netlifyConfig.build.command
      ? `${netlifyConfig.build.command} && ${newCommand}`
      : newCommand;

    // Modify build command's environment variables
    netlifyConfig.build.environment.DATABASE_URI = getDatabaseUri();

    // Add redirects
    netlifyConfig.redirects.push({
      from: "/ORIGIN_PATH",
      to: "/DESTINATION_PATH",
    });

    // Add headers
    netlifyConfig.headers.push({
      for: "/YOUR_PATH",
      values: { YOUR_HEADER_NAME: "YOUR_HEADER_VALUE" },
    });

    // Add edge functions
    netlifyConfig.edge_functions
      ? netlifyConfig.edge_functions.push({ path: '/YOUR_PATH', function: 'YOUR_EDGE_FUNCTION' })
      : (netlifyConfig.edge_functions = [{ path: '/YOUR_PATH', function: 'YOUR_EDGE_FUNCTION' }])
  },
};
```
</TabItem>

### `packageJson`

Each plugin event handler includes a `packageJson` argument. When an event handler executes, the contents of the `package.json` in a site's [base directory](/build/configure-builds/overview#definitions-1) get passed to a plugin. The data fields are [normalized](https://github.com/npm/normalize-package-data#what-normalization-currently-entails) to prevent plugin errors. If the site has no `package.json`, the argument is an empty object.

To access the `packageJson` object in your plugin code, use the following pattern:

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ packageJson }) {
  console.log(packageJson);
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: ({ packageJson }) => {
    console.log(packageJson);
  },
}
```
</TabItem>

### Environment variables

Plugins can access [build environment variables](/build/configure-builds/environment-variables) two different ways: 

- [`process.env`](https://nodejs.org/api/process.html#processenv): includes all Netlify build environment variables and any variables you declare using the Netlify UI or TOML. We recommend you use this when you only need to **get** values during the build process.
- [`netlifyConfig.build.environment`](#netlifyconfig): includes only the variables you declare using the Netlify UI or TOML. We recommend you use this when you need to **modify** values during the build process.

Visit our Forums for a verified Support Guide on [how to access environment variables during your site build](https://answers.netlify.com/t/support-guide-using-environment-variables-on-netlify-correctly/267).

## Plugin methods

We've provided a number of utilities and API methods to assist you in writing plugins.

### Utilities

Several utilities are provided with the `utils` argument to event handlers:

- **[`build`](#error-reporting):** used to report errors or cancel builds
- **[`status`](#logging):** used to display information in the deploy summary
- **[`cache`](https://github.com/netlify/build/blob/main/packages/cache-utils/README.md):** used to cache files between builds
- **[`run`](https://github.com/netlify/build/blob/main/packages/run-utils/README.md):** used to run commands and processes
- **[`git`](https://github.com/netlify/build/blob/main/packages/git-utils/README.md):** used to retrieve Git-related information such as the list of
  modified/created/deleted files

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = async function({ utils: { build, status, cache, run, git } }) {
  await run.command("eslint src/ test/");
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: async ({ utils: { build, status, cache, run, git } }) => {
    await run.command("eslint src/ test/");
  },
}
```
</TabItem>

### Error reporting

Exceptions thrown inside event handlers are reported in logs as bugs. Instead of using the `onError` event to handle exceptions, plugins should rely on `try`/`catch`/`finally` blocks and use `utils.build`:

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ utils }) {
  try {
    badMethod();
  } catch (error) {
    utils.build.failBuild("YOUR_FAILURE_MESSAGE");
  }
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: ({ utils }) => {
    try {
      badMethod();
    } catch (error) {
      utils.build.failBuild("YOUR_FAILURE_MESSAGE");
    }
  },
}
```
</TabItem>

The following methods are available depending on the error's type:

- **`utils.build.failBuild("YOUR_MESSAGE")`:** method that fails the build - the build in your dashboard would show "Failed". Use this to
  indicate something went wrong.
- **`utils.build.failPlugin("YOUR_MESSAGE")`:** method that fails the plugin but not the build.
- **`utils.build.cancelBuild("YOUR_MESSAGE")`:** method that cancels the build - the dashboard would show "Cancelled" for that build. Use
  this to indicate that the build is being cancelled as planned.

`utils.build.failBuild()`, `utils.build.failPlugin()` and `utils.build.cancelBuild()` can specify an options object with
the following properties:

- **`error`:** original `Error` instance. Its stack trace will be preserved and its error message will be appended to
  the `"YOUR_MESSAGE"` argument.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ utils }) {
  try {
    badMethod();
  } catch (error) {
    utils.build.failBuild("YOUR_FAILURE_MESSAGE", { error });
  }
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: ({ utils }) => {
    try {
      badMethod();
    } catch (error) {
      utils.build.failBuild("YOUR_FAILURE_MESSAGE", { error });
    }
  },
}
```
</TabItem>

### Logging

Anything logged to the console will be printed in the build logs.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function() {
  console.log("This is printed in the build logs");
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild() {
    console.log("This is printed in the build logs");
  },
}
```
</TabItem>

If you'd prefer to make the information more visible, `utils.status.show()` can be used to display them in the [deploy summary](/deploy/deploy-overview#deploy-summary) instead.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = function({ utils }) {
  utils.status.show({
    // Optional. Default to the plugin's name followed by a generic title.
    title: "Main title",
    // Required.
    summary: "Message below the title",
    // Optional. Empty by default.
    text: "Detailed information shown in a collapsible section",
  });
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild({ utils }) {
    utils.status.show({
      // Optional. Default to the plugin's name followed by a generic title.
      title: "Main title",
      // Required.
      summary: "Message below the title",
      // Optional. Empty by default.
      text: "Detailed information shown in a collapsible section",
    });
  },
}
```
</TabItem>

Only one status is shown per plugin. Calling `utils.status.show()` twice overrides the previous status.

This is meant for successful information. Errors should be reported [with `utils.build.*` instead](#error-reporting).

### Asynchronous code

Asynchronous code can be achieved by using `async` methods:

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = async function({ utils }) {
  try {
    await doSomethingAsync();
  } catch (error) {
    utils.build.failBuild("YOUR_FAILURE_MESSAGE", { error });
  }
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: async ({ utils }) => {
    try {
      await doSomethingAsync();
    } catch (error) {
      utils.build.failBuild("YOUR_FAILURE_MESSAGE", { error });
    }
  },
}
```
</TabItem>

Any thrown `Error` or rejected `Promise` that is not handled by [`utils.build`](#error-reporting) will be shown in the
build logs as a plugin bug.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export const onPreBuild = async function({ utils }) {

  // Any error thrown inside this function will be shown
  // in the build logs as a plugin bug.

  await doSomethingAsync();
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = {
  onPreBuild: async ({ utils }) => {

    // Any error thrown inside this function will be shown
    // in the build logs as a plugin bug.

    await doSomethingAsync();
  },
}
```
</TabItem>

Plugins end as soon as their methods end. Therefore you should `await` any asynchronous operation. The following
examples show invalid code and the way to fix it.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js
// Example of how to use callbacks.

const { promisify } = require("util");

// VALID EXAMPLE: please use this.
// This callback will be awaited.
export const onPostBuild = async function({ utils }) {
  const response = await promisify(doSomethingAsync)();

  console.log(response);
}

// INVALID EXAMPLE: do not use this.
// This callback will not be awaited.
export const onPostBuild = function({ utils }) {
  doSomethingAsync((error, response) => {
    console.log(response);
  })
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js
// Example of how to use callbacks.

const { promisify } = require("util");

module.exports = {

  // VALID EXAMPLE: please use this.
  // This callback will be awaited.
  onPostBuild: async ({ utils }) => {
    const response = await promisify(doSomethingAsync)();

    console.log(response);
  },

  // INVALID EXAMPLE: do not use this.
  // This callback will not be awaited.
  onPreBuild: ({ utils }) => {
    doSomethingAsync((error, response) => {
      console.log(response);
    })
  },
}
```
</TabItem>

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js
// Example of how to use events.

const pEvent = require("p-event");

// VALID EXAMPLE: please use this.
// This event will be awaited.
export const onPreBuild = async function({ utils }) {
  const emitter = doSomethingAsync();

  emitter.start();

  const response = await pEvent(emitter, "response");

  console.log(response);
}

// INVALID EXAMPLE: do not use this.
// This event will not be awaited.
export const onPreBuild = function({ utils }) {
  const emitter = doSomethingAsync();

  emitter.on("response", response => {
    console.log(response)
  });

  emitter.start()
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js
// Example of how to use events.

const pEvent = require("p-event");

module.exports = {
  // VALID EXAMPLE: please use this.
  // This event will be awaited.
  onPreBuild: async ({ utils }) => {
    const emitter = doSomethingAsync();

    emitter.start();

    const response = await pEvent(emitter, "response");

    console.log(response);
  },

  // INVALID EXAMPLE: do not use this.
  // This event will not be awaited.
  onPreBuild: ({ utils }) => {
    const emitter = doSomethingAsync();

    emitter.on("response", response => {
      console.log(response)
    });

    emitter.start();
  },
}
```
</TabItem>

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js
// Example of how to use `Array.forEach()`.

// VALID EXAMPLE: please use this.
// This callback will be awaited.
export const onPostBuild = async function({ utils }) {
  await Promise.all(
    array.map(async () => {
      await doSomethingAsync()
    }),
  );
}

// INVALID EXAMPLE: do not use this.
// This callback will not be awaited.
export const onPostBuild = function({ utils }) {
  array.forEach(async () => {
    await doSomethingAsync();
  });
}
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js
// Example of how to use `Array.forEach()`.

module.exports = {
  // VALID EXAMPLE: please use this.
  // This callback will be awaited.
  onPostBuild: async ({ utils }) => {
    await Promise.all(
      array.map(async () => {
        await doSomethingAsync();
      }),
    );
  },

  // INVALID EXAMPLE: do not use this.
  // This callback will not be awaited.
  onPreBuild: ({ utils }) => {
    array.forEach(async () => {
      await doSomethingAsync();
    });
  },
}
```
</TabItem>

### Dynamic events

Some plugins trigger different events depending on the user's `inputs`. This can be achieved by returning the plugin
object from a function instead.

### Tabs Component:

<TabItem label="ES modules">
``` js
// index.js

export default function helloWorldPlugin(inputs) {
  if (inputs.before) {
    return {
      onPreBuild: () => {
        console.log("Hello world from onPreBuild event!");
      },
    }
  } else {
    return {
      onPostBuild: () => {
        console.log("Hello world from onPostBuild event!");
      },
    }
  }
};
```
</TabItem>

<TabItem label="Common JS">
``` js
// index.js

module.exports = function helloWorldPlugin(inputs) {
  if (inputs.before) {
    return {
      onPreBuild: () => {
        console.log("Hello world from onPreBuild event!");
      },
    }
  } else {
    return {
      onPostBuild: () => {
        console.log("Hello world from onPostBuild event!");
      },
    }
  }
}
```
</TabItem>


