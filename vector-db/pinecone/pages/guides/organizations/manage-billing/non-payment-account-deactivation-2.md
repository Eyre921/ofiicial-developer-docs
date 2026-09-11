---
title: "Account deactivation for non-payment"
source: https://docs.pinecone.io/guides/organizations/manage-billing/non-payment-account-deactivation
path: guides/organizations/manage-billing/non-payment-account-deactivation
---

Learn what happens when a Pinecone account is deactivated for non-payment: 30-day data retention, permanent deletion, and how to reactivate.

If your organization has continued non-payment on a paid billing plan, Pinecone may deactivate your account. While your account is deactivated, you cannot use Pinecone services, but your data is retained for a limited time so you can reactivate and recover it.

## Data retention after deactivation

When your account is deactivated for non-payment:

* Your account data is retained for **30 days** from deactivation.
* After 30 days, all account data is **permanently deleted**. This action cannot be undone.

<Note>
  This 30-day retention period applies specifically to accounts deactivated for continued non-payment. Other deletion flows, such as when you [delete resources](/guides/production/data-deletion) or [end your relationship with Pinecone](/guides/production/data-deletion), follow different retention timelines described in the [data deletion policy](/guides/production/data-deletion).
</Note>

If you see a deactivation notice in the Pinecone console, it reflects this policy:

> Your account has been deactivated due to continued non-payment. Account data will be retained for 30 days. After 30 days, all data will be permanently deleted. This action cannot be undone.
>
> To reactivate your account and preserve your data, please visit the billing page and update your payment information. If you believe this is an error, please reach out to our support team.

## Reactivate your account

To reactivate your account and preserve your data before the 30-day retention period ends:

1. Sign in to the [Pinecone console](https://app.pinecone.io).
2. Go to [**Settings > Billing**](https://app.pinecone.io/organizations/-/settings/billing).
3. Update your payment information or resolve the outstanding balance.

Organization [owners and billing admins](/guides/organizations/understanding-organizations#organization-roles) can update billing details. For help changing how you pay, see [Change your payment method](/guides/organizations/manage-billing/change-payment-method).

## API access while deactivated

API requests may fail with a [**402 - Payment Required**](/reference/api/errors#402---payment-required) response while your account has a payment issue or is deactivated for non-payment. After you reactivate your account, retry your requests. For general error-handling guidance, see [Error handling](/guides/production/error-handling).

## Contact support

If you believe your account was deactivated in error, [contact Support](https://www.pinecone.io/contact/support/) or [open a support ticket](https://app.pinecone.io/organizations/-/settings/support/ticket) from the console.

## See also

* [Change your payment method](/guides/organizations/manage-billing/change-payment-method)
* [Data deletion on Pinecone](/guides/production/data-deletion)
* [Billing disputes and refunds](/troubleshooting/billing-disputes-and-refunds)
