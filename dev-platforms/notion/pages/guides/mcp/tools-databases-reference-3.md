---
title: "Manage databases and views — technical reference"
source: https://developers.notion.com/guides/mcp/tools-databases-reference
path: guides/mcp/tools-databases-reference
---

Find parameters for Notion MCP databases, data sources, views, and queries, including filters and access requirements.

## Create a database

`notion-create-database`

Creates a new Notion database, initial data source, and initial view with the specified properties.

## Update a data source

`notion-update-data-source`

Update a Notion data source's properties, name, description, or other attributes.

To change a `select`, `multi_select`, or `status` property, list every option to keep. Omitted options are removed. Existing options keep their IDs and can be recolored, and `status` options keep their group when you omit it.

Pass `page_layout` to replace the layout that every page in the data source uses, such as pinned properties, the sidebar, and property sections. Fetch the data source first to get its current layout, then edit it. Read the `notion://docs/database-page-layouts` MCP resource for the format. Change properties and the page layout in separate calls. A call that does both returns a `validation_error`.

## Create a view

`notion-create-view`

Create a new view on a Notion database. Supports table, board, list, calendar, timeline, gallery, form, chart, map, and dashboard view types. Use the optional configuration DSL for filters, sorts, grouping, and display options.

The tool can also add a linked view of a data source to a page. Set `show_data_source_title` to `false` to hide the data source title above that linked view, like turning off **Show data source title** in the Notion app.

> [!NOTE]
>
> Use a page URL or ID for relation filters. Use a user ID or `"me"` for person, created-by, and last-edited-by filters. Use an option or group name for status filters, and use `"verified"`, `"expired"`, or `"none"` for verification filters. Page and people names aren't accepted, so resolve them to a URL or ID first. Read the `notion://docs/view-dsl-spec` resource for the full syntax.

## Update a view

`notion-update-view`

Update a view's name, filters, sorts, or display configuration. Only the fields you specify will be changed. Supports clearing existing configuration like filters, sorts, and grouping. Uses the same configuration DSL — and the same filter value formats — as `notion-create-view`.

## Query across data sources

`notion-query-data-sources`

Query Notion data sources with SQL, read rows from one data source, or run a saved view.

Pass `mode: "rows"` and `data_source_url` to read one data source. Rich-text properties use [Notion markdown](/guides/data-apis/enhanced-markdown) strings to preserve page and user mentions, link targets, formatting, inline dates, and equations.

Rows mode accepts optional `filter` and `sort` fields. A filter supports two levels of `and` or `or` groups. Sorts run in listed order. `limit` defaults to 50 and has a maximum of 100.

The response contains `results` and `has_more`. Each result uses property names as keys. Results include only rows and properties that the connected user can read. Rows mode does not return a cursor.

A query can resolve up to 1,000 distinct mention targets. A query over this limit returns an error instead of partial rich text.

> [!WARNING]
>
> SQL output can omit mention text, link targets, and formatting. Their absence in SQL output does not mean that a rich-text property is damaged. Read the property with rows mode or `notion-fetch` before changing it.

> [!NOTE]
>
> View mode is available on every plan without a tool-specific quota. SQL across one or more data sources is unlimited on Business and Enterprise plans with Notion AI. Other plans share a per-workspace usage limit for single-data-source SQL and receive an upgrade prompt after the allowance is exhausted. Rows mode uses the same allowance as single-data-source SQL.

## Query multiple data sources

`notion-query-multiple-data-sources`

Runs one read-only SQLite query across 2 to 100 data sources, for joins, unions, comparisons, and totals. Fetch each data source first with `notion-fetch` to get its schema and `collection://` URL. Pass the URLs in `data_source_urls` and use each one as a quoted table name in `query`. Bind untrusted values with `?` placeholders and `params` instead of putting them in the SQL. Saved view filters and sorts aren't applied, so put every filter in `WHERE`.

The response contains the matching rows, the IDs of the queried data sources, and whether the results were truncated. SQL output can omit mention text, link targets, and formatting, the same as SQL in `notion-query-data-sources`. To read one data source or run a saved view, use `notion-query-data-sources`.

> [!NOTE]
>
> Requires a Business or Enterprise plan with Notion AI. On other plans the call doesn't run the query. It returns an error that says the tool needs the full version of Notion MCP and links to the next step. To check before you call, read the tool's entry in `notion-get-tool-access`.

## Delete databases

`notion-delete-databases`

Move up to 20 Notion databases to Trash, with all of their rows. Each one must be a full-page or inline database that owns its data, not a linked view. To move a page or a single row to Trash, use `notion-delete-pages`. Items in Trash can be restored with `notion-restore-pages` or from Trash in Notion. Locked databases can't be moved to Trash; unlock them in Notion first.

The call must set `user_confirmed: true`. Without it, nothing is moved to Trash, and the error lists the databases and their row counts so the MCP client can confirm them with the user. The tool is marked destructive (`destructiveHint: true`), so MCP clients that honor tool annotations ask before running it. Requires the update content [capability](/reference/capabilities).
