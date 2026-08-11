---
title: "Sources API"
source: https://docs.stripe.com/api/sources/object.md
path: api/sources/object
---

# The Source object

### The Source object

```json
{
  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_eb829353ed79",
    "bank_name": "TEST BANK",
    "fingerprint": "kBQsBk9KtfCgjEYK",
    "refund_account_holder_name": null,
    "refund_account_holder_type": null,
    "refund_routing_number": null,
    "routing_number": "110000000",
    "swift_code": "TSTEZ122"
  },
  "amount": null,
  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",
  "created": 1683144457,
  "currency": "usd",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "110000000-test_eb829353ed79",
    "amount_charged": 0,
    "amount_received": 0,
    "amount_returned": 0,
    "refund_attributes_method": "email",
    "refund_attributes_status": "missing"
  },
  "statement_descriptor": null,
  "status": "pending",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `allow_redisplay` (enum, nullable)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
Possible enum values:
  - `always`
    Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  - `limited`
    Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  - `unspecified`
    This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `amount` (integer, nullable)
  A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources.

- `client_secret` (string)
  The client secret of the source. Used for client-side retrieval using a publishable key.

- [`code_verification`](https://docs.stripe.com/api/sources/object.md?query=code_verification) (object, nullable)
  Information related to the code verification flow. Present if the source is authenticated by a verification code (`flow` is `code_verification`).

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum, nullable)
  Three-letter [ISO code for the currency](https://docs.stripe.com/currencies.md) associated with the source. This is the currency for which the source will be chargeable once ready. Required for `single_use` sources.

- `customer` (string, nullable)
  The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.

- `flow` (string)
  The authentication `flow` of the source. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (map, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- [`owner`](https://docs.stripe.com/api/sources/object.md?query=owner) (object, nullable)
  Information about the owner of the payment instrument that may be used or required by particular source types.

- [`receiver`](https://docs.stripe.com/api/sources/object.md?query=receiver) (object, nullable)
  Information related to the receiver flow. Present if the source is a receiver (`flow` is `receiver`).

- [`redirect`](https://docs.stripe.com/api/sources/object.md?query=redirect) (object, nullable)
  Information related to the redirect flow. Present if the source is authenticated by a redirect (`flow` is `redirect`).

- [`source_order`](https://docs.stripe.com/api/sources/object.md?query=source_order) (object, nullable)
  Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.

- `statement_descriptor` (string, nullable)
  Extra information about a source. This will appear on your customer’s statement every time you charge the source.

- `status` (string)
  The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`, or `pending`. Only `chargeable` sources can be used to create a charge.

- `type` (enum)
  The `type` of the source. The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`, `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`, `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or `wechat`. An additional hash is included on the source with a name matching this value. It contains additional information specific to the [payment method](https://docs.stripe.com/docs/sources.md) used.
Possible enum values:
  - `ach_credit_transfer`
  - `ach_debit`
  - `alipay`
  - `bancontact`
  - `card`
  - `card_present`
  - `eps`
  - `giropay`
  - `ideal`
  - `klarna`
  - `multibanco`
  - `p24`
  - `sepa_debit`
  - `sofort`
  - `three_d_secure`
  - `wechat`

- `usage` (string, nullable)
  Either `reusable` or `single_use`. Whether this source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. If an incompatible value is passed, an error will be returned.

