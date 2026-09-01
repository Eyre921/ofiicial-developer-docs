---
title: "Secure Reinforcement Fine-Tuning"
source: https://docs.fireworks.ai/guides/security_compliance/secure_training/secure_rft
path: guides/security_compliance/secure_training/secure_rft
---

Run RFT end to end with your dataset, reward pipeline, and rollout infrastructure under your own control

Use reinforcement fine-tuning while keeping sensitive components and data under your control. This composes [BYOB](/guides/security_compliance/secure_training/byob) storage with a reward pipeline and rollout infrastructure that stay in your environment.

<Steps>
  <Step title="Configure storage (BYOB)">
    Set up your dataset storage using [GCS](/guides/security_compliance/secure_training/byob#gcs-bucket-integration), [AWS S3](/guides/security_compliance/secure_training/byob#aws-s3-bucket-integration), or [Azure Blob Storage](/guides/security_compliance/secure_training/byob#azure-blob-storage-integration) on the BYOB page.

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
