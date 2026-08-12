---
title: "Hugo framework on Netlify"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/hugo.md
path: build/frameworks/framework-setup-guides/hugo
---

---
title: "Hugo on Netlify"
description: "Learn about Hugo on our platform. Manage your Hugo version and themes to ensure they work optimally with our platform."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Hugo is a fast and flexible open source static site generator written in Go.

## Key features

These features provide important benefits for Hugo sites, including ones built and deployed with Netlify.

- **Build speed.** Hugo boasts near-instant build times of less than one millisecond per page. For large sites with a lot of pages, this can translate into significant time savings during site development and Netlify build and deploy processes.
- **Choice of themes.** The Hugo ecosystem includes a wide range of premade [themes](https://themes.gohugo.io/) for styling static content.
- **Robust templating.** Hugo uses Go templates with `html/template` and `text/template` libraries to control templating.
- **Instant previews.** The [LiveReload](https://gohugo.io/getting-started/usage/#livereload) tool is integrated into Hugo for a hot reloading experience during development.
- **URL management.** Hugo has built-in support for [URL manipulations](https://gohugo.io/content-management/urls/) and [redirects](https://gohugo.io/content-management/urls/#aliases). 
- **Functions and variables.** When building out templates, you can use Go functions, built-in [Hugo-specific functions](https://gohugo.io/functions/), and a variety of [variables](https://gohugo.io/variables/).

## Netlify integration

Hugo sites on Netlify can benefit from automatic framework detection and control over Hugo version selection. They also require theme setup considerations.

### Automatic framework detection

When you [link a repository](/manage/projects/add-new-project/#import-from-an-existing-repository) for a project, Netlify tries to detect the framework your site is using. If your site is built with Hugo, Netlify provides a suggested build command and publish directory: `hugo` and `public`. If you're using the CLI to run [Netlify Dev](/api-and-cli-guides/cli-guides/local-development) for a local development environment, Netlify also suggests a dev command and port: `hugo server -w` and `1313`. You can override suggested values or set them in a configuration file instead, but automatic framework detection may help simplify the process of setting up a site on Netlify.

For manual configuration, check out the [typical build settings](/build/frameworks/overview#hugo) for Hugo.

### Hugo version

In order to install Hugo on the [build image](/build/configure-builds/overview#build-image-selection), you will need to set a `HUGO_VERSION` environment variable. You can set the variable to the version string for any released version after 0.19, for example, `0.80.0`.

1. First, confirm your local Hugo version with `hugo version`.

2. Then add an [environment variable](/build/environment-variables/overview) in the Netlify UI as you set up your site or in a [Netlify configuration file](/build/configure-builds/file-based-configuration) stored in your repository. 
    - Follow the steps to [import from an existing repository](/manage/projects/add-new-project/#import-from-an-existing-repository) and on the **Configure site and deploy** step, select **Add environment variables**. Select **New variable** and then enter the key and value. 
    ![](/images/integrations-frameworks-hugo-build-settings.png)
    - Alternatively, add the following to `netlify.toml` in your site's [base directory](/build/configure-builds/overview#definitions-1), where `YOUR_HUGO_VERSION` is a version string such as `0.80.0`.
      ```toml
      [build]
        command = "hugo"
        publish = "public"

      [build.environment]
        HUGO_VERSION = "YOUR_HUGO_VERSION"
      ```

### Tip - Failed build?

If you get an error with `exit code: 255` when building a Hugo site on Netlify, remember to set `HUGO_VERSION` to the version you are using locally.

### Hugo themes

Hugo themes work by default on Netlify. Like any continuous integration system, however, Netlify can't use a theme installed by the `git clone` method. Instead, you should install a Hugo theme for your site as a [git submodule](https://git-scm.com/docs/gitsubmodules).

Here's an example:
```sh
cd YOUR_PROJECT_DIRECTORY
git init
git submodule add https://github.com/THEME_CREATOR/THEME_NAME
```

## More resources

- [Typical Hugo build settings](/build/frameworks/overview#hugo)
- [Host Hugo on Netlify](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)
- [Hugo documentation](https://gohugo.io/documentation/)

