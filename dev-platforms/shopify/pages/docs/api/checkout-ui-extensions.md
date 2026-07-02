---
title: "Checkout UI Extensions"
source: https://shopify.dev/docs/api/checkout-ui-extensions.md
path: docs/api/checkout-ui-extensions
---

---
title: Checkout UI extensions
description: >
  Build extensions that integrate into Shopify's checkout interface. For
  example, you can add custom fields to collect additional information, display
  personalized upsells, or customize the Thank you page experience.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/checkout-ui-extensions/latest'
  md: 'https://shopify.dev/docs/api/checkout-ui-extensions/latest.md'
api_name: checkout-ui-extensions
---

# Checkout UI extensions

Extensions add custom UI and logic into any step of the [Shopify checkout](https://shopify.dev/docs/apps/checkout) experience. For example, you can display personalized messages during cart review, integrate custom payment options at checkout, or add a survey to the thank-you page.

By using extension target APIs and web components from Shopify's Polaris design system, you can build performant customizations that look and feel familiar while tailoring the checkout experience to a store's specific needs.

**Shopify Plus:**

Checkout UI extensions for the information, shipping, and payment steps are available only to stores on a [Shopify Plus plan](https://www.shopify.com/plus).

## Getting started

To get started customizing your store's checkout, scaffold an app extension using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli).

Scaffolding the extension creates a file framework that includes your extension's [TOML configuration file](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions) and a templated `Checkout.jsx` file where you add your extension's code.

## Generate scaffold

```bash
cd my-app
shopify app generate extension --template checkout_ui
```

[Tutorial - Getting started with checkout UI extensions](https://shopify.dev/docs/apps/build/checkout/start-building)

***

## Upgrading your extension

The latest version of checkout UI extensions adds new components and target APIs, and updates how extensions read and write metafields. Check out the [migration guide](https://shopify.dev/docs/apps/build/checkout/migrate-to-web-components) for the steps to upgrade your extension.

***

## Building your extension

Checkout UI extensions are made up of three interconnected parts: targets that determine where your custom UI appears in the checkout interface, target APIs that provide access to checkout data and functionality, and web components that render UI elements like buttons and menus.

### Targets: Choose where your custom UI appears

Targets define where your custom UI appears within Shopify's checkout interface. There are three types of targets:

| Target type | Description |
| - | - |
| Block | Flexible placement targets that merchants can position using the [checkout and accounts editor](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-editor). Merchants can place block targets in various locations throughout the checkout flow and on the Thank you page. |
| Runnable | Targets that provide data or functionality without rendering UI components. These targets run in response to specific events, such as when a customer types in an address field, and return data like autocomplete suggestions or formatted address information. |
| Static | Targets that appear at fixed locations in checkout, such as before actions, after contact fields, or after cart line items. These targets render automatically when the checkout page loads and can't be moved or repositioned. |

[Reference - Explore all targets](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/targets)

![Checkout UI targets overview](https://shopify.dev/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-07/building.your.extension-BobGcef1.png)

### Target APIs: Define what your extension does

Target APIs provide access to data and functionality within the checkout flow. Use them to add custom logic to your extension.

When your extension runs, Shopify provides a `shopify` global object that you use to access data and features. Most target APIs are properties on this object. For example, `shopify.buyerIdentity` gives you information about the buyer who's interacting with the checkout, and `shopify.cost` provides the cost breakdown for the current checkout.

If your app uses ESLint, update your configuration to include the global `shopify` object to prevent linting errors.

[Reference - Explore all target APIs](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/target-apis)

## Cost API: Display checkout subtotal

```tsx
import '@shopify/ui-extensions/preact';
import {render} from 'preact';


export default function extension() {
  render(<Extension />, document.body);
}


function Extension() {
  const subtotal = shopify.cost.subtotalAmount.value;
  return (
    <s-stack>
      <s-text>
        Subtotal: {subtotal.amount}{' '}
        {subtotal.currencyCode}
      </s-text>
    </s-stack>
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

The component library includes options like form inputs, buttons, overlays, and feedback indicators. You can use these components individually for simple displays, or combine them with layout primitives like stack, grid, and section to build more complex interfaces.

[Reference - Explore all web components](https://shopify.dev/docs/api/checkout-ui-extensions/2026-04/web-components)

## Using web components

```typescript
import '@shopify/ui-extensions/preact';
import {render} from 'preact';


export default function extension() {
  render(<Extension />, document.body);
}


function Extension() {
  return (
    <s-stack direction="inline">
      <s-image src="https://cdn.shopify.com/YOUR_IMAGE_HERE" />
      <s-stack>
        <s-heading>Heading</s-heading>
        <s-text type="small">Description</s-text>
      </s-stack>
      <s-button
        onClick={() => {
          console.log('button was pressed');
        }}
      >
        Button
      </s-button>
    </s-stack>
  );
}
```

![Checkout UI extension web components example](https://shopify.dev/assets/assets/images/templated-apis-screenshots/checkout-ui-extensions/2025-07/web.components-BVHhzg7k.png)

### Apply changes: Update the cart and checkout

Some target APIs include methods that update the cart and checkout. For example:

* [`applyAttributeChange`](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/checkout-apis/attributes-api) sets a cart attribute.
* [`applyMetafieldChange`](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/platform-apis/metafields-api) writes a cart metafield.

Each method returns a promise that resolves after Shopify applies the change and the corresponding API property updates with the new state.

**Rate limits may apply:**

Rate limits may apply to extensions that make too many changes during a checkout. After an extension is rate limited, it can't make further changes during the buyer's session.

Batch multiple changes with `Promise.all`. Only apply the changes your extension needs.

## Apply changes

##### Single change

```tsx
import '@shopify/ui-extensions/preact';
import {render} from 'preact';

async function onCheckboxChange(event) {
  const isChecked = event.target.checked;

  await shopify.applyAttributeChange({
    type: 'updateAttribute',
    key: 'includeGift',
    value: isChecked ? 'yes' : 'no',
  });
}

function Extension() {
  return (
    <s-checkbox
      onChange={onCheckboxChange}
      label="Include a complimentary gift"
    />
  );
}

export default function extension() {
  render(<Extension />, document.body);
}
```

##### Multiple changes

```tsx
import '@shopify/ui-extensions/preact';
import {render} from 'preact';

async function saveGiftPreferences() {
  // Shopify batches these into a single request.
  await Promise.all([
    shopify.applyAttributeChange({
      type: 'updateAttribute',
      key: 'includeGift',
      value: 'yes',
    }),
    shopify.applyMetafieldChange({
      type: 'updateCartMetafield',
      metafield: {
        namespace: '$app:gift',
        key: 'message',
        type: 'single_line_text_field',
        value: 'Happy birthday!',
      },
    }),
  ]);
}

function Extension() {
  return (
    <s-button onClick={saveGiftPreferences}>
      Save gift preferences
    </s-button>
  );
}

export default function extension() {
  render(<Extension />, document.body);
}
```

[Guidelines - Applying changes to checkout](https://shopify.dev/docs/apps/build/checkout/extension-performance/applying-changes)

***

## Configuration

You define your extension's configuration in a `shopify.extension.toml` file. This file contains the extension's name, targeting definitions, API version, and other settings. We recommend that you always set the latest supported `api_version` in your configuration file.

When you scaffold your extension using Shopify CLI, a `shopify.extension.toml` file with a default configuration is created for you. As you build your extension, you define the targets you want to use and their corresponding code modules in this file.

### Properties

Checkout UI extensions use the following configuration properties:

##### `api_version` required

The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`.

##### `[[extensions]]` required

The name of the array that contains all extensions listed in the TOML file. Contains the following properties:

* `type`: required The extension type. For checkout UI extensions, use `ui_extension`.

* `name`: required The customer-facing name of the extension.

  **Limitations**:

  * 5 characters minimum.
  * 30 characters maximum.

* `handle`: required The unique internal identifier for the extension. After you create a draft version of the extension, or deploy an extension, you can't change the `handle` value.

  **Limitations**:

  * Allowed characters: `a-z`, `A-Z`, `0-9`, `-`.
  * 50 characters maximum.
  * Must be unique within the app.

* `uid`: required The extension user identifier that must be unique within the app. An app-scoped identifier used by `shopify app deploy` to determine whether an extension is being created, updated, or deleted. This identifier is generated automatically when you scaffold your extension using Shopify CLI.

* `description`: optional The merchant-facing description of the extension.

##### `[[extensions.targeting]]` required

The name of the array that contains a target and its associated module. Contains the following properties:

* `target`: required

  An identifier that specifies where you're injecting your extension into the checkout interface.

* `module`: required

  The path to the JavaScript or TypeScript file that contains your extension code.

You can define multiple targets in a single configuration file, but each target must point to a separate module file. For block targets, you can also define the default placement. See the [targets overview](https://shopify.dev/docs/api/checkout-ui-extensions/latest/targets#block-extension-targets) for more details.

##### `[extensions.capabilities]` optional

Defines the capabilities associated with your extension.

| Capability | Description |
| - | - |
| [`api_access`](https://shopify.dev/docs/apps/build/checkout/capabilities#storefront-api-access) | Allows your extension to query the Storefront API. |
| [`network_access`](https://shopify.dev/docs/apps/build/checkout/capabilities#network-access) | Allows your extension to make external network calls. |
| [`collect_buyer_consent`](https://shopify.dev/docs/apps/build/checkout/capabilities#collect-buyer-consent) | Allows your extension to collect buyer consent for policies like SMS marketing. |
| [`block_progress`](https://shopify.dev/docs/apps/build/checkout/capabilities#block-progress) | Allows your extension to block the buyer's progress. |

##### `[[extensions.metafields]]` optional

Define [metafields](https://shopify.dev/docs/apps/build/metafields) your extension needs access to. Use `[[extensions.metafields]]` for metafields needed by all targets, or `[[extensions.targeting.metafields]]` for target-specific metafields.

Checkout targets can use the [Metafields API](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/platform-apis/metafields-api) to read metafields you request in the TOML, and to write cart metafields with `applyMetafieldChange` (`updateCartMetafield` and `removeCartMetafield`). Thank you page targets can read metafields through the Metafields API, but don't have write access.

See which [resources support metafields](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#resources-that-support-metafields) and the available [metafield data types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

Learn more in the [Metafields API](https://shopify.dev/docs/api/checkout-ui-extensions/latest/target-apis/platform-apis/metafields-api) reference.

##### `[extensions.settings]` optional

Settings let merchants configure your extension from the [checkout editor](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-editor). Each settings definition can include up to 20 settings. All setting inputs are optional. Build your extension so it still works if the merchant hasn't set a value.

Each field in `[[extensions.settings.fields]]` accepts the following properties:

* `key`: required The identifier for the setting. The configured value is exposed under this key at runtime.

* `type`: required The setting type. Determines what input the merchant sees and how the value is validated. Supported types: `boolean`, `single_line_text_field`, `multi_line_text_field`, `number_integer`, `number_decimal`, `date`, `date_time`, and `variant_reference`.

* `name`: required The display name shown to the merchant in the checkout editor.

* `description`: optional Help text displayed to the merchant in the checkout editor.

* `validations`: optional Constraints on the input that Shopify validates, such as min/max length or a regex pattern. Learn more about [validation options](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#settings-fields).

## shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "My checkout UI extension"
handle = "my-checkout-extension"
uid = "fddfc370-27c7-c30f-4ee0-a927194e2accadefd40c"


    [[extensions.targeting]]
    target = "purchase.checkout.block.render"
    module = "./src/Checkout.tsx"


    [[extensions.targeting]]
    target = "purchase.thank-you.block.render"
    module = "./src/ThankYou.tsx"
```

[Reference - Configuring app extensions](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions)

***

## Testing and deployment

[Shopify CLI](https://shopify.dev/docs/api/shopify-cli) provides a set of tools to help you test and deploy your extension.

### Local testing

**Info:**

As of API version `2026-04`, you can write unit tests for checkout UI extensions using [`@shopify/ui-extensions-tester`](https://github.com/Shopify/ui-extensions/blob/2026-04/packages/ui-extensions-tester/README.md). Check out the [example test suite](https://github.com/Shopify/ui-extensions/tree/2026-04/examples/testing/checkout-basic-testing-example) to get started.

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

[Tutorial - Testing checkout UI extensions](https://shopify.dev/docs/apps/checkout/test-ui-extensions#test-the-extension-in-the-checkout-editor)

[Reference - Deploy app versions](https://shopify.dev/docs/apps/launch/deployment/deploy-app-versions)

### Versioning

Polaris reference docs follow [Shopify's API versioning policy](https://shopify.dev/docs/api/usage/versioning). Each stable version is supported for a minimum of 12 months. Older versions continue to work, they just won't have dedicated docs on Shopify.dev. [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) already prevents deploys targeting API versions older than 12 months, so we recommend keeping your extensions on a supported version.

***

## Security

Checkout UI extensions are a safe and secure way to customize the appearance and functionality of checkout without compromising the security of customer data.

* They run in an isolated sandbox, separate from the checkout page and other UI extensions.
* They don't have access to sensitive payment information or the checkout page itself (HTML or other assets).
* They are limited to specific UI components and APIs that are exposed by the platform.
* They have limited access to [global web APIs](https://github.com/Shopify/ui-extensions/blob/unstable/documentation/runtime-environment.md).
* Apps that wish to access [protected customer data](https://shopify.dev/docs/apps/store/data-protection/protected-customer-data) must submit an application and are subject to strict security guidelines and review processes by Shopify.

***

## Error handling

To handle errors in your extension, add an `unhandledrejection` listener for promise rejections or an `error` listener for other exceptions like Javascript runtime errors or failures to load a resource.

You can also use third party error-reporting libraries. However, these libraries might require extra configuration because UI extensions run inside of a [Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) which doesn't have access to `window` or the DOM. You'll typically need to disable default integrations and manually attach error listeners to `self`.

The third-party tool example shown uses [Sentry](https://sentry.io/). To install and initialize this tool, follow their [Browser JavaScript guide](https://docs.sentry.io/platforms/javascript/). We recommend disabling the default integrations to be sure the tool will run within a Web Worker. You'll need to add event listeners manually.

**Note:**

You must request [network access](https://shopify.dev/docs/apps/build/checkout/capabilities#network-access) to transmit errors to a third party service.

## Error handling examples

##### Using a listener

```ts
// For unhandled promise rejections
self.addEventListener('unhandledrejection', (event) => {
  console.warn('event unhandledrejection', event.reason);
});

// For other exceptions
self.addEventListener('error', (event) => {
  console.warn('event error', event.error);
});
```

##### Using Sentry

```ts
import '@shopify/ui-extensions/preact';
import {render} from 'preact';
import {
  BrowserClient,
  captureException,
  defaultStackParser,
  getCurrentScope,
  makeFetchTransport,
} from '@sentry/browser';

const sentryClient = new BrowserClient({
  dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',
  transport: makeFetchTransport,
  stackParser: defaultStackParser,
  integrations: [],
});
getCurrentScope().setClient(sentryClient);
sentryClient.init();

self.addEventListener('unhandledrejection', (event) => {
  captureException(event.reason);
});

self.addEventListener('error', (event) => {
  captureException(event.error);
});

// Your normal extension code.
export default function extension() {
  render(<Extension />, document.body);
}

function Extension() {
  return <s-banner>Your extension</s-banner>;
}
```

***

## Tutorials and resources

Deepen your understanding of checkout UI extensions with these tutorials and community resources.

### Tutorials

[Tutorial - Customizing Shopify checkout](https://shopify.dev/docs/apps/checkout/build-options)

[Tutorial - Start building for checkout](https://shopify.dev/docs/apps/build/checkout/start-building)

[Tutorial - Display custom data at checkout](https://shopify.dev/docs/apps/build/checkout/display-custom-data?extension=polaris)

[Tutorial - Customize the checkout header](https://shopify.dev/docs/apps/build/checkout/customize-header?extension=polaris)

### Design resources

[Guidelines - App design guidelines](https://shopify.dev/docs/apps/design)

### Community resources

[Reference - Developer changelog](https://shopify.dev/changelog)

[Community - Developer community](https://community.shopify.dev)

***

