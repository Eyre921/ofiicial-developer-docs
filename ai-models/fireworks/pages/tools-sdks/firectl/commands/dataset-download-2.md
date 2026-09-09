---
title: "firectl dataset download"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-download
path: tools-sdks/firectl/commands/dataset-download
---

Downloads a dataset to a local directory.

```
firectl dataset download [flags]
```

### Examples

```
# Download a single dataset
firectl dataset download my-dataset --output-dir /path/to/download

# Download entire lineage chain (only for batch inference continuation jobs)
firectl dataset download my-dataset --download-lineage --output-dir /path/to/download
```

### Flags

```
      --download-lineage    If true, downloads entire lineage chain (all related datasets)
  -h, --help                help for download
      --output-dir string   Directory to download dataset files to (default ".")
      --quiet               If true, does not show download progress
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
