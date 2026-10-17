---
title: "Get user activity analytics report"
source: https://developers.notion.com/reference/admin/get-user-activity-analytics-report
path: reference/admin/get-user-activity-analytics-report
---

openapi-adminApi.json GET /v1/analytics/user_activity/reports/{job_id}
Fetch a user activity analytics report.

The organization bot token must have the following scopes:

* `analytics:user-activity`

Authenticate the report request with an organization bot bearer credential. Supply the workspace UUID in `workspace_id` and the report UUID in `job_id`. A live bot in the same organization with the current `analytics:user-activity` scope can fetch a report created by another bot.

Completed reports include `download_url` and `link_expires_at` when the file is available. Follow that URL directly; it contains a derived organization bot file token and needs no additional Authorization header. Downloads use the configured secure file host (`file.notion.com` or `file.notion.so`; local environments use their configured file host).

Links expire after seven days or at the saved file expiry, whichever comes first. Files retain their original 30-day lifetime. Fetch the report again to renew a link while its file remains available. Permissions, credential revocation, and file expiry are checked again when downloading.

Expired or definitively missing files return HTTP 200 with `status: "expired"` and no download URL. Queued, running, and failed reports also omit download URLs. Storage failures and integrity mismatches remain errors.

Treat the full download URL as a credential. Do not log or share it, and avoid sending it in referrers. Report responses and downloaded files use `Cache-Control: private, no-store`.
