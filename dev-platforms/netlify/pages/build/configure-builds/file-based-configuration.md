---
title: "Netlify File-Based Configuration"
source: https://docs.netlify.com/build/configure-builds/file-based-configuration.md
path: build/configure-builds/file-based-configuration
---

---
title: "File-based configuration"
description: "Use a netlify.toml configuration file to specify how the platform builds and deploys your project."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

In addition to using the Netlify UI to configure [build settings](/build/configure-builds/overview#build-settings), [deploy settings](/build/post-processing/overview/), and [environment variables](/build/environment-variables/overview), you can also configure many of these settings in a `netlify.toml` file.

### Caution - File-based configuration settings take precedence

Be aware that if you have conflicting configuration values, settings specified in `netlify.toml` override any corresponding settings in the Netlify UI.

The `netlify.toml` is a configuration file that specifies how Netlify builds and deploys your site - including redirects, branch and context-specific settings, and more. Its goal is to describe much of your project configuration alongside your code - with two goals:

- When someone forks your repository, they can instantly create a Netlify site using the new repo. They don't have to configure anything in the UI, and they'll still get an identical project configuration.
- You can track configuration changes using version control and configure some things that aren't customizable in our UI.

There are other ways to accomplish some of the things you would use the `netlify.toml` for. For example, you can use [`_headers`](/manage/routing/headers) and [`_redirects`](/manage/routing/redirects/overview) files to accomplish what the filename suggests, but having these settings all live in the same file can greatly simplify maintaining them.

There are also certain settings that you can only configure using the Netlify UI, CLI, or API. The `netlify.toml` file is not a fully comprehensive configuration method. 

### Tip - Declare environment variables in the Netlify UI for more options

While you can use `netlify.toml` to declare environment variables, we recommend that you use the [Netlify UI](/build/environment-variables/get-started/#create-environment-variables) to avoid storing sensitive values in your repository, and for the option to set [scopes](/build/environment-variables/overview#scopes), track changes in the [team audit log](/manage/accounts-and-billing/team-management/team-audit-log), and access values with the Netlify [CLI](/api-and-cli-guides/cli-guides/get-started-with-cli#manage-environment-variables) and [API](/api-and-cli-guides/api-guides/get-started-with-api#environment-variables).

The following sections will go through where to store the `netlify.toml`, each thing you'll be able to do in the file, and some examples that you could use in your code. For more information on TOML syntax, visit the [TOML website](https://toml.io/en/).

## File location

The `netlify.toml` is normally stored in the root of your site repository. You also have the option to include different configuration files in other directories for special cases such as [monorepos](/build/configure-builds/monorepos#use-a-netlify-configuration-file). 

If you store the Netlify configuration file in a directory other than the root, you will need to set either the [base directory](/build/configure-builds/overview#set-the-base-directory) or the [package directory](/build/configure-builds/overview#set-the-package-directory) to indicate where it is located. Learn more about [how Netlify searches for your configuration file](/build/configure-builds/monorepos#how-netlify-finds-your-configuration-files) in our monorepos doc.

## Configuration details

The following sections provide details for some commonly used configuration settings.

All paths configured in the `netlify.toml` should be absolute paths relative to the [base directory](/build/configure-builds/overview#definitions), which is the root by default (`/`).

### Build settings

The `[build]` command runs in the Bash shell, allowing you to add Bash-⁠compatible syntax to the command. Netlify also supports these properties (keys) for the `[build]` command:

- `base`: to specify the [base directory](/build/configure-builds/overview#definitions) 
- `publish`: to specify the [publish directory](/build/configure-builds/overview#definitions)
- `command`: to specify the [build command](/build/configure-builds/overview#definitions)
- `environment`: to declare [build environment variables](/build/configure-builds/environment-variables)
- `processing`: to configure [post-processing settings](#post-processing)

If a key has a list of key/value pairs as its value, you can set that key in its own block like this:

```toml
[build.environment]
  VARIABLE = "value"
```

### Ignore builds

Netlify tries to determine if there are any changes in the site's base directory by comparing the last known version of the files within that directory. If no change is detected, the build system skips the build, returning early from the build process.

To override the default check with a custom workflow, you can use the `ignore` attribute in `netlify.toml`. This allows you to specify a Bash or Node.js command to determine whether the site needs rebuilding or not.

Check out our [ignore builds](/build/configure-builds/ignore-builds) doc for more information on the default ignore behavior and details about constructing a custom `ignore` command.

### Build Plugins

Netlify [Build Plugins](/extend/install-and-use/build-plugins) extend the functionality of the build process. In addition to installing plugins through the 
### NavigationPath Component:

Project configuration > Build & deploy > Build plugins
 section in the Netlify UI, you can also add them to a site using [file-based installation](/extend/install-and-use/build-plugins#file-based-installation). Here's an example `[[plugins]]` section in `netlify.toml`:

```toml
[[plugins]]
package = "netlify-plugin-check-output-for-puppy-references"
  [plugins.inputs]
  breeds = ["pomeranian", "chihuahua", "bulldog"]
```

For more detailed information about installing and removing plugins, configuration options, and building and sharing different types of plugins, check out our [Build Plugins](/extend/install-and-use/build-plugins) docs.

### Extensions

Some [extensions](/extend/install-and-use/extensions-and-integrations/) run during the build-deploy lifecycle for a site - for example, to analyze your build or to inject edge functions and serverless functions. If you install an extension that runs during the build process, you can configure the extension in `netlify.toml` for the sites that use it. 

1. Follow the instructions to [install the extension](/extend/install-and-use/extensions-and-integrations/#install-an-extension) on your team.
2. Use `[[integrations]]` in your `netlify.toml` to configure the extension settings for each site that uses the extension. 

Here is an example:

```toml
[[integrations]]
  name = "abc-performance-extension"

  [integrations.config]
    output_path = "reports/performance-reports.html"
    fail_deploy_on_score_thresholds = "true"
  
  [integrations.config.thresholds]
    performance = 0.9
    accessibility = 0.9
    best-practices = 0.9
    seo = 0.9
    pwa = 0.9
```

The extension author defines the format of the configuration options you can provide in `netlify.toml`, so we recommend reviewing the extension's documentation for detailed instructions.

### Deploy contexts

Certain keys, such as `[build]` and `[[plugins]]` but not `[[redirects]]` or `[[headers]]`, allow you to set `[context]` properties based on the [kind of deploy](/deploy/deploy-overview#deploy-contexts). These keys are _context-aware_.

During a build, the following ordering determines which context covers a particular deploy:

- UI settings are overridden if a `netlify.toml` file is present and a setting for the same property/redirect/header exists in the UI and the TOML file.
- any property of a context-aware key, such as `[build]` or `[[plugins]]`, will be applied to all contexts unless the same property key is present in a more specific context.
- any property in `[context.production]`, `[context.deploy-preview]`, `[context.branch-deploy]`, or `[context.dev]` will override less specific contexts:
  - production - a deploy generated from the production branch set in the UI under 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Branches and deploy contexts

  - deploy-preview - a deploy generated from a pull request or merge request
  - branch-deploy - a deploy generated from a branch that is not your production branch
  - dev - local development environments run using [Netlify Dev](/api-and-cli-guides/cli-guides/local-development). Use `[context.dev]` to set environment variables and use the [`[dev]`](/build/configure-builds/file-based-configuration/#netlify-dev) section to configure all other local development properties.
- any property in `[context.branchname]`, for a given branchname, is the most specific, and thus overrides all the less specific contexts.

```toml
# Production context: all deploys from the Production branch
# set in your site's Branches settings in the UI will inherit
# these settings.
[context.production]
  publish = "output/"
  command = "make publish"

# Deploy Preview context: all deploys generated from
# a pull/merge request will inherit these settings.
[context.deploy-preview]
  publish = "dist/"
```

### Post processing

You can manage the Pretty URLs post processing setting with the `processing` property. 

#### Pretty URLs

This setting overrides the corresponding setting under 
### NavigationPath Component:

Project configuration > Build & deploy > Post processing > Pretty URLs
.

```toml
[build.processing.html]
  pretty_urls = true
```

### Redirects

You can manage your [redirects](/manage/routing/redirects/overview) directly in your `netlify.toml`. For each redirect you want to declare, add an entry with the `[[redirects]]` heading:

```toml
[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301
  force = false
  query = {path = ":path"} #  apply this rule for /old-path?path=example
  conditions = {Language = ["en","es"], Country = ["US"]}

[[redirects]]
  from = "/news"
  to = "/blog"
```

Here's a [proxy redirect](/manage/routing/redirects/rewrites-proxies#proxy-to-another-service):

```toml
[[redirects]]
  from = "/api/*"
  to = "https://us-central1-netlify-intercom.cloudfunctions.net/readHeaders/:splat"
  status = 200
  force = true
  conditions = {Role = ["admin", "cms"]}
  [redirects.headers]
    X-From = "Netlify"
    X-Api-Key = "some-api-key-string"
```

You can redirect your netlify subdomain to your custom domain. Note that the `force = true` is equivalent to the `!` (for [shadowing](/manage/routing/redirects/rewrites-proxies#shadowing) in the `_redirects` file:

```toml
[[redirects]]
  from = "https://somenetlifysite.netlify.app"
  to = "https://mycustomdomain.com"
  status = 301
  force = true
```

For more details on options to use with your redirects, review the [redirect options](/manage/routing/redirects/redirect-options) doc.

### Headers

You can define custom [headers](/manage/routing/headers) in `netlify.toml`. Here is an example of some headers you could configure:

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"

    #  Multi-value headers are expressed with multi-line strings
	cache-control = '''
	max-age=0,
	no-cache,
	no-store,
	must-revalidate'''

    # The Basic-Auth header may not be available on all plans.
    Basic-Auth = "someuser:somepassword anotheruser:anotherpassword"
```

By default, headers set in the `netlify.toml` are global for all builds and cannot be scoped for specific branches or deploy contexts. However, there is a workaround you can use to [set unique headers for each deploy context](/manage/routing/headers#custom-headers-for-different-branch-or-deploy-contexts).

### Functions

Although there are default settings for [Netlify Functions](/build/functions/overview) to help you get started, you can use the `[functions]` section in `netlify.toml` for optional, custom configuration.

The following property applies for all functions:

- **`directory`:** custom absolute path to your functions. The default location is `YOUR_BASE_DIRECTORY/netlify/functions`.

Meanwhile, the following properties apply only for functions written in TypeScript or JavaScript. You can set them for all functions in your project or filter them by name, including using [glob patterns](https://www.npmjs.com/package/glob#glob-primer). If a function matches several configuration blocks containing one of these properties, the values are concatenated.

- **`node_bundler`:** function bundling method used in [@netlify/zip-it-and-ship-it](https://github.com/netlify/zip-it-and-ship-it). Valid values:
  - **`esbuild`:** method that leverages [esbuild](https://esbuild.github.io/) to bundle functions, resulting in shorter bundling times and smaller artifacts. TypeScript functions always use `esbuild`.
  - **`zisi`:** default function bundling method for JavaScript functions.
- **`external_node_modules`:** list of Node.js modules that are copied to the bundled artifact without adjusting their source or references during the bundling process; only applies when `node_bundler` is set to `esbuild`. This property helps handle dependencies that can't be inlined, such as modules with native add-ons.
- **`included_files`:** list of additional paths to include in the function bundle. Although our build system includes statically referenced files (like `require("./some-file.js")`) by default, `included_files` lets you specify additional files or directories and reference them dynamically in function code. You can use `*` to match any character or prefix an entry with `!` to exclude files. Paths are absolute paths relative to the [base directory](/build/configure-builds/overview#definitions-1).

  For more context, check out our blog post about [including files in Netlify Functions](https://www.netlify.com/blog/2021/08/12/how-to-include-files-in-netlify-serverless-functions/) with caveats for the `esbuild` bundler.

```toml
[functions]
  # Sets a custom directory for Netlify Functions
  directory = "myfunctions/"

  # Specifies `esbuild` for functions bundling
  node_bundler = "esbuild"

  # Flags "package-1" as an external node module for all functions
  external_node_modules = ["package-1"]

  # Includes all Markdown files inside the "files/" directory.
  included_files = ["files/*.md"]

[functions."api_*"]
  # Flags "package-2" as an external node module for functions
  # with a name beginning with "api_". Functions matching this
  # pattern have both "package-1" and "package-2" as
  # external modules, because modules from this object
  # are concatenated with any from the top-level object.
  external_node_modules = ["package-2"]

  # Includes all Markdown files previously defined in the
  # top-level object, except for "post-1.md".
  included_files = ["!files/post-1.md"]

[functions.api_payment]
  # Flags "package-3" and "package-4" as external node modules
  # for a function named "api_payment".
  # This function has 4 external node modules:
  #  "package-1" from the top-level object
  #  "package-2" from the "api_*" object
  #  "package-3" and "package-4" from this object
  external_node_modules = ["package-3", "package-4"]

  # Includes all Markdown files inside "files/", except for
  # "post-1.md" (excluded in the "api_*" object)
  # and "post-2.md" (excluded in this object).
  # Also includes "package.json" and any files
  # inside "images/" or any of its subdirectories.
  included_files = ["!files/post-2.md", "package.json", "images/**"]
```

### Netlify Dev

[Netlify Dev](/api-and-cli-guides/cli-guides/local-development) uses [detectors](/api-and-cli-guides/cli-guides/local-development#project-detection) to enable a local development environment for most tools and frameworks without any additional setup.

You can use the `[dev]` section in `netlify.toml` for optional configuration. Note that `[dev]` doesn't run in the Bash shell, however, so you won't be able to use Bash-⁠compatible syntax with the command.

All paths configured in the `[dev]` section should be absolute paths relative to the [base directory](/build/configure-builds/overview#definitions), which is the root by default (`/`).

Netlify Dev also makes use of the [functions directory setting](#functions) to scaffold and serve your functions in a local development environment.

`[dev]` includes optional properties such as these:

- **`command`:** command that starts your development server or runs a command such as a compiler watch in the background. If no `targetPort` is specified, it runs the command in the background in addition to the static file server.
- **`port`:** port that Netlify Dev is accessible from in the browser.
- **`targetPort`:** port for your application server, framework, or site generator. If provided, the CLI will wait until the provided `targetPort` is reachable and then proxy requests to it. If you specify values for both `command` and `targetPort`, `framework` must be `#custom`.
- **`functionsPort`**: the port where Netlify Dev serves functions.
- **`publish`:** path to your static content folder.
- **`jwtRolePath`:** object path that points to role values for JWT-based redirects.
- **`jwtSecret`:** secret used to verify tokens for JWT-based redirects.
- **`autoLaunch`:** boolean value that determines whether Netlify Dev launches the local server address in your browser.
- **`framework`:** setting to use if a project is detected incorrectly, flagged by multiple detectors, or requires a `command` and `targetPort`. Valid values:
  - **`#auto`:** default, tests all available detectors.
  - **`#static`:** property that specifies a static file server.
  - **`#custom`:** property that uses the `command` value to run an app server and the `targetPort` value to connect to it. Required if `command` and `targetPort` are both set.
- **`https`:** property that specifies an SSL/TLS certificate and key file for the Netlify Dev local server. By default, Netlify Dev starts an HTTP server, but you can configure a certificate and key file if you require HTTPS. The `https` configuration is an object with the following properties:
  - **`certFile`:** path to the certificate file.
  - **`keyFile`:** path to the private key file.

Note that an **`environment`** property doesn't exist for `[dev]`. If you would like to set environment variables for use locally with the Netlify CLI, use [`context.dev`](/build/configure-builds/file-based-configuration#deploy-contexts) instead.

Here's an example `[dev]` section for Netlify Dev configuration overrides:

```toml
[dev]
  command = "yarn start"
  port = 8888
  targetPort = 3000
  publish = "dist"
  jwtRolePath = "app_metadata.authorization.roles"
  jwtSecret = "MY_JWT_SECRET_VALUE"
  autoLaunch = true
  framework = "#custom"
  [dev.https]
    certFile = "cert.pem"
    keyFile = "key.pem"
```

### Templates

While a template repository can make use of other `netlify.toml` settings, you can use the `[template]` section of a `netlify.toml` to provide template-specific configuration for [Deploy to Netlify buttons](/deploy/create-deploys#deploy-to-netlify-button).

```toml
[template]
  incoming-hooks = ["Contentful"]

[template.environment]
  SECRET_TOKEN = "change me for your secret token"
  CUSTOM_LOGO = "set the url to your custom logo here"
```

Visit our [template configuration](/deploy/create-deploys#template-configuration) docs to learn more about setting up templates and the configuration options in the example above.

## Inject environment variable values

Using environment variables directly as values in your `netlify.toml` isn't supported. For example, `key = "$VARIABLENAME"` will not inject `$VARIABLENAME`'s value into `netlify.toml`. One exception to this rule is [signed proxy redirects](/manage/routing/redirects/rewrites-proxies#signed-proxy-redirects).

For all other cases, you have two options for working with environment variable values in a file-based or programmatic way.

Note that if you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your environment variables, the scope must include **Builds** for the following options to work.

### Use a local build plugin

We recommend [creating a local build plugin](/extend/develop-and-share/develop-build-plugins#local-plugins) to use environment variable values in a programmatic way because it's the most versatile approach. It enables you to [read environment values](/extend/develop-and-share/develop-build-plugins#environment-variables) and change many aspects of your build configuration (including redirects and headers) through [the `netlifyConfig` object](/extend/develop-and-share/develop-build-plugins#netlifyconfig).

### Use the `[build]` command to substitute environment variable values

Substituting values using the `[build]` command in `netlify.toml` only works for the `[[headers]]` and `[[redirects]]` sections, as they are read after the build is complete. Note that substitutions made in the configuration file using this approach will not be available to build plugins, as build plugins run before the build command.

The [`[build]` command](/build/configure-builds/file-based-configuration/#build-settings) is a Bash command and so it has access to variables set in the build environment. You can use the following steps to substitute values in the file with environment variable values during the build step, **but only if you are changing headers or redirects**.

1. Add a placeholder like `HEADER_PLACEHOLDER` somewhere in the `[[headers]]` or `[[redirects]]` sections of your TOML file.
2. Create an environment variable, for example `PROD_API_LOCATION`, with the desired value in the Netlify UI.
3. Prepend a replacement `sed` command to your build command in `netlify.toml`. The `sed` command must use double quotation marks, not single ones. Here's an example for a site using `yarn build` to build:

   ```toml
   [build]
   command = "sed -i \"s|HEADER_PLACEHOLDER|${PROD_API_LOCATION}|g\" netlify.toml && yarn build"
   ```

## Sample `netlify.toml` file

This example `netlify.toml` demonstrates how you can combine multiple settings in a single file. It's not a comprehensive example of all available configuration options.

```toml
# Settings for the [build] key are global and are applied to
# all deploy contexts unless overridden by a context-specific setting.
[build]
  # Directory where the build system installs dependencies
  # and runs your build. Store your package.json, .nvmrc, etc here.
  # If not set, defaults to the root directory.
  base = "project/"

  # Directory that contains the deploy-ready HTML files and
  # assets generated by the build. This is an absolute path relative 
  # to the base directory, which is the root by default (/).
  # This sample publishes the directory located at the absolute 
  # path "root/project/build-output"

  publish = "build-output/"

  # Default build command.
  command = "echo 'default context'"

[[plugins]]
  # Installs the Lighthouse Build Plugin for all deploy contexts
  package = "@netlify/plugin-lighthouse"

# Production context: all deploys from the Production branch
# set in your site's Branches settings in the UI will inherit
# these settings. You can define environment variables
# here but we recommend using the Netlify UI for sensitive
# values to keep them out of your source repository.
[context.production]
  publish = "output/"
  command = "make publish"
  environment = { NODE_VERSION = "14.15.3" }

# Deploy Preview context: all deploys generated from
# a pull/merge request will inherit these settings.
[context.deploy-preview]
  publish = "dist/"

# Here is an example of how to define context-specific
# environment variables. To avoid committing sensitive
# values to public source repositories, set variables
# with the Netlify UI, CLI, or API instead.
[context.deploy-preview.environment]
  NOT_PRIVATE_ITEM = "not so secret"

# Branch Deploy context: all deploys that are not from
# a pull/merge request or from the Production branch
# will inherit these settings.
[context.branch-deploy]
  command = "echo branch"
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
[context.staging] # "staging" is a branch name
  command = "echo 'staging'"
  base = "staging"

# For contexts of branches with special characters,
# enclose the branch name with quotes.
[context."feat/branch"]
  command = "echo 'special branch'"
  base = "branch"

# Redirects and headers are GLOBAL for all builds - they do not
# get scoped to contexts no matter where you define them in the file.
# For context-specific rules, use _headers or _redirects files,
# which are PER-DEPLOY.

# A basic redirect rule
[[redirects]]
  from = "/*"
  to = "/blog/:splat"

# A redirect rule with many of the supported properties
[[redirects]]
  from = "/old-path"
  to = "/new-path"

  # The default HTTP status code is 301, but you can
  # define a different one.
  status = 302

  # By default, redirects won't be applied if there's a file
  # with the same path as the one defined in the `from` property.
  # Setting `force` to `true` will make the redirect rule
  # take precedence over any existing files.
  force = true

  # Redirect from /old-path?id=123 to /new-path.
  # Each combination of query params needs to be
  # defined in a separate [[redirects]] block.
  # More information at https://docs.netlify.com/manage/routing/redirects/redirect-options/#query-parameters
  query = {id = ":id"}

  # Redirect based on conditions including browser language,
  # geolocation, identity role, and/or cookie presence.
  conditions = {Language = ["en"], Country = ["US"]}

  # Sign each request with a value defined in an environment variable
  signed = "API_SIGNATURE_TOKEN"

  # You can also define custom headers within your redirects blocks.
  [redirects.headers]
    X-From = "Netlify"
    X-Api-Key = "some-api-key-string"

# Redirects for role-based access control don't use the 'to' property.
[[redirects]]
  from = "/gated-path"
  status = 200
  conditions = {Role = ["admin"]}
  force = true

# The following redirect is intended for use with most SPAs
# that handle routing internally.
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  # Define which paths this specific [[headers]] block will cover.
  for = "/*"

  [headers.values]
    X-Frame-Options = "DENY"
    Content-Security-Policy = "frame-ancestors https://www.facebook.com"

    # Multi-value headers are expressed with multi-line strings.
  cache-control = '''
  max-age=0,
  no-cache,
  no-store,
  must-revalidate'''

    # Basic-Auth allows you to password protect your whole site.
    # This feature may not be available on all plans.
    Basic-Auth = "someuser:somepassword anotheruser:anotherpassword"

[functions]
  # Directory with serverless functions, including background
  # functions, to deploy. This is an absolute path relative to the 
  # base directory, which is the root by default (/).
  directory = "functions/"

# Use [dev] to set configuration overrides for local
# development environments run using Netlify Dev - except
# for environment variables. Environment variables for Netlify
# Dev should be set under [context.dev.environment] instead.
[dev]
  command = "yarn start"
  port = 8888
  publish = "dist"

```

