---
title: "Hydrogen"
source: https://shopify.dev/docs/api/hydrogen.md
path: docs/api/hydrogen
---

---
title: Hydrogen
description: >-
  Hydrogen is Shopify’s opinionated stack for headless commerce, built on React
  Router.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/hydrogen/latest'
  md: 'https://shopify.dev/docs/api/hydrogen/latest.md'
api_name: hydrogen
---

# Hydrogen

Hydrogen is Shopify’s opinionated stack for headless commerce, built on [React Router](https://reactrouter.com/home). It provides a set of tools, utilities, and best-in-class examples for building dynamic and performant commerce applications.

## Setup

1. Create a new Hydrogen project with your preferred package manager.
2. Import components, hooks, or utilities that you want to use in your app. For more, see the [getting started guide](https://shopify.dev/docs/custom-storefronts/hydrogen/getting-started).

[API Reference - Getting started with Hydrogen and Oxygen](https://shopify.dev/docs/custom-storefronts/hydrogen/getting-started)

## Create a new Hydrogen project

##### npm

```txt
npm create @shopify/hydrogen@latest
```

##### yarn

```txt
yarn create @shopify/hydrogen
```

***

## Authentication

To make full use of Hydrogen, you need to authenticate with and make requests to the [Storefront API](https://shopify.dev/docs/api/storefront) and the [Customer Account API](https://shopify.dev/docs/api/customer). Hydrogen includes full-featured API clients to securely handle API queries and mutations.

You can create access tokens for your own Shopify store by [installing the Hydrogen sales channel](https://apps.shopify.com/hydrogen), which includes built-in support for Oxygen, Shopify’s global edge hosting platform. Or install the [Headless sales channel](https://apps.shopify.com/headless) to host your Hydrogen app anywhere.

Both the Storefront API and Customer Account API offer public credentials for client-side applications.

[API Reference - Hydrogen sales channel](https://apps.shopify.com/hydrogen)

[API Reference - Headless sales channel](https://apps.shopify.com/headless)

## Authenticate a Hydrogen app

##### server.js

```js
/**
 * server.js
 * ---------
 * Create a storefront client.
 * Check the server.js file in the root of your new Hydrogen project to see
 * an example implementation of this function. If you start from an official
 * Hydrogen template (Hello World or Demo Store), then the client is already
 * set up for you. Update the Shopify store domain and API token to start
 * querying your own store inventory.
 */
const {storefront} = createStorefrontClient({
  cache,
  waitUntil,
  i18n: {language: 'EN', country: 'US'},
  // `env` provides access to runtime data, including environment variables
  publicStorefrontToken: env.PUBLIC_STOREFRONT_API_TOKEN,
  privateStorefrontToken: env.PRIVATE_STOREFRONT_API_TOKEN,
  storeDomain: env.PUBLIC_STORE_DOMAIN,
  storefrontId: env.PUBLIC_STOREFRONT_ID,
  storefrontHeaders: getStorefrontHeaders(request),
});
```

##### .env

```txt
# These API credentials fetch example inventory from the Hydrogen Demo Store
# https://hydrogen.shop
#
# Replace with your own store domain and Storefront API token

SESSION_SECRET="foobar"
PUBLIC_STOREFRONT_API_TOKEN="3b580e70970c4528da70c98e097c2fa0"
PUBLIC_STORE_DOMAIN="hydrogen-preview.myshopify.com"
```

***

## Versioning

Hydrogen is tied to specific versions of the [Storefront API](https://shopify.dev/api/storefront), which is versioned quarterly. For example, if you're using Storefront API version `2023-10`, then Hydrogen versions `2023.10.x` are fully compatible.

**Caution:**

If a Storefront API version includes breaking changes, then the corresponding Hydrogen version will include the same breaking changes.

[API Reference - Shopify API versioning](https://shopify.dev/docs/api/usage/versioning)

[API Reference - API release notes](https://shopify.dev/docs/api/release-notes)

***

## How Hydrogen works with Hydrogen React

Hydrogen is [built on React Router](https://shopify.dev/docs/custom-storefronts/hydrogen/project-structure). But many of the components, hooks and utilities built into Hydrogen come from [Hydrogen React](https://shopify.dev/docs/api/hydrogen-react), an underlying package that’s framework-agnostic. For convenience, the Hydrogen package re-exports those resources. This means that if you’re building a Hydrogen app, then you should import modules from the `@shopify/hydrogen` package.

## Importing Hydrogen components

## example-page.jsx

```jsx
import {ShopPayButton} from '@shopify/hydrogen';


export function renderShopPayButton({variantId, storeDomain}) {
  return <ShopPayButton variantIds={[variantId]} storeDomain={storeDomain} />;
}
```

***

## Resources

[Custom storefronts on Shopify\
\
](https://shopify.dev/custom-storefronts)

[Learn more about how to design, build, and manage custom storefronts on Shopify.](https://shopify.dev/custom-storefronts)

[Hydrogen on GitHub\
\
](https://github.com/Shopify/hydrogen)

[Follow the Hydrogen project, file bugs and feature requests, preview upcoming features, and more](https://github.com/Shopify/hydrogen)

***

