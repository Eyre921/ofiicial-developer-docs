---
title: "firectl reinforcement-fine-tuning-job cancel"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-cancel
path: tools-sdks/firectl/commands/reinforcement-fine-tuning-job-cancel
---

Cancels a running reinforcement fine-tuning job.

```
firectl reinforcement-fine-tuning-job cancel [flags]
```

### Examples

```
firectl reinforcement-fine-tuning-job cancel my-rftj
firectl reinforcement-fine-tuning-job cancel accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for cancel
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
