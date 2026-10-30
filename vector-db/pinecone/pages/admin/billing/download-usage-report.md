---
title: "Download a usage report"
source: https://docs.pinecone.io/admin/billing/download-usage-report
path: admin/billing/download-usage-report
---

Download a usage and cost report for your Pinecone organization from the console, or export one with the Admin API.

> [!NOTE]
>
> To view usage and costs across your Pinecone organization, you must be an [organization owner or billing admin](/admin/organizations/understanding-organizations#organization-roles). Also, this feature is available only to organizations on the Standard or Enterprise plans.

The **Usage** dashboard in the Pinecone console reports usage and costs across your organization. On the page you can group the charts by SKU or project and switch the cost distribution between services. The CSV download covers whichever time range you select, regardless of how you group the charts.

> [tab] Pinecone console
>
> 1. In the top-right navigation of the Pinecone console, go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage).
> 2. Select the time range to report on. This defaults to the current month, or to the previous month during the first five days of a month.
> 3. Click **Download**.
>
>    On Standard plans, the report downloads right away.
>
>    On Enterprise plans, choose **Download CSV** from the menu. The export runs in the background and appears in the list on the page. When it finishes, click **Click to download** on its entry.
>
>    > [!TIP]
>    >
>    > The download provides more granular detail than the console view, including breakdowns by individual index as well as project and index tags.
>
> On Enterprise plans, exports you create through the Admin API appear in that same list.

