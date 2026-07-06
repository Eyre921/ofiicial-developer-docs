---
title: "POS UI extensions"
source: https://shopify.dev/docs/api/pos-ui-extensions.md
path: docs/api/pos-ui-extensions
---

---
title: POS UI extensions
description: >-
  Targets define where your POS UI extensions appear within Shopify's Point of
  Sale interface and what capabilities they receive. Targets serve specific
  purposes — some render persistent UI elements within existing screens, others
  provide interactive menu items or buttons, and some launch full-screen modal
  experiences for complex workflows.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/pos-ui-extensions/latest'
  md: 'https://shopify.dev/docs/api/pos-ui-extensions/latest.md'
api_name: pos-ui-extensions
---

# POS UI extensions

Build extensions that integrate into [Shopify's Point of Sale](https://shopify.dev/docs/apps/build/pos) interface. For example, you can add a clickable tile to the POS home screen that launches your app's features, insert custom content sections into checkout and sales processes, or show additional product details.

Extensions run in the context of key merchant workflows, so always prioritize performance.

## Getting started

POS UI extensions require a TOML configuration file and TSX (or JSX) files containing your Preact-based extension code.

Use [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) to scaffold your extension with the essential configuration and files. You can alter the default configuration later to customize the way your POS UI extension operates.

## Generate scaffold

```terminal
cd my-app
shopify app generate extension
```

[Tutorial - Getting started with POS UI extensions](https://shopify.dev/docs/apps/build/pos/getting-started)

***

## Building your extension

POS UI extensions are made up of three interconnected parts: targets that determine where your extension appears in the POS interface, target APIs that provide access to data and functionality based on your chosen target, and web components that define which interface elements you can use.

### Targets: Choose where your extension appears

Targets define where your extensions appear within Shopify's POS interface and what capabilities they have. There are three types of targets:

| Target type | Description |
| - | - |
| Tile | Appear on the smart grid (homepage) of the POS system. Use to show status, quickly access common actions, and initiate workflows. |
| Action | Trigger workflows and display modals. This target has two varieties, commonly used together: - **Menu item:** Add buttons to action menus on native POS screens. Use to provide entry points that launch modals.
- **Modal:** Display full-screen interfaces for complete workflows, forms, or multi-step processes. Modals are launched from tiles or menu items. |
| Block | Appear as inline content within native POS screens. Use to render content such as metrics, instructions, or printed content on receipts. |

[Reference - Explore all targets](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/targets)

![Placeholder image](https://shopify.dev/assets/assets/images/templated-apis-screenshots/pos-ui-extensions/2025-07/pos-overview-targets-hb2whYxm.png)

### Target APIs: Define what your extension does

Your extension can show customer loyalty points, add warranty card printing, or capture product details. Use target APIs to access the data and functionality for each scenario.

When your extension runs, Shopify provides a `shopify` global object that you use to access data and features. Most target APIs are properties on this object. For example, `shopify.storage` persists data between sessions, `shopify.toast` displays feedback messages, and `shopify.action.presentModal()` launches full-screen workflows.

If your app uses ESLint, update your configuration to include the global `shopify` object to prevent linting errors.

[Reference - Explore all target APIs](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/target-apis)

## Storage API: Getting a single value

```typescript
import {render} from 'preact';


export default async () => {
  render(<TileComponent />, document.body);
};


export function TileComponent() {
  return (
    <s-tile
      title="Storage app"
      subheading="Get example"
      onClick={async () => {
        const storedData = await shopify.storage.get('key');
        shopify.toast.show(String(storedData ?? ''));
      }}
      enabled
    />
  );
}
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

Use web components to build interfaces that automatically adapt across iOS and Android devices running Shopify POS.

[Reference - Explore all web components](https://shopify.dev/docs/api/pos-ui-extensions/2026-04/web-components)

## Tile component: Render a tile on the smart grid

```typescript
import {render} from 'preact';


export default async () => {
  render(<TileComponent />, document.body);
};


export function TileComponent() {
  return (
    <s-tile
      title="My app"
      subheading="Hello world!"
      onClick={() => {
        shopify.action.presentModal();
      }}
      enabled
    />
  );
}
```

![Placeholder image](https://shopify.dev/assets/assets/images/templated-apis-screenshots/pos-ui-extensions/2026-01/tile-default-Bh6-qbCa.png)

***

## Configuration

POS UI extensions rely on a `shopify.extension.toml` file that contains the extension's configuration. This includes the extension name, type, API version, and targeting definitions.

The `name` value is what displays in the POS interface to merchants, so consider this value carefully. We recommend that the `api_version` reflects the latest supported API version.

### Properties

POS UI extensions use the following configuration properties:

##### `api_version` required

The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`.

##### `[[extensions]]` required

The name of the array that contains all extensions listed in the TOML file. Contains the following properties:

* `type`: required The extension type. For more information, refer to [Extension types](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#extension-types).

* `name`: required The merchant-facing name of the extension. After you [generate an extension](https://shopify.dev/docs/api/shopify-cli/app/app-generate-extension), you're prompted to provide a name for your extension. The `name` property is translatable if it starts with a `t:` and uses a key defined in your translation data. For example, you might have a `t:name` key that matches a translation key called `name`. [Learn more about localization](https://shopify.dev/docs/apps/build/checkout/localized-checkout-ui-extensions#how-it-works).

* `handle`: required The unique internal identifier for the extension. After you create a draft version of the extension, or deploy an extension, you can't change the `handle` value. If not specified, the `handle` value is automatically populated using a transformed `name` value that removes any unsupported characters. For example, if you enter `google maps` as the extension name, then Shopify populates the `handle` value as `google-maps`.

* `description`: required The merchant-facing description of the extension. The `description` property is translatable if it starts with a `t:` and uses a key defined in your translation data. For example, `t:description` and you have a matching translation key called `description`. [Learn more about localization](https://shopify.dev/docs/apps/build/checkout/localized-checkout-ui-extensions#how-it-works).

##### `[[extensions.targeting]]` required

The name of the array that contains a target and its associated module. Contains the following properties:

* `target`: required

  An identifier that specifies where you're injecting your extension into the POS interface.

* `module`: required

  The path to the JavaScript or TypeScript file that contains your extension code. This file exports the extension function that renders your UI or handles events.

##### `[extensions.supported_features]`

Declares additional features for your extension. Contains the following properties:

* `runs_offline`: When set to `true`, the extension runs even when POS loses network access. Defaults to `false`. For more information, refer to [Run extensions without network access](#run-extensions-without-network-access).

## shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "My POS UI extension"
handle = "my-pos-ui-extension"
description = "My POS UI extension description"


[[extensions.targeting]]
target = "pos.home.tile.render"
module = "./src/Tile.tsx"


[[extensions.targeting]]
target = "pos.home.modal.render"
module = "./src/Modal.tsx"
```

***

## App authentication

Use authenticated requests when your extension needs to fetch data or trigger actions on your own backend service. For example, you might need to display a customer's loyalty status, process a custom discount calculation, or log POS transactions to an external analytics system.

Extensions automatically include authorization headers when making requests to your app's domain. Relative URLs resolve against your `application_url`.

**Note:**

App authentication is available as of POS version 10.6.0 for extensions targeting 2025-07 or later.

ID tokens are only returned for authenticated users with proper app permissions. Without correct permissions, the token will be `null`. POS Staff members aren't authenticated users. [Learn more about configuring app permissions](https://help.shopify.com/manual/your-account/users/roles/permissions/store-permissions#apps-and-channels-permissions).

## Make requests to your app's backend

```typescript
import {render} from 'preact';
import {useState, useEffect} from 'preact/hooks';


export default async () => {
  render(<CustomerDetailsBlock />, document.body);
};


export function CustomerDetailsBlock() {
  const [loyaltyInfo, setLoyaltyInfo] = useState('');
  useEffect(() => {
    getLoyaltyInfo();
  }, [shopify.customer.id]);


  async function getLoyaltyInfo() {
    const res = await fetch(`/api/loyalty/${shopify.customer.id}`);
    const json = await res.json();
    setLoyaltyInfo(json.loyaltySummary);
  }
  return (
    <s-pos-block>
      <s-box padding="large">
        <s-text>{loyaltyInfo}</s-text>
      </s-box>
    </s-pos-block>
  );
}
```

***

## Direct API access

Use direct API access when your extension needs to query or modify Shopify data in real-time. For example, you might want to update product metafields based on POS interactions, fetch detailed customer order history, or modify inventory levels during special promotions.

Make [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) requests directly from your extension with automatic authentication. These requests are fast because Shopify handles them directly without requiring a round trip to your backend.

**Note:**

Direct API access is available as of POS version 10.6.0 for extensions targeting 2025-07 or later.

You must declare all required [access scopes](https://shopify.dev/docs/api/usage/access-scopes) in your app's TOML file. For local development, access scopes are only registered or updated when the app is deployed and installed on your test store.

## Query Shopify data directly

```typescript
import {render} from 'preact';
import {useState, useEffect} from 'preact/hooks';


// This mutation requires the `write_products` access scope.
// /docs/api/admin-graphql/latest/mutations/metafieldsset
async function mutateMetafield(productId) {
  const requestBody = {
    query: `#graphql
        mutation MetafieldsSet($metafields: [MetafieldsSetInput!]!) {
          metafieldsSet(metafields: $metafields) {
            metafields {
              key
              namespace
              value
              createdAt
              updatedAt
            }
          }
        }
      `,
    variables: {
      metafields: [
        {
          key: 'direct_api',
          namespace: 'custom',
          ownerId: `gid://shopify/Product/${productId}`,
          value: 'Example Value',
          type: 'single_line_text_field',
        },
      ],
    },
  };


  await fetch('shopify:admin/api/graphql.json', {
    method: 'POST',
    body: JSON.stringify(requestBody),
  });
}


// This query requires the `read_products` access scope.
// /docs/api/admin-graphql/latest/queries/product
async function queryProductMetafields(productId) {
  const requestBody = {
    query: `#graphql
      query GetProduct($id: ID!) {
        product(id: $id) {
          id
          metafields(first: 10) {
            edges {
              node {
                id
                namespace
                key
                value
              }
            }
          }
        }
      }
    `,
    variables: {id: `gid://shopify/Product/${productId}`},
  };
  const res = await fetch('shopify:admin/api/graphql.json', {
    method: 'POST',
    body: JSON.stringify(requestBody),
  });
  return res.json();
}


export default async () => {
  render(<ProductDetailsBlock />, document.body);
};


export function ProductDetailsBlock() {
  const [productInfo, setProductInfo] = useState('');
  useEffect(() => {
    async function getProductInfo() {
      const result = await queryProductMetafields(shopify.product.id);
      setProductInfo(JSON.stringify(result, null, 2));
    }
    getProductInfo();
  }, [shopify.product.id]);


  return (
    <s-pos-block>
      <s-box padding="large">
        <s-text>Metafields: {productInfo}</s-text>
      </s-box>
      <s-box padding="large">
        <s-text>Set Metafields: {productInfo}</s-text>
        <s-button onClick={() => mutateMetafield(shopify.product.id)}>Set Metafields</s-button>
      </s-box>
    </s-pos-block>
  );
}
```

***

## Run extensions without network access

POS UI extensions can continue to run when the merchant's device loses internet connectivity, so merchants can use your extension during network outages.

**Note:**

Extensions can run without network access in POS versions 11.0 and later. Features that require network connectivity, such as Direct API access and app authentication, don't function without network access. Use the [Connectivity API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/connectivity-api) to detect network status and handle these scenarios gracefully.

To run extensions without network access, under `[extensions.supported_features]` in your extension's `shopify.extension.toml` configuration file, set `runs_offline` to `true`. [Shopify CLI v3.92.0](https://github.com/Shopify/cli/releases/tag/3.92.0) or later is required to recognize this configuration.

When your extension runs without network access, it continues to function using locally available data and APIs that don't require network connectivity. This ensures merchants can maintain essential workflows even without an active internet connection.

##### Supported APIs

The following APIs work when your extension runs without network access:

* [Storage API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/storage-api)
* [Locale API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/standard-apis/locale-api)
* [Toast API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/standard-apis/toast-api)
* [Connectivity API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/connectivity-api)
* [Device API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/device-api)
* [Scanner API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/scanner-api)
* [Navigation API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/navigation-api)
* [Action API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/standard-apis/action-api)
* [PinPad API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/pinpad-api)
* [Cash Drawer API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/cash-drawer-api)
* [Camera API](https://shopify.dev/docs/api/pos-ui-extensions/latest/target-apis/platform-apis/camera-api)

##### Supported targets

The following extension targets render without network access:

* [`pos.home.tile.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/home-screen)
* [`pos.home.modal.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/home-screen)
* [`pos.product-details.block.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/product-details)
* [`pos.product-details.action.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/product-details)
* [`pos.product-details.action.menu-item.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/product-details)
* [`pos.cart.line-item-details.action.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/cart-details)
* [`pos.cart.line-item-details.action.menu-item.render`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/cart-details)
* [`pos.transaction-complete.event.observe`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/post-purchase)
* [`pos.cash-tracking-session-start.event.observe`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/register-details)
* [`pos.cash-tracking-session-complete.event.observe`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/register-details)
* [`pos.cart-update.event.observe`](https://shopify.dev/docs/api/pos-ui-extensions/latest/targets/cart-details)

## shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "My extension"
handle = "my-extension"
description = "An extension that runs when POS loses network access"


[extensions.supported_features]
runs_offline = true


[[extensions.targeting]]
target = "pos.home.tile.render"
module = "./src/Tile.tsx"


[[extensions.targeting]]
target = "pos.home.modal.render"
module = "./src/Modal.tsx"
```

***

## Testing and deployment

After you've built your extension, test it thoroughly and deploy it to production.

### Local testing

**Info:**

As of API version `2026-04`, you can write unit tests for POS UI extensions using [`@shopify/ui-extensions-tester`](https://github.com/Shopify/ui-extensions/blob/2026-04/packages/ui-extensions-tester/README.md). Check out the [example test suite](https://github.com/Shopify/ui-extensions/tree/2026-04/examples/testing/point-of-sale-testing-example) to get started.

Testing POS UI extensions requires a [development store](https://shopify.dev/docs/api/development-stores) and the [Shopify POS app](https://www.shopify.com/pos/pos-app) on any mobile or tablet device—no dedicated POS hardware needed. Download the POS app from the [App Store](https://apps.apple.com/us/app/shopify-point-of-sale-pos/id686830644) or [Google Play](https://play.google.com/store/apps/details?id=com.shopify.pos\&hl=en_US), log in to your development store, and start testing.

Extensions run in preview mode during development, allowing you to test functionality and iterate quickly without affecting live merchant operations.

[Tutorial - Debugging POS UI extensions](https://shopify.dev/docs/apps/build/pos/debugging)

[Tutorial - Troubleshooting POS UI extensions](https://shopify.dev/docs/apps/build/pos/troubleshooting)

### Deployment

Use [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) to deploy your app and its extensions to production.

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

Deepen your understanding of POS UI extensions with these tutorials and community resources.

### Tutorials

[Tutorial - Getting started with POS UI extensions](https://shopify.dev/docs/apps/build/pos/getting-started)

[Tutorial - Build a discount extension](https://shopify.dev/docs/apps/build/pos/tutorials/build-discount-extension)

[Tutorial - Build a print extension](https://shopify.dev/docs/apps/build/pos/tutorials/build-print-extension)

[Tutorial - Build a subscription UI extension](https://shopify.dev/docs/apps/build/pos/tutorials/build-subscription-extension)

[Tutorial - Communicate with a server](https://shopify.dev/docs/apps/build/pos/communicate-with-server)

### Community resources

[Reference - Developer changelog for POS UI extensions](https://shopify.dev/changelog?filter=pos-extensions)

[Community - Community forum for POS UI extensions](https://community.shopify.dev/tag/pos-extensions)

***

