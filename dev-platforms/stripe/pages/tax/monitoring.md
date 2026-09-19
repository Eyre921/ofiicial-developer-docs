---
title: "Monitor tax obligations"
source: https://docs.stripe.com/tax/monitoring.md
path: tax/monitoring
---

# Monitor your obligations

Use our tool to see where you might need to register to collect tax based on past transactions.

Stripe Tax provides insights about your potential tax registration obligations (called economic nexus in the US). We help you understand where you might have to register, collect, and remit tax based on your sales into a state or country, even if you don’t have physical presence there. You can also use [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register.md) on your behalf.

> Tax provides threshold monitoring primarily for payments processed by Stripe. The only out of band payments we currently include are invoices processed off of Stripe and transactions created using the Stripe Tax APIs.

## How it works

Stripe Tax tracks your Stripe-processed sales (minus refunds) based on each customer’s location and compares these sales against local tax registration thresholds. It uses your [preset tax code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#preset-tax-codes) and [location attribution](https://docs.stripe.com/tax/monitoring.md#location-attribution) to calculate your total sales within the [time windows](https://docs.stripe.com/tax/monitoring.md#time-window) defined by local tax rules.

The threshold monitoring tool highlights potential registration obligations, but it’s up to you to confirm whether registration is actually required in each jurisdiction. Learn more about [when you need to register to collect tax in each location](https://docs.stripe.com/tax/supported-countries.md).

To correctly determine your tax obligations, Stripe Tax attributes a location to each processed transaction. As a result, the new resulting transactions are added to your monitoring threshold within 7 days (and often sooner, as shown by the last updated date in the Thresholds table).

### Refunds and threshold calculations

Refunding a transaction (or applying a credit note to an invoice) automatically adjusts your threshold calculations to account for the reduction. Your total sales calculations subtract the refunded or credited amount, which might lower your overall sales volume for a particular jurisdiction. If the refund or credit brings you below a previously exceeded threshold, this updates your obligation status. These adjustments typically process within 24-48 hours of the refund.

For a partial refund or credit note, the remaining amount will keep at least 0.01 USD in tax liability. This is because it uses a cumulative remainder approach to deal with rounding.

After a refund processes, your threshold status includes the refunded amount. Your Dashboard still shows any threshold notifications you received before processing the refund.

### Connect

By default, transactions linked to your platform’s connected accounts don’t count toward your platform’s tax registration thresholds. They only count toward the connected accounts’ tax thresholds. To change this:

1. Go to the [Connect settings](https://dashboard.stripe.com/settings/connect/tax-threshold-monitoring) for Sales tax collection.
2. Choose to be held liable for sales made by your connected accounts.

Connected accounts’ transactions with the following charge types are then included in your platform’s threshold monitoring:

| Charge type | Without `on_behalf_of` | With `on_behalf_of` |
| --- | --- | --- |
| [Destination Charges](https://docs.stripe.com/connect/destination-charges.md) | Included. | Included. |
| [Separate Charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) | Not included. | Included. |

Separate charges and transfers without `on_behalf_of` aren’t included. This is because Stripe can’t know who the liable party for the transfer is. Stripe assumes the [settlement party](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) to be the liable entity, which is the Connect Platform.

### Exceptions and assumptions

- We only monitor Stripe-processed sales or [imported transactions](https://docs.stripe.com/tax/imports.md).
- We assume that all sales are conducted with your [preset tax code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#preset-tax-codes).
- We assume that all sales are taxable at the destination. Stripe doesn’t consider the actual location of supply, which might be the merchant’s business address, where the goods are shipped from, or where an event occurs.
- We provide insight into the places where you don’t have a physical presence so obligations aren’t monitored for your home US state or country.
- Obligations are only monitored in live mode.
- Application fees that Connect platforms charge don’t count toward the platform’s tax registration thresholds.
- We monitor Stripe Tax [supported locations](https://docs.stripe.com/tax/supported-countries.md).
- We don’t monitor transactions that might contribute to exceeding a threshold to collect retail delivery fees, amusement taxes, or parking taxes.
- We treat obligations for tangible product sales and services the same.
- We can’t differentiate between retail and wholesale sales.
- We can’t differentiate between marketplace and non-marketplace sales.
- For Connect platforms liable for sales made by their connected accounts, a location might be marked as (Undetermined). This means that Stripe lacks the information needed to support you on tax obligations for this location. This can occur if the customer’s location is outside the United States and not in the United Kingdom or European Union with a default PTC of Digital Goods.
- When a Connect platform reports [PaymentRecords](https://docs.stripe.com/payments/payment-records.md) on behalf of its connected accounts, we don’t count them against the platform’s tax registration thresholds.
- Some US jurisdictions (such as [Arizona](https://docs.stripe.com/tax/supported-countries/united-states/collect-tax.md?tax-jurisdiction-united-states=arizona), [Indiana](https://docs.stripe.com/tax/supported-countries/united-states/collect-tax.md?tax-jurisdiction-united-states=indiana), and [North Carolina](https://docs.stripe.com/tax/supported-countries/united-states/collect-tax.md?tax-jurisdiction-united-states=north-carolina)) include nontaxable sales in their threshold calculations. This might require businesses that sell only nontaxable goods or services register and file a *zero* or *information* tax return, where no tax is due. Read each state’s threshold to learn about specific filing obligations.

### Location attribution 

Location attribution is an important part of monitoring tax thresholds. To correctly determine your tax obligations, Stripe Tax attributes a location to each processed transaction once per day, adding new resulting transactions to your monitoring threshold in a 24-hour cycle. Location attribution happens even if tax isn’t calculated for the transactions, and it’s a different process from the [address validation](https://docs.stripe.com/tax/customer-locations.md) that we perform to calculate tax. You might not need specific tax rates and precise address information for threshold monitoring purposes, unlike when Stripe calculates and collects tax for transactions.

To attribute a location, Stripe Tax uses available information for that transaction and prefers some information sources to others—some examples are the current customer address, country of the card issuer, and the customer’s IP address.

Stripe Tax uses information in the following order:

1. **Stripe Tax validated address:** if we calculated tax for the transaction, Stripe Tax already validated the address. We use the same address when calculating the tax threshold.
2. **Customer address:** property in the [Customer](https://docs.stripe.com/api/customers/object.md) object responsible for the transaction.
Stripe Tax uses the country, state, and postal code fields to determine a jurisdiction.
3. **Address Verification (AVS) postal code:** [AVS](https://docs.stripe.com/disputes/prevention/verification.md#avs-check) is a service that verifies the authenticity of a transaction by checking if the provided address matches the cardholder’s billing address. If the transaction is successful, Stripe Tax converts a US or Canadian postal code into a state and determines the jurisdiction.
4. **Country of the card issuer:** Stripe Tax uses the credit card issuer’s bank country to determine a jurisdiction for the transaction. For transactions in the US and Canada, we might also need state information.
5. **Payment method:** Stripe Tax uses country-specific payment methods to determine the location of a payment. We assume that a transaction through *iDeal* (iDeal is a payment method in the Netherlands that uses direct, online transfers from the user's bank account) is from the Netherlands and that a transaction through Giropay is from Germany, for example.
6. **Customer’s IP address:** as a last resort, we use the customers IP address to determine a jurisdiction.

When Stripe Tax can’t determine the location for a transaction, we group its information into an **Unattributed revenue** category. Where possible, we break out globally unattributed revenue and US unattributed revenue. For example, if we’re able to determine the customer is in the US (perhaps by using an IP address) but don’t have enough information to make a granular determination, we categorize that as US unattributed revenue.
![Unattributed revenue in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/unattributed-revenue.dfbed304297c0e568b633542130bbd39.png)

#### Handling unattributed revenue

The table below explains what information is needed for different countries.

#### United States

| Example addresses | Explanation | Attributed |
| --- | --- | --- |
| - `country`: US
- `state`: NY | **Country and state**

You need to provide country and state information to calculate tax thresholds in the US. | ✓ Attributed |
| - `country`: US
- `postal_code`: 10038 | **Country and postal code**

We match the 5 or 9-digit postal code with its corresponding state. | ✓ Attributed |
| - `country`: US | **Country**

In the US, each state defines it’s rules for when to establish economic nexus. Therefore, country-only information isn’t enough to attribute locations to transactions. Transactions without state information appear under US unattributed revenue. | ✗ Not attributed |

#### Canada

| Example addresses | Explanation | Attributed |
| --- | --- | --- |
| - `country`: CA
- `state`: ON | **Country and state**

Canada defines it’s country-wide tax threshold, but each state might have specific laws. Therefore, we need country, and state information to fully attribute a location to a transaction. | ✓ Attributed |
| - `country`: CA
- `postal_code`: A1A A1A | **Country and postal code**

We match a valid postal code with it’s corresponding state. | ✓ Attributed |
| - `country`: CA | **Country**

Each state might define its specific laws. A transaction without state information counts towards the Canadian country-wide threshold but doesn’t count towards any state-specific threshold. | ⚠ Partially attributed |

#### Everywhere else

| Example addresses | Explanation | Attributed |
| --- | --- | --- |
| - `country`: IE | **Country**

For all other supported countries, the country is the only information we need. | ✓ Not attributed |

## Review potential obligations in the Dashboard 

Use the [Needs attention](https://dashboard.stripe.com/tax/locations?primary_tab=needs_attention) tab to review your potential tax registration obligations.

We group your location statuses into the following categories:

- (Needs attention): You need to make a decision or take action for this location. This can appear when:
  - Your estimated sales or transactions exceed the location’s registration threshold and you need to register.
  - You have an active registration but your tax setup is incomplete (for example, missing head office address or preset product tax code).
  - You have a draft registration application that needs to be submitted.
- (Collecting tax): You have an active registration in this location and your tax setup is complete. Stripe Tax is automatically calculating and collecting tax on applicable transactions.
- (Not collecting tax): You aren’t collecting tax in this location. This can occur when:
  - Your registration is expired.
  - You don’t have a registration and haven’t exceeded the threshold yet.
  - You don’t have a registration and we can’t determine your threshold status (for example, the revenue is unattributed or your preset product tax code doesn’t match the location’s supported tax types).
- (Issue): There’s a problem with your registration application that requires your attention. Review your application details to resolve the issue.
- (Registration in progress): You’ve submitted a registration application through Stripe and our partners, and it’s currently being processed. You’ll be notified when the registration is complete.

To learn more about an individual state or country comparison, click the overflow menu (⋯), then **View details**. This page contains information about the threshold itself and your latest sales.

### Downloading transaction data

In the details view, you can download the transaction data used to compute the threshold.

Downloaded transaction data includes the `is_customer_business` and `is_customer_taxable` fields for completeness, but they might not be relevant or applicable in all [supported jurisdictions](https://docs.stripe.com/tax/supported-countries.md).

Don’t use the transaction data for reporting, as it applies only to the current threshold’s time window. Stripe Tax doesn’t support historical reports on thresholds. The transaction data helps you understand which transactions comprise the threshold computation, but isn’t suitable for other purposes.

### Time windows 

As noted above, each jurisdiction might have a different time window for calculating nexus obligations. For example, some only look at the past calendar month or quarter whereas others use a rolling basis. You can see how each individual jurisdiction calculates economic nexus as part of the Review flow, but in general, Stripe Tax supports the following calculation windows and methodology:

- **Previous or current year:** Stripe Tax uses the previous or current calendar year to calculate the count and amount of transactions.
- **Previous year:** Stripe Tax uses the previous calendar year to calculate the count and amount of transactions.
- **Rolling year by quarter:** Stripe Tax uses the last four full quarters to calculate the count and amount of transactions.
- **Rolling 12 months:** Stripe Tax uses the last 12 months to calculate the count and amount of transactions.

### Stripe Tax API transactions

By default, Stripe Tax monitors all [Stripe Tax API](https://docs.stripe.com/tax/standalone-tax-api.md) transactions. You can exclude your Stripe Tax API transactions by adjusting the **API transactions** setting on the [tax settings](https://dashboard.stripe.com/settings/tax/thresholds) page.

## Tax threshold notifications

Stripe Tax alerts you to potential tax obligations (known as economic nexus in the US) when your business reaches 10,000 USD in yearly revenue. We send notifications after you hit a threshold in any location. Stripe sends tax threshold notifications by email, and displays them in the Dashboard to the account owner.

### Email notification

We send email notifications from `support+updates@stripe.com` to the account owner’s email. The email notification includes:

- A list of locations generating over 5% of your revenue where you’re not registered.
- The count of locations generating less than 5% of your revenue where you’ve recently exceeded a threshold and aren’t registered.
![Preview of tax threshold notification](https://b.stripecdn.com/docs-statics-srv/assets/tax-threshold-email-preview.e685687dcb47a209a7aef60cc2402d36.png)

If you’re registered in one of these locations, add your registration in the [Dashboard](https://dashboard.stripe.com/tax/locations).

### Dashboard notification

If you log into the Dashboard as the account owner, you can see notifications. Click the bell icon in the navigation bar to show all of your Dashboard notifications.

> Click **Review tax thresholds** inside of the notification to go to the tax monitoring tool.

#### Crossing a tax threshold in a single location

You can exceed a tax threshold in a single location.
![](https://b.stripecdn.com/docs-statics-srv/assets/tax-threshold-single-location.c59b7a897eb7c29de32a97c959277b67.png)

#### Crossing tax thresholds in multiple locations

You can exceed tax thresholds in multiple locations during the same day.
![](https://b.stripecdn.com/docs-statics-srv/assets/tax-threshold-multiple-locations.c3e06f52f762750733384d82c1b841ee.png)

### Tax threshold notification preconditions

Stripe only notifies you when you have exceeded a tax threshold based on Stripe’s calculations. To receive tax threshold notifications, you must meet the following requirements:

- You’ve opted into [Stripe Tax](https://dashboard.stripe.com/tax).
- You haven’t disabled [Stripe Tax notifications](https://dashboard.stripe.com/settings/communication-preferences).
- You’ve had 10,000 USD in revenue in the previous year.
- You don’t have an active live mode tax registration for the location.
- You haven’t received any tax threshold notification within the past 7 days.

### Tax threshold notification frequency

After you cross a threshold, Stripe sends you a notification within 1 or 2 days. If Stripe sent you a notification in the past 7 days, you receive batched notifications for new threshold status changes a week after the last notification.

#### No grouping of notifications

1. **March 15**: You exceed a threshold in Germany.
2. **March 16**: Stripe notifies you about exceeding a tax threshold in Germany.
3. **March 25**: You exceed a threshold in the Netherlands.
4. **March 26**: Stripe notifies you about exceeding a tax threshold in the Netherlands.

#### Grouping of notifications

1. **March 15**: You exceed a threshold in Germany.
2. **March 16**: Stripe notifies you about exceeding a tax threshold in Germany.
3. **March 17**: You exceed a threshold in the Netherlands and in Sweden.
4. **March 18**: You exceed a threshold in Denmark.
5. **March 23**: Stripe notifies you about exceeding a tax threshold in the Netherlands, Sweden, and Denmark.

### Configure threshold notifications

As the account owner, manage where we alert you about potential tax obligations. To set your preferences:

1. Go to the [Tax settings](https://dashboard.stripe.com/settings/tax/thresholds) page.
2. Choose your notification preferences for specific locations or regions, or opt out entirely.

## See also

- [Checkout and Tax](https://docs.stripe.com/tax/checkout.md)
- [Billing and Tax](https://docs.stripe.com/billing/taxes/collect-taxes.md)
- [Products, prices, tax codes, and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md)

