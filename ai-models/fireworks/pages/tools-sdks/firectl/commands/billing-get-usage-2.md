---
title: "firectl billing get-usage"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-get-usage
path: tools-sdks/firectl/commands/billing-get-usage
---

Prints account usage and rated costs for a time range.

```
firectl billing get-usage [flags]
```

### Examples

```
firectl billing get-usage --start-time 2026-05-01 --end-time 2026-06-01
firectl billing get-usage --start-time 2026-05-01 --end-time 2026-06-01 --usage-type serverless --group-by model_name
firectl billing get-usage --start-time 2026-05-01 --end-time 2026-06-01 --usage-type dedicated-deployment --filter deployment_name=accounts/my-account/deployments/my-deployment
```

### Flags

```
      --account-costs-only   Only print account-level cumulative costs for the date range.
      --dry-run              Print the request proto without running it.
      --end-time string      The end time (exclusive), as YYYY-MM-DD or 'YYYY-MM-DD hh:mm:ss'.
      --filter stringArray   Filter in key=value form. Can be repeated; repeated values for the same key are OR'ed.
      --group-by strings     Dimension to group usage by. Can be repeated; valid dimensions are server-validated.
  -h, --help                 help for get-usage
  -o, --output Output        Set the output format to "text", "json", or "flag". (default text)
      --start-time string    The start time (inclusive), as YYYY-MM-DD or 'YYYY-MM-DD hh:mm:ss'.
      --timezone string      IANA timezone identifier for daily aggregation, for example "America/Los_Angeles". Defaults to UTC.
      --usage-type string    Usage type to query: all, serverless, or dedicated-deployment.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
