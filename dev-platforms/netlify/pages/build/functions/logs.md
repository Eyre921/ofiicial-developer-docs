---
title: "Function logs"
source: https://docs.netlify.com/build/functions/logs.md
path: build/functions/logs
---

---
title: "Function logs"
description: "Use Function logs to observe and troubleshoot serverless functions in your current published deploy, branch deploys, and Deploy Previews."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Netlify provides logs in the Netlify UI to help you observe and troubleshoot serverless functions in your current [published deploy](/deploy/deploy-overview#definitions), branch deploys, and Deploy Previews.

## Access function logs in the Netlify UI

1. In the Netlify UI, for your chosen site, go to 
### NavigationPath Component:

Logs & Metrics > Functions
.
2. Select a function from the list to open the log for that function.

By default, the Functions list displays the functions in the current published deploy. To find functions on another deploy, you can use the search field at the top of the list. You can start typing to jump to a particular branch, or find a Deploy Preview by number.

Team Owners and Developers can monitor the function logs for a specific deploy by going to the **Function logs** tab of the [Netlify Drawer](/deploy/review-deploys/netlify-drawer-for-feedback/overview#monitor-logs) in a collaborative Deploy Preview.

### Log contents

Netlify displays a log for each function, including:

- Start of each invocation
- Any `console.log()` statements you include in your function code
- Log statements as each [background function](/build/functions/background-functions) is executed

Note that function [log retention limits](#log-retention-and-limits) apply and may impact what the Netlify UI displays.

#### Date filter

By default, the function log displays a live tail of the latest activity in **Real-time**. You can also filter to review data from a specific time period, including the **Last hour**, **Last day**, **Last 7 days**, or select **Custom** to input a specific date and time range.

#### Text filter

You can filter the contents of the log with simple text matches on request ID, message, or log level. Some common log levels include:
- `INFO`
- `ERROR`
- `WARN`
- `FATAL`
- `DEBUG`
- `TRACE`

## Access function logs from the Netlify CLI

The [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli) `logs` command brings function logs into your terminal, either as a live tail or for a historical window. This is useful for quickly debugging without leaving your editor.

```bash
netlify logs
```

By default, the command shows the last 10 minutes of activity from functions and edge functions on the current project. Pass `--follow` (or `-f`) to switch to a live tail.

### Common options

- **`--follow`**, **`-f`** - stream logs in real time. Cannot be combined with `--since` or `--until`.
- **`--source <type...>`**, **`-s`** - one or more of `functions`, `edge-functions`, or `deploy`. Defaults to `functions` and `edge-functions`.
- **`--function <name...>`** - limit to specific functions by name. Pass multiple times to include more than one.
- **`--edge-function <name...>`** - limit to specific edge functions by name or path.
- **`--since <time>`** - start of the historical window. Accepts a duration (`10m`, `1h`, `24h`) or an ISO 8601 timestamp.
- **`--until <time>`** - end of the historical window. Defaults to now. Requires `--since`.
- **`--level <levels...>`**, **`-l`** - filter by log level: `trace`, `debug`, `info`, `warn`, `error`, or `fatal`.
- **`--url <url>`**, **`-u`** - show logs for the deploy behind a given URL (deploy permalink or branch subdomain).
- **`--json`** - output logs as JSON Lines.

### Examples

```bash
# Live tail of all function and edge function activity
netlify logs --follow

# Last hour of logs for the "checkout" function only
netlify logs --function checkout --since 1h

# Errors and fatals across the last 24 hours
netlify logs --since 24h --level error --level fatal

# JSON Lines output, useful for piping to other tools
netlify logs --json --since 1h
```

## Log retention and limits

Logs are retained for at least 24 hours of function activity, even after a new function deployment. This log retention period increases to 7 days for certain pricing plans. 

### Caution - Log limitations

For functions using the [Lambda compatibility mode](/build/functions/lambda-compatibility), historical function log output is limited to 4 KB total per invocation. If a log's output exceeds 4 KB, only the last 4 KB of the log is retained and the log message will be truncated.

## Log Drains

> **Pricing Information:** This feature is available on [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

You can connect your function logs to third-party monitoring services for analysis using Netlify's Log Drains feature. Check out our [Log Drains](/manage/monitoring/log-drains) doc for more information. 

For logs sent via Log Drains, the output for a single log entry is limited to 700 KB.

## Function metrics

On credit-based plans, function metrics are available through [Observability](/manage/monitoring/observability/overview), with a dedicated [Functions reference](/manage/monitoring/observability/reference/functions) covering success and error rates, invocation count, duration, and other indicators you can use to optimize performance, troubleshoot issues, and make data-driven decisions to enhance the overall quality and user experience of your projects.

If you're on a legacy plan, the same project shows a more limited [Function Metrics](/manage/monitoring/function-metrics) page instead.

