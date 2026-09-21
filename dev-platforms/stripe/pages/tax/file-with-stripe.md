---
title: "File US sales tax with Stripe"
source: https://docs.stripe.com/tax/file-with-stripe.md
path: tax/file-with-stripe
---

# File with Stripe

Learn about filing with Stripe using TaxJar.

You can set up and manage sales tax filing directly in the Stripe Dashboard. Stripe Tax integrates with TaxJar to automate filing for US sales tax, helping you file on time and avoid errors that can occur with manual filing.

## Availability

Automated US filing is available in all 46 US locations with a state-level sales and use tax.

## Before you begin

- **Set up Stripe Tax**: To enable calculations and collection with Stripe Tax, see [Set up Tax](https://docs.stripe.com/tax/set-up.md). Make sure you’ve [added your tax registrations](https://docs.stripe.com/tax/set-up.md#add-registrations). If you haven’t registered with the taxing authorities and you sell remotely in the US, [Stripe can register with local tax authorities](https://docs.stripe.com/tax/use-stripe-to-register.md) on your behalf.
- **Sign up for Tax Complete**: For TaxJar to file on your behalf, you need a [Tax Complete](https://stripe.com/tax/pricing) subscription plan.
- **Make sure you have a US-based bank account**: TaxJar uses this account to remit your collected tax to the applicable state taxing authorities. If you’re an international business without a US bank account, you can use a service like [Mercury](https://mercury.com/) to set one up.
- **Gather relevant state tax information**: To sign up for automated filing, you’ll need to provide information about your business. This varies by state, but usually includes data such as your filing frequency and state tax identification number.

## Set up filing

## Select the location you want to file in

1. In the Dashboard, navigate to **Locations** > [Collecting and filing](https://dashboard.stripe.com/tax/registrations).
2. Select the location where you want to file, then select **Set up filing**.

> If you don’t have a [Tax Complete](https://stripe.com/tax/pricing) subscription, you’ll be prompted to sign up during setup.

## Set up filing with TaxJar

Stripe files your US sales tax through TaxJar, a Stripe company that enables US filing. Select **Continue**, and Stripe will create a TaxJar account for you.

This account lets you access TaxJar directly from your Stripe account without needing an additional login or password. You can access TaxJar from the Stripe Dashboard to view your filing history.

> If you already have a TaxJar account, you’ll be redirected to TaxJar Support for assistance.

## Review your business information

Confirm your business details, including your address and [bank details](https://stripe-tax-filing.helpscoutdocs.com/article/1147-banking). TaxJar uses your bank account to remit any tax that you collected to the taxing authorities. Always make sure you have sufficient funds in this bank account to cover your sales tax liabilities. If you have a [debit blocker](https://stripe-tax-filing.helpscoutdocs.com/article/1147-banking#debit-blocks) enabled on your bank account, you could also need to add the ACH originator IDs to your bank account to make sure payments to the taxing authorities process successfully.

## Add your state details

Provide your state-specific business registration and filing information. These details differ by state, but generally include your state tax ID, nexus start date, and assigned filing frequency. Select the first filing period you want Stripe to file, typically the next available filing period. Available filing period options are based on the date you submit your filing application, your filing frequency, and state processing deadlines. TaxJar has [detailed information by state](https://stripe-tax-filing.helpscoutdocs.com/category/1150-set-up-filings) to help you set up your filings.

- **Filing for previous filing periods**: If you need to file returns for previous filing periods, you can request TaxJar to [file overdue returns](https://stripe-tax-filing.helpscoutdocs.com/article/1213-file-overdue-returns) for you.
- **Updating your filing frequency**: If you later receive a notice that a state has changed your filing frequency, [send a copy to TaxJar support](https://stripe-tax-filing.helpscoutdocs.com/article/1214-change-your-filing-frequency-for-a-state) to make sure that your filing is updated correctly and you don’t miss a return.

## Review and submit your application

Review all the information you provided, and click **Submit**.

The TaxJar team reviews your filing application and emails you if they need more information. After TaxJar processes your application and you’re successfully signed up for automated filing, you’ll receive an email. You can check the status of your filing application by navigating to **Locations** > **Collecting and filing** and reviewing the **Filing setup** column:

- (Needs attention): You have a filing setup issue for this location. Check the email address associated with your TaxJar account for details on how to resolve it. You can also view this location by looking at the **Needs attention** filter in your Dashboard, where it’s labeled as a filing setup issue under the **Issue type** column.
- (Cancelled): Your filing setup for this location has been cancelled. To restart the filing setup process, select **Set up filing**.
- (Incomplete): You need to complete your filing setup for this location to enable automated filing.
- (Under review): No action is required from you at this time. TaxJar is reviewing the information you provided and will reach out within two weeks if anything additional is needed .
- (Automatic filing): You’re set up for filing. TaxJar will file on your behalf before the next filing deadline for this location.

If you need help during this process, contact [TaxJar Support](https://stripe-tax-filing.helpscoutdocs.com/article/1145-support).

## How automatic filing works

Each month, before your tax filing begins processing, Stripe sends a summary of your upcoming filings to the email address associated with your TaxJar account. The email includes the locations where you’re signed up for automated filing and a link to review the details of what Stripe will file for you.

You can also review these details in the Stripe Dashboard. Navigate to **Tax > Overview**. Under **Automatic filing with Stripe**, choose the relevant location and period to review what Stripe will file on your behalf.

These details show key totals such as total sales, tax collected, and estimated tax due. You can also review the transactions included in the filing and use filters to find specific transactions. It’s important you review your data for accuracy and completeness before Stripe begins filing for you.

### Import additional transactions

If you need to include additional transactions from another platform in the filing period you’re reviewing, import them using Stripe’s CSV import feature. In the details for that relevant location and period, under **Transactions in this filing**, select **Import**.

You can also import additional sales transactions from the Stripe Dashboard. Navigate to **Tax > Quick actions > Import transactions**, then upload your CSV file.

For CSV formatting requirements, see [Import transactions](https://docs.stripe.com/tax/imports.md#csv-file-format-requirements).

### How Stripe files for you

Stripe files your sales tax returns based on the amount of tax you actually collected. Amounts filed and remitted can vary slightly due to required prepayments, timely filing discounts, rounding, refunds, or incomplete addresses.

**Prepayments**: Some tax authorities require prepayments and communicate when a prepayment is required. Prior prepayments made will decrease the amount of tax you owe for a relevant period while currently due prepayments increase the amount owed for a given period.

**Filing discounts**: Many US states offer taxpayers a small discount if you file and pay on time. Stripe automatically applies these discounts when calculating the amount it will file.

**Rounding rules specific to each jurisdiction**: Different tax authorities enforce their own standards for how they round figures on official returns. These rounding differences tend to be more apparent for businesses that process high volumes of lower-priced items, but they are both expected and necessary to stay compliant.

**Refunds**: Stripe deducts refunds and returns from gross sales in the filing period when the refund occurred, regardless of the original transaction date. If refunds exceed sales in a given filing period, creating a negative balance, Stripe automatically carries those refunds forward to the next filing period. These refunds will be utilized once sufficient sales are available to offset these amounts.

### Common scenarios

**Transactions without automatic tax enabled**: Stripe only includes transactions where automatic tax is enabled. Common examples of transactions that would not be included:

- Manual invoices created in Stripe without Stripe Tax applied
- Transactions using manual tax rates
- Sales processed before Stripe Tax was enabled on your account
- Existing subscriptions that have [not yet been migrated to Stripe Tax](https://docs.stripe.com/billing/taxes/migration.md)

### View additional transaction details

The details for each location will show the transactions Stripe will include in your filing. To review additional transaction-level detail, you can either click on any individual transaction or export itemized transaction data from Stripe.

1. Log in to the [Stripe Dashboard](https://dashboard.stripe.com/).
2. Select **+ Quick actions > Export transactions**.
3. Under **Select a location**, choose the relevant state.
4. Set your time zone to **UTC**.
5. Select **Itemized export** and choose your preferred file format: CSV or XLSX.
6. Select the box to send the export to your account email. We recommend this for exports with a large number of transactions.
7. Select **Export**.

### Understand differences in exported data

In certain cases, not all transactions for a given location will be included in your filing. For example, local amusement taxes may be filed separately from state-level sales and use taxes included on the current return. As a result, the itemized export can differ from the transaction details shown for the relevant location and period.

### Next steps

If all reviewed details are accurate, you don’t need to take further action. Stripe automatically begins processing filings as early as the 7th of the month. You receive an email when your filing is complete.

If you need to make changes to an upcoming automatic filing, submit your request before the 6th of the month at 6 PM ET. In the details for the relevant location and period, click **Request changes** and provide details about the changes you need. After you submit your request, you’ll receive an update at the email address associated with your TaxJar account within three business days.

You can view completed filings at any time in your [TaxJar Filing History](https://stripe-tax-filing.helpscoutdocs.com/article/1217-how-to-view-your-completed-filings).

