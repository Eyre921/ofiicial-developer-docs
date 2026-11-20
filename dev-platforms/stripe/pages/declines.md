---
title: "Declines"
source: https://docs.stripe.com/declines.md
path: declines
---

# Declines

Understand payment declines, find decline codes, and improve payment handling.

Payments can fail because of [issuer declines](https://docs.stripe.com/declines/how-declines-work.md#issuer-declines), [blocked payments](https://docs.stripe.com/declines/how-declines-work.md#blocked-payments), or [invalid API calls](https://docs.stripe.com/declines/how-declines-work.md#invalid-api-calls). Use these guides to understand the cause of a failed payment and decide what to do next.

## Understand declines

Each type of payment failure requires a different response. Learn how to distinguish issuer declines, blocked payments, and invalid API calls.

[How declines work](https://docs.stripe.com/declines/how-declines-work.md): Understand the different types of payment failures and how to review them in the Dashboard or API.

[Card declines](https://docs.stripe.com/declines/card.md): Learn why card issuers decline payments and how to reduce card declines.

## Look up a code

Choose a reference based on the type of code you received. For network codes, use the payment method or card network to interpret the code in context.

[Stripe decline codes](https://docs.stripe.com/declines/codes.md): Look up a Stripe decline code to understand why a payment was declined and what to do next.

[Network decline codes](https://docs.stripe.com/declines/network-codes.md): Find a network decline code for the payment method or card network that returned it.

[API error codes](https://docs.stripe.com/error-codes.md): Look up Stripe API error codes to understand what they mean and what to do next.

## Improve payment handling

Use error handling guidance and test payments to check how your integration handles failures. Analyze payment acceptance data to identify recurring issues and decide what to investigate.

[Handle errors](https://docs.stripe.com/error-handling.md): Detect and handle errors in your integration.

[Test declined payments](https://docs.stripe.com/testing.md#declined-payments): Simulate declined payments to test how your integration responds.

[Analyze payment acceptance](https://docs.stripe.com/payments/analytics/acceptance.md): Understand your payment acceptance rates and identify why payments fail.

