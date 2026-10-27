---
title: "Set payment methods per-subscription"
source: https://docs.stripe.com/billing/subscriptions/payment-methods-setting.md
path: billing/subscriptions/payment-methods-setting
---

# Set payment method types per subscription

Learn how to specify which payment method types are available for a subscription.

The subscription [payment_settings.payment_method_types](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-payment_settings-payment_method_types) parameter lets you specify which payment method types are available for a subscription. For example, you can allow a subscription to accept only cards and bank debits, even if your account supports other payment methods. This controls the allowed types instead of selecting a single default payment method.

A subscription’s [collection_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) affects which payment method types are eligible and how customers use them:

- For `send_invoice`, customers can select from the eligible payment method types when they pay on the Hosted Invoice Page. Some payment method types only support `send_invoice`.
- For `charge_automatically`, Stripe attempts payment without first showing the customer a payment method selector. The configured payment method types limit which types the invoice’s `PaymentIntent` can use. If the customer later enters an invoice payment or recovery flow, only eligible types are available.

## Before you begin

Before configuring payment method types:

- Activate payment methods in your [account settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.
- Review [payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support) for recurring payment and collection method requirements.

## Choose which payment method types can be used 

By default, Stripe automatically determines which payment method types can be used to pay a subscription’s generated *invoice* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) based on the [Invoice default payment method configuration](https://dashboard.stripe.com/settings/billing/invoice). Stripe also attempts to include the type of the applicable default payment method and filters the result based on eligibility for the invoice.

You can instead explicitly set a subscription’s [payment_settings.payment_method_types](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-payment_settings-payment_method_types), which takes priority over default invoice settings for the specific subscription. Stripe passes these payment method types to the subscription’s [setup intent](https://docs.stripe.com/api/setup_intents.md) and invoices.

For payment method-specific configuration, see [payment_settings.payment_method_options](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-payment_settings-payment_method_options).

#### Dashboard

In the Dashboard, you can select payment method types when creating a subscription that emails invoices to the customer:

1. In the Stripe Dashboard, go to the [Subscriptions](https://dashboard.stripe.com/test/subscriptions) page.
2. Click **+Create subscription**.
3. Find or add a customer.
4. Under **Payment**, select **Email invoice the customer to pay manually**.
5. Under **Payment methods**, click **Manage**.
6. Select each payment method type you want to be available for this subscription, then click **Save**.

#### API

Use an existing customer and recurring price to [create a subscription](https://docs.stripe.com/api/subscriptions/create.md). Your restricted API key needs the [subscription_write permission](https://docs.stripe.com/keys/permissions-reference.md). Follow [best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md).

Set `payment_settings.payment_method_types` to the types you want to allow:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "payment_settings[payment_method_types][0]=card" \
  -d "payment_settings[payment_method_types][1]=link"
```

> #### Include the default payment method type
> 
> If the subscription uses a [default payment method](https://docs.stripe.com/billing/invoices/subscription.md#collect-payment), include that method’s type in `payment_method_types`. Otherwise, the default payment method can’t be used to pay the subscription’s invoices.

### Payment method type eligibility 

Eligibility depends on account activation, currency, payment amount, country, collection method, and product support. Ineligible payment method types can’t be used to pay the subscription’s invoices and don’t appear in customer-facing payment flows.

If you explicitly configure an ineligible type, Stripe might return an error when creating or updating the subscription or finalizing an invoice. For more information, see [Payment method errors](https://docs.stripe.com/invoicing/payment-methods.md#payment-method-errors).

