---
title: "The Subscription object"
source: https://docs.stripe.com/api/subscriptions/object.md
path: api/subscriptions/object
---

# The Subscription object

### The Subscription object

```json
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_Na6dzxczY5fwHx",
        "object": "subscription_item",
        "created": 1679609768,
        "current_period_end": 1682288167,
        "current_period_start": 1679609767,
        "metadata": {},
        "plan": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "plan",
          "active": true,
          "amount": 1000,
          "amount_decimal": "1000",
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "discounts": null,
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "quantity": 1,
        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"
  },
  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",
  "livemode": false,
  "metadata": {},
  "next_pending_invoice_item_invoice": null,
  "on_behalf_of": null,
  "pause_collection": null,
  "payment_settings": {
    "payment_method_options": null,
    "payment_method_types": null,
    "save_default_payment_method": "off"
  },
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "pending_update": null,
  "schedule": null,
  "start_date": 1679609767,
  "status": "active",
  "test_clock": null,
  "transfer_data": null,
  "trial_end": null,
  "trial_settings": {
    "end_behavior": {
      "missing_payment_method": "create_invoice"
    }
  },
  "trial_start": null
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `application` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the Connect Application that created the subscription.

- `application_fee_percent` (number, nullable)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account.

- [`automatic_tax`](https://docs.stripe.com/api/subscriptions/object.md?query=automatic_tax) (object)
  Automatic tax settings for this subscription.

- `billing_cycle_anchor` (timestamp)
  The reference point that aligns future [billing cycle](https://docs.stripe.com/subscriptions/billing-cycle.md) dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The timestamp is in UTC format.

- [`billing_cycle_anchor_config`](https://docs.stripe.com/api/subscriptions/object.md?query=billing_cycle_anchor_config) (object, nullable)
  The fixed values used to calculate the `billing_cycle_anchor`.

- [`billing_mode`](https://docs.stripe.com/api/subscriptions/object.md?query=billing_mode) (object)
  Controls how prorations and invoices for subscriptions are calculated and orchestrated.

- [`billing_schedules`](https://docs.stripe.com/api/subscriptions/object.md?query=billing_schedules) (array of objects)
  Billing schedules for this subscription.

- [`billing_thresholds`](https://docs.stripe.com/api/subscriptions/object.md?query=billing_thresholds) (object, nullable)
  Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period

- `cancel_at` (timestamp, nullable)
  A date in the future at which the subscription will automatically get canceled

- `cancel_at_period_end` (boolean)
  Whether this subscription will (if `status=active`) or did (if `status=canceled`) cancel at the end of the current billing period.

- `canceled_at` (timestamp, nullable)
  If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state.

- [`cancellation_details`](https://docs.stripe.com/api/subscriptions/object.md?query=cancellation_details) (object, nullable)
  Details about why this subscription was cancelled

- `collection_method` (enum)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
Possible enum values:
  - `charge_automatically`
  - `send_invoice`

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).

- `customer` (string, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the customer who owns the subscription.

- `customer_account` (string, nullable)
  ID of the account representing the customer who owns the subscription.

- `days_until_due` (integer, nullable)
  Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `collection_method=charge_automatically`.

- `default_payment_method` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/api/customers/object.md#customer_object-default_source).

- `default_source` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/api/customers/object.md#customer_object-default_source).

- [`default_tax_rates`](https://docs.stripe.com/api/subscriptions/object.md?query=default_tax_rates) (array of objects, nullable)
  The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.

- `description` (string, nullable)
  The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  The maximum length is 500 characters.

- `discounts` (array of strings, expandable (can be expanded into an object with the `expand` request parameter))
  The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.

- `ended_at` (timestamp, nullable)
  If the subscription has ended, the date the subscription ended.

- [`invoice_settings`](https://docs.stripe.com/api/subscriptions/object.md?query=invoice_settings) (object)
  All invoices will be billed using the specified settings.

- [`items`](https://docs.stripe.com/api/subscriptions/object.md?query=items) (object)
  List of subscription items, each with an attached price.

- `latest_invoice` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The most recent invoice this subscription has generated over its lifecycle (for example, when it cycles or is updated).

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- [`managed_payments`](https://docs.stripe.com/api/subscriptions/object.md?query=managed_payments) (object, nullable)
  Settings for Managed Payments for this Subscription and resulting [Invoices](https://docs.stripe.com/api/invoices/object.md) and [PaymentIntents](https://docs.stripe.com/api/payment_intents/object.md).

- `metadata` (map)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `next_pending_invoice_item_invoice` (timestamp, nullable)
  Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`.

- `on_behalf_of` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The account (if any) the charge was made on behalf of for charges associated with this subscription. See the [Connect documentation](https://docs.stripe.com/connect/subscriptions.md#on-behalf-of) for details.

- [`pause_collection`](https://docs.stripe.com/api/subscriptions/object.md?query=pause_collection) (object, nullable)
  If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md).

- [`payment_settings`](https://docs.stripe.com/api/subscriptions/object.md?query=payment_settings) (object, nullable)
  Payment settings passed on to invoices created by the subscription.

- [`pending_invoice_item_interval`](https://docs.stripe.com/api/subscriptions/object.md?query=pending_invoice_item_interval) (object, nullable)
  Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://docs.stripe.com/api/invoices/create.md) for the given subscription at the specified interval.

- `pending_setup_intent` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  You can use this [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to collect user authentication when creating a subscription without immediate payment or updating a subscription’s payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://docs.stripe.com/billing/migration/strong-customer-authentication.md#scenario-2).

- [`pending_update`](https://docs.stripe.com/api/subscriptions/object.md?query=pending_update) (object, nullable)
  If specified, [pending updates](https://docs.stripe.com/billing/subscriptions/pending-updates.md) that will be applied to the subscription once the `latest_invoice` has been paid.

- [`presentment_details`](https://docs.stripe.com/api/subscriptions/object.md?query=presentment_details) (object, nullable)
  A hash containing information about the currency presented to the customer.

- `schedule` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The schedule attached to the subscription

- `start_date` (timestamp)
  Date when the subscription was first created. The date might differ from the `created` date due to backdating.

- `status` (enum)
  Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, or `paused`.

  For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated.

  A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over.

  A subscription can only enter a `paused` status [when a trial ends without a payment method](https://docs.stripe.com/billing/subscriptions/trials.md#create-free-trials-without-payment). A `paused` subscription doesn’t generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md), which still generates invoices and leaves the subscription’s status unchanged.

  If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings).

  If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices.

- `test_clock` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  ID of the test clock this subscription belongs to.

- [`transfer_data`](https://docs.stripe.com/api/subscriptions/object.md?query=transfer_data) (object, nullable)
  The account (if any) the subscription’s payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the subscription’s invoices.

- `trial_end` (timestamp, nullable)
  If the subscription has a trial, the end of that trial.

- [`trial_settings`](https://docs.stripe.com/api/subscriptions/object.md?query=trial_settings) (object, nullable)
  Settings related to subscription trials.

- `trial_start` (timestamp, nullable)
  If the subscription has a trial, the beginning of that trial.

