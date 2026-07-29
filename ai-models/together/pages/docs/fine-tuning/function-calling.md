---
title: "Function-calling fine-tuning"
source: https://docs.together.ai/docs/fine-tuning/function-calling
path: docs/fine-tuning/function-calling
---

Train a model to invoke tools and structured functions reliably.

Function-calling fine-tuning adapts a model to invoke tools in response to user queries. The result is a model that produces well-formed `tool_calls` with high reliability, useful for agents and any pipeline that depends on structured function invocation.

This page covers the function-calling data shape, supported models, and launch parameters.

## Supported models

The following models support function-calling fine-tuning. See [supported models](/docs/fine-tuning/supported-models) for context lengths and batch limits.

<Accordion title="Supported models">
  | Organization | Model                                              | API ID                                               |
  | ------------ | -------------------------------------------------- | ---------------------------------------------------- |
  | NVIDIA       | NVIDIA Nemotron 3 Nano Omni 30B A3B Reasoning BF16 | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` |
  | NVIDIA       | NVIDIA Nemotron 3 Super 120B A12B BF16             | `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`      |
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
  | Moonshot AI  | Kimi K2.7 Code                                     | `moonshotai/Kimi-K2.7-Code`                          |
  | Moonshot AI  | Kimi K2.6                                          | `moonshotai/Kimi-K2.6`                               |
  | Z.ai         | GLM 5.1                                            | `zai-org/GLM-5.1`                                    |
  | OpenAI       | GPT-OSS 20B                                        | `openai/gpt-oss-20b`                                 |
  | OpenAI       | GPT-OSS 120B                                       | `openai/gpt-oss-120b`                                |
  | Meta         | Llama 4 Scout 17B 16E Instruct                     | `meta-llama/Llama-4-Scout-17B-16E-Instruct`          |
  | Meta         | Llama 4 Scout 17B 16E Instruct VLM                 | `meta-llama/Llama-4-Scout-17B-16E-Instruct-VLM`      |
  | Meta         | Llama 4 Maverick 17B 128E Instruct                 | `meta-llama/Llama-4-Maverick-17B-128E-Instruct`      |
  | Meta         | Llama 4 Maverick 17B 128E Instruct VLM             | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-VLM`  |
  | Meta         | Llama 3.3 70B Instruct Reference                   | `meta-llama/Llama-3.3-70B-Instruct-Reference`        |
  | Meta         | Meta Llama 3.1 8B Instruct Reference               | `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference`    |
  | Google       | Gemma 4 31B IT                                     | `google/gemma-4-31B-it`                              |
  | Google       | Gemma 4 31B IT VLM                                 | `google/gemma-4-31B-it-VLM`                          |
  | Google       | Gemma 4 26B A4B IT                                 | `google/gemma-4-26B-A4B-it`                          |
</Accordion>

## Prepare your data

Prepare data in a JSONL file. Each line should carry:

* `messages`: The conversation. Assistant messages can include `tool_calls` (a list of structured invocation objects) in place of `content`. Tool results come back via messages with the `tool` role.
* `tools`: A list of available tools for the example.

### Conversational format

```json theme={null}
{
  "messages": [
    {"role": "system", "content": "You are a helpful travel planning assistant."},
    {"role": "user", "content": "What is the current temperature in San Francisco?"},
    {
      "role": "assistant",
      "tool_calls": [
        {
          "id": "call_abc123",
          "type": "function",
          "function": {
            "name": "getCurrentWeather",
            "arguments": "{\"location\": \"San Francisco, CA\"}"
          }
        }
      ]
    },
    {"role": "tool", "content": "{\"location\": \"San Francisco\", \"temperature\": \"65\", \"unit\": \"fahrenheit\"}"}
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "getCurrentWeather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA."}
          },
          "required": ["location"]
        }
      }
    }
  ]
}
```

### Preference format

For preference fine-tuning, the `tools` array nests inside `input`. See [Preference tuning](/docs/fine-tuning/preference-tuning) for the broader DPO workflow.

```json theme={null}
{
  "input": {
    "messages": [
      {"role": "system", "content": "You are a helpful travel planning assistant."},
      {"role": "user", "content": "What is the current temperature in San Francisco?"}
    ],
    "tools": [
      {"type": "function", "function": {
        "name": "getCurrentWeather",
        "description": "Get the current weather in a given location",
        "parameters": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}
      }}
    ]
  },
  "preferred_output": [
    {"role": "assistant", "tool_calls": [
      {"id": "call_abc123", "type": "function", "function": {
        "name": "getCurrentWeather", "arguments": "{\"location\": \"San Francisco, CA\"}"
      }}
    ]}
  ],
  "non_preferred_output": [
    {"role": "assistant", "content": "Sorry, I can't help you with that."}
  ]
}
```

## Validate and upload

Upload your data using the Together Python/TypeScript SDK or the [Together CLI](/reference/cli/getting-started):

<CodeGroup>
  ```bash CLI theme={null}
  tg files check "function_calling_dataset.jsonl"
  tg files upload "function_calling_dataset.jsonl"
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  train_file = client.files.upload(
      file="function_calling_dataset.jsonl",
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
    file: fs.createReadStream("function_calling_dataset.jsonl"),
    purpose: "fine-tune",
  });
  console.log(trainFile.id);
  ```
</CodeGroup>

## Launch the job

LoRA is the default and recommended training mode. Pass `lora=False` for full fine-tuning.

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

For details on all available parameters, see the [API reference](/reference/cli/finetune).

## Watch and deploy

Function-calling jobs use the same lifecycle as text jobs:

* [Poll the job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) with the SDK or CLI. Expect 10 to 30 minutes for a LoRA job on an 8B model with a few thousand examples.
* Deploy the result on a [dedicated endpoint](/docs/fine-tuning/deployment) and call it with the same [function-calling request shape](/docs/inference/function-calling/overview) as the base model.
