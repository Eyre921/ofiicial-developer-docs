---
title: "Run a batch job"
source: https://docs.together.ai/docs/inference/batch/tutorial
path: docs/inference/batch/tutorial
---

Prepare a JSONL file, upload it, start a batch job, poll until it finishes, and retrieve results.

In this tutorial you'll upload a JSONL file of chat completion requests, run it as a single batch job, and match the responses back to your inputs. With the CLI, the whole flow takes three commands:

```bash theme={null}
# upload the file and create the batch
tg batches submit batch_input.jsonl --api chat.completions

# poll until COMPLETED
tg batches get <BATCH_ID>

# save the results
tg batches download <BATCH_ID> --output batch_output.jsonl
```

The steps below break down this flow and show the SDK and REST equivalents for each part.

## Requirements

Before you begin, make sure you have:

* [Created an account](https://api.together.ai/settings/projects/~first/api-keys) and generated an API key.
* Set `TOGETHER_API_KEY` as an environment variable:
  ```bash theme={null}
  export TOGETHER_API_KEY=<your_key>
  ```
* [Installed the Python or TypeScript SDK](/docs/quickstart#step-2-install-the-sdk). Python examples require `together>=2.0.0`.
* [Installed the Together CLI](/reference/cli/getting-started), version 2.32.0 or later (check with `tg --version`), to follow the CLI examples.

## Step 1: Prepare a JSONL input file

Each line of the JSONL file is one request with two fields: a unique `custom_id` you choose (up to 64 characters), and a `body` matching the schema of the endpoint you're calling. Every line runs independently, and its output carries the same `custom_id`, which is how you'll match results to inputs at the end.

Save the following as `batch_input.jsonl`:

```json batch_input.jsonl theme={null}
{"custom_id": "request-1", "body": {"model": "meta-llama/Llama-3.3-70B-Instruct-Turbo", "messages": [{"role": "user", "content": "Hello, world!"}], "max_tokens": 200}}
{"custom_id": "request-2", "body": {"model": "meta-llama/Llama-3.3-70B-Instruct-Turbo", "messages": [{"role": "user", "content": "Explain quantum computing."}], "max_tokens": 200}}
```

Audio requests add a third field, `method`. See [Run an audio transcription batch](#run-an-audio-transcription-batch).

<Warning>
  Each line must be under 10 MB, including any inline base64 payloads (a single high-resolution image embedded as a `data:image/...;base64,` URL can exceed it). Oversized lines aren't caught during validation and fail with `error reading input file`. Reference images by hosted URL instead of inlining them, or resize and compress them before encoding.
</Warning>

## Step 2: Upload the file

Upload the JSONL file with `purpose="batch-api"`. The response includes the file `id` you'll pass to the batch job in the next step. CLI users can skip this step: `tg batches submit` accepts a local file path and uploads it for you (see the next step).

<Visibility>
  Pass `check=False` (`--no-check` in the CLI) to skip client-side validation. The server still validates the file during the `VALIDATING` phase, and skipping the client check is faster for large files without changing the error surface. With `check=True` (default), the SDK parses each JSONL line locally and raises `TogetherException` before uploading if a line is malformed.
</Visibility>

<CodeGroup>
  ```bash CLI theme={null}
  tg files upload batch_input.jsonl --purpose batch-api --no-check
  ```

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

Create the batch by passing the file `id` from step 2 and the endpoint each request runs against: `/v1/chat/completions` for chat completions, or `--api chat.completions` in the CLI. For audio, see [Run an audio transcription batch](#run-an-audio-transcription-batch).

<CodeGroup>
  ```bash CLI theme={null}
  # Pass the file ID from step 2
  tg batches submit file-abc123 --api chat.completions

  # Or pass the local path to upload and create the job in one command
  tg batches submit batch_input.jsonl --api chat.completions
  ```

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
  In the SDKs, `batches.create()` returns a wrapper with the batch object at `.job`. `batches.retrieve()` (used in the next step) returns the batch object directly.
</Note>

## Step 4: Poll for completion

The job moves through `VALIDATING` and `IN_PROGRESS`, and finally to a terminal state: `COMPLETED`, `FAILED`, `EXPIRED`, or `CANCELLED`. Poll every 30 to 60 seconds (tighter loops will likely cause you to hit rate limits).

<CodeGroup>
  ```bash CLI theme={null}
  # Shows the status and a progress bar. Re-run until the job reaches a terminal state.
  tg batches get a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
  ```

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

  ```bash cURL theme={null}
  # Returns the batch object. Re-run until status reaches a terminal state.
  curl -X GET "https://api.together.ai/v1/batches/a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

<Note>
  `progress` tracks the percentage of requests completed, from 0 to 100. It may stay at 0 while the job is in `VALIDATING`.
</Note>

Most batches under 1,000 requests finish in minutes. The 24-hour completion window is a maximum, not a typical wait.

## Step 5: Retrieve the results

When the job reaches `COMPLETED`, the batch object includes an `output_file_id`. Download that file to get one JSON result per line. Results aren't guaranteed to be in input order, so match them to inputs using the `custom_id` field.

<CodeGroup>
  ```bash CLI theme={null}
  tg batches download a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d --output batch_output.jsonl
  ```

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

Failed requests land in a separate file referenced by `error_file_id`. Always check it: a batch can be `COMPLETED` and still contain failures. The CLI's `download` saves the error file automatically (here as `batch_output.errors.jsonl`). See [retrieve results and error files](/docs/inference/batch/manage#retrieve-results).

## Run an audio transcription batch

The batch API also supports `/v1/audio/transcriptions` and `/v1/audio/translations` (for example, with `openai/whisper-large-v3`). Upload, poll, and retrieve work exactly as above. Two things change:

**1. Each JSONL line must include `"method": "FILE"`.** This tells the worker to send the request as `multipart/form-data`, which the audio endpoints require. Without it, every line fails with `Content-Type must be multipart/form-data` in the error file.

```json audio_batch.jsonl theme={null}
{"custom_id": "transcription-1", "method": "FILE", "body": {"file": "https://example.com/clip-1.wav", "model": "openai/whisper-large-v3"}}
{"custom_id": "transcription-2", "method": "FILE", "body": {"file": "https://example.com/clip-2.wav", "model": "openai/whisper-large-v3"}}
```

`body.file` is a publicly reachable URL for the audio clip. The worker fetches it at run time. Optional fields such as `response_format`, `language`, and `prompt` pass through to the underlying API. See the [audio transcriptions reference](/reference/audio-transcriptions) for the full schema.

**2. Pass the audio endpoint when creating the batch.**

<CodeGroup>
  ```bash CLI theme={null}
  tg batches submit audio_batch.jsonl --api audio.transcriptions
  ```

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

For `/v1/audio/translations`, swap the endpoint and use a translation-capable model. The JSONL line shape is the same.

## Complete script

The full flow as a CLI session or a Python program:

<CodeGroup>
  ```bash CLI theme={null}
  # Upload the file and create the batch in one command
  tg batches submit batch_input.jsonl --api chat.completions

  # Re-run until the status is COMPLETED (use the batch ID printed by submit)
  tg batches get a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d

  # Save the results (and any error file) to disk
  tg batches download a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d --output batch_output.jsonl
  ```

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
</CodeGroup>

## Next steps

* [Manage batch jobs](/docs/inference/batch/manage): cancel, list, and download error files.
* [Batches CLI](/reference/cli/batches): the full `tg batches` command reference.
* [Batch processing overview](/docs/inference/batch/overview): rate limits, discounted models, best practices, and FAQ.
