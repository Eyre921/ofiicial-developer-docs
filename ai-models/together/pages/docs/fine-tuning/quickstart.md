---
title: "Fine-tuning quickstart"
source: https://docs.together.ai/docs/fine-tuning/quickstart
path: docs/fine-tuning/quickstart
---

Prepare a conversational dataset, launch a LoRA job on Qwen3.5 9B, and evaluate the fine-tuned model.

<Tip>
  Using a coding agent? Install the [together-fine-tuning](https://github.com/togethercomputer/skills/tree/main/skills/together-fine-tuning) skill so your agent writes correct fine-tuning code automatically. See [Coding agent setup](/docs/agent-skills) for the install flow.
</Tip>

This quickstart walks through a full fine-tuning lifecycle. You'll prepare a conversational dataset (CoQA), upload it, launch a LoRA job on Qwen3.5 9B, watch it complete, deploy the result, and compare it to the base model. End-to-end runtime is roughly 20 to 40 minutes for the example dataset.

For background on what fine-tuning is and when to use it, see the [overview](/docs/fine-tuning/overview). You can find a runnable notebook for this tutorial [on GitHub](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb).

## Prerequisites

Before you begin, make sure you have:

* [A Together AI account and API key](https://api.together.ai/settings/projects/~first/api-keys).
* [The Together CLI](/reference/cli/getting-started) or the [Python / TypeScript SDK](/docs/quickstart) installed.
* Python install, with [`datasets`](https://huggingface.co/docs/datasets), [`transformers`](https://huggingface.co/docs/transformers), and [`tqdm`](https://tqdm.github.io/) if you want to follow the data-prep step verbatim:

```bash theme={null}
pip install -U together datasets transformers tqdm
```

Make sure to export your API key before you begin:

```shellscript theme={null}
export TOGETHER_API_KEY=<your_key>
```

## Step 1: Prepare your dataset

This quickstart uses the CoQA conversational dataset. Together AI supports four text data formats: [conversational](/docs/fine-tuning/data-preparation#conversational-data), [instruction](/docs/fine-tuning/data-preparation#instruction-data), [preference](/docs/fine-tuning/data-preparation#preference-data), and [generic text](/docs/fine-tuning/data-preparation#generic-text-data). JSONL is the default file format, but you can use Parquet for pre-tokenized data and custom loss masking.

Transform CoQA into the conversational shape:

```python Python theme={null}
from datasets import load_dataset

coqa = load_dataset("stanfordnlp/coqa")

system_prompt = (
    "Read the story and extract answers for the questions.\nStory: {}"
)


def map_fields(row):
    messages = [
        {"role": "system", "content": system_prompt.format(row["story"])}
    ]
    for q, a in zip(row["questions"], row["answers"]["input_text"]):
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})
    return {"messages": messages}


train = coqa["train"].map(
    map_fields, remove_columns=coqa["train"].column_names
)
train.to_json("coqa_train.jsonl")
```

<Tip>
  To train the model on only part of each example (for instance, the assistant turns but not the user turns), you can use [loss masking](/reference/post-fine-tunes#body-train-on-inputs) or [data weights](/docs/fine-tuning/data-preparation#data-weights).
</Tip>

Next we'll upload the file. `files.upload()` runs a local structural check by default (`check=True`), catching basic formatting errors such as non-UTF-8 encoding or malformed JSON lines before the file is sent. To inspect the check report yourself before uploading, run `check_file()` first (see [Data preparation](/docs/fine-tuning/data-preparation#validate-and-upload) for details):

<CodeGroup>
  ```bash CLI theme={null}
  tg files upload "coqa_train.jsonl"
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  train_file = client.files.upload(
      file="coqa_train.jsonl",
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
    file: fs.createReadStream("coqa_train.jsonl"),
    purpose: "fine-tune",
  });
  console.log(trainFile.id);
  ```
</CodeGroup>

<Tip>
  For very large files, you can skip the local check with `check=False` to speed up the upload. After upload, the server validates the full schema (conversation roles, tool calls, and other dataset requirements) during ingestion, reported through the file's `processing_status`.
</Tip>

To see files you've already uploaded, list them with `client.files.list()` (`tg files list`).

<Note>
  If you upload a file whose contents already exist on Together AI, `client.files.upload()` doesn't create a duplicate. It returns the existing file's metadata, including its `id`, so you can reuse it directly. To force a re-upload, delete the existing file first with `client.files.delete(<file_id>)`.
</Note>

Upload returns before ingestion finishes, so poll the Files API until `processing_status` reaches `COMPLETED` before launching the job. If validation rejects the dataset, `processing_status` becomes `INVALID_FORMAT` and `validation_report.error` carries the reason.

```python Python theme={null}
import time

while True:
    meta = client.files.retrieve(train_file.id)
    if meta.processing_status == "COMPLETED":
        break
    if meta.processing_status == "INVALID_FORMAT":
        raise ValueError(
            f"file is not valid for fine-tuning: {meta.validation_report}"
        )
    if meta.processing_status == "FAILED":
        raise RuntimeError(
            f"file processing did not complete: {meta.processing_status}"
        )
    time.sleep(5)
```

Once processing finishes, the file metadata reflects the outcome. A successful validation (`processing_status: COMPLETED`):

```json theme={null}
{
  "processing_status": "COMPLETED",
  "validation_report": {
    "valid": true,
    "dataset_format": "conversation",
    "nlines": 7199
  }
}
```

A user-correctable failure (`processing_status: INVALID_FORMAT`):

```json theme={null}
{
  "processing_status": "INVALID_FORMAT",
  "validation_report": {
    "valid": false,
    "error_type": "INVALID_FORMAT",
    "error": "Line 7: `messages[1]` must contain a `role` field"
  }
}
```

Save the `id` from the upload response. You'll pass it as `training_file` in the next step.

## Step 2: Launch the job

`client.fine_tuning.create()` starts a LoRA job by default. The example below tunes Qwen3.5 9B for three epochs. See the [API reference](/reference/cli/finetune) for the full list of parameters.

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3.5-9B" \
    --train-on-inputs auto \
    --lora \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --learning-rate 1e-5 \
    --suffix "qwen35_9b_demo"
  ```

  ```python Python theme={null}
  job = client.fine_tuning.create(
      training_file=train_file.id,
      model="Qwen/Qwen3.5-9B",
      n_epochs=3,
      n_checkpoints=1,
      learning_rate=1e-5,
      warmup_ratio=0,
      train_on_inputs="auto",
      lora=True,
      suffix="qwen35_9b_demo",
      # wandb_api_key=os.environ.get("WANDB_API_KEY"),  # optional
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  const job = await client.fineTuning.create({
    training_file: trainFile.id,
    model: "Qwen/Qwen3.5-9B",
    n_epochs: 3,
    n_checkpoints: 1,
    learning_rate: 1e-5,
    warmup_ratio: 0,
    train_on_inputs: "auto",
    lora: true,
    suffix: "qwen35_9b_demo",
  });
  console.log(job.id);
  ```
</CodeGroup>

Response:

```text theme={null}
ft-d1522ffb-8f3e-4106-9774-aed81e0164a4
```

Save the job ID.

<Accordion title="Job parameters">
  Here are some common job parameters:

  | Parameter         | Required | Default   | Notes                                                                                                                                                                                                                |
  | ----------------- | -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `training_file`   | Required | n/a       | File ID from Step 1.                                                                                                                                                                                                 |
  | `model`           | Required | n/a       | Base model to fine-tune.                                                                                                                                                                                             |
  | `lora`            | Optional | `true`    | Set `false` for full fine-tuning.                                                                                                                                                                                    |
  | `n_epochs`        | Optional | `1`       | Passes through the training set.                                                                                                                                                                                     |
  | `learning_rate`   | Optional | `0.00001` | Step size.                                                                                                                                                                                                           |
  | `batch_size`      | Optional | `"max"`   | Examples per optimization step. With [packing](/docs/fine-tuning/data-preparation#packing) enabled (the default for JSONL), a step can cover several short examples, so this isn't the same as JSONL lines per step. |
  | `warmup_ratio`    | Optional | `0.0`     | Fraction of steps for LR warmup.                                                                                                                                                                                     |
  | `weight_decay`    | Optional | `0.0`     | L2 regularization.                                                                                                                                                                                                   |
  | `max_grad_norm`   | Optional | `1.0`     | Gradient-clipping threshold. Set to `0` to disable clipping.                                                                                                                                                         |
  | `train_on_inputs` | Optional | `"auto"`  | Mask user or prompt tokens from the loss.                                                                                                                                                                            |
  | `suffix`          | Optional | n/a       | Up to 64 characters appended to the output model name.                                                                                                                                                               |
  | `n_checkpoints`   | Optional | `1`       | Intermediate checkpoints saved during training.                                                                                                                                                                      |
  | `n_evals`         | Optional | `0`       | Evaluations against `validation_file` during training.                                                                                                                                                               |
  | `hf_api_token`    | Optional | n/a       | Only required for a private Hugging Face base. Omit otherwise.                                                                                                                                                       |

  See the [API reference](/reference/post-fine-tunes) for the full list of parameters.
</Accordion>

<Warning>
  Each `fine_tuning.create()` call starts a new billed job. If you get a retryable error, run `client.fine_tuning.list()` first to make sure you aren't launching a duplicate.
</Warning>

## Step 3: Watch the job complete

Jobs move through these states: `pending → queued → running → uploading → completed`. Queue wait time is typically under an hour. Once running, multiply the first epoch's duration by `n_epochs` to estimate the time remaining.

Poll for completion (or error/cancellation), then read the Model Object ID:

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning retrieve "<JOB_ID>"

  # Sample events
  tg fine-tuning list-events "<JOB_ID>"
  ```

  ```python Python theme={null}
  import time

  job_id = job.id
  deadline = time.time() + 6 * 60 * 60  # safety cap: 6 hours

  while True:
      status = client.fine_tuning.retrieve(id=job_id)
      print(status.status)
      if status.status in ("completed", "error", "cancelled"):
          break
      if time.time() > deadline:
          raise TimeoutError(f"Job still {status.status} after 6 hours")
      time.sleep(60)

  if status.status != "completed":
      raise RuntimeError(f"Job ended with status: {status.status}")

  # Model Object ID (ml_...); deploy references this, not the output name.
  model_object_id = status.api_model_object_id
  print(model_object_id)
  ```

  ```typescript TypeScript theme={null}
  const deadline = Date.now() + 6 * 60 * 60 * 1000;
  const terminal = new Set(["completed", "error", "cancelled"]);

  let status = await client.fineTuning.retrieve(job.id);
  while (!terminal.has(status.status)) {
    if (Date.now() > deadline) {
      throw new Error(`Job still ${status.status} after 6 hours`);
    }
    await new Promise((r) => setTimeout(r, 60000));
    status = await client.fineTuning.retrieve(job.id);
    console.log(status.status);
  }

  if (status.status !== "completed") {
    throw new Error(`Job ended with status: ${status.status}`);
  }

  // Model Object ID (ml_...); deploy references this, not the output name.
  const modelObjectId = status.model_object_id;
  console.log(modelObjectId);
  ```
</CodeGroup>

Here's a sample event log:

```text theme={null}
Fine tune request created
Job started at 2026-04-03T03:19:46Z
Model data downloaded at 2026-04-03T03:19:48Z
WandB run initialized.
Training started for Qwen/Qwen3.5-9B
Epoch completed, at step 24
Epoch completed, at step 48
Epoch completed, at step 72
Training completed for Qwen/Qwen3.5-9B at 2026-04-03T03:27:55Z
Uploading output model
Model upload complete
Job finished at 2026-04-03T03:31:33Z
```

You can also monitor the run on the [fine-tuning jobs dashboard](https://api.together.ai/jobs). For per-step loss curves, see [training metrics](/docs/fine-tuning/monitoring).

## Step 4: Deploy and call your model

Fine-tuned models run on Together AI through [dedicated model inference](/docs/fine-tuning/deployment). A completed job is already a private model in your project, so there's no upload step: you deploy it with the `tg beta` CLI by its Model Object ID (`model_object_id`, the `ml_...` value from Step 3). The deploy commands require Together CLI version `2.24.0` or later.

The CLI's `deploy` command creates the endpoint, attaches a deployment, and routes all traffic to it in one step. Then poll until the deployment reaches `DEPLOYMENT_STATE_READY`:

```bash CLI theme={null}
# Deploy the fine-tuned model to a new endpoint
tg beta endpoints deploy "<MODEL_OBJECT_ID>" \
  --endpoint qwen-finetune

# Poll until the deployment reaches DEPLOYMENT_STATE_READY
# (pass the endpoint ID from the deploy output)
tg beta endpoints get "<ENDPOINT_ID>"
```

The SDK has no single-call equivalent, so it runs the same steps individually, referencing the fine-tune by its Model Object ID (`ml_...`):

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  project_id = client.whoami().project_id

  # Reference the fine-tune by its Model Object ID (ml_...) and a config
  # for the base model. List configs: tg beta models configs <model>.
  model = f"projects/{project_id}/models/<MODEL_OBJECT_ID>"
  config = f"projects/{project_id}/configs/<CONFIG_ID>"

  endpoint = client.beta.endpoints.create(
      project_id=project_id,
      name="qwen-finetune",
  )
  deployment = client.beta.endpoints.deployments.create(
      endpoint.id,
      project_id=project_id,
      name="prod",
      model=model,
      config=config,
      autoscaling={"min_replicas": 1, "max_replicas": 1},
  )
  client.beta.endpoints.update(
      endpoint.id,
      project_id=project_id,
      traffic_split=[{"deployment_id": deployment.id, "weight": 1}],
  )

  # Poll until ready
  deployment = client.beta.endpoints.deployments.retrieve(
      deployment.id, project_id=project_id, endpoint_id=endpoint.id
  )
  print(endpoint.name, deployment.status.state)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();
  const { project_id: projectId } = await client.whoami();

  // Reference the fine-tune by its Model Object ID (ml_...) and a config
  // for the base model. List configs: tg beta models configs <model>.
  const model = `projects/${projectId}/models/<MODEL_OBJECT_ID>`;
  const config = `projects/${projectId}/configs/<CONFIG_ID>`;

  const endpoint = await client.beta.endpoints.create({
    projectId,
    name: "qwen-finetune",
  });
  const deployment = await client.beta.endpoints.deployments.create(
    endpoint.id,
    {
      projectId,
      name: "prod",
      model,
      config,
      autoscaling: { minReplicas: 1, maxReplicas: 1 },
    },
  );
  await client.beta.endpoints.update(endpoint.id, {
    projectId,
    trafficSplit: [{ deploymentId: deployment.id, weight: 1 }],
  });
  console.log(endpoint.name);
  ```
</CodeGroup>

Once the deployment is ready, send a request. The deploy output prints the **endpoint string** (`your-project-slug/qwen-finetune`): pass this as the `model` parameter. Point the base URL at `https://api-inference.together.ai/v1`:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  # A dedicated client for inference: this base URL serves only
  # inference, not the fine-tuning or files APIs.
  inference_client = Together(base_url="https://api-inference.together.ai/v1")

  response = inference_client.chat.completions.create(
      model="your-project-slug/qwen-finetune",
      messages=[{"role": "user", "content": "What is the capital of France?"}],
      max_tokens=128,
  )
  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  // A dedicated client for inference: this base URL serves only
  // inference, not the fine-tuning or files APIs.
  const inferenceClient = new Together({
    baseURL: "https://api-inference.together.ai/v1",
  });

  const response = await inferenceClient.chat.completions.create({
    model: "your-project-slug/qwen-finetune",
    messages: [{ role: "user", content: "What is the capital of France?" }],
    max_tokens: 128,
  });
  console.log(response.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl -s https://api-inference.together.ai/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "your-project-slug/qwen-finetune",
      "messages": [{"role": "user", "content": "What is the capital of France?"}],
      "max_tokens": 128
    }'
  ```
</CodeGroup>

When you're done, delete the endpoint and its deployment to stop billing:

```bash CLI theme={null}
tg beta endpoints rm "<ENDPOINT_ID>" --force
```

<Note>
  Pass the endpoint string (`your-project-slug/qwen-finetune`, printed by the deploy output) as the `model` parameter, not the Model Object ID. If `deploy` reports that the model has more than one deployment profile, re-run it with `--config <cr_...>`; list a model's profiles with `tg beta models configs "<MODEL_OBJECT_ID>"`.
</Note>

<Check>
  Congrats! You fine-tuned a model, deployed it to a dedicated endpoint, and ran inference end-to-end.
</Check>

## Step 5: Compare against the base model (optional)

To measure the impact of fine-tuning, run the same prompts through the base model and the fine-tuned model.

<Note>
  **Many fine-tunable base models aren't available on [serverless](/docs/serverless/models).** For example, calling `Qwen/Qwen3.5-9B` directly returns `Unable to access non-serverless model`. To compare, deploy the base on its own [dedicated endpoint](/docs/dedicated-endpoints/overview), evaluate against its endpoint string, then tear that endpoint down too. Serverless bases (those with a per-token price listed on the [models dashboard](https://api.together.ai/models)) can be called directly without deploying anything.
</Note>

This [GitHub notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb) runs an Exact Match and F1 comparison on the CoQA validation split. Here's a sample result from one run:

| Model      | EM   | F1   |
| ---------- | ---- | ---- |
| Base       | 0.01 | 0.18 |
| Fine-tuned | 0.32 | 0.41 |

## Stop the endpoint

Dedicated model inference bills per minute per running replica as long as the deployment is running. Step 4 deletes the endpoint at the end, but if you skipped that step or want to delete it later, run:

```bash theme={null}
tg beta endpoints rm "<ENDPOINT_ID>" --force
```

Find the endpoint ID by running `tg beta endpoints ls`.

## Continue from a checkpoint

Resume training from an existing job by passing `from_checkpoint`:

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<NEW_FILE_ID>" \
    --from-checkpoint "<PREVIOUS_JOB_ID>"
  ```

  ```python Python theme={null}
  job = client.fine_tuning.create(
      training_file="<NEW_FILE_ID>",
      from_checkpoint="<PREVIOUS_JOB_ID>",
  )
  ```
</CodeGroup>

`from_checkpoint` accepts the output model name, the job ID, or a specific step in the form `ft-...:{STEP_NUM}`. List available checkpoints with `tg fine-tuning list-checkpoints <JOB_ID>`.

## Next steps

<CardGroup>
  <Card title="Data preparation" icon="database" href="/docs/fine-tuning/data-preparation">
    See the full schema for conversational, instruction, preference, and tokenized data.
  </Card>

  <Card title="Supported models" icon="list" href="/docs/fine-tuning/supported-models">
    Browse base models with context lengths and batch size limits.
  </Card>

  <Card title="Preference tuning" icon="scale" href="/docs/fine-tuning/preference-tuning">
    Align a model with paired preferred and dispreferred responses.
  </Card>

  <Card title="Deploy your model" icon="server" href="/docs/fine-tuning/deployment">
    Hosting, teardown, and local inference for fine-tuned models.
  </Card>
</CardGroup>
