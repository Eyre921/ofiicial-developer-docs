---
title: "Data deletion on Pinecone"
source: https://docs.pinecone.io/guides/production/data-deletion
path: guides/production/data-deletion
---

Learn how Pinecone permanently deletes customer data, including soft deletion, the 90-day retention window, and secure erasure of records and indexes.

Pinecone follows a secure process to ensure that customer data is permanently deleted from our system. This page gives an overview of the process.

As defined in the [Master Subscription Agreement](https://www.pinecone.io/legal/master-subscription-agreement/), customer data is data that you provide to Pinecone through the services of the Pinecone system, or such data provided on your behalf by connected systems. This includes objects such as [records](/guides/core-concepts/key-terms#record), [indexes](/guides/core-concepts/key-terms#index), [backups](/guides/core-concepts/key-terms#backup), [projects](/guides/core-concepts/key-terms#project), [API keys](/guides/core-concepts/key-terms#api-key), [users](/admin/organizations/manage-organization-members), [assistants](/guides/assistant/overview), and [organizations](/guides/core-concepts/key-terms#organization).

## Deletion request

The deletion of customer data begins when you initiate a deletion request through the Pinecone API, console, or a connected service. A deletion request can delete a single resource, such as a record, or can delete a resource and all its dependent resources, such as an index and all its records.

Deletion of your customer data also occurs automatically when you end your relationship with Pinecone. If your account is [deactivated for continued non-payment](/admin/billing/non-payment-account-deactivation), account data is retained for 30 days before permanent deletion.

## Soft deletion

After you initiate a deletion request, Pinecone marks the data for deletion. The data isn't immediately removed from the system. Instead, Pinecone retains the data for a maximum of 90 days. During this period, the data isn't accessible to you or any other user.

## Permanent deletion

Before the end of the 90-day retention window, Pinecone permanently deletes the data from its system. Once the data is permanently deleted, it's no longer recoverable.

> [!NOTE]
>
> Pinecone creates an [audit log](/admin/security/security-overview#audit-logs) of user, service account, and API events. Events are captured within two hours of occurrence and are retained for 90 days, after which they're permanently deleted.

## See also

* [Delete records](/guides/manage-data/delete-data)
* [Delete an index](/guides/manage-data/manage-indexes#delete-an-index)
* [Delete a project](/admin/projects/manage-projects#delete-a-project)
* [Delete an API key](/admin/projects/manage-api-keys#delete-an-api-key)
* [Delete a user](/admin/projects/manage-project-members#remove-a-member)
* [Delete an organization](/admin/organizations/delete-your-organization)
* [Master Subscription Agreement](https://www.pinecone.io/legal/master-subscription-agreement/)
