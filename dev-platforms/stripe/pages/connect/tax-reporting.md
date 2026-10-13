---
title: "US tax reporting for Connect platforms"
source: https://docs.stripe.com/connect/tax-reporting.md
path: connect/tax-reporting
---

# US tax reporting for Connect platforms

Learn how to report the annual payments for your US-based connected accounts.

Stripe [Connect](https://stripe.com/connect) allows platforms to provide a seamless, end-to-end payment service for their connected accounts. This service might come with certain responsibilities, including tax information reporting.

> #### Getting your 1099 Forms
> 
> If you work for a platform that pays you through Stripe and want to learn about your 1099 forms and how to get them, see [1099 tax forms](https://support.stripe.com/express/topics/1099-tax-forms) on the Stripe Support site.

Stripe issues 1099-K forms for connected accounts where Stripe controls the pricing or for transactions where the connected account pays fees directly to Stripe. For all other transactions where the platform controls the pricing, the platform is responsible for filing any relevant 1099 forms.

In other words, Stripe issues 1099-K forms for your connected accounts that have transactions where [controller.fees.payer](https://docs.stripe.com/api/accounts/object.md#account_object-controller-fees-payer) equals `account` or where [controller.fees.payer](https://docs.stripe.com/api/accounts/object.md#account_object-controller-fees-payer) equals `application_unified_accounts_beta` and the connected account pays the processing fees.

Stripe doesn’t issue a 1099-K to your connected account in the following scenarios:

- Where [controller.fees.payer](https://docs.stripe.com/api/accounts/object.md#account_object-controller-fees-payer) equals `application` or `application_express` or `application_custom`

Consider issuing a Form 1099 to report income and payment transactions. There are several types of 1099 forms, and the applicable form depends on the type of payments you make to your connected account.

> Stripe recommends that you consult a tax advisor to determine your tax filing and reporting requirements.

## 1099-NEC

Use the [1099-NEC](https://support.stripe.com/questions/intro-to-1099-nec-tax-forms-for-platforms-and-marketplaces) form to report non-employee compensation.

The account must meet all of the following criteria in the previous calendar year:

- Based in the US or a US taxpayer
- $2,000 or more in payments

## 1099-MISC

Use the [1099-MISC](https://support.stripe.com/questions/intro-to-1099-misc-tax-forms-for-platforms-and-marketplaces) form to report other forms of payments made in the course of your business.

The account must meet all of the following criteria in the previous calendar year:

- Based in the US or a US taxpayer
- $2,000 or more in payments or $10 in royalties

## 1099-K

Use the [1099-K](https://support.stripe.com/questions/intro-to-1099-k-tax-forms-for-platforms-and-marketplaces) form to report payment transactions.

The account must meet all of the following criteria in the previous calendar year:

- Based in the US or a US taxpayer
- More than $20,000 in gross volume
- More than 200 transactions

## Connected accounts that share a legal entity 

Stripe [groups connected accounts with the same tax identity](https://docs.stripe.com/connect/file-tax-forms.md#below-threshold-forms) to determine whether they meet filing thresholds. Stripe still creates a separate tax form for each connected account. It doesn’t automatically consolidate their totals onto one form.

If you need one form for a legal entity instead of separate forms for its connected accounts, consolidate the totals before filing:

1. On the [Tax reporting](https://dashboard.stripe.com/connect/taxes/forms) page, use the **Forms grouped with** filter to find the accounts in the group. If the grouping is unexpected, [review the accounts’ identity information](https://docs.stripe.com/connect/identify-forms-missing-information.md).
2. [Export the forms as CSV](https://docs.stripe.com/connect/modify-tax-forms.md?method=csv#export-tax-forms) and save the original totals. Choose a primary connected account for each form type and tax year.
3. If any forms have existing Delta adjustments, import `0` for each adjusted field using a [Delta import](https://docs.stripe.com/connect/modify-tax-forms.md?method=csv#adding-to-existing-values-with-delta). Wait for the import to finish. Update imports replace base totals but retain Delta adjustments.
4. Using the saved original totals, add the amounts across the accounts for each reporting box. Prepare an Update CSV without any `*_delta` columns, keeping the original export separately for your calculations. Use a [CSV Update import](https://docs.stripe.com/connect/modify-tax-forms.md?method=csv#overwriting-existing-values-with-update) to set the primary account’s amount to that combined total and the corresponding amounts on the other accounts to `0`. Handle withholding and state reporting amounts according to your filing obligations. For 1099-K forms, also sum `number_of_payment_transactions` from the saved export. Import the combined count on the primary form and `0` on the other forms.
5. After processing finishes, confirm that the primary form contains the combined totals and the other forms contain the intended zero totals. Check that the other forms show **Will not file** before you file the primary form.

Zero payment totals don’t remove every filing obligation. Withholding, state requirements, or a [filing requirement override](https://docs.stripe.com/connect/modify-tax-forms.md?method=csv#tax-form-status) can still require a form to be filed. Review these conditions with your tax advisor before excluding a form.

## See also

- [Get started with the Stripe 1099 tax reporting product](https://docs.stripe.com/connect/get-started-tax-reporting.md)
- [Configure your tax form settings](https://docs.stripe.com/connect/tax-form-settings.md)

> Looking for help calculating sales tax, VAT, or GST? Check out [Stripe Tax](https://docs.stripe.com/tax.md).

