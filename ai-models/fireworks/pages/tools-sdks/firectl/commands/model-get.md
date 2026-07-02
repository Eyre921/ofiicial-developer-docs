---
title: "firectl model get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-get
path: tools-sdks/firectl/commands/model-get
---

Prints information about a model.

```
firectl model get [flags]
```

### Examples

```
firectl model get my-model
firectl model get accounts/fireworks/models/my-model
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
