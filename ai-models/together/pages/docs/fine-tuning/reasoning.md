---
title: "Reasoning fine-tuning"
source: https://docs.together.ai/docs/fine-tuning/reasoning
path: docs/fine-tuning/reasoning
---

Train a reasoning model on chain-of-thought data.

Reasoning fine-tuning adapts a model that supports chain-of-thought reasoning. By providing `reasoning` or `reasoning_content` alongside the final assistant response, you shape how the model thinks through problems before producing an answer.

This page covers the reasoning data shape, supported models, and launch parameters.

<Warning>
  Reasoning models should always be fine-tuned with reasoning data. Training a reasoning model without it can degrade its reasoning ability. If your dataset doesn't include reasoning, use an instruct model instead.
</Warning>

## Supported models

| Organization | Model                                                                       | API ID                             |
| ------------ | --------------------------------------------------------------------------- | ---------------------------------- |
| Qwen         | Qwen 3 (0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 235B-A22B) and Base variants | `Qwen/Qwen3-*`                     |
| Qwen         | Qwen 3 Next 80B A3B Thinking                                                | `Qwen/Qwen3-Next-80B-A3B-Thinking` |
| Qwen         | Qwen 3.5 (0.8B, 2B, 4B, 9B, 27B, 35B-A3B, 122B-A10B, 397B-A17B)             | `Qwen/Qwen3.5-*`                   |
| Qwen         | Qwen 3.6 35B A3B                                                            | `Qwen/Qwen3.6-35B-A3B`             |
| Z.ai         | GLM 4.6, GLM 4.7, GLM 5, GLM 5.1                                            | `zai-org/GLM-*`                    |
| Google       | Gemma 4 31B IT, Gemma 4 26B A4B IT                                          | `google/gemma-4-*`                 |
| OpenAI       | GPT-OSS 20B, GPT-OSS 120B                                                   | `openai/gpt-oss-*`                 |

## Prepare your data

Prepare data in a JSONL file. Each assistant message should carry the chain of thought in a `reasoning` (or `reasoning_content`) field and the final answer in `content`.

### Conversational format

```json theme={null}
{
  "messages": [
    {"role": "user", "content": "What is the capital of France?"},
    {
      "role": "assistant",
      "reasoning": "The user is asking about the capital of France. France is a country in Western Europe. Its capital city is Paris, which has been the capital since the 10th century.",
      "content": "The capital of France is Paris."
    }
  ]
}
```

<Info>
  When fine-tuning reasoning models on conversational data, only the last assistant message is trained on by default. For multi-turn reasoning, split the conversation so each assistant message is the final message in its own example.
</Info>

### Preference format

For preference fine-tuning, both outputs carry `reasoning`. See [preference tuning](/docs/fine-tuning/preference-tuning) for the broader DPO workflow.

```json theme={null}
{
  "input": {
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  },
  "preferred_output": [
    {
      "role": "assistant",
      "reasoning": "France is in Western Europe. Its capital is Paris.",
      "content": "The capital of France is Paris."
    }
  ],
  "non_preferred_output": [
    {
      "role": "assistant",
      "reasoning": "Let me think about European capitals.",
      "content": "The capital of France is Berlin."
    }
  ]
}
```

## Validate and upload

Upload your data using the Together Python/TypeScript SDK or the [Together CLI](/reference/cli/getting-started):

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  train_file = client.files.upload(
      file="reasoning_dataset.jsonl",
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
    file: fs.createReadStream("reasoning_dataset.jsonl"),
    purpose: "fine-tune",
  });
  console.log(trainFile.id);
  ```

  ```bash CLI theme={null}
  tg files check "reasoning_dataset.jsonl"
  tg files upload "reasoning_dataset.jsonl"
  ```
</CodeGroup>

## Launch the job

LoRA is the default. Pass `lora=False` for full fine-tuning.

<CodeGroup>
  ```python Python theme={null}
  job = client.fine_tuning.create(
      training_file=train_file.id,
      model="Qwen/Qwen3-8B",
      lora=True,
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  const job = await client.fineTuning.create({
    training_file: trainFile.id,
    model: "Qwen/Qwen3-8B",
    lora: true,
  });
  console.log(job.id);
  ```

  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3-8B" \
    --lora
  ```
</CodeGroup>

For details on every available parameter, see the [API reference](/reference/cli/finetune).

## Watch and deploy

Reasoning jobs use the same lifecycle as text jobs:

* [Poll the job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) with the SDK or CLI. Expect 10 to 30 minutes for a LoRA job on an 8B model with a few thousand examples.
* Deploy the result on a [dedicated endpoint](/docs/fine-tuning/deployment).
* Call the endpoint with the same chat-completions shape. The model emits `reasoning_content` alongside `content` for clients that surface it. See [Inference → Reasoning](/docs/inference/chat/reasoning) for details.
