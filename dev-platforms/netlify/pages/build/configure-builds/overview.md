---
title: "Netlify Build Configuration"
source: https://docs.netlify.com/build/configure-builds/overview.md
path: build/configure-builds/overview
---

---
title: "Build configuration overview"
description: "Configure build settings for a repository that uses continuous deployment, and understand build image options for your site."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Netlify lets you link a GitHub, GitLab, Bitbucket, or Azure DevOps repository to a site for [continuous deployment](/deploy/create-deploys#deploy-with-git). Each time you push to your Git provider, Netlify runs a build with your tool of choice and deploys the result to our powerful CDN.

![Simple workflow diagram with words "start, build, deploy, manage, extend" with build highlighted](/images/simplified-start-build-deploy-manage-extend-diagram-with-build-highlighted.png)

## Build settings

With continuous deployment configured, you can specify how Netlify will build your site. You can specify these settings when you first [add your site from an existing repository](/start/quickstarts/deploy-from-repository/) and anytime afterwards by going to 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
.

### Tip - Missing Build settings?

If **Build settings** aren't available for your site, you may not have continuous deployment set up. You can [link a Git repository]( /build/git-workflows/repo-permissions-linking#link-a-git-repository) to enable continuous deployment and access these settings.

For basic project configurations, you may need to [set the build command](#set-the-build-command) and [publish directory](#set-the-publish-directory). For more advanced configurations, such as sites that build from a subdirectory of a repository or a monorepo, you may also need to [set the base directory](#set-the-base-directory) and [package directory](#set-the-package-directory).

If Netlify automatically detects that your site is a monorepo or uses a framework that Netlify is able to identify, Netlify will automatically fill in some of these configuration fields for you when you first [create your site](/manage/projects/add-new-project/). You can update the fields afterwards as needed. Learn more about [commonly used build settings for frameworks](/build/frameworks/overview) and how to [configure sites from monorepos](/build/configure-builds/monorepos).

For public repositories, you can also toggle your deploy log visibility. With continuous deployment, builds are active by default. You can [stop or activate builds](/build/configure-builds/stop-or-activate-builds) at will for more control of your workflow.

![](/images/configure-builds-edit-build-settings-ui.png)

You can also specify some of these build settings and others in a [configuration file](/build/configure-builds/file-based-configuration), which allows you to change your settings depending on the [deploy context](/deploy/deploy-overview#deploy-contexts). For an example, refer to this [sample `netlify.toml` file](/build/configure-builds/file-based-configuration#sample-netlify-toml-file) that illustrates how to configure some of the available build settings. The configuration file settings override build settings specified in the UI.

### Definitions

The following definitions highlight terms related to build configuration. For definitions regarding branches and site deploys, visit the [site deploys overview](/deploy/deploy-overview#definitions).

- **Base directory:** directory where Netlify checks for [dependency management](/build/configure-builds/manage-dependencies/) files such as `package.json` or `.nvmrc`, installs dependencies, and runs your build command. The build system will use this directory to perform caching during the build process. If not set, the base directory defaults to the root of the repository. 
- **Site files:** source files in your repository that represent the code for your site and any related configurations. Also known as your site's package. 
- **Package directory:** typically used for monorepos, the directory that contains your site files, including the `netlify.toml`. Set this only if the location is different from the base directory. Learn more about how Netlify searches for your [configuration files in monorepos](/build/configure-builds/monorepos/#how-netlify-finds-your-configuration-files). 
- **Build command:** the command to run to build your site if you are using a static site generator or other build tool. For example, `npm run build`. The build command runs in the Bash shell, allowing you to add Bash-⁠compatible syntax to the command. Visit the [frameworks](/build/frameworks/overview) doc to learn about typical build commands for popular tools.
- **Publish directory:** directory that contains the deploy-ready HTML files and assets generated by the build. The directory is relative to the base directory, which is root by default (`/`). Visit the [frameworks](/build/frameworks/overview) doc to learn about typical publish directories for popular tools.
  > **Note - Only files in the publish directory are deployed:** Files and assets located outside of the publish directory won't be included in site deploys.
- **Functions directory:** directory that contains function files and optional subdirectories for organizing function files. Netlify will access the functions directory during every build, preparing and deploying each supported code file as a function. Default is `netlify/functions`. The functions directory is relative to the base directory. 
- **Netlify configuration file:** optional configuration file (`netlify.toml`) that specifies how Netlify builds and deploys your site - including redirects, branch and context-specific settings, and more. Learn more about [file-based configuration](/build/configure-builds/file-based-configuration/).   
- **Deploy log visibility:** privacy level for the [deploy logs](/deploy/deploy-overview#deploy-log) for a site linked to a public repo. The default setting **Public logs** makes deploy logs available to anyone with a deploy detail URL. You can limit deploy log access to site members by selecting **Private logs**.
- **Active builds:** used to indicate when [builds are active](/build/configure-builds/stop-or-activate-builds). Netlify builds your site according to your continuous deployment settings when you push to your Git provider.
- **Stopped builds:** used to indicate when [builds are stopped](/build/configure-builds/stop-or-activate-builds#stop-builds). Netlify will never build your site. You can [build your site locally](/api-and-cli-guides/cli-guides/get-started-with-cli#run-builds-locally) instead using Netlify CLI and then publish new deploys manually [with the CLI](/api-and-cli-guides/cli-guides/get-started-with-cli#manual-deploys) or [the API](/api-and-cli-guides/api-guides/get-started-with-api#deploy-with-the-api).

### Set the build command 

You can manually set the [build command](#definitions) in the following ways:

- in the Netlify UI, when you select **Add new project**. For an existing site, you can update the setting at 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
.
 - in a [Netlify configuration file](/build/configure-builds/file-based-configuration/#build-settings). Use the `command` property under `[build]` settings. Learn more about [file-based configuration](/build/configure-builds/file-based-configuration/).
 - using [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli/) when setting up continuous deployment for a site. 

To find the typical build command for your framework, refer to the [frameworks](/build/frameworks/overview) doc.

### Set the publish directory

You can manually set the [publish directory](#definitions) in the following ways:

- in the Netlify UI, when you select **Add new project**. For an existing project, you can update the setting at 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
.
 - in a [Netlify configuration file](/build/configure-builds/file-based-configuration/#build-settings). Use the `publish` property under `[build]` settings. Learn more about [file-based configuration](/build/configure-builds/file-based-configuration/).
 - using [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli/) when setting up continuous deployment for a site. 

 To find the typical publish directory for your framework, refer to the [frameworks](/build/frameworks/overview) doc. 

### Set the base directory

If not explicitly set, the [base directory](#definitions) defaults to the root of the repository. If you want to install dependencies and build your site in a subdirectory rather than root, you can specify this by setting a base directory.

You can set a base directory in the following ways:

 - in the Netlify UI, when you select **Add new project**. For an existing site, you can update the setting at 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
.
 - in a [Netlify configuration file](/build/configure-builds/file-based-configuration/#build-settings) stored at the root of your repository. Use the `base` property under `[build]` settings, and Netlify will use that value to set the base directory when you first set up the site.
 - if you're creating a [Deploy to Netlify](/deploy/create-deploys/#deploy-to-netlify-button) button for other people to easily clone and deploy your site, use the [`base` query parameter](/deploy/create-deploys/#set-a-base-directory-for-monorepos) to set the base directory for that button. You can create different buttons for each site in your monorepo by setting a different `base` value for each button.

A base directory specified in a root-level `netlify.toml` overrides the UI setting. 

### Set the package directory 

If you use a [monorepo](/build/configure-builds/monorepos/) and store your [site files](#definitions) in a different directory from your base directory, you can specify the location using the **Package directory** field in the Netlify UI. 

This is helpful if you want to install dependencies and run builds in the root but want to store your site's source files, including the  corresponding `netlify.toml`, in separate project directories. If you don't set this value, Netlify will [search for the `netlify.toml`](/build/configure-builds/monorepos/#how-netlify-finds-your-configuration-files) in the base and root directories.

In addition, if you don't [set an explicit publish directory](#set-the-publish-directory), Netlify uses the package directory to search for the directory that contains the output of your build (for example, a `dist` folder) and any related `_headers` and `_redirects` files within that directory.

To set the package directory for a site:

1. Navigate to 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build settings
. 
2. Select **Configure**.
3. Enter the **Package directory**. For example, `/packages/website`.
4. Select **Save**.

## Recommendations for specific setups

Consider the following suggestions based on your project configuration. 

- If your repository contains only the site you want to deploy, stored in the repository root, Netlify will automatically detect the build settings for you. In most cases, you can proceed with these default settings. But, if you do need to manually configure any settings, these would likely be the [build command](#set-the-build-command) and the [publish directory](#set-the-publish-directory).
- If your site is a [monorepo](/build/configure-builds/monorepos), Netlify will automatically detect each site directory in your repository and configure the build settings automatically based on the site you select. But, you also have the option to manually configure the build settings. For monorepos, this will include setting the [package directory](/build/configure-builds/monorepos#set-the-package-directory). Refer to our documentation on the [recommended monorepo setup](/build/configure-builds/monorepos#recommended-monorepo-setup) to learn more.
- If you have a larger repository that includes more than just your site files, you may need to deploy a self-contained site or monorepo workspace from a specific subdirectory. For example, a documentation site from the `/docs` subdirectory of your Python library. Or, a monorepo workspace set up in a `/frontend` subdirectory. To work from a specific subdirectory, update the [base directory](#set-the-base-directory). The [publish directory](#definitions) is relative to the base directory by default.

For larger repositories and monorepos, note that you can customize the default [ignore builds](/build/configure-builds/ignore-builds) behavior to determine whether or not your site builds as changes are made.

## Build image selection
 
When a build is triggered on Netlify, our build system starts a virtual machine from a build image. The build image is a snapshot of an operating system that has [various software tools and other settings](/build/configure-builds/available-software-at-build-time) preinstalled and configured.

Although all new Netlify sites use a default build image, you may be able to select from multiple images with different operating system and software versions. You might choose a different build image to meet a software requirement for your build tool, to try out experimental pre-release build features, or to keep up-to-date with the included operating system environment. Build image selection also enables Netlify to release breaking changes into the build image while allowing you to accommodate those changes with time to upgrade.

We recommend upgrading to the most recent build image regularly to take advantage of the latest features and security enhancements.

To change the build image for a site, go to 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build image selection
, and select the build image you would like to use. Our build system will use this image for all production deploys, branch deploys, and Deploy Previews.

### Build image defaults and project dependencies

Each build image has a set of [software with pre-defined default versions](/build/configure-builds/available-software-at-build-time). You can [customize these defaults](/build/configure-builds/manage-dependencies).

During your project's first build, we pin a version of [Node](/build/configure-builds/manage-dependencies#node-js-and-javascript), [Ruby](/build/configure-builds/manage-dependencies#ruby), [Go](/build/configure-builds/manage-dependencies#go), and [Yarn](/build/configure-builds/manage-dependencies#yarn) that matches the default version installed on the build image. These pinned versions are stored in your project's repository object, associating those pinned versions with your project's Git repository. This ensures your project's software versions will not be affected if the build image's defaults change.

## More build configuration resources

- [Common framework configurations](/build/frameworks/overview)
- [Monorepos](/build/configure-builds/monorepos)
- [JavaScript SPAs](/build/configure-builds/javascript-spas)
- [Ignore builds](/build/configure-builds/ignore-builds)
- [Manage build dependencies](/build/configure-builds/manage-dependencies)
- [Build environment variables](/build/configure-builds/environment-variables)
- [File-based configuration](/build/configure-builds/file-based-configuration)
- [Example `netlify.toml` file](/build/configure-builds/file-based-configuration#sample-netlify-toml-file)
- [On-demand Builders](/build/configure-builds/on-demand-builders)
- [Build hooks](/build/configure-builds/build-hooks)
- [Stop or activate builds](/build/configure-builds/stop-or-activate-builds)
- [Build troubleshooting tips](/build/configure-builds/troubleshooting-tips)
- [Available software at build time](/build/configure-builds/available-software-at-build-time)
- [Private Connectivity](/manage/security/private-connectivity)
- [Compiled build and deploy resources - start here!](https://answers.netlify.com/t/support-guide-compiled-build-and-deploy-resources-start-here/50679)
