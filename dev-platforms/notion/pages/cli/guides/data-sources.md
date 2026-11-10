---
title: "Data sources"
source: https://developers.notion.com/cli/guides/data-sources
path: cli/guides/data-sources
---

Create, query, and manage data sources from the terminal.

A [data source](/reference/data-source) is a table of pages under a Notion database. For background on how databases and data sources fit together, see [Working with databases](/guides/data-apis/working-with-databases).

[Log in to the CLI](/cli/get-started/authentication) before you start.

## Find a data source ID

Set `DATABASE_ID` to the [ID of the parent database](/guides/data-apis/working-with-databases#adding-pages-to-a-data-source). List its data sources with this command.

```bash theme={null}
ntn api "v1/databases/$DATABASE_ID"
```

Find your data source in the response's `data_sources` array and set `DATA_SOURCE_ID` to its `id`. In Notion, you can also find the ID under **Manage data sources** in the database settings. Open the data source's `•••` menu and select **Copy data source ID**.

## Retrieve a data source

Fetch the schema (properties, title, parent) for a single data source. See [Retrieve a data source](/reference/retrieve-a-data-source) for the response shape:

```bash theme={null}
ntn api "v1/data_sources/$DATA_SOURCE_ID"
```

## Create a data source

To add a data source, pass the parent database ID and define each column in `properties`. See [Create a data source](/reference/create-a-data-source) for the full list of fields.

```bash theme={null}
ntn api v1/data_sources \
  'parent[type]=database_id' \
  "parent[database_id]=$DATABASE_ID" \
  'title[0][type]=text' \
  'title[0][text][content]=Bugs' \
  properties:='{"Name":{"title":{}},"Status":{"select":{"options":[{"name":"Open","color":"red"},{"name":"Closed","color":"green"}]}},"Priority":{"number":{"format":"number"}}}'
```

A default "table" view is created alongside the data source. See [Working with views](/guides/data-apis/working-with-views) to learn about managing views.

## Query a data source

Use `ntn datasources query` to list pages in a data source:

```bash theme={null}
ntn datasources query "$DATA_SOURCE_ID" --limit 50
```

Pass `--filter` with the same shape documented in [Filter data source entries](/reference/filter-data-source-entries):

```bash theme={null}
ntn datasources query "$DATA_SOURCE_ID" --filter '{"property":"Status","select":{"equals":"Open"}}'
```

Paginate with `--start-cursor` using the `next_cursor` from the previous response. Add `--json` for machine-readable output.

To use the [query endpoint](/reference/query-a-data-source) directly, pass the filter and sort order in the request body.

```bash theme={null}
ntn api "v1/data_sources/$DATA_SOURCE_ID/query" \
  filter:='{"and":[{"property":"Status","select":{"equals":"Open"}},{"property":"Priority","number":{"greater_than_or_equal_to":2}}]}' \
  sorts:='[{"property":"Priority","direction":"descending"}]' \
  page_size:=25
```

To return fewer columns, pass `filter_properties` once for each property name or ID you need.

```bash theme={null}
ntn api "v1/data_sources/$DATA_SOURCE_ID/query" --data '{}' \
  filter_properties==title filter_properties==Status
```

While `has_more` is `true`, pass `next_cursor` as `start_cursor` in the next request. If your query reaches the 10,000-result limit, follow [Query large data sources](/guides/data-apis/query-large-data-sources) to read the remaining pages.

## Update a data source

`PATCH` updates the title, description, parent, or schema. To add a column, pass it under `properties` keyed by name:

```bash theme={null}
ntn api "v1/data_sources/$DATA_SOURCE_ID" -X PATCH \
  title:='[{"type":"text","text":{"content":"Bugs (Q2)"}}]' \
  properties:='{"Assignee":{"people":{}}}'
```

To rename or remove a property, key it by its existing name and pass either a new `name` or `null`:

```bash theme={null}
ntn api "v1/data_sources/$DATA_SOURCE_ID" -X PATCH \
  properties:='{"Priority":{"name":"Severity"},"Notes":null}'
```

See [Update a data source](/reference/update-a-data-source) for the full list of editable fields and properties that can't be changed via the API.

## List page templates

List the page templates that show up in a data source's **New** dropdown. See [List data source templates](/reference/list-data-source-templates) for the response shape:

```bash theme={null}
ntn api "v1/data_sources/$DATA_SOURCE_ID/templates"
```

Set `TEMPLATE_ID` to a template ID from the response, then [retrieve the page](/reference/retrieve-a-page):

```bash theme={null}
ntn api "v1/pages/$TEMPLATE_ID"
```

## Discover the endpoints

To see the request schema or jump to the docs for any of these commands:

```bash theme={null}
ntn api v1/data_sources --spec -X POST
ntn api v1/data_sources --docs -X POST
```
