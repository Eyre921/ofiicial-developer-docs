---
title: "Link with Invoicing"
source: https://docs.stripe.com/payments/link/invoicing.md
path: payments/link/invoicing
---

# Link with Invoicing

Speed up invoice payments by using Link with the hosted invoice page.

Use [Link](https://docs.stripe.com/payments/link.md) with the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md) to let your customers pay invoices faster. Stripe assigns all invoices a unique URL that you can send to your customer. We host these invoices, which means you can securely collect payments without any extra implementation code. Link is compatible with both the [Invoices](https://docs.stripe.com/api/invoices.md) and [Subscriptions](https://docs.stripe.com/api/subscriptions.md) APIs.

For information about how your payment integration affects Link, see [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md).
![Link in the hosted invoice page](https://b.stripecdn.com/docs-statics-srv/assets/link-in-hip.a98a2864a383c265c375109b168d62ab.png)

Link in the hosted invoice page

## Enable Link in the hosted invoice page 

Your customers can pay invoices faster using Link as a payment method to autofill their payment details. The hosted invoice page provides a secure, private URL where your customers can view, pay, and download copies of the invoice.

To enable Link on the hosted invoice page:

1. Go to the [Invoice template](https://dashboard.stripe.com/settings/billing/invoice) in the Dashboard and under  **Payment methods**, click **Manage**.
2. Find Link, toggle it on, and click **Save**.

After you enable Link in the hosted invoice page, all of your customers can pay their invoices faster using Link.

