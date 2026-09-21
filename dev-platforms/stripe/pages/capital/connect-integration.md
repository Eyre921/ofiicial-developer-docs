---
title: "How Capital affects your Connect integration"
source: https://docs.stripe.com/capital/connect-integration.md
path: capital/connect-integration
---

# How Capital affects your Connect integration

Learn how Capital offers, applications, financing payouts, and payments affect connected accounts.

Stripe Capital can introduce offers, application requirements, financing payouts, and payment activity to connected accounts. Stripe manages the financing lifecycle for accounts that use the Stripe Dashboard or Express Dashboard. You usually don’t need to change your Connect integration unless you build custom reporting or accounting, control payout logic, or provide a Capital interface in your platform.

Review the following sections if you:

- Build reports, accounting records, or make business decisions from Balance Transactions or Stripe Data Pipeline data.
- Calculate or trigger payouts outside Stripe’s standard payout flow.
- Use account requirements or capability status in your product or to manually monitor connected accounts.

## Dashboard access to Capital

Access to the Capital flow varies with the connected account’s [Stripe Dashboard access](https://docs.stripe.com/connect/saas/tasks/dashboard.md). Connected accounts with Stripe Dashboard access or Express Dashboard access can access Capital entirely within those Dashboards. Regardless of where connected accounts access Capital, the application and servicing flow is the same.

#### Integration toggle with pref "connect-dashboard-type"

This integration toggle is using global pref "connect-dashboard-type".

There are 3 available values for this integration toggle:
- full
	— label: Stripe Dashboard
	— description: The full Stripe Dashboard
- express
	— label: Express Dashboard
	— description: The Stripe-hosted Express Dashboard
- none
	— label: Custom dashboard
	— description: A dashboard that your platform provides

#### Item 1

The connected account uses the full Stripe Dashboard. Stripe hosts Capital discovery, application, reporting, and servicing.

#### Item 2

The connected account uses the Express Dashboard. Stripe hosts Capital discovery, application, reporting, and servicing.

#### Item 3

The connected account doesn’t use a Stripe-hosted Dashboard for Capital. You have several options for how connected accounts can access Capital, including Stripe-hosted flows and embedded components. Using these options requires you to [set up Capital](https://docs.stripe.com/capital/getting-started.md) first.

## The Capital flow

### Eligible connected accounts receive a Capital offer

Connected accounts are reviewed based on their payment activity, and eligible businesses might receive offers. When Stripe manages offer emails, Stripe sends offers to connected accounts automatically, without your platform needing to take action.

#### Item 1

The offer appears in the Capital section of the Stripe Dashboard. The connected account might also receive emails with details about the offer.

#### Item 2

The offer appears in **Financing** in the Express Dashboard. See the [Express financing demo](https://express.stripe.dev/financing) for an example. The connected account might also receive emails with details about the offer.

#### Item 3

If your platform manages offer emails, it must handle the `capital.financing_offer.created` event, notify the connected account, and [mark the offer as delivered](https://docs.stripe.com/capital/api-integration.md#send-offer-email). This applies to embedded components integrations configured with Custom email management and to custom API integrations. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) before you process events. See [how Capital for platforms works](https://docs.stripe.com/capital/how-capital-for-platforms-works.md). You can show the offer with the [Capital promotion embedded component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion.md) or an [Account Link](https://docs.stripe.com/api/account_links/create.md) with `type` set to `capital_financing_offer`. With a [no-code integration](https://docs.stripe.com/capital/no-code-integration.md), Stripe emails the connected account a Stripe-hosted link to view the offer and begin the application.

### Connected accounts apply for financing

The connected account reviews the offer, confirms its business information, provides any additional required information, and submits the application to Stripe. After submission, Stripe reviews the application. Stripe usually makes a decision soon after submission, but the review can take up to 30 days. In some cases, Stripe emails the connected account to request more information. Connected accounts can take any required actions in the same place they completed their application.

#### Item 1

The connected account applies through Stripe’s hosted Capital flow in the Stripe Dashboard.

#### Item 2

The connected account applies through Stripe’s hosted Capital flow in the Express Dashboard.

#### Item 3

The connected account applies in the [Capital application embedded component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application.md), through an [Account Link](https://docs.stripe.com/api/account_links/create.md) with `type` set to `capital_financing_offer`, or on the Stripe-hosted page opened from a [no-code offer email](https://docs.stripe.com/capital/no-code-integration.md).

#### Requirements and capabilities

Starting or restarting an application requests or resets the relevant Capital [capability](https://docs.stripe.com/api/accounts/object.md?api-version=2026-08-26.preview&rds=1#account_object-capabilities)—`loans` or `cash_advances`, depending on the financing product and jurisdiction. This can add Capital requirements and emit an `account.updated` event.

A Capital-specific requirement can cause the account to appear restricted, but it doesn’t disable payments or payouts. Stripe collects the required information directly from the connected account, so your platform doesn’t need to take action. Use `charges_enabled` and `payouts_enabled` to determine whether the account can accept payments and receive payouts.

During the application, the connected account can also update [`Account`](https://docs.stripe.com/api/accounts/object.md?api-version=2026-08-26.preview&rds=1) and [`Person`](https://docs.stripe.com/api/persons/object.md?api-version=2026-08-26.preview&rds=1) information. If your platform manages this information, monitor `account.updated` and `person.updated`, then reconcile the changes with your system of record. Some changes, such as an update to a connected account’s TIN, can trigger new requirements for other capabilities. Continue handling requirements for payments, payouts, and other capabilities through your existing Connect integration.

### Connected accounts receive the financing funds

After approval, funds are disbursed to the connected account’s bank account or financial account. When Stripe disburses the financing, the funds first appear in a separate financing balance before Stripe initiates a Capital-specific payout. When a financial partner disburses the financing directly, the funds don’t appear in the connected account’s Stripe balance or payout activity.

The following information applies when Stripe disburses the financing.

#### Item 1

In the Stripe Dashboard, the Capital page shows the financing and its transaction history. **Balances** > **All activity** shows the positive financing deposit, and **Payouts** shows the Capital-specific payout and its status and details.

#### Item 2

In the Express Dashboard, **Financing** shows the financing details, **Balance** and transaction activity show the positive financing deposit, and **Payouts** shows the Capital-specific payout and its status and details.

#### Item 3

The [Capital financing component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing.md) or an Account Link with `type` set to `capital_financing_reporting` shows the financing balance and transaction history. The Balance component shows balance and payout timing, while the Payouts component shows payout history, status, details, and the transactions included in an automatic payout. You don’t need a separate Capital payout component.

#### Payout and balance activity

When Stripe disburses the financing, Stripe first credits the financing to the connected account’s Stripe balance as a positive balance transaction with `type` set to `financing_payout` and `reporting_category` set to `financing_payout`. Stripe holds the funds in a separate financing source balance until it initiates the Capital payout. The funds aren’t combined with the connected account’s other available balances and aren’t available for platform-initiated payouts.

Stripe initiates a separate payout from the financing source balance to the connected account’s bank account. This Capital payout is independent of the connected account’s regular payouts. The financing credit and bank payout are separate records and can occur at different times. See [Capital reporting and reconciliation](https://docs.stripe.com/capital/reporting-and-reconciliation.md) for details on all balance transactions.

### Connected accounts pay the financing

Stripe automatically applies a percentage of eligible payments to the financing balance. Connected accounts can also make additional or manual payments. For financing products with a minimum or fixed periodic payment, Stripe might debit the connected account’s bank account to cover a shortfall. See [how Stripe Capital payments work](https://docs.stripe.com/capital/how-stripe-capital-works.md?capital-country=US#pay-down-your-financing).

Your [Connect charge type](https://docs.stripe.com/connect/charges.md) determines which amount Stripe withholds from.

| [Direct charges](https://docs.stripe.com/connect/direct-charges.md) | [Destination charges](https://docs.stripe.com/connect/destination-charges.md) | [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) |
| --- | --- | --- |
| Stripe withholds from the connected account’s eligible charge amount, including any application fee. | Stripe withholds from the amount transferred to the connected account, not from the charge on your platform. This applies whether you set `on_behalf_of`. | Stripe withholds from each eligible transfer to the connected account, not from the charge on your platform. |

#### Where withholding appears

Stripe automatically records withholding and displays the resulting financing, balance, and payout activity. If your connected accounts use a Stripe-hosted Dashboard, you don’t need to make any changes.

#### Item 1

The Capital page shows payment progress and payment history. **Balances** > **All activity** shows each Capital payment as balance activity, and automatic-payout details show the transactions included in that payout.

#### Item 2

**Financing** shows payment progress and payment history. Balance and transaction activity show each Capital payment, and automatic-payout details show the transactions included in that payout.

#### Item 3

The [Capital financing component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing.md) or an Account Link with `type` set to `capital_financing_reporting` shows payment progress, payment history, the financing balance, and manual-payment controls when available. The Payouts component shows automatic-payout status and details and the transactions included in the payout, including Capital withholding in the transaction overlay. The Balance component continues to show balance and payout timing.

#### Payment activity and custom reporting

Capital payments can include automatic withholding, connected account-initiated bank payments, and collection attempts. They generally appear as Balance Transactions. If you build custom reports, use [Capital reporting and reconciliation](https://docs.stripe.com/capital/reporting-and-reconciliation.md) for the complete transaction types, API fields, reversal handling, and reconciliation guidance.

### Stripe services the financing

Stripe services the financing until the connected account repays it in full. The connected account can track progress, review transactions, make applicable payments, and get support directly from Stripe.

#### Item 1

The connected account uses the hosted Capital flow in the Stripe Dashboard to track progress, review transactions, make payments when available, and get support.

#### Item 2

The connected account uses **Financing** in the Express Dashboard to track progress, review transactions, make payments when available, and get support. You can disable Capital for your connected accounts, but existing offers remain available until they expire and active financing continues through completion.

#### Item 3

Use the [Capital financing component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing.md) or an Account Link with `type` set to `capital_financing_reporting` to provide progress, transaction history, applicable payments, and support routing.

