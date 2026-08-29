---
title: "Billing troubleshooting"
source: https://docs.together.ai/docs/billing-troubleshooting
path: docs/billing-troubleshooting
---

Resolving payment issues, understanding charges, and managing billing problems.

## Troubleshooting payment declines

There are many reasons that payments can be declined. If your payment isn't going through, check the following:

* Is there enough money in your account to cover the payment?
* Have you filled in all of the address information when adding the card?
* Is the payment card in date?
* Have you activated the card? (If recently replaced)
* Have you entered the correct CVV number?
* **Have you filled in all of the address information when adding the card?** Ensure the billing address exactly matches what's registered with your card provider, including the zip/post code. Even if your payment provider shows the transaction as approved, address mismatches can still cause the payment to be declined.
* **Are you using a supported card type?** Together AI only accepts credit or debit cards linked to a bank account. Prepaid cards are not supported and will be declined. Virtual cards are also often blocked by issuing banks for certain types of transactions.
* **Does your card support recurring payments?** Together AI requires payment cards that support recurring payments. Some prepaid cards or cards from certain banks may not support this feature, which can cause payment declines even with valid card information.
* **Are you seeing a \$0 authorization hold from your bank?** This is a normal verification process to confirm your card is active before charging the actual amount. You need to approve this authorization hold in your banking app or with your bank for the real payment to go through.
* **Are you waiting long enough for processing?** Credit purchases can take up to 15 minutes to complete. Avoid re-entering your card details during this processing period, as this may cause multiple credit purchases.
* Is your card frozen/blocked by your bank?
* Does your card have any spending limits that you might have reached?
* Is your bank sending you an additional security prompt that you need to complete?

If you see the error message "We only accept credit or debit cards," this indicates you're trying to use an unsupported payment method. Make sure you're using a regular credit or debit card linked to a bank account, not a prepaid card, virtual card, or alternative payment method.

### ACH bank transfer declines

If you're paying with a linked US bank account, also check:

* Does the linked account have enough available balance to cover the purchase?
* Is the bank account authorized for ACH debits?
* Did instant bank verification succeed when you linked the account?
* Did your bank block or return the debit after the purchase was submitted?

If an ACH payment fails, no credits are deposited. Contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) if you need help with a failed ACH payment.

## Understanding pending payments

There are a number of stages to every payment made on the Together AI platform.

First, Together AI's payment processor contacts your bank or card issuer to approve the payment.

Once the payment has gone through, an invoice is generated, which you can access from [your billing settings](https://api.together.ai/settings/organization/~current/billing).

The payment systems then need to update your account balance to reflect the purchase.

Once all of this has happened, your balance updates.

### Card payments

For credit and debit card purchases, this usually completes within 60 seconds of you confirming the payment, often instantly. Sometimes there can be a delay in the process, either on Together AI's side or due to your bank taking longer than expected to confirm the payment.

### ACH bank transfers

For ACH purchases, credits are deposited **only after the payment clears**. This usually takes **1–3 business days**, but can take longer depending on your bank.

While the payment is pending, your credit balance does not increase. You will see a pending banner on your [billing settings](https://api.together.ai/settings/organization/~current/billing) page.

If the ACH payment ultimately fails, no credits are deposited. See [Payment methods & invoices](/docs/billing-payment-methods#ach-bank-transfers) for details.

### What to do while a payment is pending

If this happens, you will see a pending banner on your [billing settings](https://api.together.ai/settings/organization/~current/billing) page to let you know that the transaction has been received but is still in progress.

If this is the case, don't make any further payments. Each further payment will be treated as an individual transaction, so you could end up buying more credit packs than you intended.

## Unexpected auto-recharge charges

If you were charged right after configuring auto-recharge, check your threshold. Setting the threshold above your current balance triggers an immediate purchase to bring your balance up to your target. Auto-recharge always charges in a single transaction, so if you see repeated charges, check whether multiple manual purchases were submitted while a payment was still pending. See [Auto-recharge credits](/docs/billing-credits#auto-recharge-credits) for how the amounts are calculated.

## Understanding unexpected charges

If you're seeing charges on your account without making API calls, you may be incurring costs from deployed resources that continue to run even when not actively used.

### Common causes of unexpected charges

1. **Fine-tuned Model Hosting**: Deployed fine-tuned models incur per-minute hosting fees regardless of API usage. These charges continue until you stop the endpoint.

2. **Dedicated model inference**: This is charged based on hardware allocation, even without active requests. Charges accrue as long as the endpoint remains active.

3. **Serverless Model Usage**: Charged based on actual token usage and model size - you only pay for what you use.

### Managing your deployments

To avoid unexpected charges:

1. Visit your [models dashboard](https://api.together.ai/models)
2. Check for deployed fine-tuned models or active dedicated endpoints
3. Stop any unused endpoints

Monitor usage and pricing at [together.ai/pricing](https://www.together.ai/pricing). Deployment charges are separate from usage charges and credit purchases.