> [tab] Code
>
> > [!NOTE]
> >
> > Exporting through the Admin API is available only on [Enterprise plans](https://www.pinecone.io/pricing/) and requires an [access token](/admin/organizations/manage-service-accounts#retrieve-an-access-token).
>
> Exporting with the Admin API takes three requests: create the export, poll it until it finishes, then download the file.
>
> **1. Create the export**
>
> An export covers whole UTC calendar days, each written as `YYYY-MM-DD`. `period_start` is the first day you want and can be no earlier than 365 days before today. `period_end` is the day *after* the last day you want, so `2026-08-01` through `2026-09-01` covers all of August. Omit the request body to export the trailing 30 complete days.
>
> ```bash curl theme={null}
> PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
>
> curl -X POST "https://api.pinecone.io/admin/cost-usage-exports" \
>      -H "X-Pinecone-Api-Version: 2026-07" \
>      -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
>      -H "Content-Type: application/json" \
>      -d '{
>            "period_start": "2026-08-01",
>            "period_end": "2026-09-01"
>          }'
> ```
>
> The export is recorded but hasn't run yet, so the response returns `"status": "Pending"` and the file fields are empty:
>
> ```json theme={null}
> {
>   "id": "9f2c1a4e-8b3d-4c5f-a1b2-c3d4e5f6a7b8",
>   "status": "Pending",
>   "format": "zip",
>   "period_start": "2026-08-01",
>   "period_end": "2026-09-01",
>   "data_available_through": null,
>   "row_count": null,
>   "size_bytes": null,
>   "download_url": null,
>   "download_url_expires_at": null,
>   "file_expires_at": null,
>   "file_expired": false,
>   "error": null,
>   "created_at": "2026-09-02T14:31:07.482910355Z",
>   "started_at": null,
>   "finished_at": null,
>   "updated_at": "2026-09-02T14:31:07.482910355Z"
> }
> ```
>
> An organization can run only one export at a time. Starting another while one is `Pending` or `InProgress` returns a `409`. An organization can also start at most five exports per hour. Going over that returns a `429` with a `Retry-After` header.
>
> **2. Poll until the export finishes**
>
> Use the `id` from the previous step to check on the export.
>
> ```bash curl theme={null}
> EXPORT_ID="9f2c1a4e-8b3d-4c5f-a1b2-c3d4e5f6a7b8"
>
> curl -X GET "https://api.pinecone.io/admin/cost-usage-exports/$EXPORT_ID" \
>      -H "X-Pinecone-Api-Version: 2026-07" \
>      -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
> ```
>
> `status` moves from `Pending` to `InProgress`, and then to either `Completed` or `Failed`. Both of those are terminal and never change afterward. When the export completes, the response carries the file's size, row count, and download link:
>
> ```json theme={null}
> {
>   "id": "9f2c1a4e-8b3d-4c5f-a1b2-c3d4e5f6a7b8",
>   "status": "Completed",
>   "format": "zip",
>   "period_start": "2026-08-01",
>   "period_end": "2026-09-01",
>   "data_available_through": "2026-08-31",
>   "row_count": 48213,
>   "size_bytes": 4183902,
>   "download_url": "https://storage.googleapis.com/example-bucket/cost_usage_exports/export.zip?X-Goog-Expires=3600&X-Goog-Signature=abc123",
>   "download_url_expires_at": "2026-09-02T15:36:11.237604891Z",
>   "file_expires_at": "2026-09-04T14:35:52.904155718Z",
>   "file_expired": false,
>   "error": null,
>   "created_at": "2026-09-02T14:31:07.482910355Z",
>   "started_at": "2026-09-02T14:31:19.118374902Z",
>   "finished_at": "2026-09-02T14:35:52.904155718Z",
>   "updated_at": "2026-09-02T14:36:11.237604891Z"
> }
> ```
>
> `data_available_through` is the date of the most recent usage row in the export. Because cost data lags behind usage, it can be earlier than the `period_end` you asked for.
>
> **3. Download the file**
>
> `download_url` is a signed link to a zip archive. The archive holds the cost records as one or more CSV files whose columns follow the [FOCUS v1.4](https://focus.finops.org/) Cost and Usage dataset. Each CSV starts with a header line and holds at most 800,000 rows, so a large export is split across several files, named `part-1-of-3.csv` through `part-3-of-3.csv` and ordered by those names. The numbers are zero-padded once an export runs to ten or more parts, so a 12-part export starts at `part-01-of-12.csv`.
>
> The archive also holds a `manifest.json` listing the export's window, `row_count`, the 45 column names, and each part with its own row count.
>
> FOCUS uses its own names for the things being billed, so Pinecone's organization, project, and index appear under FOCUS columns rather than under the headings you see in the console:
>
> | Pinecone | FOCUS columns |
> | - | - |
> | Organization | `x_OrganizationId` for the ID, `BillingAccountName` for the name |
> | Project | `SubAccountId`, `SubAccountName` |
> | Resource | `ResourceId`, `ResourceName`, with `ResourceType` naming the kind |
>
> `BillingAccountId` holds your billing customer ID, which isn't the same as your Pinecone organization ID.
>
> Most rows describe an index, but an export also covers other resources, so `ResourceType` can be `index`, `assistant`, `backup`, `collection`, or `model`. Rows for fixed fees leave it empty.
>
> Columns prefixed with `x_` are Pinecone extensions, which is how FOCUS requires a provider to name a column the specification doesn't define. For the full column list, see [Create a cost usage export](/reference/api/latest/admin/cost-usage-exports/create-a-cost-usage-export).
>
> ```bash curl theme={null}
> DOWNLOAD_URL="YOUR_DOWNLOAD_URL"
>
> curl -o cost-usage-export.zip "$DOWNLOAD_URL"
> ```
>
> Pinecone generates a new link each time you read a single export, and each link is valid for one hour. `download_url_expires_at` tells you when the current one stops working. To get a fresh link, read the export again. Treat the link as a secret while it's valid, since anyone who has it can download the file.
>
> Pinecone deletes the file itself two days after the export finishes, and you can't download it again. Check `file_expired` rather than `status` to know whether the file is still there, because a `Completed` export whose file has expired can no longer be downloaded. Create another export instead.
>
> To see the exports your organization has already run, use [List cost usage exports](/reference/api/latest/admin/cost-usage-exports/list-cost-usage-exports). List responses always return `download_url` as `null`, so read a single export when you need a link.

Dates are shown in UTC to match billing invoices. Cost data is delayed up to three days from the actual usage date.
