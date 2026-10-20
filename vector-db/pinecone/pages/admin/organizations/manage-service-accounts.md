---
title: "Manage organization service accounts"
source: https://docs.pinecone.io/admin/organizations/manage-service-accounts
path: admin/organizations/manage-service-accounts
---

Create and manage service accounts at the organization level in Pinecone for programmatic Admin API access, including client secrets and role assignment.

> [!NOTE]
>
> This feature is available on the [Enterprise plan](https://www.pinecone.io/pricing/).

This page shows how [organization owners](/admin/organizations/understanding-organizations#organization-roles) can add and manage service accounts at the organization level. Service accounts enable programmatic access to Pinecone's Admin API, which you can use to create and manage projects and API keys.

> [!TIP]
>
> Once you add a service account at the organization level, you can add it to a project. For more information, see [Manage service accounts at the project level](/admin/projects/manage-service-accounts).

## Create a service account

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).

2. Enter a **Name** for the service account.

3. Choose an [**Organization role**](/admin/organizations/understanding-organizations#organization-roles) for the service account. The role determines the service account's permissions within Pinecone.

4. Click **Create**.

5. Copy and save the **Client secret** in a secure place for future use. You'll need the client secret to retrieve an access token.

   > [!WARNING]
   >
   > You cannot view the client secret again after you close the dialog.

6. Click **Copy and Continue**.

Once you've created a service account, [add it to a project](/admin/projects/manage-service-accounts#add-a-service-account-to-a-project) to give it access to the project's resources.

## Retrieve an access token

To access the Admin API, you must authenticate with an access token. To get one, use the client secret you received when you [created the service account](#create-a-service-account).

This example requests an access token for a service account from the `https://login.pinecone.io/oauth/token` endpoint:

```bash curl theme={null}
curl "https://login.pinecone.io/oauth/token" \
	-H "X-Pinecone-Api-Version: 2026-07" \
	-H "Content-Type: application/json" \
	-d '{
		"grant_type": "client_credentials",
		"client_id": "YOUR_CLIENT_ID",
		"client_secret": "YOUR_CLIENT_SECRET",
		"audience": "https://api.pinecone.io/"
	}'
```

The response includes an `access_token` field, which you can use to authenticate with the Admin API.

```
{
    "access_token":"YOUR_ACCESS_TOKEN",
    "expires_in":86400,
    "token_type":"Bearer"
}
```

## Change a service account's role

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Edit role**.
3. Select an [**Organization role**](/admin/organizations/understanding-organizations#organization-roles) for the service account.
4. Click **Save**.

## Update service account name

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Rename**.
3. Enter a new **Name**.
4. Click **Save**.

## Rotate a service account's secret

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).

2. In the row of the service account you want to update, click **ellipsis (...) menu > Rotate secret**.

3. **Enter the service account name** to confirm.

4. Click **Rotate secret**.

5. Copy and save the **Client secret** in a secure place for future use.

   > [!WARNING]
   >
   > You cannot view the client secret again after you close the dialog.

6. Click **Copy and Continue**.

## Delete a service account

Deleting a service account removes it from all projects and disrupts any applications that use it to access Pinecone.

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Delete**.
3. **Enter the service account name** to confirm.
4. Click **Delete service account**.
