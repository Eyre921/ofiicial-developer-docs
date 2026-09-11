---
title: "Integrate with Amazon S3"
source: https://docs.pinecone.io/guides/operations/integrations/integrate-with-amazon-s3
path: guides/operations/integrations/integrate-with-amazon-s3
---

Set up a Pinecone storage integration with an Amazon S3 bucket using an IAM role to bulk import data into indexes and export audit logs.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows you how to integrate Pinecone with an Amazon S3 bucket. Once your integration is set up, you can use it to [import data](/guides/index-data/import-data) from your Amazon S3 bucket into a Pinecone index hosted on AWS, or to [export audit logs](/guides/production/configure-audit-logs) to your Amazon S3 bucket.

## Before you begin

Ensure you have the following:

* A [Pinecone account](https://app.pinecone.io/).
* An [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets.html).

## 1. Create an IAM policy

In the [AWS IAM console](https://console.aws.amazon.com/iam/home):

1. In the navigation pane, click **Policies**.
2. Click **Create policy**.
3. In **Select a service** section, select **S3**.
4. Select the following actions to allow:
   * `ListBucket`: Permission to list some or all of the objects in an S3 bucket. Required for [importing data](/guides/index-data/import-data) and [exporting audit logs](/guides/production/configure-audit-logs).
   * `GetObject`: Permission to retrieve objects from an S3 bucket. Required for [importing data](/guides/index-data/import-data).
   * `PutObject`: Permission to add an object to an S3 bucket. Required for [exporting audit logs](/guides/production/configure-audit-logs).
5. In the **Resources** section, select **Specific**.
6. For the **bucket**, specify the ARN of the bucket you created. For example: `arn:aws:s3:::example-bucket-name`
7. For the **object**, specify an object ARN as the target resource. For example: `arn:aws:s3:::example-bucket-name/*`
8. Click **Next**.
9. Specify the name of your policy. For example:  "Pinecone-S3-Access".
10. Click **Create policy**.

### Targeting a subdirectory (optional)

To write [audit logs](/guides/production/configure-audit-logs) to a specific subdirectory within your S3 bucket (e.g., `my-bucket/pinecone-logs/`), you need to configure your IAM policy differently for `ListBucket` vs. object-level actions:

1. For `ListBucket`, use a **Condition** block with `StringLike` to specify the prefix. Include both the directory path with and without the trailing wildcard:

   ```json theme={null}
   {
       "Sid": "ListBucketWithPrefix",
       "Effect": "Allow",
       "Action": "s3:ListBucket",
       "Resource": "arn:aws:s3:::example-bucket-name",
       "Condition": {
           "StringLike": {
               "s3:prefix": [
                   "pinecone-logs/",
                   "pinecone-logs/*"
               ]
           }
       }
   }
   ```

2. For `PutObject` and `GetObject`, use the **Resource** specifier with the subdirectory path:

   ```json theme={null}
   {
       "Sid": "ObjectActionsInSubdirectory",
       "Effect": "Allow",
       "Action": [
           "s3:PutObject",
           "s3:GetObject"
       ],
       "Resource": "arn:aws:s3:::example-bucket-name/pinecone-logs/*"
   }
   ```

**Complete example policy for subdirectory access:**

```json theme={null}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListBucketWithPrefix",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example-bucket-name",
            "Condition": {
                "StringLike": {
                    "s3:prefix": [
                        "pinecone-logs/",
                        "pinecone-logs/*"
                    ]
                }
            }
        },
        {
            "Sid": "ObjectActionsInSubdirectory",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::example-bucket-name/pinecone-logs/*"
        }
    ]
}
```

<Note>
  The key difference is that `ListBucket` operates on the bucket resource and uses conditions to filter by prefix, while object-level actions (`PutObject`, `GetObject`) operate directly on object resources specified in the ARN.
</Note>

## 2. Set up access using an IAM role

In the [AWS IAM console](https://console.aws.amazon.com/iam/home):

1. In the navigation pane, click **Roles**.

2. Click **Create role**.

3. In the **Trusted entity type** section, select **AWS account**.

4. Select **Another AWS account**.

5. Enter the Pinecone AWS VPC account ID: `713131977538`

6. Click **Next**.

7. Select the [policy you created](#1-create-an-iam-policy).

8. Click **Next**.

9. Specify the role name. For example: "Pinecone".

10. Click **Create role**.

11. Click the role you created.

12. On the **Summary** page for the role, find the **ARN**.

    For example: `arn:aws:iam::123456789012:role/PineconeAccess`

13. Copy the **ARN**.

    You will need to enter the ARN into Pinecone later.

## 3. Add a storage integration

<Note>
  This step is required for [importing data](/guides/index-data/import-data). It is not required for [storing audit logs](/guides/production/configure-audit-logs).
</Note>

You can add a storage integration in the Pinecone console or with the API.

### Use the console

In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), add an integration with Amazon S3.

1. Select your project.
2. Go to [**Manage > Storage integrations**](https://app.pinecone.io/organizations/-/projects/-/storage).
3. Click **Add integration**.
4. Enter a unique integration name.
5. Select **Amazon S3**.
6. Enter the **ARN** of the [IAM role you created](/guides/operations/integrations/integrate-with-amazon-s3#2-set-up-access-using-an-iam-role).
7. Click **Add integration**.

### Use the API

<Note>
  This endpoint requires `X-Pinecone-Api-Version: unstable`. Unstable endpoints can change without notice.
</Note>

Pass the ARN of your IAM role as the `aws_iam_role.role_arn` field:

```bash curl theme={null}
curl -sS -X POST "https://api.pinecone.io/storage-integrations" \
    -H "Api-Key: ${PINECONE_API_KEY}" \
    -H "X-Pinecone-Api-Version: unstable" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "my-s3-integration",
      "provider": "s3",
      "aws_iam_role": {
        "role_arn": "arn:aws:iam::123456789012:role/pinecone-s3-access"
      }
    }'
```

Replace the `role_arn` value with the ARN of the [IAM role you created](#2-set-up-access-using-an-iam-role), and `my-s3-integration` with a unique name for the integration.

The response includes the integration's `id`, which you need to [import data](/guides/index-data/import-data), and a `status` of `Validated` or `Invalid`. If Pinecone can't assume the role, the request still succeeds and the integration is created with a `status` of `Invalid`, so check the status before you import.

## Next steps

* [Import data](/guides/index-data/import-data) from your Amazon S3 bucket into a Pinecone index.
* [Configure audit logs](/guides/production/configure-audit-logs) to export logs to your Amazon S3 bucket.
