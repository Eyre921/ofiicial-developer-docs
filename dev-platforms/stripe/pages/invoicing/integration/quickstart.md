---
title: "Create and send an invoice"
source: https://docs.stripe.com/invoicing/integration/quickstart.md
path: invoicing/integration/quickstart
---

# Create and send an invoice

Build a sample Invoicing integration.

Use the Stripe API to create an example of an automated invoicing integration. This involves creating products, prices, and customers and using those resources to create and send an invoice to a customer.

## Before you begin

### Install the Stripe library

Use our official libraries for access to the Stripe API.

```
sudo gem install stripe
```

### Initialize the library

Initialize the library with your secret API key.

```ruby
require 'stripe'
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')
```

## Create Products, Prices, and Customers

Create a *product* (Products represent what your business sells—whether that's a good or a service) and assign it a default *price* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). You use the product and price when you create the invoice.

### Create a product with a price

```curl
curl https://api.stripe.com/v1/products \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "name=Example Services" \
  -d "default_price_data[currency]=usd" \
  -d "default_price_data[unit_amount]=10000"
```

Create a customer object to represent the person purchasing your product.

### Create a customer

```curl
curl https://api.stripe.com/v1/customers \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "email=${env:userEmail}" \
  -d "description=Customer to Invoice"
```

## Create and send the invoice

To have Stripe email the invoice to your customer with payment instructions, set the [collection_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) attribute to `send_invoice`.

To have Stripe mark an invoice as past due, add the [days_until_due](https://docs.stripe.com/api/invoices/create.md#create_invoice-days_until_due) parameter.

You can also configure Stripe to immediately pay the invoice using the customer’s default payment method by specifying `charge_automatically` for the `collection_method`. This example uses `send_invoice` to prevent unintentional customer charges.

### Create an empty invoice

```curl
curl https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "customer=${node.set-up-chapter.create-customer.create-customer-request:id}" \
  -d collection_method=send_invoice \
  -d days_until_due=30
```

Create and attach an invoice item to represent what the customer is purchasing. Use the `customer.id`, the product’s `price.id`, and the `invoice.id`. You can add up to 250 invoice items.

### Add an invoice item

```curl
curl https://api.stripe.com/v1/invoiceitems \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "customer=${node.set-up-chapter.create-customer.create-customer-request:id}" \
  --data-urlencode "pricing[price]=${node.set-up-chapter.create-product.create-product-request:default_price}" \
  --data-urlencode "invoice=${node.create-invoice-chapter.create-invoice.create-invoice-request:id}"
```

Send the invoice to the customer’s email address. Stripe [finalizes](https://docs.stripe.com/invoicing/integration/workflow-transitions.md#finalized) immediately after you send it. You can only collect payment on finalized invoices. Many jurisdictions consider a finalized invoice a legal document and limit what you can change on. Learn more about [finalized invoice restrictions](https://docs.stripe.com/invoicing/integration/workflow-transitions.md#not-editable-status).

### Send the invoice

```curl
curl -X POST https://api.stripe.com/v1/invoices/${node.create-invoice-chapter.create-invoice.create-invoice-request:id}/send \
  -u "<<YOUR_SECRET_KEY>>:"
```

The emailed invoice has a [link](https://docs.stripe.com/api/invoices/object.md#invoice_object-hosted_invoice_url) to the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md), where the customer can view and pay their invoice online. Test the payment by using `4242 4242 4242 4242` as the card number with a future date and any three-digit CVC. You can use other [test cards](https://docs.stripe.com/testing.md#use-test-cards) to test different scenarios, like failed payments.

## Next steps

- [Use incoming webhooks to get real-time updates](https://docs.stripe.com/webhooks.md)
- [Customize invoices](https://docs.stripe.com/invoicing/customize.md)
- [Automate tax collection](https://docs.stripe.com/tax/invoicing.md)

