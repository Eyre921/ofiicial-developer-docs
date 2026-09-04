---
title: "Configure audit logs"
source: https://docs.pinecone.io/guides/production/configure-audit-logs
path: guides/production/configure-audit-logs
---

Enable Pinecone audit logging to an Amazon S3 bucket to track user, service account, and API actions for compliance, security review, and WORM retention.

This page describes how to configure audit logs in Pinecone. Audit logs provide a detailed record of user, service account, and API actions that occur on the management and [control plane](/guides/core-concepts/architecture#control-plane) within Pinecone. Pinecone supports Amazon S3 as a destination for audit logs.

<Note>
  To enable and manage audit logs, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-roles). This feature is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Enable audit logs

1. Set up a [IAM policy and role in Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3).
2. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging) in the Pinecone console.
3. Enter the **Role ARN** of the IAM role you created.
4. Enter the name of the Amazon S3 bucket you created.
   <Note>
     **Targeting a subdirectory:** You can write audit logs to a specific subdirectory by entering `bucket-name/subdirectory-path` in the bucket name field. For example: `my-bucket/pinecone-logs`. Make sure your [IAM policy is configured for subdirectory access](/guides/operations/integrations/integrate-with-amazon-s3#targeting-a-subdirectory-optional).
   </Note>
5. Click **Enable audit logging**.

Once you enable audit logs, Pinecone will start writing logs to the S3 bucket. In your bucket, you will also see a file named `audit-log-access-test`, which is a test file that Pinecone writes to verify that it has the necessary permissions to write logs to the bucket.

## Make your audit-log bucket immutable (recommended)

Because audit logs are written to an Amazon S3 bucket you control, you can enforce write-once-read-many (WORM) immutability so that log files cannot be modified or deleted — including by your own administrators — for a retention period you define. This is recommended for compliance use cases.

Enable [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in **compliance mode** with a retention period. Object Lock requires bucket versioning and, in general, must be enabled when the bucket is created — plan for it when you set up the [IAM policy and S3 bucket](/guides/operations/integrations/integrate-with-amazon-s3) above. Set the retention period to at least your required audit-log retention. Pinecone writes each log batch as a new, uniquely named file and does not modify or delete previously written logs.

<Warning>
  Compliance mode is intentionally irreversible: until a retention period expires, objects cannot be deleted and the period cannot be shortened — not even by the root account. Logs already written to the bucket are therefore retained for the full period even if you later disable or remove the audit log integration.
</Warning>

## View audit logs

Logs are written to the S3 bucket approximately every 30 minutes. Each log batch will be saved into its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled will be saved.

For more information about the log schema and captured events, see [Understanding security - Audit logs](/guides/production/security-overview#audit-logs).

## Edit audit log integration details

You can edit the details of the audit log integration in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Enter the new **Role ARN** or **AWS Bucket**.
3. Click **Update settings**.

## Disable audit logs

If you disable audit logs, logs not yet saved will be lost. You can disable audit logs in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Click the toggle next to **Audit logs are active**.
3. Click **Confirm**.

## Remove audit log integration

If you remove the audit log integration, logs not yet saved will be lost. You can remove the audit log integration in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. At the top of the page, click the **ellipsis (...) menu > Remove integration**.
3. Click **Remove integration**.
