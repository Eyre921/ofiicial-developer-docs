---
title: "The Payment Link object"
source: https://docs.stripe.com/api/payment-link/object.md
path: api/payment-link/object
---

# The Payment Link object

### The Payment Link object

```json
{
  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",
  "object": "payment_link",
  "active": true,
  "after_completion": {
    "hosted_confirmation": {
      "custom_message": null
    },
    "type": "hosted_confirmation"
  },
  "allow_promotion_codes": false,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_address_collection": "auto",
  "consent_collection": null,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer_creation": "if_required",
  "invoice_creation": {
    "enabled": false,
    "invoice_data": {
      "account_tax_ids": null,
      "custom_fields": null,
      "description": null,
      "footer": null,
      "issuer": null,
      "metadata": {},
      "rendering_options": null
    }
  },
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_intent_data": null,
  "payment_method_collection": "always",
  "payment_method_types": null,
  "phone_number_collection": {
    "enabled": false
  },
  "shipping_address_collection": null,
  "shipping_options": [],
  "submit_type": "auto",
  "subscription_data": {
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "trial_period_days": null
  },
  "tax_id_collection": {
    "enabled": false
  },
  "transfer_data": null,
  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string, value is "payment_link")
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the payment link’s `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.

- [`after_completion`](https://docs.stripe.com/api/payment-link/object.md?query=after_completion) (object)
  Behavior after the purchase is complete.

- `allow_promotion_codes` (boolean)
  Whether user redeemable promotion codes are enabled.

- `application` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The ID of the Connect application that created the Payment Link.

- `application_fee_amount` (integer, nullable)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account.

- `application_fee_percent` (number, nullable)
  This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account.

- [`automatic_tax`](https://docs.stripe.com/api/payment-link/object.md?query=automatic_tax) (object)
  Configuration details for automatic tax collection.

- `billing_address_collection` (enum)
  Configuration for collecting the customer’s billing address. Defaults to `auto`.
Possible enum values:
  - `auto`
    Checkout will only collect the billing address when necessary. When using [automatic_tax](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-automatic_tax-enabled), Checkout will collect the minimum number of fields required for tax calculation.

  - `required`
    Checkout will always collect the customer’s billing address.

- [`consent_collection`](https://docs.stripe.com/api/payment-link/object.md?query=consent_collection) (object, nullable)
  When set, provides configuration to gather active consent from customers.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).

- [`custom_fields`](https://docs.stripe.com/api/payment-link/object.md?query=custom_fields) (array of objects)
  Collect additional information from your customer using custom fields. Up to 3 fields are supported. You can’t set this parameter if `ui_mode` is `custom`.

- [`custom_text`](https://docs.stripe.com/api/payment-link/object.md?query=custom_text) (object)
  Display additional text for your customers using custom text. You can’t set this parameter if `ui_mode` is `custom`.

- `customer_creation` (enum)
  Configuration for Customer creation during checkout.
Possible enum values:
  - `always`
    The Checkout Session will always create a [Customer](https://docs.stripe.com/api/customers.md) when a Session confirmation is attempted.

  - `if_required`
    The Checkout Session will only create a [Customer](https://docs.stripe.com/api/customers.md) if it is required for Session confirmation. Currently, only `subscription` mode Sessions and `payment` mode Sessions with [post-purchase invoices enabled](https://docs.stripe.com/receipts.md?payment-ui=checkout#paid-invoices) require a Customer.

- `inactive_message` (string, nullable)
  The custom message to be displayed to a customer when a payment link is no longer active.

- [`invoice_creation`](https://docs.stripe.com/api/payment-link/object.md?query=invoice_creation) (object, nullable)
  Configuration for creating invoice for payment mode payment links.

- [`line_items`](https://docs.stripe.com/api/payment-link/object.md?query=line_items) (object, expandable (can be expanded into an object with the `expand` request parameter))
  The line items representing what is being sold.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- [`managed_payments`](https://docs.stripe.com/api/payment-link/object.md?query=managed_payments) (object, nullable)
  Settings for Managed Payments for this Payment Link and resulting [CheckoutSessions](https://docs.stripe.com/api/checkout/sessions/object.md), [PaymentIntents](https://docs.stripe.com/api/payment_intents/object.md), [Invoices](https://docs.stripe.com/api/invoices/object.md), and [Subscriptions](https://docs.stripe.com/api/subscriptions/object.md).

- `metadata` (map)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- [`name_collection`](https://docs.stripe.com/api/payment-link/object.md?query=name_collection) (object, nullable)
  Details on the state of name collection for the payment link.

- `on_behalf_of` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.

- `optional_items` (array of objects, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The optional items presented to the customer at checkout.

- [`payment_intent_data`](https://docs.stripe.com/api/payment-link/object.md?query=payment_intent_data) (object, nullable)
  Indicates the parameters to be passed to PaymentIntent creation during checkout.

- `payment_method_collection` (enum)
  Configuration for collecting a payment method during checkout. Defaults to `always`.
Possible enum values:
  - `always`
    The Checkout Session will always collect a PaymentMethod.

  - `if_required`
    The Checkout Session will only collect a PaymentMethod if there is an amount due.

- [`payment_method_options`](https://docs.stripe.com/api/payment-link/object.md?query=payment_method_options) (object, nullable)
  Payment-method-specific configuration.

- `payment_method_types` (array of enums, nullable)
  The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you’ve enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).

- [`phone_number_collection`](https://docs.stripe.com/api/payment-link/object.md?query=phone_number_collection) (object)
  Controls phone number collection settings during checkout.

- [`restrictions`](https://docs.stripe.com/api/payment-link/object.md?query=restrictions) (object, nullable)
  Settings that restrict the usage of a payment link.

- [`shipping_address_collection`](https://docs.stripe.com/api/payment-link/object.md?query=shipping_address_collection) (object, nullable)
  Configuration for collecting the customer’s shipping address.

- [`shipping_options`](https://docs.stripe.com/api/payment-link/object.md?query=shipping_options) (array of objects)
  The shipping rate options applied to the session.

- `submit_type` (enum)
  Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button.
Possible enum values:
  - `auto`
    Default value. `pay` will used in all scenarios

  - `book`
    Recommended when offering bookings. Submit button includes a ‘Book’ label and URLs use the `book.stripe.com` hostname

  - `donate`
    Recommended when accepting donations. Submit button includes a ‘Donate’ label and URLs use the `donate.stripe.com` hostname

  - `pay`
    Submit button includes a ‘Buy’ label and URLs use the `buy.stripe.com` hostname

  - `subscribe`
    Submit button includes a ‘Subscribe’ label and URLs use the `buy.stripe.com` hostname

- [`subscription_data`](https://docs.stripe.com/api/payment-link/object.md?query=subscription_data) (object, nullable)
  When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.

- [`tax_id_collection`](https://docs.stripe.com/api/payment-link/object.md?query=tax_id_collection) (object)
  Details on the state of tax ID collection for the payment link.

- [`transfer_data`](https://docs.stripe.com/api/payment-link/object.md?query=transfer_data) (object, nullable)
  The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.

- `url` (string)
  The public URL that can be shared with customers.

