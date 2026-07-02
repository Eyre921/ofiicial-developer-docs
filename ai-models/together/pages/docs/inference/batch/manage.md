---
title: "Manage batch jobs"
source: https://docs.together.ai/docs/inference/batch/manage
path: docs/inference/batch/manage
---

Status, results, errors, and operational reference for the Together Batch API.

Reference for managing live batch jobs: checking status, downloading outputs and error files, cancelling, and listing. For an end-to-end walkthrough, see [Run a batch job](/docs/inference/batch/tutorial).

<Note>
  Python examples require `together>=2.0.0`
</Note>

## Check batch status

`batches.retrieve()` returns the batch object directly (no `.job` wrapper, unlike `create()`).

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  batch = client.batches.retrieve("batch-xyz789")

  print(batch.status)
  print(batch.progress)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const batch = await client.batches.retrieve("batch-xyz789");

  console.log(batch.status);
  console.log(batch.progress);
  ```

  ```bash cURL theme={null}
  curl -X GET "https://api.together.ai/v1/batches/batch-xyz789" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

| Status        | Description                                                   |
| ------------- | ------------------------------------------------------------- |
| `VALIDATING`  | The input file is being validated before the batch can begin. |
| `IN_PROGRESS` | Requests are being processed.                                 |
| `COMPLETED`   | All requests processed; results available.                    |
| `FAILED`      | Processing failed.                                            |
| `EXPIRED`     | The job exceeded its time limit.                              |
| `CANCELLED`   | The job was cancelled.                                        |

Poll every 30 to 60 seconds. Tighter loops will hit rate limits without giving the server time to make progress.

## Retrieve results

When the batch reaches `COMPLETED`, download the output file referenced by `output_file_id`. Per-request failures are stored separately in `error_file_id`. Always download both: a `COMPLETED` batch can still contain individual request failures.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  batch = client.batches.retrieve("batch-xyz789")

  if batch.output_file_id:
      with client.files.with_streaming_response.content(
          id=batch.output_file_id,
      ) as response:
          with open("batch_output.jsonl", "wb") as f:
              for chunk in response.iter_bytes():
                  f.write(chunk)

  if batch.error_file_id:
      with client.files.with_streaming_response.content(
          id=batch.error_file_id,
      ) as response:
          with open("batch_errors.jsonl", "wb") as f:
              for chunk in response.iter_bytes():
                  f.write(chunk)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import * as fs from "fs";

  const client = new Together();

  const batch = await client.batches.retrieve("batch-xyz789");

  if (batch.output_file_id) {
    const resp = await client.files.content(batch.output_file_id);
    fs.writeFileSync("batch_output.jsonl", await resp.text());
  }

  if (batch.error_file_id) {
    const errResp = await client.files.content(batch.error_file_id);
    fs.writeFileSync("batch_errors.jsonl", await errResp.text());
  }
  ```
</CodeGroup>

Output and error lines are both keyed by the `custom_id` from your input, so you can reconcile them with a single pass over each file. Line order does not match input order.

## Cancel a batch

You can cancel a batch while it is `VALIDATING` or `IN_PROGRESS`. Requests that have already completed before the cancellation are still billed, and their responses are still returned in the output file.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  client.batches.cancel("batch-xyz789")
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  await client.batches.cancel("batch-xyz789");
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/batches/batch-xyz789/cancel" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

## List batches

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  for batch in client.batches.list():
      print(batch.id, batch.status)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const batches = await client.batches.list();

  for (const batch of batches ?? []) {
    console.log(batch.id, batch.status);
  }
  ```

  ```bash cURL theme={null}
  curl -X GET "https://api.together.ai/v1/batches" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

## Errors

### Error codes

| Code | Description            | Solution                                |
| ---- | ---------------------- | --------------------------------------- |
| 400  | Invalid request format | Check JSONL syntax and required fields. |
| 401  | Authentication failed  | Verify your API key.                    |
| 404  | Batch not found        | Check the batch ID.                     |
| 429  | Rate limit exceeded    | Reduce request frequency.               |
| 500  | Server error           | Retry with exponential backoff.         |

### Error file format

Each line in the error file pairs a `custom_id` from your input with the failure reason:

```json batch_errors.jsonl theme={null}
{"custom_id": "req-1", "error": {"message": "Invalid model specified", "code": "invalid_model"}}
{"custom_id": "req-5", "error": {"message": "Request timeout", "code": "timeout"}}
```
