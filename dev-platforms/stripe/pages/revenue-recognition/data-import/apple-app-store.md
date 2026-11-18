---
title: "Stripe Connector for the Apple App Store"
source: https://docs.stripe.com/revenue-recognition/data-import/apple-app-store.md
path: revenue-recognition/data-import/apple-app-store
---

# Stripe Connector for the Apple App Store

Manage your revenue recognition in Stripe by importing data from the Apple App Store.

The [Stripe Connector for the Apple App Store](https://docs.stripe.com/data/import-external-data/connectors/apple-app-store.md) lets you automatically import subscription purchases from the Apple App Store into [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition.md).

The benefits of using Stripe Revenue Recognition for the Apple App Store are:

- **Automated imports**: Stripe fetches Apple App Store data daily and processes it before Revenue Recognition reports reflect it.
- **Increased accuracy**: Improve recognition accuracy by considering time zone differences.
- **Improved refund treatment**: Associate refunds with original purchases, and generate more accurate refund journal entries that adjust deferred revenue instead of treating refunds as negative line items.
- **Audit by subscribers**: Break down numbers on a per subscriber basis to help with audits.

## Get started 

To import data from the Apple App Store, [set up the Stripe Connector for the Apple App Store](https://docs.stripe.com/data/import-external-data/connectors/apple-app-store.md). Stripe fetches data daily. Revenue Recognition reports reflect the data approximately 24 hours after connector import, not 24 hours after the original purchase. These timings are estimates. See [Revenue Recognition data freshness](https://docs.stripe.com/revenue-recognition/data-freshness.md).

### Follow an import through to revenue 

Follow the [subscription purchase example](https://docs.stripe.com/revenue-recognition/data-import/apple-app-store.md#subscription-purchase) from import to accounting output. The connector imports Apple subscription data for Revenue Recognition, not to collect another payment or create a Stripe Billing subscription.

1. **Prepare the connection**: Complete the linked connector setup. If you previously uploaded Apple sales manually, follow the [migration instructions](https://docs.stripe.com/revenue-recognition/data-import/apple-app-store.md#manual-data-import) to remove overlapping transactions.
2. **Verify the import**: After a daily fetch, check the connector’s status and latest sync details in [Data management](https://dashboard.stripe.com/data-management/connectors). A successful sync doesn’t mean the revenue is already visible.
3. **Wait for accounting processing**: Allow approximately 24 hours after connector import. Check the data freshness timestamp on the Revenue Recognition overview before concluding that a sale is missing. Don’t upload a manual copy to compensate for this delay.
4. **Verify the financial output**: Follow the [subscriber audit steps](https://docs.stripe.com/revenue-recognition/data-import/apple-app-store.md#audit-numbers) and compare the balances with the example’s table. The 31 USD developer proceeds increase External Asset, with 28 USD recognized in December and 3 USD deferred until January. Revenue Recognition uses developer proceeds, not the 32 USD customer price, and [doesn’t book Apple commissions or tax liabilities](https://docs.stripe.com/revenue-recognition/data-import/apple-app-store.md#limitations).

#### Correct data without duplicating the sale 

Choose the correction path based on where the issue occurred:

- **A failed sync**: Follow the [connection maintenance instructions](https://docs.stripe.com/data/import-external-data/connectors/apple-app-store.md#maintain-connection) to re-authenticate or resolve an Apple agreement issue.
- **An overlapping manual CSV import**: Follow the [migration instructions](https://docs.stripe.com/revenue-recognition/data-import/apple-app-store.md#manual-data-import). Reports can take up to 24 hours to reflect deletions. Verify the remaining connector-generated revenue in the subscriber audit view.
- **An unexpected amount or service period in connector data**: Compare the source report with the subscriber audit view and contact [Stripe support](https://support.stripe.com/contact) before attempting a manual replacement or re-import. Don’t assume a CSV upload replaces connector-generated records or that deleting and reconnecting the connector reverses previous accounting entries.

For corrections that belong in a past accounting period, [open the period and wait for recalculation](https://docs.stripe.com/revenue-recognition/data-import.md#opening-accounting-periods) instead of re-importing.

### Backfill historical data 

When you onboard, the connector backfills up to 1 year of historical data.

### Handle Apple transactions previously imported through manual data import 

If you previously imported data from the Apple App Store using the Stripe Revenue Recognition [data import](https://docs.stripe.com/revenue-recognition/data-import.md#general-import) feature, you want to avoid double-counting Apple revenue upon switching to the automated connector.

To migrate from manual data imports to the connector, [delete](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data.md#transactions-deletion) all Apple transactions from the past year that you manually uploaded using data import CSVs. The connector replaces these transactions with the entries it generates during import.

> Because the connector only backfills up to 1 year of historical data, we recommend keeping your data import CSV uploads for Apple transactions that occurred more than 1 year ago.

## Examples 

### Subscription purchase 

A subscriber purchases 1 unit of a News Plan Monthly subscription on December 3. The subscription is valid for 1 month, which means the service period is December 3 to January 3. The customer pays 32 USD, but the developer receives 31 USD.

The developer proceeds count toward revenue rather than customer price, because the customer price also includes taxes and Apple commissions. Revenue is billed and paid in full on December 3. Stripe recognizes most of the revenue in December, and a smaller portion in January.

At the end of January, the summary might look like this:

| Account | December | January |
| --- | --- | --- |
| External Asset | +31 |  |
| Revenue | +28 | +3 |
| Deferred Revenue | +3 | -3 |

### Subscription refund 

A subscriber purchases a 3-month subscription on January 2. The service period is January 2 to April 2. The customer pays 91 USD, but the developer receives 90 USD. On February 1, the customer receives a full refund.

During a full refund:

- The customer receives their money back.
- Recognized revenue is offset by the refunds in a contra revenue account.
- The unused portion of the subscription revenue is cleared from the deferred revenue.

The refund reduces the external assets balance by 90 USD. The customer received 30 days of service, so you add 30 USD to the external refunds balance. The remainder of the deferred revenue–60 USD in this example–is also cleared.

At the end of April, the summary might look like this:

| Account | December | January |
| --- | --- | --- |
| Revenue | +30 |  |
| Deferred Revenue | +60 | -60 |
| External Asset | +90 | -90 |
| External Refunds |  | +30 |

### Free trial 

Stripe doesn’t generate journal entries for free trials.

## Limitations 

- The most detailed reporting Stripe can provide is an audit by subscriber. Stripe can’t provide an invoice-level audit because Apple App Store financial reports don’t include invoice IDs.
- Stripe can’t book tax liabilities or Apple commissions because Apple doesn’t provide the required data.
- The connector supports auto-renewable subscriptions but not one-time in-app purchases. The report becomes available after you sell at least one auto-renewable subscription. Subscriptions sold at introductory prices count toward this requirement. For more information, see [Apple’s report availability documentation](https://developer.apple.com/help/app-store-connect/reference/reporting/sales-and-trends-reports-availability/).

## Audit numbers 

To view account balances for an Apple subscriber:

1. Click a number in the [Period summary](https://docs.stripe.com/revenue-recognition/reports/period-summary.md) section to view a list of customers. Apple subscribers have names that consist solely of numbers.
2. Click any Apple subscriber to enter the audit view.

