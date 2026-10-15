---
title: "Redeem a promo code"
source: https://docs.pinecone.io/admin/billing/redeem-a-promo-code
path: admin/billing/redeem-a-promo-code
---

Learn how to redeem a Pinecone promo code when you upgrade to the Builder plan, and how to fix common redemption errors.

Pinecone promo codes, also called discount codes, discount the Builder plan. You enter a code while upgrading an organization from Starter to Builder, and you can't add one after the organization is on a paid plan.

## Before you start

Each code works for one email address and one plan, and only until its redemption date.

* Sign in with the email address the code was sent to. The code doesn't work for anyone else, even a teammate in the same organization.
* Select the organization you want to discount. The code applies to whichever organization is selected when you upgrade. To switch, click the organization name at the top left of the console.
* Make sure that organization is on the Starter plan and isn't in an active [Standard trial](/admin/billing/standard-trial).
* Make sure you're an organization owner or billing admin. Other [organization roles](/admin/organizations/understanding-organizations#organization-roles) can't change the plan.
* Make sure the code hasn't expired. Codes look like `BUILDER-20261231-0A1B2C3D4E5F`, where the 8-digit date is the last day you can redeem it, in UTC.

## Redeem a code

1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. In the **Builder** plan section, click **Upgrade**.
3. In the **Continue on Builder** dialog, click **Add discount code**.
4. Paste your code and click **Add code**. Letter case and extra spaces don't matter.
5. Click **Continue**.
6. Enter your credit or debit card information and click **Upgrade**.

The dialog shows **Discount code applied** for any code you add, valid or not. Pinecone checks the code when you click **Upgrade**, and if the code is rejected, the upgrade doesn't go through and you aren't charged.

## After you redeem a code

When the upgrade succeeds, the console confirms that your discount code has been applied. The cost table in the upgrade dialog still shows the full \$20/month, because the discount is applied to your [invoices](/admin/billing/access-your-invoices).

While the discount is active, the plan card on [**Settings > Billing > Overview**](https://app.pinecone.io/organizations/-/settings/billing) shows the date it ends. Pinecone emails you 5 days before that date and again when the discount ends. After that, Builder is billed at the regular price.

The discount only applies to the Builder plan. If you move the organization to another plan, the discount ends. If the upgrade dialog offers a Builder launch promotion, your code replaces it.

## Troubleshoot redemption errors

| Message or symptom | Cause | Fix |
| - | - | - |
| "Failed to upgrade. Discount code is not valid for this account." | The code has a typo, is for a plan other than Builder, or was sent to a different email address than the one you're signed in with. | Paste the code exactly as you received it, and check that it starts with `BUILDER-`. Sign in with the email address the code was sent to. |
| "Failed to upgrade. Discount code has expired." | The redemption date in the code has passed. | [Contact support](/admin/support/contact-support) if you think the code should still be valid. |
| "Failed to upgrade. A subscription already exists for this organization." | The selected organization is already on a paid plan. | Select an organization on the Starter plan. To discount an existing subscription, [contact support](/admin/support/contact-support). |
| The Add discount code link is missing | The organization isn't on Starter or is in an active Standard trial, or you clicked **Upgrade** on a plan other than Builder. | Check which organization is selected and its current plan, and then click **Upgrade** in the **Builder** plan section. |
| The Upgrade button is disabled | You aren't an owner or billing admin, or the organization is billed through a cloud marketplace. | Ask an organization owner to upgrade or to give you the billing admin role. If the organization is billed through a cloud marketplace, [contact support](/admin/support/contact-support). |

## Contact support

[Contact support](/admin/support/contact-support) if you upgraded without entering your code, applied it to the wrong organization, or your code was sent to an email address you don't use to sign in. Include the code, the organization name, and the email address you sign in with.
