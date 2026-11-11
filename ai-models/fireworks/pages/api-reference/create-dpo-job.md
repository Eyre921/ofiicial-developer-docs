---
title: "Create DPO Job"
source: https://docs.fireworks.ai/api-reference/create-dpo-job
path: api-reference/create-dpo-job
---

post /v1/accounts/{account_id}/dpoJobs
Create a DPO fine-tuning job from a dataset, with training config, a loss config for DPO or ORPO, Weights & Biases logging, and S3 or Azure dataset access.

> [!WARNING]
>
> Managed SFT and DPO no longer accept new jobs. Your trained models stay deployable. To keep training, follow [Migrate from Managed Training](/fine-tuning/migrate-from-managed-training).
