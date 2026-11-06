---
title: "Customers"
source: https://docs.stripe.com/invoicing/customer.md
path: invoicing/customer
---

# Customers

Learn how to use the Customer object with Stripe Invoicing.

Create a customer for every new user or business you want to bill. When you create a new customer, set up a [minimal customer profile](https://docs.stripe.com/invoicing/customer.md#customer-profile) to help generate more useful invoices, and enable Smart Retries (if you’re an [Invoicing Plus](https://stripe.com/invoicing/pricing) user). After you set up your customer, you can issue one-off invoices or create *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

> #### Use the Accounts v2 API to represent customers
> 
> You can instead use customer-configured `Account` objects to represent your customers. Using `Accounts` gives you a unified way to represent your customers across Stripe products.
> 
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. Learn more about [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using `Customer` objects.

#### Dashboard

Before you create a customer, check the [Customers list](https://dashboard.stripe.com/customers) in your Dashboard to make sure that they don’t already exist. Multiple records for the same customer can cause problems later on, such as when you need to reconcile transaction history or coordinate saved payment methods.

You can create and manage customers on the [Customers page](https://dashboard.stripe.com/customers) when you don’t want to use code to create a customer, or if you want to manually bill a customer with a one-off invoice. You can also create a customer in the Dashboard during invoice creation.

### Create a customer 

When you create a new customer, you can set their account and billing information, such as **Email**, **Name**, and **Country**. You can also set a customer’s preferred language, currency, and other important details.

To create a customer, complete these steps:

1. Verify that the customer doesn’t already exist.

2. Click **Add customer**, or press **N**, on the **Customers** page.

3. As you start typing your customer’s name or email, you might see it match to a [Stripe profile](https://docs.stripe.com/get-started/account/profile.md). You can choose to attach the customer’s Stripe profile to autofill in their business information. At a minimum, enter your customer’s **Name** and **Account email**.

4. Click **Add customer** in the dialog.

### Edit a customer 

To edit a customer’s profile, complete these steps:

1. Find the customer you want to modify and click the name on the **Customers** page.

2. In the account information page, select **Actions** > **Edit information**.

3. Make your changes to the customer profile.

4. Click **Update customer**.

### Delete a customer 

To delete a customer, complete these steps:

1. Find the customer you want to delete on the **Customers** page.

2. Click the checkbox next to your customer’s name followed by **Delete**. You can also click into the customer’s details page and select **Actions** > **Delete customer**.

#### API

Before you create a new customer, verify that the customer doesn’t already exist. For example, pass an email address to the [list all customers](https://docs.stripe.com/api/customers/list.md) API.

```curl
curl -G https://api.stripe.com/v1/customers \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d email={EMAIL_ADDRESS}
```

The following example shows how to create a new customer with an email address and a default payment method. See [create a customer](https://docs.stripe.com/api/customers/create.md) for a full list of arguments you can pass to the API.

```curl
curl https://api.stripe.com/v1/customers \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "email=jenny.rosen@example.com" \
  -d payment_method=pm_card_visa \
  -d "invoice_settings[default_payment_method]=pm_card_visa"
```

## Customer profiles 

​​Use a basic customer profile for invoice and receipt generation or as a lightweight customer relationship management system (CRM) for your application. To create a minimal customer profile, set these properties:

- Email address.
- Customer name.
- Metadata with a reference to your application’s internal customer ID.

Stripe uses your customer’s [email address](https://docs.stripe.com/api/customers/object.md#customer_object-email) to notify them of payment failures. Stripe also uses email addresses to notify customers when they need to perform an action to complete a payment.

Store the internal customer ID for your application in the [metadata](https://docs.stripe.com/api/customers/object.md#customer_object-metadata) attribute. Like most Stripe resources, the `Customer` resource includes a [Metadata](https://docs.stripe.com/api/metadata.md) object hash to flexibly store contextual key-value information. To aid in auditing and support, store your internal customer ID as a key-value pair on the `Customer` resource. This allows you to search for the customer using your internal reference ID. We recommend storing Stripe customer IDs against the internal customer model of your application.

### Billing and shipping addresses 

Use the [address attributes](https://docs.stripe.com/api/customers/object.md#customer_object-address) to set a billing address for invoicing and credit notes. For physical good delivery, add a [shipping](https://docs.stripe.com/api/customers/object.md#customer_object-shipping) address.

> Invoices, credit notes, and receipts display the billing address—a common requirement for tax compliance.

### Email and PDF language localization 

When you create a customer, use the **Language** dropdown to add their preferred language. (You can also add or edit a customer’s preferred language in the **Customer details** page or when creating an invoice.) Stripe uses the chosen language to localize invoice emails and PDFs, receipt emails and PDFs, and credit note PDFs.

To update the language through the API, use the [preferred_locales](https://docs.stripe.com/api/customers/object.md#customer_object-preferred_locales) parameter. This parameter accepts an ordered list of preferred languages sorted by preference. These preferred locale values are based on [RFC-4646](https://tools.ietf.org/html/rfc4646). Examples include en for English, or fr-CA for Canadian French. To learn more, see [Customer preferred languages](https://docs.stripe.com/invoicing/customize.md#customer-language).

## Customer properties 

The following table contains additional customer properties:

| Property | Description |
| --- | --- |
| Payment properties | Stripe uses the [payment](https://docs.stripe.com/payments.md) details associated with a customer to collect payment. A customer can have multiple [payment methods](https://docs.stripe.com/payments/payment-methods.md). Separately, their [customer invoice balance](https://docs.stripe.com/invoicing/customer/balance.md), also called the customer credit balance, can offset an invoice. This invoice-adjustment ledger isn’t a payment method or a billing credit grant. Customers are single-currency, which means that after you assign a currency, invoice the customer, or set a customer credit balance, you can’t change the currency. You can see this locked state in the Dashboard in a disabled **Currency** dropdown. If you need to bill a single entity with multiple currencies, create a new customer for each currency. |
| Invoicing properties | All [invoicing-related resources](https://docs.stripe.com/api/customers/create.md#create_customer-invoice_settings) are associated with the billed customer. |
| Tax properties | You’re responsible for making sure your invoices contain the correct tax information to meet tax jurisdiction requirements, such as [tax IDs](https://docs.stripe.com/invoicing/customer/tax-ids.md), [tax status](https://docs.stripe.com/billing/customer.md#tax-status), and [addresses](https://docs.stripe.com/invoicing/customer.md#addresses). Tax IDs let you store and render one or more tax ID numbers on invoices. Use the customer-level **Tax status** setting to choose between **Taxable**, **Exempt**, and **Reverse charge**, or set the [tax_exempt](https://docs.stripe.com/api/customers/update.md#update_customer-tax_exempt) parameter through the API. |

## Common tasks 

Here are some of the common tasks you can perform with the `Customer` resource:

- **Send an invoice to a customer**: After you create the customer, you can [send them an invoice](https://docs.stripe.com/invoicing/dashboard.md#create-invoice).

- **Store invoice balance adjustments**: The [customer invoice balance](https://docs.stripe.com/billing/customer/balance.md), also called the customer credit balance, records credit and debit adjustments for future invoices. It doesn’t hold bank transfer funds.

- **Add and validate tax ID numbers**: Displaying a customer’s tax ID on an invoice is a common requirement, and Stripe allows you to add multiple tax IDs to a customer. Their tax IDs display in the header of invoice and credit note PDFs. See the [Customer tax IDs](https://docs.stripe.com/invoicing/customer/tax-ids.md) page for more details.

- **Set the currency for a customer**: You can set the default currency to charge a customer for invoices using the Dashboard by navigating to the **Customers** page, selecting your customer, and clicking **Edit** next to **Details**. See the [Multi-currency customers](https://docs.stripe.com/invoicing/multi-currency-customers.md) page for more details on billing the same customer using a different currency than their default currency.

- **Create customers in bulk**: Bulk upload Customers using [Productivity Stripe Apps](https://marketplace.stripe.com/categories/productivity).

