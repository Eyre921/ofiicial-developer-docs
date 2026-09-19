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

## Select the state for TaxJar to file in

1. In the Dashboard, navigate to **Locations** > [Collecting and filing](https://dashboard.stripe.com/tax/registrations).
2. Select the state where you want to set up filing.
3. Click the overflow menu (⋯) on the right side, then select **Set up filing**. If you’re not already subscribed to [Tax Complete](https://stripe.com/tax/pricing), you can sign up now.

Alternatively, you can go to **+ Quick Actions** and select **Setup filing**.

## Install the TaxJar app and create an account

Select **Install** to connect the TaxJar App. Stripe will then create a TaxJar account for you. If you already have a TaxJar account, select this option and you’ll be redirected to TaxJar Support. This account lets you access TaxJar directly from your Stripe account without needing an additional login or password.

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

## Review your filing reports

Each month, before TaxJar begins processing your returns, it sends a summary of your upcoming filings to the email address associated with your account. The email includes the US locations where you’re signed up for automated filing and reminds you to review your filing reports.

You can view a summary of what TaxJar will file for you in the current month in the **Filings** tab within the TaxJar app. From there, you can see the estimated tax payment, including any filing discounts the state offers for on-time filing. Select **Review report on TaxJar** to see a detailed breakdown of what TaxJar will file on your behalf.

To reconcile this report with your Stripe data:

### Run the Itemized export in Stripe

1. Log in to the [Stripe Dashboard](https://dashboard.stripe.com/).
2. Select **+ Quick actions** > **Export transactions**.
3. Under **Select a location**, choose the relevant state.
4. Set your time zone to **UTC**. This ensures you’re comparing the same reporting periods in both Stripe and TaxJar.
5. Select **Itemized export** and choose your preferred file format: CSV or XLSX.
6. Select the box to send the export to your account email. We recommend this for exports with a large number of transactions.
7. Select **Export**.

### Export transactions from TaxJar

1. From the **Filings** tab in the [TaxJar app](https://dashboard.stripe.com/dashboard?apps%5Bcom.app.taxjar%5D%5Bdrawer%5D=), select the relevant state, then click **View Report on TaxJar**.
2. TaxJar directs you to the state tax report.
3. Select the correct filing period, if needed.
4. Select **View Transactions** to see all the sales from that filing period.
5. From the **Actions** dropdown menu, select **Export Receipts to CSV**.

### Match individual transactions

To understand how a particular sale was handled, compare it in both export reports. Individual transactions can be located by their unique order number, which appears in the `id (column A)` of the Stripe itemized tax report and in `order_ID (column B)` of the TaxJar export.

### Understanding minor discrepancies

TaxJar reports the sales tax that was collected through Stripe Tax. It’s common to see slight differences between the two reports, and these are generally caused by routine tax compliance procedures, such as:

**Filing discounts**: Many US states offer a small discount if you file and pay on time. TaxJar automatically applies these discounts where applicable.

**Rounding rules specific to each jurisdiction**: Different tax authorities enforce their own standards for how they round figures on official returns. These rounding differences tend to be more apparent for businesses that process high volumes of lower-priced items, but they are both expected and necessary to stay compliant.

### Common scenarios

**Refunds**: TaxJar deducts refunds and returns from gross sales in the filing period when the refund occurred, regardless of the original transaction date. If refunds exceed sales in a given filing period, creating a negative balance, TaxJar automatically carries those refunds forward to the next filing period.

**Transactions without automatic tax enabled**: The TaxJar tax return only includes transactions where automatic tax is enabled in Stripe Tax. Common examples include:

- Manual invoices created in Stripe without Stripe Tax applied
- Transactions using manual tax rates
- Sales processed before Stripe Tax was enabled on your account

TaxJar includes transactions where Stripe Tax calculated and collected the tax. To include other transactions in your tax filings, contact TaxJar support at [support@taxjar.com](mailto:support@taxjar.com).

### Next steps

If you disagree with the filing report or need to make changes, you must [pause your filings](https://stripe-tax-filing.helpscoutdocs.com/article/1152-pause) before the 6th of the month at 6 PM ET. For help understanding specific differences or resolving issues, contact TaxJar support at [support@taxjar.com](mailto:support@taxjar.com). If everything looks correct, no action is required. TaxJar automatically begins processing filings as early as the 7th of the month and sends you a confirmation email when complete. You can view completed filings at any time in your [TaxJar Filing History](https://stripe-tax-filing.helpscoutdocs.com/article/1217-how-to-view-your-completed-filings).

