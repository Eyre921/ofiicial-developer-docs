---
title: "Customer-Managed Encryption Keys (CMEK)"
source: https://docs.fireworks.ai/guides/security_compliance/secure_training/cmek
path: guides/security_compliance/secure_training/cmek
---

Use your own cloud KMS key to control encryption of your managed training data

With Customer-Managed Encryption Keys (CMEK), you bring an encryption key from your own cloud KMS — AWS KMS, Google Cloud KMS, or Azure Key Vault — and Fireworks uses it to encrypt the data your managed training jobs read and write. Your key controls access to your data at rest: revoke it and Fireworks can no longer decrypt your datasets or checkpoints. Calls Fireworks makes to your key are recorded in your own cloud's audit log.

<Info>
  Fireworks never stores your root key. Each fine-tuning resource gets a unique data key that is encrypted ("wrapped") by your KMS key and stored only in wrapped form. The unwrapped key exists only briefly in memory during a job and is then discarded.
</Info>

## How it works

CMEK uses envelope encryption:

1. You create a key (your key-encryption key, or KEK) in your own cloud KMS and grant Fireworks permission to call `Encrypt` and `Decrypt` on it — nothing else.
2. The first time a job, dataset, or checkpoint needs encryption, Fireworks generates a unique 256-bit data-encryption key (DEK) for that resource and immediately wraps it with your KEK. Only the wrapped key is persisted.
3. Fireworks encrypts your artifacts locally with AES-256-GCM before they are written to storage.
4. To read the data back, Fireworks asks your KMS to unwrap the DEK. That call — and every call — is logged in your cloud's KMS audit trail. Unwrapped keys are cached briefly (about 5 minutes) and then discarded, so subsequent reads re-validate against your KMS.

Because access to your data depends on your KMS answering an unwrap request, you stay in control: disable or revoke the key and the data becomes unreadable.

<Note>
  During an active fine-tuning job, training compute processes your data in plaintext in memory — that is inherent to training a model on it. CMEK controls access to your data **at rest** (datasets, checkpoints, and logs), not the in-memory computation during the job itself.
</Note>

## What CMEK protects

CMEK covers the durable artifacts your fine-tuning jobs read and write:

* Training and evaluation datasets you upload
* Intermediate checkpoints and distributed-checkpoint shards

The following are governed by separate operational and contractual controls rather than your key:

* Job metadata (job names, hyperparameters, status) stored in the Fireworks control plane
* Transient scratch data that exists only for the duration of a job and is destroyed when the job ends

<Note>
  CMEK supports **LoRA** Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Reinforcement Fine-Tuning (RFT). Full-parameter training is not supported. Today, CMEK covers the datasets and intermediate checkpoints your jobs read and write. Encrypting **final model weights** with your key, and deploying a model whose weights were encrypted with your key, is coming soon. Encrypting inference requests and responses with your key is not part of CMEK today.
</Note>

## Supported KMS providers

CMEK supports all three major cloud KMS services. Fireworks needs only `Encrypt` and `Decrypt` on your key, and authenticates with short-lived, federated credentials.

| Cloud        | KMS             | How Fireworks authenticates                               |
| ------------ | --------------- | --------------------------------------------------------- |
| AWS          | AWS KMS         | IAM role assumed via OIDC web-identity federation         |
| Google Cloud | Cloud KMS       | Workload Identity Federation via a workload identity pool |
| Azure        | Azure Key Vault | Workload Identity Federation to an Entra app registration |

### How Fireworks authenticates

CMEK uses the federated trust model described in [How Fireworks accesses your cloud](/guides/security_compliance/secure_training#how-fireworks-accesses-your-cloud): Fireworks authenticates as a Google-issued OIDC identity, you configure your cloud's IAM to trust it, and you allow it `Encrypt`/`Decrypt` on your key — nothing else. No long-lived secret is exchanged, and nothing Fireworks runs is deployed into your account.

Pin trust on these values:

| Value                        | Identifier                      |
| ---------------------------- | ------------------------------- |
| OIDC issuer                  | `https://accounts.google.com`   |
| Fireworks identity (subject) | `<FIREWORKS_CMEK_OIDC_SUBJECT>` |
| Token audience               | `<YOUR_FIREWORKS_ACCOUNT_ID>`   |

The subject is stable per environment and is provided during CMEK onboarding; the audience is your own Fireworks account ID. Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) if you need the exact subject identifier.

<Note>
  CMEK and [BYOB](/guides/security_compliance/secure_training/byob) authenticate as **different** Fireworks service accounts, so their subject identifiers differ. Use the CMEK subject here, not the one from your BYOB setup.
</Note>

<Warning>
  Grant only `Encrypt` and `Decrypt` on the specific key. CMEK never needs to export key material, and never needs administrative permissions on your key.
