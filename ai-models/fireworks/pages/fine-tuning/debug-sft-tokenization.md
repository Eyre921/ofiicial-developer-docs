---
title: "Debug SFT tokenization"
source: https://docs.fireworks.ai/fine-tuning/debug-sft-tokenization
path: fine-tuning/debug-sft-tokenization
---

Download rendered token IDs and loss masks for supervised fine-tuning jobs.

When supervised fine-tuning quality looks wrong, first check what the trainer actually saw. Fireworks can attach a **Render Samples** download to supervised fine-tuning job details. The file is a JSONL sample of records after Fireworks applies the model's chat template, tokenizer, and training mask.

Use render samples to answer questions such as:

* Did `system`, `user`, `assistant`, and tool messages render with the expected special tokens?
* Are only the intended assistant tokens included in the loss?
* Did a message-level `weight: 0` or sample-level `weight` remove the tokens you expected?
* Does Fireworks' tokenizer output match the tokenizer behavior you tested locally?

<Note>
  The render samples file is a diagnostic sample, not a full dataset export. New supervised fine-tuning jobs capture up to 20 rendered records by default. Older jobs, jobs that fail before rendering, or jobs without captured samples may not show the download.
</Note>

## Download render samples

<Steps>
  <Step title="Open the supervised fine-tuning job">
    Go to the [Fireworks dashboard](https://app.fireworks.ai/dashboard/fine-tuning), then open the supervised fine-tuning job you want to inspect.
  </Step>

  <Step title="Find the Render Samples row">
    In the job details sidebar, look for **Render Samples**.
  </Step>

  <Step title="Download the JSONL file">
    Click **Download**. Each line in the downloaded file is one rendered training record.
  </Step>
</Steps>

<Warning>
  Render samples can contain text from your training dataset in `decoded_tokens`. Treat the downloaded file like training data and do not share it publicly.
</Warning>

## Understand the JSONL fields

A render sample record looks like this:

```json theme={null}
{
  "source_jsonl_row_index": 4,
  "source_jsonl_line_number": 5,
  "split_index": 0,
  "worker_id": 2,
  "renderer": "qwen3",
  "train_on_what": "all_assistant_messages",
  "token_ids": [10, 11, 12],
  "decoded_tokens": ["<|im_start|>", "assistant", "Hello"],
  "token_weights": [0.0, 0.0, 1.0],
  "training_target_token_ids": [11, 12],
  "training_loss_weights": [0.0, 1.0]
}
```

| Field                       | Meaning                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `source_jsonl_row_index`    | Zero-based index of the source dataset row.                                                                 |
| `source_jsonl_line_number`  | One-based source line number, useful for opening the row in an editor.                                      |
| `split_index`               | Index of the rendered record produced from that source row. Most rows produce one record.                   |
| `renderer`                  | Chat template renderer selected for the base model.                                                         |
| `train_on_what`             | Which message content is configured to contribute to training loss.                                         |
| `token_ids`                 | Full rendered token sequence before the next-token shift.                                                   |
| `decoded_tokens`            | One-token decode for each token ID. Tokenizers may show whitespace markers or byte fallback pieces.         |
| `token_weights`             | Per-token training weight in rendered order. `0` means context only; a positive value contributes to loss.  |
| `training_target_token_ids` | Shifted next-token targets passed to the trainer. This array is usually one shorter than `token_ids`.       |
| `training_loss_weights`     | Loss weights aligned with `training_target_token_ids`. A positive value means that target token is trained. |

<Note>
  In the REST response, the render preview identifies each datum produced from a source row with `examples[].renderings[].renderedDatums[].datumIndex`. Downloaded **Render Samples** use the legacy `split_index` field shown above. The fields play corresponding roles in different schemas; `split_index` has not been renamed in the downloadable artifact.
</Note>

For quick inspection, `token_ids`, `decoded_tokens`, and `token_weights` are the easiest fields to scan. For exact trainer behavior, use `training_target_token_ids` and `training_loss_weights`; those are shifted for next-token prediction.

## Inspect a downloaded file

Use this local script to print each rendered token with its training status:

```python theme={null}
import json
from pathlib import Path

for line in Path("render_samples.jsonl").read_text().splitlines():
    record = json.loads(line)
    print(
        f"\nsource line {record['source_jsonl_line_number']} "
        f"split {record['split_index']} "
        f"renderer={record['renderer']} "
        f"train_on={record['train_on_what']}"
    )
    for index, (token_id, text, weight) in enumerate(
        zip(record["token_ids"], record["decoded_tokens"], record["token_weights"])
    ):
        status = "TRAIN" if float(weight) > 0 else "ctx"
        print(f"{index:04d} {int(token_id):8d} {float(weight):g} {status:5s} {text!r}")
```

Then compare the reported `source_jsonl_line_number` with the original dataset row:

```bash theme={null}
sed -n '5p' train.jsonl
```

Replace `5` with the line number from the render sample.

## Common findings

| What you see                                        | Likely cause                                                                                                                                                                                                                         | What to do                                                                                                                                                   |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Assistant answer tokens have `token_weights` of `0` | The assistant message has `weight: 0`, the sample has zero weight, or the job is configured to train on different content.                                                                                                           | Check the original JSONL row and remove unintended weights.                                                                                                  |
| User or system tokens have positive `token_weights` | The row schema or training configuration is not representing roles as intended.                                                                                                                                                      | Verify every message has the correct `role`, and avoid putting assistant text in a `user` message.                                                           |
| Expected text is missing from `decoded_tokens`      | The source row may have been split, truncated, or rendered differently by the model chat template.                                                                                                                                   | Check `split_index`, source line number, and the job's max context length.                                                                                   |
| Extra special tokens appear around messages         | The selected model renderer is adding chat template markers.                                                                                                                                                                         | This is often expected. If the markers are wrong for your use case, check that the base model and dataset format match.                                      |
| Thinking traces missing from conversation history   | The job's thinking-history mode and model renderer decide whether earlier turns' `reasoning_content` is retained. Interleaved removes thinking across user-turn boundaries; Preserved retains it. Datum unrolling is model-specific. | Compare the available modes in the render preview, then verify the created job's mode. See [Thinking history in fine-tuning](/fine-tuning/thinking-history). |
| Token boundaries look surprising                    | Many tokenizers encode whitespace, Unicode, and byte fallback pieces in non-obvious ways.                                                                                                                                            | Compare with the same Hugging Face tokenizer using `skip_special_tokens=False`.                                                                              |
| The Render Samples row is missing                   | The job may predate this feature, may have failed before rendering, or may not have captured samples.                                                                                                                                | Create a new supervised fine-tuning job, or contact support with the job ID if the job should have rendered samples.                                         |

## Compare with a local tokenizer

If you have access to the matching Hugging Face tokenizer, compare Fireworks' rendered tokens with local tokenizer output:

```python theme={null}
import json
from pathlib import Path
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("<HF_TOKENIZER_OR_LOCAL_PATH>", trust_remote_code=True)
record = json.loads(Path("render_samples.jsonl").read_text().splitlines()[0])

print(tokenizer.decode(record["token_ids"], skip_special_tokens=False))
```

The local decode should help explain token boundaries and special tokens. If local tokenization differs, confirm that you are using the same tokenizer family and revision as the base model selected for fine-tuning.
