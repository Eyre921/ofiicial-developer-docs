---
title: "Disputes on Connect platforms"
source: https://docs.stripe.com/connect/disputes.md
path: connect/disputes
---

# Disputes on Connect platforms

Learn about the dispute responsibilities on Connect platforms.

You can view all disputes filed against your platform and connected accounts in your Dashboard. When one of your connected accounts receives a dispute against a payment, the [charge type](https://docs.stripe.com/connect/charges.md#types) and negative balance responsibility determine:

- Whether you or your connected account responds to that dispute to accept or challenge it.
- Which account Stripe debits for the chargeback and fees.

This guide describes how Stripe processes disputes for each charge type and how you can handle them.

| Behavior | Direct charges | Indirect charges |
| --- | --- | --- |
| Account to use when responding through the API | Connected account. Use its ID in the [`Stripe-Account` header](https://docs.stripe.com/connect/authentication.md#stripe-account-header). | Platform account. |
| Balance debited for the disputed amount | Connected account’s balance. | Platform’s balance, with or without `on_behalf_of`. |
| Account debited for dispute-related fees | Depends on the connected account’s [fee configuration](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md). | Platform account. |

## Direct charges

For connected accounts that use [direct charges](https://docs.stripe.com/connect/direct-charges.md), Stripe always attempts to debit disputed amounts from the connected account’s balance. However, if Stripe can’t debit the amount, ultimate responsibility depends on whether Stripe or the platform is [responsible for negative balances](https://docs.stripe.com/connect/risk-management.md#identify-negative-balance-responsibility).

For dispute-related fees, responsibility depends on your connected account options. The following table shows whether Stripe debits dispute-related fees from the platform or the connected account:

| Account option | Dispute fee payer |
| --- | --- |
| v2 `Account` with [defaults.responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-defaults-responsibilities-fees_collector) = `application` | Platform |
| v2 `Account` with [defaults.responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-defaults-responsibilities-fees_collector) = any of the following values, including legacy Standard, Express, and Custom accounts:
- `stripe`
- `application_custom`
- `application_express` | Connected account |
| v2 `Account` with [defaults.responsibilities.fees_collector](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-defaults-responsibilities-fees_collector) = `application_unified_accounts_beta` | Connected account (for information about changing the payer to your platform, [contact Stripe Support](https://support.stripe.com/)) |
| v1 `Account` with [controller.fees.payer](https://docs.stripe.com/api/accounts/create.md#create_account-controller-fees-payer) = `application` | Platform |
| v1 `Account` with [controller.fees.payer](https://docs.stripe.com/api/accounts/create.md#create_account-controller-fees-payer) = any of the following values, including legacy Standard, Express, and Custom accounts:
- `account`
- `application_custom`
- `application_express` | Connected account |
| v1 `Account` with [controller.fees.payer](https://docs.stripe.com/api/accounts/create.md#create_account-controller-fees-payer) = `application_unified_accounts_beta` | Connected account (for information about changing the payer to your platform, [contact Stripe Support](https://support.stripe.com/)) |

## Destination and separate charges and transfers

For [destination charges](https://docs.stripe.com/connect/destination-charges.md) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md), with or without `on_behalf_of`, Stripe debits dispute amounts and fees from your platform account.

Set up [a webhook](https://docs.stripe.com/webhooks.md) to listen for [dispute created events](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created).

You can reverse the transfer to your connected account through the [Dashboard](https://dashboard.stripe.com/test/transfers) or by [creating a transfer reversal](https://docs.stripe.com/api/transfer_reversals/create.md) to recover the dispute chargeback funds. If the connected account has a negative balance, Stripe attempts to debit its external account if [debit_negative_balances](https://docs.stripe.com/connect/account-balances.md#automatically-debit-connected-accounts) is set to `true`.

Time your reversal according to how you choose to handle the dispute:

- If you accept the dispute, you can reverse the transfer immediately.
- If you challenge the dispute, wait for the dispute outcome before reversing the transfer.
  - If you win, don’t reverse the transfer.
  - If you lose, reverse the transfer.

If you reverse the transfer for a disputed payment that you challenge and win, transfering those funds back to a connected account can have unexpected results:

- If your platform has an insufficient balance, the transfer fails. Prevent insufficient balance errors by [adding funds to your Stripe balance](https://docs.stripe.com/get-started/account/add-funds.md).
- [Cross-border transfer restrictions](https://docs.stripe.com/connect/account-capabilities.md#transfers-cross-border) might prevent you from repaying your connected account.

If Stripe is responsible for the connected account’s negative balances, a transfer reversal can fail when the account has insufficient available funds. Handle reversal failures by retrying when sufficient funds become available.

To automate transfer reversals without writing code, use [Workflows](https://docs.stripe.com/workflows.md). For destination charges, use the [Recover lost dispute funds from connected accounts](https://dashboard.stripe.com/workflows/create?workflow=eyJkZWVwX2xpbmtfdmVyc2lvbiI6MSwibmFtZSI6IlJlY292ZXIgbG9zdCBkaXNwdXRlIGZ1bmRzIGZyb20gY29ubmVjdGVkIGFjY291bnRzIiwiZGVmaW5pdGlvbiI6IkN1UUNFbHNLRVhKbGRISnBaWFpsWDJGZlkyaGhjbWRsRUFFYVJBb2hjM1J5YVhCbExtRndhVjlqWVd4c1gyZGxkRjkyTVY5amFHRnlaMlZ6WDJsa0VoOEtIUW9DYVdRU0Z4b1ZKSHQ3SUhSeWFXZG5aWEl1WTJoaGNtZGxJSDE5RXVRQkNnWmljbUZ1WTJnUUF5clhBUXJVQVFwTWRISnBaMmRsY2k1emRHRjBkWE1nUFQwOUlDSnNiM04wSWlBbUppQW9jM1JsY0hNdWNtVjBjbWxsZG1WZllWOWphR0Z5WjJVdWRISmhibk5tWlhJcExtbHpUbTkwUlcxd2RIa29LUktEQVFvYVkzSmxZWFJsWDJGZmRISmhibk5tWlhKZmNtVjJaWEp6WVd3UUFScGpDaTV6ZEhKcGNHVXVZWEJwWDJOaGJHeGZjRzl6ZEY5Mk1WOTBjbUZ1YzJabGNuTmZhV1JmY21WMlpYSnpZV3h6RWpFS0x3b0NhV1FTS1JvbkpIdDdJSE4wWlhCekxuSmxkSEpwWlhabFgyRmZZMmhoY21kbExuUnlZVzV6Wm1WeUlIMTlHaDRJQWhJYUNoVmphR0Z5WjJVdVpHbHpjSFYwWlM1amJHOXpaV1FhQVFFU0VUSXdNall0TURrdE16QXVaVzVrYVhabCIsInN0cmlwZV9hcGlfdmVyc2lvbiI6IjIwMjYtMDktMzAuZW5kaXZlIn0) template. It triggers when a dispute closes, checks that the dispute is lost and the charge has a transfer, and then reverses the transfer.

To recover funds as soon as Stripe withdraws them from your balance instead, use the following two templates. Use either this approach or the lost dispute template, not both, to avoid reversing the same transfer twice.

- [Recover dispute funds from connected accounts when withdrawn](https://dashboard.stripe.com/workflows/create?workflow=eyJkZWVwX2xpbmtfdmVyc2lvbiI6MSwibmFtZSI6IlJlY292ZXIgZGlzcHV0ZSBmdW5kcyBmcm9tIGNvbm5lY3RlZCBhY2NvdW50cyB3aGVuIHdpdGhkcmF3biIsImRlZmluaXRpb24iOiJDdEFDRWxzS0VYSmxkSEpwWlhabFgyRmZZMmhoY21kbEVBRWFSQW9oYzNSeWFYQmxMbUZ3YVY5allXeHNYMmRsZEY5Mk1WOWphR0Z5WjJWelgybGtFaDhLSFFvQ2FXUVNGeG9WSkh0N0lIUnlhV2RuWlhJdVkyaGhjbWRsSUgxOUVzY0JDZ1ppY21GdVkyZ1FBeXE2QVFxM0FRb3ZLSE4wWlhCekxuSmxkSEpwWlhabFgyRmZZMmhoY21kbExuUnlZVzV6Wm1WeUtTNXBjMDV2ZEVWdGNIUjVLQ2tTZ3dFS0dtTnlaV0YwWlY5aFgzUnlZVzV6Wm1WeVgzSmxkbVZ5YzJGc0VBRWFZd291YzNSeWFYQmxMbUZ3YVY5allXeHNYM0J2YzNSZmRqRmZkSEpoYm5ObVpYSnpYMmxrWDNKbGRtVnljMkZzY3hJeENpOEtBbWxrRWlrYUp5UjdleUJ6ZEdWd2N5NXlaWFJ5YVdWMlpWOWhYMk5vWVhKblpTNTBjbUZ1YzJabGNpQjlmUm9uQ0FJU0l3b2VZMmhoY21kbExtUnBjM0IxZEdVdVpuVnVaSE5mZDJsMGFHUnlZWGR1R2dFQkVoRXlNREkyTFRBNUxUTXdMbVZ1WkdsMlpRIiwic3RyaXBlX2FwaV92ZXJzaW9uIjoiMjAyNi0wOS0zMC5lbmRpdmUifQ): Triggers when Stripe withdraws the disputed amount from your platform balance, then reverses the transfer if the charge has one. Stripe doesn’t withdraw funds for inquiries, so this workflow doesn’t run for them.
- [Return dispute funds to connected accounts when reinstated](https://dashboard.stripe.com/workflows/create?workflow=eyJkZWVwX2xpbmtfdmVyc2lvbiI6MSwibmFtZSI6IlJldHVybiBkaXNwdXRlIGZ1bmRzIHRvIGNvbm5lY3RlZCBhY2NvdW50cyB3aGVuIHJlaW5zdGF0ZWQiLCJkZWZpbml0aW9uIjoiQ3I4RUVsc0tFWEpsZEhKcFpYWmxYMkZmWTJoaGNtZGxFQUVhUkFvaGMzUnlhWEJsTG1Gd2FWOWpZV3hzWDJkbGRGOTJNVjlqYUdGeVoyVnpYMmxrRWg4S0hRb0NhV1FTRnhvVkpIdDdJSFJ5YVdkblpYSXVZMmhoY21kbElIMTlFclVEQ2daaWNtRnVZMmdRQXlxb0F3cWxBd292S0hOMFpYQnpMbkpsZEhKcFpYWmxYMkZmWTJoaGNtZGxMblJ5WVc1elptVnlLUzVwYzA1dmRFVnRjSFI1S0NrU2NRb1RjbVYwY21sbGRtVmZZVjkwY21GdWMyWmxjaEFCR2xnS0kzTjBjbWx3WlM1aGNHbGZZMkZzYkY5blpYUmZkakZmZEhKaGJuTm1aWEp6WDJsa0VqRUtMd29DYVdRU0tSb25KSHQ3SUhOMFpYQnpMbkpsZEhKcFpYWmxYMkZmWTJoaGNtZGxMblJ5WVc1elptVnlJSDE5RXY0QkNoRmpjbVZoZEdWZllWOTBjbUZ1YzJabGNoQUJHdVlCQ2lGemRISnBjR1V1WVhCcFgyTmhiR3hmY0c5emRGOTJNVjkwY21GdWMyWmxjbk1Td0FFS05Rb0lZM1Z5Y21WdVkza1NLUm9uSkh0N0lITjBaWEJ6TG5KbGRISnBaWFpsWDJGZlkyaGhjbWRsTG1OMWNuSmxibU41SUgxOUNra0tDMlJsYzNScGJtRjBhVzl1RWpvYU9DUjdleUJ6ZEdWd2N5NXlaWFJ5YVdWMlpWOWhYMk5vWVhKblpTNTBjbUZ1YzJabGNsOWtZWFJoTG1SbGMzUnBibUYwYVc5dUlIMTlDandLQm1GdGIzVnVkQkl5R2pBa2Uzc2djM1JsY0hNdWNtVjBjbWxsZG1WZllWOTBjbUZ1YzJabGNpNWhiVzkxYm5SZmNtVjJaWEp6WldRZ2ZYMGFLQWdDRWlRS0gyTm9ZWEpuWlM1a2FYTndkWFJsTG1aMWJtUnpYM0psYVc1emRHRjBaV1FhQVFFU0VUSXdNall0TURrdE16QXVaVzVrYVhabCIsInN0cmlwZV9hcGlfdmVyc2lvbiI6IjIwMjYtMDktMzAuZW5kaXZlIn0): Triggers when Stripe returns the disputed amount to your balance after you win, then transfers the reversed amount back to the connected account. This transfer can fail for the reasons listed above.

You can also browse [Fraud Stripe Apps](https://marketplace.stripe.com/categories/fraud) on the App Marketplace to automate dispute management and handle chargebacks.

## Provide Connect embedded components to allow your connected accounts to respond to disputes

Your connected accounts can use [Connect embedded components](https://docs.stripe.com/connect/get-started-connect-embedded-components.md) to manage disputes from within your site.

The following components support dispute management:

- [Payments component](https://docs.stripe.com/connect/supported-embedded-components/payments.md): Displays all of an account’s payments and disputes.
- [Disputes list component](https://docs.stripe.com/connect/supported-embedded-components/disputes-list.md): Displays all of an account’s disputes.
- [Disputes for a payment component](https://docs.stripe.com/connect/supported-embedded-components/disputes-for-a-payment.md): Displays the disputes for a single specified payment. You can use it to include dispute management functionality on a page with your payments UI.

Note: The following is a preview/demo component that behaves differently than live mode usage with real connected accounts. The actual component has more functionality than what might appear in this demo component. For example, for connected accounts without Stripe dashboard access (custom accounts), no user authentication is required in production.

## Smart Disputes

If you use [Smart Disputes](https://docs.stripe.com/disputes/smart-disputes.md), you can [enable Smart Disputes auto-responses for your connected accounts](https://docs.stripe.com/disputes/smart-disputes/auto-respond.md?dashboard-or-api=dashboard#settings-for-connect-platforms).

## See also

- [Dispute categories](https://docs.stripe.com/disputes/categories.md)
- [Use Radar with Connect](https://docs.stripe.com/connect/radar.md)
- [Smart Disputes](https://docs.stripe.com/disputes/smart-disputes.md)
- [Smart Disputes fee passthrough](https://docs.stripe.com/connect/smart-disputes-fee-passthrough.md)

