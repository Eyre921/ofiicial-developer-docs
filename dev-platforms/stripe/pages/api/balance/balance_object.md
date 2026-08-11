---
title: "The Balance object"
source: https://docs.stripe.com/api/balance/balance_object.md
path: api/balance/balance_object
---

# The Balance object

### The Balance object

```json
{
  "object": "balance",
  "available": [
    {
      "amount": 666670,
      "currency": "usd",
      "source_types": {
        "card": 666670
      }
    }
  ],
  "connect_reserved": [
    {
      "amount": 0,
      "currency": "usd"
    }
  ],
  "livemode": false,
  "pending": [
    {
      "amount": 61414,
      "currency": "usd",
      "source_types": {
        "card": 61414
      }
    }
  ]
}
```

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- [`available`](https://docs.stripe.com/api/balance/balance_object.md?query=available) (array of objects)
  Available funds that you can transfer or pay out automatically by Stripe or explicitly through the [Transfers API](https://docs.stripe.com/api/balance/balance_object.md#transfers) or [Payouts API](https://docs.stripe.com/api/balance/balance_object.md#payouts). You can find the available balance for each currency and payment type in the `source_types` property.

- [`connect_reserved`](https://docs.stripe.com/api/balance/balance_object.md?query=connect_reserved) (array of objects, nullable)
  Funds held due to negative balances on connected accounts where [account.controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. You can find the connect reserve balance for each currency and payment type in the `source_types` property.

- [`instant_available`](https://docs.stripe.com/api/balance/balance_object.md?query=instant_available) (array of objects, nullable)
  Funds that you can pay out using Instant Payouts.

- [`issuing`](https://docs.stripe.com/api/balance/balance_object.md?query=issuing) (object, nullable)
  Funds that you can spend on your [Issued Cards](https://docs.stripe.com/api/balance/balance_object.md#issuing/cards).

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- [`pending`](https://docs.stripe.com/api/balance/balance_object.md?query=pending) (array of objects)
  Funds that aren’t available in the balance yet. You can find the pending balance for each currency and each payment type in the `source_types` property.

- [`refund_and_dispute_prefunding`](https://docs.stripe.com/api/balance/balance_object.md?query=refund_and_dispute_prefunding) (object, nullable)
  Funds to cover future refunds, disputes, or a negative balance. See the [Add funds to your Stripe balance](https://docs.stripe.com/docs/get-started/account/add-funds.md) guide for more information.

