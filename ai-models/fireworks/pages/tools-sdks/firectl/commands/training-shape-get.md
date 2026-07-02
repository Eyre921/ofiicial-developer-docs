---
title: "firectl training-shape get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-get
path: tools-sdks/firectl/commands/training-shape-get
---

Prints information about a training shape.

```
firectl training-shape get <training-shape-id> [flags]
```

### Examples

```
firectl training-shape get my-shape
firectl training-shape get accounts/my-account/trainingShapes/my-shape
```

### Flags

```
  -h, --help   help for get
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
