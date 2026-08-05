---
title: "Payment methods & invoices"
source: https://docs.together.ai/docs/billing-payment-methods
path: docs/billing-payment-methods
---

Managing payment cards, ACH transfers, viewing invoices, and updating billing details.

## Supported payment methods

Together AI supports two payment methods to fund your account:

* **Credit and debit cards**: accepted from all major networks (Visa, Mastercard, American Express). Available to all customers.
* **ACH bank transfers**: pay directly from a U.S. bank account. Available to customers with an enterprise contract only (early access).

***

## Credit and debit cards

Together AI accepts all major credit and debit cards on networks including Visa, Mastercard, and American Express. Prepaid cards are not supported.

<Note>
  In some territories, banks require authorization for every transaction. Together AI sends an authorization link to your account's registered email. Approve these promptly to avoid credit purchase failures.
</Note>

### Managing payment methods

You can save **multiple payment methods** on an organization, for example a US bank account (ACH) and one or more credit cards. Choose which method is **default**. Credit purchases and auto-recharge (if enabled) use the default.

1. Go to your [billing settings](https://api.together.ai/settings/organization/~current/billing)
2. In the **Payment method** panel, select **Manage payment methods**
3. Add a card or bank account, set a **default** method, or remove methods you no longer need

**Requirements:**

* You must always keep **at least one valid credit or debit card** on file (even if ACH is your default payment method).
* You cannot remove the default method until you set another method as default.
* You cannot set an expired card as default.

### Invoice address

Your **invoice address** is separate from the address collected when you add a payment method. It is used for invoices and tax.

1. Go to your [billing settings](https://api.together.ai/settings/organization/~current/billing)
2. In the **Invoice address** panel, select **Edit** (or **Add** if no address is on file)
3. Update the address and save

You can change your invoice address without updating your payment methods. The Tax ID field appears after you enter address information.

**Note:** If you need to add your organization name, add a different email address to receive invoices, or add a non-standard Tax ID format, contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) for assistance. These changes cannot be made through the billing settings interface.

***

## ACH bank transfers (early access)

<Note>
  ACH bank transfers are currently in early access and available to customers with an enterprise contract only. [Contact Support](https://portal.usepylon.com/together-ai/forms/support-request) to request access.
</Note>

ACH (Automated Clearing House) payments allow you to purchase Together AI credits directly from your U.S. bank account. It's a good fit if you're making large purchases or running into credit card limits. You can purchase up to \$100,000 per transaction.

### Adding a bank account

Together AI supports most U.S. financial institutions with instant verification. Once your account has been enabled for ACH as a payment method, you can link your bank by following these steps:

1. Go to your [Billing settings](https://api.together.ai/settings/organization/~current/billing)
2. In the **Payment method** panel, select **Manage payment methods** (or **Add payment method** if no method is on file)
3. Select **Add payment method**, then choose **US Bank Account**
4. Enter your email and full name
5. Search for or select your bank and follow the on-screen steps to authorize your account
6. Enter your billing address
7. Select **Save Payment Method**

<Note>
  Only U.S. financial institutions that support instant verification are available right now. Manual entry of routing and account numbers is not supported.
</Note>

### Purchasing credits

Once your bank account is linked, start a purchase from your [Billing settings](https://api.together.ai/settings/organization/~current/billing) the same way you would with a card:

1. Select **Add Credits** in the Credits Balance block
2. Enter an amount (up to \$100,000) and confirm

Credits are **not** deposited until the ACH payment clears. Settlement usually takes **1–3 business days**, but can take longer depending on your bank. Until then, the purchase shows as pending and your balance will not increase.

If the payment fails, no credits are deposited. Contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) if you need help with a failed transaction.

### Things to know

* **Default method controls charges.** Credit purchases use whichever payment method is marked default. You can keep both cards and a bank account on file and switch the default as needed.
* **Auto-recharge requires a card.** Auto-recharge only works when your default payment method is a credit or debit card. If you set a US bank account as default, auto-recharge is turned off automatically.
* **Keep at least one valid card on file.** Your organization must always have at least one valid credit or debit card saved, even when ACH is enabled or set as default.
* **Failed payments.** If an ACH payment fails, no credits are deposited. Contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) if you have questions about a failed transaction.

### Troubleshooting

**My bank isn't showing up in the list.**
Only U.S. banks that support instant verification are currently available. If your institution isn't listed, try searching by name or contact [Support](https://portal.usepylon.com/together-ai/forms/support-request).

**I got an error during bank selection.**
This can happen if your bank is temporarily unable to verify the account link. Contact [Support](https://portal.usepylon.com/together-ai/forms/support-request) for help investigating.

**I got an error after clicking Save.**
Try refreshing the page and attempting again. If the issue persists, reach out to [Support](https://portal.usepylon.com/together-ai/forms/support-request) with any error details.

***

## Viewing previous invoices

All of your previous invoices (and current usage) can be viewed and downloaded in your [billing settings](https://api.together.ai/settings/organization/~current/billing).

Scroll down to billing history.

Note that you may receive \$0 invoices even when using free or pre-purchased credits. These provide a record of your usage, including tokens used and models accessed. You can download the invoice PDF for details.

## Adding business details to invoices

You can add your business name or other details to your invoices. Unfortunately this can't be done through your billing settings at the moment, so reach out to Support and they'll get it sorted for you!
