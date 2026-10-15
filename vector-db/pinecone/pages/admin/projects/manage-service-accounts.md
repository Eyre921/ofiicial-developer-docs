---
title: "Manage project service accounts"
source: https://docs.pinecone.io/admin/projects/manage-service-accounts
path: admin/projects/manage-service-accounts
---

Add service accounts to a Pinecone project and assign project roles to enable programmatic API access for automated workflows and CI pipelines.

<Note>
  This feature is available on the [Enterprise plan](https://www.pinecone.io/pricing/).
</Note>

This page shows how [organization owners](/admin/organizations/understanding-organizations#organization-roles) and [project owners](/admin/projects/understanding-projects#project-roles) can add and manage service accounts at the project level. Service accounts enable programmatic access to Pinecone's Admin API, which you can use to create and manage projects and API keys.

## Add a service account to a project

After a service account is [added to an organization](/admin/organizations/manage-service-accounts#create-a-service-account), you can add it to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to [**Settings > Access**](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts) and select the **Service accounts** tab.
3. Select the service account to add.
4. Select a [**Project role**](/admin/projects/understanding-projects#project-roles) for the service account. The role determines its permissions within Pinecone.
5. Click **Connect**.

## Change project role

To change a service account's role in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to [**Settings > Access**](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts) and select the **Service accounts** tab.
3. In the row of the service account you want to edit, click **ellipsis (...) menu > Edit role**.
4. Select a [**Project role**](/admin/projects/understanding-projects#project-roles) for the service account.
5. Click **Save**.

## Remove a service account from a project

To remove a service account from a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to [**Settings > Access**](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts) and select the **Service accounts** tab.
3. In the row of the service account you want to remove, click **ellipsis (...) menu > Remove from project**.
4. Click **Remove service account**.
