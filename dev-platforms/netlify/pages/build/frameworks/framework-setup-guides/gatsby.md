---
title: "Gatsby on Netlify"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/gatsby.md
path: build/frameworks/framework-setup-guides/gatsby
---

---
title: "Gatsby on Netlify"
description: "Learn about Gatsby on our platform. Use the Gatsby adapter for Netlify or the Essential Gatsby build plugin to extend your Gatsby application."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Gatsby is a React-based, open source static site generator that pulls in data using a GraphQL API layer that can connect to a wide array of content sources.

## Key features

These Gatsby features provide key benefits for sites and apps, including ones built and deployed with Netlify.

- **Content aggregation.** Gatsby provides a diverse ecosystem of data plugins that allow developers to use a centralized GraphQL API to pull in content from files, APIs, and SaaS platforms. This makes development feel familiar, even if content sources are completely different.

- **Performance optimizations.** By default, Gatsby optimizes JavaScript bundles, adds preloading and browser optimizations, and includes other performance enhancements. In general, Gatsby sites are performant and fast.

- **Image optimization.** Gatsby ships an image component that works with the GraphQL data layer to generate highly optimized images. The images are lazy-loaded and configured for different viewport sizes. This cuts down on page load times and bandwidth usage. You can also use [Netlify Image CDN with Gatsby](/build/frameworks/framework-setup-guides/gatsby/?gatsby-version=adapters#netlify-image-cdn) for deferred image resizing instead of processing images at build time.

- **Serverless functions.** Gatsby includes an integrated [Functions](https://www.gatsbyjs.com/docs/reference/functions/) feature to help create an API for a site or application.

- **Server-side rendering (SSR) and deferred static generation (DSG).** You can choose between several rendering modes, including SSR and DSG. This means you can pick the rendering mode that makes sense for your site.

## Netlify integration

## Facet Switcher

Choose your Gatsby version:

### Available Tabs:

#### Adapters Tab

When you trigger a build on Netlify for a site that uses Gatsby version 5.12.0 or later, Gatsby detects that you are using Netlify and automatically installs `gatsby-adapter-netlify`. This is a Gatsby adapter that enables [zero-configuration deployments](https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting/zero-configuration-deployments/), making it easier to build and deploy your Gatsby sites. The same automatic detection and installation occurs when you trigger a build using the Netlify CLI.

You can also choose to [install the adapter yourself](https://github.com/gatsbyjs/gatsby/tree/master/packages/gatsby-adapter-netlify).

Note that if your site already uses the [Gatsby adapter for Netlify](#gatsby-adapter-for-netlify), you don't have to use the [Essential Gatsby build plugin](https://github.com/netlify/netlify-plugin-gatsby).

### Caution - Gatsby 5 requires updated Node.js version

[Gatsby 5](https://www.gatsbyjs.com/gatsby-5/) requires Node.js 18. If your build is using another Node.js version, [follow our Node.js docs](/build/configure-builds/manage-dependencies#node-js-and-javascript) to manually set the Node.js version to 18.

### Gatsby adapter for Netlify

The official Gatsby adapter for Netlify, `gatsby-adapter-netlify`, enables [zero-configuration deployments](https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting/zero-configuration-deployments/) for your site. When you trigger a build on Netlify for a site that uses Gatsby version 5.12.0 or later, Gatsby automatically installs the adapter. The adapter prepares your site for deployment on Netlify in a number of ways, including:

- Applying HTTP headers to assets
- Applying redirects and rewrites
- Applying trailing slash behavior to URLs
- Setting up user-defined API functions to be used on Netlify
- Setting up Deferred Static Generation (DSG) and Server-Side Rendering (SSR)
- Storing Gatsby cache after build is complete and restoring it on subsequent builds to decrease build time between builds

For more information on adapters, including information on how to create your own, visit [Gatsby's documentation on adapters](https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting/adapters/).

#### Install the Gatsby adapter for Netlify

Gatsby will automatically install `gatsby-adapter-netlify` for new Gatsby sites on Netlify. If you want to install the adapter manually, you can use the use the following command:

```shell
  npm install gatsby-adapter-netlify
```

If you want to further configure the adapter, you can add `gatsby-adapter-netlify` to your `gatsby-config.js` file and configure the `adapter` option. For example:

```js
const adapter = require("gatsby-adapter-netlify");

module.exports = {
  adapter: adapter({
    excludeDatastoreFromEngineFunction: false
  })
};
```

For more information, visit the [`gatsby-adapter-netlify` docs](https://github.com/gatsbyjs/gatsby/tree/master/packages/gatsby-adapter-netlify).

#### Limitations

`StaticImage` and `gatsby-transformer-sharp` don't work properly for SSR or DSG pages. Instead, you can host your images on a CDN such as [Cloudinary](https://www.gatsbyjs.com/docs/how-to/images-and-media/using-cloudinary-image-service/) or [imgix](https://github.com/imgix/gatsby).

#### Auto-generated Netlify Functions

To support Gatsby Functions and SSR/DSG render modes, the Gatsby adapter automatically generates Netlify Functions called `SSR` and `DSG`. If your site doesn't have Gatsby Functions or SSR/DSG pages, then the Netlify Functions won't be generated.

#### Optional loading of the Gatsby datastore from the CDN

By default, Netlify includes the Gatsby datastore in the Netlify Function bundle, which is a deployment package that's zipped for direct upload to AWS. If you have a larger site, the site's datastore may exceed the [maximum function deploy size](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#function-configuration-deployment-and-execution), preventing you from successfully deploying your website.

`GATSBY_EXCLUDE_DATASTORE_FROM_BUNDLE` is an environment variable that loads the Gatsby datastore from the CDN rather than bundling it with the function, bypassing the size limitation.

Note that enabling loading the datastore from the CDN results in different page load behavior. On the first load of  functions that handle SSR and DSG pages, the datastore is downloaded, which can result in a slower initial page load. 

During the build process, pre-warm requests are sent to the SSR and DSG function endpoints to reduce the user-facing impact of the datastore download.

#### Local development

When developing Gatsby Functions, you can use the built-in `gatsby develop` functions server. However, if you want to run the Netlify Functions that are generated during the build step, you can use [`netlify dev`](/api-and-cli-guides/cli-guides/local-development/). Make sure to run `netlify build` first to generate the Netlify Functions from your Gatsby Functions.

### Suggested configuration values

When you link a repository for a Gatsby project, Netlify provides a suggested build command and publish directory: `gatsby build` and `public`.

If you're using the CLI to run [Netlify Dev](/api-and-cli-guides/cli-guides/local-development/) for a local development environment, Netlify suggests a dev command and port: `gatsby develop` and `8000`.

You can override suggested values or set them in a configuration file instead, but suggested values from automatic framework detection may help simplify the process of setting up a Gatsby site on Netlify.

For manual configuration, check out the [typical build settings](/build/frameworks/overview#gatsby) for Gatsby.

### Environment variables

Environment variables prefixed with `GATSBY_` are processed by Gatsby and made available in the browser for client-side JavaScript access. For more information on how to use environment variables in Gatsby, including with SSR or DSG pages, check out the [Environment variables and frameworks doc](/build/frameworks/use-environment-variables-with-frameworks).

<div class="legacy-anchor" id="gatsby-image-cdn-on-netlify">

#### Essential Tab

When you [link a repository](/manage/projects/add-new-project/#import-from-an-existing-repository) for a project, Netlify detects the framework your site is using. If you are using Gatsby version 5.11.0 or earlier, Netlify will automatically install the [Essential Gatsby build plugin](#essential-gatsby-build-plugin) and provides [suggested configuration values](#suggested-configuration-values-2). For existing sites already linked to Netlify, you can choose to [install](http://app.netlify.com/plugins/@netlify/plugin-gatsby/install) the plugin yourself.

### Caution - Gatsby 5 requires updated Node.js version

[Gatsby 5](https://www.gatsbyjs.com/gatsby-5/) requires Node.js 18. If your build is using another Node.js version, [follow our Node.js docs](/build/configure-builds/manage-dependencies#node-js-and-javascript) to manually set the Node.js version to 18.

### Essential Gatsby build plugin

The [Essential Gatsby](https://github.com/netlify/netlify-plugin-gatsby#readme) build plugin enables key functionality on sites that use Gatsby versions earlier than 5.12.0. It speeds up Netlify builds by preserving a site's `public` and `.cache` directories between builds. The plugin supports [Gatsby Functions](https://www.gatsbyjs.com/docs/reference/functions/) and SSR and DSG rendering. If you don't need those, you can [remove the plugin](/extend/install-and-use/build-plugins#remove-a-plugin) from your site.

Gatsby sites on Netlify need two plugins to support all features:

- **[The Essential Gatsby build plugin](#install-the-essential-gatsby-build-plugin) (`@netlify/plugin-gatsby`).** This plugin installs automatically for all Gatsby sites deployed on Netlify.
- **[The Gatsby plugin for Netlify](#install-the-gatsby-plugin-for-netlify) (`gatsby-plugin-netlify`).** This needs to be installed manually and is required for SSR rendering, Gatsby redirects, and asset caching rules.

#### Install the Essential Gatsby build plugin

New Gatsby sites on Netlify automatically install the Essential Gatsby build plugin. You can confirm this in the build logs. If you want to install it manually, you can use [file-based plugin installation](/extend/install-and-use/build-plugins#file-based-installation) and add the plugin as `@netlify/plugin-gatsby` in your `netlify.toml` file.

```toml
  [[plugins]]
  package = "@netlify/plugin-gatsby"
```

#### Install the Gatsby plugin for Netlify

To enable SSR rendering, Gatsby redirects, and asset caching rules, you must also install the Gatsby plugin [gatsby-plugin-netlify](https://www.gatsbyjs.com/plugins/gatsby-plugin-netlify/).

To install the Gatsby plugin for Netlify, follow the Gatsby plugin process:

1. Add the package as a dependency.

   ```shell
   npm install -D gatsby-plugin-netlify
   ```

2. Add `gatsby-plugin-netlify` to your `gatsby-config.js` file's plugins array.

   ```js
   module.exports = {
     plugins: ["gatsby-plugin-netlify"]
   };
   ```

For more information, including optional plugin configuration, check out the [`gatsby-plugin-netlify` docs](https://github.com/netlify/gatsby-plugin-netlify/#readme).

#### Limitations

`StaticImage` and `gatsby-transformer-sharp` don't work properly for SSR or DSG pages. Instead, you can host your images on a CDN such as [Cloudinary](https://www.gatsbyjs.com/docs/how-to/images-and-media/using-cloudinary-image-service/) or [imgix](https://github.com/imgix/gatsby).

#### Auto-generated Netlify Functions

To support Gatsby Functions and SSR/DSG render modes, the Essential Gatsby build plugin automatically generates Netlify Functions called `__api`, `__ssr`, `__dsg`, and `__ipx`. If your site doesn't have Gatsby Functions or SSR/DSG pages, then the Netlify Functions won't be generated.

You can use one or more of the following build environment variables to directly control generation of these functions.

- **`NETLIFY_SKIP_GATSBY_FUNCTIONS`:** skips generation of all functions (`__api`, `__ssr`, `__dsg`, and `__ipx`). Takes precedence over the following function skip environment variables.
- **`NETLIFY_SKIP_API_FUNCTION`:** skips generation of the `__api` function.
- **`NETLIFY_SKIP_SSR_FUNCTION`:** skips generation of the `__ssr` function.
- **`NETLIFY_SKIP_DSG_FUNCTION`:** skips generation of the `__dsg` function.

#### Optional loading of the Gatsby datastore from the CDN

By default, Netlify includes the Gatsby datastore in the Netlify Function bundle, which is a deployment package that's zipped for direct upload to AWS. If you have a larger site, the site's datastore may exceed the [maximum function deploy size](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#function-configuration-deployment-and-execution), preventing you from successfully deploying your website.

`GATSBY_EXCLUDE_DATASTORE_FROM_BUNDLE` is an environment variable that loads the Gatsby datastore from the CDN rather than bundling it with the function, bypassing the size limitation.

Note that enabling loading the datastore from the CDN results in different page load behavior. On the first load of  functions that handle SSR and DSG pages, the datastore is downloaded, which can result in a slower initial page load. 

During the build process, pre-warm requests are sent to the SSR and DSG function endpoints to reduce the user-facing impact of the datastore download.

#### Local development

When developing Gatsby Functions, you can use the built-in `gatsby develop` functions server. However, if you want to run the Netlify Functions that are generated during the build step, you can use [`netlify dev`](/api-and-cli-guides/cli-guides/local-development/). Make sure to run `netlify build` first to generate the Netlify Functions from your Gatsby Functions.

### Suggested configuration values

When you link a repository for a Gatsby project, Netlify provides a suggested build command and publish directory: `gatsby build` and `public`.

If you're using the CLI to run [Netlify Dev](/api-and-cli-guides/cli-guides/local-development/) for a local development environment, Netlify suggests a dev command and port: `gatsby develop` and `8000`.

You can override suggested values or set them in a configuration file instead, but suggested values from automatic framework detection may help simplify the process of setting up a Gatsby site on Netlify.

For manual configuration, check out the [typical build settings](/build/frameworks/overview#gatsby) for Gatsby.

### Environment variables

Environment variables prefixed with `GATSBY_` are processed by Gatsby and made available in the browser for client-side JavaScript access. For more information on how to use environment variables in Gatsby, including with SSR or DSG pages, check out the [Environment variables and frameworks doc](/build/frameworks/use-environment-variables-with-frameworks).

### Netlify Image CDN

Gatsby supports deferred image resizing with [Netlify Image CDN](/build/image-cdn/overview).

To enable the image CDN, you need to do the following:

- Set the environment variable `NETLIFY_IMAGE_CDN` to `true`
- Use the Contentful, Drupal, or WordPress source plugins

For more information, including how to allow remote images, visit the [Essential Gatsby build plugin's documentation](https://github.com/netlify/netlify-plugin-gatsby/blob/main/docs/image-cdn.md).

## More resources

- [Typical Gatsby build settings](/build/frameworks/overview#gatsby)
- [Gatsby Adapters: Realize the Full Potential of Gatsby on Your Platform](https://www.netlify.com/blog/gatsby-adapters-realize-the-full-potential-of-gatsby-on-your-platform/)
- [Essential Gatsby build plugin documentation](https://github.com/netlify/netlify-plugin-gatsby#readme)
- [Five Optimizations for Faster Gatsby Builds](https://www.netlify.com/blog/2020/06/11/5-optimizations-for-faster-gatsby-builds/)
- [Gatsby 101: Features, Benefits, and Trade-Offs](https://www.netlify.com/blog/2020/06/25/gatsby-101-features-benefits-and-trade-offs/)
- [Improve Gatsby Build Speeds With Parallel Image Processing](https://www.netlify.com/blog/2020/02/25/gatsby-build-speed-improvements-with-parallel-image-processing/)
- [Netlify Blog: Gatsby posts](https://www.netlify.com/tags/gatsby/)
- [Deploying to Netlify](https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting/deploying-to-netlify/)
- [Gatsby documentation](https://www.gatsbyjs.com/docs/)

