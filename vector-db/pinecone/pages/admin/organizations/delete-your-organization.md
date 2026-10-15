---
title: "Delete your organization"
source: https://docs.pinecone.io/admin/organizations/delete-your-organization
path: admin/organizations/delete-your-organization
---

Permanently delete a Pinecone organization after you delete its indexes, collections, and projects and downgrade to the Starter plan.

Before you can delete your Pinecone organization, you need to delete all of its projects and downgrade to the Starter plan. To delete a project, first delete its indexes and collections.

* [Delete an index](/guides/manage-data/manage-indexes#delete-an-index)
* [Delete a project](/admin/projects/manage-projects#delete-a-project)
* [Downgrade to the Starter plan](/admin/billing/downgrade-billing-plan)

Once you've downgraded to the Starter plan and deleted your indexes and projects, you can delete your organization.

<Warning>This action cannot be undone.</Warning>

1. In the Pinecone console, go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage).
2. Click **Delete this organization**.
3. Type the organization name and confirm the deletion.
