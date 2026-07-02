---
title: "firectl rlor-trainer-job get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/rlor-trainer-job-get
path: tools-sdks/firectl/commands/rlor-trainer-job-get
---

Retrieves information about a rlor trainer job.

```
firectl rlor-trainer-job get [flags]
```

### Examples

```
firectl rlor-trainer-job get my-rlor-job
firectl rlor-trainer-job get accounts/my-account/rlorTrainerJobs/my-rlor-job
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
