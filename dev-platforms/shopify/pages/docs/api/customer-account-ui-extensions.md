---
title: "Customer account UI extensions"
source: https://shopify.dev/docs/api/customer-account-ui-extensions.md
path: docs/api/customer-account-ui-extensions
---

---
title: Customer account UI extensions
description: >-
  Customer account UI extensions let app developers build custom functionality
  that merchants can install at defined points on the Order index, Order status,
  and Profile pages in customer accounts.
api_version: 2026-04
source_url:
  html: 'https://shopify.dev/docs/api/customer-account-ui-extensions/latest'
  md: 'https://shopify.dev/docs/api/customer-account-ui-extensions/latest.md'
api_name: customer-account-ui-extensions
---

# Customer account UI extensions

Build extensions that integrate into [customer accounts](https://shopify.dev/docs/apps/customer-accounts) on Shopify, including order status pages, profile sections, and order action buttons. For example, you can add loyalty program information, create subscription management interfaces, or enable customers to track shipments and request returns.

## Getting started

Customer account UI extensions require a TOML configuration file and TSX (or JSX) files containing your Preact-based extension code.

Use [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) to scaffold your extension with the essential configuration and files. You can alter the default configuration later to customize the way your customer account UI extension operates.

## Generate scaffold

```terminal
cd my-app
shopify app generate extension
```

[Tutorial - Start building for customer accounts](https://shopify.dev/docs/apps/build/customer-accounts/start-building)

***

## Upgrading your extension

The latest version of customer account UI extensions adds new components and target APIs, and replaces checkout metafields with order metafields. Check out the [migration guide](https://shopify.dev/docs/apps/build/customer-accounts/migrate-to-web-components) for the steps to upgrade your extension.

***

## Building your extension

Customer account UI extensions are made up of three interconnected parts: targets that determine where your extension appears in the customer account interface, target APIs that provide access to customer and order data, and web components that define which interface elements you can use.

### Targets: Choose where your extension appears

Targets define where your extensions appear within the customer account interface and what capabilities they have. There are three types of targets:

| Target type | Description |
| - | - |
| Block | Render at merchant-defined locations within customer account pages. Merchants control placement using the [checkout and accounts editor](https://help.shopify.com/manual/checkout-settings/customize-checkout-configurations/checkout-editor). Use to display custom content that works independently of specific page features. |
| Full page | Create custom pages with dedicated routes in the customer account. Merchants can add `customer-account.page.render` targets to the customer account navigation menu. Order-specific `customer-account.order.page.render` targets can't be added to the menu. Use to build standalone experiences like loyalty dashboards or subscription management interfaces. |
| Static | Render at fixed locations tied to specific page features, such as order action buttons or announcement banners. These targets only appear when their associated page feature is present. Use when your extension's functionality depends on a specific page element. |

[Reference - Explore all targets](https://shopify.dev/docs/api/customer-account-ui-extensions/2026-04/targets)

![Customer account extension targets overview showing where extensions appear in the customer account interface](https://shopify.dev/assets/assets/images/templated-apis-screenshots/customer-account-ui-extensions/2025-07/building-your-extension-DCOU_qNv.png)

### Target APIs: Define what your extension does

Your extension can display order tracking, show loyalty rewards, enable reordering, or manage subscriptions. Use target APIs to access the data and functionality for each scenario.

When your extension runs, Shopify provides a `shopify` global object that you use to access data and features. Most target APIs are properties on this object. For example, [`shopify.order`](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/target-apis/order-apis/order-api) gives you order data, [`shopify.authenticatedAccount`](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/target-apis/account-apis/authenticated-account-api) provides customer identity, and [`shopify.navigation.navigate()`](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/target-apis/platform-apis/navigation-api) moves between pages.

If your app uses ESLint, update your configuration to include the global `shopify` object to prevent linting errors.

[Reference - Explore all target APIs](https://shopify.dev/docs/api/customer-account-ui-extensions/2026-04/target-apis)

## Order API: Access order data

```tsx
import {render} from 'preact';


export default () => {
  render(<Extension />, document.body);
};


function Extension() {
  const order = shopify.order.value;
  return (
    <s-card>
      <s-text>Order {order?.name}</s-text>
      <s-text color="subdued">ID: {order?.id}</s-text>
    </s-card>
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

The component library includes form inputs, buttons, layout primitives, overlays, feedback indicators, and more. You can use individual components for simple displays, or combine the stack, section, badge, and button components to build richer interfaces like a loyalty status display.

[Reference - Explore all web components](https://shopify.dev/docs/api/customer-account-ui-extensions/2026-04/web-components)

## Stack component: Display loyalty information

```tsx
import {render} from 'preact';


export default () => {
  render(
    <s-section>
      <s-stack direction="block" gap="base">
        <s-heading>Loyalty Status</s-heading>
        <s-stack direction="inline" gap="small">
          <s-badge tone="auto">Gold Member</s-badge>
          <s-text>2,450 points</s-text>
        </s-stack>
        <s-button onClick={() => shopify.navigation.navigate('extension:loyalty-page/rewards')}>
          View Rewards
        </s-button>
      </s-stack>
    </s-section>,
    document.body
  );
};
```

![Stack component displaying loyalty status information with a badge and points](https://shopify.dev/assets/assets/images/templated-apis-screenshots/customer-account-ui-extensions/2025-07/display-loyalty-info-CxZR7I9l.png)

***

## Configuration

Customer account UI extensions rely on a `shopify.extension.toml` file that contains the extension's configuration. This includes the extension name, type, API version, and targeting definitions.

The `name` value is what displays to merchants in certain contexts, so consider this value carefully. We recommend that the `api_version` reflects the latest supported API version.

### Properties

Customer account UI extensions use the following configuration properties:

##### `api_version` required

The version of the API that's being used for the extension. If provided in the `[[extensions]]` array, then the specified API version is used instead of the root level `api_version`.

##### `[[extensions]]` required

The name of the array that contains all extensions listed in the TOML file. Contains the following properties:

* `type`: required The extension type. For customer account UI extensions, use `ui_extension`.

* `name`: required The merchant-facing name of the extension.

  **Limitations**:

  * 5 characters minimum.
  * 50 characters maximum.

* `handle`: required The unique internal identifier for the extension. After you create a draft version of the extension, or deploy an extension, you can't change the `handle` value.

  **Limitations**:

  * Allowed characters: `a-z`, `A-Z`, `0-9`, `-`, `_`.
  * 100 characters maximum.
  * Must be unique within the app.

* `uid`: required The extension user identifier that must be unique within the app. An app-scoped identifier used by `shopify app deploy` to determine whether an extension is being created, updated, or deleted.

* `description`: optional The merchant-facing description of the extension.

##### `[[extensions.targeting]]` required

The name of the array that contains a target and its associated module. Contains the following properties:

* `target`: required

  An identifier that specifies where you're injecting your extension into the customer account interface.

* `module`: required

  The path to the JavaScript or TypeScript file that contains your extension code.

You can define multiple targets in a single configuration file, but each target must point to a separate module file. For block targets, you can also [define the default placement](https://shopify.dev/docs/apps/build/customer-accounts/extension-placement#define-default-placement). See the [targets overview](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/targets) for more details.

##### `[extensions.capabilities]` optional

Defines the capabilities associated with your extension.

| Capability | Description |
| - | - |
| [`api_access`](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#storefront-api-access) | Allows your extension to query the Storefront API. |
| [`network_access`](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#network-access) | Allows your extension to make external network calls. |
| [`collect_buyer_consent`](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#collect-buyer-consent) | Allows your extension to collect buyer consent for policies like SMS marketing. |

##### `[[extensions.metafields]]` optional

Define [metafields](https://shopify.dev/docs/apps/build/metafields) your extension needs access to. Use `[[extensions.metafields]]` for metafields needed by all targets, or `[[extensions.targeting.metafields]]` for target-specific metafields.

All customer account UI extension [targets](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/targets) can read and write to metafields using the [Customer Account API](https://shopify.dev/docs/api/customer). [Order status targets](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/targets#order-status) can also read metafields using the [Metafields API](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/target-apis/order-apis/metafields-api).

See which [resources support metafields](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#resources-that-support-metafields) and the available [metafield data types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

Learn more about [using metafields in customer account UI extensions](https://shopify.dev/docs/apps/build/customer-accounts/metafields-in-customer-accounts).

##### `[extensions.settings]` optional

Settings let merchants configure your extension from the checkout and accounts editor. Each settings definition can include up to 20 settings. All setting inputs are optional — code your extension so it still works if the merchant hasn't set a value. Learn more about [settings fields, supported types, and validation options](https://shopify.dev/docs/apps/build/app-extensions/configure-app-extensions#settings-fields).

## shopify.extension.toml

```toml
api_version = "2026-04"


[[extensions]]
type = "ui_extension"
name = "Loyalty program"
handle = "loyalty-program-extension"
uid = "4be0643f-1d98-e73b-17cd-ca98a65347dda7632660"


    [[extensions.targeting]]
    target = "customer-account.order-status.block.render"
    module = "./src/OrderStatusBlock.tsx"


    [[extensions.targeting]]
    target = "customer-account.profile.block.render"
    module = "./src/ProfileBlock.tsx"


    [[extensions.targeting]]
    target = "customer-account.page.render"
    module = "./src/LoyaltyPage.tsx"


    [extensions.capabilities]
    api_access = true
    network_access = true


    [extensions.capabilities.collect_buyer_consent]
    customer_privacy = true


    [[extensions.metafields]]
    namespace = "my-namespace"
    key = "my-key"


    [extensions.settings]
    [[extensions.settings.fields]]
    key = "banner_title"
    type = "single_line_text_field"
    name = "Banner title"
```

**Info:**

If your extension accesses customer data, then your app must have [protected customer data](https://shopify.dev/docs/apps/store/data-protection/protected-customer-data) access approved before it can go live.

***

## App authentication

Use app authentication when your extension needs to fetch data from your own backend service. For example, you might need to display a customer's loyalty status or log extension interactions to an external analytics system.

To enable network access, add `network_access = true` to your extension's [capabilities](https://shopify.dev/docs/apps/build/customer-accounts/capabilities) and [request access](https://partners.shopify.com/current/apps) in the Partner Dashboard. Your server must include `Access-Control-Allow-Origin: *` in response headers because UI extensions run in a Web Worker with a null origin.

Use `fetch` to call your backend and pass a [session token](https://shopify.dev/docs/api/customer-account-ui-extensions/latest/target-apis/platform-apis/session-token-api) to authenticate the request. If you don't need data from an external source, then consider using [metafields](https://shopify.dev/docs/apps/build/customer-accounts/metafields-in-customer-accounts) as an alternative to network calls.

## Make requests to your app's backend

```tsx
import {render} from 'preact';
import {useState, useEffect} from 'preact/hooks';


export default () => {
  render(<Extension />, document.body);
};


async function getLoyaltyPoints(sessionToken) {
  const res = await fetch('https://your-app.com/api/loyalty', {
    headers: {
      Authorization: `Bearer ${sessionToken}`,
    },
  });
  return res.json();
}


function Extension() {
  const [points, setPoints] = useState(null);


  useEffect(() => {
    async function fetchPoints() {
      const token = await shopify.sessionToken.get();
      const data = await getLoyaltyPoints(token);
      setPoints(data.points);
    }
    fetchPoints();
  }, []);


  return (
    <s-section>
      <s-text>Loyalty points: {points ?? 'Loading...'}</s-text>
    </s-section>
  );
}
```

***

## Direct API access

Use direct API access when your extension needs to query Shopify data in real-time. For example, you might want to display related products, fetch the customer's order history, or retrieve the customer's profile information.

Customer account extensions provide two ways to query Shopify data:

* **Customer Account API**: Query customer data including profile information, order history, and saved addresses using `fetch()`. Requests to the Customer Account API are automatically authenticated and don't require additional capabilities.
* **Storefront API**: Query products, collections, metaobjects, and other storefront data using `shopify.query()`. Enable the [`api_access`](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#storefront-api-access) capability to make authenticated requests without manually managing tokens. If you need to call your own backend or other external services, use the [`network_access`](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#network-access) capability instead.

[Reference - Customer Account API](https://shopify.dev/docs/api/customer-account-ui-extensions/2026-04/target-apis/account-apis/customer-account-api)

[Reference - Storefront API](https://shopify.dev/docs/api/customer-account-ui-extensions/2026-04/target-apis/platform-apis/storefront-api)

## Query Shopify data directly

##### Customer Account API

```tsx
import {render} from 'preact';
import {useState, useEffect} from 'preact/hooks';

export default () => {
  render(<Extension />, document.body);
};

const API_VERSION = '2026-04';

function Extension() {
  const [customer, setCustomer] = useState(null);

  useEffect(() => {
    fetch(\`shopify://customer-account/api/\$2026-04/graphql.json\`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: `{
          customer {
            firstName
            lastName
            emailAddress { emailAddress }
          }
        }`,
      }),
    })
      .then((res) => res.json())
      .then(({ data }) => setCustomer(data.customer))
      .catch(console.error);
  }, []);

  return (
    <s-card>
      <s-text>
        {customer
          ? `${customer.firstName} ${customer.lastName}`
          : 'Loading...'}
      </s-text>
    </s-card>
  );
}
```

##### Storefront API

```tsx
import {render} from 'preact';
import {useState, useEffect} from 'preact/hooks';

export default () => {
  render(<Extension />, document.body);
};

function Extension() {
  const [data, setData] = useState(null);

  useEffect(() => {
    shopify
      .query(
        `query ($first: Int!) {
          products(first: $first) {
            nodes {
              id
              title
            }
          }
        }`,
        { variables: { first: 5 } }
      )
      .then(({ data }) => setData(data))
      .catch(console.error);
  }, []);

  return (
    <s-section>
      <s-text>
        {data?.products?.nodes.map((node) => node.title).join(', ') ?? 'Loading...'}
      </s-text>
    </s-section>
  );
}
```

***

## Custom protocols

Customer account UI extensions support custom protocols for navigating to customer account pages, other extensions, and routes within your extension without hardcoding full URLs. The following custom protocols are supported.

### Shopify protocol

Use the `shopify:customer-account` protocol when you want to construct a URL with a root of customer accounts. This allows you to link directly to customer account pages like orders, profile, or addresses.

## shopify:customer-account

##### Link to orders page

```tsx
<s-link href="shopify:customer-account/orders">View all orders</s-link>
```

##### Link to profile page

```tsx
<s-link href="shopify:customer-account/profile">View profile</s-link>
```

### Extension protocol

Use the `extension:` protocol to navigate between extensions within the same application. The handle identifies the target extension to navigate to.

## extension:

##### Link to full-page extension

```tsx
<s-link href={`extension:${extension.handle}/${path}`}>
  View details
</s-link>
```

##### Order-specific extension

```tsx
<s-link href={`extension:${extension.handle}/customer-account.order.page.render/${orderId}/${path}`}>
  View order details
</s-link>
```

### Relative URLs

Relative URLs are relative to your extension and are useful when you want to link to a route within your extension.

## /relative/urls

```tsx
<s-link href={`/subscriptions/${subscription.id}`}>
  View subscription details
</s-link>
```

***

## Testing and deployment

After you've built your extension, test it thoroughly and deploy it to production.

### Local testing

To run your extension locally during development, start a dev server using [Shopify CLI](https://shopify.dev/docs/api/shopify-cli). The `dev` command creates a preview of your extension on your chosen [dev store](https://shopify.dev/docs/apps/build/dev-dashboard/development-stores). If your extension is built on an app with a backend, then this command also serves your backend locally using a Cloudflare tunnel.

The dev server automatically reloads your extension when you make changes to your code, so you can test updates in real-time.

## Start development server

```terminal
shopify app dev
```

Testing customer account UI extensions requires a dev store with customer accounts enabled and test customer accounts created.

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

## Security

Customer account UI extensions are a safe and secure way to customize the appearance and functionality of the customer account pages without compromising the security of customer data.

* They run in an isolated sandbox, separate from the customer account page and other UI extensions.
* They don't have access to sensitive payment information or the customer account page itself (HTML or other assets).
* They are limited to specific UI components and APIs that are exposed by the platform.
* They have limited access to [global web APIs](https://github.com/Shopify/ui-extensions/blob/unstable/documentation/runtime-environment.md).
* Apps that wish to access [protected customer data](https://shopify.dev/docs/apps/store/data-protection/protected-customer-data) must submit an application and are subject to strict security guidelines and review processes by Shopify.

***

## Error handling

To handle errors in your extension, add an `unhandledrejection` listener for promise rejections or an `error` listener for other exceptions like JavaScript runtime errors or failures to load a resource.

You can also use third-party error-reporting libraries. However, these libraries might require extra configuration because UI extensions run inside of a [Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) which doesn't have access to `window` or the DOM. You'll typically need to disable default integrations and manually attach error listeners to `self`.

The third-party tool example shown uses [Sentry](https://sentry.io/). To install and initialize this tool, follow their [browser JavaScript guide](https://docs.sentry.io/platforms/javascript/). We recommend disabling the default integrations to make sure the tool runs within a Web Worker. You'll need to add event listeners manually.

**Note:**

You must request [network access](https://shopify.dev/docs/apps/build/customer-accounts/capabilities#network-access) to transmit errors to a third-party service.

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

[Tutorial - Build an inline order status UI extension](https://shopify.dev/docs/apps/build/customer-accounts/inline-extensions/build-order-status)

[Tutorial - Build an inline profile UI extension](https://shopify.dev/docs/apps/build/customer-accounts/inline-extensions/build-profile)

[Tutorial - Build for order action menus](https://shopify.dev/docs/apps/build/customer-accounts/order-action-extensions/build-for-order-action-menus)

[Tutorial - Build new pages in customer accounts](https://shopify.dev/docs/apps/build/customer-accounts/full-page-extensions/build-new-pages)

[Tutorial - Building metafield writes into extensions](https://shopify.dev/docs/apps/build/customer-accounts/metafields)

[Tutorial - Build pre-auth order status UI extensions](https://shopify.dev/docs/apps/build/customer-accounts/pre-auth-order-status-page-extensions/build-pre-auth-order-status-page-extensions)

[Tutorial - Localize a customer account UI extension](https://shopify.dev/docs/apps/build/customer-accounts/localization/localize)

[Guide - UX for customer accounts](https://shopify.dev/docs/apps/build/customer-accounts/ux)

### Community resources

[Reference - Developer changelog for customer account UI extensions](https://shopify.dev/changelog?filter=customer-account-extensions)

[Community - Community forum for customer account extensions](https://community.shopify.dev/tag/customer-account-ext)

***

