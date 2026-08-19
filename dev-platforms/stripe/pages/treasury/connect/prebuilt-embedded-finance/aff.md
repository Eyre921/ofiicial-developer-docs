---
title: "Administrative facilitation fee"
source: https://docs.stripe.com/treasury/connect/prebuilt-embedded-finance/aff.md
path: treasury/connect/prebuilt-embedded-finance/aff
---

# Administrative facilitation fee

Understand how Stripe calculates and pays out the administrative facilitation fee for your platform.
Available in: US
Stripe pays eligible Connect platforms an administrative facilitation fee (AFF) as compensation for providing administrative services in connection with your connected accounts’ financial accounts.

> #### Eligibility
> 
> AFF is available to eligible EFS platforms in the US only. To add AFF to your Stripe contract, [contact Stripe](https://stripe.com/contact/sales).

## AFF Calculation

Each day at 23:59:59 UTC, Stripe records the end-of-day (EOD) balance of each financial account, treating negative balances as 0 USD.

Stripe calculates the daily AFF using the following formula, rounded to the nearest cent:

`(sum of financial account EOD balances) × (EFFR - N bps) / 360`

- **EFFR** is the 50th percentile Effective Federal Funds Rate published by the [Federal Reserve Bank of New York](https://www.newyorkfed.org/markets/reference-rates/effr).
- **N bps** is the negotiated rate in your contract. If EFFR is lower than N bps, the daily AFF is 0 USD.
- For non-business days, Stripe uses the previous business day’s EFFR value.

The following example illustrates three days of AFF calculations for one financial account:

| Day | EOD balance | EFFR midpoint rate % | AFF rate in contract | Calculation | Daily AFF |
| --- | --- | --- | --- | --- | --- |
| 1 | 20,000 USD | 4.33 | EFFR - 275 bps | 20000 × (0.0433 - 0.0275) / 360 | 0.88 USD |
| 2 | 22,000 USD | 3.80 | EFFR - 275 bps | 22000 × (0.038 - 0.0275) / 360 | 0.64 USD |
| 3 | 15,000 USD | 3.80 | EFFR - 275 bps | 15000 × (0.038 - 0.0275) / 360 | 0.44 USD |

Total AFF for the 3 days: 0.88 + 0.64 + 0.44 = **1.96 USD**.

## AFF Payouts

You receive the sum of all daily AFF amounts from the previous month, with no compounding, by the 4th of each month.

You can view your monthly AFF earnings under **Transactions** > **All Activity** > **Financial Accounts** in the Dashboard. AFF payouts appear with the label **Treasury for platforms - Administrative Facilitation Fee** and the relevant date range.

## Download AFF reports

You can download a detailed breakdown of your AFF data from the Dashboard. The [Financial account balance summary](https://dashboard.stripe.com/reports/financial-account-balance-summary) report includes per-account, per-day breakdowns of EOD balance, EFFR value, and fee amount.

## See also

- [Prebuilt embedded finance](https://docs.stripe.com/treasury/connect/prebuilt-embedded-finance.md)
- [Financial accounts](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md)

