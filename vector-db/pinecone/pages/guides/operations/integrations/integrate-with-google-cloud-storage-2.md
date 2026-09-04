---
title: "Integrate with Google Cloud Storage"
source: https://docs.pinecone.io/guides/operations/integrations/integrate-with-google-cloud-storage
path: guides/operations/integrations/integrate-with-google-cloud-storage
---

Set up a Pinecone storage integration with a Google Cloud Storage bucket using a service account key to bulk import data into your indexes.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows you how to integrate Pinecone with a Google Cloud Storage (GCS) bucket. Once your integration is set up, you can use it to [import data](/guides/index-data/import-data) from your bucket into a Pinecone index hosted on AWS, GCP, or Azure.

## Before you begin

Ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/)
* A [Google Cloud Storage bucket](https://cloud.google.com/storage/docs/creating-buckets)

## 1. Create a service account and key

Pinecone will use a service account to access your GCS bucket.

1. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create) for your Pinecone integration.
2. [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating). Select **JSON** as the key type.

   The key will be downloaded to your computer. You'll use this key when adding a storage integration in Pinecone.

## 2. Grant access to the bucket

[Add your service account as a principal to the bucket](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

* For the principal, use your service account email address.
* For the role, select **Storage Object Viewer** or another role that has permission to list and read objects in a bucket.

## 3. Add a storage integration

You can add a storage integration in the Pinecone console or with the API.

### Use the console

In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), add an integration with Google Cloud Storage:

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. Click **Add integration**.
4. Enter a unique integration name.
5. Select **Google Cloud Storage**.
6. Open the JSON key file for your service account.
7. Copy the contents of the key file and paste them into the **Index account key JSON** field.
8. Click **Add integration**.

### Use the API

<Note>
  This endpoint requires `X-Pinecone-Api-Version: unstable`. Unstable endpoints can change without notice.
</Note>

Pass the contents of your service account key file as the `gcp_service_account.key_json` field. The following example uses [`jq`](https://jqlang.github.io/jq/) to safely JSON-encode the key file before sending it:

```bash curl theme={null}
jq -n --arg key "$(cat service-account-key.json)" \
    '{name: "my-gcs-integration", provider: "gcs", gcp_service_account: {key_json: $key}}' \
  | curl -sS -X POST "https://api.pinecone.io/storage-integrations" \
      -H "Api-Key: ${PINECONE_API_KEY}" \
      -H "X-Pinecone-Api-Version: unstable" \
      -H "Content-Type: application/json" \
      --data @-
```

Replace `service-account-key.json` with the path to the [JSON key file you created](#1-create-a-service-account-and-key), and `my-gcs-integration` with a unique name for the integration.

The response includes the integration's `id`, which you need to [import data](/guides/index-data/import-data), and a `status` of `Validated` or `Invalid`. If the service account key is invalid, the request still succeeds and the integration is created with a `status` of `Invalid`, so check the status before you import.

## Next steps

[Import data](/guides/index-data/import-data) from your GCS bucket into your Pinecone index.
