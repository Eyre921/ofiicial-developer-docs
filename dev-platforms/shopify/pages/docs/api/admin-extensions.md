---
title: "admin UI extension"
source: https://shopify.dev/docs/api/admin-extensions.md
path: docs/api/admin-extensions
---

---
title: Admin UI extensions
description: >
  Build extensions that integrate into the Shopify admin interface. For example,
  you can add custom content blocks to product or order detail pages, create
  action modals that launch from context menus, or build custom settings
  interfaces for Shopify Functions.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/admin-extensions/latest'
  md: 'https://shopify.dev/docs/api/admin-extensions/latest.md'
api_name: admin-extensions
---

# Admin UI extensions

Build extensions that integrate into the [Shopify admin interface](https://shopify.dev/docs/apps/admin). For example, you can add custom content blocks to product or order detail pages, create action modals that launch from context menus, or build custom settings interfaces for [Shopify Functions](https://shopify.dev/docs/apps/functions).

Extensions run in the context of key merchant workflows, so always prioritize performance.

## Getting started

Admin UI extensions require a TOML configuration file and TSX (or JSX) files containing your Preact-based extension code.

Use [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) to scaffold your extension with the essential configuration and files. You can alter the default configuration later to customize the way your admin UI extension operates.

## Generate scaffold

```terminal
cd my-app
shopify app generate extension
```

[Tutorial - Build an admin action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action)

***

## Building your extension

Admin UI extensions are made up of three interconnected parts: targets that determine where your extension appears in the Shopify admin interface, target APIs that provide access to data and functionality based on your chosen target, and web components that define which interface elements you can use.

### Targets: Choose where your extension appears

Targets define where your extensions appear within Shopify's admin interface and what capabilities they have. There are six types of targets:

| Target type | Description |
| - | - |
| Action | Add menu items to the **More actions** menu on details and index pages. When triggered, your UI extension displays in a modal. This target has two varieties that can be used together: - **Render:** Displays the action menu item and renders your UI extension content in the modal.
- **Should render:** Controls whether the action appears in the menu based on conditions. |
| Selection action | Add menu items to the **More actions** menu on index pages when merchants select multiple resources. Use for bulk operations on selected items, such as batch exports, bulk tagging, or multi-item processing. This target has two varieties that can be used together: - **Render:** Displays the action menu item and renders your UI extension content in the modal when resources are selected.
- **Should render:** Controls whether the selection action appears based on conditions. |
| Block | Render inline cards on resource pages like product details, order details, or customer details. Merchants must [add and pin](https://help.shopify.com/manual/apps/working-with-apps#add-app-blocks-to-your-shopify-admin) blocks to their pages before they can use them. You can launch action targets from block targets for complex interactions. |
| Configuration | Provide configuration interfaces for various admin features. This target has two varieties: - **Product and variant configuration:** Render configuration settings for [product bundles](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui) and customizable products on product and product variant pages.
- **Function settings:** Provide configuration interfaces for [Shopify Functions](https://shopify.dev/docs/apps/build/functions), including [discount](https://shopify.dev/docs/api/functions/latest/discount), [validation](https://shopify.dev/docs/api/functions/latest/cart-and-checkout-validation), and [order routing](https://shopify.dev/docs/api/functions/latest/order-routing-location-rule) functions. |
| Print action | Add menu items to the **Print** menu on order and product pages. This target has two varieties that can be used together: - **Render:** Displays the print action menu item and opens a print interface when triggered.
- **Should render:** Controls whether the print action appears in the menu based on conditions. |
| Runnable | Execute code and return data to Shopify without rendering UI. Used for extensions that supply data to Shopify features, such as [Sidekick](https://shopify.dev/docs/apps/build/sidekick/build-app-data) and [customer segment templates](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-a-template-extension). |

[Reference - Explore all targets](https://shopify.dev/docs/api/admin-extensions/2026-04/targets)

![Shopify admin page showing a placeholder extension target location.](https://shopify.dev/assets/assets/images/templated-apis-screenshots/admin-extensions/2025-07/admin.product-details.action.render-C1xNd2nJ.png)

### Target APIs: Define what your extension does

Your extension can display inventory alerts, add shipping label actions, or configure discount functions. Use target APIs to access the data and functionality for each scenario.

When your extension runs, Shopify provides a `shopify` global object that you use to access data and features. Most target APIs are properties on this object. For example, `shopify.data` gives you contextual resource data, `shopify.query()` runs GraphQL Admin API queries, and `shopify.navigation.navigate()` moves between pages.

If your app uses ESLint, update your configuration to include the global `shopify` object to prevent linting errors.

[Reference - Explore all target APIs](https://shopify.dev/docs/api/admin-extensions/2026-04/target-apis)

## Block Extension API: Access product data

```tsx
import {render} from 'preact';


export default () => {
  const productId = shopify.data.selected?.[0]?.id;


  render(
    <s-admin-block heading="Product information">
      <s-text>Product ID: {productId}</s-text>
    </s-admin-block>,
    document.body
  );
};
```

## ESLint configuration

```javascript
module.exports = {
  globals: {
    shopify: 'readonly',
  },
};
```

### Web components: Design your interface

Web components are the UI building blocks that you use to display data and trigger API functions. These components are native UI elements that follow [Shopify's design system](https://shopify.dev/docs/apps/design) and are built with [remote-dom](https://github.com/Shopify/remote-dom), Shopify's library for building cross-platform user interfaces.

Use web components to build interfaces that integrate with Shopify's admin design system.

[Reference - Explore all web components](https://shopify.dev/docs/api/admin-extensions/2026-04/web-components)

## Admin action component: Configure an admin action modal

```html
<s-admin-action heading="Extension title">
  Modal content
  <s-button slot="primary-action">Save</s-button>
  <s-button slot="secondary-actions">Cancel</s-button>
</s-admin-action>
```

![Admin extension using an action component to display a modal dialog.](https://shopify.dev/assets/assets/images/templated-apis-screenshots/admin/components/adminaction-example-CJj9EXBo.png)

***

## Configuration

Admin UI extensions rely on a `shopify.extension.toml` file that contains the extension's configuration. This includes the extension name, type, API version, and targeting definitions.

The `name` value is what displays in the admin interface to merchants, so consider this value carefully. We recommend that the `api_version` reflects the latest supported API version.

### Properties

Admin UI extensions use the following configuration properties:

##### `api_version` required

The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`.

##### `[[extensions]]` required

The name of the array that contains all extensions listed in the TOML file. Contains the following properties:

* `type`: required The extension type. For admin UI extensions, use `ui_extension`.

* `name`: required The merchant-facing name of the extension. After you [generate an extension](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension), you're prompted to provide a name for your extension. The `name` property is translatable if it starts with a `t:` and uses a key defined in your translation data.

  **Limitations**:

  * 5 characters minimum
  * 30 characters maximum

* `handle`: required The unique internal identifier for the extension. After you create a draft version of the extension, or deploy an extension, you can't change the `handle` value.

  **Limitations**:

  * Allowed characters: `a-z`, `A-Z`, `0-9`, `-`
  * 100 characters maximum
  * Must be unique within the app

* `uid`: required The extension user identifier that must be unique within the app. An app-scoped identifier used by `shopify app deploy` to determine whether an extension is being created, updated, or deleted.

* `description`: optional The merchant-facing description of the extension.

##### `[[extensions.targeting]]` required

The name of the array that contains a target and its associated module. Contains the following properties:

* `target`: required

  An identifier that specifies where you're injecting your extension into the admin interface.

* `module`: required

  The path to the JavaScript or TypeScript file that contains your extension code. This file exports the extension function that renders your UI or handles events.

## shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "My Admin UI extension"
handle = "my-admin-ui-extension"
uid = "f62f100d-15e6-9866-eda9-23f99de4b5d26e347042"
description = "Custom product details extension"


    [[extensions.targeting]]
    target = "admin.product-details.block.render"
    module = "./src/ProductBlock.tsx"


    [[extensions.targeting]]
    target = "admin.product-details.action.render"
    module = "./src/ProductAction.tsx"
```

***

## App authentication

Use authenticated requests when your extension needs to fetch data or trigger actions on your own backend service. For example, you might need to display external analytics data, sync inventory with a warehouse system, or validate custom business rules.

Admin UI extensions can make authenticated calls to your app's backend. When you use `fetch()` to make a request to your app's configured auth domain or any of its subdomains, an `Authorization` header is automatically added with a Shopify [OpenID Connect ID Token](https://shopify.dev/docs/api/app-home/apis/id-token). There's no need to manually manage ID tokens.

Relative URLs passed to `fetch()` are resolved against your app's `app_url`. This means if your app's backend is on the same domain as your `app_url`, you can make requests to it using `fetch('/path')`.

If you need to make requests to a different domain, you can use the [`auth.idToken()`](https://shopify.dev/docs/api/admin-extensions/latest/api/standard-api#standardapi-propertydetail-auth) method to retrieve the ID token and manually add it to your request headers.

## Make requests to your app's backend

##### Get product data

```tsx
import {render} from 'preact';
import {useEffect, useState} from 'preact/hooks';

export default async () => {
  render(<Extension />, document.body);
}

// Get product info from app backend
async function getProductInfo(id) {
  const res = await fetch(`/api/products/${id}`);
  return res.json();
}

function Extension() {
  // Contextual "input" data passed to this extension:
  const {data} = shopify;
  const productId = data.selected?.[0]?.id;

  const [productInfo, setProductInfo] = useState();
  useEffect(() => {
    getProductInfo(productId).then(setProductInfo);
  }, [productId]);

  return (
    <s-admin-block heading="Product Info">
      <s-text>Info: {productInfo?.title}</s-text>
    </s-admin-block>
  );
}
```

##### Get data from a different domain

```tsx
import {render} from 'preact';
import {useEffect, useState} from 'preact/hooks';

export default async () => {
  render(<Extension />, document.body);
}

// Get product info from a different app backend
async function getProductInfo(id, auth) {
  const token = await auth.idToken();
  const res = await fetch(`https://app.example.com/api/products/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.json();
}

function Extension() {
  // Contextual "input" data passed to this extension:
  const {data, auth} = shopify;
  const productId = data.selected?.[0]?.id;

  const [productInfo, setProductInfo] = useState();
  useEffect(() => {
    getProductInfo(productId, auth).then(setProductInfo);
  }, [productId, auth]);

  return (
    <s-admin-block heading="Product Info">
      <s-text>Info: {productInfo?.title}</s-text>
    </s-admin-block>
  );
}
```

**Note:**

Your server must support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) for `https://extensions.shopifycdn.com`. Include this origin in your [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) header. The [Shopify App Remix template](https://github.com/Shopify/shopify-app-template-remix) handles this automatically.

***

## Direct API access

Use direct API access when your extension needs to query or modify Shopify data in real-time. For example, you might want to update product metafields, fetch detailed order information, or modify inventory levels.

You can make [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) requests directly from your extension using the [`query`](https://shopify.dev/docs/api/admin-extensions/latest/api/standard-api#standardapi-propertydetail-query) method in the Standard API or the standard [web fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch). Any `fetch()` calls from your extension to the GraphQL Admin API are automatically authenticated by default. These requests are fast because Shopify handles them directly without requiring a round trip to your backend.

Direct API requests use [online access mode](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/online-access-tokens) by default. If you want to use [offline access mode](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/offline-access-tokens), you can set the `direct_api_mode` property to `offline` in your [app TOML file](https://shopify.dev/docs/apps/tools/cli/configuration#admin).

You must declare all required [access scopes](https://shopify.dev/docs/api/usage/access-scopes) in your app's TOML file.

**Note:**

Direct API can't be used to manage storefront access tokens.

## Query Shopify data directly

##### Fetch product data

```tsx
import {render} from 'preact';

export default async () => {
  const productId = shopify.data.selected?.[0]?.id;
  const product = await getProduct(productId);
  render(<Extension product={product} />, document.body);
};

async function getProduct(id) {
  const res = await fetch('shopify:admin/api/graphql.json', {
    method: 'POST',
    body: JSON.stringify({
      query: `
        query GetProduct($id: ID!) {
          product(id: $id) {
            title
          }
        }
      `,
      variables: {id},
    }),
  });
  const {data} = await res.json();
  return data.product;
}

function Extension({product}) {
  return (
    <s-admin-block heading="Product Info">
      <s-text>The selected product title is {product.title}</s-text>
    </s-admin-block>
  );
}
```

##### Query product data

```tsx
import {render} from 'preact';

export default async () => {
  const productId = shopify.data.selected?.[0]?.id;
  const {
    data: {product},
  } = await shopify.query(
    `
    query GetProduct($id: ID!) {
      product(id: $id) {
        title
      }
    }
  `,
    {variables: {id: productId}},
  );
  render(<Extension product={product} />, document.body);
};

function Extension({product}) {
  return (
    <s-admin-block heading="Product Info">
      <s-text>The selected product title is {product.title}</s-text>
    </s-admin-block>
  );
}
```

***

## Custom protocols

Custom protocols make it easier to navigate to common locations and construct URLs within your extensions.

### Shopify protocol

Use the `shopify:admin` protocol when you want to construct a URL with a root of the Shopify admin.

## shopify:admin

##### Link to product page

```tsx
<s-link href="shopify:admin/products/1234567890">Link to Product Page</s-link>;
```

##### Fetch data

```typescript
fetch('shopify:admin/api/graphql.json', {
  method: 'POST',
  body: JSON.stringify(simpleProductQuery),
});
```

### App protocol

Use the `app:` protocol to construct a URL for your app. Shopify will handle constructing the base URL for your app. This works for both apps rendered in the Shopify admin and standalone apps.

## app:

```tsx
<s-link href="app:settings/advanced">App settings</s-link>;
```

### Extension protocol

Trigger an action extension from a block extension using the `extension:` protocol. The `extensionTarget` is the target of the action extension. The handle is the handle of the action extension that will be opened.

## extension:

```tsx
<s-link href={`extension:${extension.handle}/${extensionTarget}`}>Open extension</s-link>;
```

### Relative URLs

Relative urls are relative to your app and are useful when you want to link to a route within your app. This works for both apps rendered in the Shopify admin and standalone apps.

## /relative/urls

```tsx
<s-link href={`/reviews/${product.id}`}>View reviews</s-link>;
```

***

## Testing and deployment

After you've built your extension, test it thoroughly and deploy it to production.

### Local testing

**Info:**

As of API version `2026-04`, you can write unit tests for admin UI extensions using [`@shopify/ui-extensions-tester`](https://github.com/Shopify/ui-extensions/blob/2026-04/packages/ui-extensions-tester/README.md). Check out the [example test suite](https://github.com/Shopify/ui-extensions/tree/2026-04/examples/testing/admin-testing-example) to get started.

To run your extension locally during development, start a dev server using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli). The `dev` command creates a preview of your extension on your chosen [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores). If your extension is built on an app with a backend, then this command also serves your backend locally using a Cloudflare tunnel.

The dev server automatically reloads your extension when you make changes to your code, so you can test updates in real-time.

## Start development server

```terminal
shopify app dev
```

### Deployment

When you're ready to go live, deploy your extension to production using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

The Shopify CLI `deploy` command builds your extension bundle and uploads everything to Shopify. If your extension is built on an app with a backend, then you need to deploy your app to a hosting service first. Shopify hosts only your extension's code.

**Note:**

Your compiled UI extension bundle can't exceed 64 KB. Shopify enforces this limit at deployment to ensure fast loading times and optimal performance. Learn how to [analyze your bundle size](https://shopify.dev/docs/apps/build/app-extensions#analyzing-bundle-size).

## Deploy your extension

```terminal
shopify app deploy
```

### Versioning

Polaris reference docs follow [Shopify's API versioning policy](https://shopify.dev/docs/api/usage/versioning). Each stable version is supported for a minimum of 12 months. Older versions continue to work, they just won't have dedicated docs on Shopify.dev. [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) already prevents deploys targeting API versions older than 12 months, so we recommend keeping your extensions on a supported version.

***

## Tutorials and resources

Deepen your understanding of admin UI extensions with these tutorials and community resources.

### Tutorials

[Tutorial - Build an admin action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-action)

[Tutorial - Build an admin block UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-block)

[Tutorial - Connect admin UI extensions](https://shopify.dev/docs/apps/build/admin/actions-blocks/connect-admin-extensions)

[Tutorial - Connect UI extensions to your app's backend](https://shopify.dev/docs/apps/build/admin/actions-blocks/connect-app-backend)

[Tutorial - Hide admin UI extensions](https://shopify.dev/docs/apps/build/admin/actions-blocks/hide-extensions)

[Tutorial - Build an admin print action UI extension](https://shopify.dev/docs/apps/build/admin/actions-blocks/build-admin-print-action)

[Tutorial - Build a discounts UI with admin UI extensions](https://shopify.dev/docs/apps/build/discounts/build-ui-extension)

[Tutorial - Add a product configuration extension](https://shopify.dev/docs/apps/build/product-merchandising/bundles/product-configuration-extension/add-merchant-config-ui)

[Tutorial - Build a customer segment template extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-a-template-extension)

[Tutorial - Build a customer segment action extension](https://shopify.dev/docs/apps/build/marketing-analytics/customer-segments/build-an-action-extension)

[Tutorial - Use extensions to surface app data](https://shopify.dev/docs/apps/build/sidekick/build-app-data)

### Community resources

[Reference - Developer changelog](https://shopify.dev/changelog)

[Community - Community forum for admin UI extensions](https://community.shopify.dev/tag/admin-ui-extensions)

***

