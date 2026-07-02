---
title: "firectl evaluator-revision alias"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/evaluator-revision-alias
path: tools-sdks/firectl/commands/evaluator-revision-alias
---

Alias an evaluator revision

```
firectl evaluator-revision alias [flags]
```

### Examples

```
firectl evaluator-revision alias accounts/my-account/evaluators/my-evaluator/versions/abc123 --alias-id current
```

### Flags

```
  -h, --help   help for alias
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
