---
title: "Working with views"
source: https://developers.notion.com/guides/data-apis/working-with-views
path: guides/data-apis/working-with-views
---

Learn how to set up and manage database views using the Notion API.

<Info>
  The Views API requires API version `2025-09-03` or later. If your connection uses an older version, see the [upgrade guide](/guides/get-started/upgrade-guide-2025-09-03) for migration steps.
</Info>

## Overview

[Database views](https://www.notion.com/help/views-filters-and-sorts) let users see the same data in different ways — for example, as a table, board, calendar, timeline, gallery, list, form, chart, map, or dashboard. Each view can have its own filters, sorts, and layout configuration, so a single database can serve many different workflows.

The Notion API exposes views as first-class resources. This means connections can programmatically manage the same view presets that users create in the UI, enabling use cases like workspace bootstrapping, migration tooling, and automated view setup.

In this guide, you'll learn:

<CardGroup>
  <Card title="How views relate to databases and data sources." href="#structure" icon="angles-right" />

  <Card title="What happens by default when you create a database." href="#default-behavior" icon="angles-right" />

  <Card title="How to list, create, and delete views." href="#listing-views" icon="angles-right" />

  <Card title="How to configure view-specific settings." href="#view-configuration" icon="angles-right" />

  <Card title="How to create and manage dashboard views." href="#dashboard-views" icon="angles-right" />

  <Card title="How to query data through a view." href="#querying-a-view" icon="angles-right" />
</CardGroup>

## Structure

A **view** is scoped to a single [data source](/reference/data-source) within a [database](/reference/database). It defines how pages in that data source are filtered, sorted, and displayed.

The view object looks like this:

<CodeGroup>
  ```json View object example expandable theme={null}
  {
    "object": "view",
    "id": "a3f1b2c4-5678-4def-abcd-1234567890ab",
    "parent": {
      "type": "database_id",
      "database_id": "248104cd-477e-80fd-b757-e945d38000bd"
    },
    "data_source_id": "248104cd-477e-80af-bc30-000bd28de8f9",
    "name": "High priority items",
    "type": "table",
    "filter": {
      "property": "Priority",
      "select": {
        "equals": "High"
      }
    },
    "sorts": [
      {
        "property": "Last ordered",
        "direction": "descending"
      }
    ],
    "quick_filters": {
      "Status": {
        "status": { "equals": "In progress" }
      }
    },
    "configuration": {
      "type": "table",
      "properties": [
        { "property_id": "title", "visible": true, "width": 300 },
        { "property_id": "abc1", "visible": true, "width": 200 },
        { "property_id": "def2", "visible": false }
      ],
      "group_by": {
        "type": "status",
        "property_id": "ghi3",
        "group_by": "group",
        "sort": { "type": "manual" }
      },
      "wrap_cells": false,
      "frozen_column_index": 1,
      "show_vertical_lines": true
    },
    "created_time": "2026-01-15T10:30:00.000Z",
    "last_edited_time": "2026-01-20T14:22:00.000Z",
    "created_by": {
      "object": "user",
      "id": "e7f3a4b2-1234-5678-9abc-def012345678"
    },
    "last_edited_by": {
      "object": "user",
      "id": "e7f3a4b2-1234-5678-9abc-def012345678"
    },
    "url": "https://www.notion.com/example/248104cd477e80fdb757e945d38000bd?v=a3f1b2c45678"
  }
  ```
</CodeGroup>

Key fields:

* **`type`** — The layout type. One of: `table`, `board`, `list`, `calendar`, `timeline`, `gallery`, `form`, `chart`, `map`, or `dashboard`.
* **`data_source_id`** — Which data source this view is "over". A database can have multiple data sources, and each view targets exactly one. For dashboard views this is `null` since dashboards contain multiple widget views, each with their own data source.
* **`filter`** and **`sorts`** — Use the same shapes as the [filter](/reference/filter-data-source-entries) and [sort](/reference/sort-data-source-entries) parameters in data source queries.
* **`quick_filters`** — A map of property-level filters that appear in the view's filter bar. Keys are property names or IDs, values are filter conditions (same shape as property filters, without the `property` field), or an empty object for a quick filter without criteria. See [Quick filters](#quick-filters).
* **`configuration`** — Type-specific presentation settings that vary by view type. This is a discriminated union keyed on `type` — see [View configuration](#view-configuration) for the full schema per view type. This field is `null` when no custom configuration has been set.
* **`parent`** — Always a database. Views are retrieved and managed through their parent database.
* **`dashboard_view_id`** — Only present on widget views that belong to a dashboard. References the parent dashboard view's ID.

## Default behavior

When you [create a database](/reference/create-database) through the API, Notion automatically provisions:

1. One **data source** under the database container
2. One **Table view** named "Default view" over that data source

This means every newly created database is immediately usable — it has a data source to hold pages and a view to display them.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.notion.com/v1/databases \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "parent": { "type": "page_id", "page_id": "YOUR_PAGE_ID" },
      "title": [{ "type": "text", "text": { "content": "My Database" } }],
      "is_inline": false
    }'
  ```

  ```javascript JavaScript theme={null}
  const { Client } = require("@notionhq/client");

  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  const database = await notion.databases.create({
    parent: { type: "page_id", page_id: "YOUR_PAGE_ID" },
    title: [{ type: "text", text: { content: "My Database" } }],
    is_inline: false,
  });

  // database.data_sources[0].id is the auto-created data source
  ```
</CodeGroup>

After creating the database, you can [list the views](#listing-views) to discover the default view, then create additional views as needed.

## Listing views

Use the [list endpoint](/reference/list-views) to discover views. You can filter by the view's parent `database_id` or by the `data_source_id` that the view references.

### By database

Pass `database_id` to list the views belonging to a specific database block.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET "https://api.notion.com/v1/views?database_id=DATABASE_ID" \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.views.list({
    database_id: "DATABASE_ID",
  });

  for (const view of response.results) {
    console.log(view.id);
  }
  ```
</CodeGroup>

### By data source

Pass `data_source_id` to list all views that reference a given data source (collection), including linked views on other pages across the workspace.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET "https://api.notion.com/v1/views?data_source_id=DATA_SOURCE_ID" \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const response = await notion.views.list({
    data_source_id: "DATA_SOURCE_ID",
  });

  for (const view of response.results) {
    console.log(view.id);
  }
  ```
</CodeGroup>

<Info>
  Results are filtered by your connection's access permissions. Views on pages the connection cannot access are excluded.
</Info>

Both variants return a paginated list of view references:

```json theme={null}
{
  "object": "list",
  "results": [
    { "object": "view", "id": "a3f1b2c4-5678-4def-abcd-1234567890ab" },
    { "object": "view", "id": "b4e2c3d5-6789-5ef0-bcde-2345678901bc" }
  ],
  "next_cursor": null,
  "has_more": false
}
```

<Info>
  The list endpoint returns minimal view references (just `object` and `id`). To get full view details including filters, sorts, and configuration, retrieve each view individually.
</Info>

## Retrieving a view

[Retrieve a view](/reference/retrieve-a-view) by its ID to see its full configuration, including filters, sorts, and layout settings.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET https://api.notion.com/v1/views/VIEW_ID \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const view = await notion.views.retrieve({
    view_id: "VIEW_ID",
  });

  console.log(view.name);            // "High priority items"
  console.log(view.type);            // "table"
  console.log(view.configuration);   // { type: "table", properties: [...], ... }
  ```
</CodeGroup>

The response is a full [view object](#structure).

## Creating a view

Create a new view by specifying the target data source, a name, and a view type. You must also provide one of `database_id` (to create a top-level view on a database), `view_id` (to add a widget view to an existing dashboard), or `create_database` (to create a linked database view on a page). You can optionally include filters, sorts, and a [configuration](#view-configuration) object. For the full parameter reference, see [Create a view](/reference/create-view).

<Note>
  `database_id` and `data_source_id` are different IDs. The `database_id` is the database container's ID (the same ID returned by the [Retrieve a database](/reference/retrieve-a-database) endpoint). The `data_source_id` is the ID of a specific data source within that database (found in the database's `data_sources` array). Most databases have a single data source, but both IDs are required.
</Note>

<CodeGroup>
  ```bash cURL expandable theme={null}
  curl -X POST https://api.notion.com/v1/views \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "database_id": "DATABASE_ID",
      "data_source_id": "DATA_SOURCE_ID",
      "name": "Recent orders",
      "type": "table",
      "filter": {
        "property": "Last ordered",
        "date": {
          "past_week": {}
        }
      },
      "sorts": [
        {
          "property": "Last ordered",
          "direction": "descending"
        }
      ],
      "configuration": {
        "type": "table",
        "properties": [
          { "property_id": "title", "visible": true, "width": 300 },
          { "property_id": "abc1", "visible": true, "width": 200 }
        ],
        "wrap_cells": true
      }
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  const view = await notion.views.create({
    database_id: "DATABASE_ID",
    data_source_id: "DATA_SOURCE_ID",
    name: "Recent orders",
    type: "table",
    filter: {
      property: "Last ordered",
      date: {
        past_week: {},
      },
    },
    sorts: [
      {
        property: "Last ordered",
        direction: "descending",
      },
    ],
    configuration: {
      type: "table",
      properties: [
        { property_id: "title", visible: true, width: 300 },
        { property_id: "abc1", visible: true, width: 200 },
      ],
      wrap_cells: true,
    },
  });

  console.log(view.id);  // The new view's ID
  console.log(view.url); // Deep link to the view in Notion
  ```
</CodeGroup>

The response is the newly created [view object](#structure) with all fields populated.

<Tip>
  Views in a database can be configured to show pages from a data source that's owned by another database. In Notion, this is called a [linked database](https://www.notion.com/help/data-sources-and-linked-databases) (or linked view), and it's useful for showing the same underlying data in multiple places—for example, putting filtered views of your Tasks, Projects, and Bugs on a single dashboard page.

  In the API, the main requirement is that your connection has access to both the database that owns the data source, and the database you're creating the view in.
</Tip>

<Tip>
  **Filtering by multiple select or status values**

  Select, status, and multi\_select filter operators accept an array of strings to filter by multiple values at once. For example, to match Priority "Low" or "Medium":

  ```json theme={null}
  {
    "filter": {
      "property": "Priority",
      "select": { "equals": ["Low", "Medium"] }
    }
  }
  ```

  You can also exclude multiple values:

  ```json theme={null}
  {
    "filter": {
      "property": "Status",
      "status": { "does_not_equal": ["Done", "Archive"] }
    }
  }
  ```

  The API validates each value in the array against the property's configured options. For status properties, group names (e.g. "To-do", "In progress", "Complete") are also accepted. If any value doesn't match an existing option or group, the API returns a descriptive error listing the available values.
</Tip>

### Required parameters

| Parameter | Description |
| - | - |
| `data_source_id` | The ID of the data source this view is over. Retrieve this from the database object's `data_sources` array. |
| `name` | A display name for the view. |
| `type` | The view layout: `table`, `board`, `list`, `calendar`, `timeline`, `gallery`, `form`, `chart`, `map`, or `dashboard`. |

### Optional parameters

| Parameter | Description |
| - | - |
| `database_id` | The ID of the database to create the view in. Mutually exclusive with `view_id` and `create_database`. |
| `view_id` | The ID of a dashboard view to add this view to as a widget. Mutually exclusive with `database_id` and `create_database`. |
| `create_database` | Creates a linked database view on a page referencing an existing data source. See [Creating a linked database view](#creating-a-linked-database-view). Mutually exclusive with `database_id` and `view_id`. |
| `filter` | A [filter object](/reference/filter-data-source-entries) to apply. Uses the same shape as data source queries. |
| `sorts` | An array of [sort objects](/reference/sort-data-source-entries). Uses the same shape as data source queries. |
| `quick_filters` | A map of [quick filters](#quick-filters) for the view's filter bar. Keys are property names or IDs, values are filter conditions or an empty object for no criteria. |
| `configuration` | A [view configuration](#view-configuration) object. The `type` field inside must match the view `type`. |
| `position` | Where to place the new view in the database's view tab bar. Only applicable when `database_id` is provided. See [View positioning](#view-positioning). Defaults to appending at the end. |
| `placement` | Where to place the new widget in a dashboard layout. Only applicable when `view_id` is provided. See [Widget placement](#widget-placement). Defaults to creating a new row at the end. |

<Note>
  You must provide exactly one of `database_id`, `view_id`, or `create_database`. Use `database_id` to create a top-level view on a database. Use `view_id` to add a widget view to an existing dashboard — see [Dashboard views](#dashboard-views) for details. Use `create_database` to create a linked database view on a page — see [Creating a linked database view](#creating-a-linked-database-view).
</Note>

<Note>
  **Finding the data source ID**

  If you already have a database ID, call the [Retrieve a database](/reference/retrieve-database) endpoint. The response includes a `data_sources` array with each data source's `id` and `name`.
</Note>

### Creating different view types

Here's an example of creating a Board view with grouping, cover images, and property configuration:

<CodeGroup>
  ```bash cURL expandable theme={null}
  curl -X POST https://api.notion.com/v1/views \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "database_id": "DATABASE_ID",
      "data_source_id": "DATA_SOURCE_ID",
      "name": "Task board",
      "type": "board",
      "configuration": {
        "type": "board",
        "group_by": {
          "type": "status",
          "property_id": "STATUS_PROPERTY_ID",
          "group_by": "group",
          "sort": { "type": "manual" }
        },
        "cover": {
          "type": "page_cover"
        },
        "cover_size": "medium",
        "card_layout": "compact"
      }
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  const boardView = await notion.views.create({
    database_id: "DATABASE_ID",
    data_source_id: "DATA_SOURCE_ID",
    name: "Task board",
    type: "board",
    configuration: {
      type: "board",
      group_by: {
        type: "status",
        property_id: "STATUS_PROPERTY_ID",
        group_by: "group",
        sort: { type: "manual" },
      },
      cover: {
        type: "page_cover",
      },
      cover_size: "medium",
      card_layout: "compact",
    },
  });
  ```
</CodeGroup>

### View positioning

When creating a top-level database view (using `database_id`), you can control where it appears in the view tab bar with the `position` parameter. This is a discriminated union on the `type` field:

| Variant | Fields | Description |
| - | - | - |
| `start` | `type` | Places the new view as the first tab. |
| `end` | `type` | Places the new view as the last tab (default). |
| `after_view` | `type`, `view_id` | Places the new view immediately after the specified view. |

<CodeGroup>
  ```json Place at start theme={null}
  {
    "position": { "type": "start" }
  }
  ```

  ```json Place after a specific view theme={null}
  {
    "position": {
      "type": "after_view",
      "view_id": "EXISTING_VIEW_ID"
    }
  }
  ```
</CodeGroup>

<Note>
  The `position` parameter is only valid when `database_id` is provided. It cannot be used with `view_id` (dashboard widget creation).
</Note>

### Creating a linked database view

Use the `create_database` parameter to create a lightweight linked database view on a page that references an existing data source. This creates a new database container on the target page with a single view over the specified data source — similar to inserting a "linked view of database" in the Notion UI.

This differs from `POST /v1/databases`, which creates a full standalone database with its own schema, data source, and default view. With `create_database`, the view points to an existing data source owned by another database, so no new schema is created.

<CodeGroup>
  ```javascript JavaScript expandable theme={null}
  const view = await notion.views.create({
    create_database: {
      parent: {
        type: "page_id",
        page_id: "TARGET_PAGE_ID",
      },
    },
    data_source_id: "EXISTING_DATA_SOURCE_ID",
    name: "Tasks overview",
    type: "table",
  });
  ```

  ```bash cURL expandable theme={null}
  curl -X POST https://api.notion.com/v1/views \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "create_database": {
        "parent": {
          "type": "page_id",
          "page_id": "TARGET_PAGE_ID"
        }
      },
      "data_source_id": "EXISTING_DATA_SOURCE_ID",
      "name": "Tasks overview",
      "type": "table"
    }'
  ```
</CodeGroup>

The `create_database` object accepts the following fields:

| Field | Required | Description |
| - | - | - |
| `parent` | Yes | The parent page for the linked database. Must be `{ "type": "page_id", "page_id": "..." }`. |
| `position` | No | Controls where the new database block appears within the parent page. Use `{ "type": "after_block", "block_id": "..." }` to place it after a specific block. The referenced block must be a direct child of the parent page. Defaults to appending at the end. |

All view types are supported with `create_database`, including `form` views with full form configuration and `dashboard` views. Dashboard views are created with an empty layout — add widgets to them via separate `POST /v1/views` calls with `view_id`.

<Note>
  Your connection must have access to both the target page (where the new database container is created) and the database that owns the data source being referenced.
</Note>

## Updating a view

[Update a view](/reference/update-a-view) to change its name, filters, sorts, or configuration. All fields are optional — only include the fields you want to change.

<CodeGroup>
  ```bash cURL expandable theme={null}
  curl -X PATCH https://api.notion.com/v1/views/VIEW_ID \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "name": "Completed this month",
      "filter": {
        "and": [
          {
            "property": "Status",
            "status": { "equals": "Done" }
          },
          {
            "property": "Completed date",
            "date": { "this_month": {} }
          }
        ]
      },
      "sorts": [
        {
          "property": "Completed date",
          "direction": "descending"
        }
      ],
      "configuration": {
        "type": "table",
        "group_by": null,
        "properties": [
          { "property_id": "title", "visible": true, "width": 400 },
          { "property_id": "abc1", "visible": true },
          { "property_id": "def2", "visible": false }
        ]
      }
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  const updated = await notion.views.update({
    view_id: "VIEW_ID",
    name: "Completed this month",
    filter: {
      and: [
        {
          property: "Status",
          status: { equals: "Done" },
        },
        {
          property: "Completed date",
          date: { this_month: {} },
        },
      ],
    },
    sorts: [
      {
        property: "Completed date",
        direction: "descending",
      },
    ],
    configuration: {
      type: "table",
      group_by: null,
      properties: [
        { property_id: "title", visible: true, width: 400 },
        { property_id: "abc1", visible: true },
        { property_id: "def2", visible: false },
      ],
    },
  });
  ```
</CodeGroup>

To clear a view's filter, sorts, or specific configuration fields, set them to `null`. See [Clearing configuration with null](#clearing-configuration-with-null) for concrete examples.

## Deleting a view

[Delete a view](/reference/delete-view) by its ID. This permanently removes the view from the database's view list.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE https://api.notion.com/v1/views/VIEW_ID \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  const deleted = await notion.views.delete({
    view_id: "VIEW_ID",
  });

  // deleted.object === "view"
  // deleted.id === "VIEW_ID"
  ```
</CodeGroup>

The response is a partial view object containing only identity fields (`object`, `id`, `parent`, and `type`). Full view details like filters, sorts, and configuration are not included since the view has been deleted.

<Warning>
  Deleting a view cannot be undone through the API. The view will no longer appear in the database's view list.
</Warning>

<Note>
  A database must always have at least one view. Attempting to delete the last remaining view returns a `validation_error`. To remove the database entirely, set [`in_trash`](/reference/update-database#body-in-trash) to `true` via the update database endpoint instead.
</Note>

## View configuration

The `configuration` field on a view object controls type-specific presentation settings — things like column widths, grouping, cover images, subtasks, and more. It is a discriminated union keyed on the `type` field, which must match the view's top-level `type`.

You can pass `configuration` when [creating](#creating-a-view) or [updating](#updating-a-view) a view. Nullable fields accept `null` to clear the setting.

### Feature support by view type

| Feature | Table | Board | Calendar | Timeline | Gallery | List | Map | Form | Chart | Dashboard |
| - | - | - | - | - | - | - | - | - | - | - |
| `properties` | Yes | Yes | Yes | Yes | Yes | Yes | Optional | - | - | - |
| `group_by` | Optional | **Required** | - | - | - | - | - | - | - | - |
| `sub_group_by` | - | Optional | - | - | - | - | - | - | - | - |
| `subtasks` | Optional | - | - | - | - | - | - | - | - | - |
| `cover` | - | Optional | - | - | Optional | - | - | - | - | - |
| `cover_size` / `cover_aspect` | - | Optional | - | - | Optional | - | - | - | - | - |
| `card_layout` | - | Optional | - | - | Optional | - | - | - | - | - |
| `date_property_id` | - | - | **Required** | **Required** | - | - | - | - | - | - |
| `end_date_property_id` | - | - | - | Optional | - | - | - | - | - | - |
| `view_range` / `show_weekends` | - | - | Optional | - | - | - | - | - | - | - |
| `preference` / `arrows_by` | - | - | - | Optional | - | - | - | - | - | - |
| `show_table` / `table_properties` | - | - | - | Optional | - | - | - | - | - | - |
| `wrap_cells` / `frozen_column_index` | Optional | - | - | - | - | - | - | - | - | - |
| `show_vertical_lines` | Optional | - | - | - | - | - | - | - | - | - |
| `height` | - | - | - | - | - | - | Optional | - | Optional | - |
| `map_by` | - | - | - | - | - | - | Optional | - | - | - |
| `is_form_closed` | - | - | - | - | - | - | - | Optional | - | - |
| `anonymous_submissions` | - | - | - | - | - | - | - | Optional | - | - |
| `submission_permissions` | - | - | - | - | - | - | - | Optional | - | - |
| `chart_type` | - | - | - | - | - | - | - | - | **Required** | - |
| `x_axis` / `y_axis` | - | - | - | - | - | - | - | - | Optional | - |
| `value` | - | - | - | - | - | - | - | - | Optional | - |
| `rows` | - | - | - | - | - | - | - | - | - | Yes (read-only) |

### Table configuration

```json theme={null}
{
  "type": "table",
  "properties": [...],
  "group_by": { ... } | null,
  "subtasks": { ... } | null,
  "wrap_cells": true,
  "frozen_column_index": 1,
  "show_vertical_lines": true
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"table"` | **Required.** Must be `"table"`. |
| `properties` | array \| null | Property visibility and display settings. See [Property configuration](#property-configuration). |
| `group_by` | object \| null | Group rows by a property. See [Group-by configuration](#group-by-configuration). Pass `null` to remove. |
| `subtasks` | object \| null | Sub-item display settings. See [Subtask configuration](#subtask-configuration). Pass `null` to reset to defaults. Use `{ "display_mode": "disabled" }` to explicitly disable. |
| `wrap_cells` | boolean | Whether to wrap cell content. |
| `frozen_column_index` | integer (>= 0) | Number of columns frozen from the left. |
| `show_vertical_lines` | boolean | Whether to show vertical grid lines between columns. |

### Board configuration

```json theme={null}
{
  "type": "board",
  "group_by": { ... },
  "sub_group_by": { ... } | null,
  "properties": [...],
  "cover": { "type": "page_cover" },
  "cover_size": "medium",
  "cover_aspect": "cover",
  "card_layout": "compact"
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"board"` | **Required.** Must be `"board"`. |
| `group_by` | object | **Required.** Group-by configuration for board columns. See [Group-by configuration](#group-by-configuration). |
| `sub_group_by` | object \| null | Secondary group-by for sub-grouping within columns. Pass `null` to remove. |
| `properties` | array \| null | Property visibility on cards. See [Property configuration](#property-configuration). |
| `cover` | object \| null | Cover image source. See [Cover configuration](#cover-configuration). |
| `cover_size` | `"small"` \| `"medium"` \| `"large"` \| null | Size of the cover image on cards. |
| `cover_aspect` | `"contain"` \| `"cover"` \| null | `"contain"` fits the image; `"cover"` fills the area. |
| `card_layout` | `"list"` \| `"compact"` \| null | `"list"` shows full cards; `"compact"` shows condensed cards. |

### Calendar configuration

```json theme={null}
{
  "type": "calendar",
  "date_property_id": "DATE_PROPERTY_ID",
  "properties": [...],
  "view_range": "month",
  "show_weekends": true
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"calendar"` | **Required.** Must be `"calendar"`. |
| `date_property_id` | string | **Required.** Property ID of the date property used to position items on the calendar. |
| `properties` | array \| null | Property visibility on calendar cards. See [Property configuration](#property-configuration). |
| `view_range` | `"week"` \| `"month"` \| null | Default calendar range. |
| `show_weekends` | boolean \| null | Whether to show weekend days. |

### Timeline configuration

```json theme={null}
{
  "type": "timeline",
  "date_property_id": "START_DATE_PROPERTY_ID",
  "end_date_property_id": "END_DATE_PROPERTY_ID",
  "properties": [...],
  "show_table": true,
  "table_properties": [...],
  "preference": {
    "zoom_level": "month",
    "center_timestamp": 1706745600000
  },
  "arrows_by": {
    "property_id": "RELATION_PROPERTY_ID"
  },
  "color_by": true
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"timeline"` | **Required.** Must be `"timeline"`. |
| `date_property_id` | string | **Required.** Property ID for the start date of timeline items. |
| `end_date_property_id` | string \| null | Property ID for the end date. Pass `null` to clear. |
| `properties` | array \| null | Property visibility on timeline items. See [Property configuration](#property-configuration). |
| `show_table` | boolean \| null | Whether to show the table panel alongside the timeline. |
| `table_properties` | array \| null | Property configuration for the table panel (when `show_table` is true). |
| `preference` | object \| null | Timeline display preferences. See below. |
| `arrows_by` | object \| null | Dependency arrow configuration. See below. |
| `color_by` | boolean \| null | Whether to color timeline items by a property. |

**Timeline preference object:**

| Field | Type | Description |
| - | - | - |
| `zoom_level` | enum | **Required.** One of: `"hours"`, `"day"`, `"week"`, `"bi_week"`, `"month"`, `"quarter"`, `"year"`, `"5_years"`. |
| `center_timestamp` | integer | Timestamp in milliseconds to center the timeline on. |

**Timeline arrows\_by object:**

| Field | Type | Description |
| - | - | - |
| `property_id` | string \| null | Relation property ID for dependency arrows, or `null` to disable arrows. |

### Gallery configuration

```json theme={null}
{
  "type": "gallery",
  "properties": [...],
  "cover": { "type": "page_content" },
  "cover_size": "large",
  "cover_aspect": "cover",
  "card_layout": "list"
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"gallery"` | **Required.** Must be `"gallery"`. |
| `properties` | array \| null | Property visibility on gallery cards. See [Property configuration](#property-configuration). |
| `cover` | object \| null | Cover image source. See [Cover configuration](#cover-configuration). |
| `cover_size` | `"small"` \| `"medium"` \| `"large"` \| null | Size of the cover image on cards. |
| `cover_aspect` | `"contain"` \| `"cover"` \| null | `"contain"` fits the image; `"cover"` fills the area. |
| `card_layout` | `"list"` \| `"compact"` \| null | `"list"` shows full cards; `"compact"` shows condensed cards. |

### List configuration

```json theme={null}
{
  "type": "list",
  "properties": [...]
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"list"` | **Required.** Must be `"list"`. |
| `properties` | array \| null | Property visibility and display settings. See [Property configuration](#property-configuration). |

### Map configuration

```json theme={null}
{
  "type": "map",
  "height": "medium",
  "map_by": "LOCATION_PROPERTY_ID",
  "properties": [...]
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"map"` | **Required.** Must be `"map"`. |
| `height` | `"small"` \| `"medium"` \| `"large"` \| `"extra_large"` \| null | Map display height. Pass `null` to clear. |
| `map_by` | string \| null | Property ID of the location property used to position items on the map. Pass `null` to clear. |
| `properties` | array \| null | Property visibility on map pin cards. See [Property configuration](#property-configuration). |

In responses, an additional read-only field `map_by_property_name` may be present, containing the display name of the `map_by` property.

### Form configuration

```json theme={null}
{
  "type": "form",
  "is_form_closed": false,
  "anonymous_submissions": true,
  "submission_permissions": "comment_only"
}
```

| Field | Type | Description |
| - | - | - |
| `type` | `"form"` | **Required.** Must be `"form"`. |
| `is_form_closed` | boolean \| null | Whether the form is closed for submissions. Pass `null` to clear. |
| `anonymous_submissions` | boolean \| null | Whether anonymous (non-logged-in) submissions are allowed. Pass `null` to clear. |
| `submission_permissions` | `"none"` \| `"comment_only"` \| `"reader"` \| `"read_and_write"` \| `"editor"` \| null | Permission level granted to the submitter on the created page after form submission. Pass `null` to clear. |

### Chart configuration

Chart views display database data as visual charts. The configuration uses a flat object with `chart_type` as a required discriminator. Available fields vary by chart type.

```json theme={null}
{
  "type": "chart",
  "chart_type": "column",
  "x_axis": {
    "type": "select",
    "property_id": "CATEGORY_PROP_ID",
    "sort": { "type": "manual" }
  },
  "y_axis": {
    "aggregator": "sum",
    "property_id": "AMOUNT_PROP_ID"
  },
  "color_theme": "blue",
  "color_by_value": true,
  "show_data_labels": true,
  "height": "medium"
}
```

When `color_by_value` is enabled on a bar or column chart, each bar is shaded along a gradient based on its numeric value — higher values appear in a darker shade and lower values in a lighter shade. This is useful for quickly spotting relative magnitude across categories. Combine with `color_theme` to control the gradient's base color.

**Required fields:**

| Field | Type | Description |
| - | - | - |
| `type` | `"chart"` | **Required.** Must be `"chart"`. |
| `chart_type` | `"column"` \| `"bar"` \| `"line"` \| `"donut"` \| `"number"` | **Required.** The chart type: `"column"` (vertical bars), `"bar"` (horizontal bars), `"line"`, `"donut"`, or `"number"` (single value display). |

**Data configuration fields:**

Charts support two data modes: **grouped data** (aggregate values by grouping on a property) and **results** (use raw property values directly).

| Field | Type | Description |
| - | - | - |
| `x_axis` | object \| null | X-axis grouping configuration for column/bar/line/donut charts using grouped data. Uses the same [group-by configuration](#group-by-configuration) shape. Null when using results mode. Pass `null` to clear. |
| `y_axis` | object \| null | Y-axis [aggregation](#chart-aggregation) for column/bar/line/donut charts using grouped data. Null when using results mode. Pass `null` to clear. |
| `x_axis_property_id` | string \# Authentication
Source: https://developers.notion.com/cli/get-started/authentication

Log in to your Notion workspace and manage CLI credentials.

## Log in

Authenticate with your Notion workspace:

```bash theme={null}
ntn login
```

This opens your browser to an authorization page. Confirm that the code in the browser matches the code printed in your terminal before approving. This prevents another page from completing the login in your name.

Your workspace-scoped token will be stored securely in your system's keychain.

If you've already logged in to one or more workspaces, you can pick existing workspace to switch the default, or pick **Authenticate with new workspace** to start a fresh browser flow and add another workspace.

<Note>
  `ntn login` requires full workspace membership. [Guests](https://www.notion.com/help/whos-who-in-a-workspace) and [restricted members](https://www.notion.com/help/whos-who-in-a-workspace) cannot log in with the Notion CLI. If you need CLI access, ask a workspace admin to upgrade your role. See [Personal access tokens](/guides/get-started/personal-access-tokens) for more on who can create tokens.
</Note>

## Log in without a browser

On a remote machine, container, or CI runner that can't open a browser, use `--no-browser` to get a two-step login flow:

1. Run `ntn login --no-browser`. It prints a URL, a verification code, and a `ntn login poll` command.
2. Open the URL in any browser, sign in, and confirm the verification code.
3. Run `ntn login poll` on the original machine to redeem the token.

`ntn login` also falls back to this flow automatically when it detects there is no terminal (e.g. piped input).

Login sessions expire after a short window. If polling fails because the session expired, run `ntn login` again to start over.

For unattended use (CI, scripts, bots), prefer a [personal access token](#use-a-personal-access-token) instead.

## Target a specific workspace

To run a single command against a non-default workspace without switching defaults, set `NOTION_WORKSPACE_ID`:

```bash theme={null}
NOTION_WORKSPACE_ID=<workspace-id> ntn api v1/users/me
```

Workspace IDs are listed in the output of `ntn debug`.

## Use a personal access token

For unattended use, authenticate with a [personal access token](/guides/get-started/personal-access-tokens) (PAT) by exporting it as `NOTION_API_TOKEN`:

```bash theme={null}
export NOTION_API_TOKEN=ntn_xxx...
ntn api v1/users/me
```

`NOTION_API_TOKEN` takes precedence over anything stored in the keychain, so the same shell can mix `ntn login`-based commands and PAT-based commands depending on what's exported.

## Inspect your session

```bash theme={null}
ntn doctor
```

## Log out

```bash theme={null}
ntn logout
```

This forgets every cached workspace, deletes each one's token from the keychain, and clears the default workspace. The `config.json` and `workspaces.json` files themselves stay in place — run `ntn login` to repopulate them.

## Where credentials are stored

Tokens live in your OS credential store (Keychain on macOS, Secret Service on Linux) under the service name `notion-cli`, with the workspace ID as the account.

Two files sit alongside them in the CLI config directory:

* `config.json` — CLI version, default workspace per, and the optional `keyring` toggle.
* `workspaces.json` — cached workspace IDs and names for the interactive picker.

The config directory is `NOTION_HOME` if set, otherwise `$XDG_CONFIG_HOME/notion`, `$HOME/.config/notion`, or `$HOME/.notion` as fallbacks.

### Opt out of the OS keychain

On systems without a usable keychain, `ntn login` fails with a keychain error. Common examples include Docker containers, CI runners, SSH sessions to a Linux server, etc.

Set `NOTION_KEYRING=0` to store tokens in plain JSON at `auth.json` in the config directory instead. Treat that file like any other secret.

```bash theme={null}
NOTION_KEYRING=0 ntn login
```

To make it permanent, set `"keyring": false` in `config.json`. The env var always wins.

## Environment variables

| Variable | Purpose |
| :- | :- |
| `NOTION_API_TOKEN` | When this is set, it'll take precedence over `ntn login`'s keychain entry. Handy for scripts and CI. |
| `NOTION_WORKSPACE_ID` | Override the default workspace for a single command. |
| `NOTION_KEYRING` | Set to `0` to use file-based storage instead of the OS keychain. |
| `NOTION_HOME` | Override the config directory. |
| `NOTION_ENV` | Same as `--env`. Rarely needed. |

Run `ntn login --help` for the full list.

## Next steps

<CardGroup>
  <Card title="Workers quickstart" icon="rocket" href="/workers/get-started/quickstart">
    Create and deploy your first Notion Worker.
  </Card>

  <Card title="API requests" icon="terminal" href="/cli/guides/api-requests">
    Make Notion API requests from the terminal.
  </Card>

  <Card title="Command reference" icon="book-open" href="/cli/reference/commands">
    Full reference for every ntn command.
  </Card>

  <Card title="Personal access tokens" icon="key" href="/guides/get-started/personal-access-tokens">
    Create tokens for scripts and CI.
  </Card>
</CardGroup>
