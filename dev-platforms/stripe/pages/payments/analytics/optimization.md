---
title: "Authorization Boost"
source: https://docs.stripe.com/payments/analytics/optimization.md
path: payments/analytics/optimization
---

# Payments optimization

Learn how Authorization Boost can increase your payment success rate and lower processing costs.
![Authorization boost](https://b.stripecdn.com/docs-statics-srv/assets/authboost.44ac4691d5b4920499cd5a96b634c2d6.png)

Use the [Optimization](https://dashboard.stripe.com/optimization) page to view the estimated increase in payment volume, success rate, and cost savings from optimization features. This page describes the [Stripe Authorization Boost features](https://docs.stripe.com/payments/analytics/optimization.md#authorization-boost-features) that you can use to help increase your success rates on *card-not-present (CNP)* (A card-not-present (CNP) transaction is a purchase made remotely, without processing a physical card in a card reader, or without the cardholder manually entering a PIN. Common CNP transactions include online shopping, card-on-file payments, phone or mail orders, recurring payments, and online invoices) payments by applying AI-driven adjustments to payment attempts that fail or aren’t properly formatted. If you’re on *IC+* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing, some optimization features can also reduce network costs.

> Stripe doesn’t guarantee any outcomes for your use of Authorization Boost features. The optimization calculations we provide are estimates. You can use the data we provide to help inform your decision-making about whether to use these features. Refer to this page regularly to make sure you have the most up-to-date optimization feature information.

## Authorization Boost features 

Stripe uses the following Authorization Boost features to improve your success rates and reduce your costs on card-not-present payments. Learn more about [optimizing authorization rates](https://stripe.com/guides/optimizing-authorization-rates#how-stripe-can-help).

### Adaptive Acceptance

Adaptive Acceptance uses AI to reformat payment requests based on card issuers’ preferences. Stripe can make these changes before sending a payment or after a payment is declined.

For example, Stripe selectively adjusts and reattempts declined payments in real time, which can help recover a significant number of false declines. Additionally, Adaptive Acceptance might apply cost optimizations for businesses on IC+ pricing to help reduce network or interchange fees, or might reattempt a declined payment on an alternative card network.

| When optimization is applied | Description |
| --- | --- |
| **Recovery** | Stripe retries an initially declined payment, and the retry is successful.

PINless retries: In the US, Stripe might automatically retry an eligible transaction on a US debit network (also known as PINless network) after it’s declined on an international network (Visa or Mastercard).

Stripe also reformats the payment before authorization based on issuer preferences. |
| **Cost savings** | **Excessive retry prevention**: Stripe blocks a payment that would have incurred network retry penalties and likely failed.

**Decline prevention**: Stripe blocks a payment from reaching the card network that was unlikely to succeed, avoiding additional scheme fees for the payment.

**Data Only 3DS**: Stripe reduces scheme fees by sharing additional transaction data with issuers through [Data Only flows](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions.md#data-only), without challenging the cardholder. |

### Card account updater 

Card numbers and expiration dates regularly change, and outdated card information is a common source of declines for online businesses. Stripe uses the card account updater services offered by major card networks to improve acceptance by retrieving and updating saved card payment information automatically.

| When optimization is applied | Description |
| --- | --- |
| **Recovery** | A successful payment is made using a card that previously had updates to the underlying card information. Updates include changes to the card expiration date or the primary account number (PAN). |
| **Cost savings** | Not applicable |

### Network tokens

Network tokens are payment credentials that serve as more secure substitutes for card numbers. Network tokens can help you process payments with the most up-to-date credentials, even if the underlying card data has changed, improving success rates. For businesses on interchange pricing, using network tokens can also offer cost savings.

Stripe uses integrations with major card networks to tokenize your cards. Learn more about [network tokens](https://stripe.com/guides/understanding-benefits-of-network-tokens).

| When optimization is applied | Description |
| --- | --- |
| **Recovery** | A payment succeeds using a network token. The likelihood that the network token leads to payment success is significantly higher when the underlying card information was previously updated. Updates include changes to the card expiration date or the primary account number (PAN). |
| **Cost savings** | A payment uses a network token, which helps you qualify for reduced interchange or avoid scheme fee penalties. |

## How Stripe calculates recovered revenue from optimizations 

For each payment, Stripe assesses the likelihood that optimizations contributed to its success, given that some payments might have otherwise still been approved. This approach helps Stripe estimate the true impact on your business more accurately. If you apply multiple optimizations to a single payment, we attribute the benefit to the one most likely responsible for approval.

Here’s an example calculation:

- We determine which payments benefited from the use of an optimization feature. For example, your business had 100 payments that were optimized from a feature, each with an amount of `50 USD`.
- We determine the estimated likelihood that the feature led to the payment succeeding, where it would’ve otherwise failed. In this example, let’s assume a `20%` likelihood for each of the 100 payments for the applied optimization (actual likelihoods might differ).
- To calculate the recovered payment volume, we sum the total amount attributed to these optimized payments and multiply this sum by the probability that feature was responsible for the approval. In this example, the estimated recovered volume is: `100 payments * 50 USD * 0.20 = 1,000 USD`.

## How Stripe calculates cost savings from optimizations 

Optimization features can help reduce network costs for businesses on IC+ pricing. For example, Adaptive Acceptance might block payments that are unlikely to succeed to save you unnecessary network fees. Network tokens also lower interchange rates and prevent scheme fee penalties in certain markets.

For each payment, Stripe calculates the network cost savings that optimizations helped reduce. Stripe uses interchange and scheme fee rules or specifications from card networks to compute costs you would have incurred without the use of optimizations.

> Stripe infers what network costs would have been without the use of optimizations, and the expected network costs with the use of optimizations. However, Stripe doesn’t reconcile these estimates directly with the fees applied to your account.

### How Adaptive Acceptance can lower costs 

- **Excessive retry prevention**: This feature saves you retry penalty fees by blocking payments that either you or your customer previously attempted. Excessive retry prevention blocks charges that are subject to network penalty fees based on prior network decline or advice codes and are likely to fail. 

- **Decline prevention**: Stripe uses AI to estimate the probability of a payment succeeding. We block payments that are unlikely to succeed before they reach the card networks, saving you unnecessary scheme fees. Stripe computes savings as the network costs associated with attempting a payment with card networks.

- **Data Only 3DS**: Stripe intelligently reduces scheme fees by using [Data Only flows](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions.md#data-only) for low risk payments without adding additional friction for cardholders.

### How network tokens can lower costs 

- **Interchange savings**: Some payments that use a network token qualify for reduced interchange rates. For example, Visa offers certain discounts on consumer card-not-present payments in some markets. Not all business industries qualify, and qualification is based on your [Merchant Category Code (MCC)](https://docs.stripe.com/connect/setting-mcc.md#list).

- **Scheme fee savings**: Network tokens can prevent scheme fees for card brands that charge network scheme fees for using outdated credentials. For example, Mastercard levies a Credential Continuity Program (CCP) fee when attempting a payment using outdated card details.

The [Optimization](https://dashboard.stripe.com/optimization) page shows cost saving estimates only for domestic payments in the US and Canada, though you might also realize savings in other markets.

Stripe doesn’t reflect any fees that might occur as a result of network token use, such as the Visa Digital Credential Updater (VDCU) fee. Any such fees reduce the overall cost saving benefits from network tokens.

## Specify date range and aggregation 

You can specify a date range and aggregation filter. If you specify a range and aggregation, they apply to all of your charts, metrics, and tables. Selecting different aggregations helps you to see trends and patterns more clearly based on your goals.

### Specify the date range 

Select the date range and choose a specific period you want to analyze. You can choose from predefined options (such as **Last 3 months** or **Last 6 months**) or set a custom date range, depending on your analytical needs.

### Specify the aggregation method 

Next to the date range selector, select the aggregation period. This allows you to view data in specific intervals, such as weekly or monthly.

## Authorization Boost impact 

Use this report to see the estimated recovered volume, number of recovered payments, success rate increase, and cost savings for each optimization feature.

- To see the volume of payments recovered by using optimizations, click **Payment volume**.
- To see the number of payments recovered by using optimizations, click **Payments**.
- To see the costs saved by using optimizations, click **Cost savings**.

|  |
| **Recovered volume** | The total estimated monetary amount of payments that were successfully processed as a result of the optimization feature, which might have failed without it. It measures the financial impact of the optimization in terms of revenue retention. |
| **Recovered payments** | The estimated number of individual payments that were successfully approved as a result of the optimization feature, which might have been declined without it. |
| **Success rate increase** | The estimated growth in the approval rate as a result of the optimization feature. Stripe models this based on what we think the success rate is without this feature. |
| **Cost savings** | The total estimated network cost savings as a result of the optimization feature. The features that might drive cost savings for IC+ businesses are Adaptive Acceptance and network tokens. |

If you prefer a summary view of impact metrics, rather than a breakdown by feature, you can enable the switch on this report with the label `Show summary`.

Cost savings are available through Adaptive Acceptance for IC+ businesses that use Authorization Boost. Cost savings appear in the Dashboard if your business has the equivalent of 100 USD or more in cost savings across Adaptive Acceptance and network tokens in the last 12 months.

### Download breakdown 

To download analytics for the volume and payments recovered, click **Download** at the bottom of the chart. The download shows you individual payments where Stripe applied optimization features for acceptance rate benefits, and the estimated likelihood that the payment succeeded as a result of using the feature.

## Payment success rate 

This chart helps you visually compare what your estimated payment success rate is without the use of optimizations. The success rate on this chart is for card-not-present payments only and shows the raw rate, rather than the deduplicated rate. The raw rate counts all attempts to make the same purchases, whereas the deduplicated rate groups retried attempts together and calculates acceptance based on the final outcome.
![Payment success rate](https://b.stripecdn.com/docs-statics-srv/assets/payment-success-rate.a1d98c13714dc13ee3cb490939064ec8.png)

The blue dotted line is your estimated rate without optimization features.

## See also

- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance.md)

