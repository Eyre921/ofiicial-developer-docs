---
title: "Upload a LoRA adapter"
source: https://docs.together.ai/docs/dedicated-endpoints/adapter
path: docs/dedicated-endpoints/adapter
---

Upload a custom LoRA adapter from Hugging Face or S3 and serve it on a dedicated endpoint.

You can upload your own [LoRA (Low-Rank Adaptation) adapters](/docs/fine-tuning/lora-vs-full) to Together AI and run inference on them through a [dedicated endpoint](/docs/dedicated-endpoints/overview). Adapters can come from the Hugging Face Hub or from an archive in S3, including adapters you trained outside of Together AI.

To upload a full custom model instead of an adapter, see [Upload a model](/docs/dedicated-endpoints/custom-models).

## Prerequisites

An adapter is eligible for upload if it meets all of the following:

* **Source:** Hugging Face Hub or an S3 presigned URL.
* **Files:** the adapter directory must contain `adapter_config.json` and `adapter_model.safetensors`.
* **Base model:** the adapter must target a base model that Together AI supports for dedicated inference.

If you're uploading from S3, package the adapter files in a single archive (`.zip` or `.tar.gz`) with the files at the root of the archive, not nested inside an extra top-level directory. The presigned URL must point to the archive and have an expiration of at least 100 minutes.

## Upload the adapter

