---
title: "Set monthly spend alerts"
source: https://docs.pinecone.io/guides/manage-cost/set-spend-alerts
path: guides/manage-cost/set-spend-alerts
---

Set monthly spend alerts in Pinecone to email the recipients you choose when your organization's spending reaches a threshold you set.

You can set up email alerts that track your organization's monthly spending. An alert notifies the recipients you choose when spending reaches a threshold you set, and it resets at the start of each monthly billing cycle.

> [!NOTE]
>
> Spend alerts are available on the [Standard and Enterprise plans](https://www.pinecone.io/pricing/). They're not needed on the Starter or Builder plans, where usage is capped by plan quotas rather than billed per unit.

## Set a spend alert

1. Go to [Settings > Spend alerts](https://app.pinecone.io/organizations/-/settings/spend-alerts) in the Pinecone console.
2. Click **+ Add Alert**.
3. Enter the dollar amount for the spend alert.
4. Enter the email addresses to send the alert to. [Organization owners](/admin/organizations/understanding-organizations#organization-roles) are listed by default.
5. Click **Create**.

## Edit a spend alert

1. In the row of the spend alert you want to edit, click **ellipsis (...) menu > Edit**.
2. Change the dollar amount, the email addresses, or both.
3. Click **Update**.

## Auto-spend spike alert

To protect against unexpected cost increases, Pinecone sends an alert when spending exceeds double your previous month's invoice. You can't change that threshold or delete the alert, but you can change which email addresses receive it and turn its notifications on or off.

## See also

* [Understand Pinecone cost](/guides/manage-cost/understanding-cost)
* [Download a usage report](/admin/billing/download-usage-report)
