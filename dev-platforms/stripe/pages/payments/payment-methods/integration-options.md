---
title: "Payment method integration options"
source: https://docs.stripe.com/payments/payment-methods/integration-options.md
path: payments/payment-methods/integration-options
---

# Payment method integration options

Learn about the different ways to integrate payment methods.

If your integration uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), you can turn payment methods on or off in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) without writing code.

If your integration specifies payment methods in code, your Dashboard settings can’t add payment methods that the code doesn’t allow. A developer might need to update the integration first. Some payment methods also require activation or approval before you can offer them. See [Supported payment methods](https://docs.stripe.com/payments/payment-methods/overview.md) to learn more about all the payment methods your integration can support.

The payment methods you can offer depend on the currency, country, and Stripe products you integrate with. Use this guide to confirm that your chosen payment methods work for your business and to choose how to add them. To learn which countries, currencies, products, and API features each payment method supports, including support for subscriptions, invoices, and Checkout, see [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support).

Stripe turns on certain payment methods for you by default and might turn on additional payment methods after notifying you. To learn how Dashboard-managed payment methods apply to PaymentIntents and SetupIntents by default, see [Manage default payment methods in the Dashboard](https://docs.stripe.com/upgrades/manage-payment-methods.md).

## Before you begin 

- **Dashboard access**: Make sure you have a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) with permission to manage payment method settings.
- **Eligibility**: Confirm that your business is eligible for each payment method you want to offer. Some payment methods require activation or approval, and some are invite only.
- **Domain registration**: If you use Elements or Checkout’s embedded payment page, some payment methods, such as Apple Pay, require you to [register your domain](https://docs.stripe.com/payments/payment-methods/pmd-registration.md).
- **Connect**: If you use direct charges or `on_behalf_of`, the connected account’s payment method settings determine which payment methods are available. See [Manage payment methods for connected accounts](https://docs.stripe.com/connect/manage-payment-methods.md).

## Add payment methods 

Your customers see the available payment methods when they pay. You can either manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) or restrict payment methods in code. For detailed steps, see the guide for each payment method.

Several factors determine which payment methods a customer sees:

- **Dashboard settings**: For integrations that use dynamic payment methods, your payment method settings determine which payment methods you’ve turned on.
- **Code restrictions**: Your integration code can further limit which payment methods can appear.
- **Compatibility**: Stripe hides payment methods that don’t support the transaction, for example, because of its amount, currency, or payment flow.
- **Display order**: The payment UI, such as Checkout or the Payment Element, orders the remaining payment methods. Ordering doesn’t affect which payment methods are eligible.

### Use dynamic payment methods 

Unless your integration requires you to restrict payment methods in code, we recommend using dynamic payment methods. Stripe displays the most relevant payment methods to each customer based on your [Dashboard](https://dashboard.stripe.com/settings/payment_methods) preferences and eligibility factors, such as transaction amount, currency, and payment flow.

To keep managing payment methods in the Dashboard while excluding specific payment methods from a transaction, use [excluded_payment_method_types](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md#exclude-payment-methods).

See [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to learn more.

### Restrict payment methods in code 

Pass each payment method type you want to accept in the `allowed_payment_method_types` parameter when you create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-allowed_payment_method_types) or [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-allowed_payment_method_types). Stripe offers only the payment methods in this list that are compatible with the transaction, based on factors such as its amount, currency, and customer. The `payment_method_types` property of the response lists the compatible subset.

A payment method that isn’t in `allowed_payment_method_types` can’t appear, even if you turn it on in the Dashboard.

#### Checkout Sessions

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d mode=payment \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=2" \
  --data-urlencode "success_url=https://example.com/success" \
  -d "allowed_payment_method_types[0]=bancontact" \
  -d "allowed_payment_method_types[1]=card" \
  -d "allowed_payment_method_types[2]=eps" \
  -d "allowed_payment_method_types[3]=ideal" \
  -d "allowed_payment_method_types[4]=p24" \
  -d "allowed_payment_method_types[5]=sepa_debit"
```

#### Payment Intents

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=eur \
  -d "allowed_payment_method_types[]=bancontact" \
  -d "allowed_payment_method_types[]=card" \
  -d "allowed_payment_method_types[]=eps" \
  -d "allowed_payment_method_types[]=ideal" \
  -d "allowed_payment_method_types[]=p24" \
  -d "allowed_payment_method_types[]=sepa_debit"
```

> #### API versions
> 
> Starting with API version `2026-09-30.endive`, you can’t pass `payment_method_types` when you create Checkout Sessions, PaymentIntents, or SetupIntents. Use dynamic payment methods or `allowed_payment_method_types` instead. If your integration uses an earlier [API version](https://docs.stripe.com/upgrades.md), use the parameter documented for that version. For example, Checkout Sessions on earlier GA versions use `payment_method_types`, and PaymentIntents and SetupIntents accept `allowed_payment_method_types` starting with `2026-07-29.dahlia`.

The order of `allowed_payment_method_types` doesn’t determine the display order:

- **Checkout**: The Checkout payment page dynamically orders payment methods to prioritize the most relevant ones based on the customer’s location and other characteristics.
- **Payment Element**: The Payment Element orders payment methods dynamically by default. To override the default order, use [paymentMethodOrder](https://docs.stripe.com/payments/customize-payment-methods.md#sort-payment-methods).

## Choose your integration 

The following table compares several web integration paths, including no-code, low-code, and advanced options. For other options, such as mobile apps and embedded forms, see [Online payments](https://docs.stripe.com/payments/online-payments.md). You can also compare [features](https://docs.stripe.com/payments/online-payments.md#compare-features-and-availability) and [product support](https://docs.stripe.com/payments/online-payments.md#choose-your-api). For payment method fees, see [Stripe pricing](https://stripe.com/pricing).

You can also use [Invoicing](https://docs.stripe.com/invoicing.md) to automatically charge your customer’s saved payment method or email invoices [without writing any code](https://docs.stripe.com/invoicing/no-code-guide.md). See the [payment methods supported by Invoicing](https://docs.stripe.com/invoicing/payment-methods.md#supported).

| &nbsp; | [**Payment Links**](https://docs.stripe.com/payment-links.md) | [**Full page (Stripe-hosted)**](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) | [**Full page (embedded)**](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-page) | [**Custom payment flow (Checkout Sessions)**](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=checkout) | [**Custom payment flow (Payment Intents)**](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=paymentintents) |
| --- | --- | --- | --- | --- | --- |
| **UI** | Payment Links + Checkout | [Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works.md?payment-ui=stripe-hosted) | [Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works.md?payment-ui=embedded-page) | [Elements](https://docs.stripe.com/payments/elements.md) | [Elements](https://docs.stripe.com/payments/elements.md) |
| **API** | [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md) | [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md) | [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md) | [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md) | [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) |
| **Integration effort** | No code required | Low coding | Low coding | More coding | Most coding |
| **Hosting** | Stripe-hosted page (optional [custom domains](https://docs.stripe.com/payments/checkout/custom-domains.md)) | Stripe-hosted page (optional [custom domains](https://docs.stripe.com/payments/checkout/custom-domains.md)) | Embed on your site | Embed on your site | Embed on your site |
| **UI customization** | Limited customization1 | Limited customization1 | Limited customization1 | Extensive customization with [Appearance API](https://docs.stripe.com/elements/appearance-api.md) | Extensive customization with [Appearance API](https://docs.stripe.com/elements/appearance-api.md) |
| **Payment methods**2 |
| [Dynamically display](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) eligible payment methods | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| Manage payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) without coding3 | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| **[Faster checkout with Link](https://docs.stripe.com/payments/link.md)** and more wallet payment methods such as [Apple Pay](https://docs.stripe.com/apple-pay.md), [Google Pay](https://docs.stripe.com/google-pay.md), and [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) | ✓ Supported | ✓ Supported | ✓ Supported 4 | ✓ Supported 4 | ✓ Supported 4 |
| **[Buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later.md)** payment methods such as [Affirm](https://docs.stripe.com/payments/affirm.md), [Afterpay/Clearpay](https://docs.stripe.com/payments/afterpay-clearpay.md), and [Klarna](https://docs.stripe.com/payments/klarna.md) | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| **Custom payment methods** | Support varies by integration. See [custom payment method integrations](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#integrations). |

1Limited customization provides [20 preset fonts](https://docs.stripe.com/payments/checkout/customization/appearance.md#font-compatibility), 3 preset border radius options, logo and background customization, and custom button color.

2For detailed support for each payment method, see [learn more about payment methods](https://docs.stripe.com/payments/payment-methods/overview.md).

3Requires an integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). If your integration specifies payment methods in code, you must update it before you can manage those payment methods in the Dashboard.

4In these integrations, some wallet payment methods, such as Apple Pay, require you to [register your domain](https://docs.stripe.com/payments/payment-methods/pmd-registration.md).

## See also

- [Quickstart](https://docs.stripe.com/payments/quickstart.md)
- [Manage default payment methods in the Dashboard](https://docs.stripe.com/upgrades/manage-payment-methods.md)