<Tabs>
  <Tab title="CLI / SDK">
    Upload from Hugging Face by passing the repo URL as `model_source` and setting `model_type` to `adapter`. Include your Hugging Face token for private or gated repos.

    <CodeGroup>
      ```shell Shell theme={null}
      together models upload \
        --model-name <ADAPTER_NAME> \
        --model-source <HUGGING_FACE_REPO_URL> \
        --model-type adapter \
        --base-model <BASE_MODEL_ID> \
        --hf-token "$HUGGINGFACE_TOKEN"
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      response = client.models.upload(
          model_name="<ADAPTER_NAME>",
          model_source="<HUGGING_FACE_REPO_URL>",
          model_type="adapter",
          base_model="<BASE_MODEL_ID>",
          hf_token="<HUGGING_FACE_TOKEN>",
      )
      print(response.data.job_id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const response = await client.models.upload({
        model_name: "<ADAPTER_NAME>",
        model_source: "<HUGGING_FACE_REPO_URL>",
        model_type: "adapter",
        base_model: "<BASE_MODEL_ID>",
        hf_token: "<HUGGING_FACE_TOKEN>",
      });
      console.log(response.data.job_id);
      ```
    </CodeGroup>

    Upload from S3 by passing the presigned archive URL as `model_source`:

    <CodeGroup>
      ```shell Shell theme={null}
      together models upload \
        --model-name <ADAPTER_NAME> \
        --model-source <S3_PRESIGNED_URL> \
        --model-type adapter \
        --base-model <BASE_MODEL_ID>
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      response = client.models.upload(
          model_name="<ADAPTER_NAME>",
          model_source="<S3_PRESIGNED_URL>",
          model_type="adapter",
          base_model="<BASE_MODEL_ID>",
      )
      print(response.data.job_id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const response = await client.models.upload({
        model_name: "<ADAPTER_NAME>",
        model_source: "<S3_PRESIGNED_URL>",
        model_type: "adapter",
        base_model: "<BASE_MODEL_ID>",
      });
      console.log(response.data.job_id);
      ```
    </CodeGroup>

    A successful upload returns the upload job:

    ```json theme={null}
    {
      "data": {
        "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
        "model_name": "devuser/test-lora-model-creation-8b",
        "model_source": "remote_archive"
      },
      "message": "job created"
    }
    ```

    Note the `job_id` (used to check status) and the `model_name` (used to deploy and call the adapter).

    ### CLI options

    | Option           | Required         | Description                                                   |
    | ---------------- | ---------------- | ------------------------------------------------------------- |
    | `--model-name`   | Yes              | The name to give the uploaded adapter.                        |
    | `--model-source` | Yes              | A Hugging Face repo URL or an S3 presigned URL.               |
    | `--model-type`   | Yes              | Set to `adapter` for LoRA adapters.                           |
    | `--base-model`   | Yes              | The base model the adapter targets.                           |
    | `--hf-token`     | For Hugging Face | Your Hugging Face token. Required for private or gated repos. |
    | `--description`  | No               | A description of the adapter.                                 |
  </Tab>

  <Tab title="UI">
    <Steps>
      <Step title="Open the upload form">
        Sign in and go to [Models > Upload a model](https://api.together.ai/models/upload).
      </Step>

      <Step title="Pick adapter as the type">
        Set the model type to **Adapter** and select the base model the adapter was trained against.
      </Step>

      <Step title="Enter the source">
        In **Source URL**, enter your Hugging Face repo URL or an S3 presigned URL pointing to your adapter archive. For private or gated Hugging Face repos, also provide your Hugging Face token.
      </Step>

      <Step title="Name and describe the adapter">
        Enter an adapter name and an optional description. Both appear in your Together AI account once the upload completes.
      </Step>

      <Step title="Submit">
        Select **Upload**. Together AI returns a job ID and starts the upload.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Check upload status

Poll the upload job until its `status` field is `Complete`. The adapter is ready to deploy at that point.

<CodeGroup>
  ```shell Shell theme={null}
  curl -X GET "https://api.together.ai/v1/jobs/<JOB_ID>" \
       -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.models.uploads.status("<JOB_ID>")
  print(response.status)
  ```
</CodeGroup>

A completed job looks like this:

```json theme={null}
{
  "type": "adapter_upload",
  "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
  "status": "Complete",
  "status_updates": []
}
```

You can also see uploaded adapters on the [My models](https://api.together.ai/models?category=my-models) page in the dashboard.

## Deploy the adapter

Uploaded adapters deploy as dedicated endpoints, the same way as any other model. Use the `model_name` from the upload response as the `model` argument when creating the endpoint.

<Note>
  If you already run a LoRA-enabled endpoint for this adapter's base model, you can [attach the adapter to that endpoint](/docs/dedicated-endpoints/lora-adapter) instead of provisioning new hardware.
</Note>

<Tabs>
  <Tab title="CLI / SDK">
    List hardware available for the adapter, then create the endpoint with one of the returned hardware IDs:

    <CodeGroup>
      ```shell Shell theme={null}
      together endpoints hardware --model <ADAPTER_MODEL_NAME>

      together endpoints create \
        --display-name <ENDPOINT_NAME> \
        --model <ADAPTER_MODEL_NAME> \
        --hardware <HARDWARE_ID>
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      hw = client.endpoints.list_hardware(model="<ADAPTER_MODEL_NAME>")
      for h in hw.data:
          print(h.id)

      endpoint = client.endpoints.create(
          model="<ADAPTER_MODEL_NAME>",
          hardware="<HARDWARE_ID>",
          display_name="<ENDPOINT_NAME>",
          autoscaling={"min_replicas": 1, "max_replicas": 1},
      )
      print(endpoint.id, endpoint.name)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const hw = await client.endpoints.listHardware({
        model: "<ADAPTER_MODEL_NAME>",
      });
      for (const h of hw.data) {
        console.log(h.id);
      }

      const endpoint = await client.endpoints.create({
        model: "<ADAPTER_MODEL_NAME>",
        hardware: "<HARDWARE_ID>",
        display_name: "<ENDPOINT_NAME>",
        autoscaling: { min_replicas: 1, max_replicas: 1 },
      });
      console.log(endpoint.id, endpoint.name);
      ```
    </CodeGroup>

    See [Manage dedicated endpoints](/docs/dedicated-endpoints/manage) for the full endpoint lifecycle, including autoscaling, listing, and deletion.
  </Tab>

  <Tab title="UI">
    <Steps>
      <Step title="Open the adapter page">
        Go to [My Models](https://api.together.ai/models) and select your uploaded adapter to open its detail page.
      </Step>

      <Step title="Create the endpoint">
        Select **Create dedicated endpoint** and pick the hardware and scaling configuration you want.
      </Step>

      <Step title="Deploy">
        Confirm to deploy. Once the endpoint state is `STARTED`, call it from the playground or via the API.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Run inference

Once the endpoint is running, call it like any other Together AI chat or completions model. Use the `model_name` from the upload response as the `model` parameter.

<CodeGroup>
  ```shell Shell theme={null}
  curl -X POST "https://api.together.ai/v1/chat/completions" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "<ADAPTER_MODEL_NAME>",
      "messages": [
        {"role": "user", "content": "What is the capital of France?"}
      ],
      "max_tokens": 128,
      "temperature": 0.8
    }'
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="<ADAPTER_MODEL_NAME>",
      messages=[{"role": "user", "content": "What is the capital of France?"}],
      max_tokens=128,
      temperature=0.8,
  )
  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.chat.completions.create({
    model: "<ADAPTER_MODEL_NAME>",
    messages: [{ role: "user", content: "What is the capital of France?" }],
    max_tokens: 128,
    temperature: 0.8,
  });
  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Troubleshooting

**"Model name already exists":** Each uploaded adapter needs a unique name. Adapter versioning isn't supported, so re-upload under a new name.

**Missing required files:** The adapter source must contain both `adapter_config.json` and `adapter_model.safetensors`. Confirm both are present at the root of the archive (S3) or in the **Files and versions** tab on Hugging Face.

**Base model incompatibility:** The adapter must target a base model that Together AI supports for dedicated inference. Verify the base model you trained against is available on [dedicated endpoints](/docs/dedicated-endpoints/models).

**Upload job stuck in `Processing`:** Most often this means the source can't be reached. For S3, confirm the presigned URL hasn't expired. For Hugging Face, confirm your token has access to the repo.

**`401` or `403` during upload:** Check that `TOGETHER_API_KEY` is set, your Hugging Face token has permission for private repos, and your S3 presigned URL is valid and not expired.

## FAQ

**Can I upload adapters trained outside Together AI?** Yes, as long as the adapter targets one of the supported base models and includes the required files.

**Can I update an existing adapter?** No. Upload the new version under a different name. Adapter versioning isn't supported yet.
