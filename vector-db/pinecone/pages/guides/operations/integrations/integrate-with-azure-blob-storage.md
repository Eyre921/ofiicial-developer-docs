---
title: "Integrate with Azure Blob Storage"
source: https://docs.pinecone.io/guides/operations/integrations/integrate-with-azure-blob-storage
path: guides/operations/integrations/integrate-with-azure-blob-storage
---

Set up Azure Blob Storage integration for data import.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page describes how to integrate Pinecone with Azure Blob Storage. After setting up an integration, you can [import data](/guides/index-data/import-data) from an Azure Blob Storage container into a Pinecone index hosted on AWS, GCP, or Azure.

## Before you begin

Ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/)
* An [Azure Blob Storage container](https://learn.microsoft.com/azure/storage/blobs/storage-blobs-introduction)

## 1. Create an app registration and service principal

Pinecone uses a service principal to access your Azure Blob Storage container.

1. [Create an app registration](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app) for your Pinecone integration. This automatically creates a service principal.

   When creating your app registration:

   * Do not specify a **Redirect URI**.
   * Copy the **Application (client) ID** and the **Directory (tenant) ID**. You'll use these values when adding a storage integration in Pinecone.

2. [Create a client secret](https://learn.microsoft.com/entra/identity-platform/how-to-add-credentials?tabs=client-secret) for the service principal.

   Copy the secret's **Value** (not its **ID**). You'll use this when creating a storage integration in Pinecone.

## 2. Grant access to the storage account

[Assign the service principal to your storage account](https://learn.microsoft.com/azure/storage/common/storage-auth-aad-rbac-portal#assign-azure-rbac-roles-using-the-azure-portal):

1. In the Azure portal, navigate to the subscription associated with your storage account.
2. Select **Access control (IAM)**.
3. Click **Add** > **Add role assignment**.
4. Select **Storage Blob Data Reader** or another role that has permission to list and read blobs in a container.
5. Click **Next**.
6. Select **User, group, or service principal** and click **Select members**.
7. Select the app you created in the previous step.
8. Click **Review + assign** (you may need to click this twice).

## 3. In Pinecone, add a storage integration

In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), add an integration with Azure Blob Storage:

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. Click **Add integration**.
4. Enter a unique integration name.
5. Select **Azure Blob Storage**.
6. For **Tenant ID**, **Client ID**, and **Client secret**, enter the values you copied from Azure.
7. Click **Add integration**.

## Next steps

[Import data](/guides/index-data/import-data) from your Azure Blob Storage container into your Pinecone index.
