---
title: "Logs"
source: https://docs.sentry.io/product/logs.md
path: product/logs
---

---
title: "Logs"
description: "Structured logs allow you to send, view and query logs and parameters sent from your applications within Sentry."
url: https://docs.sentry.io/product/logs/
---

# Logs

## [Overview](https://docs.sentry.io/product/logs.md#overview)

With Structured Logs, you can send text-based log information from your applications, whether frontend or backend, to Sentry.

Sentry's structured logs are searchable, **trace-connected**, and viewable alongside your errors.

**What does trace-connected mean?** Every log entry is automatically linked to the active trace when it was recorded. This means you can click directly from any log entry to see the full trace waterfall, including all related spans, errors, and other logs from the same request. This connection makes it easy to understand the complete context of what happened—not just what was logged, but the entire execution path that led to that log entry.

When investigating an issue, you can search your logs by message content or attributes, then click into any log entry to see the exact trace, spans, and errors that occurred at that moment. Learn more about [Trace View](https://docs.sentry.io/concepts/key-terms/tracing/trace-view.md) to understand how to navigate from logs to traces.

Not everything in your application generates an error or requires full tracing. Logs are perfect for tracking:

* **Debugging information**: Cache misses, database connections, query results, and performance metrics
* **User behavior**: Login events, checkout flows, feature usage, and preference changes
* **Application state**: Configuration loading, service initialization, and connection status
* **Business events**: Order placements, payment processing, and notification delivery

Learn how to [send structured logs](https://docs.sentry.io/product/logs/getting-started.md) with custom attributes that you can search and filter in Sentry.

Your plan type determines your query window: Developer: 7 days | Team: 14 days | Business: 30 days.

## [Set up Logs](https://docs.sentry.io/product/logs.md#set-up-logs)

To get started with Logs, navigate to the [Getting Started](https://docs.sentry.io/product/logs/getting-started.md) page and select your SDK from the list.

If you're using a platform where you can't install the Sentry SDK directly, or if you want to forward logs from platform-native logging systems, you can use [log drains](https://docs.sentry.io/product/drains.md) to send logs to Sentry.

## [Viewing and Searching Logs](https://docs.sentry.io/product/logs.md#viewing-and-searching-logs)

**Raw Text Search**\
Raw text search is case sensitive and allows you to search for specific strings within the *message* attribute of the Log. **Raw text search over the entire log's JSON is not supported.** Learn more about [search syntax](https://docs.sentry.io/concepts/search.md).

**Default Properties Search**\
You can also search using the default properties (like `severity`) or [additional custom properties](https://docs.sentry.io/concepts/search/searchable-properties.md) that you've added to your log entries.

**Search Examples**\
Here are some practical examples of log searches you can use:

* `severity:error` - Find all error-level logs
* `severity:error payment.failed` - Find error logs containing "payment.failed" in the message
* `user.id:12345` - Find all logs for a specific user
* `trace_id:abc123def456` - Find all logs associated with a specific trace
* `severity:error environment:production` - Find production errors
* `order.id:order_123` - Find logs related to a specific order
* `severity:warn OR severity:error` - Find warnings or errors
* `database:"users" query.duration_ms:>1000` - Find slow database queries on the users database

Learn more about [search syntax](https://docs.sentry.io/concepts/search.md) for advanced querying.

**Expand Logs**\
Log entries can be expanded to view all properties of a log entry. Individual properties can be added as columns to the results view, allowing you to quickly view properties that matter specifically to you alongside your search results.

**Auto-Refresh**\
You can also enable auto refreshing of the logs view to see your latest logs as they come in.

Conditions in which auto-refresh is disabled:

* Auto-refresh is only supported when sorting by time in descending order.
* Auto-refresh is only supported when using a relative time period, like "Last 15 minutes" or "Last 7 days", not absolute dates like "2025-07-23".
* Auto-refresh is disabled due to high data volume (100 logs per second). Try adding a [filter](https://docs.sentry.io/concepts/data-management/filtering.md#logs-filtering) to reduce the number of logs.
* Auto-refresh will be disabled due to reaching a max auto-refresh time of 10 minutes.
* Auto-refresh will be disabled if there is an error fetching logs.
* Auto-refresh is not available in the [aggregates view](https://docs.sentry.io/product/logs.md#aggregates-view).

**Export Data**\
You can export up to 10,000 log lines in CSV or [JSON Lines (JSONL)](https://jsonlines.org/) format.

* Click **Export Data** to select your format, pick whether to export only the currently displayed columns or all columns, and choose the number of rows.
  * **Note:** Use either format to export the currently displayed columns, or use JSONL to export All Columns.
* Depending on the size, the file will either download directly or be sent to you via email.

### [Pinning Logs](https://docs.sentry.io/product/logs.md#pinning-logs)

Logs can be pinned to the top of the logs view to keep them visible as you scroll through large datasets. This helps you to keep critical log lines (such as session start markers or specific state changes) visible as a "sticky header".

To pin or un-pin a log, click the push pin icon that appears when you hover over a log row:

## [Visualizing Log Data](https://docs.sentry.io/product/logs.md#visualizing-log-data)

The Logs Explorer includes a **Visualize** panel under **Advanced** that controls the charts displayed above the log table.

### [Configuring Charts](https://docs.sentry.io/product/logs.md#configuring-charts)

* The first chart defaults to `count(logs)` as a fixed time-series bar chart representing log volume over the selected time range. Change the function (like `sum`, `avg`, `count`) to visualize a different metric.
* Click **+ Add Chart** to add additional charts. Each additional chart lets you choose a function (like `sum`, `avg`, `count`) and an attribute (like `payload_size`) to visualize.
* Additional charts also support **Area**, **Line**, and **Bar** chart types.

### [Group By](https://docs.sentry.io/product/logs.md#group-by)

Use the **Group By** section under Visualize to break down charts by an attribute (for example, `device.name` or `severity`). You can ad multiple Group Bys to the same chart.

## [Aggregates View](https://docs.sentry.io/product/logs.md#aggregates-view)

Switch to the **Aggregates** tab to see the grouped by log data. The table shows one row per group with columns for each function you've configured in Visualize (for example, `count(logs)` and `sum(payload_size)` grouped by `device.name`).

Use the aggregates view to identify high-volume log sources, compare payload sizes across functions, or spot patterns without scrolling through individual log lines.

Auto-refresh is not available in the aggregates view.

## [Query Volumes](https://docs.sentry.io/product/logs.md#query-volumes)

When the number of logs returned by a query is too high, there are a couple of changes to the logs explorer functionality. To reduce query volumes, consider [filtering logs](https://docs.sentry.io/concepts/data-management/filtering.md#logs-filtering) or refining your [search query](https://docs.sentry.io/concepts/search.md) with more specific criteria.

* Auto-refresh will be disabled.
* Data shown in the chart will be extrapolated from a sampled amount of the complete dataset.

When doing very specific queries, like looking for a particular line of code that is causing an issue, you may see a message that says "No logs found yet". This happens when the dataset is very large, and Sentry needs to batch the results. You can continue scanning to see the next batch of logs by clicking "Continue Scanning".

## [Trace-Connected Debugging Flow](https://docs.sentry.io/product/logs.md#trace-connected-debugging-flow)

Sentry's trace-connected logs enable a seamless debugging workflow that connects logs, traces, and errors:

1. **Search your logs**: Start by searching for logs related to the issue you're investigating. Use message content, attributes, or filters to narrow down relevant log entries.

2. **Click into a log**: When you find a log entry that looks suspicious or relevant, click on it to open the log details.

3. **Navigate to the trace**: From the log details, click the trace link to open the full [Trace View](https://docs.sentry.io/concepts/key-terms/tracing/trace-view.md). This shows you the complete execution path, including all spans, operations, and timing information.

4. **Examine related data**: In the trace view, you can see:

   * **Related errors**: Any errors that occurred during the same trace
   * **Other logs**: Additional log entries from the same request
   * **Performance data**: Slow spans, database queries, and API calls
   * **User context**: User information and session data

5. **Find the root cause**: With full context in hand—logs, traces, spans, and errors all connected—you can quickly identify and resolve the root cause.

Instead of jumping between different tools and trying to correlate timestamps, trace-connected logs give you a **single flow**: Log search → log entry → trace → root cause.

## [Log-based Alerts and Dashboard widgets](https://docs.sentry.io/product/logs.md#log-based-alerts-and-dashboard-widgets)

You can create [Alerts](https://docs.sentry.io/product/monitors-and-alerts/alerts.md) and [dashboard widgets](https://docs.sentry.io/product/dashboards/widget-builder.md) based on your log queries.

Learn more about [Alerts](https://docs.sentry.io/product/monitors-and-alerts/alerts.md) and [custom dashboards](https://docs.sentry.io/product/dashboards/custom-dashboards.md).

## [AI-Powered Log Analysis](https://docs.sentry.io/product/logs.md#ai-powered-log-analysis)

Your Sentry logs can be leveraged with agents and tooling for debugging, summarizing, and automated analysis.

* **[Sentry CLI](https://docs.sentry.io/cli/logs.md)**: Provides command-line access to your logs, making it easy to feed log data directly into AI tools and scripts for analysis.
* **[Sentry MCP Server](https://mcp.sentry.dev)**: Provides secure connectivity between your Sentry data and LLM clients using the Model Context Protocol. This enables natural language queries and deep integration with AI tools like Claude, Cursor, and VS Code.
* **[Seer](https://docs.sentry.io/product/ai-in-sentry/seer.md)**: Sentry's AI debugging agent automatically uses logs alongside other telemetry data to provide intelligent issue analysis and automated fixes.

## Pages in this section

- [Set Up](https://docs.sentry.io/product/logs/getting-started.md)

