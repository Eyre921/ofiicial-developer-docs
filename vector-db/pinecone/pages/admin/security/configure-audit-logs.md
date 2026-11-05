---
title: "Configure audit logs"
source: https://docs.pinecone.io/admin/security/configure-audit-logs
path: admin/security/configure-audit-logs
---

Enable Pinecone audit logging to an Amazon S3 or Google Cloud Storage bucket to track user, service account, and API actions for compliance and security review.

Audit logs provide a detailed record of user, service account, and API actions that occur on the management and [control plane](/guides/get-started/architecture#control-plane) within Pinecone. Pinecone supports Amazon S3 and Google Cloud Storage (GCS) as destinations for audit logs.

> [!NOTE]
>
> To enable and manage audit logs, you must be an [organization owner](/admin/organizations/organizations-overview#organization-roles). This feature is available only on [Enterprise plans](https://www.pinecone.io/pricing/) or with the [HIPAA compliance add-on](/guides/cost/understand-cost#hipaa-compliance-add-on).

## Enable audit logs

1. Give Pinecone write access to your bucket:
   * For Amazon S3, set up an [IAM policy and role](/guides/storage-integrations/integrate-with-amazon-s3).
   * For GCS, [create a service account and key](/guides/storage-integrations/integrate-with-google-cloud-storage#1-create-a-service-account-and-key), and [grant it access to the bucket](/guides/storage-integrations/integrate-with-google-cloud-storage#2-grant-access-to-the-bucket) with a role that can list, create, and delete objects.
2. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging) in the Pinecone console.
3. For **Destination**, select **Amazon S3** or **Google Cloud Storage**.
4. Enter the credentials for your bucket:
   * For Amazon S3, enter the **Role ARN** of the IAM role you created.
   * For GCS, paste the contents of your service account's JSON key file into **Service account key JSON**.
5. For **Bucket name**, enter the name of your bucket.
   > [!NOTE]
   >
   > To write audit logs to a specific subdirectory, enter `bucket-name/subdirectory-path` in the bucket name field, for example, `my-bucket/pinecone-logs`. For Amazon S3, make sure your [IAM policy is configured for subdirectory access](/guides/storage-integrations/integrate-with-amazon-s3#targeting-a-subdirectory-optional). For GCS, a role granted on the bucket already covers every subdirectory.
6. Click **Enable audit logs**.

Once you enable audit logs, Pinecone starts writing logs to your bucket. Pinecone also writes a test file named `audit-log-access-test` to verify that it can write logs to the bucket, and then tries to delete it. The file stays in your bucket if Pinecone can't delete objects, as with the Amazon S3 policy.

## Make your audit-log bucket immutable (recommended)

Audit logs are written to a bucket you control, so you can enforce write-once-read-many (WORM) immutability. Log files then can't be modified or deleted, even by your own administrators, for a retention period you define. We recommend this for compliance use cases. These steps cover Amazon S3 only.

For Amazon S3, enable [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in compliance mode with a retention period. Object Lock requires bucket versioning and, in general, must be enabled when the bucket is created. Plan for it when you set up the [IAM policy and S3 bucket](/guides/storage-integrations/integrate-with-amazon-s3) above. Set the retention period to at least your required audit-log retention. Pinecone writes each log batch as a new, uniquely named file and doesn't modify or delete previously written logs.

> [!WARNING]
>
> Compliance mode is intentionally irreversible: until a retention period expires, objects can't be deleted and the period can't be shortened, not even by the root account. Logs already written to the bucket are therefore retained for the full period even if you later disable or remove the audit log integration.

## View audit logs

Logs are written to your bucket every 30 minutes. Each log batch is saved to its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled are saved.

For more information about the log schema and captured events, see [Audit logs](/admin/security/security-overview#audit-logs) in the security overview.

## Edit audit log integration details

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Enter the new credentials or **Bucket name**. You can't change the destination of an existing integration.
   > [!NOTE]
   >
   > For GCS, Pinecone doesn't return your service account key after you save it, so paste the full key into **Service account key JSON** again whenever you update the integration.
3. Click **Update settings**.

## Disable audit logs

Disabling audit logs pauses delivery to your bucket. Your integration settings are kept, and if you enable audit logs again, Pinecone delivers the logs that weren't written to your bucket before you disabled them.

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Click the toggle next to **Audit logging is active**.
3. Click **Disable integration**.

## Remove audit log integration

If you remove the audit log integration, logs that haven't been written to your bucket yet aren't delivered, even if you set up a new integration later.

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. At the top of the page, click the **ellipsis (...) menu > Remove integration**.
3. Click **Remove integration**.
