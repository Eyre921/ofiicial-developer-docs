---
title: "Netlify Environment Variables: Get Started"
source: https://docs.netlify.com/build/environment-variables/get-started.md
path: build/environment-variables/get-started
---

---
title: "Get started with environment variables"
description: "Use environment variables to configure your site's build and functionality. Learn how to declare and use environment variables with your site."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Netlify offers multiple ways to securely create, update, and use environment variables for your sites.

This page outlines how to [create and manage](#create-environment-variables) site environment variables and shared environment variables, how to [use environment variables](#use-environment-variables) once they are declared, how to work with [`.env` files](#work-with-env-files) on Netlify, and how [untrusted deploys](#untrusted-deploys-and-sensitive-variables) handle sensitive variables.

## Create environment variables

You can create environment variables with the Netlify UI, CLI, or API, or with a Netlify configuration file. Once you create environment variables, build and deploy your site for the additions to take effect.

### Create variables with the Netlify UI, CLI, or API

When you create environment variables using the Netlify UI, CLI, or API, they are set and securely stored on Netlify. This means you can avoid committing any sensitive values to your repository. The Netlify UI reflects any changes made using the CLI or API and vice versa.

You can create [site environment variables](#site-environment-variables) and [shared environment variables](#shared-environment-variables).

Be aware that variables set in a Netlify [configuration file](#create-variables-with-a-netlify-configuration-file) override variables set with the Netlify UI, CLI, or API.

#### Site environment variables

There are three ways to create site environment variables:

- In the Netlify UI, create site variables under 
### NavigationPath Component:

Project configuration > Environment variables
. You can create variables individually or - With the Netlify CLI, use `env:set` to create a site environment variable, and `env:import` to import from a `.env` file. Review our [Get Started with Netlify CLI guide](/api-and-cli-guides/cli-guides/get-started-with-cli#manage-environment-variables) to learn more.
- With the Netlify API, use `createEnvVars` to create a new site environment variable. Review our [Get Started with Netlify API guide](/api-and-cli-guides/api-guides/get-started-with-api#environment-variables) to learn more.

If a shared environment variable and a site environment variable exist with the same key name and scope, the site environment variable's contextual values take precedence in each deploy context. In addition, variables set in the `netlify.toml` will override those with the same key set in the Netlify UI. Review the [overrides](/build/environment-variables/overview#overrides) section to learn more.

#### Shared environment variables

> **Pricing Information:** This feature is available on [Pro](https://www.netlify.com/pricing/?category=developer) and [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

There are two ways to create shared environment variables:

- In the Netlify UI, create shared variables under 
### NavigationPath Component:

Team settings > Environment variables
.
- With the Netlify API, use `createEnvVars` to create a new shared environment variable. Review our [Get Started with Netlify API guide](/api-and-cli-guides/api-guides/get-started-with-api#environment-variables) to learn more.

Variables set at the team level are shared by all sites owned by the team. Only Team Owners can read and access shared variables through the Netlify UI, CLI, and API.

If a shared environment variable and a site environment variable exist with the same key name and scope, the site environment variable's contextual values take precedence in each deploy context. Review the [overrides](/build/environment-variables/overview#overrides) section to learn more.

### Create variables with a Netlify configuration file

You can create site environment variables with a Netlify [configuration file](/build/configure-builds/file-based-configuration) stored in your repository. This file-based configuration method allows you to set different environment variables for different [deploy contexts](/build/configure-builds/file-based-configuration#deploy-contexts) .

Note that you can't set scopes for variables declared using the configuration file. All variables declared using this method have the **Builds** and **Post processing** scope.

Since `netlify.toml` is stored in your repository, we recommend setting sensitive values with the [Netlify UI, CLI, or API](#create-variables-with-the-netlify-ui-cli-or-api) instead, where possible.

Here is an example of how to declare variables in `netlify.toml`:

```toml
# Production context: all deploys from the Production branch
# set in your site's Branches settings in the UI will inherit
# these settings. You can define environment variables
# here but we recommend using the Netlify UI for sensitive
# values to keep them out of your source repository.
[context.production]
  publish = "output/"
  command = "make publish"
  environment = { NODE_VERSION = "14.15.3" }

# Here is an example of how to define context-specific
# environment variables. Be mindful when using this
# option and avoid committing sensitive values to public
# source repositories.
[context.deploy-preview.environment]
  NOT_PRIVATE_ITEM = "not so secret"

# Branch Deploy context: all deploys that are not from
# a pull/merge request or from the Production branch
# will inherit these settings.
[context.branch-deploy.environment]
  NODE_ENV = "development"

# Dev context: environment variables set here
# are available for local development environments
# run using Netlify Dev. These values can be
# overwritten on branches that have a more specific
# branch context configured.
[context.dev.environment]
  NODE_ENV = "development"

# Specific branch context: all deploys from
# this specific branch will inherit these settings.
[context.staging.environment] # "staging" is a branch name
  NODE_ENV = "development"
```

Variables set in a configuration file override variables set with the Netlify UI, CLI, or API.

## Modify and delete environment variables

There are multiple ways to edit or delete environment variables that you set using the Netlify UI, CLI, or API. Note that only Team Owners can read and modify shared variables.

Need to export your variables? Review the [export variables for your `.env`](#export-variables-for-env-files) section below.

### Caution - To apply environment variable changes, build and deploy.

Environment variable changes require a build and deploy to take effect.

### Update variables with the Netlify UI

To edit or delete site environment variables:

1. Navigate to 
### NavigationPath Component:

Project configuration > Environment variables
 for site environment variables or to 
### NavigationPath Component:

Team settings > Environment variables
 for shared environment variables.
2. Filter the list of variables by key name to find the variable you want to modify. Then, select the variable from the list to expand the variable details.
3. Select 
### NavigationPath Component:

Options > Edit
 or 
### NavigationPath Component:

Options > Delete
 and then follow the prompts to complete your change.

### Update variables with the Netlify CLI or API

You can use the Netlify CLI to update site environment variables and the Netlify API to update both site and shared environment variables.

- With the Netlify CLI, use `env:set` to update a site environment variable, `env:import` to import from an updated `.env` file, and `env:unset` to delete a site environment variable and all of its contextual values.
- With the Netlify API, use `updateEnvVar` to update all values for an environment variable, `setEnvVarValue` to update or create a single value for an existing variable, `deleteEnvVar` to delete a variable and all of its values, or `deleteEnvVarValue` to delete a specific value.

Review our [Get Started with Netlify CLI guide](/api-and-cli-guides/cli-guides/get-started-with-cli#manage-environment-variables) and our [Get Started with Netlify API guide](/api-and-cli-guides/api-guides/get-started-with-api#environment-variables) to learn more.

## Use environment variables

Once you've created environment variables, there are many different ways you can use them:

- Use environment variables [during the build process](/build/configure-builds/environment-variables#access-variables) - such as in the `netlify.toml`, to install private npm modules, in Node.js script files, and in build plugins.
- Use a custom script or framework-specific variables to [copy values into the site](/build/frameworks/use-environment-variables-with-frameworks#embed-variable-values-in-the-site-build) code during the build process, for use while your site runs.
- Use a [function](/build/functions/environment-variables#access-environment-variables) to access values during runtime.
- Use variables for spam prevention with [forms](/manage/forms/spam-filters#custom-recaptcha-2) or to specify [signed proxy redirects](/manage/routing/redirects/rewrites-proxies#signed-proxy-redirects).
- Use [snippet injection](/build/post-processing/snippet-injection/#environment-variables) to access values during post-processing.

If you inject values into the site using a build script or snippet injection, make sure to only include non-sensitive values.

## Work with `.env` files

When you build on Netlify, the build system does not read `.env` files. Instead, you can [
For local builds, the Netlify CLI will read the `.env` files you have stored in your local environment. These variables will therefore be available to your site for use.

### Tip

Using Netlify configuration variables in <code>.env</code> files for your framework</span>">
If your framework references your `.env` file during the build step and you need to use Netlify's configuration or read-only variables, review our docs on [how to add Netlify variable values to your `.env`](/build/frameworks/use-environment-variables-with-frameworks#env-files-and-netlify-variables).

### Import variables from `.env` files

We recommend that you 
Environment variables in a `.env` file are formatted as key-value pairs. That is, a list of variables where each variable is on a new line and is formatted with the key name, followed by an equals sign, and then the value.

A single `.env` file represents the variables for a specific environment. Here is an example of a production `.env` file:

```
YOUR_API_KEY=a production secret
NODE_VERSION=16
NODE_ENV=production
```

To learn more about the parsing rules the Netlify UI and CLI follow for `.env` imports, review the [dotenv docs](https://www.npmjs.com/package/dotenv#what-rules-does-the-parsing-engine-follow).

#### Import variables with the Netlify UI

With the Netlify UI, you can import a `.env` file to your site environment variables or shared environment variables.

Imported variables are merged with existing environment variables. If existing variables have any of the key names in the `.env` file you're importing, you can specify how Netlify should handle those conflicts.

1. Navigate to 
### NavigationPath Component:

Project configuration > Environment variables
 for site environment variables or to 
### NavigationPath Component:

Team settings > Environment variables
 for shared environment variables.
2. Select 
### NavigationPath Component:

Add a variable > Import from a .env file
.
3. Copy the contents of your `.env` file into the form.
4. Set the **Scopes** and **Deploy contexts** to use for these variables and values. All variables imported through this form submission will have the same scope and deploy context settings.
5. If the variables to import include keys that conflict with existing variables, a **Merge strategy** section will appear in the form. You can choose to either **Skip conflicts** and ignore any new values, or **Update conflicts** and set new [contextual values](/build/environment-variables/overview#value-per-deploy-context) for the existing variables.
6. Select **Import variables** to add the variables.

### Note - Scope changes may be ignored for environment variable conflicts

Scope changes only apply to existing variables when you select **All deploy contexts** to apply the same value for use across all deploy contexts. If an environment variable already exists with the same key name and you're adding specific contextual values with this import, changes to the scope will be ignored.

#### Import variables with the Netlify CLI

Use the Netlify CLI command `env:import` to 
As the CLI works on a site level, you can only use it to import site environment variables. The imported variables are set to all scopes and with the same value for all deploy contexts.

By default, environment variables you import are merged with any existing ones on Netlify. If you would rather remove all existing variables and replace them with what is in the imported file, use the `--replace-existing` flag. For example:

```sh
# Warning: using the --replace-existing flag will delete all
# existing variables and keep only those imported from the .env
netlify env:import .env --replace-existing
```

### Export variables for `.env` files

If you would like to export variables set and stored on Netlify, you can export them in `.env` format using the [Netlify UI](#export-variables-with-the-netlify-ui) or the [Netlify CLI](#export-variables-with-the-netlify-cli).

#### Export variables with the Netlify UI

As `.env` files include variables for a specific environment, you can export environment variables from the Netlify UI for each deploy context.

1. Navigate to 
### NavigationPath Component:

Project configuration > Environment variables
 for site environment variables or to 
### NavigationPath Component:

Team settings > Environment variables
 for shared environment variables.
2. Select a deploy context in the **Context** filter.
3. Select the clipboard icon to copy the filtered list in `.env` format to your clipboard.
4. Paste the results in your local `.env` file or [import the variables](#import-variables-with-the-netlify-ui) into another Netlify site.

![](/images/environment-variables-export-env-ui.png)

#### Export variables with the Netlify CLI

You can export environment variables for each deploy context using the Netlify CLI command `env:list --plain`. With the `--plain` flag, the CLI outputs the results in plain text format that you can copy into your `.env` file locally.

By default, only those values set for the `Local development (Netlify CLI)` deploy context are output. To export the values from another deploy context, use the `--context` flag.

For example, to export all of the `production` deploy context values in `.env` format, use this command:

```sh
# list the production deploy context values in .env format
netlify env:list --plain --context production

# list the production deploy context values in .env format
# and pipe results into a .env file
netlify env:list --plain --context production > .env
```

## Untrusted deploys and sensitive variables

If your project is connected to a public repository, Deploy Previews from forks are handled by your project's [untrusted deploys policy](/deploy/deploy-overview#untrusted-deploys-policy).

If your untrusted deploys policy is set to **Build without sensitive variables**, untrusted deploys build automatically, but variables identified as sensitive are not passed to the deploy environment. This means that extensions or integrations that rely on those variables may not work in these Deploy Previews. Learn more about the [untrusted deploys policy options](/deploy/deploy-overview#untrusted-deploys-policy).

You can adjust your project's code to accommodate builds without sensitive variables present, or you can set a [separate value for the `deploy-preview` deploy context](/build/environment-variables/overview#value-per-deploy-context) that's safe to expose publicly.

Netlify always treats an environment variable as sensitive if it's marked as **Contains secret values** (via the [Secrets Controller](/build/environment-variables/secrets-controller) feature). For variables not explicitly marked in this way, Netlify automatically attempts to detect if the variable is likely to hold a secret. 

Automatic detection looks at both the variable name (e.g., names including terms like `PASSWORD`, `TOKEN`, `SECRET`, `API_KEY`) and its value (e.g., values that match a known credential format such as AWS access keys).

Automatic detection is based on heuristics, so to make sure a value is always treated as sensitive, it's best to explicitly mark it as **Contains secret values**.

