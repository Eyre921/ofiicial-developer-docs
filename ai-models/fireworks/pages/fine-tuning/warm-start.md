---
title: "Warm Start from Fine-Tuned Models"
source: https://docs.fireworks.ai/fine-tuning/warm-start
path: fine-tuning/warm-start
---

Continue training from a previously fine-tuned model with RFT

Fireworks supports RFT training on warm start and already-fine-tuned models. Upload models to Fireworks and use the warm start option to continue training (e.g. from an SFT LoRA) with RFT, rather than start from scratch with a base model.

## When to use warm start

Use the `--warm-start-from` flag when you want to:

* Start RFT from an SFT model you've trained with Fireworks
* Continue training from an existing fine-tuned LoRA adapter you've uploaded to Fireworks

## Basic usage

```bash theme={null}
eval-protocol create rft \
  --warm-start-from accounts/your-account/models/<SFT_MODEL_ID> \
  --output-model <RFT_MODEL_ID>
```

<Warning>
  When using `--warm-start-from`, do NOT include `--base-model`. The base model is automatically determined from the LoRA adapter.

  ```bash theme={null}
  # Wrong, includes --base-model
  eval-protocol create rft \
    --base-model accounts/fireworks/models/qwen3-4b \
    --warm-start-from accounts/your-account/models/<SFT_MODEL_ID>
  ```
</Warning>

## SFT to RFT workflow

<Steps>
  <Step title="Create or upload SFT model">
    Get started with supervised fine-tuning on Fireworks:

    ```bash theme={null}
    firectl sftj create \
      --base-model accounts/fireworks/models/<BASE_MODEL_ID> \
      --dataset accounts/your-account/datasets/<DATASET_ID> \
      --output-model <MODEL_ID>
    ```

    Or if you already have a LoRA adapter, upload it to Fireworks:

    ```bash theme={null}
    firectl model create <MODEL_ID> /path/to/files/ \
      --base-model "accounts/fireworks/models/<BASE_MODEL_ID>"
    ```

    <Note>
      Learn more about uploading custom LoRA adapters in the [Custom Models guide](/models/uploading-custom-models#importing-fine-tuned-models).
    </Note>
  </Step>

  <Step title="Start RFT from SFT model">
    Use an existing model as a starting point, and combine with standard RFT parameters.

    ```bash theme={null}
    eval-protocol create rft \
      --warm-start-from accounts/your-account/models/<SFT_MODEL_ID> \
      --output-model <RFT_MODEL_ID> \
      --epochs 2 \
      --learning-rate 5e-5 \
      --temperature 0.8
    ```
  </Step>
</Steps>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error: 'not of kind base_model, but HF_PEFT_ADDON'">
    This means you specified both `--base-model` and `--warm-start-from`. Remove the `--base-model` flag.
  </Accordion>

  <Accordion title="Model not found">
    Verify the model exists in your account:

    ```bash theme={null}
    firectl model list --account accounts/your-account
    ```
  </Accordion>
</AccordionGroup>
