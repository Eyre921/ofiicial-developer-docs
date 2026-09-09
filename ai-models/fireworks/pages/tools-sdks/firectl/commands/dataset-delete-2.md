---
title: "firectl dataset delete"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-delete
path: tools-sdks/firectl/commands/dataset-delete
---

Deletes a dataset.

```
firectl dataset delete [flags]
```

### Examples

```
firectl dataset delete my-dataset
firectl dataset delete accounts/my-account/datasets/my-dataset
```

### Flags

```
      --dry-run                 Print the request proto without running it.
  -h, --help                    help for delete
  -o, --output Output           Set the output format to "text", "json", or "flag". (default text)
      --wait                    Wait until the dataset is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
