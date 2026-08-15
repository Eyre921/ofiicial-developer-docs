---
title: "Run a batch job"
source: https://docs.together.ai/docs/inference/batch/tutorial
path: docs/inference/batch/tutorial
---

Prepare a JSONL file, upload it, start a batch job, poll until it finishes, and retrieve results.

This tutorial walks through a complete batch inference job from start to finish. By the end you'll have uploaded a JSONL file of chat completion requests, run them as a single job at up to 50% off serverless rates, and reconciled the responses with your original inputs.

## Requirements

Before you begin, make sure you have:

* [Created an account](https://api.together.ai/settings/projects/~first/api-keys) and generated an API key.
* Set `TOGETHER_API_KEY` as an environment variable: `export TOGETHER_API_KEY=<your-key>`. See [API keys and authentication](/docs/api-keys-authentication) for details.
* [Installed the Python or TypeScript SDK](/docs/quickstart#step-2-install-the-sdk). Python examples require `together>=2.0.0`.

## Step 1: Prepare a JSONL input file

Each request lives on its own line in a JSONL file. A request has two fields: a `custom_id` you choose, and a `body` matching the schema of the endpoint you're calling. The Batch API runs every line independently and stamps each output with the same `custom_id`, so this is how you'll map results back to inputs at the end.

Save the following as `batch_input.jsonl`:

```json batch_input.jsonl theme={null}
{"custom_id": "request-1", "body": {"model": "meta-llama/Llama-3.3-70B-Instruct-Turbo", "messages": [{"role": "user", "content": "Hello, world!"}], "max_tokens": 200}}
{"custom_id": "request-2", "body": {"model": "meta-llama/Llama-3.3-70B-Instruct-Turbo", "messages": [{"role": "user", "content": "Explain quantum computing."}], "max_tokens": 200}}
```

| Field       | Type   | Required    | Description                                                                                                                                                                                                                                                       |
| ----------- | ------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_id` | string | Yes         | Unique identifier for tracking (max 64 chars).                                                                                                                                                                                                                    |
| `method`    | string | Conditional | Set to `"FILE"` when batching `/v1/audio/transcriptions` or `/v1/audio/translations` so the worker dispatches each request as `multipart/form-data`. Omit for chat completion batches. See [Run an audio transcription batch](#run-an-audio-transcription-batch). |
| `body`      | object | Yes         | Request body matching the endpoint's schema.                                                                                                                                                                                                                      |

<Warning>
  Each line must be under 10 MB. The limit applies to the full serialized line, so inline base64 payloads count toward it (e.g. a single high-resolution image embedded as a `data:image/...;base64,` URL). Oversized lines aren't caught during validation, and will fail with `error reading input file`. To stay under the limit, reference images by hosted URL instead of inlining them, or resize and compress images before encoding.
</Warning>

## Step 2: Upload the file

Upload the JSONL file with `purpose="batch-api"`. The upload returns a file object whose `id` you'll pass to the batch job in the next step.

Pass `check=False` to skip client-side validation. The server still validates the file during the `VALIDATING` phase, and skipping the client check is faster for large files without changing the error surface. With `check=True` (default), the SDK parses each JSONL line locally and raises `TogetherException` before uploading if a line is malformed.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  file_resp = client.files.upload(
      file="batch_input.jsonl",
      purpose="batch-api",
      check=False,
  )

  print(file_resp.id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const fileResp = await client.files.upload(
    "batch_input.jsonl",
    "batch-api",
    false,
  );

  console.log(fileResp.id);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/files/upload" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -F "purpose=batch-api" \
    -F "file_name=batch_input.jsonl" \
    -F "file=@batch_input.jsonl"
  ```
</CodeGroup>

<Note>
  The SDK examples infer the file name from the local path. When calling the REST API directly,
  include `file_name` in the multipart form. See the [file upload reference](/reference/upload-file)
  for the full request shape.
</Note>

## Step 3: Create the batch

Now hand the uploaded file's `id` to the batch endpoint, along with the API endpoint each request should run against. For chat completion requests, that's `/v1/chat/completions`. Audio batches use `/v1/audio/transcriptions` or `/v1/audio/translations` — see [Run an audio transcription batch](#run-an-audio-transcription-batch).

<CodeGroup>
  ```python Python theme={null}
  response = client.batches.create(
      input_file_id=file_resp.id,
      endpoint="/v1/chat/completions",
  )

  batch = response.job
  print(batch.id)
  ```

  ```typescript TypeScript theme={null}
  const response = await client.batches.create({
    input_file_id: fileResp.id,
    endpoint: "/v1/chat/completions",
  });

  const batchId = response.job?.id;
  console.log(batchId);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/batches" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"input_file_id": "file-abc123", "endpoint": "/v1/chat/completions"}'
  ```
</CodeGroup>

<Note>
  `batches.create()` returns a wrapper; the batch object lives at `.job`. `batches.retrieve()` (used in the next step) returns the batch object directly.
</Note>

## Step 4: Poll for completion

The job moves through `VALIDATING`, then `IN_PROGRESS`, then a terminal status: `COMPLETED`, `FAILED`, `EXPIRED`, or `CANCELLED`. Poll every 30 to 60 seconds until you hit a terminal status. Tighter loops will hit rate limits without giving the server time to make progress.

<CodeGroup>
  ```python Python theme={null}
  import time

  while True:
      batch = client.batches.retrieve(batch.id)
      print(f"{batch.status}: {batch.progress:.0f}%")

      if batch.status == "COMPLETED":
          break
      if batch.status in ("FAILED", "EXPIRED", "CANCELLED"):
          raise SystemExit(f"Batch ended: {batch.status}")

      time.sleep(30)
  ```

  ```typescript TypeScript theme={null}
  let batch = await client.batches.retrieve(batchId);

  while (true) {
    batch = await client.batches.retrieve(batchId);
    console.log(`${batch.status}: ${(batch.progress ?? 0).toFixed(0)}%`);

    if (batch.status === "COMPLETED") break;
    if (["FAILED", "EXPIRED", "CANCELLED"].includes(batch.status)) {
      throw new Error(`Batch ended: ${batch.status}`);
    }

    await new Promise((r) => setTimeout(r, 30_000));
  }
  ```
</CodeGroup>

<Note>
  `progress` is a float from 0 to 100 representing the percentage of requests completed. It is present on all batch objects but may remain 0 while the job is in `VALIDATING`.
</Note>

Most batches under 1,000 requests finish in minutes. The 24-hour completion window is a maximum, not a typical wait.

## Step 5: Retrieve the results

When the job reaches `COMPLETED`, the batch object carries an `output_file_id`. Download that file and you'll get one JSON object per line, each keyed by the `custom_id` from your input. Output line order does not match input line order, so use `custom_id` to reconcile.

<CodeGroup>
  ```python Python theme={null}
  with client.files.with_streaming_response.content(
      id=batch.output_file_id,
  ) as response:
      with open("batch_output.jsonl", "wb") as f:
          for chunk in response.iter_bytes():
              f.write(chunk)
  ```

  ```typescript TypeScript theme={null}
  import * as fs from "fs";

  const resp = await client.files.content(batch.output_file_id);
  fs.writeFileSync("batch_output.jsonl", await resp.text());
  ```

  ```bash cURL theme={null}
  curl -X GET "https://api.together.ai/v1/files/file-output456/content" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -o batch_output.jsonl
  ```
</CodeGroup>

A successful output line looks like:

```json theme={null}
{
  "custom_id": "request-1",
  "response": {
    "status_code": 200,
    "body": {
      "choices": [
        {
          "index": 0,
          "message": { "role": "assistant", "content": "Hello!" },
          "finish_reason": "stop"
        }
      ],
      "usage": { "prompt_tokens": 12, "completion_tokens": 3, "total_tokens": 15 }
    }
  }
}
```

Per-request failures land in a separate file referenced by `error_file_id`. Always check it: a batch can be `COMPLETED` and still contain individual request failures. See [retrieve results and error files](/docs/inference/batch/manage#retrieve-results) on the manage page.

## Run an audio transcription batch

The Batch API also supports `/v1/audio/transcriptions` and `/v1/audio/translations` for audio workloads (for example, `openai/whisper-large-v3`). The upload, poll, and retrieve steps above are identical. Two things change:

**1. Each JSONL line must include `"method": "FILE"`.** The audio endpoints expect `multipart/form-data` requests, so the worker uses the `method` field to choose its dispatch mode. Omitting it causes every line to fail with `Content-Type must be multipart/form-data` in the error file.

```json audio_batch.jsonl theme={null}
{"custom_id": "transcription-1", "method": "FILE", "body": {"file": "https://example.com/clip-1.wav", "model": "openai/whisper-large-v3"}}
{"custom_id": "transcription-2", "method": "FILE", "body": {"file": "https://example.com/clip-2.wav", "model": "openai/whisper-large-v3"}}
```

`body.file` is the publicly-reachable URL of the audio clip; the worker fetches the audio at execution time. Optional fields such as `response_format`, `language`, and `prompt` pass through to the underlying API — see the [audio transcriptions reference](/reference/audio-transcriptions) for the full schema.

**2. Pass the audio endpoint when creating the batch.**

<CodeGroup>
  ```python Python theme={null}
  response = client.batches.create(
      input_file_id=file_resp.id,
      endpoint="/v1/audio/transcriptions",
  )

  batch = response.job
  print(batch.id)
  ```

  ```typescript TypeScript theme={null}
  const response = await client.batches.create({
    input_file_id: fileResp.id,
    endpoint: "/v1/audio/transcriptions",
  });

  const batchId = response.job?.id;
  console.log(batchId);
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/batches" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"input_file_id": "file-abc123", "endpoint": "/v1/audio/transcriptions"}'
  ```
</CodeGroup>

A successful output line looks like:

```json theme={null}
{
  "custom_id": "transcription-1",
  "response": {
    "status_code": 200,
    "body": {
      "duration": 4.825,
      "language": "en",
      "text": "Yet these thoughts affected Hester Prynne less with hope than apprehension."
    }
  }
}
```

For `/v1/audio/translations`, swap the endpoint and use a translation-capable model — the JSONL line shape is the same.

## Complete script

The full Python program combining all steps above:

```python Python theme={null}
import time
from together import Together

client = Together()

file_resp = client.files.upload(
    file="batch_input.jsonl",
    purpose="batch-api",
    check=False,
)
print(f"Uploaded file: {file_resp.id}")

response = client.batches.create(
    input_file_id=file_resp.id,
    endpoint="/v1/chat/completions",
)
batch = response.job
print(f"Created batch: {batch.id}")

while True:
    batch = client.batches.retrieve(batch.id)
    print(f"{batch.status}: {batch.progress:.0f}%")

    if batch.status == "COMPLETED":
        break
    if batch.status in ("FAILED", "EXPIRED", "CANCELLED"):
        raise SystemExit(f"Batch ended: {batch.status}")

    time.sleep(30)

with client.files.with_streaming_response.content(
    id=batch.output_file_id,
) as response:
    with open("batch_output.jsonl", "wb") as f:
        for chunk in response.iter_bytes():
            f.write(chunk)

print("Results saved to batch_output.jsonl")
```

## Next steps

* [Manage batch jobs](/docs/inference/batch/manage): cancel, list, and download error files.
* [Batch processing overview](/docs/inference/batch/overview): rate limits, discounted models, best practices, and FAQ.
