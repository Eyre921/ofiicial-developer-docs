---
title: "Secure Training (BYOB)"
source: https://docs.fireworks.ai/fine-tuning/secure-fine-tuning
path: fine-tuning/secure-fine-tuning
---

Fine-tune models while keeping sensitive data and components under your control

Fireworks enables secure model fine-tuning while maintaining customer control over sensitive components and data. Use your own cloud storage, keep reward functions proprietary, and ensure training data never persists on our platform beyond active workflows.

## Dataset Storage (BYOB)

Point Fireworks to your own cloud storage for training datasets. This applies to both Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT) jobs.

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

Create an IAM role with a trust policy that allows Fireworks to assume it via web identity federation. Fireworks provides the OIDC audience value during BYOB onboarding.

* **Federated Principal:** `accounts.google.com`
* **Action:** `sts:AssumeRoleWithWebIdentity`
* **Condition:** `accounts.google.com:aud` equals `<FIREWORKS_GCP_OIDC_AUDIENCE>`

Then attach a policy granting `s3:GetObject` and `s3:ListBucket` on your bucket.

Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) if you need the exact audience value.

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
            "batch_size": 32768,
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
      When continuing from a LoRA checkpoint, training parameters such as `lora_rank`, `learning_rate`, `max_context_length`, and `batch_size` must match the original LoRA training.
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

## Related Resources

<CardGroup>
  <Card title="Data Security Overview" href="/guides/security_compliance/data_security" icon="shield-check">
    Learn about our comprehensive security measures
  </Card>

  <Card title="Reinforcement Fine Tuning" href="/fine-tuning/reinforcement-fine-tuning-models" icon="brain">
    Full guide to reinforcement fine-tuning
  </Card>
</CardGroup>
