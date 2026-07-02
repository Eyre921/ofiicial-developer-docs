---
title: "firectl reinforcement-fine-tuning-job update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-update
path: tools-sdks/firectl/commands/reinforcement-fine-tuning-job-update
---

Update fields on a reinforcement fine-tuning job.

```
firectl reinforcement-fine-tuning-job update [flags]
```

### Examples

```
firectl-admin rftj update my-job --training-accelerator-type=NVIDIA_B200_180GB
firectl-admin rftj update accounts/my-account/reinforcementFineTuningJobs/my-job --training-accelerator-type=NVIDIA_B200_180GB --toleration=fireworks.ai/rftj
```

### Flags

```
      --dry-run         Print the request proto without running it.
  -h, --help            help for update
  -o, --output Output   Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
