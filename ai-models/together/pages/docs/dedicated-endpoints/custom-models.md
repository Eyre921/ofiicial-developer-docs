---
title: "Upload a model"
source: https://docs.together.ai/docs/dedicated-endpoints/custom-models
path: docs/dedicated-endpoints/custom-models
---

Upload a custom or fine-tuned model from Hugging Face or S3 and serve it on a dedicated endpoint.

You can run inference on your own custom or fine-tuned models by uploading them to Together AI and deploying them on a [dedicated endpoint](/docs/dedicated-endpoints/overview). Models can come from the Hugging Face Hub or from an archive in S3.

## Prerequisites

A model is eligible for upload if it meets all of the following:

* **Source:** Hugging Face Hub or an S3 presigned URL.
* **Type:** text generation or embedding model.
* **Scale:** fits on a single node. Multi-node models aren't supported.

The model files must be in standard Hugging Face repository format, compatible with `from_pretrained`. A valid model directory contains files like:

```
config.json
generation_config.json
model-00001-of-00004.safetensors
model-00002-of-00004.safetensors
model-00003-of-00004.safetensors
model-00004-of-00004.safetensors
model.safetensors.index.json
special_tokens_map.json
tokenizer.json
tokenizer_config.json
```

To upload a LoRA adapter instead of a full model, see [Deploy a fine-tuned adapter](/docs/dedicated-endpoints/adapter).

### S3 archive requirements

If you're uploading from S3, package the files in a single archive (`.zip` or `.tar.gz`) with the model files at the root of the archive. Don't nest them inside an extra top-level directory.

Correct (files at root):

```
config.json
model.safetensors
tokenizer.json
...
```

Incorrect (files nested in a directory):

```
my-model/
  config.json
  model.safetensors
  tokenizer.json
  ...
```

To create the archive from within the model directory:

```bash Shell theme={null}
cd /path/to/your/model
tar -czvf ../model.tar.gz .
```

The presigned URL must point to the archive file in S3 and have an expiration of at least 100 minutes.

## Upload the model

<Tabs>
  <Tab title="CLI / SDK">
    Upload from Hugging Face by passing the repo path as `model_source`. Include your Hugging Face token for private or gated repos.

    <CodeGroup>
      ```shell Shell theme={null}
      together models upload \
        --model-name <MODEL_NAME> \
        --model-source <HUGGING_FACE_REPO> \
        --hf-token "$HUGGINGFACE_TOKEN"
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      response = client.models.upload(
          model_name="<MODEL_NAME>",
          model_source="<HUGGING_FACE_REPO>",
          hf_token="<HUGGING_FACE_TOKEN>",
      )
      print(response.data.job_id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const response = await client.models.upload({
        model_name: "<MODEL_NAME>",
        model_source: "<HUGGING_FACE_REPO>",
        hf_token: "<HUGGING_FACE_TOKEN>",
      });
      console.log(response.data.job_id);
      ```
    </CodeGroup>

    Upload from S3 by passing the presigned archive URL as `model_source`:

    <CodeGroup>
      ```shell Shell theme={null}
      together models upload \
        --model-name <MODEL_NAME> \
        --model-source <S3_PRESIGNED_URL>
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      response = client.models.upload(
          model_name="<MODEL_NAME>",
          model_source="<S3_PRESIGNED_URL>",
      )
      print(response.data.job_id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const response = await client.models.upload({
        model_name: "<MODEL_NAME>",
        model_source: "<S3_PRESIGNED_URL>",
      });
      console.log(response.data.job_id);
      ```
    </CodeGroup>

    The response includes a `job_id`. Use it to poll for upload status.

    ### CLI options

    | Option           | Required         | Description                                                   |
    | ---------------- | ---------------- | ------------------------------------------------------------- |
    | `--model-name`   | Yes              | The name to give the uploaded model.                          |
    | `--model-source` | Yes              | A Hugging Face repo path or an S3 presigned URL.              |
    | `--hf-token`     | For Hugging Face | Your Hugging Face token. Required for private or gated repos. |
    | `--model-type`   | No               | `model` (default) or `adapter`.                               |
    | `--description`  | No               | A description of the model.                                   |
  </Tab>

  <Tab title="UI">
    <Steps>
      <Step title="Open the upload form">
        Sign in and go to [Models > Upload a model](https://api.together.ai/models/upload).
      </Step>

      <Step title="Enter the source">
        In **Source URL**, enter your Hugging Face repo path (for example, `meta-llama/Llama-3.3-70B-Instruct`) or an S3 presigned URL pointing to your model archive.
      </Step>

      <Step title="Name and describe the model">
        Enter a model name and an optional description. Both appear in your Together AI account once the upload completes.
      </Step>

      <Step title="Submit">
        Select **Upload**. Together AI returns a job ID and starts the upload.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Check upload status

Poll the upload job until its `status` field is `Complete`. The model is ready to deploy at that point.

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

You can also see uploaded models on the [My models](https://api.together.ai/models?category=my-models) page in the dashboard.

## Deploy the model

Uploaded models deploy as dedicated endpoints, the same way as any other model.

<Tabs>
  <Tab title="CLI / SDK">
    List hardware available for the uploaded model:

    <CodeGroup>
      ```shell Shell theme={null}
      together endpoints hardware --model <MODEL_NAME>
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      response = client.endpoints.list_hardware(model="<MODEL_NAME>")
      for hw in response.data:
          print(hw.id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const response = await client.endpoints.listHardware({
        model: "<MODEL_NAME>",
      });
      for (const hw of response.data) {
        console.log(hw.id);
      }
      ```
    </CodeGroup>

    Create the endpoint, using the hardware ID from the list:

    <CodeGroup>
      ```shell Shell theme={null}
      together endpoints create \
        --display-name <ENDPOINT_NAME> \
        --model <MODEL_NAME> \
        --hardware <HARDWARE_ID>
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      endpoint = client.endpoints.create(
          model="<MODEL_NAME>",
          hardware="<HARDWARE_ID>",
          display_name="<ENDPOINT_NAME>",
          autoscaling={"min_replicas": 1, "max_replicas": 1},
      )
      print(endpoint.id, endpoint.name)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const endpoint = await client.endpoints.create({
        model: "<MODEL_NAME>",
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
      <Step title="Open the model page">
        Go to [My models](https://api.together.ai/models?category=my-models) and select your uploaded model to open its detail page.
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
