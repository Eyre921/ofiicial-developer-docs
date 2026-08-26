---
title: "Vision fine-tuning"
source: https://docs.together.ai/docs/fine-tuning/vision
path: docs/fine-tuning/vision
---

Fine-tune vision-language models on image and text data with Together AI.

Vision-language models (VLMs) combine language understanding with visual comprehension. Fine-tuning a VLM adapts it to image-and-text tasks such as visual question answering, image captioning, and document understanding.

This page covers the VLM-specific data shape, supported models, and launch parameters.

## Supported models

The following models support vision-language fine-tuning. See [supported models](/docs/fine-tuning/supported-models) for context lengths and batch limits.

<Accordion title="Supported models">
  | Organization | Model                                  | API ID                                              |
  | ------------ | -------------------------------------- | --------------------------------------------------- |
  | Qwen         | Qwen3.8 27B                            | `Qwen/Qwen3.8-27B`                                  |
  | Qwen         | Qwen3.5 27B                            | `Qwen/Qwen3.5-27B`                                  |
  | Qwen         | Qwen3.5 9B                             | `Qwen/Qwen3.5-9B`                                   |
  | Qwen         | Qwen3.5 4B                             | `Qwen/Qwen3.5-4B`                                   |
  | Qwen         | Qwen3.5 2B                             | `Qwen/Qwen3.5-2B`                                   |
  | Qwen         | Qwen3.5 0.8B                           | `Qwen/Qwen3.5-0.8B`                                 |
  | Qwen         | Qwen3.6 27B                            | `Qwen/Qwen3.6-27B`                                  |
  | Meta         | Llama 4 Scout 17B 16E Instruct VLM     | `meta-llama/Llama-4-Scout-17B-16E-Instruct-VLM`     |
  | Meta         | Llama 4 Maverick 17B 128E Instruct VLM | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-VLM` |
  | Google       | Gemma 4 31B IT VLM                     | `google/gemma-4-31B-it-VLM`                         |
</Accordion>

## Prepare your data

Prepare data in a JSONL file, where each line represents one example, with messages that contain text and images. Constraints include:

* **Image encoding:** Each image is base64-encoded with a MIME type prefix (`data:image/jpeg;base64,...`). If your data references URLs, download and encode the images first.
* **Per-example image limit:** 10 images.
* **Per-image size:** 10 MB.
* **Supported formats:** PNG, JPEG, WEBP.

Only `user` messages can contain images.

### Conversational format

```json theme={null}
{
  "messages": [
    {
      "role": "system",
      "content": [
        {"type": "text", "text": "You are a helpful assistant with vision capabilities."}
      ]
    },
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "How many oranges are in the bowl?"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,iVBORw0KGgo..."}}
      ]
    },
    {
      "role": "assistant",
      "content": [
        {"type": "text", "text": "There are at least 7 oranges in this bowl."}
      ]
    }
  ]
}
```

### Instruction format

```json theme={null}
{
  "prompt": [
    {"type": "text", "text": "How many oranges are in the bowl?"},
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,iVBORw0KGgo..."}}
  ],
  "completion": [
    {"type": "text", "text": "There are at least 7 oranges in this bowl."}
  ]
}
```

### Preference format

```json theme={null}
{
  "input": {
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "How many oranges are in the bowl?"},
          {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,iVBORw0KGgo..."}}
        ]
      }
    ]
  },
  "preferred_output": [
    {"role": "assistant", "content": [{"type": "text", "text": "There are at least 7 oranges."}]}
  ],
  "non_preferred_output": [
    {"role": "assistant", "content": [{"type": "text", "text": "There are 11 oranges."}]}
  ]
}
```

### Convert image URLs to base64

```python Python theme={null}
import base64
import requests


def url_to_base64(url: str, mime_type: str = "image/jpeg") -> str:
    response = requests.get(url)
    encoded = base64.b64encode(response.content).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"
```

## Validate and upload

Upload your data using the Together Python/TypeScript SDK or the [Together CLI](/reference/cli/getting-started):

<CodeGroup>
  ```bash CLI theme={null}
  tg files check "vlm_dataset.jsonl"
  tg files upload "vlm_dataset.jsonl"
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  train_file = client.files.upload(
      file="vlm_dataset.jsonl",
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
    file: fs.createReadStream("vlm_dataset.jsonl"),
    purpose: "fine-tune",
  });
  console.log(trainFile.id);
  ```
</CodeGroup>

Sample response:

```json theme={null}
{
  "id": "file-629e58b4-ff73-438c-b2cc-f69542b27980",
  "object": "file",
  "purpose": "fine-tune",
  "filename": "vlm_dataset.jsonl",
  "FileType": "jsonl"
}
```

## Launch the job

By default, fine-tuning only updates language-model parameters. Pass `train_vision=True` to also update the vision encoder. The trade-off here is that training the encoder costs more compute and is rarely necessary unless your domain images are extremely dissimilar from the pretraining data.

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3-VL-8B-Instruct" \
    --train-vision false \
    --lora
  ```

  ```python Python theme={null}
  job = client.fine_tuning.create(
      training_file=train_file.id,
      model="Qwen/Qwen3-VL-8B-Instruct",
      lora=True,
      train_vision=False,
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  const job = await client.fineTuning.create({
    training_file: trainFile.id,
    model: "Qwen/Qwen3-VL-8B-Instruct",
    lora: true,
    train_vision: false,
  });
  console.log(job.id);
  ```
</CodeGroup>

For full fine-tuning, set `lora=False`. For details on all available parameters, see the [API reference](/reference/cli/finetune).

## Watch and deploy

VLM jobs use the same lifecycle as text jobs:

* [Poll the job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) with the SDK or CLI. Expect 15 to 60 minutes for a LoRA job on an 8B model with a few thousand examples, and several hours for a full job on a 30B model.
* Deploy the result on a [dedicated endpoint](/docs/fine-tuning/deployment).

VLM endpoints accept the same vision request shapes as the base models. See [vision inputs](/docs/inference/vision/inputs) for details.
