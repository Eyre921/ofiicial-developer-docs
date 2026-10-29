---
title: "Set up Stripe Tax"
source: https://docs.stripe.com/tax/set-up.md
path: tax/set-up
---

# Set up Stripe Tax

Enable Stripe Tax to automatically calculate and collect tax.

You can set up Stripe Tax in the Dashboard by [configuring your tax settings](https://dashboard.stripe.com/settings/tax). After you set up Stripe Tax, [enable automatic tax](https://docs.stripe.com/tax/set-up.md#integrate) in the Dashboard or in your API integration, depending on which Stripe products you use. To set up Stripe Tax programmatically, use the [Tax Settings API](https://docs.stripe.com/tax/settings-api.md). If you’re a platform or marketplace that wants to set up Stripe Tax, see [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect.md).

## Before you begin

Confirm you have:

- A [Stripe account](https://dashboard.stripe.com/register).
- Tax activated on the [Tax settings page](https://dashboard.stripe.com/settings/tax).
- For API integrations, a [secret or restricted API key](https://docs.stripe.com/keys-best-practices.md).

> #### Sign in to enable Stripe Tax
> 
> [Log in](https://dashboard.stripe.com/settings/tax) or [sign up](https://dashboard.stripe.com/register) to enable Stripe Tax.

## Watch a Dashboard setup demo 

This video shows how to enable automatic tax collection in the Dashboard. The following steps cover the same setup.
[Watch on YouTube](https://www.youtube.com/watch?v=PFzV64TjSmo)
## Set your head office address

Your head office is where your business is located or, if you sell physical goods, the address where you’re shipping goods from.

By default, Stripe uses your Stripe business address as your head office address. Confirm that the details are correct on the [Tax settings page](https://dashboard.stripe.com/settings/tax). Alternatively, you can [retrieve](https://docs.stripe.com/api/tax/settings/retrieve.md) and [update](https://docs.stripe.com/api/tax/settings/update.md) your head office address using the API.

## Select your preset tax code

A tax code is a classification of your product or service for Stripe Tax. Stripe uses the tax code to apply the correct tax rate to your transactions.

The preset product tax code applies to your [products](https://docs.stripe.com/api/products/object.md) when you don’t specify a [tax_code](https://docs.stripe.com/api/products/object.md#product_object-tax_code). To learn how tax codes affect tax behavior, see [Specify product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

You must select the most appropriate product tax code for every product or service you sell. Visit the [tax settings page](https://dashboard.stripe.com/settings/tax) to select a preset product tax code to serve as the default. Then go to the [product catalog](https://dashboard.stripe.com/products?active=true&has_tax_code=false) to confirm that the default is correct for your existing products. If not, edit each product to select a more appropriate product tax code for it.

If you sell physical goods and want to charge tax on the shipping fees, use the preset shipping tax code. Shipping fees might be taxed differently than products, so this code applies the appropriate [tax treatment](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#shipping-tax-code) for state- and country-specific rules.

## Select whether prices include tax by default

Tax behavior determines whether Stripe adds tax on top of your price or whether the price already includes tax.

To calculate the total amount, Stripe needs to know the tax behavior of each price in the transaction. The default tax behavior applies when you don’t specify [tax_behavior](https://docs.stripe.com/api/prices/object.md#price_object-tax_behavior) on a [Price](https://docs.stripe.com/api/prices/object.md).

You have three options:

- **Exclusive**: Stripe adds tax on top of the price.
- **Inclusive**: The price includes tax, so tax doesn’t change the total.
- **Automatic**: Stripe uses the price’s [currency](https://docs.stripe.com/api/prices/object.md#price_object-currency) to decide. It excludes tax for USD and CAD and includes it for all other currencies.

Learn about [tax behavior for products and prices](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior).

## Add registrations

Before you start collecting tax from your customers, you must [register](https://docs.stripe.com/tax/registering.md) with the local tax authority. A [tax registration](https://docs.stripe.com/api/tax/registrations.md) lets Stripe know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax. The [monitoring tool in the Dashboard](https://dashboard.stripe.com/tax/transactions) helps you understand where you might need to register with the local tax authority. Without a registration in the customer’s location, the calculation returns zero tax. To learn more, see [Zero tax amounts and reverse charges](https://docs.stripe.com/tax/zero-tax.md).

Go to the [Locations](https://dashboard.stripe.com/tax/locations) tab in the Dashboard to add your tax registrations. If you plan to register, you can schedule a registration to take effect on a future date. You can also [use Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register/united-states.md) in the US, or [use Taxually to register](https://docs.stripe.com/tax/use-taxually-to-register.md) outside the US.

## Enable Tax in your Stripe integration

To enable automatic tax on your Stripe integration:

#### Dashboard

After you activate Stripe Tax by clicking **Get started** on the [tax settings page](https://dashboard.stripe.com/settings/tax), Stripe Tax is automatically enabled for new transactions that you create in the Dashboard. To disable it, go to the [tax settings](https://dashboard.stripe.com/settings/tax/integrations) page.

| Product | What automatic tax does |
| --- | --- |
| [Invoicing](https://dashboard.stripe.com/invoices) | Automatically calculate tax on your invoices. To learn more, see [Automatically collect tax on invoices](https://docs.stripe.com/tax/invoicing.md). |
| [Subscriptions](https://dashboard.stripe.com/subscriptions) | Calculate the tax to collect on your recurring payments. To learn more, see [Collect taxes for recurring payments](https://docs.stripe.com/tax/subscriptions.md). |
| [Payment Links](https://dashboard.stripe.com/payment-links) | Automatically calculate and collect tax on a payment page and share a link to it with your customers. To learn more, see [Automatically collect tax on Payment Links](https://docs.stripe.com/tax/payment-links.md). |

Enabling Stripe Tax doesn’t update your existing invoices, subscriptions, and payment links. To start calculating and collecting tax on them, edit each one in the Dashboard to enable automatic tax.

#### API

If you create invoices, subscriptions, payment links, or Checkout Sessions with the API, set `automatic_tax.enabled=true` when you create each object.

For custom `PaymentIntent` flows, use the [Tax API](https://docs.stripe.com/tax/payment-intent/custom.md) to calculate and record tax instead.

Make these requests from your server using a restricted API key with write access to the relevant resource. See [best practices for managing secret keys](https://docs.stripe.com/keys-best-practices.md).

| Product | What automatic tax does |
| --- | --- |
| [Invoicing](https://docs.stripe.com/api/invoices/create.md#create_invoice-automatic_tax-enabled) | Automatically calculate tax on your invoices. To learn more, see [Automatically collect tax on invoices](https://docs.stripe.com/tax/invoicing.md?dashboard-or-api=api). |
| [Subscriptions](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-automatic_tax-enabled) | Calculate the tax to collect on your recurring payments. To learn more, see [Collect taxes for recurring payments](https://docs.stripe.com/tax/subscriptions.md#create-subscription). |
| [Payment Links](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-automatic_tax-enabled) | Automatically calculate and collect tax on a payment page and share a link to it with your customers. To learn more, see [Automatically collect tax on Payment Links](https://docs.stripe.com/tax/payment-links.md?dashboard-or-api=api). |
| [Checkout](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-automatic_tax-enabled) | Automatically calculate tax on one-time purchases and subscriptions in a Checkout Session. To learn more, see [Collect tax with Checkout](https://docs.stripe.com/tax/checkout.md). |
| [Custom flows](https://docs.stripe.com/tax/payment-intent/custom.md) | Use Stripe Tax with the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md), or collect tax on payments outside Stripe. |

Enabling automatic tax in your integration doesn’t update your existing invoices, subscriptions, and payment links. To start calculating and collecting tax on them, update each one with `automatic_tax.enabled=true`:

- [Update an invoice](https://docs.stripe.com/api/invoices/update.md#update_invoice-automatic_tax-enabled)
- [Update a subscription](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-automatic_tax-enabled)
- [Update a payment link](https://docs.stripe.com/api/payment-link/update.md#update_payment_link-automatic_tax-enabled)

## Set up filing

After you add your registrations and start collecting tax, you can set up filing to automatically submit returns and remit tax in the regions where you’re registered. Stripe and its filing partners can help you file automatically in [more than 90 countries](https://docs.stripe.com/tax/supported-countries.md) and in all US states.

Automated filing can help you:

- Prepare and submit returns automatically
- Receive email notifications and reminders to review your scheduled returns
- Track the status of each filing and payment
- View copies of your completed filings

You can [file with Stripe in the US](https://docs.stripe.com/tax/file-with-stripe.md). You can also [file with Stripe outside the US](https://docs.stripe.com/tax/file-with-stripe-outside-us.md) for simplified GST/HST registrations in Canada and non-Union One Stop Shop (OSS) registrations through Ireland. For other filings outside the US, [file with Taxually](https://docs.stripe.com/tax/file-with-taxually.md).

## Disable tax collection

To stop calculating and collecting tax in your payments integrations:

1. Turn off automatic tax calculation on the [tax settings page](https://dashboard.stripe.com/settings/tax) in the Dashboard.
2. Remove active tax registrations on the [Locations](https://dashboard.stripe.com/tax/locations) tab in the Dashboard.
3. Turn off automatic tax on each existing [subscription](https://dashboard.stripe.com/subscriptions), [payment link](https://dashboard.stripe.com/payment-links), and [invoice](https://dashboard.stripe.com/invoices).

Instead of using the Dashboard, you can set `automatic_tax.enabled=false` when you update a [subscription](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-automatic_tax-enabled), [payment link](https://docs.stripe.com/api/payment-link/update.md#update_payment_link-automatic_tax-enabled), or [invoice](https://docs.stripe.com/api/invoices/update.md#update_invoice-automatic_tax-enabled).

If you use the API to create [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/create.md), stop setting `automatic_tax.enabled=true`. If you use the [Tax API](https://docs.stripe.com/tax/payment-intent/custom.md), remove the tax calculation calls from your custom flow.

