---
title: "Netlify Environment Variables with Frameworks"
source: https://docs.netlify.com/build/frameworks/use-environment-variables-with-frameworks.md
path: build/frameworks/use-environment-variables-with-frameworks
---

---
title: "Use environment variables with frameworks"
description: "Learn how to use environment variables during a build with a framework. Access environment variables after deployment."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Projects on Netlify can use [environment variables](/build/environment-variables/overview) at two different stages: during the build process or once the site is built and running in the browser.

## Use variables during the build

Our docs cover how to [create environment variables](/build/environment-variables/get-started/#create-environment-variables) and how to use environment variables [during the build process](/build/configure-builds/environment-variables#use-variables-during-the-build).

Depending on the framework you use, there are specific [configuration variables](/build/configure-builds/environment-variables#netlify-configuration-variables) you may want to set to change an aspect of your build - such as the `HUGO_VERSION` or `NEXTAUTH_SECRET`. Visit the Netlify doc for your [framework](/build/frameworks/overview) to find out more. 

Note that if you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your environment variables, the scope must include **Builds** to be available during the build process.

## Use variables after the build is complete

If you want to use environment variable values after the site is built, you have a few options:

- Use a function, including [serverless functions](/build/functions/environment-variables) and [edge functions](/build/edge-functions/environment-variables), to access values during runtime. This is the best option to avoid revealing sensitive values.
- [Embed variable values](#embed-variable-values-in-the-site-build) in the site code during the build process. 
- [Leverage snippet injection](/build/post-processing/snippet-injection/#environment-variables) to access values during post-processing.

### Embed variable values in the site build

You can embed environment variables into your site while it's building, for use within your site after the build is complete. You should not copy sensitive values into your build as these values are accessible to anyone inspecting your app files in the browser.

Along with your framework's built-in environment variables, you may want to use custom variables or Netlify variables in your site.

#### Custom variables

To set custom variables in the Netlify UI or the `netlify.toml` and then use them within your site, most frameworks require the use of a framework-specific prefix in the name of each [variable you declare](/build/environment-variables/get-started/#create-environment-variables).

Here are a few examples of frameworks and the prefix to use for each:
- Create React App: `REACT_APP_`
- Gatsby: `GATSBY_`
- Next: `NEXT_PUBLIC_`
- Nuxt: `NUXT_ENV_`
- Vue CLI: `VUE_APP_`

For example, here is a non-sensitive custom variable `GREETING` set in `netlify.toml` for the production context. To make it work with React, use the name `REACT_APP_GREETING`:  

```toml
[context.production.environment]
  REACT_APP_GREETING = "Hello"
```

You can then use the custom environment variable in your React site code in production:

```js
<section>
  <p>
    This is my greeting: { process.env.REACT_APP_GREETING }
  </p>
</section>
```

Check the docs for your framework to confirm if a prefix is necessary.

##### Setting variables for use with server-side rendering
If your project uses server-side rendering (SSR) or deferred static generation (DSG), Netlify automatically handles these pages using Netlify [Functions](/build/functions/overview) or Netlify [Edge Functions](/build/edge-functions/overview).

As the `netlify.toml` file is only read during the build process and not accessible by functions, you need to set custom variables in the Netlify [UI, CLI, or API](/build/environment-variables/get-started/#create-variables-with-the-netlify-ui-cli-or-api) if you want your SSR or DSG pages to access them during runtime. If you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your custom environment variables, the scope must include both **Functions** and **Builds** to support both server-side and client-side rendering.

To access Netlify configuration or [read-only variables](/build/configure-builds/environment-variables#read-only-variables) in SSR or DSG pages, create variables with these values in the build command as outlined in the following section.

#### Netlify variables

To use Netlify's build environment variables in your site, create variables in your project code (where applicable, these should be framework-prefixed variables) and assign the Netlify variables as their values.

The recommended way to do this is to create the variables in-line before your project's build command. For example, to access Netlify's `CONTEXT` variable in your Create React App site, update the build command in the `netlify.toml` to set `REACT_APP_CONTEXT=$CONTEXT` before running the build:

```toml
[build]
  command = "REACT_APP_CONTEXT=$CONTEXT npm run build"
```

You can do the same update to the [build command](/build/configure-builds/overview#build-settings) in the Netlify UI. 

Note that it's not possible to use Netlify variables as values in the environment variables sections of the Netlify UI or `netlify.toml`. Depending on your framework, however, it might be possible to use variables as values in [a `.env` file](#env-files-and-netlify-variables).

As the framework builds your site, it retrieves the environment variable `CONTEXT` from the build environment and uses the variable's value when it injects the framework-prefixed variable, such as `REACT_APP_CONTEXT`, into your site.

You can then access the variable in your JavaScript files using the format `process.env.VARIABLE_NAME`, such as `process.env.REACT_APP_CONTEXT`:

```javascript
if (process.env.REACT_APP_CONTEXT === `deploy-preview`){
  console.log(`This is a preview version of our site.`);
}
```

##### `.env` files and Netlify variables

While Netlify may not read your `.env` files, depending on where you [build your project](/build/configure-builds/environment-variables#prepare-your-build-environment), your framework may read the files during the framework's build step. 

If you would like to use Netlify environment variables as values in a `.env` file for your framework to access, such as `REACT_APP_CONTEXT=$CONTEXT`, your project needs to support variable expansion. 

Framework support for variable expansion, the term for retrieving variables from the build environment for use as values in `.env` files, varies.

Some frameworks, such as [Create React App](https://create-react-app.dev/docs/adding-custom-environment-variables/#expanding-environment-variables-in-env) and [Vue](https://cli.vuejs.org/guide/mode-and-env.html#environment-variables), have built-in variable expansion support. Some frameworks support similar functionality in their unique configuration files, such as Nuxt with [`nuxt.config.js`](https://nuxtjs.org/docs/directory-structure/nuxt-config/#env). Other frameworks will require the use of a separate library, such as [`dotenv-expand`](https://github.com/motdotla/dotenv-expand), to make this work. 

We recommend searching your framework's docs for "expand variables" or "variable expansion" to confirm what's possible.


