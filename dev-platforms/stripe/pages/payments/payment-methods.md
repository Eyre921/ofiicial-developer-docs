---
title: "Payment Methods API"
source: https://docs.stripe.com/payments/payment-methods.md
path: payments/payment-methods
---

# Payment Methods API

Learn about the API that allows you to accept a range of global payment methods.

The Payment Methods API allows you to accept a variety of payment methods through a single API. A [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) object contains the payment method details to create payments. With the Payment Methods API, you can combine a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs):

- With a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) to accept a payment
- With a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) and a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) to save payment details for later

## Supported payment methods

To determine which payment methods to use for specific locales, see the [guide to payment methods](https://stripe.com/payments/payment-methods-guide).

The guide includes available payment methods for different regions, a detailed description of each payment method’s characteristics, and the geographic regions where they’re most relevant. You can enable any payment methods available to you in the [Dashboard](https://dashboard.stripe.com). Activation is generally instantaneous and doesn’t require additional contracts.

## Customer actions 

Some payment methods require your customer to take additional steps to complete the payment. The `PaymentIntent` object’s `next_action` property specifies the customer action.

Some common actions that customers need to perform are:

- Redirect to their bank’s online service to authenticate and approve the payment.
- Verify ownership of their account by providing a one-time code that you post to the Stripe API (for example, microdeposits).
- Push funds (for example, in the case for bank transfers) through their bank’s online service.

Not all payment methods require additional customer actions. For example, card payments (excluding 3D Secure) require no additional authentication beyond collecting card details.

> For payment methods that require customer action, configure [webhook endpoints](https://docs.stripe.com/payments/payment-methods.md#webhooks) for notifications on whether a payment has succeeded or not.

## Immediate or delayed notification of payment success 

Some payment methods, such as cards, immediately report whether a payment succeeded or failed. Others, such as ACH debits, report the result after a delay. For payment methods with immediate notification, the `PaymentIntent` status changes to `succeeded` or `requires_payment_method`. A `succeeded` status indicates that the payment completed successfully according to the payment method’s processing flow, but funds can still be refunded, disputed, returned, or reversed.

Payment methods with delayed notification can’t guarantee the outcome while the payment is processing. The `PaymentIntent` remains in the `processing` status until the payment succeeds or fails. During this time, we recommend keeping the order pending and not fulfilling it until the payment succeeds.

> For payment methods with delayed notification, configure [webhook endpoints](https://docs.stripe.com/payments/payment-methods.md#webhooks) for notifications on whether a payment has succeeded or not.

## Single-use or reusable 

You can reuse certain payment methods (for example, cards or bank debits) for additional payments without authorizing and collecting payment details again.

You should always set up reusable payment methods for future use to reduce the chance of future declines and payment friction (such as [authentication being required](https://docs.stripe.com/strong-customer-authentication.md)). Reusable payment methods can be [set up for future use when accepting a payment](https://docs.stripe.com/payments/save-during-payment.md) or [set up for future use without taking a payment](https://docs.stripe.com/payments/save-and-reuse.md).

Single-use payment methods (for example, some kinds of bank transfers) can’t be attached to customers because they’re consumed after a payment attempt.

## Use webhooks to track payment status 

Configure webhooks by creating an [event destination](https://docs.stripe.com/events/set-up-events.md) for payment methods that require customer action or have delayed payment notification. Verify [webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe.

Stripe sends the following events when the `PaymentIntent` status is updated:

| Event | Description | Next steps |
| --- | --- | --- |
| `payment_intent.processing` | The customer’s payment was submitted to Stripe successfully. Only applicable to payment methods with [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification). | Wait for the initiated payment to succeed or fail. |
| `payment_intent.succeeded` | The payment succeeded. | Fulfill the purchased goods or services. |
| `payment_intent.payment_failed` | The payment failed. | Send an email or push notification to request another payment method. |

### Other tracking options

You can also use one of the following options to track payment status:

- Manually track payment status in the Stripe Dashboard if you accept a low volume of orders using payment methods with delayed notification. In the Dashboard, you can [view all payments](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, and retry failed payments.
- Poll the API by repeatedly retrieving a `PaymentIntent` and checking its status. Polling is less reliable than webhooks and might not work at high volumes. Stripe also rate-limits API requests, so use polling with caution.
- Integrate a partner application to handle common business workflows, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales).

## The PaymentMethod object 

A `PaymentMethod` contains reusable payment details, such as a card’s expiration date or a billing address. It doesn’t include transaction-specific information, such as the amount or currency. Attach a `PaymentMethod` to a `PaymentIntent` to use it throughout the [payment lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle.md).

Each `PaymentMethod` has a [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type) attribute, such as `"type": "sepa_debit"`, and a corresponding hash that contains information specific to the payment method.

The following example shows a `sepa_debit` `PaymentMethod` object:

```json
{
  "id": "pm_123456789",
  "object": "payment_method",
  "billing_details": {
    "address": {...},
    "email": "jenny@example.com",
    "name": "Jenny Rosen",
    "phone": "+335555555555"
  },
  "sepa_debit": {
    "bank_code": "37040044",
    "branch_code": "94832",
    "country": "FR",
    "fingerprint": "ygEJfUjzWMGyWnZg",
    "last4": "3000"
  },
  "type": "sepa_debit",
  (...)
}
```

> To safely handle sensitive payment information and automatically handle customer actions, Stripe recommends that you create payment methods using [Stripe.js](https://docs.stripe.com/js.md#stripe-create-payment-method).

## See also

- [Guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [Payment Methods API reference](https://docs.stripe.com/api/payment_methods.md)

