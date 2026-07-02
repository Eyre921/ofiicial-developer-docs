---
title: "firectl deployment undelete"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-undelete
path: tools-sdks/firectl/commands/deployment-undelete
---

Undeletes a deployment.

```
firectl deployment undelete [flags]
```

### Examples

```
firectl deployment undelete my-deployment
```

### Flags

```
  -h, --help                    help for undelete
      --wait                    Wait until the deployment is undeleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
