---
title: "Bring Your Own Bucket (BYOB)"
source: https://docs.fireworks.ai/guides/security_compliance/secure_training/byob
path: guides/security_compliance/secure_training/byob
---

Keep training datasets in your own cloud storage; Fireworks reads them in place and never persists a copy

Bring Your Own Bucket (BYOB) is the recommended configuration for Managed Training under strict data-governance requirements. Your dataset stays in your own cloud storage: Fireworks reads it in-place during active training only, with no copy persisted on Fireworks-managed storage, and you retain full ownership and deletion authority. This applies to both Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT) jobs.

BYOB works with all three major cloud providers — bring a bucket from whichever you already use:

* [Google Cloud Storage (GCS)](#gcs-bucket-integration)
* [AWS S3](#aws-s3-bucket-integration)
* [Azure Blob Storage](#azure-blob-storage-integration)

<Tip>
  Grant least-privilege IAM to only the bucket/path prefixes needed for training. Use server-side encryption and your KMS policies where required.
</Tip>

## GCS Bucket Integration

Use external Google Cloud Storage (GCS) buckets for fine-tuning while keeping your data private. Fireworks creates proxy datasets that reference your external buckets—data is only accessed during fine-tuning within a secure, isolated cluster.

<Info>
  Your data never leaves your GCS bucket except during fine-tuning, ensuring maximum privacy and security.
</Info>

### Required Permissions

You need to grant access to three service accounts. Fireworks provides the control plane and inference service account emails during BYOB onboarding.

**Fireworks Control Plane**

* **Account**: Fireworks control plane service account (provided at onboarding)
* **Required role**: Custom role with `storage.buckets.getIamPolicy` permission

```bash theme={null}
gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
  --member=serviceAccount:<FIREWORKS_CONTROL_PLANE_SA> \
  --role=projects/<YOUR_PROJECT>/roles/<YOUR_CUSTOM_ROLE>
```

**Inference Service Account**

* **Account**: Fireworks inference service account (provided at onboarding)
* **Required role**: Storage Object Viewer (`roles/storage.objectViewer`)

```bash theme={null}
gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
  --member=serviceAccount:<FIREWORKS_INFERENCE_SA> \
  --role=roles/storage.objectViewer
```

**Your Company's Fireworks Service Account**

* **Account**: Your company's Fireworks account email (get it with `firectl account get`)
* **Required role**: Storage Object Viewer (`roles/storage.objectViewer`)

```bash theme={null}
gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
  --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
  --role=roles/storage.objectViewer
```

<Tip>
  After the job completes, revoke or rotate these IAM bindings to remove Fireworks' access to your bucket.
</Tip>

<Note>
  GCS access is granted directly to the Fireworks service account emails above rather than through token federation, so there is no token audience to scope to your account the way the [S3](#aws-s3-bucket-integration) trust policy does. Fireworks instead verifies at dataset creation that the bucket grants access to your own Fireworks account, which is what keeps another customer from referencing your bucket.
</Note>

### Usage

```bash theme={null}
# Create dataset referencing your GCS bucket
firectl dataset create {DATASET_NAME} --external-url gs://bucket-name/path/to/data.jsonl

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME}
```

## AWS S3 Bucket Integration

Use external AWS S3 buckets for fine-tuning while keeping your data private. Fireworks accesses your S3 data using GCP-to-AWS OIDC federation—no long-lived credentials are stored.

<Note>
  S3 bucket integration is currently supported for **training datasets only** (SFT and RFT jobs). Evaluation datasets are not yet supported.
</Note>

### IAM Role Setup

Create an IAM role that Fireworks can assume via web identity federation. You do **not** need to register an OIDC identity provider — `accounts.google.com` is a built-in federated principal in AWS STS.

Trust policy on the role, locked to the Fireworks identity and scoped to your account:

```json theme={null}
{
  "Effect": "Allow",
  "Principal": { "Federated": "accounts.google.com" },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "accounts.google.com:sub": "<FIREWORKS_GCP_SERVICE_ACCOUNT_UNIQUE_ID>",
      "accounts.google.com:oaud": "<YOUR_FIREWORKS_ACCOUNT_ID>"
    }
  }
}
```

This is the standard trust model described in [How Fireworks accesses your cloud](/guides/security_compliance/secure_training#how-fireworks-accesses-your-cloud): `sub` locks assumption to the Fireworks identity, `oaud` pins the token's audience to your Fireworks account so a token issued for any other account is rejected by your own IAM. Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) for the BYOB subject identifier; the audience is your own Fireworks account ID.

Then attach a policy granting `s3:GetObject` and `s3:ListBucket` on your bucket.

See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html) for detailed steps on creating roles for OIDC federation.

### Usage

```bash theme={null}
# Create dataset referencing your S3 bucket
firectl dataset create {DATASET_NAME} --external-url s3://bucket-name/path/to/data.jsonl

# Use in fine-tuning job with IAM role
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --aws-iam-role "arn:aws:iam::{AWS_ACCOUNT_ID}:role/{ROLE_NAME}"
```

<Check>
  For RFT jobs, use `firectl rftj create` with the same `--aws-iam-role` flag.
</Check>

### Alternative: Credentials Secret

Instead of IAM role federation, you can use static AWS access keys stored in a Fireworks secret:

```bash theme={null}
# Create secret
firectl secret create --name aws-creds \
  --aws-access-key-id "AKIA..." \
  --aws-secret-access-key "..."

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --aws-credentials-secret "accounts/{ACCOUNT}/secrets/aws-creds"
```

<Warning>
  IAM role federation is recommended for production. If using credentials, rotate them regularly.
</Warning>

## Azure Blob Storage Integration

Use external Azure Blob Storage containers for fine-tuning while keeping your data private. Fireworks accesses your Azure data using GCP-to-Azure Workload Identity Federation—no long-lived credentials are stored.

<Note>
  Azure Blob Storage integration is currently supported for **training datasets only** (SFT and RFT jobs). Evaluation datasets are not yet supported.
</Note>

### Federated Identity Setup

Create an App Registration (or user-assigned Managed Identity) in your Azure AD tenant with a federated credential that trusts the Fireworks GCP service account. Fireworks provides the subject identifier during BYOB onboarding.

* **Issuer:** `https://accounts.google.com`
* **Subject identifier:** `<FIREWORKS_GCP_SERVICE_ACCOUNT_UNIQUE_ID>`
* **Audience:** `api://AzureADTokenExchange`

Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) if you need the exact subject identifier.

Then assign the **Storage Blob Data Reader** role on your storage account or container to the app registration.

See the [Azure documentation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust) for detailed steps on configuring workload identity federation.

### Usage

```bash theme={null}
# Create dataset referencing your Azure Blob container
firectl dataset create {DATASET_NAME} \
  --external-url https://{STORAGE_ACCOUNT}.blob.core.windows.net/{CONTAINER}/path/to/data.jsonl

# Use in fine-tuning job with managed identity federation
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --azure-managed-identity-client-id "{MANAGED_IDENTITY_CLIENT_ID}" \
  --azure-tenant-id "{AZURE_TENANT_ID}"
```

<Check>
  For RFT jobs, use `firectl rftj create` with the same `--azure-managed-identity-client-id` and `--azure-tenant-id` flags.
</Check>

### Alternative: Credentials Secret

Instead of workload identity federation, you can store Azure credentials in a Fireworks secret. The secret value must be a JSON object containing one of: `connection_string`, `sas_token`, or `account_key`.

```bash theme={null}
# Create secret with Azure credentials
firectl secret create --name azure-creds \
  --value '{"sas_token": "sv=2023-01-03&ss=b&srt=o&sp=rl&se=..."}'

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --azure-credentials-secret "accounts/{ACCOUNT}/secrets/azure-creds"
```

<Warning>
  Workload Identity Federation is recommended for production. If using credentials, rotate them regularly.
</Warning>
