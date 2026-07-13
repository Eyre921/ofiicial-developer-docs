---
title: "Customer-Managed Encryption Keys (CMEK)"
source: https://docs.fireworks.ai/fine-tuning/cmek
path: fine-tuning/cmek
---

Use your own cloud KMS key to control encryption of your managed fine-tuning data

With Customer-Managed Encryption Keys (CMEK), you bring an encryption key from your own cloud KMS — today, AWS KMS — and Fireworks uses it to encrypt the data your managed fine-tuning jobs read and write. Your key controls access to your data at rest: revoke it and Fireworks can no longer decrypt your datasets or checkpoints. Calls Fireworks makes to your key are recorded in your own cloud's audit log.

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
  CMEK currently supports Supervised Fine-Tuning (SFT). Support for Direct Preference Optimization (DPO) and Reinforcement Fine-Tuning (RFT) is coming soon. Today, CMEK covers the datasets and intermediate checkpoints your jobs read and write. Encrypting **final model weights** with your key, and deploying a model whose weights were encrypted with your key, is also coming soon. Encrypting inference requests and responses with your key is not part of CMEK today.
</Note>

## Supported KMS providers

CMEK currently supports **AWS KMS**. Fireworks needs only `Encrypt` and `Decrypt` on your key, and authenticates with short-lived, federated credentials.

| Cloud | KMS     | How Fireworks authenticates                       |
| ----- | ------- | ------------------------------------------------- |
| AWS   | AWS KMS | IAM role assumed via OIDC web-identity federation |

<Note>
  Support for **Azure Key Vault** and **Google Cloud KMS** is coming soon.
</Note>

### How Fireworks authenticates

Fireworks reaches your cloud from a **single federated identity** — a Google-issued OIDC identity that the managed fine-tuning service runs as. You configure your cloud's IAM to trust that identity through federation (for AWS, web-identity federation into an IAM role) and to allow it `Encrypt`/`Decrypt` on your key. Three properties follow from this design:

* **No long-lived secrets.** Fireworks presents a short-lived, automatically rotated token on each call. There is no API key or client secret for you to store, rotate, or risk leaking.
* **Nothing runs in your cloud.** Fireworks does not deploy software into your account to reach your KMS — it calls your KMS's API from Fireworks infrastructure, as the identity you authorized.
* **Scoped to your account.** The token Fireworks presents when it authenticates carries your Fireworks account ID as its audience, and you configure your federation trust to accept only that audience. A token issued for any other account is rejected by your cloud — so cross-tenant access is blocked by your own infrastructure, not just by Fireworks.

To configure trust, you use the Fireworks identity below, scoped to your own account as the token audience:

| Value                        | Identifier                    |
| ---------------------------- | ----------------------------- |
| OIDC issuer                  | `https://accounts.google.com` |
| Fireworks identity (subject) | `108606366655288854355`       |
| Token audience               | `<YOUR_FIREWORKS_ACCOUNT_ID>` |

The issuer and subject are published by Fireworks (stable per environment); the audience is your own Fireworks account ID.

<Warning>
  Grant only `Encrypt` and `Decrypt` on the specific key. CMEK never needs to export key material, and never needs administrative permissions on your key.
</Warning>

## Setup

<Steps>
  <Step title="Create or choose a key in your KMS">
    Create a symmetric encryption key in your cloud KMS (or pick an existing one). One key per Fireworks account is sufficient — Fireworks derives a unique data key per resource underneath it.

    * **AWS KMS** — a symmetric KMS key in your account and region.
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
              "accounts.google.com:sub": "108606366655288854355",
              "accounts.google.com:oaud": "<YOUR_FIREWORKS_ACCOUNT_ID>"
            }
          }
        }
        ```

        The `sub` condition locks assumption to the Fireworks identity; the `oaud` condition pins the token's audience to your Fireworks account, so a token issued for any other account is rejected.

        AWS KMS authorizes against both IAM and the key policy, so grant `kms:Encrypt` and `kms:Decrypt` on the specific key in **both** the role's permissions policy **and** the key policy.

        You'll register the account ID, region, key ARN, and role ARN with Fireworks in the next step.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Register the key with your Fireworks account">
    Register the key — together with the identity references you gathered above — on your account. You register one key per account.

    ```bash theme={null}
    firectl account external-keys create \
      --cloud aws \
      --kms-key "<YOUR_KMS_KEY_RESOURCE_ID>"

    firectl account external-keys list
    ```

    Also pass the identity references from the AWS tab above (for example, `--role-arn`).

    Once a key is registered, encryption is automatic — your data is encrypted at rest with your key, and uploads through `firectl` and the SDKs are encrypted client-side, so plaintext never leaves your environment. Keep your `firectl` / SDK up to date.
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
* **Rotating the registered key** *(planned)* — Changing the key registered with your account isn't supported yet; today you set one key at registration. We expect to support registering additional keys and promoting a new primary — so new data wraps under the new key while previously registered keys keep older data decryptable — in a future release.
* **Revocation** — Revoke the grant, disable the key, or schedule it for destruction in your KMS. In-flight jobs holding a cached key continue until the cache expires (about 5 minutes), then fail closed. New jobs fail immediately.
* **Re-grant** — Restore the grant or re-enable the key and access resumes; new jobs work right away.

<Warning>
  Disabling or destroying your key makes the data encrypted under it **permanently unrecoverable** by Fireworks — by design. Likewise, if your KMS is unreachable for longer than the key cache window, in-flight jobs will fail.
</Warning>

## Auditing

Every `Encrypt` and `Decrypt` call Fireworks makes against your key is recorded in your cloud's native audit log — AWS CloudTrail — including the calls that fail after you revoke access. You hold the authoritative record of when and how your key was used.

## Limitations

* CMEK currently supports **AWS KMS**. Support for Azure Key Vault and Google Cloud KMS is coming soon.
* Encrypting **final model weights** with your key — and deploying a model whose weights were encrypted with your key — is coming soon. Today CMEK covers your datasets and intermediate checkpoints.
* During an active job, compute processes your data in plaintext in memory; CMEK protects data at rest, not in-memory computation.
* Encrypting inference requests and responses with your key is not part of CMEK today.
* Uploads must go through `firectl` or the SDKs, which encrypt client-side before data leaves your environment. The web-console upload path doesn't perform that client-side encryption yet, so it isn't supported on CMEK-enabled accounts. *(Planned: web-console upload support is expected in a future release.)*
* Changing the registered key is not supported yet — you register one key per account at registration time. *(Planned: rotating to a new registered key is expected in a future release.)*
* Job metadata and transient scratch data are covered by separate operational and contractual controls, not your key.

## Related Resources

<CardGroup>
  <Card title="Secure Training (BYOB)" href="/fine-tuning/secure-fine-tuning" icon="lock">
    Keep datasets and models in your own cloud storage
  </Card>

  <Card title="Data Security Overview" href="/guides/security_compliance/data_security" icon="shield-check">
    Learn about our comprehensive security measures
  </Card>
</CardGroup>
