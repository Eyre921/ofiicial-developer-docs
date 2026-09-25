---
title: "API upgrades"
source: https://docs.stripe.com/upgrades.md
path: upgrades
---

# Upgrade your integration

Upgrade your integration to the latest API version.

Check the [Developer Changelog](https://docs.stripe.com/changelog.md) for the complete record of changes to Stripe’s API.

To upgrade your integration, complete the following steps. Search the [Changelog](https://docs.stripe.com/changelog.md?api_usage=true) for information specific to your integration.

## Define the target version for your upgrade

Make sure that you specify the API version that you’re integrating against in your code instead of relying on your account’s default API version. To test a newer version for API calls, set the `Stripe-Version` header (in live or testing environments). Learn how to [set an API version in our server-side SDKs](https://docs.stripe.com/upgrades.md#specify-sdk-api-version).

View which API versions your integration uses in the [Overview tab](https://dashboard.stripe.com/workbench/overview) of [Workbench](https://docs.stripe.com/workbench/overview.md).

Review the [Changelog](https://docs.stripe.com/changelog.md) to find the target version for your upgrade.

## Specify the API version in your SDK

Your account has a *default API version* (The API version set the first time you make an API request. If your API requests don't specify an API, Stripe uses your account's default API version) that defines how you call the API, what functionality you have access to, and the structure of API responses. When you use a [server-side SDK](https://docs.stripe.com/sdks.md#server-side-libraries), your API calls to Stripe use the API version that was current when the SDK was released. You can’t target a different API version when using a strongly typed language, such as Java, Go, or .NET.

#### Ruby

The [stripe-ruby](https://github.com/stripe/stripe-ruby) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-ruby use the API version that was latest at the time your version of stripe-ruby was released. Versions of stripe-ruby before [v9](https://github.com/stripe/stripe-ruby/blob/master/CHANGELOG.md#900---2023-08-16) use your account’s default API version.

To set the API version **globally** with the SDK, assign the version to the `Stripe.api_version` property:

```ruby
require 'stripe'
# Don't put any keys in code. See /keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>', stripe_version: '2026-08-26.dahlia')
```

Or set the version per-request:

```ruby
require 'stripe'
# Don't put any keys in code. See /keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')
intent = client.v1.payment_intents.retrieve(
  'pi_1DlIVK2eZvKYlo2CW4yj5l2C',
  {
    stripe_version: '2026-08-26.dahlia',
  },
)
intent.capture
```

> When you override the version globally or per-request, the API response objects are also returned in that version.

#### Python

The [stripe-python](https://github.com/stripe/stripe-python) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-python use the API version that was latest at the time your version of stripe-python was released. Versions of stripe-python before [v6](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#600---2023-08-16) use your account’s default API version.

To set the API version **globally** with the SDK, assign the version to the `stripe.api_version` property:

```python
import stripe
# Don't put any keys in code. See /keys-best-practices.
stripe.api_key = <<YOUR_SECRET_KEY>>
stripe.api_version = '2026-08-26.dahlia'
```

Or set the version per-request:

```python
import stripe
intent = stripe.PaymentIntent.retrieve(
  "pi_1DlIVK2eZvKYlo2CW4yj5l2C",
  stripe_version="2026-08-26.dahlia",
)
intent.capture()
```

> When you override the version globally or per-request, the API response objects are also returned in that version.

#### PHP

The [stripe-php](https://github.com/stripe/stripe-php) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-php use the API version that was latest at the time your version of stripe-php was released. Versions of stripe-php before [v11](https://github.com/stripe/stripe-php/blob/master/CHANGELOG.md#1100---2023-08-16) use your account’s default API version.

To set the API version **globally** with the SDK, pass the version to the `\Stripe\Stripe::setApiVersion()` method:

```php
$stripe = new \Stripe\StripeClient([
  // Don't put any keys in code. See /keys-best-practices.
  "api_key" => "<<YOUR_SECRET_KEY>>",
  "stripe_version" => "2026-08-26.dahlia"
]);
```

Or set the version per-request:

```php
$intent = $stripe->paymentIntents->capture(
  'pi_1DlIVK2eZvKYlo2CW4yj5l2C',
  [],
  ['stripe_version' => '2026-08-26.dahlia']
);
```

> When you override the version globally or per-request, the API response objects are also returned in that version.

#### Java

Because Java is a strongly-typed programming language, the API version used in the SDK is *fixed* and is the latest API version at the time of the SDK release.

We don’t recommend setting a different API version for strongly-typed programming languages, because the response objects might not match the strong types in the SDK and result in request failures. For example, if the API version you’re targeting requires parameters that aren’t present in the SDK types, the request fails.

#### Node

The [stripe-node](https://github.com/stripe/stripe-node) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-node will use the API version that was latest at the time your version of stripe-node was released. Versions of stripe-node before [v12](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1200---2023-04-06) use your account’s default API version.

To set the API version **globally** with the SDK, provide the `apiVersion` option:

```javascript
// Don't put any keys in code. See /keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-08-26.dahlia',
});
```

Or set the version per-request:

```javascript
const intent = await stripe.paymentIntents.retrieve('pi_1DlIVK2eZvKYlo2CW4yj5l2C', {
  apiVersion: '2026-08-26.dahlia',
});
```

#### Typescript usage

The TypeScript types reflect the latest API version at the time of release. This version is encoded in the [API_VERSION file](https://github.com/stripe/stripe-node/blob/master/API_VERSION).

Import Stripe as a default import and instantiate it as `new Stripe()` with the latest API version.

```javascript
import Stripe from 'stripe';
const stripe = new Stripe('<<YOUR_PUBLISHABLE_KEY>>', {
  apiVersion: '2026-08-26.dahlia'
});
```

#### Go

Because Go is a strongly-typed programming language, the API version used in the SDK is *fixed* and is the latest API version at the time of the SDK release.

We don’t recommend setting a different API version for strongly-typed programming languages, because the response objects might not match the strong types in the SDK and result in request failures. For example, if the API version you’re targeting requires parameters that aren’t present in the SDK types, the request fails.

#### .NET

Because C# is a strongly-typed programming language, the API version used in the .NET SDK is *fixed* and is the latest API version at the time of the SDK release.

We don’t recommend setting a different API version for strongly-typed programming languages, because the response objects might not match the strong types in the SDK and result in request failures. For example, if the API version you’re targeting requires parameters that aren’t present in the SDK types, the request fails.

#### cURL

```sh
curl https://api.stripe.com/v1/charges \
  -u <<YOUR_SECRET_KEY>>: \
  -H "Stripe-Version: 2026-08-26.dahlia"
```

#### Stripe CLI

```sh
stripe charges create --stripe-version 2026-08-26.dahlia
```

## Update your code to handle API changes

Review your most important requests and update your code to handle changes to the response. For each request, review the [relevant breaking changes in the changelog](https://docs.stripe.com/changelog.md?api_usage=true) to understand the changes required to adopt your target version.

View your API requests in the [Overview tab](https://dashboard.stripe.com/workbench/overview) of [Workbench](https://docs.stripe.com/workbench/overview.md).

## Update your event destinations

> [Thin events](https://docs.stripe.com/event-destinations.md#thin-events) for API v1 resources are available in private preview. You can use them to streamline integration upgrades without changing your webhook configuration. Previously, thin events only supported API v2 resources. [Learn more and request access](https://docs.google.com/forms/d/e/1FAIpQLSeEkqzB02afvlklMkqwA6wsBH90eW8gxmc-hBOvqe2N6TRujQ/viewform?usp=dialog).

Review each event destination that receives snapshot events, including webhook endpoints and cloud destinations for Amazon EventBridge and Azure Event Grid. For snapshot events, the destination’s [snapshot_api_version](https://docs.stripe.com/api/v2/core/event-destinations/object.md#v2_event_destination_object-snapshot_api_version) property controls the API version used to render the event payload. This setting is independent of the API version used by your server-side SDK. Thin event payloads are unversioned.

You can set `snapshot_api_version` only when you create an event destination. To use a different API version, create and test a destination configured with that version before deleting the existing destination. If both destinations are active during the migration, your event handler must be idempotent because Stripe delivers subscribed events to both destinations.

## Update your webhook endpoints

To upgrade your webhook endpoints, you need to [verify incoming webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) and allow traffic from Stripe [public IP addresses](https://docs.stripe.com/ips.md). You also need to create new endpoints, redirect traffic to them, then disable the old endpoints.

#### Create new disabled webhook endpoints

Create a new webhook endpoint with the following parameters:

- `url`: the same URL as your original webhook endpoint, but add a query parameter to distinguish between events sent to the two different endpoints. For example `https://example.com/webhooks?version=2024-04-10`.
- `enabled_events`: the same events as your original webhook endpoint.
- `api_version`: the API version you want to upgrade to. If you’re upgrading to the latest API version, you can use the Dashboard or the API to create the endpoint. For other versions, use the API to set a specific version.

After you create the new webhook endpoint, disable it. You’ll re-enable it in the next step.
![Two endpoints, but only the old one is sending events](https://b.stripecdn.com/docs-statics-srv/assets/diagram-1.ac21ab637180179813f503649b543e99.png)

#### Update your webhook code to ignore events sent to the new endpoint

Update your event processing code:

- If the query parameter is for the older API version, process it as usual.
- If the query parameter is for the newer API version, ignore the event and return a 200 response to prevent delivery retries.

Next, enable the new webhook endpoint that you created in the previous step. At this point every event is sent twice: once with the old API version and once with the new one.
![Two endpoints sending events, but only processing the old one](https://b.stripecdn.com/docs-statics-srv/assets/diagram-2.f6b4d3cc0c78971b721fe173f19d5e28.png)

#### Update your webhook code to process events for the new endpoints

Update your event processing code:

- If the query parameter is for the older version, ignore the event. We recommend returning a 400 status to let Stripe automatically retry the event. This ensures that if you need to revert, events are re-sent to the older webhook endpoint.
- If the query parameter is for the new version, process it.
![Two endpoints sending events, but only processing the new one](https://b.stripecdn.com/docs-statics-srv/assets/diagram-3.8a8b9da70ed66eca60434d406c82f476.png)

#### Monitor your webhook endpoints

Monitor traffic to the new webhook endpoints to confirm that they process events correctly.

If events aren’t being correctly handled by your new code, try the following:

1. Revert to the earlier version of your code.
2. Temporarily disable the new webhook endpoint.
3. Process the failed events (if you returned a 400 status as described in the previous step, Stripe automatically resends all the events).
4. Investigate and fix the issue.
5. Enable the new webhook endpoint and resume monitoring.

#### Disable the old webhook endpoint

After the upgrade is successful, disable the old webhook endpoint to stop your server from returning `400` status. If you don’t disable it, this may cause issues with integrations that rely on a `200` response.

After you disable the old webhook endpoint, Stripe won’t re-deliver events that returned a `400`.
![Two endpoints, but only the new one is sending events](https://b.stripecdn.com/docs-statics-srv/assets/diagram-4.907bbd1016f9fbe79283e8c35be7f3cd.png)

## Test and monitor your integration

[Test your integration](https://docs.stripe.com/testing.md) in a [sandbox](https://docs.stripe.com/sandboxes.md) to confirm that it handles the new version as expected.

In addition to the general testing guidance, follow the guidelines for the products and resources that your integration uses:

- [Billing](https://docs.stripe.com/billing/testing.md): Use [test clocks](https://docs.stripe.com/billing/testing/test-clocks.md) to [simulate subscriptions](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions.md).
- [Invoicing](https://docs.stripe.com/invoicing/integration/testing.md): Test webhook notifications, payment failures, and other scenarios.
- [Connect](https://docs.stripe.com/connect/testing.md): Create [test accounts](https://docs.stripe.com/connect/testing.md?accounts-namespace=v2#creating-accounts) and use them for [verification testing](https://docs.stripe.com/connect/testing-verification.md).
- [Terminal](https://docs.stripe.com/terminal/references/testing.md): Test [simulated reader updates](https://docs.stripe.com/terminal/references/testing.md?terminal-card-present-integration=terminal#simulated-reader-updates).
- [Payment Intents](https://docs.stripe.com/payments/quickstart-payment-intents.md#test-payment): Create PaymentIntents and use test card numbers to simulate payments.

