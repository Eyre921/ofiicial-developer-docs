---
title: "firectl training-shape-version get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-version-get
path: tools-sdks/firectl/commands/training-shape-version-get
---

Prints information about a training shape version.

```
firectl training-shape-version get [flags]
```

### Examples

```
firectl training-shape-version get accounts/my-account/trainingShapes/my-shape/versions/my-version
firectl training-shape-version get accounts/my-account/trainingShapes/my-shape/versions/latest
```

### Flags

```
      --dry-run         Print the request proto without running it.
  -h, --help            help for get
  -o, --output Output   Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
