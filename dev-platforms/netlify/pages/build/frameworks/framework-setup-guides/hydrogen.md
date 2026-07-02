---
title: "Hydrogen on Netlify"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/hydrogen.md
path: build/frameworks/framework-setup-guides/hydrogen
---

---
title: "Hydrogen on Netlify"
description: "Learn about Hydrogen on our platform. Deploy your Hydrogen app to our edge network by using Edge Functions."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Hydrogen is a headless stack built by Shopify on top of React Router 7 that enables you to build custom Shopify storefronts. With Netlify, you can deploy your storefront using Netlify Edge Functions for improved performance and faster rendering.

### Promoted Content

**Title - Explore a Hydrogen site**

**description**
Get started with a new Hydrogen site on your Netlify account or view the demo.

## Netlify integration

Hydrogen apps on Netlify use [Netlify Edge Functions](#edge-functions) to deploy your app to Netlify Edge, bringing serverless capabilities closer to your customers.

To successfully deploy a Hydrogen app to Netlify, you should use Netlify's [starter template](https://github.com/netlify/hydrogen-template). This template creates everything you need to deploy to Netlify, including Hydrogen's Storefront API data cache backed by the [Netlify Cache API](/build/caching/cache-api). The template also includes the [Netlify Vite plugin](/build/frameworks/framework-setup-guides/vite) so that local development fully emulates the Netlify platform.

### Create a new Hydrogen app to deploy to Netlify

Using the command line, you can create a new project based on the Netlify starter template for Hydrogen.

Before you begin, make sure you have [Node.js](https://nodejs.org/en/download) version 22 or later.

1. In your terminal, run the following to create your project:

    ```bash
    npm create @shopify/hydrogen@latest -- --template https://github.com/netlify/hydrogen-template
    ```

2. Enter the project directory and prepare the development environment:

    ```bash
    cp .env.example .env
    ```

3. Run your Hydrogen app:

    ```bash
    npm run dev
    ```

From here you can customize your site. Check out your project's README for some tips or read the [How to deploy a Shopify Hydrogen storefront to Netlify guide](https://developers.netlify.com/guides/how-to-deploy-a-shopify-hydrogen-storefront-to-netlify/) for more detailed instructions.

### Edge Functions

[Edge Functions](/build/edge-functions/overview) connect the Netlify platform and workflow with an open runtime standard at the network edge. This enables you to build fast, personalized web experiences with an ecosystem of development tools.

To get the latest support for Edge Functions in your Hydrogen site, use the latest [starter template](https://github.com/netlify/hydrogen-template).

You can browse a [full library of reference examples](https://edge-functions-examples.netlify.app/) for different ways to use Edge Functions. For more details, check out the [Edge Functions documentation](/build/edge-functions/overview).

## Limitations

- Currently, only [Netlify Edge Functions](#edge-functions) can be used to power Hydrogen's
  Server-Side Rendering (SSR). **[Netlify Functions](/build/functions/overview) are not officially
  supported for Hydrogen SSR**.

## More resources

- [How to deploy a Shopify Hydrogen storefront to
  Netlify](https://developers.netlify.com/guides/how-to-deploy-a-shopify-hydrogen-storefront-to-netlify/)
- [Hydrogen documentation](https://shopify.dev/custom-storefronts/hydrogen)
- [Netlify Hydrogen starter template](https://github.com/netlify/hydrogen-template)
- [Troubleshooting Hydrogen on
  Netlify](https://github.com/netlify/hydrogen-template/blob/main/README.md#faq-and-troubleshooting)

