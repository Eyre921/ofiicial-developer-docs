---
title: "Create a subscription"
source: https://docs.stripe.com/api/subscriptions/create.md
path: api/subscriptions/create
---

# Create a subscription

Creates a new subscription on an existing customer. Each customer can have up to 500 active or scheduled subscriptions.

When you create a subscription with `collection_method=charge_automatically`, the first invoice is finalized as part of the request. The `payment_behavior` parameter determines the exact behavior of the initial payment.

To start subscriptions where the first invoice always begins in a `draft` status, use [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md#managing) instead. Schedules provide the flexibility to model more complex billing configurations that change over time.

## Prerequisites

Before you can run the following code snippet, you need to call these APIs with the provided parameters to set up the prerequisite API object(s).

1. Create a payment method
POST /v1/payment_methods {"type":"card","card":{"token":"tok_visa"}}
2. Create a customer and attach the payment method
POST /v1/customers {"name":"Jenny Rosen","email":"jennyrosen@example.com","payment_method":"${node.prerequisites.createPaymentMethod.createPaymentMethod:id}","invoice_settings":{"default_payment_method":"${node.prerequisites.createPaymentMethod.createPaymentMethod:id}"}}
3. Create a product
POST /v1/products {"name":"Gold Plan"}
4. Create a price
POST /v1/prices {"product":"${node.prerequisites.createProduct.createProduct:id}","unit_amount":2000,"currency":"usd","recurring":{"interval":"month"}}

## Request

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]={{PRICE_ID}}"
```

### Response

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

## Returns

The newly created `Subscription` object, if the call succeeded. If the attempted charge fails, the subscription is created in an `incomplete` status.

## Parameters

- [`add_invoice_items`](https://docs.stripe.com/api/subscriptions/create.md?query=add_invoice_items) (array of objects, optional)
  A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.

- `application_fee_percent` (number, optional)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://docs.stripe.com/connect/subscriptions.md#collecting-fees-on-subscriptions).

- [`automatic_tax`](https://docs.stripe.com/api/subscriptions/create.md?query=automatic_tax) (object, optional)
  Automatic tax settings for this subscription.

- `backdate_start_date` (timestamp, optional)
  A past timestamp to backdate the subscription’s start date to. If set, the first invoice will contain line items for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.

- `billing_cycle_anchor` (timestamp, optional)
  A future timestamp in UTC format to anchor the subscription’s [billing cycle](https://docs.stripe.com/subscriptions/billing-cycle.md). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals.

- [`billing_cycle_anchor_config`](https://docs.stripe.com/api/subscriptions/create.md?query=billing_cycle_anchor_config) (object, optional)
  Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurrence of the day_of_month at the hour, minute, and second UTC.

- [`billing_mode`](https://docs.stripe.com/api/subscriptions/create.md?query=billing_mode) (object, optional)
  Controls how prorations and invoices for subscriptions are calculated and orchestrated.

- [`billing_schedules`](https://docs.stripe.com/api/subscriptions/create.md?query=billing_schedules) (array of objects, optional)
  An array of billing schedules, which allow you to bill customers in advance for multiple service periods. Requires flexible billing mode and API version 2026-05-27.dahlia or later. Learn more about [prebilling](https://docs.stripe.com/billing/subscriptions/prebilling.md).

- [`billing_thresholds`](https://docs.stripe.com/api/subscriptions/create.md?query=billing_thresholds) (object, optional)
  Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.

- `cancel_at` (timestamp | enum, optional)
  A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
Possible enum values:
  - `max_billed_until`
    Set subscription to cancel at the latest date that each subscription item is billed until.

  - `max_period_end`
    Set subscription to cancel at the latest end date among all subscription items’ current billing periods.

  - `min_period_end`
    Set subscription to cancel at the earliest end date among all subscription items’ current billing periods.

- `cancel_at_period_end` (boolean, optional)
  Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.

- `collection_method` (enum, optional)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
Possible enum values:
  - `charge_automatically`
  - `send_invoice`

- `currency` (enum, optional)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies.md).

- `customer` (string, optional)
  The identifier of the customer to subscribe.

- `customer_account` (string, optional)
  The identifier of the account representing the customer to subscribe.

- `days_until_due` (integer, optional)
  Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.

- `default_payment_method` (string, optional)
  ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/api/customers/object.md#customer_object-default_source).

- `default_source` (string, optional)
  ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer’s [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) or [default_source](https://docs.stripe.com/api/customers/object.md#customer_object-default_source).

- `default_tax_rates` (array of strings, optional)
  The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.

- `description` (string, optional)
  The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

  The maximum length is 500 characters.

- [`discounts`](https://docs.stripe.com/api/subscriptions/create.md?query=discounts) (array of objects, optional)
  The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription’s customer.

- [`invoice_settings`](https://docs.stripe.com/api/subscriptions/create.md?query=invoice_settings) (object, optional)
  All invoices will be billed using the specified settings.

- [`items`](https://docs.stripe.com/api/subscriptions/create.md?query=items) (array of objects, required)
  A list of up to 20 subscription items, each with an attached price.

- `metadata` (map, optional)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `off_session` (boolean, optional)
  Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).

- `on_behalf_of` (string, optional)
  The account on behalf of which to charge, for each of the subscription’s invoices.

- `payment_behavior` (enum, optional)
  Controls how Stripe handles the first invoice when payment is required and `collection_method=charge_automatically`. Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status.
Possible enum values:
  - `allow_incomplete`
    This is the default behavior since [2019-03-14](changelog/2019-03-14/subscriptions-successfully-created-first-payment-fails). If payment fails, the Subscription is created with `status=incomplete`, otherwise `status=active`. This behavior allows you to manage scenarios where additional customer actions are needed to pay the Invoice. For example, SCA regulations might require 3DS authentication to complete payment. See the [SCA Migration Guide](https://docs.stripe.com/billing/migration/strong-customer-authentication.md) for Billing to learn more.

  - `default_incomplete`
    When the first invoice requires payment, creates a Subscription with `status=incomplete` without attempting payment, otherwise `status=active`. You must request explicit confirmation of the Invoice’s PaymentIntent to activate the subscription. The resulting Invoice has [auto_advance=false](https://docs.stripe.com/api/invoices/object.md#invoice_object-auto_advance), so Stripe doesn’t automatically attempt payment, retry payment, or finalize the subscription.

  - `error_if_incomplete`
    If payment fails, return an HTTP `402` status code and don’t create the subscription. This behavior doesn’t support payments that require user action, such as 3DS authentication, because it returns an error instead of creating a PaymentIntent with `status=requires_action`. To handle payments that require action, use `allow_incomplete` or `default_incomplete` instead. This behavior was the default for API versions before [2019-03-14](changelog/2019-03-14/subscriptions-successfully-created-first-payment-fails).

  - `pending_if_incomplete`
    This behavior is exclusive to Subscription updates and cannot be used for creation.

- [`payment_settings`](https://docs.stripe.com/api/subscriptions/create.md?query=payment_settings) (object, optional)
  Payment settings to pass to invoices created by the subscription.

- [`pending_invoice_item_interval`](https://docs.stripe.com/api/subscriptions/create.md?query=pending_invoice_item_interval) (object, optional)
  Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://docs.stripe.com/api/invoices/create.md) for the given subscription at the specified interval.

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/billing/subscriptions/prorations.md) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
Possible enum values:
  - `always_invoice`
    **Unsupported** for subscription creation.

  - `create_prorations`
    Will cause proration invoice items to be created when applicable.

  - `none`
    Disable creating prorations in this request.

- [`transfer_data`](https://docs.stripe.com/api/subscriptions/create.md?query=transfer_data) (object, optional)
  If specified, the funds from the subscription’s invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.

- `trial_end` (string, value is "now" | timestamp, optional)
  Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer’s trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials.md) to learn more.

- `trial_from_plan` (boolean, optional)
  Indicates if a plan’s `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials.md) to learn more.

- `trial_period_days` (integer, optional)
  Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials.md) to learn more.

- [`trial_settings`](https://docs.stripe.com/api/subscriptions/create.md?query=trial_settings) (object, optional)
  Settings related to subscription trials.

