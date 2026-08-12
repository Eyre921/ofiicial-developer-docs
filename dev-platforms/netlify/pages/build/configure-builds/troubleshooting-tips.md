---
title: "Netlify Build Troubleshooting"
source: https://docs.netlify.com/build/configure-builds/troubleshooting-tips.md
path: build/configure-builds/troubleshooting-tips
---

---
title: "Build troubleshooting tips"
description: "Find troubleshooting tips for failing builds, learn how to address certain build errors, and access additional support resources."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

This article provides troubleshooting tips for failing builds in Netlify's build service.

### Tip - Get suggested solutions for failed builds

To help you fix failed deploys, Netlify offers AI capabilities that diagnose and suggest solutions for deploy failures and build errors so you can get back to shipping code.

Learn more about Netlify's AI capabilities to [give solutions for failed deploys](/resources/troubleshooting/fix-a-failed-deploy/).

## Best practices for troubleshooting your build

In case your build fails on Netlify, **first make sure it builds locally in your own development environment.** This is a prerequisite to all of the below suggestions.

If your build works locally, **the next debugging step is to ensure the package versions we use to build match yours.** You can find the settings for these in the [dependency management](/build/configure-builds/manage-dependencies) doc. That's the leading cause of build failure.

Once you've considered the most frequently encountered issues listed below, there is some additional reading linked at the bottom of this article which may help you debug in more depth or find answers to less commonly asked questions.

To understand the available software and tools that Netlify supports during a build, check out the [available software at build time](/build/configure-builds/available-software-at-build-time).

## Command not found

If your build fails with `jekyll: command not found` or `gulp: command not found` or anything in that pattern, it means that the software required for that command hasn't been installed in your build.
You can tell the build system to install the software you need by including the proper configuration file, like a `Gemfile` for Ruby programs like `jekyll`, or `package.json` for Node programs like `gulp`.

Check out the [dependency management](/build/configure-builds/manage-dependencies) doc for more details on how to tell us to install your toolchain. Once we find your configuration file, we'll automatically use it before trying to run your build command.

