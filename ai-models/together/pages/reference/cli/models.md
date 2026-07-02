---
title: "Models"
source: https://docs.together.ai/reference/cli/models
path: reference/cli/models
---

List Together AI models and upload your own from Hugging Face or S3.

## Upload

Upload a model from Hugging Face or S3 for inference on a [dedicated endpoint](/docs/dedicated-endpoints/overview).

<CodeGroup>
  ```bash Basic theme={null}
  tg models upload \
      --model-name [TEXT] \
      --model-source [URI]
  ```

  ```bash Hugging Face theme={null}
  # Upload a model from Hugging Face.
  tg models upload \
      --model-name together-m1-3b-personal-clone \
      --model-source https://huggingface.co/togethercomputer/M1-3B \
      --hf-token "$HUGGINGFACEHUB_API_TOKEN"
  ```

  ```bash S3 theme={null}
  # Upload a model from S3.
  PRESIGNED_URL=$(sh ./get-presigned-url)

  tg models upload \
    --model-name my-s3-upload-model \
    --model-source "$PRESIGNED_URL"
  ```
</CodeGroup>

### Parameters

| Flag             | Type                 | Description                                                                                                  |
| ---------------- | -------------------- | ------------------------------------------------------------------------------------------------------------ |
| `--model-name`   | `string`             | The name to give your uploaded model. **required**                                                           |
| `--model-source` | `string`             | The source URI of the model. **required**                                                                    |
| `--model-type`   | `model` or `adapter` | Whether the model is a full model or an adapter.                                                             |
| `--hf-token`     | `string`             | Hugging Face token, used when uploading from Hugging Face.                                                   |
| `--description`  | `string`             | A description of your model.                                                                                 |
| `--base-model`   | `string`             | The base model for an adapter when running against a serverless pool. Only used with `--model-type adapter`. |
| `--lora-model`   | `string`             | The LoRA pool for an adapter when running against a dedicated pool. Only used with `--model-type adapter`.   |

## List all models

<CodeGroup>
  ```bash Basic theme={null}
  # List models
  tg models list
  ```

  ```bash List Deployable Models theme={null}
  # List models that can be deployed on dedicated endpoints
  tg models list --type dedicated
  ```

  ```bash JSON output theme={null}
  # Output in JSON mode and pipe to jq.
  tg models list --json | jq 'length'
  ```
</CodeGroup>

### Parameters

| Flag      | Type        | Description                                                                                            |
| --------- | ----------- | ------------------------------------------------------------------------------------------------------ |
| `--type`  | `dedicated` | Filter to models that can be deployed on dedicated endpoints. `dedicated` is the only available value. |
| `--after` | `string`    | The cursor to start from for pagination.                                                               |
