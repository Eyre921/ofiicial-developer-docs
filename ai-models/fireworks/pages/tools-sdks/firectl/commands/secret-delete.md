---
title: "firectl secret delete"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/secret-delete
path: tools-sdks/firectl/commands/secret-delete
---

Deletes a secret.

```
firectl secret delete [flags]
```

### Examples

```
firectl secret delete MY_SECRET
```

### Flags

```
      --dry-run         Print the request proto without running it.
  -h, --help            help for delete
  -o, --output Output   Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
