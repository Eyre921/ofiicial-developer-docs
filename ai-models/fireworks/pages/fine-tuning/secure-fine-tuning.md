---
title: "Secure Training Overview"
source: https://docs.fireworks.ai/fine-tuning/secure-fine-tuning
path: fine-tuning/secure-fine-tuning
---

Choose the right training surface for your data-privacy needs, and understand what Fireworks retains and how to delete it

Fireworks lets you fine-tune models while keeping your data and sensitive components under your control. Across every training surface, one principle holds: **your training data is never used to train Fireworks-owned or shared models**.

This page covers training. Inference follows [Zero Data Retention](/guides/security_compliance/data_handling) by default — prompts and generations are never written to persistent storage — so we focus here on the training lifecycle: where your data lives while you train, what Fireworks retains afterward (checkpoints and traces), and the controls you have to delete it.

Use it to:

* Understand how each training surface handles your data.
* Choose the surface that fits your data-privacy requirements.
* Know exactly what is retained, what is not, and how to delete it.

## Choosing a training surface

Fireworks offers three ways to train, differing mainly in **where your training data lives**:

| Surface                     | Where your training data lives                                                                                                             | What Fireworks retains           | Your deletion controls                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | --------------------------------------------------------------------------- |
| **Managed Training**        | Uploaded to Fireworks-managed storage (GCS); only a reference link is kept in our database                                                 | Dataset, checkpoints, and traces | Delete the dataset anytime after the job; request checkpoint/trace deletion |
| **Managed Training + BYOB** | Stays in your own cloud bucket; Fireworks reads it in-place during training, with no copy persisted                                        | Checkpoints and traces only      | Revoke bucket access after the job; request checkpoint/trace deletion       |
| **Training API**            | No dataset upload — you load and tokenize data locally; the trainer receives only transient tokenized batches, never a stored dataset file | Checkpoints and traces only      | Request checkpoint/trace deletion                                           |

