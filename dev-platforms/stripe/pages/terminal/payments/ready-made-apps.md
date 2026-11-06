---
title: "Accept in-person payments without code"
source: https://docs.stripe.com/terminal/payments/ready-made-apps.md
path: terminal/payments/ready-made-apps
---

# Use Terminal ready-made apps to accept in-person payments

Collect payments in person without writing code.

Terminal ready-made apps let you accept in-person payments without writing code — no custom app, SDK integration, or POS system required. There are two options. Standalone mode is a no-code point-of-sale (POS) application built into supported Stripe Terminal smart readers (Stripe Reader S700/S710 and Verifone V660p), which you enable through a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object. The Stripe Terminal app runs on a supported iPhone or Android device that supports [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md). Both options require an internet connection and don’t support offline payments. Supported features include card payments, additional payment methods (Affirm, WeChat Pay, PayNow), refunds, incremental and extended authorizations, and transaction history. Standalone mode additionally supports on-reader tipping and P2PE encryption.

Stripe offers two ways to accept in-person payments without building your own point-of-sale (POS):

- **Standalone mode** (Public preview): Accept payments on a compatible Stripe Terminal reader.
- **Stripe Terminal app** (Private preview): Accept payments on a supported iPhone or Android device.

Both options require an internet connection and don’t support offline payments.

