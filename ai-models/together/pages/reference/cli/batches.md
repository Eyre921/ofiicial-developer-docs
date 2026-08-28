---
title: "Batches"
source: https://docs.together.ai/reference/cli/batches
path: reference/cli/batches
---

Submit, monitor, download, and cancel batch inference jobs from your terminal.

Submit and manage [batch inference](/docs/inference/batch/overview) jobs from the Together CLI. A batch job runs each line of a JSONL input file as its own request against a chat completions or audio endpoint. For the end-to-end workflow and input format, see [Run a batch job](/docs/inference/batch/tutorial).

## Submit

Submit a new batch job. Pass either a local JSONL path, which the CLI uploads for you with `purpose=batch-api`, or the ID of a file you already uploaded. Each request names its model in its JSONL `body`. There is no model flag.

```bash theme={null}
tg batches submit [FILE_ID_OR_PATH] [API]
```

`API` is required and must be one of `chat.completions`, `audio.transcriptions`, or `audio.translations`. You can pass it positionally or with `--api`.

```bash theme={null}
# Local file (uploads, then creates the job)
tg batches submit ./requests.jsonl chat.completions

# Previously uploaded file ID
tg batches submit file-abc123 --api chat.completions

# Audio transcription batch
tg batches submit ./audio.jsonl --api audio.transcriptions
```

### Parameters

| Flag                                                                         | Description                                                                                                                                                |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FILE_ID_OR_PATH`                                                            | File ID from the Files API, or a local path to a JSONL file to upload.<br />**required**                                                                   |
| `API` / `--api [chat.completions\|audio.transcriptions\|audio.translations]` | API to run each line of the input file against. Maps to `/v1/chat/completions`, `/v1/audio/transcriptions`, or `/v1/audio/translations`.<br />**required** |

On success, the command prints a job summary and the exact `tg batches get` command for checking progress. Pass `--json` for the full create response (including any `warning`). If the API returns no job, the command exits with status 1.

## List

List batch jobs, newest first.

```bash theme={null}
tg batches list
```

Alias: `tg batches ls`.

### Parameters

| Flag               | Description                             |
| ------------------ | --------------------------------------- |
| `--after [string]` | Pagination cursor from a previous page. |

## Retrieve

Get details for a specific batch job.

```bash theme={null}
tg batches retrieve [BATCH_ID]
```

Alias: `tg batches get`.

The output shows the created and completed times, the API, the model, the output and error file IDs, and the status, with a progress bar while the job is `VALIDATING` or `IN_PROGRESS`. Once the job has finished and has files to download, the command prints the matching `tg batches download` command.

## Download

Download the batch output file and, when present, the error file.

```bash theme={null}
tg batches download [BATCH_ID]
```

Omit `--output` to stream the output file to stdout. Pass `--output` with a file or directory path to save the files to disk instead. When the job has both an output and an error file, the error file is written as `<stem>.errors<suffix>` next to the output file so it never overwrites your results. With `--json`, `--output` is required, and the JSON response lists the saved paths.

```bash theme={null}
# Stream output to stdout
tg batches download a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d

# Save to a file (errors go to results.errors.jsonl when present)
tg batches download a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d --output ./results.jsonl

# Save into a directory (the output file keeps its server filename)
tg batches download a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d --output ./out
```

### Parameters

| Flag                     | Description                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------ |
| `--output` / `-o [path]` | File or directory to write result files to. Omit to print the output file to stdout. |

The job must have reached a terminal status (`COMPLETED`, `FAILED`, `EXPIRED`, or `CANCELLED`) before you can download anything. Use `tg batches get` to check progress while it's still running.

## Cancel

Cancel a batch job.

```bash theme={null}
tg batches cancel [BATCH_ID]
```

The command confirms the cancellation and prints the job summary. Pass `--json` for the raw batch object instead.
