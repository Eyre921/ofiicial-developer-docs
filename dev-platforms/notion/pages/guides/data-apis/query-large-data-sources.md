---
title: "Query large data sources"
source: https://developers.notion.com/guides/data-apis/query-large-data-sources
path: guides/data-apis/query-large-data-sources
---

Read every page in a data source that holds more rows than the per-query result limit.

A single [data source query](/reference/query-a-data-source) returns at most **10,000 results**. That limit is per query, not per data source: a query is defined by its filter and sort, and once one reaches the limit, pagination stops. `has_more` comes back `false` and the response carries a `request_status` that marks the result as incomplete.

This trips up full exports. A loop that just follows `next_cursor` until `has_more` is `false` looks like it finished, but on a 25,000-row database it quietly returns 10,000 rows. This guide shows how to detect the limit and read every row past it.

A runnable version of everything here is in the [query-large-data-sources cookbook example](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/query-large-data-sources).

## Detect when a query was cut off

Every page of a query response can include a `request_status`. When the result set is capped it is:

```json theme={null}
{
  "request_status": {
    "type": "incomplete",
    "incomplete_reason": "query_result_limit_reached"
  }
}
```

Check every response page as you paginate. Any page with `request_status.type === "incomplete"` means the whole query result was capped, even if that signal appears before the last page you receive.

```typescript TypeScript theme={null}
const response = await notion.dataSources.query({
  data_source_id: dataSourceId,
})

if (response.request_status?.type === "incomplete") {
  // The query hit the 10,000-result limit. Some matching pages were not
  // returned, and following next_cursor will not reach them.
}
```

## Read every row with created\_time windows

Because the limit is per query, you can change the query to get a fresh budget. Split the data source into windows by `created_time`: sort ascending, and each time a window hits the limit, start a new query from the last row's timestamp.

<Steps>
  <Step title="Sort by created_time ascending">
    This gives every window a stable order to walk through.
  </Step>

  <Step title="Page through the window">
    Follow `next_cursor` until `has_more` is `false`. The limit also ends the window, because it sets `has_more` to `false`.
  </Step>

  <Step title="If the window was incomplete, start the next one">
    Filter to `created_time` on or after the last row you saw, and repeat. Rows that share the boundary timestamp appear in both windows, so de-duplicate by row ID.
  </Step>
</Steps>

Use `created_time`, not `last_edited_time`. `created_time` never changes, so windows stay stable. `last_edited_time` shifts as rows are edited, which moves rows between windows and causes gaps or duplicates.

```typescript TypeScript theme={null}
import { Client, isFullPageOrDataSource } from "@notionhq/client"
import type {
  QueryDataSourceParameters,
  QueryDataSourceResponse,
} from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

type DataSourceRow = QueryDataSourceResponse["results"][number]
type DataSourceFilter = QueryDataSourceParameters["filter"]

async function queryAllRows({
  dataSourceId,
  filter,
}: {
  dataSourceId: string
  filter?: DataSourceFilter
}) {
  const rowsById = new Map<string, DataSourceRow>()
  let windowStart: string | undefined

  for (;;) {
    let limitReached = false
    let lastCreatedTime: string | undefined
    let cursor: string | undefined

    // Drain one window. This loop also ends when the limit is hit, because the
    // limit sets has_more (and so next_cursor) to false.
    do {
      const response = await notion.dataSources.query({
        data_source_id: dataSourceId,
        sorts: [{ timestamp: "created_time", direction: "ascending" }],
        filter: buildWindowFilter(filter, windowStart),
        start_cursor: cursor,
        page_size: 100,
      })

      for (const row of response.results) {
        rowsById.set(row.id, row) // de-duplicates boundary rows
        // Pages and child data sources (in wikis) both carry created_time, and
        // either can be the last row in a window, so advance on either.
        if (isFullPageOrDataSource(row)) lastCreatedTime = row.created_time
      }

      if (response.request_status?.type === "incomplete") limitReached = true
      cursor = response.next_cursor ?? undefined
    } while (cursor)

    if (!limitReached) break // the last window finished under the limit
    if (!lastCreatedTime || lastCreatedTime === windowStart) {
      throw new Error(
        `More than the per-query limit share created_time ${lastCreatedTime}. ` +
          "Add another filter to split this window."
      )
    }
    windowStart = lastCreatedTime
  }

  return [...rowsById.values()]
}

function buildWindowFilter(
  filter: DataSourceFilter,
  windowStart: string | undefined
): DataSourceFilter {
  if (windowStart === undefined) return filter

  const windowFilter = {
    timestamp: "created_time",
    created_time: { on_or_after: windowStart },
  } satisfies DataSourceFilter

  if (!filter) return windowFilter
  if ("and" in filter) return { and: [...filter.and, windowFilter] }
  if ("or" in filter) {
    throw new Error("Split top-level or filters into separate windowed queries.")
  }
  return { and: [filter, windowFilter] }
}
```

<Note>
  The Notion JavaScript SDK includes `iterateAllDataSourceRows` and `collectAllDataSourceRows` helpers that wrap this pattern, so you can stream or collect a full data source without writing the windowing loop yourself.
</Note>

## When a window can't be split

Notion stores `created_time` to the minute. If a single minute holds more than 10,000 rows, for example from a bulk import, the window can't advance by time alone, and the loop above throws. Add another filter to narrow each window, such as a status or category your data divides on, so every window stays under the limit.

## When to use a different approach

Windowing reads the whole data source on demand. Two alternatives are often a better fit:

* **Incremental sync.** If you poll a data source on a schedule to catch changes, switch to [connection webhooks](/reference/webhooks). They notify you of changes as they happen, so you never paginate the full data source or hit the limit.
* **Smaller payloads.** If queries are slow rather than truncated, use the `filter_properties` parameter to return only the properties you need. See the [performance recommendations](/reference/query-a-data-source) on the query endpoint.

## Views

The same 10,000-result limit applies to [view queries](/reference/get-view-query-results), but you can't window them. A view query paginates a fixed, already-capped result set and doesn't accept a filter while paginating. To read every row behind a view, query its underlying data source with the approach above. Pass the view's filter into the windowed data source query so you keep the same row set, then apply the view's sort locally after collection if your export needs the exact display order.

A [retrieved view](/reference/retrieve-a-view) tells you which data source it is scoped to, along with the filter and sort it applies. Read those, then run the windowing query against the data source. The windowing query must keep its own `created_time` sort, so don't pass `view.sorts` into `queryAllRows`:

```typescript TypeScript theme={null}
const view = await notion.views.retrieve({ view_id: viewId })

// Dashboard views aren't scoped to a single data source.
if (!view.data_source_id) {
  throw new Error("This view is not scoped to a single data source")
}

const rows = await queryAllRows({
  dataSourceId: view.data_source_id,
  filter: view.filter ?? undefined,
})

// If you need the exact view order, apply view.sorts to rows in your app after
// collection. Don't pass view.sorts to queryAllRows; it must control API sorts.
```

<Note>
  `buildWindowFilter` combines the view filter with the `created_time` lower bound using `and`. If a view has a top-level `or` filter, the sample throws. Run one windowed query per `or` branch and merge rows by ID, or rewrite the view filter as an `and` group, so the window bound does not exceed the API's filter nesting limit.
</Note>

## Related

* [Query a data source](/reference/query-a-data-source) endpoint reference
* [Pagination](/reference/intro#pagination) conventions
* [query-large-data-sources cookbook example](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/query-large-data-sources)
