---
title: "firectl router update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/router-update
path: tools-sdks/firectl/commands/router-update
---

Update a router.

```
firectl router update [flags]
```

### Examples

```
firectl router update my-router --deployments=my-deployment1,my-deployment2
firectl router update my-router --strategy=weighted-random
firectl router update my-router --strategy=even-load
```

### Flags

```
      --display-name string   The display name of the router.
      --strategy string       The strategy to use for routing traffic. (default "weighted-random")
      --deployments strings   The deployment names to be covered by the router.
      --public                Whether the router is public. If not specified, the router is private.
      --session-affinity      Enable regional-level session affinity for this router.
      --dry-run               Print the request proto without running it.
  -o, --output Output         Set the output format to "text", "json", or "flag". (default text)
  -h, --help                  help for update
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
