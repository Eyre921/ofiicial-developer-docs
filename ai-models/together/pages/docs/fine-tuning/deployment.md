---
title: "Deploy a fine-tuned model"
source: https://docs.together.ai/docs/fine-tuning/deployment
path: docs/fine-tuning/deployment
---

Serve your fine-tuned model on a dedicated endpoint or download it for local inference.

Once a fine-tuning job completes, your model is available for inference in two ways: hosted on a dedicated endpoint at Together AI, or downloaded as a standalone checkpoint.

## Prerequisites

* A completed fine-tuning job. See the [quickstart](/docs/fine-tuning/quickstart) for the full lifecycle.
* The job's **Model Object ID** (`model_object_id`, an `ml_...` value) — the model-registry ID of the trained weights and the identifier you deploy. It's available once the job status is `completed`, from the `tg fine-tuning retrieve` output.

## Deploy on a dedicated endpoint

Together AI serves fine-tuned models through [dedicated model inference](/docs/dedicated-endpoints/overview) (DMI). A completed fine-tuning job is already a private model in your project, so you deploy it by its Model Object ID with no separate upload step. Deployment and lifecycle operations use the `tg beta` CLI.

<Warning>
  Dedicated model inference bills per minute per running replica, even when idle. Scale the deployment to zero or delete the endpoint when you're done to stop charges.
</Warning>

<Note>
  The dedicated model inference commands require Together CLI version `2.24.0` or later. Install or upgrade with `uv tool install "together[cli]"` (or `uv tool upgrade "together[cli]"`), and check your version with `tg --version`.
</Note>

