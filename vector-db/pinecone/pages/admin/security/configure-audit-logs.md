---
title: "Configure audit logs"
source: https://docs.pinecone.io/admin/security/configure-audit-logs
path: admin/security/configure-audit-logs
---

Enable Pinecone audit logging to an Amazon S3 bucket to track user, service account, and API actions for compliance, security review, and WORM retention.

Audit logs provide a detailed record of user, service account, and API actions that occur on the management and [control plane](/guides/core-concepts/architecture#control-plane) within Pinecone. Pinecone supports Amazon S3 as a destination for audit logs.

<Note>
  To enable and manage audit logs, you must be an [organization owner](/admin/organizations/understanding-organizations#organization-roles). This feature is available only on [Enterprise plans](https://www.pinecone.io/pricing/) or with the [HIPAA compliance add-on](/guides/manage-cost/understanding-cost#hipaa-compliance-add-on).
</Note>

## Enable audit logs

1. Set up an [IAM policy and role in Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3).
2. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging) in the Pinecone console.
3. Enter the **Role ARN** of the IAM role you created.
4. Enter the name of the Amazon S3 bucket you created.
   <Note>
     To write audit logs to a specific subdirectory, enter `bucket-name/subdirectory-path` in the bucket name field, for example, `my-bucket/pinecone-logs`. Make sure your [IAM policy is configured for subdirectory access](/guides/operations/integrations/integrate-with-amazon-s3#targeting-a-subdirectory-optional).
   </Note>
5. Click **Enable audit logging**.

Once you enable audit logs, Pinecone starts writing logs to the S3 bucket. In your bucket, you'll also see a file named `audit-log-access-test`, a test file that Pinecone writes to verify that it has the necessary permissions to write logs to the bucket.

## Make your audit-log bucket immutable (recommended)

Audit logs are written to an Amazon S3 bucket you control, so you can enforce write-once-read-many (WORM) immutability. Log files then can't be modified or deleted, even by your own administrators, for a retention period you define. We recommend this for compliance use cases.

Enable [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in compliance mode with a retention period. Object Lock requires bucket versioning and, in general, must be enabled when the bucket is created. Plan for it when you set up the [IAM policy and S3 bucket](/guides/operations/integrations/integrate-with-amazon-s3) above. Set the retention period to at least your required audit-log retention. Pinecone writes each log batch as a new, uniquely named file and doesn't modify or delete previously written logs.

<Warning>
  Compliance mode is intentionally irreversible: until a retention period expires, objects cannot be deleted and the period cannot be shortened, not even by the root account. Logs already written to the bucket are therefore retained for the full period even if you later disable or remove the audit log integration.
</Warning>

## View audit logs

Logs are written to the S3 bucket every 30 minutes. Each log batch is saved to its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled are saved.

For more information about the log schema and captured events, see [Audit logs](/admin/security/security-overview#audit-logs) in the security overview.

## Edit audit log integration details

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Enter the new **Role ARN** or **Bucket name**.
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
