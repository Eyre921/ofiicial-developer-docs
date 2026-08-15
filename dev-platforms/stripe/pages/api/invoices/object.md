---
title: "The Invoice object"
source: https://docs.stripe.com/api/invoices/object.md
path: api/invoices/object
---

# The Invoice object

### The Invoice object

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "account_country": "US",
  "account_name": "Stripe Docs",
  "account_tax_ids": null,
  "amount_due": 0,
  "amount_paid": 0,
  "amount_overpaid": 0,
  "amount_remaining": 0,
  "amount_shipping": 0,
  "application": null,
  "attempt_count": 0,
  "attempted": false,
  "auto_advance": false,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_reason": "manual",
  "collection_method": "charge_automatically",
  "created": 1680644467,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_NeZwdNtLEOXuvB",
  "customer_address": null,
  "customer_email": "jennyrosen@example.com",
  "customer_name": "Jenny Rosen",
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "confirmation_secret": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "due_date": null,
  "ending_balance": null,
  "footer": null,
  "from_invoice": null,
  "hosted_invoice_url": null,
  "invoice_pdf": null,
  "issuer": {
    "type": "self"
  },
  "last_finalization_error": null,
  "latest_revision": null,
  "lines": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"
  },
  "payments": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/invoice_payments"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": null,
  "number": null,
  "on_behalf_of": null,
  "parent": null,
  "payment_settings": {
    "default_mandate": null,
    "payment_method_options": null,
    "payment_method_types": null
  },
  "period_end": 1680644467,
  "period_start": 1680644467,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "shipping_cost": null,
  "shipping_details": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "draft",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subtotal": 0,
  "subtotal_excluding_tax": 0,
  "test_clock": null,
  "total": 0,
  "total_discount_amounts": [],
  "total_excluding_tax": 0,
  "total_taxes": [],
  "transfer_data": null,
  "webhooks_delivered_at": 1680644467
}
```

## Attributes

- `id` (string)
  Unique identifier for the object. For preview invoices created using the [create preview](https://docs.stripe.com/api/invoices/create_preview.md) endpoint, this id will be prefixed with `upcoming_in`.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account_country` (string, nullable)
  The country of the business associated with this invoice, most often the business creating the invoice.

- `account_name` (string, nullable)
  The public name of the business associated with this invoice, most often the business creating the invoice.

