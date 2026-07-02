---
title: "firectl reinforcement-fine-tuning-job get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-get
path: tools-sdks/firectl/commands/reinforcement-fine-tuning-job-get
---

Retrieves information about a reinforcement fine-tuning job.

```
firectl reinforcement-fine-tuning-job get [flags]
```

### Examples

```
firectl reinforcement-fine-tuning-job get my-rftj
firectl reinforcement-fine-tuning-job get accounts/my-account/reinforcementFineTuningJobs/my-rftj
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
