---
title: "Query a data source"
source: https://developers.notion.com/reference/query-a-data-source
path: reference/query-a-data-source
---

post /v1/data_sources/{data_source_id}/query

### Overview

Gets a list of [pages](/reference/page) contained in the data source, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](/reference/pagination) for details about how to use a cursor to iterate through the list.

> [!NOTE]
>
> **Databases, data sources, and wikis**
>
> [Wiki](https://www.notion.com/help/wikis-and-verified-pages) data sources can contain either pages or databases as children. In all other cases, the children can only be pages.
>
> For wikis, instead of directly returning any [database](/reference/database) results, this API returns all [data sources](/reference/data-source) that are children of *that* database. Surfacing the data source instead of the direct database child helps make it easier to craft your next API request (for example, retrieving the data source or listing its children.)
>
> Another tip for wikis is to use the `result_type` filter of `"page"` or `"data_source"` if you're only looking for query results that are one of those two types instead of both.

### Filtering

Use [filters](/reference/filter-data-source-entries) to match property values. Combine conditions with `and` or `or`. This filter returns rows where **Done** is checked and **Tags** contains A or B.

![The filter requires Done to be checked and Tags to contain A or B.](https://mintcdn.com/notion-demo/S-I3qLQnwRa7HjdK/images/reference/image-6.png?fit=max\&auto=format\&n=S-I3qLQnwRa7HjdK\&q=85\&s=27e3bc94089d8d763ae7de032ded2fa3)

The above filters in the UI can be represented as the following filter object

```json Filter object theme={null}
{
  "and": [
    { "property": "Done", "checkbox": { "equals": true } },
    {
      "or": [
        { "property": "Tags", "multi_select": { "contains": "A" } },
        { "property": "Tags", "multi_select": { "contains": "B" } }
      ]
    }
  ]
}
```

In addition to chained filters, data sources can be queried with single filters.

```json JSON theme={null}
{
    "property": "Done",
    "checkbox": {
        "equals": true
   }
}
```

### Archived pages

Page objects use `is_archived` to indicate whether a page is archived.
Use the top-level `archive_status` body parameter to select active pages, archived pages, or both.

| Value | Results |
| - | - |
| `active` | Non-archived pages. This is the default. |
| `archived` | Archived pages only. |
| `all` | Both active and archived pages. |

```json theme={null}
{
  "archive_status": "all"
}
```

The archive selector applies before property filters, sorts, limits, and pagination.
Use the same selector on every request in a paginated query.

Archive selection does not include pages in Trash or broaden permissions.

### Sorting

[**Sorts**](/reference/sort-data-source-entries) are similar to the [sorts provided in the Notion UI](https://notion.com/notion/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e#0eb303043b1742468e5aff2f3f670505). Sorts operate on database properties or page timestamps and can be combined. The order of the sorts in the request matter, with earlier sorts taking precedence over later ones.

Notion doesn't guarantee any particular sort order when no sort parameters are provided.

### Pagination limit

This endpoint supports paginating through up to **10,000 results** per query. If a data source contains more matching entries than this limit, pagination stops at the 10,000th result: `has_more` becomes `false`, and every response page served from the capped result includes a `request_status` marking the result as incomplete:

```json theme={null}
{
  "request_status": {
    "type": "incomplete",
    "incomplete_reason": "query_result_limit_reached"
  }
}
```

Check `request_status.type === "incomplete"` on every response page to know whether a query was cut off. Any page with that status means the whole query result was capped. The limit is per query (a query is defined by its filter and sort), not per data source.

For connections that need to process all pages in a large data source, we recommend:

* Reading every row past the limit by partitioning the query into `created_time` windows. See [Query large data sources](/guides/data-apis/query-large-data-sources) for the technique and a [runnable cookbook example](https://github.com/makenotion/notion-cookbook/tree/main/examples/query-large-data-sources).
* Using [filters](/reference/filter-data-source-entries) to narrow the result set (e.g. filter by `last_edited_time` to fetch only recently changed pages).
* Setting up [connection webhooks](/reference/webhooks) for incremental sync instead of polling the full data source on a schedule.

> [!WARNING]
>
> **Incremental sync via webhooks**
>
> If your connection polls this endpoint on a recurring schedule to detect changes, consider switching to [connection webhooks](/reference/webhooks) instead. Webhooks notify your connection of changes in real time, eliminating the need to paginate through the entire data source. This is faster, more efficient, and avoids hitting the pagination limit.

### Recommendations for performance

Pass `filter_properties` once per property in the query string, or pass an array of strings in the SDK. Use property names or IDs from [Retrieve a data source](/reference/retrieve-a-data-source). For example, for a data source with a **Status** property:

```bash curl theme={null}
curl -X POST "https://api.notion.com/v1/data_sources/$NOTION_DATA_SOURCE_ID/query?filter_properties=title&filter_properties=Status" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11" \
  -H "Content-Type: application/json" \
  --data '{}'
```

```javascript JavaScript theme={null}
import { Client } from "@notionhq/client";

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const response = await notion.dataSources.query({
  data_source_id: process.env.NOTION_DATA_SOURCE_ID,
  filter_properties: ["title", "Status"],
});
console.log(response.results);
```

Using `filter_properties` can speed up the query and reduce its response size, especially for data sources with many properties, formulas, rollups, or relations. Use this endpoint to find pages and return only the properties your list shows. Fetch more data after you select a page:

* Call [Retrieve a page](/reference/retrieve-a-page) with the returned page ID to get more properties from one page. You can also pass `filter_properties` to that endpoint.
* Call [Retrieve a page property](/reference/retrieve-a-page-property) with the page and property IDs to retrieve one property. Use it when a formula, rollup, or relation contains more than 25 references.

This example lists 10 pages with their title and **Status**, then reads a **Total hours** rollup for each one:

```javascript JavaScript theme={null}
import { Client } from "@notionhq/client";

// The SDK retries 429 and 529 responses and waits for Retry-After.
const notion = new Client({
  auth: process.env.NOTION_API_KEY,
  notionVersion: "2026-03-11",
});

// Step 1: list 10 pages with only the properties the list shows.
const list = await notion.dataSources.query({
  data_source_id: process.env.NOTION_DATA_SOURCE_ID,
  filter_properties: ["title", "Status"],
  result_type: "page",
  page_size: 10,
});
// To show the next 10, send list.next_cursor as start_cursor.

// Step 2: fetch the expensive rollup for each page you show.
for (const { id } of list.results) {
  const page = await notion.pages.retrieve({
    page_id: id,
    filter_properties: ["Total hours"],
  });
  console.log(id, JSON.stringify(page.properties["Total hours"]));
}
```

```python Python theme={null}
import os
import time

import requests

API_URL = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
    "Notion-Version": "2026-03-11",
}


def notion(method, path, **kwargs):
    for attempt in range(5):
        response = requests.request(method, API_URL + path, headers=HEADERS, **kwargs)
        if response.status_code not in (429, 529):
            break
        time.sleep(int(response.headers.get("Retry-After", 2**attempt)))
    response.raise_for_status()
    return response.json()


# Step 1: list 10 pages with only the properties the list shows.
listing = notion(
    "POST",
    f"/data_sources/{os.environ['NOTION_DATA_SOURCE_ID']}/query",
    params={"filter_properties": ["title", "Status"]},
    json={"result_type": "page", "page_size": 10},
)
# To show the next 10, send listing["next_cursor"] as start_cursor.

# Step 2: fetch the expensive rollup for each page you show.
for summary in listing["results"]:
    page = notion(
        "GET",
        f"/pages/{summary['id']}",
        params={"filter_properties": ["Total hours"]},
    )
    print(summary["id"], page["properties"]["Total hours"])
```

```go Go theme={null}
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"strconv"
	"time"
)

const apiURL = "https://api.notion.com/v1"

type page struct {
	ID         string                     `json:"id"`
	Properties map[string]json.RawMessage `json:"properties"`
}

func notion(method, path string, query url.Values, body any, out any) error {
	var payload []byte
	if body != nil {
		var err error
		if payload, err = json.Marshal(body); err != nil {
			return err
		}
	}
	for attempt := 0; ; attempt++ {
		request, err := http.NewRequest(method, apiURL+path+"?"+query.Encode(), bytes.NewReader(payload))
		if err != nil {
			return err
		}
		request.Header.Set("Authorization", "Bearer "+os.Getenv("NOTION_API_KEY"))
		request.Header.Set("Notion-Version", "2026-03-11")
		request.Header.Set("Content-Type", "application/json")
		response, err := http.DefaultClient.Do(request)
		if err != nil {
			return err
		}
		retryable := response.StatusCode == 429 || response.StatusCode == 529
		if retryable && attempt < 4 {
			response.Body.Close()
			seconds, err := strconv.Atoi(response.Header.Get("Retry-After"))
			if err != nil {
				seconds = 1 << attempt
			}
			time.Sleep(time.Duration(seconds) * time.Second)
			continue
		}
		defer response.Body.Close()
		if response.StatusCode >= 300 {
			return fmt.Errorf("Notion API returned %s", response.Status)
		}
		return json.NewDecoder(response.Body).Decode(out)
	}
}

func main() {
	// Step 1: list 10 pages with only the properties the list shows.
	var list struct {
		Results    []page  `json:"results"`
		NextCursor *string `json:"next_cursor"`
	}
	path := "/data_sources/" + os.Getenv("NOTION_DATA_SOURCE_ID") + "/query"
	query := url.Values{"filter_properties": {"title", "Status"}}
	body := map[string]any{"result_type": "page", "page_size": 10}
	if err := notion(http.MethodPost, path, query, body, &list); err != nil {
		panic(err)
	}
	// To show the next 10, send list.NextCursor as start_cursor.

	// Step 2: fetch the expensive rollup for each page you show.
	for _, summary := range list.Results {
		var full page
		query := url.Values{"filter_properties": {"Total hours"}}
		if err := notion(http.MethodGet, "/pages/"+summary.ID, query, nil, &full); err != nil {
			panic(err)
		}
		fmt.Println(summary.ID, string(full.Properties["Total hours"]))
	}
}
```

Don't fetch every property for every result unless you need all of them.

If you're still running into long query times with this API, other tips include:

* Using more specific filter conditions to reduce the result set, e.g. a more specific title query or a shorter time window.
* Dividing large data sources (ones with more than several dozen thousand pages) into multiple; e.g. splitting a "tasks" database into "Tasks" and "Bugs".
* Pruning data source schemas to remove any complex formulas, rollups, two-way relations, or other properties that are no longer in use.
* Setting up [connection webhooks](/reference/webhooks) to reduce the need for polling this API by instead automatically notifying your system of incremental workspace events.

For more information, visit our [help center article on optimizing database load times](https://www.notion.com/help/optimize-database-load-times-and-performance).

### Other important details and tips

> [!NOTE]
>
> **Permissions**
>
> Before a connection can query a data source, its parent database must be shared with the connection. Attempting to query a data source in a database that has not been shared will return an HTTP response with a 404 status code.
>
> To share a database with a connection, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the connection from the dropdown list.

> [!NOTE]
>
> **Connection capabilities**
>
> This endpoint requires a connection to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).

> [!NOTE]
>
> **To display the page titles of related pages rather than just the ID:**
>
> 1. Add a rollup property to the data source which uses a formula to get the related page's title. This works well if you have access to [update](/reference/update-a-data-source) the data source's schema.
> 2. Otherwise, [retrieve the individual related pages](/reference/retrieve-a-page) using each page ID.

> [!WARNING]
>
> **Formula and rollup limitations**
>
> * If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
> * Rollups and formulas that depend on multiple layers of relations may not return correct results.
> * Notion recommends individually [retrieving each page property item](/reference/retrieve-a-page-property) to get the most accurate result.

### Errors

Returns a 404 HTTP response if the data source doesn't exist, or if the connection doesn't have access to the data source.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

Returns a 503 HTTP response if the data source query is temporarily unavailable due to backend datastore timeouts. The response body includes an `additional_data` object with retry guidance:

```json 503 response example theme={null}
{
  "object": "error",
  "status": 503,
  "code": "service_unavailable",
  "message": "Public API data source query is temporarily unavailable due to backend datastore timeouts. Retry with exponential backoff; if retries continue to fail, reduce page_size or narrow filters/sorts.",
  "additional_data": {
    "endpoint_name": "public_queryDataSource",
    "notion_error_name": "PgPoolWaitConnectionTimeout",
    "retry_guidance": [
      "Use exponential backoff with jitter",
      "Reduce page_size",
      "Narrow query filters/sorts"
    ]
  }
}
```

> [!CAUTION]
>
> **Note**: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