<Tip>
  For the strictest data governance, use [BYOB](#dataset-storage-byob) (keep the dataset in your own bucket) or the [Training API](#training-api) (no dataset is ever uploaded to or stored on Fireworks).
</Tip>

## Data retention by surface

When training runs on Fireworks-managed storage, training data is stored in Google Cloud Storage (GCS) with only a reference link retained in our database. Customers control deletion of their own datasets.

### Managed Training

Retention behavior depends on the job type:

| Job Type               | Data Generated                                       | Retention / Deletion                                                                                                                                             |
| ---------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SFT — Managed Training | Uploaded dataset only                                | Customer-controlled; deletable immediately after the job completes                                                                                               |
| DPO — Managed Training | Uploaded dataset only                                | Customer-controlled; deletable immediately after the job completes                                                                                               |
| RFT — Managed Training | Input prompts + rollout datasets (generated outputs) | Input prompts: customer-controlled, deletable after the job completes (same policy as SFT and DPO). Rollout datasets (generated outputs): deletable upon request |
| Job chunks / artifacts | Intermediate checkpoints                             | Retained for 30 days, then deleted; deletable earlier on request. Kept so jobs can be retrieved or restarted                                                     |
| Traces / logs          | Request/response metadata                            | Retained for 30 days, then deleted; deletable earlier on request                                                                                                 |

### Training API

The [Training API](/fine-tuning/training-api/introduction) works differently: you write the training loop in your own environment, load and tokenize data locally, and send tokenized `Datum` batches to Fireworks GPUs on each `forward_backward` call. What this means for your data:

* **No dataset upload step and no dataset file stored on Fireworks' side.** Fireworks never receives your raw JSONL, and for RL or distillation the trainer never sees raw prompt text.
* **The trainer does receive the training content** — as tokenized `Datum` batches on every `forward_backward` call. Those tokens are your data; they are processed transiently for the gradient step and are not retained as a dataset.

What Fireworks does retain is minimal and deletable on request:

* **Checkpoints** — retained for 30 days (deletable earlier on request) so you can restart jobs without losing work.
* **Traces / logs** — retained for 30 days (deletable earlier on request) so you can evaluate job performance and improve your training.

This barebones retention is by design: it keeps the product easy to use — retrieve checkpoints to restart jobs, and inspect traces to understand and improve training — while your training data is never uploaded or stored as a dataset on Fireworks.

## Encryption at rest (CMEK)

If you use Managed Training but want to control encryption of the data Fireworks stores, Customer-Managed Encryption Keys (CMEK) let you bring an encryption key from your own cloud KMS. Fireworks uses your key to encrypt the artifacts your jobs read and write, and every use of the key is recorded in your own cloud's audit log. Because Fireworks can only decrypt your data while your KMS answers an unwrap request, you stay in control: disable or revoke the key and Fireworks can no longer read your datasets or checkpoints.

CMEK covers the durable artifacts a Managed Training job reads and writes:

* Training and evaluation datasets you upload
* Intermediate checkpoints and distributed-checkpoint shards

<Note>
  CMEK currently supports **AWS KMS** and **Supervised Fine-Tuning (SFT)**. Support for Azure Key Vault, Google Cloud KMS, DPO, and RFT is coming soon. CMEK protects data **at rest** — during an active job, training compute processes your data in plaintext in memory.
</Note>

CMEK and BYOB address different needs and can be used independently: [BYOB](#dataset-storage-byob) keeps your dataset in your own bucket with no copy persisted on Fireworks, while CMEK controls the encryption key for data that *is* stored on Fireworks-managed storage. For setup, key rotation, and revocation, see the [CMEK guide](/fine-tuning/cmek).

## Dataset Storage (BYOB)

Bring Your Own Bucket (BYOB) is the recommended configuration for Managed Training under strict data-governance requirements. Your dataset stays in your own cloud storage: Fireworks reads it in-place during active training only, with no copy persisted on Fireworks-managed storage, and you retain full ownership and deletion authority. This applies to both Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT) jobs.

BYOB works with all three major cloud providers — bring a bucket from whichever you already use:

* [Google Cloud Storage (GCS)](#gcs-bucket-integration)
* [AWS S3](#aws-s3-bucket-integration)
* [Azure Blob Storage](#azure-blob-storage-integration)

<Tip>
  Grant least-privilege IAM to only the bucket/path prefixes needed for training. Use server-side encryption and your KMS policies where required.
</Tip>

### GCS Bucket Integration

Use external Google Cloud Storage (GCS) buckets for fine-tuning while keeping your data private. Fireworks creates proxy datasets that reference your external buckets—data is only accessed during fine-tuning within a secure, isolated cluster.

<Info>
  Your data never leaves your GCS bucket except during fine-tuning, ensuring maximum privacy and security.
</Info>

#### Required Permissions

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

#### Usage

```bash theme={null}
# Create dataset referencing your GCS bucket
firectl dataset create {DATASET_NAME} --external-url gs://bucket-name/path/to/data.jsonl

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME}
```

### AWS S3 Bucket Integration

Use external AWS S3 buckets for fine-tuning while keeping your data private. Fireworks accesses your S3 data using GCP-to-AWS OIDC federation—no long-lived credentials are stored.

<Note>
  S3 bucket integration is currently supported for **training datasets only** (SFT and RFT jobs). Evaluation datasets are not yet supported.
</Note>

#### IAM Role Setup

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

The `sub` condition locks assumption to the Fireworks identity. The `oaud` condition pins the token's audience to your Fireworks account, so a token issued for any other Fireworks account is rejected by your own IAM.

Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) for the subject identifier; the audience is your own Fireworks account ID.

Then attach a policy granting `s3:GetObject` and `s3:ListBucket` on your bucket.

See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html) for detailed steps on creating roles for OIDC federation.

#### Usage

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

#### Alternative: Credentials Secret

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

### Azure Blob Storage Integration

Use external Azure Blob Storage containers for fine-tuning while keeping your data private. Fireworks accesses your Azure data using GCP-to-Azure Workload Identity Federation—no long-lived credentials are stored.

<Note>
  Azure Blob Storage integration is currently supported for **training datasets only** (SFT and RFT jobs). Evaluation datasets are not yet supported.
</Note>

#### Federated Identity Setup

Create an App Registration (or user-assigned Managed Identity) in your Azure AD tenant with a federated credential that trusts the Fireworks GCP service account. Fireworks provides the subject identifier during BYOB onboarding.

* **Issuer:** `https://accounts.google.com`
* **Subject identifier:** `<FIREWORKS_GCP_SERVICE_ACCOUNT_UNIQUE_ID>`
* **Audience:** `api://AzureADTokenExchange`

Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) if you need the exact subject identifier.

Then assign the **Storage Blob Data Reader** role on your storage account or container to the app registration.

See the [Azure documentation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust) for detailed steps on configuring workload identity federation.

#### Usage

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

#### Alternative: Credentials Secret

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

## Secure Reinforcement Fine-Tuning (RFT)

Use reinforcement fine-tuning while keeping sensitive components and data under your control. Follow these steps to run secure RFT end to end using your own storage and reward pipeline.

<Steps>
  <Step title="Configure storage (BYOB)">
    Set up your dataset storage using [GCS](#gcs-bucket-integration), [AWS S3](#aws-s3-bucket-integration), or [Azure Blob Storage](#azure-blob-storage-integration) as described above.

    For models, you can optionally use [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model).
  </Step>

  <Step title="Prepare your reward pipeline and rollouts">
    Keep your reward functions, rollout servers, and training metrics under your control. Generate rewards from your environment and write them to examples in your dataset (or export a dataset that contains per-example rewards).

    * Reward functions and reward models remain proprietary and never need to be shared
    * Rollouts and evaluation infrastructure run in your environment
    * Model checkpoints can be registered to your storage registry if desired
  </Step>

  <Step title="Create a dataset that includes rewards">
    Create or point a `Dataset` at your BYOB storage. Ensure each example contains the information required by your reward pipeline (for example, prompts, outputs/trajectories, and numeric rewards).

    <Info>
      You can reuse existing supervised data by attaching reward signals produced by your pipeline, or export a fresh dataset into your bucket for consumption by RFT.
    </Info>
  </Step>

  <Step title="Run reinforcement fine-tuning step from Python">
    Use the Python SDK to create a reinforcement fine-tuning step that reads from your BYOB dataset and produces a new checkpoint.

    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    # Create a reinforcement fine-tuning step
    step = client.reinforcement_fine_tuning_steps.create(
        rlor_trainer_job_id="my-rft-job-001",
        display_name="Secure RFT Training Step",
        training_config={
            "base_model": "accounts/fireworks/models/{BASE_MODEL}",
            "learning_rate": 1e-5,
            "lora_rank": 8,
            "max_context_length": 4096,
            "batch_size_samples": 32,
        },
        dataset="accounts/{ACCOUNT}/datasets/{DATASET_NAME}",  # Your BYOB dataset with rewards
        output_model="accounts/{ACCOUNT}/models/my-improved-model-v1",
        reward_weights=["score"],  # Field name for rewards in your dataset
    )

    # Poll for completion
    import time
    timeout = 3600  # 1 hour timeout
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Job polling timed out after {timeout} seconds")
        job = client.reinforcement_fine_tuning_steps.get(
            rlor_trainer_job_id="my-rft-job-001"
        )
        if job.state == "JOB_STATE_COMPLETED":
            print("Training complete!")
            break
        elif job.state in ("JOB_STATE_FAILED", "JOB_STATE_CANCELLED"):
            raise RuntimeError(f"Training failed: {job.state}")
        time.sleep(10)
    ```

    See the [Create Reinforcement Fine-tuning Step API reference](/api-reference/create-reinforcement-fine-tuning-step) for full parameters and options.

    <Tip>
      For a complete iterative RL workflow example using the [Python SDK](/tools-sdks/python-sdk), including rollout generation, reward computation, and hot-reloading LoRA adapters, see the [iterative RL workflow example on GitHub](https://github.com/fw-ai-external/python-sdk/tree/main/examples/iterative_rl_workflow).
    </Tip>

    <Note>
      When continuing from a LoRA checkpoint, training parameters such as `lora_rank`, `learning_rate`, `max_context_length`, and `batch_size_samples` must match the original LoRA training.
    </Note>
  </Step>

  <Step title="Verify outputs and enforce controls">
    * Validate the new checkpoint functions as expected in your environment
    * If exporting models to your storage, apply your registry policies and access reviews
    * Review audit logs and rotate any temporary credentials used for the run
  </Step>
</Steps>

<Warning>
  Do not store long-lived credentials in code. Use short-lived tokens, workload identity, or scoped service accounts when granting Fireworks access to your buckets.
</Warning>

<Check>
  You now have an end-to-end secure RFT workflow with BYOB datasets, proprietary reward pipelines, and isolated training jobs that generate new checkpoints.
</Check>

## Inference

Inference at Fireworks follows Zero Data Retention by default: prompts and generations exist only in volatile memory for the duration of the request and are never written to persistent storage or used to train any model. For full details, including the Response API storage exception and how to opt out, see the [Zero Data Retention policy](/guides/security_compliance/data_handling).

## Customer controls

The following controls are available for training workloads:

| Control                                                          | How to exercise it                                                                                                                        |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Delete a fine-tuning dataset                                     | Delete via the Fireworks console or API after the job completes.                                                                          |
| Request deletion of checkpoints, traces, or RFT rollout datasets | Contact your Fireworks account team to delete these retained artifacts.                                                                   |
| Keep data in your own bucket                                     | Use [BYOB integration](#dataset-storage-byob) to register an external dataset URL.                                                        |
| Control encryption of managed data with your own key             | Register a [CMEK](/fine-tuning/cmek) key from your cloud KMS (AWS KMS today); revoke it anytime to cut off Fireworks' ability to decrypt. |
| Avoid storing a dataset on Fireworks                             | Use the [Training API](#training-api): no dataset is uploaded or stored; the trainer only receives transient tokenized batches.           |
| Revoke Fireworks access post-training                            | Remove the IAM bindings from your bucket after the job completes.                                                                         |

For inference-side controls — disabling Response API storage (`store=False`) or deleting a specific response — see the [Zero Data Retention policy](/guides/security_compliance/data_handling).

## Related Resources

<CardGroup>
  <Card title="Zero Data Retention" href="/guides/security_compliance/data_handling" icon="lock">
    How Fireworks handles inference data by default
  </Card>

  <Card title="Customer-Managed Encryption Keys (CMEK)" href="/fine-tuning/cmek" icon="key">
    Encrypt managed fine-tuning data with your own KMS key
  </Card>

  <Card title="Data Security Overview" href="/guides/security_compliance/data_security" icon="shield-check">
    Learn about our comprehensive security measures
  </Card>

  <Card title="Reinforcement Fine Tuning" href="/fine-tuning/reinforcement-fine-tuning-models" icon="brain">
    Full guide to reinforcement fine-tuning
  </Card>

  <Card title="Training API" href="/fine-tuning/training-api/introduction" icon="code">
    Custom training loops that keep your data on your side
  </Card>
</CardGroup>