</Warning>

## Setup

<Steps>
  <Step title="Create or choose a key in your KMS">
    Create a symmetric encryption key in your cloud KMS (or pick an existing one). One key per Fireworks account is sufficient — Fireworks derives a unique data key per resource underneath it.

    * **AWS KMS** — a symmetric KMS key in your account and region.
    * **Google Cloud KMS** — a symmetric key in a key ring.
    * **Azure Key Vault** — a key in a Standard vault or Managed HSM.
  </Step>

  <Step title="Grant Fireworks Encrypt/Decrypt on the key">
    Authorize the Fireworks identity to call `Encrypt` and `Decrypt` on your key. You grant access to the federated identity — you never share a secret.

    <Tabs>
      <Tab title="AWS KMS">
        Create an IAM role the Fireworks identity can assume via web-identity federation, and allow that role `Encrypt`/`Decrypt` on your key. You do **not** need to register an OIDC identity provider — `accounts.google.com` is a built-in federated principal in AWS STS.

        Trust policy on the role, locked to the Fireworks identity:

        ```json theme={null}
        {
          "Effect": "Allow",
          "Principal": { "Federated": "accounts.google.com" },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "accounts.google.com:sub": "<FIREWORKS_CMEK_OIDC_SUBJECT>",
              "accounts.google.com:oaud": "<YOUR_FIREWORKS_ACCOUNT_ID>"
            }
          }
        }
        ```

        The `sub` condition locks assumption to the Fireworks identity; the `oaud` condition pins the token's audience to your Fireworks account, so a token issued for any other account is rejected.

        AWS KMS authorizes against both IAM and the key policy, so grant `kms:Encrypt` and `kms:Decrypt` on the specific key in **both** the role's permissions policy **and** the key policy.

        You'll register the account ID, region, key ARN, and role ARN with Fireworks in the next step.
      </Tab>

      <Tab title="Google Cloud KMS">
        Create a workload identity pool with an OIDC provider that trusts the Fireworks identity, then grant the federated principal `Encrypt`/`Decrypt` on your key. The principal lives in your own project, so this works even under org policies that forbid granting roles to service accounts outside your organization.

        ```bash theme={null}
        # 1. Create a workload identity pool
        gcloud iam workload-identity-pools create fireworks-cmek \
          --location="global" --display-name="Fireworks CMEK"

        # 2. Add an OIDC provider that trusts the Fireworks identity,
        #    scoped to your Fireworks account ID as the allowed audience
        gcloud iam workload-identity-pools providers create-oidc fireworks-cmek \
          --location="global" \
          --workload-identity-pool="fireworks-cmek" \
          --issuer-uri="https://accounts.google.com" \
          --allowed-audiences="<YOUR_FIREWORKS_ACCOUNT_ID>" \
          --attribute-mapping="google.subject=assertion.sub" \
          --attribute-condition="assertion.sub == '<FIREWORKS_CMEK_OIDC_SUBJECT>'"

        # 3. Grant Encrypt/Decrypt on the key to the federated principal
        gcloud kms keys add-iam-policy-binding <YOUR_KEY> \
          --keyring="<YOUR_KEYRING>" --location="<LOCATION>" \
          --member="principal://iam.googleapis.com/projects/<YOUR_PROJECT_NUMBER>/locations/global/workloadIdentityPools/fireworks-cmek/subject/<FIREWORKS_CMEK_OIDC_SUBJECT>" \
          --role="roles/cloudkms.cryptoKeyEncrypterDecrypter"
        ```

        The predefined `cryptoKeyEncrypterDecrypter` role is exactly `useToEncrypt` + `useToDecrypt`. If you prefer to pin the permission set yourself, create a custom role with just those two permissions and bind that instead.

        You'll register your project number, workload identity pool and provider IDs, and the key resource name with Fireworks in the next step.
      </Tab>

      <Tab title="Azure Key Vault">
        Add a federated credential to an Entra app registration (or a user-assigned managed identity) that trusts the Fireworks identity, then grant that identity crypto permissions on your key. Works with both Standard vaults and Managed HSM.

        ```bash theme={null}
        # 1. Trust the Fireworks identity on your app registration
        az identity federated-credential create \
          --name fireworks-cmek \
          --identity-name <YOUR_MANAGED_IDENTITY> \
          --resource-group <YOUR_RESOURCE_GROUP> \
          --issuer "https://accounts.google.com" \
          --subject "<FIREWORKS_CMEK_OIDC_SUBJECT>" \
          --audiences "<YOUR_FIREWORKS_ACCOUNT_ID>"

        # 2. Grant Encrypt/Decrypt on the key
        az role assignment create \
          --assignee <YOUR_CLIENT_ID> \
          --role "Key Vault Crypto User" \
          --scope <YOUR_KEY_VAULT_KEY_ID>
        ```

        Fireworks authenticates as one app registration per Fireworks account. You'll register the tenant ID, client ID, and the fully versioned Key Vault key identifier (including the version segment) with Fireworks in the next step.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Register the key with your Fireworks account">
    Send the identity references you gathered above to your Fireworks account team, who register the key on your account and enable CMEK enforcement for it.

    Depending on your cloud, that is:

    | Cloud        | What to send                                                                              |
    | ------------ | ----------------------------------------------------------------------------------------- |
    | AWS          | Key ARN and the ARN of the IAM role Fireworks assumes                                     |
    | Google Cloud | Cloud KMS key resource name and the workload identity pool provider resource name         |
    | Azure        | Fully versioned Key Vault key identifier, Entra tenant ID, and app registration client ID |

    <Note>
      Key registration and CMEK enablement are performed by Fireworks, not self-serve — the underlying commands are restricted to Fireworks operators. Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) or your account team to start onboarding.
    </Note>

    Once a key is registered and CMEK is enabled, encryption is automatic — your data is encrypted at rest with your key, and uploads through `firectl` and the SDKs are encrypted client-side, so plaintext never leaves your environment. Keep your `firectl` / SDK up to date.
  </Step>

  <Step title="Verify">
    <Check>
      Run a small fine-tune (below) and confirm `Encrypt` / `Decrypt` calls appear in your cloud's KMS audit log.
    </Check>
  </Step>
