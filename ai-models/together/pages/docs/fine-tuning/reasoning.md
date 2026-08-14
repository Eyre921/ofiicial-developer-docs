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

The following models support reasoning fine-tuning. See [supported models](/docs/fine-tuning/supported-models) for context lengths and batch limits.

<Accordion title="Supported models">
  | Organization | Model                                              | API ID                                               |
  | ------------ | -------------------------------------------------- | ---------------------------------------------------- |
  | DeepSeek     | DeepSeek V4 Flash 0731                             | `deepseek-ai/DeepSeek-V4-Flash-0731`                 |
  | DeepSeek     | DeepSeek V4 Flash                                  | `deepseek-ai/DeepSeek-V4-Flash`                      |
  | NVIDIA       | NVIDIA Nemotron 3 Nano Omni 30B A3B Reasoning BF16 | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` |
  | Qwen         | Qwen3.5 397B A17B                                  | `Qwen/Qwen3.5-397B-A17B`                             |
  | Qwen         | Qwen3.5 122B A10B                                  | `Qwen/Qwen3.5-122B-A10B`                             |
  | Qwen         | Qwen3.5 35B A3B                                    | `Qwen/Qwen3.5-35B-A3B`                               |
  | Qwen         | Qwen3.5 35B A3B Base                               | `Qwen/Qwen3.5-35B-A3B-Base`                          |
  | Qwen         | Qwen3.5 27B                                        | `Qwen/Qwen3.5-27B`                                   |
  | Qwen         | Qwen3.5 9B                                         | `Qwen/Qwen3.5-9B`                                    |
  | Qwen         | Qwen3.5 4B                                         | `Qwen/Qwen3.5-4B`                                    |
  | Qwen         | Qwen3.5 2B                                         | `Qwen/Qwen3.5-2B`                                    |
  | Qwen         | Qwen3.5 0.8B                                       | `Qwen/Qwen3.5-0.8B`                                  |
  | Qwen         | Qwen3.6 35B A3B                                    | `Qwen/Qwen3.6-35B-A3B`                               |
  | Qwen         | Qwen3.6 27B                                        | `Qwen/Qwen3.6-27B`                                   |
  | Z.ai         | GLM 5.1                                            | `zai-org/GLM-5.1`                                    |
  | Z.ai         | GLM 5.2                                            | `zai-org/GLM-5.2`                                    |
  | OpenAI       | GPT-OSS 20B                                        | `openai/gpt-oss-20b`                                 |
  | OpenAI       | GPT-OSS 120B                                       | `openai/gpt-oss-120b`                                |
  | Google       | Gemma 4 31B IT                                     | `google/gemma-4-31B-it`                              |
  | Google       | Gemma 4 31B IT VLM                                 | `google/gemma-4-31B-it-VLM`                          |
  | Google       | Gemma 4 26B A4B IT                                 | `google/gemma-4-26B-A4B-it`                          |
</Accordion>

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
  ```bash CLI theme={null}
  tg files check "reasoning_dataset.jsonl"
  tg files upload "reasoning_dataset.jsonl"
  ```

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
</CodeGroup>

## Launch the job

LoRA is the default. Pass `lora=False` for full fine-tuning.

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3-8B" \
    --lora
  ```

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
</CodeGroup>

For details on every available parameter, see the [API reference](/reference/cli/finetune).

## Watch and deploy

Reasoning jobs use the same lifecycle as text jobs:

* [Poll the job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) with the SDK or CLI. Expect 10 to 30 minutes for a LoRA job on an 8B model with a few thousand examples.
* Deploy the result on a [dedicated endpoint](/docs/fine-tuning/deployment).
* Call the endpoint with the same chat-completions shape. The model emits `reasoning_content` alongside `content` for clients that surface it. See [Inference → Reasoning](/docs/inference/chat/reasoning) for details.
