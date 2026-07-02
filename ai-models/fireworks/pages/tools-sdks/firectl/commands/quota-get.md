---
title: "firectl quota get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/quota-get
path: tools-sdks/firectl/commands/quota-get
---

Prints information about a quota.

```
firectl quota get [flags]
```

### Examples

```
firectl quota get serverless-inference-rpm
firectl quota get accounts/my-account/quotas/serverless-inference-rpm
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
