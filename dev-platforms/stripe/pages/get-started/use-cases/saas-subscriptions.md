---
title: "SaaS subscription business"
source: https://docs.stripe.com/get-started/use-cases/saas-subscriptions.md
path: get-started/use-cases/saas-subscriptions
---

# Sell subscriptions as a SaaS startup

Launch a prebuilt subscriptions integration as a SaaS startup.

This guide is for SaaS startups who want to accept recurring payments (subscriptions) using a [flat rate pricing model](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate). This means you charge a flat rate per month for your product or service at the beginning of a certain time period.

Stripe also supports other recurring pricing models, such as [per-seat](https://docs.stripe.com/products-prices/pricing-models.md#per-seat), [usage-based](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing), and [tiered](https://docs.stripe.com/products-prices/pricing-models.md#tiered-pricing) pricing. This guide implements flat-rate pricing only.

The payment flow redirects your customers to a Stripe-hosted page to enter their payment details, then returns them to your site. You use [Checkout](https://docs.stripe.com/payments/checkout.md) to create the Stripe-hosted page, which calls the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md).

## Create a Stripe account

Before integrating with Stripe, create a Stripe account.

1. [Create an account](https://dashboard.stripe.com/register) by entering your email address, full name, country, and creating a password.
2. Fill out your business profile.
3. In the Dashboard, click **Verify your email**. Stripe sends a verification email to your email address.
4. Verify your email address.

Coding agents should install the Stripe CLI (`npm i -g @stripe/cli`) and run the command `stripe sandbox create --help` to provision an anonymous Stripe sandbox with working API keys. No account registration required.

## Create a test product and price

Create products and set prices in the Dashboard.

1. [Create a test product in the Dashboard](https://dashboard.stripe.com/test/products/create).

2. Enter the product and price details:

   - Name: Enter “Plus”
   - Price: Enter “8”
   - Currency: Select **USD**

3. Upload a test product image.

4. Select **Recurring**.

5. Click **Add test product**.

## Accept subscriptions payments

To accept payments, build an integration with [Stripe-hosted Checkout](https://docs.stripe.com/payments/checkout.md), a prebuilt payment page.

Instead of building your own page to start checkout, you can embed a [pricing table](https://docs.stripe.com/payments/checkout/pricing-table.md) on your website. A pricing table displays your subscription options and sends customers to Checkout after they select one. It’s an alternative to the checkout page in this guide, not an additional step. Review the pricing table [limitations](https://docs.stripe.com/payments/checkout/pricing-table.md#limitations) before you choose it.

### Before you begin

Refer to the Stripe-hosted Checkout [quickstart](https://docs.stripe.com/checkout/quickstart.md) as you go through this step. You can download the example app or open it in VS Code.

### Set up your server

Your server communicates with the Stripe API to initialize the checkout process, but Stripe securely hosts the actual payment form. Setting up your server varies by programming language, but typically involves installing the Stripe library, configuring your API keys, and implementing the endpoints needed to create a `Checkout Session` and handle post-payment processes.

1. Open the [Quickstart](https://docs.stripe.com/checkout/quickstart.md), and select **React** for the front end, and **Node** for the back end.
2. [Install the Stripe Node library](https://docs.stripe.com/checkout/quickstart.md#init-stripe).
3. [Create a Checkout Session](https://docs.stripe.com/checkout/quickstart.md#create). A [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) is a server-side object in Stripe that defines a payment flow for a customer. The endpoint path must match the `action` attribute of your [checkout button](https://docs.stripe.com/get-started/use-cases/saas-subscriptions.md#create-your-checkout-page).
4. [Define a product to sell](https://docs.stripe.com/checkout/quickstart.md#line-items). Add the test product (“Plus”) you created earlier in the Dashboard. After you set the test product, you get a price ID value, which your front end needs to pass when creating a `Checkout Session`.
5. [Choose a payment mode](https://docs.stripe.com/checkout/quickstart.md#mode). To initiate recurring payments with subscriptions, set the `mode` to `subscription`.
6. [Supply a success URL](https://docs.stripe.com/checkout/quickstart.md#urls). Stripe redirects your customer to these pages after they complete or cancel a  payment. Host these pages on your site.
7. [Redirect your customer to the URL for the Checkout page](https://docs.stripe.com/checkout/quickstart.md#redirect). This is the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the `Checkout Session` response.

### Create your checkout page

This is a page on your site that shows the customer a summary of their order before they proceed to complete payment. They can review and modify their selections if needed.

1. [Add an order preview page](https://docs.stripe.com/checkout/quickstart.md#preview-page).
2. [Add a checkout button](https://docs.stripe.com/checkout/quickstart.md#add-button). This is the button the customer clicks on the order preview page that redirects them to the Stripe-hosted payment page.

### Test your checkout page

1. Add `"proxy": "<http://localhost:4242>"` to your `package.json` file during local development.
2. Run `npm start` and go to <http://localhost:3000/checkout>.
3. In your checkout page, enter the test card `4242424242424242` to submit a test payment as a customer.
4. (Optional) To sign up for a [Link](https://docs.stripe.com/payments/link.md) account, select **Save my information for faster checkout**. You can test Link as the payment method to see the checkout flow for a returning customer.

These steps test the initial payment only. To test how your integration handles renewals, trial transitions, and payment failures over time, use [test clocks](https://docs.stripe.com/billing/testing.md#test-clocks) to simulate subscriptions in a sandbox. Test clocks move time forward for Billing objects, such as subscriptions and invoices, and trigger the related webhook events. They don’t run the Checkout payment page.

## Additional recommended configurations

Learn how to customize your payment page, add payment methods, enable discounts, add trial periods, and set up a customer portal.

### Customize payment page

You can apply custom branding to Checkout. In the Dashboard, go to [Branding settings](https://dashboard.stripe.com/settings/branding/checkout) to:

- Upload a logo or icon
- Customize the background color, button color, font, and shapes for the page

### Add payment methods

In the [Payment methods](https://dashboard.stripe.com/settings/payment_methods) page in the Dashboard, enable the payment methods you want to accept from your customers. Checkout supports [several payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support), and [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

This means Stripe handles the logic for dynamically displaying the most relevant eligible payment methods to each customer to maximize conversion. Stripe only shows customers the payment methods they’re eligible to use, based on factors such as their [location](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#country-currency-support) or whether the payment method [supports subscriptions](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support).

### Enable discounts

Use discounts to attract and retain subscribers. You can create coupons and apply them to subscriptions, or create customer-facing promotion codes that customers enter in Checkout. Learn how to [add coupons and promotion codes to subscriptions](https://docs.stripe.com/billing/subscriptions/coupons.md).

### Add trial periods

Configure a `Checkout Session` to add a free trial to your customer’s subscription by passing one of the following parameters:

- [subscription_data.trial_period_days](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days): the length (in days) of your free trial
- [subscription_data.trial_end](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end): a Unix timestamp representing the end of the trial period

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d mode=subscription \
  --data-urlencode "success_url=https://example.com/success" \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=1" \
  -d "subscription_data[trial_period_days]=30"
```

You can also let customers start a trial without entering payment details, and automatically email customers before their trial ends. Learn more about [free trials in Checkout](https://docs.stripe.com/payments/checkout/free-trials.md).

### Add a customer portal

Your customers manage their existing subscriptions and invoices in a customer portal. Use the [Dashboard](https://dashboard.stripe.com/test/settings/billing/portal) to create the portal. At a minimum, make sure to configure it so that customers can update their payment methods.

Depending on how you configure the portal, customers can also change or cancel their subscriptions, update their billing information, and review their invoice history. Learn how to [set up the customer portal](https://docs.stripe.com/customer-management.md).

## Monitor your subscriptions

To monitor subscriptions for your Stripe-hosted Checkout integration, you can set up an endpoint to listen to specific webhook events that occur throughout the subscription lifecycle.

### Set up a webhook endpoint

1. Create a webhook endpoint on your server to receive event notifications from Stripe.

2. In the Dashboard, register this endpoint in your [webhook settings](https://dashboard.stripe.com/webhooks).

3. Implement webhook signature verification for security using your webhook secret. If you don’t know your `STRIPE_WEBHOOK_SECRET` key, go to the destination details view of the [Webhooks tab](https://dashboard.stripe.com/workbench/webhooks) in Workbench to view it.

4. In [Workbench](https://dashboard.stripe.com/workbench/webhooks), select the events you want.

5. Enter the endpoint’s name, URL, and description in the Dashboard.

6. Monitor the following events at minimum (for more events, see [Subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks.md)):

| Event name                   | Description                                                                            | Your response                                                                                                                                                                                                                                                                           |
| ---------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `checkout.session.completed` | Sent when a customer successfully completes checkout, informing you of a new purchase. | Use [entitlements](https://docs.stripe.com/billing/entitlements.md) to grant access to your product’s features. Entitlements also help you determine when to revoke feature access.                                                                                                     |
| `invoice.paid`               | Sent each billing period when a payment succeeds.                                      | For monthly billing, continue to provision the subscription each month as you receive `invoice.paid` events. Examine the event type and parse the payload of each event object. Store the `subscription.id` and `customer.id` event objects in your database for verification purposes. |
| `invoice.payment_failed`     | Sent each billing period if there’s an issue with your customer’s payment method.      | Notify your customer and direct them to the customer portal to update their payment method.                                                                                                                                                                                             |

> The `checkout.session.completed` event tells your integration that the customer completed checkout, but payment can still be pending for delayed-notification payment methods. Before provisioning access, wait for `invoice.paid` or [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded), and verify the subscription or payment status. These events don’t reset the subscription’s billing period. Learn more about [when the initial billing period starts](https://docs.stripe.com/billing/subscriptions/overview.md#confirm-payment).

### Set the billing cycle

You can explicitly set a subscription’s billing cycle anchor to a fixed date (for example, the 1st of the next month) when creating a `Checkout Session`. The billing cycle anchor determines the first full invoice date, when customers are billed the full subscription amount. For example, a monthly subscription created on May 15 with an anchor on June 1 is first initially billed on May 15, then always on the 1st of the month.

To configure a billing cycle anchor, set the [subscription_data.billing_cycle_anchor](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-billing_cycle_anchor) parameter when you create a `Checkout Session` in `subscription` mode. The anchor must be a future UNIX timestamp before the next natural subscription billing date.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=1" \
  -d mode=subscription \
  --data-urlencode "success_url=https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  -d "subscription_data[billing_cycle_anchor]=1611008505"
```

If the billing cycle anchor is during a session’s active period and a customer attempts payment after it has passed, Checkout displays and charges for the full period starting with the billing cycle anchor instead of the prorated period before the billing cycle anchor.

To learn more, see [Set the billing cycle date](https://docs.stripe.com/payments/checkout/billing-cycle.md).

## Go live

1. In the Dashboard, open your [Account settings](https://dashboard.stripe.com/account/onboarding).
2. Enter your business type, tax details, business details, personal verification information, and customer-facing information (for example, a statement descriptor).
3. Add bank details to confirm where to pay out your money.
4. Set up two-step authentication to secure your account.
5. You can optionally add automatic tax collection or revenue-based climate donations.
6. Review the information you entered, and click **Agree and submit**.
7. After you activate your profile, Stripe updates you from sandbox mode to live mode.

Learn more about [setting up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md).

## Next steps

After setting up your integration, we recommend that you implement the following features:

- [Recover failed payments](https://docs.stripe.com/billing/revenue-recovery.md). In addition to notifying customers when you receive `invoice.payment_failed` events, use Smart Retries to retry failed payments and recovery emails to ask customers to update their payment details.
- [Register to collect tax](https://docs.stripe.com/tax/registering.md), then [enable and automatically collect tax](https://docs.stripe.com/tax/checkout.md) on subscriptions in a `Checkout Session`.
- [Cancel or refund a payment](https://docs.stripe.com/refunds.md). You can cancel a payment before it’s completed, or refund all or part of a payment after it succeeds.
- [Set up your bank account to receive payouts](https://docs.stripe.com/payouts.md).
- [Enable Adaptive pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md). This allows Stripe to let your customers pay in their local currency in over 150 countries.

You can also use these optional features as your business grows:

- [Send invoices](https://docs.stripe.com/invoicing/no-code-guide.md). Stripe generates an invoice for each subscription billing period. You can also invoice customers for custom deals or one-time charges.
- [Automate revenue recognition](https://docs.stripe.com/revenue-recognition.md). If you use accrual accounting, Revenue Recognition generates revenue reports from your payments and billing transactions.

