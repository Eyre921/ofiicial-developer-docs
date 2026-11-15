---
title: "Bring your own bucket (BYOB)"
source: https://docs.fireworks.ai/guides/security_compliance/secure_training/byob
path: guides/security_compliance/secure_training/byob
---

Dataset creation and Managed Training are retired. Learn how the Training API reads data directly from your local machine or cloud bucket, and how to clean up existing BYOB dataset records.

> [!WARNING]
>
> **Dataset creation and Managed Training are retired.** Creating new datasets (including `--external-url` proxy datasets), uploading or downloading dataset files, and launching new Managed Training jobs are disabled. Train new models with the [Training API](/fine-tuning/training-api/introduction), which reads data directly in your environment without creating a dataset resource on Fireworks.

Bring Your Own Bucket (BYOB) previously let Managed Training jobs read a dataset in place from your own Google Cloud Storage, Amazon S3, or Azure Blob Storage bucket without persisting a copy on Fireworks-managed storage.

## Keep training data in your bucket on the Training API

With the [Training API](/fine-tuning/training-api/introduction), your training script runs in your own environment, loads and tokenizes your dataset locally, and sends only tokenized batches to Fireworks GPUs on each step. No dataset resource is created, uploaded, or stored on Fireworks.

* Read a local JSONL file or stream directly from your Google Cloud Storage bucket (`gs://...`) using your own cloud credentials. See [Cookbook: Supervised Fine-Tuning](/fine-tuning/training-api/cookbook/sft#using-the-recipe) and [Migrate from Managed Training](/fine-tuning/migrate-from-managed-training).
* For data in Amazon S3 or Azure Blob Storage, read or sync it in your own training environment before tokenizing batches.

## Existing BYOB datasets

Existing BYOB dataset records still point at your bucket, and any IAM bindings or federated credentials you configured during onboarding remain active until you remove them. Once any in-flight jobs have finished:

1. Inspect or list remaining dataset records with `firectl dataset list` / `firectl dataset get <DATASET_ID>`, and delete records you no longer need with `firectl dataset delete <DATASET_ID>` (or [Delete Dataset](/api-reference/delete-dataset)).
2. Remove the IAM policy bindings, AWS IAM role trust, or Azure federated credential you granted to Fireworks.

See [Secure Training](/guides/security_compliance/secure_training) for what Fireworks retains from training jobs and how to request artifact deletion.
