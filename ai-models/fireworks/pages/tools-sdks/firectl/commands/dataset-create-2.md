---
title: "firectl dataset create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-create
path: tools-sdks/firectl/commands/dataset-create
---

Creates and uploads a dataset.

```
firectl dataset create [flags]
```

### Examples

```
firectl dataset create my-dataset /path/to/dataset.jsonl
firectl dataset create --trace-from-model-id model_abc --format chat --date 2024-01-10 my-dataset
firectl dataset create my-dataset --external-url gs://bucket-name/object-name
```

### Flags

```
      --display-name string    The display name of the dataset.
      --dry-run                Print the request proto without running it.
      --end-time string        The end time for which to trace data (format: YYYY-MM-DD). Only specify for traced dataset.
      --eval-protocol-output   If true, the dataset is in eval protocol output format.
      --external-url string    The GCS URI that points to the dataset file.
      --filter string          Filter condition to apply to the source dataset.
  -h, --help                   help for create
  -o, --output Output          Set the output format to "text", "json", or "flag". (default text)
      --quiet                  If true, does not print the upload progress bar.
      --source string          Source dataset ID to filter from.
      --start-time string      The start time for which to trace data (format: YYYY-MM-DD). Only specify for traced dataset.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
