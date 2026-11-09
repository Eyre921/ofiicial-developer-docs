---
title: "Multi-currency settlement"
source: https://docs.stripe.com/payouts/multi-currency-settlement.md
path: payouts/multi-currency-settlement
---

# Multi-currency settlement

Accept, settle, and pay out funds in multiple currencies.

If you’re a Connect platform looking to offer multi-currency settlement capabilities to your connected accounts, see our [Connect docs](https://docs.stripe.com/connect/multi-currency-settlement.md).

Stripe automatically converts all incoming funds into your default currency. With multi-currency settlement, you can configure your account to accrue balances and get paid out in up to 18 supported currencies to pay suppliers, process refunds, and avoid FX fees. Where supported, you can use [instant currency conversion](https://docs.stripe.com/treasury/convert-funds.md) to convert between currencies.

## Availability

Multi-currency settlement is available in the following locations:

- AE
- AU
- CH
- EU
- GB
- HK
- LI
- NO
- SG
- US

## Enable multi-currency settlement

Enable additional settlement currencies in your [settlement settings](https://dashboard.stripe.com/settings/settlement). Select a currency, then confirm and save your changes. To accrue a balance in a currency, accept payments presented in that currency. You can also manage settlement currencies using the [settlement_currencies](https://docs.stripe.com/api/balance-settings/update.md?api-version=2026-10-28.preview#update_balance_settings-payments-settlement_currencies) parameter on the Balance Settings API.

## Disable multi-currency settlement

In your [settlement settings](https://dashboard.stripe.com/settings/settlement), select a settlement currency to disable, then confirm and save your changes. Repeat this process for each additional currency you want to disable. You can’t disable your default settlement currency.

## Add bank accounts for local-currency payouts

To receive payouts in a settlement currency, you must add a separate supported bank account with the same currency. Add bank accounts in [Payout Settings](https://dashboard.stripe.com/settings/money-management). Stripe sends payouts from each multi-currency balance to the bank account with the matching currency.

## Configure payout settings

After you meet a currency’s [minimum payout amount](https://docs.stripe.com/payouts/multi-currency-settlement.md#multicurrency-settlement-fees), payouts follow your configured [payout schedule](https://docs.stripe.com/connect/manage-payout-schedule.md), whether manual or automatic. You can’t pay out until your balance for the currency meets the minimum payout amount.

## Settlement pricing and minimum payout amounts 

Stripe charges the applicable fee when funds settle into a non-primary settlement currency, not when you initiate a payout. The following table shows the pricing, supported bank-account countries, and minimum payout amounts for each settlement currency.
[See table on original page](https://docs.stripe.com/payouts/multi-currency-settlement)
## See also

- [Instant currency conversion](https://docs.stripe.com/treasury/convert-funds.md)
- [Supported currencies](https://docs.stripe.com/currencies.md)
- [Localize prices](https://docs.stripe.com/payments/currencies/localize-prices.md)
- [Multi-currency settlement for Connect platforms and marketplaces](https://docs.stripe.com/connect/multi-currency-settlement.md)

