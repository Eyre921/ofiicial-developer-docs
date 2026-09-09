---
title: "firectl dataset update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-update
path: tools-sdks/firectl/commands/dataset-update
---

Updates a dataset.

```
firectl dataset update [flags]
```

### Examples

```
firectl dataset update my-dataset
firectl dataset update accounts/my-account/datasets/my-dataset
```

### Flags

```
      --display-name string   The display name of the dataset.
      --dry-run               Print the request proto without running it.
  -h, --help                  help for update
  -o, --output Output         Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