<Tabs>
  <Tab title="CLI / SDK">
    The CLI's `deploy` command creates the endpoint, attaches a deployment, and routes all traffic to it in one step. Pass the fine-tune's Model Object ID (`ml_...`) — not the `x_model_output_name`, which isn't a deployable identifier in dedicated model inference:

    ```bash CLI theme={null}
    # Retrieve the job to copy its Model Object ID (model_object_id, an ml_... value)
    tg fine-tuning retrieve "<JOB_ID>"

    # Deploy the fine-tuned model to a new endpoint
    tg beta endpoints deploy "<MODEL_OBJECT_ID>" \
      --endpoint my-finetuned-endpoint
    ```

    The SDK has no single-call equivalent, so it runs the same steps individually: create the endpoint, bind the model and a config to a deployment, then route traffic to it. Reference the fine-tune by its **Model Object ID** (`ml_...`, the job's `model_object_id`):

    <CodeGroup>
      ```python Python theme={null}
      from together import Together

      client = Together()
      project_id = client.whoami().project_id

      # Reference the fine-tune by its Model Object ID (ml_...) and a config
      # for the base model. List configs: tg beta models configs <model>.
      model = f"projects/{project_id}/models/<MODEL_OBJECT_ID>"
      config = f"projects/{project_id}/configs/<CONFIG_ID>"

      # 1. Create the endpoint.
      endpoint = client.beta.endpoints.create(
          project_id=project_id,
          name="my-finetuned-endpoint",
      )

      # 2. Bind the model and config to a deployment.
      deployment = client.beta.endpoints.deployments.create(
          endpoint.id,
          project_id=project_id,
          name="prod",
          model=model,
          config=config,
          autoscaling={"min_replicas": 1, "max_replicas": 1},
      )

      # 3. Route 100% of traffic to the deployment.
      client.beta.endpoints.update(
          endpoint.id,
          project_id=project_id,
          traffic_split=[{"deployment_id": deployment.id, "weight": 1}],
      )
      print(endpoint.name)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();
      const { project_id: projectId } = await client.whoami();

      // Reference the fine-tune by its Model Object ID (ml_...) and a config
      // for the base model. List configs: tg beta models configs <model>.
      const model = `projects/${projectId}/models/<MODEL_OBJECT_ID>`;
      const config = `projects/${projectId}/configs/<CONFIG_ID>`;

      // 1. Create the endpoint.
      const endpoint = await client.beta.endpoints.create({
        projectId,
        name: "my-finetuned-endpoint",
      });

      // 2. Bind the model and config to a deployment.
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

      // 3. Route 100% of traffic to the deployment.
      await client.beta.endpoints.update(endpoint.id, {
        projectId,
        trafficSplit: [{ deploymentId: deployment.id, weight: 1 }],
      });
      console.log(endpoint.name);
      ```
    </CodeGroup>

    Poll until the deployment reaches `DEPLOYMENT_STATE_READY`:

    ```bash CLI theme={null}
    tg beta endpoints get "<ENDPOINT_ID>"
    ```

    From the SDK, retrieve the deployment and read `status.state`:

    <CodeGroup>
      ```python Python theme={null}
      deployment = client.beta.endpoints.deployments.retrieve(
          deployment.id,
          project_id=project_id,
          endpoint_id=endpoint.id,
      )
      print(deployment.status.state)
      ```

      ```typescript TypeScript theme={null}
      const current = await client.beta.endpoints.deployments.retrieve(
        deployment.id,
        { projectId, endpointId: endpoint.id },
      );
      console.log(current.status.state);
      ```
    </CodeGroup>

    Once the deployment is `READY`, the endpoint serves at its **endpoint string** (`your-project-slug/my-finetuned-endpoint`, returned as `endpoint.name`). Pass it as the `model` parameter and point the base URL at `https://api-inference.together.ai/v1`:

    <CodeGroup>
      ```bash cURL theme={null}
      curl -s https://api-inference.together.ai/v1/chat/completions \
        -H "Authorization: Bearer $TOGETHER_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "your-project-slug/my-finetuned-endpoint",
          "messages": [{"role": "user", "content": "Hello!"}]
        }'
      ```

      ```python Python theme={null}
      from together import Together

      # A dedicated client for inference: this base URL serves only
      # inference, not the fine-tuning or files APIs.
      inference_client = Together(base_url="https://api-inference.together.ai/v1")

      response = inference_client.chat.completions.create(
          model="your-project-slug/my-finetuned-endpoint",
          messages=[{"role": "user", "content": "Hello!"}],
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
        model: "your-project-slug/my-finetuned-endpoint",
        messages: [{ role: "user", content: "Hello!" }],
      });
      console.log(response.choices[0].message.content);
      ```
    </CodeGroup>

    When you're done, delete the endpoint and its deployment to stop billing. The CLI's `rm --force` removes both in one step:

    ```bash CLI theme={null}
    tg beta endpoints rm "<ENDPOINT_ID>" --force
    ```

    The SDK has no smart-delete, so stop billing by scaling the deployment to zero, then delete the resources once it reaches `DEPLOYMENT_STATE_STOPPED`:

    <CodeGroup>
      ```python Python theme={null}
      # Scale to zero to stop billing.
      client.beta.endpoints.deployments.update(
          deployment.id,
          project_id=project_id,
          endpoint_id=endpoint.id,
          autoscaling={"min_replicas": 0, "max_replicas": 0},
      )

      # Once it's DEPLOYMENT_STATE_STOPPED, drop its traffic weight, then
      # delete the deployment and the endpoint.
      client.beta.endpoints.update(
          endpoint.id,
          project_id=project_id,
          traffic_split=[{"deployment_id": deployment.id, "weight": 0}],
      )
      client.beta.endpoints.deployments.delete(
          deployment.id, project_id=project_id, endpoint_id=endpoint.id
      )
      client.beta.endpoints.delete(endpoint.id, project_id=project_id)
      ```

      ```typescript TypeScript theme={null}
      // Scale to zero to stop billing.
      await client.beta.endpoints.deployments.update(deployment.id, {
        projectId,
        endpointId: endpoint.id,
        autoscaling: { minReplicas: 0, maxReplicas: 0 },
      });

      // Once it's DEPLOYMENT_STATE_STOPPED, drop its traffic weight, then
      // delete the deployment and the endpoint.
      await client.beta.endpoints.update(endpoint.id, {
        projectId,
        trafficSplit: [{ deploymentId: deployment.id, weight: 0 }],
      });
      await client.beta.endpoints.deployments.delete(deployment.id, {
        projectId,
        endpointId: endpoint.id,
      });
      await client.beta.endpoints.delete(endpoint.id, { projectId });
      ```
    </CodeGroup>

    To pause billing without deleting anything (for example, if you plan to use the endpoint again later), scale the deployment to zero and stop there. See [Delete resources](/docs/dedicated-endpoints/manage#delete-resources) for the full teardown order.

    <Note>
      If `deploy` reports that the model has more than one deployment profile, re-run it with `--config <cr_...>`. List a model's profiles with `tg beta models configs "<MODEL_OBJECT_ID>"`. See [Choose a deployment profile](/docs/dedicated-endpoints/configs).
    </Note>
  </Tab>

  <Tab title="UI">
    <Steps>
      <Step title="Open your models">
        Go to [My models](https://api.together.ai/models?category=my-models). Your completed fine-tuned models appear here once training finishes.
      </Step>

      <Step title="Create the endpoint">
        Select your fine-tuned model, then select **Create dedicated endpoint**.
      </Step>

      <Step title="Configure the deployment">
        Choose a deployment configuration (hardware and GPU count) and set the replica bounds.
      </Step>

      <Step title="Deploy">
        Select **Deploy**. Provisioning takes up to 10 minutes. You can navigate away while it runs.
      </Step>

      <Step title="Stop when done">
        Open the endpoint from the dashboard and stop or delete it when you're not using it to halt per-minute billing.
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

* **No Model Object ID yet:** The job hasn't reached `completed`, so `model_object_id` isn't populated. Poll status with `client.fine_tuning.retrieve(id=...)` until it's done. See [Monitor a fine-tuning job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) for the polling pattern.
* **`endpoints_v1_create_access_disabled` (HTTP 403):** You're calling the retired v1 endpoints API (`client.endpoints.create(...)` or `tg endpoints create`). Deploy on dedicated model inference with `tg beta endpoints deploy` instead. See [Migrate from v1](/docs/dedicated-endpoints/migrate-from-v1).
* **`deploy` reports multiple deployment profiles:** Re-run with `--config <cr_...>`. List a model's profiles with `tg beta models configs "<MODEL_OBJECT_ID>"`.
* **Deploy fails because the base isn't supported:** Not every base model can be hosted for dedicated inference. Confirm the base appears in the [supported models](/docs/dedicated-endpoints/models) list before training (`-Reference` models often can't be deployed).
* **404 on inference:** Point the base URL at `https://api-inference.together.ai/v1` and pass the endpoint string (`your-project-slug/<endpoint_name>`, printed by the deploy output) as the `model` parameter, not the Model Object ID.

## Next steps

<CardGroup>
  <Card title="Upload a custom model" icon="upload" href="/docs/dedicated-endpoints/custom-models">
    Upload your own model weights from outside the Together catalog.
  </Card>

  <Card title="Manage endpoints" icon="settings" href="/docs/dedicated-endpoints/manage">
    Inspect, start, stop, update, and delete dedicated endpoints.
  </Card>

  <Card title="Configure autoscaling" icon="adjustments-horizontal" href="/docs/dedicated-endpoints/scaling">
    Tune replica bounds and autoscale a deployment on the metric that fits your workload.
  </Card>
</CardGroup>
