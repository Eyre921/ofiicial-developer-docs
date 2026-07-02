---
title: "Netlify SPA Build Configurations"
source: https://docs.netlify.com/build/configure-builds/javascript-spas.md
path: build/configure-builds/javascript-spas
---

---
title: "JavaScript SPAs"
description: "Access common build configuration information for JavaScript single-page applications (SPAs) on our platform."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Netlify supports many frameworks and project architectures. On this page, you'll find generic common configuration information for JavaScript single-page applications (SPAs). For framework-specific configurations, refer to our [frameworks page](/build/frameworks/overview).

## Build configuration for JavaScript SPAs

Most SPAs declare a build command in the `scripts` array of the project's `package.json` file. To run this script in Netlify, set the **Build command** to `npm run YOUR_BUILD_SCRIPT` or `yarn YOUR_BUILD_SCRIPT`, depending on your chosen [JavaScript dependency manager](/build/configure-builds/manage-dependencies#javascript-dependencies).

The **Publish directory** for single-page apps is often called `dist` but varies by framework and build tool. You can check the framework documentation, or try running the build script locally, then check what folder was created as a result.

> **Avoid 404s for SPAs:** If your project is a single page app (SPA) that uses the history `pushState` method to get clean URLs, you must add a [rewrite rule](/manage/routing/redirects/rewrites-proxies/#history-pushstate-and-single-page-apps) to serve the `index.html` file no matter what URL the browser requests.

## Code splitting or hashed filenames

If your SPA (single-page application) uses code splitting or hashed filenames with our atomic deploys, filename changes may break asset references on your site and result in an `Uncaught SyntaxError: Unexpected token` error. 

To ensure your assets work across deploys, consider disabling hashed filenames, using permalinks, or using a service worker. For more details and solutions, check out our [official Support Guide on handling code-splitting issues on Netlify](https://answers.netlify.com/t/support-guide-handling-code-splitting-issues-on-netlify/113158).

## More build configuration resources

- [Common framework configurations](/build/frameworks/overview)
- [Monorepos](/build/configure-builds/monorepos)
- [Ignore builds](/build/configure-builds/ignore-builds)

