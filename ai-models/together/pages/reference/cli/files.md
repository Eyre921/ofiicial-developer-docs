---
title: "Files"
source: https://docs.together.ai/reference/cli/files
path: reference/cli/files
---

Upload and manage datasets for use in fine-tuning, evals, and batch inference.

## Upload

To upload a new dataset file:

```bash theme={null}
tg files upload [FILENAME]
```

Here's a sample output:

```bash theme={null}
$ tg files upload ./example.jsonl
Uploading file example.jsonl: 100%|██████████████████████████████| 5.18M/5.18M [00:01<00:00, 4.20MB/s]
Success!
file-d931200a-6b7f-476b-9ae2-8fddd5112308
```

The printed `file-…` identifier is the assigned `file-id` for this file object. Pass `--json` to get the full response body instead.

### Parameters

| Flag                 | Description                                                                                                                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--purpose [string]` | The purpose of the file. Default: `fine-tune`. Must be one of:<br /><ul><li>`fine-tune`</li><li>`eval`</li><li>`eval-sample`</li><li>`eval-output`</li><li>`eval-summary`</li><li>`batch-generated`</li><li>`batch-api`</li></ul> |
| `--no-check`         | Skip local structural validation before uploading (UTF-8 and JSON object per non-empty line for JSONL). The server still validates during ingestion.                                                                              |

## Check

You can precheck that a file is structurally valid before uploading.

```bash theme={null}
tg files check [PATH]
```

Here's a sample output:

```bash theme={null}
$ tg files check ./local-file.jsonl
Validating file: 1 lines [00:00, 7476.48 lines/s]
OK Checks passed
```

Pass `--json` to get the full structured report instead of the pass/fail summary:

```bash theme={null}
$ tg files check ./local-file.jsonl --json
{
  "is_check_passed": true,
  "message": "Checks passed",
  "found": true,
  "file_size": 620,
  "utf8": true,
  "line_type": true,
  "text_field": true,
  "key_value": true,
  "has_min_samples": true,
  "num_samples": 5,
  "load_json": true,
  "load_csv": null,
  "filetype": "jsonl"
}
```

For fine-tuning JSONL files, this command verifies UTF-8 encoding, that each non-empty line is parseable JSON, and that there is one JSON object per line, along with the minimum sample count and maximum file size. Schema-level validation (such as required fields and role ordering) is performed on the server when the file is used. The Files API surfaces any errors at that point.

## List

To list previously uploaded files:

```bash theme={null}
tg files list
```

## Retrieve

To retrieve the metadata of a previously uploaded file:

```bash theme={null}
tg files retrieve [FILE_ID]
```

Here's a sample output:

```bash theme={null}
$ tg files retrieve file-d931200a-6b7f-476b-9ae2-8fddd5112308
Retrieved file details
Id:      file-d931200a-6b7f-476b-9ae2-8fddd5112308 
Name:    info_provided_validation_tokenized.parquet
Size:    303.4 KB
Type:    parquet
Purpose: fine-tune
Created: 03/16/2026, 03:58 PM
```

## Retrieve content

To download a previously uploaded file:

<CodeGroup>
  ```bash Download to file theme={null}
  tg files retrieve-content <FILE_ID> \
    --output ./
  ```

  ```bash Stream to stdout theme={null}
  tg files retrieve-content <FILE_ID> \
    --stdout
  ```
</CodeGroup>

Here's a sample output:

```bash theme={null}
$ tg files retrieve-content file-d931200a-6b7f-476b-9ae2-8fddd5112308 --output ./
File saved to ./example.jsonl
```

You must pass either `--output <DIRECTORY>` to write the contents to disk under the file's original filename, or `--stdout` to stream the contents to standard output.

## Delete

To delete a previously uploaded file:

```bash theme={null}
tg files delete [FILE_ID]
```

Here's a sample output:

```bash theme={null}
$ tg files delete file-d931200a-6b7f-476b-9ae2-8fddd5112308
√ File deleted
```
