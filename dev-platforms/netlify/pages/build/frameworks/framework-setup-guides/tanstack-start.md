---
title: "TanStack Start on Netlify"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/tanstack-start.md
path: build/frameworks/framework-setup-guides/tanstack-start
---

---
title: "TanStack Start on Netlify"
description: "Learn about TanStack on our platform."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

TanStack Start is a React-based full-stack framework that is optimized for serving dynamic apps with an Enterprise-grade fully-featured routing system. TanStack Start is powered by TanStack Router, which you can use with any JavaScript framework. TanStack Start for Solid.js is also fully supported.

### Promoted Content

**Title - Explore a TanStack app**

**description**
Explore this working example of a TanStack app built with TanStack Router, Sentry, and Claude AI. This chat app uses Claude AI to answer questions.

TanStack Start apps are fully supported on Netlify. SSR, Server Routes, Server Functions, and middleware are all seamlessly deployed to Netlify serverless functions.

## TanStack Router

[TanStack Router](https://tanstack.com/router/latest) offers a fully-featured routing system with deep TypeScript support and type-safe routing. You can use the TanStack router with any JavaScript based framework.

TanStack Router includes the following benefits:

- nested routing system so you can make dynamic layouts easier
- built-in data fetching and caching with [TanStack Query](https://tanstack.com/query/latest)
- designed to be as type-safe as possible
- full-document SSR
- server functions
- streaming
- bundling

Learn more about TanStack's capabilities in the official [TanStack docs](https://tanstack.com/).

## Deploy to Netlify

To deploy a new TanStack Start app on Netlify, we recommend our official template but you can also deploy quickly with your own app.

### Deploy from a template

This TanStack template app is built with TanStack Router, Sentry, and Claude AI.

You can deploy this app directly from the Netlify UI or by clicking the **Deploy to Netlify** button at the top of this page.

To deploy from the Netlify UI:

1. Go to your Netlify team dashboard or sites overview landing page at `https://app.netlify.com/teams/<YOUR-TEAM-NAME>/projects`.
2. Select **Add new project**, then choose **Start from template**.
3. Choose the TanStack template project.
4. Follow the setup prompts to complete your first app deploy with Netlify.

### Deploy with `create-tsrouter-app`

From the terminal, you can generate your own TanStack starter app with this command:

```bash
npx create-tsrouter-app@latest --template file-router --add-ons tanchat,netlify
```

Next, you can follow these [steps](/start/quickstarts/deploy-from-repository/) to deploy your app to Netlify or use the [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli).

### Info - CLI version requirement

When deploying TanStack Start apps with Netlify CLI and `@netlify/vite-plugin-tanstack-start`, you must use netlify-cli version 17.31 or higher.

### Deploy manually

If you've got your own Tanstack Start app and want to deploy to Netlify you should have the following configured in your project.

1. Install and configure the Netlify TanStack Start Vite plugin:

```bash
npm install -D @netlify/vite-plugin-tanstack-start
```

2. In your Tanstack Start app's `vite.config.ts` file, add the plugin:

```typescript
import { defineConfig } from 'vite'
import { tanstackStart } from '@tanstack/react-start/plugin/vite'
import netlify from '@netlify/vite-plugin-tanstack-start'

export default defineConfig({
  plugins: [
    // ...
    tanstackStart(),
    netlify(),
  ],
})
```

3. Finally, add a `netlify.toml` to your project with these contents:

```toml
[build]
  command = "vite build"
  publish = "dist/client"
```

Alternatively, you can configure these build settings in the Netlify Dashboard. For your chosen project, go to 
### NavigationPath Component:

project configuration > Build & deploy > Continuous deployment > Build settings
 and enter the settings above.

Your site should successfully deploy on your next push. 🚀

### TanStack Start versions before 1.132.0

If you're using TanStack Start versions before 1.132.0, you'll need to configure things differently:

#### For versions 1.121.0 to 1.131.x

Use the `target: 'netlify'` option in your `vite.config.ts` instead of the Netlify TanStack Start Vite plugin:

```ts
import { tanstackStart } from '@tanstack/react-start/plugin/vite'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [tanstackStart({ target: 'netlify' })],
})
```

Set your build command to `dist` instead of `dist/client`:

```toml
[build]
  command = "vite build"
  publish = "dist"
```

#### For versions before 1.121.0

Use `app.config.ts` instead of `vite.config.ts`:

```ts
import { defineConfig } from '@tanstack/react-start/config'

export default defineConfig({
  server: {
    preset: 'netlify',
  },
})
```

Set your build command to `vinxi build` instead of `vite build`.

## Local development

The Netlify TanStack Start Vite plugin provides all the benefits of the [Netlify Vite plugin](https://www.npmjs.com/package/@netlify/vite-plugin): full emulation of the production Netlify platform.
This gives you the same platform primitives locally that your site uses in production.

You or an agent can access and build with the following features when running a TanStack Start dev server in your local development flow:

- Serverless functions
- Edge functions
- Blobs
- Cache API
- Image CDN
- Redirects & rewrites
- Headers
- Environment variables

### Tip - No need for Netlify CLI for dev

Because the plugin emulates Netlify's platform primitives in your dev server, you don't need to use Netlify CLI to run local dev.

## Further help

Learn more from the official [TanStack docs](https://tanstack.com/).

