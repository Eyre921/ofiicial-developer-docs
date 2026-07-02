---
title: "firectl router get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/router-get
path: tools-sdks/firectl/commands/router-get
---

Prints information about a router.

```
firectl router get [flags]
```

### Examples

```
firectl router get my-router
firectl router get accounts/my-account/routers/my-router
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
