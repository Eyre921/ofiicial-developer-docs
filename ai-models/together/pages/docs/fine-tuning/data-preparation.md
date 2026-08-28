---
title: "Data preparation"
source: https://docs.together.ai/docs/fine-tuning/data-preparation
path: docs/fine-tuning/data-preparation
---

Format your training file as JSONL or Parquet to match your task, then validate and upload.

The fine-tuning API accepts two file formats: JSONL for text data and Parquet for pre-tokenized data. Pick JSONL unless you need to set custom attention masks or labels, or you want to skip tokenization to speed up repeated experiments.

The file size limit for either format is 100 GB. The file ID returned by `client.files.upload()` is what you pass as `training_file` to a fine-tuning job.

## Pick a data format

Each line of a JSONL file is one training example, formatted to match your task.

| Format                                 | When to use                                                                               | Key fields                                          |
| -------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [Conversational](#conversational-data) | Multi-turn chat or single-turn chat.                                                      | `messages`                                          |
| [Instruction](#instruction-data)       | Prompt and completion pairs.                                                              | `prompt`, `completion`                              |
| [Preference](#preference-data)         | Paired preferred and dispreferred outputs for [DPO](/docs/fine-tuning/preference-tuning). | `input`, `preferred_output`, `non_preferred_output` |
| [Generic text](#generic-text-data)     | Free-form text completion.                                                                | `text`                                              |
| [Tool-calling](#tool-calling-data)     | Training a model to invoke tools.                                                         | `messages`, `tools`                                 |
| [Reasoning](#reasoning-data)           | Chain-of-thought data for reasoning models.                                               | `messages` with `reasoning`                         |

If the same file has two possible formats (for example both `text` and `messages`), the server rejects it. Trim unused fields before upload to speed up data transfer.

### Conversational data

Conversations are represented using a `messages` array. Each message has a `role` (`system`, `user`, or `assistant`) and `content`. The conversation must start with `system` or `user` and alternate `user` and `assistant` afterwards.

```json theme={null}
{
  "messages": [
    {"role": "system", "content": "This is a system prompt."},
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you! How can I help you?"},
    {"role": "user", "content": "Can you explain machine learning?"},
    {"role": "assistant", "content": "Machine learning is..."}
  ]
}
```

By default, training computes loss only on `assistant` messages. Pass `train_on_inputs=True` to include the rest. To mask or weight individual messages, see [Data weights](#data-weights).

The dataset is automatically formatted into the model's [chat template](https://huggingface.co/docs/transformers/main/en/chat_templating) if one is defined. Instruction-tuned models always have a chat template; base models usually don't.

Example datasets:

* [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat).
* [davanstrien/cosmochat](https://huggingface.co/datasets/davanstrien/cosmochat).

### Instruction data

Each line carries a `prompt` and a `completion` field.

```json theme={null}
{"prompt": "...", "completion": "..."}
{"prompt": "...", "completion": "..."}
```

By default, training computes loss only on `completion`. Pass `train_on_inputs=True` to include `prompt`. To scale a sample's contribution to the loss, see [Data weights](#data-weights).

Example datasets:

* [meta-math/MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA).
* [glaiveai/glaive-code-assistant](https://huggingface.co/datasets/glaiveai/glaive-code-assistant).

### Generic text data

Each line carries a single `text` field. Use this for plain text completions.

```json theme={null}
{"text": "..."}
{"text": "..."}
```

Example datasets:

* [unified\_joke\_explanations.jsonl](https://huggingface.co/datasets/laion/OIG/resolve/main/unified_joke_explanations.jsonl).
* [togethercomputer/RedPajama-Data-1T-Sample](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T-Sample).

### Preference data

Used for [preference fine-tuning](/docs/fine-tuning/preference-tuning) with DPO. Each line carries:

* `input.messages`: a context in conversational format.
* `preferred_output`: a single assistant message representing the ideal response.
* `non_preferred_output`: a single assistant message representing the suboptimal response.

```json theme={null}
{
  "input": {
    "messages": [
      {"role": "assistant", "content": "Hi! I'm powered by Together AI's open-source models. Ask me anything."},
      {"role": "user", "content": "What's open-source AI?"}
    ]
  },
  "preferred_output": [
    {"role": "assistant", "content": "Open-source AI means models are free to use, modify, and share. Together AI makes it easy to fine-tune and deploy them."}
  ],
  "non_preferred_output": [
    {"role": "assistant", "content": "It means the code is public."}
  ]
}
```

Each output must contain exactly one assistant message.

### Tool-calling data

For training a model to invoke tools, the line carries a `tools` array listing the available tools. Assistant messages can include `tool_calls` instead of `content`, and `tool`-role messages carry call results. See [function-calling fine-tuning](/docs/fine-tuning/function-calling) for the end-to-end workflow.

```json theme={null}
{
  "messages": [
    {"role": "user", "content": "What is the current temperature in San Francisco?"},
    {"role": "assistant", "tool_calls": [
      {"id": "call_abc123", "type": "function", "function": {
        "name": "getCurrentWeather", "arguments": "{\"location\": \"San Francisco\"}"
      }}
    ]},
    {"role": "tool", "content": "{\"temperature\":\"65\",\"unit\":\"fahrenheit\"}"}
  ],
  "tools": [
    {"type": "function", "function": {
      "name": "getCurrentWeather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA."}
        },
        "required": ["location"]
      }
    }}
  ]
}
```

For preference fine-tuning, the `tools` field nests inside `input`:

```json theme={null}
{
  "input": {
    "messages": [{"role": "user", "content": "What is the current temperature in San Francisco?"}],
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
        "name": "getCurrentWeather", "arguments": "{\"location\": \"San Francisco\"}"
      }}
    ]}
  ],
  "non_preferred_output": [
    {"role": "assistant", "content": "Sorry, I can't help you with that."}
  ]
}
```

### Reasoning data

For fine-tuning reasoning models, assistant messages support a `reasoning` or `reasoning_content` field that carries the chain of thought. See [reasoning fine-tuning](/docs/fine-tuning/reasoning) for the full workflow.

```json theme={null}
{
  "messages": [
    {"role": "user", "content": "What is the capital of France?"},
    {
      "role": "assistant",
      "reasoning": "France is in Western Europe. Its capital is Paris.",
      "content": "The capital of France is Paris."
    }
  ]
}
```

When fine-tuning reasoning models on conversational data, only the last assistant message is trained on by default. For multi-turn reasoning, split the conversation so each assistant message is the final message in its own example.

<Warning>
  Reasoning models should always be fine-tuned with reasoning data. Training without it can degrade the model's reasoning ability. If your dataset doesn't include reasoning, use an instruct model instead.
</Warning>

For preference fine-tuning, both outputs carry `reasoning`:

```json theme={null}
{
  "input": {
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
  },
  "preferred_output": [
    {"role": "assistant", "reasoning": "France is in Western Europe. Its capital is Paris.", "content": "The capital of France is Paris."}
  ],
  "non_preferred_output": [
    {"role": "assistant", "reasoning": "Let me think about European capitals.", "content": "The capital of France is Berlin."}
  ]
}
```

## Data weights

Two independent controls adjust how much each part of your data contributes to the training loss. You can use either one on its own or both together in the same file.

### Per-message weights

Set a `weight` on an individual message to control whether it contributes to the loss. Only `0` and `1` are supported: a message with `weight=0` is masked, and `weight=1` includes it. This is a finer-grained version of `train_on_inputs`, letting you mask or include specific messages rather than whole roles.

Per-message weights are only available for [conversational data](#conversational-data), since they weight individual messages.

```json theme={null}
{
  "messages": [
    {"role": "user", "content": "Question A", "weight": 0},
    {"role": "assistant", "content": "Answer A", "weight": 1}
  ]
}
```

### Sample weights

Set a root-level `weight` on a line to scale that entire sample's contribution to the loss. It's a non-negative floating-point multiplier applied to the sample's tokens, and it works with every JSONL format and training method, including instruction data.

```json theme={null}
{"prompt": "What is photosynthesis?", "completion": "Photosynthesis is...", "weight": 0.9}
{"prompt": "What is mitosis?", "completion": "Mitosis is...", "weight": 0.1}
```

### Combining weights

You can set per-message weights and a sample weight in the same conversational file. The sample weight scales the loss for the whole line, and the per-message weights determine which messages within it contribute.

```json theme={null}
{
  "messages": [
    {"role": "user", "content": "Can you explain machine learning?", "weight": 0},
    {"role": "assistant", "content": "Machine learning is...", "weight": 1}
  ],
  "weight": 0.9
}
{
  "messages": [
    {"role": "user", "content": "Can you explain why?", "weight": 0},
    {"role": "assistant", "content": "I can't", "weight": 1}
  ],
  "weight": 0.1
}
```

## Packing

For JSONL training data, Together uses [sample packing](https://huggingface.co/docs/trl/main/en/reducing_memory_usage#packing): multiple short examples are concatenated up to `max_seq_length` so each training window uses the full context length instead of being padded out. Packing is enabled by default and makes the effective batch size larger than the `batch_size` you set, which significantly reduces the total number of training steps and overall training time.

To control packing, either set the [`packing` flag](/reference/post-fine-tunes#body-packing) to `false` for JSONL input, or supply a pre-tokenized [Parquet file](#tokenized-parquet-data). The `packing` flag applies only to JSONL input; it has no effect on Parquet data.

## Tokenized (Parquet) data

Use Parquet when you want to skip tokenization on every job, customize attention masks or labels, or run with a tokenizer that differs from the base model's. The file must be `.parquet` and under 100 GB.

Allowed fields:

| Field            | Required | Description                                                                                                                   |
| ---------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `input_ids`      | Yes      | Token IDs fed to the model.                                                                                                   |
| `attention_mask` | Yes      | 1 for tokens the model should attend to, 0 for padding.                                                                       |
| `labels`         | No       | Target token IDs. Use `-100` to mask a position from the loss. Defaults to `input_ids`.                                       |
| `position_ids`   | No       | Position IDs. Reset to 0 at each example boundary inside a packed sequence and increment by 1. Padding tokens also receive 0. |

<Note>
  You don't need to shift `labels` relative to `input_ids`. The trainer shifts them internally for next-token prediction.
</Note>

Here's a worked example with the [together-py tokenize\_data.py script](https://github.com/togethercomputer/together-py/blob/main/examples/tokenize_data.py):

```bash theme={null}
# With packing (recommended)
python tokenize_data.py \
  --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" \
  --max-seq-length=32768 \
  --add-labels \
  --packing \
  --out-filename="processed_packed.parquet"

# Without packing
python tokenize_data.py \
  --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" \
  --max-seq-length=32768 \
  --add-labels \
  --out-filename="processed_padded.parquet"
```

If `--packing` is passed, the script concatenates multiple short sequences into each `max_seq_length` window to reduce wasted compute, matching the [packing](#packing) training applies by default. Otherwise, each example is padded to its own window.

Loading the resulting Parquet:

```python Python theme={null}
from datasets import load_dataset

packed = load_dataset(
    "parquet", data_files={"train": "processed_packed.parquet"}
)
padded = load_dataset(
    "parquet", data_files={"train": "processed_padded.parquet"}
)
print(packed["train"])
print(padded["train"])
```

## Validate and upload

Run a local data validation check before uploading to avoid unnecessary charges. The client-side check verifies the file is UTF-8, each non-empty line parses as JSON, the line count exceeds the minimum, and the file is under the maximum size. Full schema validation (conversation roles, tool calls, and other dataset requirements) runs on the server during ingestion after upload, and is reported through the file's `processing_status`.

<CodeGroup>
  ```bash CLI theme={null}
  tg files check "train.jsonl" --json
  tg files upload "train.jsonl"
  ```

  ```python Python theme={null}
  import json
  from together import Together
  from together.lib.utils import check_file
  from together.lib.resources import FileUploadProgress

  client = Together()

  report = check_file("train.jsonl")
  print(json.dumps(report, indent=2))
  assert report["is_check_passed"]


  def on_progress(event: FileUploadProgress) -> None:
      print(f"{event.uploaded_bytes}/{event.total_bytes}")


  train_file = client.files.upload(
      file="train.jsonl",
      purpose="fine-tune",
      check=True,
      progress_callback=on_progress,
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
</CodeGroup>

In the Python snippet, the optional `progress_callback` receives `FileUploadProgress` events (`uploaded_bytes`, `total_bytes`) as the upload runs. Omit it to upload silently.

`check_file()` returns a report you can inspect before uploading. A passing file looks like:

```json theme={null}
{
  "is_check_passed": true,
  "message": "Checks passed",
  "found": true,
  "file_size": 23777505,
  "utf8": true,
  "line_type": true,
  "text_field": true,
  "key_value": true,
  "has_min_samples": true,
  "num_samples": 7199,
  "load_json": true,
  "load_csv": null,
  "filetype": "jsonl"
}
```

Successful upload returns a file object with an `id` field. Save the ID—you'll pass it as `training_file` to `client.fine_tuning.create()`. Before starting a job, preview how the file tokenizes with [`tg fine-tuning preview`](/reference/cli/finetune#preview). See the [quickstart](/docs/fine-tuning/quickstart) for the full fine-tuning lifecycle.

<Note>
  If you upload a file whose contents already exist on Together AI, `client.files.upload()` doesn't create a duplicate. It returns the existing file's metadata, including its `id`, so you can reuse it directly. To force a re-upload, delete the existing file first with `client.files.delete(<file_id>)`.
</Note>

### Wait for server-side validation

Upload returns before ingestion finishes, so poll the Files API until `processing_status` reaches `COMPLETED` before you use the file. If the dataset doesn't meet fine-tuning requirements, `processing_status` becomes `INVALID_FORMAT` and `validation_report.error` carries a user-facing description of the problem.

<CodeGroup>
  ```bash CLI theme={null}
  # Inspect processing_status and validation_report
  tg files retrieve <file_id>
  ```

  ```python Python theme={null}
  import time
  from together import Together

  client = Together()

  while True:
      meta = client.files.retrieve(train_file.id)
      if meta.processing_status == "COMPLETED":
          break
      if meta.processing_status == "INVALID_FORMAT":
          # validation_report.error carries a user-facing reason.
          raise ValueError(
              f"file is not valid for fine-tuning: {meta.validation_report}"
          )
      if meta.processing_status == "FAILED":
          raise RuntimeError(
              f"file processing did not complete: {meta.processing_status}"
          )
      time.sleep(5)
  ```
</CodeGroup>

The exact `validation_report` schema may evolve, so treat `processing_status` as the authoritative readiness signal.

## Split into train and validation

To carve a validation set out of a single JSONL file:

```bash theme={null}
split_ratio=0.9
total=$(wc -l < train_full.jsonl)
split_lines=$((total * split_ratio / 1))

head -n $split_lines train_full.jsonl > train.jsonl
tail -n +$((split_lines + 1)) train_full.jsonl > validation.jsonl
```

Then pass both files to the job and set `n_evals` above 0:

```python Python theme={null}
job = client.fine_tuning.create(
    training_file="<TRAIN_FILE_ID>",
    validation_file="<VALIDATION_FILE_ID>",
    n_evals=10,
    model="Qwen/Qwen3-8B",
)
```

The model evaluates against the validation set at the specified intervals. Eval loss appears in the [training metrics](/docs/fine-tuning/monitoring) and (if `wandb_api_key` is set) on your W\&B dashboard.
