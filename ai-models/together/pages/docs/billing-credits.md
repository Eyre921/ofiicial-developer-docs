---
title: "Credits"
source: https://docs.together.ai/docs/billing-credits
path: docs/billing-credits
---

Understanding credits and billing basics on Together AI.

## What are credits used for?

Together credits are the unit used to measure and charge for usage of Together AI services on your account. Once purchased, credits can be used immediately for:

* API requests
* Dedicated model inference
* Fine-tuning jobs
* Evaluation jobs
* All other Together AI services

Note that you need sufficient balance to cover the costs of dedicated endpoint creation or fine-tuning/evaluation job creation.

## Free trial and access requirements

Together AI does not currently offer free trials. Access to the Together platform requires a minimum \$5 credit purchase.

Together AI is **fully prepaid**. You need a positive credit balance to use the platform. Add credits from your [billing settings](https://api.together.ai/settings/organization/~current/billing) before making API calls. If your balance reaches zero, API access is suspended until you add credits.

Customers with an active Scale or Enterprise contract continue to be billed under their existing contract terms.

## Buy credits

1. Go to your [billing settings](https://api.together.ai/settings/organization/~current/billing).
2. In the **Credit balance** card, select **Add credits**.
3. Enter an amount (minimum \$5) and confirm. The purchase uses your default payment method.

Credits from card purchases usually appear in your balance within a few moments. Avoid re-submitting the purchase while it's pending. ACH purchases deposit credits only after the payment clears, usually 1–3 business days. See [Payment methods & invoices](/docs/billing-payment-methods) for adding payment methods and changing the default.

## Auto-recharge credits

Together supports automatic credit purchases when your balance falls below a set threshold. When auto-recharge runs, your **default** payment method is charged in a **single transaction** to bring your balance up to your target.

**Auto-recharge and ACH:** Auto-recharge is available only when your default payment method is a credit or debit card. If your default is a US bank account (ACH), auto-recharge is not available, even if you also have a card saved. If a card is your default, auto-recharge works normally even when ACH is also on file. Setting ACH as default turns auto-recharge off automatically.

To enable auto-recharge:

1. Go to your [billing settings](https://api.together.ai/settings/organization/~current/billing)
2. In the **Auto-recharge** panel, select **Set thresholds** (or **Edit limits** if auto-recharge is already configured)
3. Enable automatic credit purchases and set:
   * **When balance goes below:** The balance at which auto-recharge is triggered
   * **Bring credit balance up to:** The target balance after auto-recharge runs. You are charged the amount needed to reach this target.
4. Save your settings

Note: If you set a threshold above your current balance, auto-recharge triggers immediately with one purchase to bring your balance up to your target.

Manual credit purchases also use your default payment method. See [Payment methods & invoices](/docs/billing-payment-methods) for how to add methods and change the default.

## Credit expiration

No, prepaid balance credits in your Together.ai account do not currently have an expiration date. You can use your credits at any time after purchase.

If any changes to this policy are made in the future, Together.ai will notify customers in advance through official communications.

Everyone's circumstances are different, and no customer should ever be put in a tricky situation by an unexpected bill.

To try and avoid such a situation, we offer usage based billing and credit packs, which are charged at the time of purchase.

**Important:** Credits purchased after an invoice is generated cannot be used to clear previous invoices or past due balances. Past due balances must be paid separately using a valid payment method, regardless of your available credit balance.

If you're experiencing access issues with a positive balance, check whether your credits are free credits or purchased credits. Platform access requires the minimum \$5 credit purchase described above.
