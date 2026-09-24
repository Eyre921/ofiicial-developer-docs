---
title: "Automatically collect tax on Payment Links"
source: https://docs.stripe.com/tax/payment-links.md
path: tax/payment-links
---

# Automatically collect tax on Payment Links

Learn how to calculate and collect tax on a payment page without writing any code.

> [Log in](https://dashboard.stripe.com/settings/tax) or [sign up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

You can use Stripe Tax with [Payment Links](https://stripe.com/payments/payment-links) to automatically calculate and collect tax on a payment page and share a link to it with your customers, without writing any code.
[Watch on YouTube](https://www.youtube.com/watch?v=aotUFvYtmys)
Stripe only calculates tax in jurisdictions where you have an active [tax registration](https://docs.stripe.com/tax/registering.md). Without a registration in the customer’s location, the calculation returns zero tax. To learn more, see [Understand zero tax amounts](https://docs.stripe.com/tax/zero-tax.md).

> #### Transfer tax liability to Stripe
> 
> If you sell digital products, [Managed Payments](https://docs.stripe.com/payments/managed-payments/tax-compliance.md) allows you to offload tax liability to Stripe so we’re directly responsible for handling sales tax, VAT, or GST globally. As a merchant of record solution, Managed Payments also handles fraud prevention, dispute management, and customer support on all transactions.

Before you start, confirm that your Stripe Tax settings are complete.

#### Dashboard

To [create a payment link](https://docs.stripe.com/payment-links/create.md) in the Dashboard:

1. Open the [Payment Links](https://dashboard.stripe.com/payment-links/create) page.
2. Click **+ New**.
3. Fill out the details.
4. Enable **Collect tax automatically**.

To update an existing payment link in the Dashboard:

1. Open the [Payment Links](https://dashboard.stripe.com/payment-links) page.
2. Select the payment link you want to update.
3. On the payment link details page, click the overflow menu (⋯), then click **Edit**.
4. In the payment link editor, select **Collect tax automatically** to enable automatic tax collection on this payment link.
5. (Optional) Select **Collect customers’ addresses** to improve tax calculation accuracy. The more information you provide, the more precise the calculation.
6. Click **Update link** to save your changes.

#### API

To create a payment link with automatic tax collection, pass the `automatic_tax[enabled]` parameter to the [Payment Link API](https://docs.stripe.com/api/payment-link/create.md) endpoint:

```curl
curl https://api.stripe.com/v1/payment_links \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "automatic_tax[enabled]=true" \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=1"
```

To update an existing payment link in the API, pass the `automatic_tax[enabled]` parameter to the [Payment Link API](https://docs.stripe.com/api/payment-link/update.md) endpoint:

```curl
curl https://api.stripe.com/v1/payment_links/{{PAYMENTLINK_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "automatic_tax[enabled]=true"
```

## Optional: Collect customer tax IDs

Configure whether business customers can provide a tax ID when they pay through your payment link.

#### Dashboard

1. [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment link.
2. Expand **Advanced options**.
3. Select **Allow business customers to provide tax IDs** to let customers in supported countries optionally provide a tax ID.
4. Select **Require tax ID collection for customers in supported countries** to require those customers to provide a tax ID before completing payment. Customers in unsupported countries can complete payment without one.

See the [supported tax ID types and countries](https://docs.stripe.com/tax/checkout/tax-ids.md#supported-types).

#### API

Set [tax_id_collection[enabled]](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-tax_id_collection-enabled) to `true` when you create or update a payment link to let customers in supported countries optionally provide a tax ID.

Set [tax_id_collection[required]](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-tax_id_collection-required) to `if_supported` to require those customers to provide a tax ID before completing payment. The default value is `never`. Customers in unsupported countries can complete payment without one.

```curl
curl https://api.stripe.com/v1/payment_links \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "line_items[0][price]={{PRICE_ID}}" \
  -d "line_items[0][quantity]=1" \
  -d "tax_id_collection[enabled]=true" \
  -d "tax_id_collection[required]=if_supported"
```

You can use the same parameters when you [update a payment link](https://docs.stripe.com/api/payment-link/update.md#update_payment_link-tax_id_collection).

See the [supported tax ID types and countries](https://docs.stripe.com/tax/checkout/tax-ids.md#supported-types).

### Check validation status in the Dashboard 

Stripe displays the verification result for a tax ID saved to a Customer:

1. Open the [Customers](https://dashboard.stripe.com/customers) page.
2. Select the customer who used the payment link.
3. Find the tax ID in the customer’s **Details**. The status icon shows whether the ID is pending, verified, unverified, or unavailable. Hover over the tax ID to view any registered name and address returned by the government database.
![Tax ID verification details in the Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/validation-tooltip.de17a6f286a786e5643e39f43c02a42e.png)

The customer details page displays the tax ID verification status and available registration information.

The Dashboard displays this result only when the Payment Link saves the tax ID to an existing customer. Subscription links and links that [save payment details](https://docs.stripe.com/payment-links/customize.md#save-payment-details-for-future-use) create a new customer. A default one-time Payment Link normally uses a [guest customer](https://docs.stripe.com/payments/checkout/guest-customers.md), so its collected tax ID isn’t available on the Customers page.

Learn more about [tax ID validation and verification events](https://docs.stripe.com/tax/checkout/tax-ids.md#validation).

## Optional: Update your products and prices

Stripe Tax uses information stored on your products and prices to calculate tax, including tax codes and tax behavior. If you don’t explicitly configure these, Stripe Tax uses the defaults from your [Tax Settings](https://dashboard.stripe.com/settings/tax).

For detailed setup instructions, see [Specify product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

## See also

- [Test your tax integration](https://docs.stripe.com/tax/testing.md)
- [Reporting and filing](https://docs.stripe.com/tax/reports.md)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect.md)

