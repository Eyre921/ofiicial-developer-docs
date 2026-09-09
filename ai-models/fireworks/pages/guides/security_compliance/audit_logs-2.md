---
title: "Audit & Access Logs"
source: https://docs.fireworks.ai/guides/security_compliance/audit_logs
path: guides/security_compliance/audit_logs
---

Monitor and track account activities with audit logging for Enterprise accounts

Audit logs are available for Enterprise accounts. This feature enhances security visibility, incident investigation, and compliance reporting.

Audit logs include data access logs. All read, write, and delete operations on storage are logged, normalized, and enriched with account context for complete visibility.

## View audit logs with the CLI

You can view audit logs, including data access logs, using the Fireworks CLI:

```bash theme={null}
firectl audit-logs list
```

<Frame>
  <img alt="Audit logs table showing data access activities with columns for timestamp, principal, response code, resource path, and message" />
</Frame>

### Narrow the range

`--start` and `--end` take `YYYY-MM-DD` dates, which the CLI resolves to midnight UTC. Because `--end` lands on the *start* of the day you name, pass the day after the last one you want:

```bash theme={null}
# Everything logged on 2026-08-01 and 2026-08-02
firectl audit-logs list --start 2026-08-01 --end 2026-08-03
```

The CLI works in whole UTC days. Use the [REST API](#retrieve-audit-logs-with-the-rest-api) when you need to bound a query to a specific time of day.

### Filter and format

`--filter` accepts an [AIP-160](https://google.aip.dev/160) expression over `message`, `resource`, `email`, `api_key_id`, `event_type`, and `target_api_key_id`, with `=` for an exact match and `:` for a substring match:

```bash theme={null}
firectl audit-logs list --filter 'email="user@example.com"'
firectl audit-logs list --filter 'message:"Create"'
firectl audit-logs list --start 2026-08-01 --filter 'resource:"my-deployment"'
```

Entries always come back newest first, so `--order-by` has no effect. Add `-o json` to emit machine-readable output instead of the table.

### Paginate with the CLI

By default the CLI prints one page and, when more results may exist, echoes the token to continue with:

```
Pass in '--page-token <token>' to go to the next page.
```

The flag reference describes `--page-token` as a page number, but it takes the opaque token echoed above, so incrementing a counter won't advance you through the results.

To read an entire range in a single command, use `--no-paginate`. It follows the tokens for you and stops only once the search is exhausted, which also means it handles the empty intermediate pages described below:

```bash theme={null}
firectl audit-logs list --start 2026-08-01 --no-paginate -o json
```

See [`firectl audit-logs list`](/tools-sdks/firectl/commands/audit-logs-list) for the complete flag list.

## Retrieve audit logs with the REST API

Use the [List Audit Logs API](/api-reference/list-audit-logs) to retrieve logs for an account. The `startTime` and `endTime` query parameters accept ISO 8601 date-time values.

```bash theme={null}
curl -sS -G "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/auditLogs" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  --data-urlencode "startTime=2026-08-01T00:00:00Z" \
  --data-urlencode "endTime=2026-08-18T23:59:59Z" \
  --data-urlencode "pageSize=200"
```

If you omit `startTime`, the API returns logs from the previous 30 days, and if you omit `endTime`, the range runs through the end of the current day. Both defaults are rounded to UTC day boundaries so that they stay stable across a paginated sequence.

## Paginate through REST results

A response carries at most `pageSize` entries (default 10, maximum 200). To read the next page, resend the same request with `pageToken` set to the `nextPageToken` returned by the previous response. Every other parameter — `startTime`, `endTime`, `filter`, and `pageSize` — must stay identical for the whole sequence, because the token encodes the query it was issued for.

`nextPageToken` is an opaque cursor rather than a page number. Incrementing a counter to jump to "page 3" is not supported and won't return the third page.

### Detecting when results are exhausted

Stop only when a response omits `nextPageToken`. That is the single signal that the search ran to completion.

An empty `auditLogs` array on its own does not mean there is nothing left to read. Fireworks retrieves audit logs by scanning a time-ordered log store, and a scan can cover part of the range without matching anything:

* **`auditLogs: []` with a `nextPageToken`** — the scan is still in progress and hasn't reached matching entries yet. Resend the request with the token to resume it. A single request scans for up to 20 seconds before handing the token back, so this response can take a few seconds to arrive.
* **`auditLogs: []` with no `nextPageToken`** — there are genuinely no more matching entries.

A short page is not an end-of-results signal either: `pageSize` is a ceiling, not a fill target, so a page can hold fewer entries than requested and still be followed by more pages.

<Note>
  `totalSize` is always `0` for audit logs — the number of matching entries isn't known until the scan finishes. Don't use it to size a loop or compute a page count.
</Note>

This loop terminates on the absence of `nextPageToken` and treats empty pages as "keep going":

```bash theme={null}
page_token=""

while :; do
  response=$(curl -sS -G "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/auditLogs" \
    -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
    --data-urlencode "startTime=2026-08-01T00:00:00Z" \
    --data-urlencode "endTime=2026-08-18T23:59:59Z" \
    --data-urlencode "pageSize=200" \
    --data-urlencode "pageToken=${page_token}")

  echo "$response" | jq -c '.auditLogs[]?'

  page_token=$(echo "$response" | jq -r '.nextPageToken // ""')
  [ -n "$page_token" ] || break
done
```
