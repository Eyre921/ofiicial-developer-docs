---
title: "firectl deployed-model get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployed-model-get
path: tools-sdks/firectl/commands/deployed-model-get
---

Prints information about a deployed model.

```
firectl deployed-model get [flags]
```

### Examples

```
firectl deployed-model get my-deployed-model
firectl deployed-model get accounts/my-account/deployedModels/my-deployed-model
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
