---
title: "plan your integration"
source: https://docs.stripe.com/billing/subscriptions/design-an-integration.md
path: billing/subscriptions/design-an-integration
---

# Design a subscriptions integration

Learn about the configuration options for a subscriptions integration.

Use this guide to learn the different ways to build your subscriptions integration, and follow the links to in-depth, step-by-step guides. You’ll need to consider the following:

- [How you want to charge customers](https://docs.stripe.com/billing/subscriptions/design-an-integration.md#pricing-model)
- [How you want your customers to check out and provide their payment information](https://docs.stripe.com/billing/subscriptions/design-an-integration.md#checkout-options)
- [When you want customers to pay for the subscription](https://docs.stripe.com/billing/subscriptions/design-an-integration.md#select-billing-model)

## Decide how you want to charge customers 

Compare the following pricing models and determine how you want to charge your customers for the subscription to your product or service:

| Pricing model | Description | Example |
| --- | --- | --- |
| [Flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing.md) | Charge customers a flat rate for each service tier. | You offer two service tiers, each with a fixed price:
- Standard: 20 USD per month or 200 USD per year
- Pro: 50 USD per month or 500 USD per year |
| [Per-seat pricing](https://docs.stripe.com/subscriptions/pricing-models/per-seat-pricing.md) | Charge customers a single rate per user or unit license. | If you offer the prices from the flat rate example as per-seat licenses, a customer pays the following rates for 12 licenses:
- Standard: 240 USD per month or 2400 USD per year
- Pro: 600 USD per month or 6000 USD per year |
| [Tiered pricing](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing.md) | Charge customers a per-seat rate that varies based on tiers of quantity or usage. There are two options:
- **Volume-based pricing**: Charge a single rate based on the tier corresponding to the total quantity or usage for the period.
- **Graduated pricing**: Charge a combination of rates based on the quantity or usage within each tier for the period, one rate per tier. | - **Volume-based pricing**: You offer three tiers:

  - For customers using 1-10 seats, you charge 15 USD per seat for that month.
  - For customers using 11-20 seats, you charge 12 USD per seat for that month.
  - For customers using 21 or more seats, you charge 10 USD per seat for that month.

  A customer using 18 seats pays 18 x 12 USD = 216 USD per month.

  A customer using 25 seats pays 25 x 10 USD = 250 USD per month.

- **Graduated pricing**: You offer three tiers:

  - For the first 10 seats that a customer uses, you charge 15 USD per seat for that month.
  - For the second 10 seats that a customer uses, you charge 12 USD per seat for that month.
  - For each seat beyond 20 that a customer uses, you charge 10 USD per seat for that month.

  A customer using 18 seats pays (10 x 15 USD) + (8 x 12 USD) = 150 USD + 96 USD = 246 USD per month.

  A customer using 25 seats pays (10 x 15 USD) + (10 x 12 USD) + (5 x 10 USD) = 150 USD + 120 USD + 50 USD = 320 USD per month. |
| [Usage-based billing](https://docs.stripe.com/billing/usage-based.md) | Use [Metronome](https://docs.stripe.com/billing/usage-based.md) to configure more complex pricing models based on usage. | Here are some examples of models you can implement using Metronome, based on tracking token usage:
- **Fixed fee and overage pricing**: You charge 100 USD per month for usage of up to 100 tokens. If a customer uses more than 100 tokens in a month (overage), you also charge 2 USD for each token used beyond the initial 100.

  A customer that uses 85 tokens in a month pays 100 USD.

  A customer that uses 105 tokens in a month pays 100 USD + (5 x 2 USD) = 110 USD.

- **Pay as you go pricing**: You charge a fixed rate for usage tracked over a period. You can charge per unit, per package, volume-based, or graduated. If you charge 2 USD per token:

  A customer that uses 85 tokens in a month pays 170 USD.

  A customer that uses 105 tokens in a month pays 210 USD.

- **Credit burndown pricing**: You collect prepayment for your product or service, and allow customers to apply billing credits as they use your product or service. If you collect 100 USD from each customer at the beginning of the month, and charge 2 USD per token used:

  A customer that uses 35 tokens in the month has 100 USD - (35 x 2 USD) = 30 USD credit remaining at the end of the month.

  A customer that uses 70 tokens in the month runs out of credit after using 50 tokens, and must purchase at least (20 x 2 USD) = 40 USD in credit before they can use the 20 remaining tokens they need. |

## Decide how customers check out 

Compare the following checkout interfaces and determine how you want your customers to provide their payment information for the subscription to your product or service.

| Interface | Description | Example |
| --- | --- | --- |
| **Stripe-hosted page** | Use a [payment page](https://docs.stripe.com/checkout/quickstart.md) that’s prebuilt and hosted by Stripe.

Benefits:

- Stripe handles payment method collection and validation.
- Stripe automatically starts the subscription process.

UI customization: 20 preset fonts, 3 preset border radiuses, custom background and border color, and custom logo | ![](https://b.stripecdn.com/docs-statics-srv/assets/checkout-subs-preview.d409ee79bf1f3280b9dfd3968b314c21.png) |
| **Embedded payment page** | Embed a [payment page](https://docs.stripe.com/checkout/embedded/quickstart.md) that’s prebuilt and hosted by Stripe directly into your site.

Benefits:

- Stripe handles payment method collection and validation.
- Stripe automatically starts the subscription process.

UI customization: 20 preset fonts, 3 preset border radiuses, custom background and border color, and custom logo | ![](https://b.stripecdn.com/docs-statics-srv/assets/embedded-checkout-form-preview.23a56550b7d522d8437b2beac672410f.png) |
| **Custom payment form** | Build a [custom payment form](https://docs.stripe.com/payments/advanced.md) using UI components that you can integrate on your website.

Benefits:

- Combines Stripe Elements with the front end of your web app.
- Allows you to customize the Payment Element layout to fit your checkout flow.

UI customization: Customize the look and feel of the payment form with the [Appearance API](https://docs.stripe.com/elements/appearance-api.md). | ![](https://b.stripecdn.com/docs-statics-srv/assets/appearance_example.e076cc750983bf552baf26c305e7fc90.png) |
| **Pricing table** | Embed a [pricing table](https://docs.stripe.com/payments/checkout/pricing-table.md) on your website to show pricing information for subscriptions.

Benefits:

- Displays a range of pricing options.
- Redirects to a Stripe-hosted payment page for the checkout flow.

UI customization: Customize the button layout, text, and appearance. | ![](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png) |
| **One-click payment button** | Accept payments through [one-click payment buttons](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment.md) for various payment methods.

Benefits:

- Allows you to add payment buttons without any front-end changes.
- Dynamically sorts payment buttons based on a customer’s location.
- Supports the following payment methods: Link, Apple Pay, Google Pay, PayPal, Klarna, and Amazon Pay.

UI customization: Customize the button layout, text, and appearance. | ![](https://b.stripecdn.com/docs-statics-srv/assets/link-in-express-checkout-element.67be6745e5a37c1c09074b0f43763cff.png) |
| **Payment link** | Create a [payment link](https://docs.stripe.com/payment-links/create.md) that you can share directly with customers. When customers click the payment link, they’re redirected to a Stripe-hosted payment page.1

Benefits:

- Allows you to accept payments using a payment link that you can share as many times as you want.

- Uses your customer’s preferred browser language.

- Supports more than 20 payment methods, including credit and debit cards, Apple Pay, and Google Pay.

- Allows you to customize the UI with 20 preset fonts, 3 preset border radiuses, custom background and border color, and custom logo | ![](https://b.stripecdn.com/docs-statics-srv/assets/payment-link.4f7ea42c63046f6714ffe620059f1a3c.png) |
| **Mobile app** | Use a payment form that’s prebuilt and hosted by Stripe [in your mobile app](https://docs.stripe.com/payments/mobile.md).

Benefits:

- Allows you to use a prebuilt sheet or a customizable drop-in component on any screen in your app.
- Supports wallet payments, such as Apple Pay, Google Pay, and Link.

UI customization: Customize the look and feel of the payment form with the [Appearance API](https://docs.stripe.com/elements/appearance-api.md). | ![](https://b.stripecdn.com/docs-statics-srv/assets/ios-landing.35eb3fe43605b2b982353f4bdac95840.png) |

1Payment links aren’t supported for usage-based billing.

## Decide when you want customers to pay 

Compare the following models and determine when you want your customers to pay for the subscription to your product or service.

| Billing model | Description |
| --- | --- |
| **Pay up front** | Require that your customers pay before you provide access to your product or service.

A typical flow looks like this:

1. Your customer chooses their subscription plan.
2. You collect payment information.
3. You provision access to your product or service.
4. You continue to provision access to the customer throughout the subscription lifecycle.
5. After the initial charge, you continue to charge the customer the same fixed price for the same service at regular periods. |
| **Free trial** | Offer your customers a free trial period for your product or service before billing them.

A typical flow looks like this:

1. Your customer chooses their subscription plan.
2. You collect payment information, but don’t charge the customer.
3. You provision access to your product or service for a limited time.
4. When the trial ends, a new billing period starts.
5. Stripe generates an invoice with the price you defined for your service. |
| **Freemium** | Allow customers access to your product or service without requesting payment information.

A typical flow looks like this:

1. Your customer chooses their subscription plan.
2. You provision access to your product or service for a limited time.
3. Before the trial ends, you collect payment information.
4. When the trial ends, a new billing period starts.
5. Stripe generates an invoice with the price you defined for your service. |

## Build your subscriptions integration

| Pricing model | Checkout interface | Billing model | Use case | Instructions |
| --- | --- | --- | --- | --- |
| Flat rate | Payment page or embedded form | Free trial | You want to offer a free trial period for your subscription and collect a payment method to use after the trial ends. Use either a Stripe-hosted page, a Stripe-hosted payment form that’s embedded in your checkout flow, or your custom payment form. | Start a free trial period using a [Stripe-hosted page](https://docs.stripe.com/payments/checkout/free-trials.md?payment-ui=stripe-hosted), an [embedded payment page](https://docs.stripe.com/payments/checkout/free-trials.md?payment-ui=embedded-page), or a [custom payment form](https://docs.stripe.com/payments/checkout/free-trials.md?payment-ui=embedded-components) |
| Usage-based | Payment page, embedded form, or mobile app |  | You want to charge customers based on their usage of your product or service. Collect payment information using either a Stripe-hosted page, a Stripe-hosted payment form that’s embedded in your checkout flow, your custom payment form, or a payment form in your mobile app. | [Set up usage-based billing](https://docs.stripe.com/billing/usage-based.md) |
| Flat rate, per-seat, or tiered | Pricing table | Free trial | You want to display different subscription pricing levels in a pricing table that’s embedded on your website. You can offer a flat rate, per-seat or tiered pricing, or a free trial. After choosing a pricing level, customers can provide their payment information in a prebuilt payment form. | Create and [embed a pricing table](https://docs.stripe.com/payments/checkout/pricing-table.md) on your website |
| Flat rate | Payment link | Pay up front | You want to sell subscriptions for a flat rate, and collect payment information using a payment link that you share with your customers. The payment link redirects to a Stripe-hosted payment page.2 | [Create your subscription](https://docs.stripe.com/no-code/subscriptions.md) and then [create a payment link](https://docs.stripe.com/payment-links/create.md?pricing-model=standard) for your subscription |
| Flat rate | Mobile app | Pay up front | You want to sell subscriptions for a flat rate. Collect payment information using a custom payment form that’s embedded in your mobile app. | Create and embed a payment form in your [iOS app](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=mobile&platform=ios), [Android app](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=mobile&platform=android), or [React Native app](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=mobile&platform=react-native) |
| Flat rate | One-click payment buttons | Pay up front | You want to sell subscriptions for a flat rate. Collect payment information using one-click payment buttons on either a Stripe-hosted payment page, a Stripe-hosted payment form that’s embedded in your checkout flow, or your custom payment form. | [Add one-click payment buttons](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment.md) on your checkout page |

2Payment links aren’t supported for usage-based billing.

