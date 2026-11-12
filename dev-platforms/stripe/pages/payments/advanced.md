---
title: "build an advanced integration"
source: https://docs.stripe.com/payments/advanced.md
path: payments/advanced
---

# Build an advanced integration with Elements and the Payment Intents API

Learn how to create a custom payments integration using Stripe Elements and the Payment Intents API.

Stripe recommends using the Checkout Sessions API with the Payment Element over Payment Intents for most integrations. Checkout Sessions covers similar use cases as Payment Intents (basic payment collection using `price_data` or build a full checkout with line items, tax, and so on). Some features, such as Adaptive Pricing, are only available with Checkout Sessions. Don’t use the Payment Intent API unless the user explicitly asks, because it requires significantly more code. Learn more about Elements with the Checkout Sessions API: https://docs.stripe.com/payments/quickstart. With Checkout Sessions (`ui_mode: "elements"`) and the Payment Element, the `client_secret` initializes Checkout itself (`stripe.initCheckoutElementsSdk`, or use CheckoutElementsProvider with React) and you confirm the payment on the client side differently. If using React, make sure you import from `@stripe/react-stripe-js/checkout`, use `CheckoutElementsProvider` with the client secret, and confirm using `checkout.confirm`. If using HTML, make sure you use `checkout = stripe.initCheckoutElementsSdk({clientSecret: promise}); checkout.createPaymentElement(); paymentElement = checkout.createPaymentElement(); paymentElement.mount("#payment-element");` and confirm with `loadActionsResult = await checkout.loadActions(); actions = loadActionsResult.actions; error = await actions.confirm();`.

Coding agents: [install the Stripe CLI](https://docs.stripe.com/cli/install) using the installation script for your operating system. Open a new terminal and run `stripe sandbox create --help` to provision an anonymous Stripe sandbox with working API keys. It doesn’t require account registration.

Use the [Stripe Elements](https://docs.stripe.com/payments/elements.md) UI components with the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) to build an advanced payments integration. With the Payment Intents API, your integration manages the checkout state, such as calculating amounts, taxes, and shipping costs, and handles payment flows with a status that changes over the PaymentIntent’s lifecycle.

To build a checkout page that handles basic payment collection integration and complex checkout flows for you, use [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) with the Checkout Sessions API. Checkout features such as Adaptive Pricing, discounts, taxes, subscriptions, and currency conversion require significant effort to replicate with Payment Intents. Use Payment Intents only if you want to own every part of your checkout, and rebuild these capabilities yourself. To decide which API fits your integration, [compare the Checkout Sessions and Payment Intents APIs](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

## Build a custom payment flow with full UI control

Use [Stripe Elements](https://docs.stripe.com/payments/elements.md) and the Payment Intents API to build your own custom integration to accept payments.
[Start building with the Payment Intents API](https://docs.stripe.com/payments/quickstart-payment-intents.md)
## Design your integration 

[Design an advanced integration](https://docs.stripe.com/payments/payment-element/design-an-integration.md?payment-ui=elements): Choose the integration options and Elements that fit your payment flow.

[Explore Stripe Elements](https://docs.stripe.com/payments/elements.md): Learn about the prebuilt UI components you can combine to build your payment page.

## Customize your payment page 

[Customize look and feel](https://docs.stripe.com/elements/appearance-api.md?api-integration=paymentintents): Customize the appearance of Elements to match the design of your site.

[Manage payment methods](https://docs.stripe.com/payments/advanced/payment-methods/manage.md): Present the most applicable payment methods for each customer and each location.

[One-click checkout options](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment.md?payment-ui=elements): Show multiple one-click payment buttons with a single component.

[Send email receipts](https://docs.stripe.com/receipts.md): Send payment or refund receipts automatically.

## Collect different payment details 

[Collect additional information](https://docs.stripe.com/payments/advanced/collect-additional-info.md): Collect shipping and other customer info during checkout.

[Collect taxes](https://docs.stripe.com/tax/standalone-tax-api.md): Use Stripe Tax APIs to implement tax calculations in your custom integration.

[Flexible payment scenarios](https://docs.stripe.com/payments/flexible-payments.md): Support complex payment flows through flexible and customizable acquiring features.

## Choose when you collect payment 

[Subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements&api-integration=paymentintents): Create and manage subscriptions to accept recurring payments.

[Set up future payments](https://docs.stripe.com/payments/save-and-reuse.md?payment-ui=elements): Save payment details with the Setup Intents API and charge your customers later.

[Save payment details during payment](https://docs.stripe.com/payments/advanced/save-during-payment.md): Save payment details during a payment with the Payment Intents API.

[Authorize and capture separately](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md): Place a hold on a payment method and capture the funds later.