> Standalone mode and the Stripe Terminal app are only available on the specified readers and devices. All other readers aren’t currently supported by either option and require a custom integration through the [Terminal SDK or Stripe API](https://docs.stripe.com/terminal/payments/setup-integration.md). See [Select a reader](https://docs.stripe.com/terminal/payments/setup-reader.md) for the full list of available readers and how to connect them.

#### Standalone mode

Standalone mode is available for [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) and [Verifone V660p](https://docs.stripe.com/terminal/payments/setup-reader/v660p.md).

1. [Order a reader](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md) compatible with standalone mode.
2. [Register the reader](https://docs.stripe.com/terminal/fleet/register-readers.md) to your Stripe account and assign it to a [Location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md).
3. [Enable standalone mode](https://docs.stripe.com/terminal/payments/ready-made-apps/get-started.md) in the Dashboard.
4. Reboot the reader to enter standalone mode.
5. Enter an amount. You can optionally add a tip.
6. Collect a payment from your customer using a card, digital wallet, or other [supported payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).
7. The payment processes through Stripe, appears in your Dashboard, and is retrievable as a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).
![Standalone mode payment entry screen showing a numeric keypad for entering a payment amount](https://b.stripecdn.com/docs-statics-srv/assets/standalone-mode-payment-entry.7c011d871357502849468fe63af8ce50.png)
![Standalone mode payment collection screen prompting the customer to tap or insert their card](https://b.stripecdn.com/docs-statics-srv/assets/standalone-mode-collect-payment.32ff6916a00e426e3a22c530cd52bb5d.png)
![Standalone mode transaction details screen showing payment status, breakdown, and refund options](https://b.stripecdn.com/docs-statics-srv/assets/standalone-mode-transaction-details.4c79be7b6f48c1acde403faf20fd4fc3.png)

> Standalone mode requires a production reader and doesn’t work on developer kit devices or readers running an [app on device](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md). To test standalone mode, register a supported reader in a sandbox and use a [test card](https://docs.stripe.com/terminal/references/testing.md).

#### Stripe Terminal app

The Stripe Terminal app is available for iOS and Android devices that support [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md).

1. To request access, email [terminal-ready-made-apps@stripe.com](mailto:terminal-ready-made-apps@stripe.com).
2. Open the app and log in with your Stripe account.
3. Select the account and location where you want to accept payments.
4. Enter an amount.
5. Collect a payment from your customer using a card, digital wallet, or other [supported payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).
6. The payment processes through Stripe, appears in your Dashboard, and is retrievable as a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

You can change the selected location at any time to accept payments at a different location. Changing the selected location changes the [reader ID](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-id). Even though you use the same device, it appears as two different readers in the Stripe Dashboard and in reporting.

> Because [Transaction history](https://docs.stripe.com/terminal/payments/ready-made-apps/customization.md#transaction-history) can be scoped to a single location, changing locations might impact which payments the app displays depending on the location’s configuration.

## Feature availability

| Feature | Standalone mode | Stripe Terminal app |
| --- | --- | --- |
| **[Collect card payments](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands.md#payment-method-availability)** [1] | ✓ Supported | ✓ Supported |
| **[Additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md)** | ✓ Supported | ✓ Supported |
| **[P2PE](https://docs.stripe.com/terminal/overview.md#encryption)** | ✓ Supported | Not applicable |
| **[Extended authorizations](https://docs.stripe.com/terminal/features/extended-authorizations.md)** | ✓ Supported | ✓ Supported |
| **[Incremental authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations.md)** | ✓ Supported | ✓ Supported |
| **[Refunds](https://docs.stripe.com/terminal/payments/ready-made-apps.md#refunds)** | ✓ Supported | ✓ Supported |
| [Require passcode for refunds](https://docs.stripe.com/terminal/payments/ready-made-apps/customization.md#refunds) | ✓ Supported | - Unsupported |
| Restrict refunds with the Terminal Operator role | - Unsupported | ✓ Supported |
| [Transaction history](https://docs.stripe.com/terminal/payments/ready-made-apps/customization.md#transaction-history) | ✓ Supported | ✓ Supported |
| **[On-reader tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-reader.md)** | ✓ Supported | - Unsupported |
| **[On-receipt tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md)** | - Unsupported | - Unsupported |
| **[Collect and save payment details for future use](https://docs.stripe.com/terminal/features/saving-payment-details/overview.md)** | - Unsupported | - Unsupported |
| **[Collect NFC data](https://docs.stripe.com/terminal/features/collect-nfc-data.md)** (Private preview) | - Unsupported | - Unsupported |
| **[Collect swiped data](https://docs.stripe.com/terminal/features/collect-data.md)** (Private preview) | - Unsupported | Not applicable |
| **[Collect on-screen inputs](https://docs.stripe.com/terminal/features/collect-inputs.md)** | - Unsupported | - Unsupported |
| **[Mail and telephone order (MOTO) payments](https://docs.stripe.com/terminal/features/mail-telephone-orders/overview.md)** | - Unsupported | - Unsupported |
| **[Offline mode](https://docs.stripe.com/terminal/features/operate-offline/overview.md)** | - Unsupported | - Unsupported |

[1] [Supported card brands vary by reader](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands.md#payment-method-availability).

## Provide customer receipts

You can send [email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) with all supported readers, and print physical receipts with the V660p. On the V660p, the reader prompts customers to select if they want a printed or emailed receipt for successful and failed payments as well as for refunds. For all other supported readers, customers are automatically offered the ability to enter an email address after each successful payment and refund. Email receipts for failed transactions are not supported.

Receipts behave differently while you’re testing. Test payments don’t automatically send receipts unless the associated email belongs to you or to another user with a verified email and access to the [sandbox](https://docs.stripe.com/sandboxes.md). For test payments associated with other email addresses, you can view or manually send a receipt using the [Dashboard](https://dashboard.stripe.com/test/payments).

> Standalone mode and the Stripe Terminal app aren’t a point-of-sale system, cash register, or fiscal system. Any receipts they issue are card-payment confirmations only. They aren’t fiscal receipts, tax invoices, or legally compliant sales documents. Stripe doesn’t accept any responsibility for your compliance with applicable fiscal, tax, or cash register laws in your jurisdiction.

## Refunds

#### Standalone mode

You can initiate [refunds](https://docs.stripe.com/terminal/features/refunds.md?terminal-sdk-platform=server-driven#refunds) directly on the reader in standalone mode, through the Dashboard, or through the [Refunds API](https://docs.stripe.com/api/refunds.md). You can optionally require a passcode to authorize refunds on the reader.

#### Stripe Terminal app

You can initiate [refunds](https://docs.stripe.com/terminal/features/refunds.md?terminal-sdk-platform=server-driven#refunds) directly in the app, through the Dashboard, or through the [Refunds API](https://docs.stripe.com/api/refunds.md). You can optionally add a user with the Terminal Operator role to prevent them from creating refunds in the app or accessing the Stripe Dashboard.

To refund a standalone mode payment using the API, create a [Refund](https://docs.stripe.com/api/refunds/create.md) with the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) ID:

```curl
curl https://api.stripe.com/v1/refunds \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_intent={{PAYMENTINTENT_ID}}"
```

## Next steps

- [Get started](https://docs.stripe.com/terminal/payments/ready-made-apps/get-started.md)
- [Select a reader](https://docs.stripe.com/terminal/payments/setup-reader.md)
- [Customize ready-made apps](https://docs.stripe.com/terminal/payments/ready-made-apps/customization.md)
- [Use standalone mode with Connect](https://docs.stripe.com/terminal/payments/ready-made-apps/connect.md)