Note that by default the build system looks for the configuration file in your site's [base directory](/build/configure-builds/overview#definitions), which is the **root of your repository** by default. If your configuration file is located in a subdirectory, you will need to change your folder structure or [set the site's package directory](/build/configure-builds/overview#set-the-package-directory) to specify the location.

## Unexpected 404 page errors

If your site unexpectedly serves a 404 page error, there can be several reasons why. For instance, if your geographic area or IP address is blocked from a site, then you will only see a Netlify-branded 404 page. Learn more about [Firewall traffic rules](/manage/security/secure-access-to-sites/traffic-rules).

For more possibilities and troubleshooting help, check out our verified [Support Forums guide on unexpected 404 page errors](https://answers.netlify.com/t/support-guide-i-ve-deployed-my-site-but-i-still-see-page-not-found/125).

## Build command named `build`

Don't name your build command `build` in our production build environment. This will fail and give you a strange build log.

## Build fails with `exit status 128`

Typically this means that we don't have permission to clone the repository you are trying to deploy. The usual cause for this is that someone made some changes to settings for the parent organization, or repository, some time after linking the repository to your site.

We only have permission to create a copy of your code when you link the repository. If you are seeing your build fail with `exit status 128` in the deploy log, relinking your repo using our UI is a good first attempt to fix things (go to 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Repository
, select **Manage repository**, then **Link to a different repository**). If you do this, please check your webhook settings at your Git provider to be sure you don't have any duplicate Netlify webhooks.

### Note - Permission levels

Your GitHub, GitLab, Bitbucket, or Azure DevOps user account may not have the privilege level required to link the repo to Netlify, even if you can log in and access it from the Git host's website. You generally need administrative privileges on the repository, owning organization, or both. Related: [documentation about repository permissions and linking]( /build/git-workflows/repo-permissions-linking).

## Build fails on warning message

In some cases, a build may fail due to a warning message that would not cause a build failure when run locally. This is because some libraries and build tools handle warnings differently when they detect that they are being run in a Continuous Integration (CI) environment.

Like many other CI tools and platforms, Netlify sets a build environment variable, `CI=true`, as a convention to indicate that your build is running in an automated environment. Many libraries use the presence of the `CI` variable to trigger changes in their behavior, such as removing progress spinner animations or user prompts. In some cases, a library may also choose to treat warning messages as errors, failing the build.

Generally, libraries that choose to fail on warnings presume their users will want to fix the issues causing the warnings. If this isn't practical for your use case, you can override the `CI` variable by adding `CI=''` to the beginning of your site [build command](/build/configure-builds/overview#build-settings). For example:

```
CI='' npm run build
```

### Caution

Though it seems like the logical opposite of `CI=true`, setting `CI=false` may not work as expected. This is because environment variable values are processed as strings, and many libraries interpret _any_ non-empty string value for `CI` as `true`.

## Build fails on peer dependency conflict

Due to [behavior in npm 8.60 through 8.12.1](https://github.com/npm/cli/issues/4998), you may find `Could not resolve dependency` or `Conflicting peer dependency` warnings in your Netlify deploy log that ultimately result in a failing build. This problem occurs mainly for sites using React 17 or later with Node 16.5.1 or later. To resolve this situation, set the `NPM_FLAGS` [environment variable](/build/configure-builds/environment-variables) to pass either `--force` or `--legacy-peer-deps` to the `npm install` command that Netlify runs at build time.

## Case sensitivity

If you develop on Windows or OSX, and your code includes something like `jQuery/jquery.js` - the Netlify build may fail as the file system used in Netlify builds is case sensitive while your build environment is not. The error messages that result may not clearly indicate this!

To effectively change case of a file stored in Git from your case insensitive local environment, it may be necessary to `git mv` or `git rm` and then add the file again, as renaming and committing will not have the desired effect.

## Large files or sites

Files over 10 MB in size are not well-supported by our CDN and may fail to upload to our system, causing your entire deploy to fail. You should host large content elsewhere, such as YouTube embedded videos.

Sites with tens of thousands of html files can lead to long processing times. This shouldn't cause the deploy to fail, but even a "quick" manual deploy can take quite awhile (many minutes) to finish if you have tens of thousands of files.

## Post processing

There are some situations during build that may lead to a failure in post processing - many things that fail will lead to a retry; if after 4 retries it still hasn't worked, we fail the deploy. You'll probably need to [contact support](https://www.netlify.com/support/) in this case to get more details about the error.

**Redirects or Custom header rules** that we can't process at all are mentioned near the end of the build log and in the Deploy Summary for a deploy, but will **not** cause the build or deploy to fail.

## Build cache

In order to make builds run faster, we cache certain directories created when we [install your dependencies](/build/configure-builds/manage-dependencies#dependency-cache). You can check which directories are cached by searching for `$NETLIFY_CACHE_DIR` in the `run-build-functions.sh` file for your site's selected [build image](/build/configure-builds/overview#build-image-selection).

If a build fails, it's worth retrying with a cleared build cache to check if this works better. You can do this by [deploying the latest branch commit](/deploy/manage-deploys/manage-deploys-overview#retry-deploy-from-latest-branch-commit) with the "Retry without cache" option.

### Build cache key behavior

Netlify's build cache behavior follows specific rules based on whether you're deploying to your project's [production branch](/deploy/deploy-overview#definitions) or other branches:

- For a deploy to your project's [**production branch**](/deploy/deploy-overview#definitions), Netlify loads only the production branch build cache.
- For a [**branch deploy**](/deploy/deploy-types/branch-deploys/), Netlify loads a build cache unique to that branch. If no cache entry is found, Netlify loads the production branch build cache as a fallback.
- For a [**Deploy Preview**](/deploy/deploy-types/deploy-previews/), a build cache unique to the corresponding pull/merge request is loaded. If no cache entry is found, Netlify loads the production branch build cache as a fallback.

Netlify will load your project's _production branch cache_ as a starting point if you open a new branch deploy or Deploy Preview since these deploys won't have their own cache yet. Once your first Deploy Preview or branch deploy is successful, Netlify creates a new dedicated cache and all subsequent deploys will load this new cache.

## Enqueued builds

Builds may be enqueued for any of the three reasons described below. Visit our Forums for a verified Support Guide on reducing build queueing by [optimizing _what_ you build](https://answers.netlify.com/t/common-issue-how-can-i-optimize-my-netlify-build-time/3907).

- **System queue.** Builds enter a system queue when the number of builds across all customers exceeds the current capacity on the build network. This triggers an increase in system capacity, so enqueued builds may start building as capacity increases as well as when other builds complete. To learn how to reduce your team's exposure to system build queues, [contact sales](https://www.netlify.com/contact/).
- **Team queue.** Builds enter your team queue when the number of concurrent builds across all sites on your team exceeds your team's build capacity. (If you have a legacy plan, learn more about [builds usage](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-for-legacy-plans/#builds-usage).) Such builds appear in your team's [**Builds** page](/manage/monitoring/monitor-builds) with the label: **Enqueued: Awaiting Capacity**. You can select the **Manage build capacity** button on that page to increase team build capacity. If you have a build that you'd like to build right away, you can [prioritize](/manage/monitoring/monitor-builds#prioritize-a-build) it. _(This feature is available on Enterprise [plans](https://www.netlify.com/pricing/).)_ You can also [cancel](/deploy/manage-deploys/manage-deploys-overview#cancel-a-deploy) unneeded team builds to move other builds up in the queue.
- **Context queue.** When multiple builds are triggered on the same site, in an _identical_ [deploy context](/deploy/deploy-overview#deploy-contexts) (such as the same Deploy Preview number, or the same branch deploy) these builds enter a context queue to ensure they complete sequentially. When the current build completes, the newest enqueued build of identical context begins, skipping any others in the same context queue. To start the newest enqueued build in a given context, you can [cancel](/deploy/manage-deploys/manage-deploys-overview#cancel-a-deploy) the current active build of identical context.

## Organization-owned private repository

If you have a Core Starter plan site connected to an organization-owned private GitHub repository, your builds will fail. You can resume deploys by taking one of these steps:

- [Upgrade your team plan](/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-for-legacy-plans#team-plans-and-usage).
- Deploy manually using the [CLI](/deploy/create-deploys#netlify-cli), [API](/api-and-cli-guides/api-guides/get-started-with-api#deploy-with-the-api), or [drag and drop](/deploy/create-deploys#drag-and-drop). You can [unlink the repository]( /build/git-workflows/repo-permissions-linking#unlink-a-git-repository) from your site to remove UI warnings and enable drag and drop.
- [Transfer the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository#transferring-a-repository-owned-by-your-organization) to a GitHub personal account.
- [Change the repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility) to public.

If you change your GitHub repository settings, you must push a commit for Netlify to receive the new settings in the triggered deploy hook.

## Error: `Uncaught SyntaxError: Unexpected token`

The `Uncaught SyntaxError: Unexpected token` error most commonly happens when your site's code refers to an asset that's no longer available.

If your SPA (single-page application) uses code splitting or hashed filenames with our atomic deploys, filename changes may break asset references on your site and result in this error.

To ensure your assets work across deploys, consider disabling hashed filenames, using permalinks, or using a service worker. For more details and solutions, check out our [official Support Guide on handling code-splitting issues on Netlify](https://answers.netlify.com/t/support-guide-handling-code-splitting-issues-on-netlify/113158).

## Error: `Page not found`

If your site returns a `Page not found` error after you've deployed, then we recommend you  check your deploy settings in the Netlify UI to confirm if you are publishing your site from the right folder. 

For your site, go to 
### NavigationPath Component:

Configuration > Build & deploy > Build settings
.

For more troubleshooting help, check out our [official Support Guide for the `Page not found` error](https://answers.netlify.com/t/support-guide-i-ve-deployed-my-site-but-i-still-see-page-not-found/125/2).

## More resources

If your issue doesn't seem to be addressed above, you can visit our [Support Forums](https://answers.netlify.com/categories) to browse posts about common issues or start a new discussion. You can also visit our [compilation of verified Support Guides on builds and deploys](https://answers.netlify.com/t/support-guide-compiled-build-and-deploy-resources-start-here/50679).

Many questions about specific build scenarios have also been [asked and answered on StackOverflow](https://stackoverflow.com/questions/tagged/netlify).

