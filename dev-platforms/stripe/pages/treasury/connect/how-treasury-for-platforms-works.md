---
title: "How Treasury for platforms works"
source: https://docs.stripe.com/treasury/connect/how-treasury-for-platforms-works.md
path: treasury/connect/how-treasury-for-platforms-works
---

# How Treasury for platforms works

Learn about connected accounts, financial accounts, and moving money.

[Stripe Treasury for platforms](https://stripe.com/treasury) is a suite of APIs for Stripe *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) platforms that allows you to embed financial services in your product.

Stripe provides the infrastructure in partnership with trusted banks. You can use Treasury for platforms to enable your connected accounts to hold funds, pay bills, and manage their cash flow.

## Use cases

The following are examples of some common Treasury for platforms use cases:

| **Use case** | **Description** |
| --- | --- |
| **Spend management** | Build a spend management product for your customers to store funds on your platform and manage spending. |
| **Store and spend account** | Allow businesses to store funds, add recipients, and pay contractors and vendors. The accounts allow storage of money into multiple financial accounts and transfers of funds to yourself or third party recipients. |
| **Programmatic money movement** | Facilitate money movement between your platform’s connected accounts and from connected accounts to third-party accounts. |

## Connected accounts

To use Treasury for platforms, you must have a Stripe [Connect](https://docs.stripe.com/connect.md) integration where your platform account provides Stripe functionality to its connected accounts. Each connected account exists as an [Account](https://docs.stripe.com/api/v2/core/accounts.md) object in the Accounts v2 API and its access to Stripe functionality is defined by its configuration capabilities, such as `merchant`, `customer`, `recipient`, or `money_manager`.

- The [merchant](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-merchant) configuration allows the connected account to accept payments from its own customers.
- The [customer](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-customer) configuration allows the connected account to pay your platform or one of your merchant-configured connected accounts.
- The [recipient](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-recipient) configuration allows the connected account to receive payouts from you or one of your merchant-configured connected accounts.
- The [money_manager](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-money_manager) configuration allows the connected account to use financial accounts to manage their Stripe balance.
- The `card_creator` configuration allows the connected account to create and issue cards to users.

As the platform, you can provision any combination of configuration capabilities to your connected accounts. Different capabilities have different onboarding requirements. Whether you create or update connected accounts to request the capabilities needed for Treasury for platforms, you must collect required information from the connected account before they can use the corresponding functionality.

To enable Treasury for platforms for an existing v1 Account, you can [specify the v1 Account ID in a v2 endpoint](https://docs.stripe.com/connect/accounts-v2/migrate-integration.md#use-v2-endpoints-for-all-your-accounts).

## Financial accounts

When you enable Treasury for platforms, we automatically provision your platform with a financial account.

- Your *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) financial account lets you set up and test your integration without affecting your live account’s platform financial account.
- Your live financial account is where you store your own funds as working capital for your Treasury for platforms program.

The financial accounts for your platform support most of the same types of money movement as the financial accounts attached to your platform’s connected accounts.

- Your platform’s live and sandbox financial accounts behave the same as the live and sandbox financial accounts of your connected accounts.
- You use the same API requests regardless of which financial account is involved, but you don’t include a [Stripe-Context header](https://docs.stripe.com/context.md) when making API calls for your platform financial account.
- You must create an [Account with the recipient configuration](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-recipient) to make a payout to a third-party.

When you onboard your platform to Treasury for platforms, Stripe automatically creates and assigns a [FinancialAccount](https://docs.stripe.com/api/v2/money-management/financial-accounts/object.md?api-version=preview) object to your platform account, where you can manage your Stripe balance. You can create additional financial accounts for your platform to categorize different balances according to your business needs.

You can also create financial accounts for your connected accounts after their relevant capabilities become active.

> You can associate a maximum of 10 financial accounts to a single account. The same limit applies to the number of financial accounts attached to the platform account. If you need a higher financial account threshold, contact [Treasury support](mailto:treasury-support@stripe.com).

## Account balances

Every Stripe account that accepts payments has an [account balance](https://docs.stripe.com/connect/account-balances.md) that tracks the flow of funds into and out of that account. You can transfer funds between your account balance and any financial accounts you might also have with Treasury for platforms, with the respective balances always remaining separate. You can:

- Transfer funds from your platform’s financial accounts to the financial accounts attached to your connected accounts.
- Use [Payouts](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#payments-balance) to send funds from your payment balance to your financial accounts.
- Use [OutboundPayments](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md) to move funds between two financial accounts owned by two different Stripe users.
- Use [OutboundTransfers](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-transfers.md) to move funds between your own financial accounts or payments balance.

## Make API requests on behalf of other accounts

By default, API requests execute on the Stripe account associated with the API key making the call. However, you can use the [Stripe-Context header](https://docs.stripe.com/context.md) to perform an API request on behalf of another account.

If you’re the platform owner making a request on behalf of your connected account, use the `Stripe-Context` header in your API call with your connected account’s ID as the value.

## See also

- [Connected accounts](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md)
- [Financial accounts](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md)

