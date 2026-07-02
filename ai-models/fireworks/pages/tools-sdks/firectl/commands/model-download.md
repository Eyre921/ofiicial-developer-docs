---
title: "firectl model download"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-download
path: tools-sdks/firectl/commands/model-download
---

Download a model.

```
firectl model download [flags]
```

### Examples

```
firectl model download my-model /path/to/checkpoint/
```

### Flags

```
  -h, --help    help for download
      --quiet   If true, does not print the upload progress bar.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