</Steps>

## Running a CMEK fine-tune

Once your key is registered, fine-tuning works exactly as it does today — encryption and decryption are transparent.

```bash theme={null}
# Upload a dataset (encrypted client-side with your key)
firectl dataset create {DATASET_NAME} --file ./data.jsonl

# Launch a supervised fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME}
```

<Note>
  Encrypting the resulting model's **final weights** with your key — so downloads decrypt transparently and you can deploy the model on Fireworks with your key — is coming soon.
</Note>

## Rotating and revoking your key

CMEK respects the lifecycle controls your KMS already gives you.

* **Key-version rotation** — When you create a new version of a key in your KMS, new data is wrapped with the new version automatically and existing data keeps working. No action is needed on the Fireworks side, and your data is never re-encrypted.
* **Rotating the registered key** — Your account can hold more than one registered key, exactly one of which is **primary**. New resources are wrapped under the primary key; previously registered keys stay registered so older data remains decryptable. To rotate, ask your account team to register the new key and promote it to primary, which demotes the previous primary. Retire the old key only once nothing still depends on it.
* **Revocation** — Revoke the grant, disable the key, or schedule it for destruction in your KMS. In-flight jobs holding a cached key continue until the cache expires (about 5 minutes), then fail closed. New jobs fail immediately.
* **Re-grant** — Restore the grant or re-enable the key and access resumes; new jobs work right away.

<Warning>
  Disabling or destroying your key makes the data encrypted under it **permanently unrecoverable** by Fireworks — by design. Likewise, if your KMS is unreachable for longer than the key cache window, in-flight jobs will fail.
</Warning>

## Auditing

Every `Encrypt` and `Decrypt` call Fireworks makes against your key is recorded in your cloud's native audit log — AWS CloudTrail, Google Cloud Logging, or Azure Monitor — including the calls that fail after you revoke access. You hold the authoritative record of when and how your key was used.

## Limitations

* CMEK applies to **LoRA** SFT, DPO, and RFT jobs. Full-parameter training is not supported.
* Encrypting **final model weights** with your key — and deploying a model whose weights were encrypted with your key — is coming soon. Today CMEK covers your datasets and intermediate checkpoints.
* During an active job, compute processes your data in plaintext in memory; CMEK protects data at rest, not in-memory computation.
* Encrypting inference requests and responses with your key is not part of CMEK today.
* Uploads must go through `firectl` or the SDKs, which encrypt client-side before data leaves your environment. The web-console upload path doesn't perform that client-side encryption yet, so it isn't supported on CMEK-enabled accounts. *(Planned: web-console upload support is expected in a future release.)*
* Key registration, rotation, and CMEK enablement are performed by Fireworks on your behalf rather than self-serve.
* Job metadata and transient scratch data are covered by separate operational and contractual controls, not your key.

## Related Resources

<CardGroup>
  <Card title="Bring Your Own Bucket (BYOB)" href="/guides/security_compliance/secure_training/byob" icon="lock">
    Keep training datasets in your own cloud storage
  </Card>

  <Card title="Data Security Overview" href="/guides/security_compliance/data_security" icon="shield-check">
    Learn about our comprehensive security measures
  </Card>
</CardGroup>