- `account_tax_ids` (array of strings, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The account tax IDs associated with the invoice. Only editable when the invoice is a draft.

- `amount_due` (integer)
  Final amount due at this time for this invoice. If the invoice’s total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the `amount_due` may be 0. If there is a positive `starting_balance` for the invoice (the customer owes money), the `amount_due` will also take that into account. The charge that gets generated for the invoice will be for the amount specified in `amount_due`.

- `amount_overpaid` (integer)
  Amount that was overpaid on the invoice. The amount overpaid is credited to the customer’s credit balance.

- `amount_paid` (integer)
  The amount, in the smallest currency unit, that was paid.

- `amount_paid_off_stripe` (integer, expandable (can be expanded into an object with the `expand` request parameter))
  Amount, in the smallest currency unit, that was paid on the invoice outside of Stripe.

- `amount_remaining` (integer)
  The difference between amount_due and amount_paid, in the smallest currency unit.

- `amount_shipping` (integer)
  This is the sum of all the shipping amounts.

- `application` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the Connect Application that created the invoice.

- `attempt_count` (integer)
  Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule. If a failure is returned with a non-retryable return code, the invoice can no longer be retried unless a new payment method is obtained. Retries will continue to be scheduled, and attempt_count will continue to increment, but retries will only be executed if a new payment method is obtained.

- `attempted` (boolean)
  Whether an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the `invoice.created` webhook, for example, so you might not want to display that invoice as unpaid to your users.

- `auto_advance` (boolean)
  Controls whether Stripe performs [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection.md) of the invoice. If `false`, the invoice’s state doesn’t automatically advance without an explicit action.

- [`automatic_tax`](https://docs.stripe.com/api/invoices/object.md?query=automatic_tax) (object)
  Settings and latest results for automatic tax lookup for this invoice.

- `automatically_finalizes_at` (timestamp, nullable)
  The time when this invoice is currently scheduled to be automatically finalized. The field will be `null` if the invoice is not scheduled to finalize in the future. If the invoice is not in the draft state, this field will always be `null` - see `finalized_at` for the time when an already-finalized invoice was finalized.

- `billing_reason` (enum, nullable)
  Indicates the reason why the invoice was created.

  - `manual`: Unrelated to a subscription, for example, created via the invoice editor.
  - `subscription`: No longer in use. Applies to subscriptions from before May 2018 where no distinction was made between updates, cycles, and thresholds.
  - `subscription_create`: A new subscription was created.
  - `subscription_cycle`: A subscription advanced into a new period.
  - `subscription_threshold`: A subscription reached a billing threshold.
  - `subscription_update`: A subscription was updated.
  - `upcoming`: Reserved for upcoming invoices created through the Create Preview Invoice API or when an `invoice.upcoming` event is generated for an upcoming invoice on a subscription.
Possible enum values:
  - `automatic_pending_invoice_item_invoice`
  - `manual`
  - `quote_accept`
  - `subscription`
  - `subscription_create`
  - `subscription_cycle`
  - `subscription_threshold`
  - `subscription_update`
  - `upcoming`

- `collection_method` (enum)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.
Possible enum values:
  - `charge_automatically`
    Attempt payment using the default source attached to the customer.

  - `send_invoice`
    Email payment instructions to the customer.

- [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md?query=confirmation_secret) (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The confirmation secret associated with this invoice. Currently, this contains the client_secret of the PaymentIntent that Stripe creates during invoice finalization.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).

- [`custom_fields`](https://docs.stripe.com/api/invoices/object.md?query=custom_fields) (array of objects, nullable)
  Custom fields displayed on the invoice.

- `customer` (string, expandable (can be expanded into an object with the `expand` request parameter))
  The ID of the customer to bill.

- `customer_account` (string, nullable)
  The ID of the account representing the customer to bill.

- [`customer_address`](https://docs.stripe.com/api/invoices/object.md?query=customer_address) (object, nullable)
  The customer’s address. Until the invoice is finalized, this field will equal `customer.address`. Once the invoice is finalized, this field will no longer be updated.

- `customer_email` (string, nullable)
  The customer’s email. Until the invoice is finalized, this field will equal `customer.email`. Once the invoice is finalized, this field will no longer be updated.

- `customer_name` (string, nullable)
  The customer’s name. Until the invoice is finalized, this field will equal `customer.name`. Once the invoice is finalized, this field will no longer be updated.

- `customer_phone` (string, nullable)
  The customer’s phone number. Until the invoice is finalized, this field will equal `customer.phone`. Once the invoice is finalized, this field will no longer be updated.

- [`customer_shipping`](https://docs.stripe.com/api/invoices/object.md?query=customer_shipping) (object, nullable)
  The customer’s shipping information. Until the invoice is finalized, this field will equal `customer.shipping`. Once the invoice is finalized, this field will no longer be updated.

- `customer_tax_exempt` (enum, nullable)
  The customer’s tax exempt status. Until the invoice is finalized, this field will equal `customer.tax_exempt`. Once the invoice is finalized, this field will no longer be updated.
Possible enum values:
  - `exempt`
  - `none`
  - `reverse`

- [`customer_tax_ids`](https://docs.stripe.com/api/invoices/object.md?query=customer_tax_ids) (array of objects, nullable)
  The customer’s tax IDs. Until the invoice is finalized, this field will contain the same tax IDs as `customer.tax_ids`. Once the invoice is finalized, this field will no longer be updated.

- `default_payment_method` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription’s default payment method, if any, or to the default payment method in the customer’s invoice settings.

- `default_source` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription’s default source, if any, or to the customer’s default source.

- [`default_tax_rates`](https://docs.stripe.com/api/invoices/object.md?query=default_tax_rates) (array of objects)
  The tax rates applied to this invoice, if any.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

- `discounts` (array of strings, expandable (can be expanded into an object with the `expand` request parameter))
  The discounts applied to the invoice. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.

- `due_date` (timestamp, nullable)
  The date on which payment for this invoice is due. This value will be `null` for invoices where `collection_method=charge_automatically`.

- `effective_at` (timestamp, nullable)
  The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated ‘Date of issue’ printed on the invoice PDF and receipt.

- `ending_balance` (integer, nullable)
  Ending customer balance after the invoice is finalized. Invoices are finalized approximately an hour after successful webhook delivery or when payment collection is attempted for the invoice. If the invoice has not been finalized yet, this will be null.

- `footer` (string, nullable)
  Footer displayed on the invoice.

- [`from_invoice`](https://docs.stripe.com/api/invoices/object.md?query=from_invoice) (object, nullable)
  Details of the invoice that was cloned. See the [revision documentation](https://docs.stripe.com/invoicing/invoice-revisions.md) for more details.

- `hosted_invoice_url` (string, nullable)
  The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.

- `invoice_pdf` (string, nullable)
  The link to download the PDF for the invoice. If the invoice has not been finalized yet, this will be null.

- [`issuer`](https://docs.stripe.com/api/invoices/object.md?query=issuer) (object)
  The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

- [`last_finalization_error`](https://docs.stripe.com/api/invoices/object.md?query=last_finalization_error) (object, nullable)
  The error encountered during the previous attempt to finalize the invoice. This field is cleared when the invoice is successfully finalized.

- `latest_revision` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The ID of the most recent non-draft revision of this invoice

- [`lines`](https://docs.stripe.com/api/invoices/object.md?query=lines) (object)
  The individual line items that make up the invoice. `lines` is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (map, nullable)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_payment_attempt` (timestamp, nullable)
  The time at which payment will next be attempted. This value will be `null` for invoices where `collection_method=send_invoice`.

- `number` (string, nullable)
  A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer’s unique invoice_prefix if it is specified.

- `on_behalf_of` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://docs.stripe.com/billing/invoices/connect.md) documentation for details.

- [`parent`](https://docs.stripe.com/api/invoices/object.md?query=parent) (object, nullable)
  The parent that generated this invoice

- [`payment_settings`](https://docs.stripe.com/api/invoices/object.md?query=payment_settings) (object)
  Configuration settings for the PaymentIntent that is generated when the invoice is finalized.

- [`payments`](https://docs.stripe.com/api/invoices/object.md?query=payments) (object, expandable (can be expanded into an object with the `expand` request parameter))
  Payments for this invoice. Use [invoice payment](https://docs.stripe.com/api/invoice-payment.md) to get more details.

- `period_end` (timestamp)
  The latest timestamp at which invoice items can be associated with this invoice. Use the [line item period](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-period) to get the service period for each price.

- `period_start` (timestamp)
  The earliest timestamp at which invoice items can be associated with this invoice. Use the [line item period](https://docs.stripe.com/api/invoices/line_item.md#invoice_line_item_object-period) to get the service period for each price.

- `post_payment_credit_notes_amount` (integer)
  Total amount of all post-payment credit notes issued for this invoice.

- `pre_payment_credit_notes_amount` (integer)
  Total amount of all pre-payment credit notes issued for this invoice.

- `receipt_number` (string, nullable)
  This is the transaction number that appears on email receipts sent for this invoice.

- [`rendering`](https://docs.stripe.com/api/invoices/object.md?query=rendering) (object, nullable)
  The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.

- [`shipping_cost`](https://docs.stripe.com/api/invoices/object.md?query=shipping_cost) (object, nullable)
  The details of the cost of shipping, including the ShippingRate applied on the invoice.

- [`shipping_details`](https://docs.stripe.com/api/invoices/object.md?query=shipping_details) (object, nullable)
  Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.

- `starting_balance` (integer)
  Starting customer balance before the invoice is finalized. If the invoice has not been finalized yet, this will be the current customer balance. For revision invoices, this also includes any customer balance that was applied to the original invoice.

- `statement_descriptor` (string, nullable)
  Extra information about an invoice for the customer’s credit card statement.

- `status` (enum, nullable)
  The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://docs.stripe.com/billing/invoices/workflow.md#workflow-overview)

- [`status_transitions`](https://docs.stripe.com/api/invoices/object.md?query=status_transitions) (object)
  The timestamps at which the invoice status was updated.

- `subtotal` (integer)
  Total of all subscriptions, invoice items, and prorations on the invoice before any invoice level discount or exclusive tax is applied. Item discounts are already incorporated

- `subtotal_excluding_tax` (integer, nullable)
  The integer amount in the smallest currency unit representing the subtotal of the invoice before any invoice level discount or tax is applied. Item discounts are already incorporated

- `test_clock` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the test clock this invoice belongs to.

- [`threshold_reason`](https://docs.stripe.com/api/invoices/object.md?query=threshold_reason) (object, nullable)
  If `billing_reason` is set to `subscription_threshold` this returns more information on which threshold rules triggered the invoice.

- `total` (integer)
  Total after discounts and taxes.

- [`total_discount_amounts`](https://docs.stripe.com/api/invoices/object.md?query=total_discount_amounts) (array of objects, nullable)
  The aggregate amounts calculated per discount across all line items.

- `total_excluding_tax` (integer, nullable)
  The integer amount in the smallest currency unit representing the total amount of the invoice including all discounts but excluding all tax.

- [`total_pretax_credit_amounts`](https://docs.stripe.com/api/invoices/object.md?query=total_pretax_credit_amounts) (array of objects, nullable)
  Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to this invoice. This is a combined list of total_pretax_credit_amounts across all invoice line items.

- [`total_taxes`](https://docs.stripe.com/api/invoices/object.md?query=total_taxes) (array of objects, nullable)
  The aggregate tax information of all line items.

- `webhooks_delivered_at` (timestamp, nullable)
  Invoices are automatically paid or sent 1 hour after webhooks are delivered, or until all webhook delivery attempts have [been exhausted](https://docs.stripe.com/billing/webhooks.md#understand). This field tracks the time when webhooks for this invoice were successfully delivered. If the invoice had no webhooks to deliver, this will be set while the invoice is being created.

