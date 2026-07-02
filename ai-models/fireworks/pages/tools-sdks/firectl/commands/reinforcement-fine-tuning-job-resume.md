---
title: "firectl reinforcement-fine-tuning-job resume"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-resume
path: tools-sdks/firectl/commands/reinforcement-fine-tuning-job-resume
---

Resumes a failed reinforcement fine-tuning job.

```
firectl reinforcement-fine-tuning-job resume [flags]
```

### Examples

```
firectl reinforcement-fine-tuning-job resume my-rftj
firectl reinforcement-fine-tuning-job resume accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for resume
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
