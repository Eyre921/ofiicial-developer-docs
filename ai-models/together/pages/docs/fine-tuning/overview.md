---
title: "Overview"
source: https://docs.together.ai/docs/fine-tuning/overview
path: docs/fine-tuning/overview
---

Adapt a base model to a task by training it on your data.

Fine-tuning tailors a pretrained model to a smaller, targeted dataset so it performs better on a specific task or domain. Together AI handles the full lifecycle: data upload, training, hosting, and inference on a [dedicated endpoint](/docs/dedicated-endpoints/overview).

Together AI currently supports two fine-tuning approaches:

* **LoRA:** Trains a small set of adapter weights on top of the frozen base model. This is the default training mode, as it's faster, cheaper, and the right choice for most use cases.
* **Full fine-tuning:** Updates every weight in the base model. Uses more compute, but can outperform LoRA when the base behavior needs to shift substantially.

See [LoRA vs. full fine-tuning](/docs/fine-tuning/lora-vs-full) to choose between them. This choice is separate from the training method you pick below.

## Get started

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/fine-tuning/quickstart">
    Prepare your data, launch a LoRA job on Qwen3 8B, and evaluate the result.
  </Card>

  <Card title="Supported models" icon="list" href="/docs/fine-tuning/supported-models">
    Browse every base model you can fine-tune, with context lengths and batch sizes.
  </Card>

  <Card title="Pricing" icon="credit-card" href="/docs/fine-tuning/pricing">
    See how Together AI bills for training tokens and dedicated hosting.
  </Card>

  <Card title="Bring your own model" icon="upload" href="/docs/fine-tuning/byom">
    Fine-tune a model from the Hugging Face Hub that isn't in the Together catalog.
  </Card>
</CardGroup>

## Prepare your data

Your training dataset needs to be a JSONL or Parquet file, formatted to match your task. See the [data preparation guide](/docs/fine-tuning/data-preparation) for the schemas, validation rules, and example datasets.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  train_file = client.files.upload(
      file="train.jsonl",
      purpose="fine-tune",
      check=True,
  )
  print(train_file.id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import fs from "node:fs";

  const client = new Together();

  const trainFile = await client.files.upload({
    file: fs.createReadStream("train.jsonl"),
    purpose: "fine-tune",
  });
  console.log(trainFile.id);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.together.ai/v1/files/upload \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -F "purpose=fine-tune" \
    -F "file_name=train.jsonl" \
    -F "file=@train.jsonl"
  ```
</CodeGroup>

## Training methods

<CardGroup>
  <Card title="Supervised fine-tuning" icon="school" href="/docs/fine-tuning/supervised">
    Train on demonstration data with one target completion per example. The default method.
  </Card>

  <Card title="Preference fine-tuning" icon="scale" href="/docs/fine-tuning/preference-tuning">
    Align a model with rankings over preferred and dispreferred responses using DPO.
  </Card>
</CardGroup>

## Advanced guides

<CardGroup>
  <Card title="Vision fine-tuning" icon="eye" href="/docs/fine-tuning/vision">
    Fine-tune vision-language models on samples with image and text data.
  </Card>

  <Card title="Function calling" icon="tool" href="/docs/fine-tuning/function-calling">
    Train a model to invoke tools and structured functions reliably.
  </Card>

  <Card title="Reasoning fine-tuning" icon="brain" href="/docs/fine-tuning/reasoning">
    Train a reasoning model with chain-of-thought data.
  </Card>

  <Card title="LoRA vs. full fine-tuning" icon="git-compare" href="/docs/fine-tuning/lora-vs-full">
    Choose how much of the model to update, and tune LoRA's rank and target modules.
  </Card>
</CardGroup>

## Monitor and deploy

<CardGroup>
  <Card title="Monitor a job" icon="chart-line" href="/docs/fine-tuning/monitoring">
    Poll job status, then retrieve per-step loss and evaluation metrics.
  </Card>

  <Card title="Deploy your model" icon="server" href="/docs/fine-tuning/deployment">
    Serve your fine-tuned model on a dedicated endpoint or download it for local use.
  </Card>
</CardGroup>
