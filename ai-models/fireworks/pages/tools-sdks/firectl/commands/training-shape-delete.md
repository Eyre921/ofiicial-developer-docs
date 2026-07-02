---
title: "firectl training-shape delete"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-delete
path: tools-sdks/firectl/commands/training-shape-delete
---

Deletes a training shape and all its versions.

```
firectl training-shape delete <training-shape-id> [flags]
```

### Examples

```
firectl training-shape delete my-shape
firectl training-shape delete accounts/my-account/trainingShapes/my-shape
```

### Flags

```
  -h, --help   help for delete
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
