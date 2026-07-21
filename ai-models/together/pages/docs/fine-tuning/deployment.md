---
title: "Deploy a fine-tuned model"
source: https://docs.together.ai/docs/fine-tuning/deployment
path: docs/fine-tuning/deployment
---

Serve your fine-tuned model on a dedicated endpoint or download it for local inference.

Once a fine-tuning job completes, your model is available for inference in two ways: hosted on a dedicated endpoint at Together AI, or downloaded as a standalone checkpoint.

## Prerequisites

* A completed fine-tuning job. See the [quickstart](/docs/fine-tuning/quickstart) for the full lifecycle.
* The job's `x_model_output_name` (visible once status is `completed`). It follows the pattern `<your_account>/<base_model>:<suffix>:<job_id>`.

## Deploy on a dedicated endpoint

<Warning>
  Dedicated model inference bills per minute even when idle. Stop or delete the endpoint when you're done to avoid charges.
</Warning>

<Tabs>
  <Tab title="CLI / SDK">
    <CodeGroup>
      ```python Python theme={null}
      import os
      import time
      from together import Together

      client = Together()

      # 1. Get the output model name from the completed job
      status = client.fine_tuning.retrieve(id="<JOB_ID>")
      output_model = status.x_model_output_name

      # 2. Preflight: confirm the base can host a fine-tune.
      # A 404 means the base (often a `-Reference` model) can't be deployed.
      client.endpoints.list_hardware(model=status.model)

      # 3. Create the endpoint. Use a hardware id returned by list_hardware
      # above; the exact options depend on the base model.
      endpoint = client.endpoints.create(
          display_name="My fine-tuned endpoint",
          model=output_model,
          hardware="1x_nvidia_h100_80gb_sxm",
          autoscaling={"min_replicas": 1, "max_replicas": 1},
      )

      # 4. Poll until ready
      deadline = time.time() + 20 * 60  # safety cap: 20 minutes
      while True:
          ep = client.endpoints.retrieve(endpoint.id)
          if ep.state == "STARTED":
              break
          if ep.state in ("FAILED", "STOPPED"):
              raise RuntimeError(f"Endpoint ended with state: {ep.state}")
          if time.time() > deadline:
              raise TimeoutError(f"Endpoint still {ep.state} after 20 minutes")
          time.sleep(30)

      # 5. Send a request. Use endpoint.name (not the raw output model) as the model parameter.
      response = client.chat.completions.create(
          model=endpoint.name,
          messages=[{"role": "user", "content": "Hello!"}],
      )
      print(response.choices[0].message.content)

      # 6. Delete when done to stop billing
      client.endpoints.delete(endpoint.id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      // 1. Get the output model name from the completed job
      const status = await client.fineTuning.retrieve("<JOB_ID>");
      const outputModel = status.x_model_output_name;

      // 2. Preflight
      await client.endpoints.listHardware({ model: status.model });

      // 3. Create the endpoint
      const endpoint = await client.endpoints.create({
        display_name: "My fine-tuned endpoint",
        model: outputModel,
        hardware: "1x_nvidia_h100_80gb_sxm",
        autoscaling: { min_replicas: 1, max_replicas: 1 },
      });

      // 4. Poll until ready
      const deadline = Date.now() + 20 * 60 * 1000;
      while (true) {
        const ep = await client.endpoints.retrieve(endpoint.id);
        if (ep.state === "STARTED") break;
        if (ep.state === "FAILED" || ep.state === "STOPPED") {
          throw new Error(`Endpoint ended with state: ${ep.state}`);
        }
        if (Date.now() > deadline) {
          throw new Error("Endpoint did not start within 20 minutes");
        }
        await new Promise((r) => setTimeout(r, 30000));
      }

      // 5. Send a request
      const response = await client.chat.completions.create({
        model: endpoint.name,
        messages: [{ role: "user", content: "Hello!" }],
      });
      console.log(response.choices[0].message.content);

      // 6. Delete when done
      await client.endpoints.delete(endpoint.id);
      ```

      ```bash CLI theme={null}
      # 1. Find your job and copy the output model name
      tg fine-tuning retrieve "<JOB_ID>"

      # 2. Create the endpoint (--wait blocks until it's ready)
      tg endpoints create \
        --model "<OUTPUT_MODEL_NAME>" \
        --hardware 1x_nvidia_h100_80gb_sxm \
        --display-name "My fine-tuned endpoint" \
        --wait

      # 3. Send a request — the CLI doesn't ship a chat command, so use curl.
      curl -s https://api.together.ai/v1/chat/completions \
        -H "Authorization: Bearer $TOGETHER_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"model":"<ENDPOINT_NAME>","messages":[{"role":"user","content":"Hello!"}]}'

      # 4. Delete when done
      tg endpoints delete "<ENDPOINT_ID>"
      ```
    </CodeGroup>

    <Note>
      If endpoint creation fails immediately with "There was an issue starting your endpoint", the cause is almost always an incompatible base model. Verify with `client.endpoints.list_hardware(model=...)`; a 404 means the base (often a `-Reference` model) can't host a fine-tune. Pick a different base before retrying.
    </Note>
  </Tab>

  <Tab title="UI">
    <Steps>
      <Step title="Open the models page">
        Go to [the models dashboard](https://api.together.ai/models). Your completed fine-tuned models appear under **My Models**.
      </Step>

      <Step title="Create the endpoint">
        Select your fine-tuned model, then select **Create dedicated endpoint**.
      </Step>

      <Step title="Pick hardware">
        Choose hardware and set `min_replicas` and `max_replicas` (these set the maximum QPS the deployment can serve).
      </Step>

      <Step title="Deploy">
        Select **Deploy**. The endpoint takes up to 10 minutes to come up. You can navigate away while it provisions.
      </Step>

      <Step title="Stop when done">
        Return to the dashboard and stop the endpoint when you're not using it to halt per-minute billing.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Run locally

To run your model outside Together, download the checkpoint by job ID:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # `checkpoint` is required unless you set `checkpoint_step`.
  # Use "merged" for LoRA jobs; full fine-tunes only support "model_output_path".
  response = client.fine_tuning.content(ft_id="<JOB_ID>", checkpoint="merged")
  response.write_to_file("my-model/model.tar.zst")
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import fs from "node:fs";

  const client = new Together();

  // `checkpoint` is required unless you set `checkpoint_step`.
  // Use 'merged' for LoRA jobs; full fine-tunes only support 'model_output_path'.
  const response = await client.fineTuning.content({ ft_id: "<JOB_ID>", checkpoint: "merged" });
  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync("my-model/model.tar.zst", buffer);
  ```

  ```bash CLI theme={null}
  tg fine-tuning download "<JOB_ID>"
  ```
</CodeGroup>

### Choose a checkpoint type

The `checkpoint` parameter selects what to download. It's required for the v2 SDK's `content()` method and the `GET /v1/finetune/download` endpoint, unless you pass `checkpoint_step`, which downloads a specific intermediate step and overrides `checkpoint`. Valid values depend on how the job was trained.

| Job type       | Valid `checkpoint` values                   | What you get                                                                                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LoRA fine-tune | `merged`, `adapter`, or `model_output_path` | `merged` combines the base model and adapter into self-contained weights, the usual choice for running the model locally or uploading it elsewhere. `adapter` returns only the LoRA adapter weights, so you can load them on top of the base model yourself (for example, with PEFT or vLLM). |
| Full fine-tune | `model_output_path` only                    | The full set of trained model weights. `merged` and `adapter` return an error for full fine-tunes.                                                                                                                                                                                            |

`model_output_path` returns the raw training output directory before any merging. It works for both job types but is mainly useful for advanced workflows that need the unmodified artifacts: for LoRA jobs, prefer `merged` or `adapter`; for full fine-tunes, it's the only option.

The v1 SDK's `client.fine_tuning.download()` selects the checkpoint automatically (`merged` for LoRA jobs, `model_output_path` for full fine-tunes), so you don't pass a `checkpoint` argument there.

The output is a `.tar.zst` archive that uses [ZStandard](https://github.com/facebook/zstd) compression. On macOS, install `zstd` with Homebrew and decompress:

```bash theme={null}
brew install zstd
cd my-model
zstd -d model.tar.zst
tar -xvf model.tar
```

You should see:

```text theme={null}
tokenizer_config.json
special_tokens_map.json
pytorch_model.bin
generation_config.json
tokenizer.json
config.json
```

Load the model with Hugging Face Transformers:

```python Python theme={null}
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("./my-model")
model = AutoModelForCausalLM.from_pretrained(
    "./my-model",
    trust_remote_code=True,
).to(device)

input_ids = tokenizer.encode("Space robots are", return_tensors="pt").to(
    device
)
output = model.generate(input_ids, max_length=128, temperature=0.7)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

To download a specific checkpoint instead of the final one, pass `--checkpoint-step <STEP_NUMBER>` to `tg fine-tuning download` (or `checkpoint_step=<STEP_NUMBER>` to `client.fine_tuning.content()`). List checkpoints with `tg fine-tuning list-checkpoints <JOB_ID>`.

## Model registry object IDs

When a job uploads its output artifacts to the Together model registry alongside the primary storage write, the job and checkpoint responses include the registry object and revision IDs. Use these IDs to reference the uploaded weights in downstream workflows (for example, when binding a fine-tuned adapter to a dedicated endpoint).

The fields are omitted when the registry upload did not run or did not succeed.

### On the job

[`GET /fine-tunes/{id}`](/reference/get-fine-tunes-id) includes the final artifact IDs once the job reaches `completed`:

| Field                        | Description                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_object_id`            | Registry object ID for the final model weights (for example, `ml_…`). Present when the job produced a model artifact and the upload succeeded. |
| `model_object_revision_id`   | Registry revision ID for the final model weights (for example, `rv_…`).                                                                        |
| `adapter_object_id`          | Registry object ID for the final adapter weights on LoRA jobs.                                                                                 |
| `adapter_object_revision_id` | Registry revision ID for the final adapter weights on LoRA jobs.                                                                               |

<CodeGroup>
  ```python Python theme={null}
  job = client.fine_tuning.retrieve(id="<JOB_ID>")
  if job.model_object_id:
      print(job.model_object_id, job.model_object_revision_id)
  if job.adapter_object_id:
      print(job.adapter_object_id, job.adapter_object_revision_id)
  ```

  ```typescript TypeScript theme={null}
  const job = await client.fineTuning.retrieve("<JOB_ID>");
  if (job.model_object_id) {
    console.log(job.model_object_id, job.model_object_revision_id);
  }
  if (job.adapter_object_id) {
    console.log(job.adapter_object_id, job.adapter_object_revision_id);
  }
  ```

  ```bash CLI theme={null}
  tg fine-tuning retrieve "<JOB_ID>"
  ```
</CodeGroup>

### On checkpoints

[`GET /fine-tunes/{id}/checkpoints`](/reference/get-fine-tunes-id-checkpoint) returns the same ID pair on each checkpoint entry:

| Field                | Description                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| `object_id`          | Registry object ID for that checkpoint's artifact (for example, `ml_…`).   |
| `object_revision_id` | Registry revision ID for that checkpoint's artifact (for example, `rv_…`). |

Intermediate checkpoints carry the IDs from the upload at that step. Final model and adapter checkpoints in the list reuse the job-level IDs from the table above.

<CodeGroup>
  ```python Python theme={null}
  checkpoints = client.fine_tuning.list_checkpoints("<JOB_ID>")
  for cp in checkpoints.data:
      if cp.object_id:
          print(cp.step, cp.object_id, cp.object_revision_id)
  ```

  ```typescript TypeScript theme={null}
  const checkpoints = await client.fineTuning.listCheckpoints("<JOB_ID>");
  for (const cp of checkpoints.data) {
    if (cp.object_id) {
      console.log(cp.step, cp.object_id, cp.object_revision_id);
    }
  }
  ```

  ```bash CLI theme={null}
  tg fine-tuning list-checkpoints "<JOB_ID>"
  ```
</CodeGroup>

## Troubleshooting

* **`x_model_output_name` is empty:** The job hasn't reached `completed`. Poll status with `client.fine_tuning.retrieve(id=...)` until it's done. See [Monitor a fine-tuning job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) for the polling pattern.
* **Endpoint creation fails immediately:** Run `client.endpoints.list_hardware(model=<base_model>)`. A 404 means the base can't host a fine-tune. `-Reference` models fall into this bucket.
* **404 on inference:** Use `endpoint.name` as the `model` parameter, not the raw output model name. The endpoint name includes a unique suffix that routes traffic to your deployment.

## Next steps

<CardGroup>
  <Card title="Upload a custom model" icon="upload" href="/docs/dedicated-endpoints/custom-models">
    Upload your own model weights from outside the Together catalog.
  </Card>

  <Card title="Manage endpoints" icon="settings" href="/docs/dedicated-endpoints/manage">
    Inspect, start, stop, update, and delete dedicated endpoints.
  </Card>

  <Card title="Endpoint settings" icon="adjustments-horizontal" href="/docs/dedicated-endpoints/settings">
    Tune autoscaling, decoding, and auto-shutdown.
  </Card>
</CardGroup>
