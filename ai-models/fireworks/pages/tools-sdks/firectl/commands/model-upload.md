---
title: "firectl model upload"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-upload
path: tools-sdks/firectl/commands/model-upload
---

Resumes or completes a model upload.

### Usage

Resumes or completes a model upload for an existing model. This command should be used when a previous upload was interrupted.

```
firectl model upload [flags]
```

### Examples

```
firectl model upload my-model /path/to/checkpoint/
```

### Flags

```
  -h, --help    help for upload
      --quiet   If true, does not print the upload progress bar.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
