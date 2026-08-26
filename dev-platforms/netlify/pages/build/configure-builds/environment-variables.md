---
title: "Netlify Build Environment Variables"
source: https://docs.netlify.com/build/configure-builds/environment-variables.md
path: build/configure-builds/environment-variables
---

---
title: "Build environment variables"
description: "Identify environment variables available in the build environment, set your own environment variables, and use environment variables during builds."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Netlify [environment variables](/build/environment-variables/overview) are accessible during your build. This allows you to change behaviors based on deploy parameters or to include information you don't want to save in your repository, such as API keys.

This page describes how to create environment variables, the specific configuration and read-only variables that are available in the Netlify build environment, and how to use environment variables during the build process.

## Declare variables

You can [declare and set environment variables](/build/environment-variables/get-started/#create-environment-variables) using the Netlify UI, CLI, API, or a Netlify configuration file. If you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your environment variables, the scope must include **Builds** to be available to the build system.

Visit the [environment variables overview](/build/environment-variables/overview) to learn more about environment variables at Netlify.

## Netlify configuration variables

By setting custom values for certain reserved environment variables, you can change some aspects of your build, such as [language and dependency versions](/build/configure-builds/manage-dependencies). Links in the variable descriptions below provide more information about requirements, defaults, and accepted values.

- **`NODE_VERSION`:** value that sets the [Node.js version](/build/configure-builds/manage-dependencies#node-js-and-javascript).
- **`NODE_ENV`:** value that sets the [Node.js environment](/build/configure-builds/manage-dependencies#node-js-environment).
- **`NPM_VERSION`:** value that sets the [npm version](/build/configure-builds/manage-dependencies#npm).
- **`NPM_FLAGS`:** value passed as [flags on the `npm install` command](/build/configure-builds/manage-dependencies#npm).
- **`NPM_RC`:** sets the contents of `.npmrc` file, takes precedence over `NPM_TOKEN`
- **`NPM_TOKEN`:** used for [fetching private npm modules](/build/configure-builds/manage-dependencies#npm). If you use Yarn, use `YARN_NPM_AUTH_TOKEN` instead.
- **`NETLIFY_USE_YARN`:** used to override the [default behavior for installing and running Yarn](/build/configure-builds/manage-dependencies#yarn).
- **`YARN_VERSION`:** used to set the [Yarn version](/build/configure-builds/manage-dependencies#yarn).
- **`YARN_FLAGS`:** passed as [flags on the `yarn` command](/build/configure-builds/manage-dependencies#yarn).
- **`YARN_NPM_AUTH_TOKEN`:** used for [fetching private npm modules](/build/configure-builds/manage-dependencies#yarn) with Yarn.
- **`BUN_FLAGS`:** passed as [flags on the `bun install` command](/build/configure-builds/manage-dependencies#bun).
- **`BUN_VERSION`:** value that sets the [Bun version](/build/configure-builds/manage-dependencies#bun).
- **`RUBY_VERSION`:** used to set the [Ruby version](/build/configure-builds/manage-dependencies#ruby).
- **`PHP_VERSION`:** value that sets the PHP version. Default and available values are determined by the site [build-image](/build/configure-builds/overview#build-image-selection).
- **`PNPM_FLAGS`:** passed as [flags on the `pnpm install` command](/build/configure-builds/manage-dependencies#pnpm).
- **`PYTHON_VERSION`:** value that sets the [Python version](/build/configure-builds/manage-dependencies#python).
- **`HUGO_VERSION`:** value that sets the [Hugo version](/build/frameworks/framework-setup-guides/hugo#hugo-version).
- **`SWIFT_VERSION`:** value that sets the [Swift version](/build/configure-builds/manage-dependencies#swift).
- **`GO_VERSION`:** value that sets the Go version. Default and available values are determined by the site [build-image](/build/configure-builds/overview#build-image-selection).
- **`NETLIFY_NEXT_PLUGIN_SKIP`:** when set to `true` for a Next.js site using Runtime v4, the build doesn't use the [Next.js Runtime](https://github.com/netlify/next-runtime#readme). Use this variable with projects that generate static HTML using `next export`.
- **`DISABLE_IPX`:** when set to `true` for a Next.js site using Runtime v4, the build will not generate a function for the `next/image` loader bundled into Next.js Runtime. This may break some sites unless another [image loader](https://nextjs.org/docs/pages/api-reference/components/image#loader) is also specified.
- **`NETLIFY_SKIP_GATSBY_FUNCTIONS`**: when set to `true` for a Gatsby site, the [Essential Gatsby build plugin](https://github.com/netlify/netlify-plugin-gatsby#readme) will not [automatically generate Netlify Functions](/build/frameworks/framework-setup-guides/gatsby#auto-generated-netlify-functions). This will disable some Gatsby features and may break some sites.
- **`NETLIFY_IMAGE_CDN`**: value defaults to `false`. When set to `true`, the [Essential Gatsby build plugin](https://github.com/netlify/netlify-plugin-gatsby/blob/main/docs/image-cdn.md) or [Gatsby adapter for Netlify](https://github.com/gatsbyjs/gatsby/blob/master/packages/gatsby-adapter-netlify/README.md#imagecdn) will use Netlify Image CDN instead of processing images at build time for Gatsby sites. Not supported for Gatsby version 5.12.x.
- **`GATSBY_CLOUD_IMAGE_CDN`**: deprecated variable that is supported but no longer recommended - use `NETLIFY_IMAGE_CDN` instead. Value defaults to `false`. When set to `true`, the [Essential Gatsby build plugin](https://github.com/netlify/netlify-plugin-gatsby/blob/main/docs/image-cdn.md) will use Netlify Image CDN instead of processing images at build time.
- **`GATSBY_EXCLUDE_DATASTORE_FROM_BUNDLE`:** value that defaults to `false`. When set to `true`, the [Essential Gatsby build plugin](https://github.com/netlify/netlify-plugin-gatsby#readme) loads the Gatsby datastore from the CDN instead of bundling it with a function.
- - **`AWS_LAMBDA_JS_RUNTIME`:** value that sets the [Node.js runtime version for Netlify Functions](/build/functions/configuration/?fn-language=js#node-js-version-for-runtime-2). This environment variable must be set using the Netlify UI, CLI, or API, and not with a Netlify configuration file (`netlify.toml`).
- **`CI`:** value that defaults to `true`, indicating that the build is running in a Continuous Integration (CI) environment. If this [causes issues for your build](/build/configure-builds/troubleshooting-tips#build-fails-on-warning-message), you can override the variable by adding `CI='' ` to the beginning of your site [build command](/build/configure-builds/overview#build-settings).

The following variables should be set in the Netlify UI rather than in `netlify.toml`. This is because the Netlify configuration file is read after your repository has been cloned.

- **`GIT_LFS_ENABLED`:** value that is undefined by default. If set, we'll use `git lfs clone` to check out your repository - otherwise we use `git clone`.
- **`GIT_LFS_FETCH_INCLUDE`:** if `GIT_LFS_ENABLED` is set, this specifies by file extension which Git LFS files will be downloaded when cloning your repository. Any other file extensions will have only text pointer files downloaded instead of the original media files.
- **`NETLIFY_BUILD_DEBUG`:** set this to `true` to print additional debugging information in the build logs. The output does not contain sensitive information. To disable debugging, delete the variable. Alternatively, delete everything in the variable's **Value** field.

## Read-only variables

In addition to the variables you choose to declare, Netlify has a number of pre-defined variables built in. **The following variables are automatically set for your builds, and their values are not changeable.**

### Build metadata

- **`NETLIFY`:** always `true`. Can be used to check if the build is running on Netlify.
- **`BUILD_ID`:** unique ID for the build; for example: `5d4aeac2ccabf517d2f219b8`.
- **`CONTEXT`:** name of the build's [deploy context](/deploy/deploy-overview#deploy-contexts). It can be `production`, `deploy-preview`, `branch-deploy`, or `dev`.
- **`NETLIFY_PREVIEW_SERVER`:** always `true` if present. Only present if your site/app is running in a Preview Server virtual environment. Learn more about [Preview Servers](/manage/preview-servers/overview).

### Git metadata

- **`REPOSITORY_URL`:** URL for the [linked Git repository]( /build/git-workflows/repo-permissions-linking).
- **`BRANCH`:** reference to check out after fetching changes from the Git repository.
- **`HEAD`:** name of the head branch received from a Git provider.
- **`COMMIT_REF`:** reference ID (also known as "SHA" or "hash") of the commit we're building.
- **`CACHED_COMMIT_REF`:** reference ID (also known as "SHA" or "hash") of the last commit that we built before the current build. When a build runs without cache, `CACHED_COMMIT_REF` will be the same as the `COMMIT_REF`.
- **`PULL_REQUEST`:** whether the build is from a pull/merge request (`true`) or not (`false`).
- **`REVIEW_ID`:** ID of the request and the Deploy Preview it generated (for example, `1211`) if from a pull/merge request. These two numbers will always match. (For example, `deploy-preview-12` is for PR #12 in your repository.)

### Deploy URLs and metadata

- **`URL`:** URL representing the main address to your site. It can be either a Netlify subdomain or your own custom domain if you set one; for example, `https://petsof.netlify.app` or `https://www.petsofnetlify.com`.
- **`DEPLOY_URL`:** URL representing the unique URL for an individual deploy. It starts with a unique ID that identifies the deploy; for example, `https://5b243e66dd6a547b4fee73ae--petsof.netlify.app`.
- **`DEPLOY_PRIME_URL`:** URL representing the primary URL for an individual deploy, or a group of them, like branch deploys and Deploy Previews; for example, `https://feature-branch--petsof.netlify.app` or `https://deploy-preview-1--petsof.netlify.app`. If you set up an [automatic deploy subdomain](/manage/domains/manage-domains/automatic-deploy-subdomains), this URL will update.
- **`DEPLOY_ID`:** unique ID for the deploy; for example, `578ab634d6865d5cf960d620`. Matches the beginning of `DEPLOY_URL`.
- **`SITE_NAME`:** name of the site, its Netlify subdomain; for example, `petsof`.
- **`SITE_ID`:** unique ID for the site; for example, `1d01c0c0-4554-4747-93b8-34ce3448ab95`.
- **`ACCOUNT_ID`:** unique ID for the Netlify team account which owns the site; for example: `63dd1fafda1bc5006q0f5cd`.

### Build hook metadata and payload

If your build is triggered from a custom [build hook](/build/configure-builds/build-hooks), Netlify also has three build-hook-specific variables:

- **`INCOMING_HOOK_TITLE`:** title of the build hook.
- **`INCOMING_HOOK_URL`:** URL of the build hook.
- **`INCOMING_HOOK_BODY`:** [payload](/build/configure-builds/build-hooks#payload) of the request sent to the build hook URL.

## Access variables

Build environment variables are available in the build system they're set in and are available for use by build plugins and scripts run during the build step for a site. This section outlines how to access these variables during the build process.

Note that, as these are build variables specifically, you will need to take extra steps if you want your site to have [access to these values after the build is complete](#use-variables-in-a-site-after-it-s-built).

### Tip - Check your variable scope

If you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your environment variables, the scope must include **Builds** to be available to the Netlify build system.

### Prepare your build environment

To use these environment variables, you need to ensure they're set in the environment where the build will run - on Netlify through continuous deployment or in your local development environment.

#### Build on Netlify

If you have continuous deployment set up, Netlify will automatically start a build and deploy whenever you push code to your Git repo. While the build runs on Netlify, the build system already has access to all of the [variables set in the Netlify build environment](/build/environment-variables/get-started/#create-environment-variables) and can use them during the build process.

Note that when you build on Netlify, the build system doesn't read `.env` files. To use variables declared in a `.env` file, we recommend you [import the variables](/build/environment-variables/get-started/#import-variables-from-env-files) into Netlify before you build. This way the variables in your `.env` file remain secure and out of your shared repository.

#### Build locally

When you build in your local development environment, you need to ensure these environment variables are set in the local environment before you run the build command.

The best way to build locally is to use the [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli#run-builds-locally). Building locally with the CLI mimics the behavior of running a build on Netlify and will give you access to the environment variables you've already set there.

```sh
netlify build
```

You can also use [Netlify Dev](/api-and-cli-guides/cli-guides/local-development) with `--context production` to run a local development environment that mimics the Netlify production environment. Netlify Dev will automatically pull down environment variables stored on Netlify and read any variables stored in a `.env` file on your machine.

If you don't want to use the Netlify CLI or Netlify Dev, you need to set the variables in your local development environment yourself.

There are a few different ways to do this, including declaring variables directly in the command line or using a `.env` file and [dotenv](https://www.npmjs.com/package/dotenv). Just remember not to commit any sensitive values to your repository.

Visit our Forums for a verified Support Guide on [how to access environment variables during your site build](https://answers.netlify.com/t/support-guide-using-environment-variables-on-netlify-correctly/267) for more tips.

### Use variables during the build

Once the variables are set correctly in the environment you want to build in, you can access them in a few different ways depending on the context.

* [Use variables in the `netlify.toml` or Netlify UI](#use-variables-in-the-netlify-toml-or-netlify-ui)
* [Use variables to install private npm modules](#use-variables-to-install-private-npm-modules)
* [Use variables in Node.js script files](#use-variables-in-node-js-script-files)
* [Use variables in build plugins](#use-variables-in-build-plugins)
* [Use variables in a site after it's built](#use-variables-in-a-site-after-it-s-built)

#### Use variables in the `netlify.toml` or Netlify UI

Netlify commands use the Bash shell, so you can use Bash syntax to select the environment variable: `$VARIABLE_NAME`.

You can use this format in the Netlify UI and in the `netlify.toml` with the `build.command` and `ignore.command`.

For example, to print a **not-sensitive** variable (`GREETING = "hi there"`) to the deploy log at the end of the build step, set the build command in the Netlify UI to `npm run build && echo $GREETING`.

![](/images/configure-builds-environment-variables-build-command-ui.png)

The next time you build and deploy the site, the build process will print the variable to the deploy log at the end of the build step.

![](/images/configure-builds-environment-variables-ui-example-deploy-log.png)

Note that if you would like to use environment variable values in the `[[headers]]` and `[[redirects]]` sections of the `netlify.toml`, you need to [inject the values as part of your build command](/build/configure-builds/file-based-configuration#inject-environment-variable-values).

#### Use variables to install private npm modules

To use an environment variable for private npm module installs, you can [set an `NPM_TOKEN` value](/build/configure-builds/manage-dependencies#npm) in your build environment. Whenever Netlify runs an install and build, npm will automatically check the environment for an `NPM_TOKEN` to use for authentication. This way, you can avoid declaring or accessing this sensitive variable value directly in your `package.json`. If you use Yarn to manage dependencies, [set `YARN_NPM_AUTH_TOKEN`](/build/configure-builds/manage-dependencies#yarn) instead of `NPM_TOKEN`.

#### Use variables in Node.js script files

To access environment variables in script files that Node.js runs during the build process, you need to use the format `process.env.VARIABLE_NAME`.

For example, create a file `sayHello` in TypeScript or JavaScript that will log your **non-sensitive** variable (`GREETING = "hi there"`) to the console when run:

### Tabs Component:

<TabItem label="TypeScript">

```typescript
  const greetPerson: string = process.env.GREETING;
  console.log(`Say hello: ${greetPerson}`);
```

</TabItem>

<TabItem label="JavaScript">

```js
  const greetPerson = process.env.GREETING;
  console.log(`Say hello: ${greetPerson}`);
```

</TabItem>

Then, update the build command in the `package.json` or in the `netlify.toml` to include the instruction to run the script file:

### Tabs Component:

<TabItem label="netlify.toml with TS file">

```toml
# Replace ts-node with the appropriate command
# for your TypeScript compiler for node.js
[build]
  command = "npm run build && ts-node ./sayHello.ts"
```

</TabItem>

<TabItem label="netlify.toml with JS file">

```toml
[build]
  command = "npm run build && node ./sayHello.js"
```

</TabItem>

The next time you build and deploy the site, the build process will print the variable to the deploy log at the end of the build step.

![](/images/configure-builds-environment-variables-script-example-deploy-log.png)

#### Use variables in build plugins

There are two ways to access environment variables in build plugins: [using `process.env.VARIABLE_NAME` or using `netlifyConfig`](/extend/develop-and-share/develop-build-plugins#environment-variables).

#### Use variables in a site after it's built

If you want to use environment variable values in a site after it's built, you need to take further action to provide access. Here are a few options:

- Use a [serverless function](/build/functions/environment-variables) or [edge function](/build/edge-functions/environment-variables) to access values during runtime. This is the best option to avoid revealing sensitive values.
- Use [snippet injection](/build/post-processing/snippet-injection/) to access values during post-processing.
- Use a custom script or framework-specific variables to [copy values into the site](/build/frameworks/use-environment-variables-with-frameworks#embed-variable-values-in-the-site-build) code during the build process.

If you inject values into the site using a build script or snippet injection, make sure to only include non-sensitive values.

More details are available in our verified Support Guide on [how to access environment variables](https://answers.netlify.com/t/support-guide-using-environment-variables-on-netlify-correctly/267).

## More environment variables resources
- [Overview of environment variables](/build/environment-variables/overview) at Netlify
- Verified Support Guide on [how to use environment variables](https://answers.netlify.com/t/support-guide-using-environment-variables-on-netlify-correctly/267)
- [Injecting environment variable values in your `netlify.toml` file](/build/configure-builds/file-based-configuration#inject-environment-variable-values)
- [Environment variables for different deploy contexts](/deploy/deploy-overview#deploy-contexts)
- [Hugo version environment variable](/build/frameworks/framework-setup-guides/hugo#hugo-version)
- [Node.js functions runtime settings](/build/functions/configuration/?fn-language=js#node-js-version-for-runtime-2)

