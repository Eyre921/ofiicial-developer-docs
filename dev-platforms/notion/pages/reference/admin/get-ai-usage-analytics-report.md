---
title: "Get ai usage analytics report"
source: https://developers.notion.com/reference/admin/get-ai-usage-analytics-report
path: reference/admin/get-ai-usage-analytics-report
---

openapi-adminApi.json GET /v1/analytics/ai_usage/reports/{job_id}
Fetch a AI usage analytics report.

The organization bot token must have the following scopes:

* `analytics:ai-analytics`

Authenticate the report request with an organization bot bearer credential. Supply the workspace UUID in `workspace_id` and the report UUID in `job_id`. A live bot in the same organization with the current `analytics:ai-analytics` scope can fetch a report created by another bot.

Completed reports include `download_url` and `link_expires_at` when the file is available. Follow that URL directly; it contains a derived organization bot file token and needs no additional Authorization header. Downloads use the configured secure file host (`file.notion.com` or `file.notion.so`; local environments use their configured file host).

Links expire after seven days or at the saved file expiry, whichever comes first. Files retain their original 30-day lifetime. Fetch the report again to renew a link while its file remains available. Permissions, credential revocation, and file expiry are checked again when downloading.

Completed reports also include `row_count`, `file_size_bytes`, and `data_as_of`, the ISO 8601 time of the source data. `data_as_of` can be earlier than `completed_time` because generation takes time.

Expired or definitively missing files return HTTP 200 with `status: "expired"` and no download URL. Queued, running, and failed reports also omit download URLs. Failed reports include `failed_time` and `error_code`.

A file that fails integrity verification returns HTTP 500 with `additional_data.tool_error_code` set to `analytics_report_integrity_failed` and `additional_data.tool_error_retryable` set to `false`. Create a new report instead of retrying. Other storage failures return HTTP 500 with `tool_error_retryable` set to `true`.

CSV and JSONL files contain the same values, with two CSV-only rules. A text value that starts with `=`, `+`, `-`, `@`, `*`, `/`, or a full-width equals sign, optionally after tabs or line breaks, gets a leading `'` so spreadsheets show it as text instead of running it as a formula. List values are JSON arrays, such as `["Engineering","Product"]`; an empty list is `[]` and a missing value is an empty cell. JSONL keeps exact values.

Treat the full download URL as a credential. Do not log or share it, and avoid sending it in referrers. Report responses and downloaded files use `Cache-Control: private, no-store`.
