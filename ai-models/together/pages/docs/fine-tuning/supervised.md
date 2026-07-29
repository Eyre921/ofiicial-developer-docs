---
title: "Supervised fine-tuning"
source: https://docs.together.ai/docs/fine-tuning/supervised
path: docs/fine-tuning/supervised
---

Train a model on demonstration data with supervised fine-tuning (SFT).

Supervised fine-tuning (SFT) trains a model on demonstration data: examples that pair an input with the exact completion you want the model to produce. It's the default training method on Together AI and the right starting point for most use cases. To train on ranked pairs of good and bad responses instead, see [preference fine-tuning](/docs/fine-tuning/preference-tuning).

Both methods share the same job lifecycle. See the [fine-tuning quickstart](/docs/fine-tuning/quickstart) for the complete flow, including data upload and evaluation.

## When to use supervised fine-tuning

Use SFT when:

* **You have demonstrations of the target behavior.** Each example shows one correct completion for an input, which is the standard format for instruction and conversational data.
* **You want to teach a new task, style, or format.** SFT shifts the model toward the patterns in your training data.
* **You're starting a new fine-tune.** SFT should be your foundation for most use cases. If you later need to align the model against ranked outputs, run [DPO](/docs/fine-tuning/preference-tuning) on top of the SFT checkpoint.

If your input dataset is made up of paired preferred and dispreferred responses for the same input, you can start with [preference fine-tuning](/docs/fine-tuning/preference-tuning) instead.

## Prepare your data

SFT accepts conversational, instruction, and general text formats. Each line carries a single target completion. See [data preparation](/docs/fine-tuning/data-preparation) for the schema and packing instructions for each format.

## Launch a fine-tuning job

Pass a training file and a base model. SFT is the default `training_method`, so you don't need to set it. Here's the minimum code to start a supervised fine-tuning job:

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3.5-9B"
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="Qwen/Qwen3.5-9B",
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "Qwen/Qwen3.5-9B",
  });
  console.log(job.id);
  ```
</CodeGroup>

## Key parameters

These are the parameters you'll reach for most often. The full list lives in the [fine-tuning API reference](/reference/post-fine-tunes).

| Parameter         | Default   | Description                                                                                                                                         |
| ----------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `n_epochs`        | `1`       | Number of passes over the dataset. Range is 1 to 20.                                                                                                |
| `learning_rate`   | `0.00001` | Learning rate multiplier.                                                                                                                           |
| `batch_size`      | `max`     | Per-iteration batch size. See [supported models](/docs/fine-tuning/supported-models) for the min and max per model.                                 |
| `train_on_inputs` | `auto`    | Whether to compute loss on the input tokens. `auto` masks inputs for conversational and instruction data, and trains on them for general text data. |
| `validation_file` | none      | A held-out file to evaluate against during training. Required when `n_evals > 0`.                                                                   |
| `suffix`          | none      | Up to 40 characters appended to the output model name to tell your fine-tunes apart.                                                                |

To stop a run automatically when validation loss plateaus, see [early stopping](/docs/fine-tuning/early-stopping).

## Choose LoRA or full fine-tuning

SFT runs as either LoRA (the default) or full fine-tuning. That choice is independent of the training method and affects cost, batch size, and how you deploy the result. See [LoRA vs. full fine-tuning](/docs/fine-tuning/lora-vs-full) to decide and to configure LoRA's rank and target modules.

## Next steps

<CardGroup>
  <Card title="Track training" icon="chart-line" href="/docs/fine-tuning/monitoring">
    Retrieve per-step loss, learning rate, and evaluation metrics.
  </Card>

  <Card title="Deploy your model" icon="server" href="/docs/fine-tuning/deployment">
    Serve the result on a dedicated endpoint or download the weights.
  </Card>

  <Card title="Continue with DPO" icon="scale" href="/docs/fine-tuning/preference-tuning">
    Continue training the SFT checkpoint with DPO to align it against ranked outputs.
  </Card>
</CardGroup>
