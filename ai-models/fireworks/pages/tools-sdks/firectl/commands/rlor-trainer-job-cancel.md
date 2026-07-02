---
title: "firectl rlor-trainer-job cancel"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/rlor-trainer-job-cancel
path: tools-sdks/firectl/commands/rlor-trainer-job-cancel
---

Cancels a running rlor trainer job.

```
firectl rlor-trainer-job cancel [flags]
```

### Examples

```
firectl rlor-trainer-job cancel my-rlor-job
firectl rlor-trainer-job cancel accounts/my-account/rlorTrainerJobs/my-rlor-job
```

### Flags

```
  -h, --help                    help for cancel
      --wait                    Wait until the rlor trainer job is cancelled.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 10m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
