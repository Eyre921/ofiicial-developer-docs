---
title: "The Customer object"
source: https://docs.stripe.com/api/customers/object.md
path: api/customers/object
---

# The Customer object

### The Customer object

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1680893993,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "email": "jennyrosen@example.com",
  "invoice_prefix": "0759376C",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none",
  "test_clock": null
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- [`address`](https://docs.stripe.com/api/customers/object.md?query=address) (object, nullable)
  The customer’s address.

- `balance` (integer)
  The current balance, if any, that’s stored on the customer in their default currency. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that’s added to their next invoice. The balance only considers amounts that Stripe hasn’t successfully applied to any invoice. It doesn’t reflect unpaid invoices. This balance is only taken into account after invoices finalize. For multi-currency balances, see [invoice_credit_balance](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_credit_balance).

- `business_name` (string, nullable)
  The customer’s business name.

  The maximum length is 150 characters.

- [`cash_balance`](https://docs.stripe.com/api/customers/object.md?query=cash_balance) (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The current funds being held by Stripe on behalf of the customer. You can apply these funds towards payment intents when the source is “cash_balance”. The `settings[reconciliation_mode]` field describes if these funds apply to these payment intents manually or automatically.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (string, nullable)
  Three-letter [ISO code for the currency](https://docs.stripe.com/currencies.md) the customer can be charged in for recurring billing purposes.

- `customer_account` (string, nullable)
  The ID of an Account representing a customer. You can use this ID with any v1 API that accepts a customer_account parameter.

- `default_source` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the default payment source for the customer.

  If you use payment methods created through the PaymentMethods API, see the [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) field instead.

- `delinquent` (boolean, nullable)
  Tracks the most recent state change on any invoice belonging to the customer. Paying an invoice or marking it uncollectible via the API will set this field to false. An automatic payment failure or passing the `invoice.due_date` will set this field to `true`.

  If an invoice becomes uncollectible by [dunning](https://docs.stripe.com/billing/automatic-collection.md), `delinquent` doesn’t reset to `false`.

  If you care whether the customer has paid their most recent subscription invoice, use `subscription.status` instead. Paying or marking uncollectible any customer invoice regardless of whether it is the latest invoice for a subscription will always set this field to `false`.

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- [`discount`](https://docs.stripe.com/api/customers/object.md?query=discount) (object, nullable)
  Describes the current discount active on the customer, if there is one.

- `email` (string, nullable)
  The customer’s email address.

- `individual_name` (string, nullable)
  The customer’s individual name.

  The maximum length is 150 characters.

- `invoice_credit_balance` (map, expandable (can be expanded into an object with the `expand` request parameter))
  The current multi-currency balances, if any, that’s stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that’s added to their next invoice denominated in that currency. These balances don’t apply to unpaid invoices. They solely track amounts that Stripe hasn’t successfully applied to any invoice. Stripe only applies a balance in a specific currency to an invoice after that invoice (which is in the same currency) finalizes.

- `invoice_prefix` (string, nullable)
  The prefix for the customer used to generate unique invoice numbers.

- [`invoice_settings`](https://docs.stripe.com/api/customers/object.md?query=invoice_settings) (object)
  The customer’s default invoice settings.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (map)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string, nullable)
  The customer’s full name or business name.

- `next_invoice_sequence` (integer, nullable)
  The suffix of the customer’s next invoice number (for example, 0001). When the account uses account level sequencing, this parameter is ignored in API requests and the field omitted in API responses.

- `phone` (string, nullable)
  The customer’s phone number.

- `preferred_locales` (array of strings, nullable)
  The customer’s preferred locales (languages), ordered by preference.

- [`shipping`](https://docs.stripe.com/api/customers/object.md?query=shipping) (object, nullable)
  Mailing and shipping address for the customer. Appears on invoices emailed to this customer.

- [`sources`](https://docs.stripe.com/api/customers/object.md?query=sources) (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The customer’s payment sources, if any.

- [`subscriptions`](https://docs.stripe.com/api/customers/object.md?query=subscriptions) (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The customer’s current subscriptions, if any.

- [`tax`](https://docs.stripe.com/api/customers/object.md?query=tax) (object, expandable (can be expanded into an object with the `expand` request parameter))
  Tax details for the customer.

- `tax_exempt` (enum, nullable)
  Describes the customer’s tax exemption status, which is `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the following text: **“Reverse charge”**.
Possible enum values:
  - `exempt`
  - `none`
  - `reverse`

- [`tax_ids`](https://docs.stripe.com/api/customers/object.md?query=tax_ids) (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The customer’s tax IDs.

- `test_clock` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the test clock that this customer belongs to.

