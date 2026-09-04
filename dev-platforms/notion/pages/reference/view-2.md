---
title: "View"
source: https://developers.notion.com/reference/view
path: reference/view
---

Learn about the Notion view object and its properties.

<Note>
  **Getting started**

  View [Working with views](/guides/data-apis/working-with-views) for a comprehensive guide to creating and managing views.
</Note>

**Views** define how pages in a [data source](/reference/data-source) are filtered, sorted, and displayed within a [database](/reference/database). Each view has its own type (table, board, calendar, etc.), filter, sort order, and layout configuration.

## Supported view types

| Type        | Description                                    |
| :---------- | :--------------------------------------------- |
| `table`     | Rows-and-columns spreadsheet layout.           |
| `board`     | Kanban board grouped by a property.            |
| `calendar`  | Calendar layout grouped by a date property.    |
| `timeline`  | Gantt-style timeline layout.                   |
| `gallery`   | Card grid with cover images.                   |
| `list`      | Simple list layout.                            |
| `form`      | Form view for data entry.                      |
| `chart`     | Chart visualization.                           |
| `map`       | Map view with location pins.                   |
| `dashboard` | Multi-widget dashboard containing other views. |

<Info>
  View-specific `configuration` is available for all view types except `dashboard`. Dashboard views use `rows` to define their layout instead. See [Working with views](/guides/data-apis/working-with-views#view-configuration) for configuration details per view type.
</Info>

## Object fields

The response of View APIs like [Retrieve a view](/reference/retrieve-a-view) contains view objects with the following fields:

| Field               | Type           | Description                                                                                                                                                 |
| :------------------ | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `object`            | `"view"`       | Always `"view"`.                                                                                                                                            |
| `id`                | UUID           | The ID of the view.                                                                                                                                         |
| `parent`            | Object         | The parent database. Contains `type: "database_id"` and `database_id`.                                                                                      |
| `data_source_id`    | String \| null | The ID of the data source this view is scoped to, or `null` for dashboard views.                                                                            |
| `name`              | String         | The display name of the view.                                                                                                                               |
| `type`              | String         | One of the [supported view types](#supported-view-types).                                                                                                   |
| `filter`            | Object \| null | The [filter](/reference/filter-data-source-entries) applied to this view, or `null` if no filter is set.                                                    |
| `sorts`             | Array \| null  | The [sorts](/reference/sort-data-source-entries) applied to this view, or `null` if no sorts are set.                                                       |
| `configuration`     | Object \| null | View-specific layout configuration, discriminated by `type`. See [Working with views](/guides/data-apis/working-with-views#view-configuration) for details. |
| `created_time`      | String         | ISO 8601 timestamp when the view was created.                                                                                                               |
| `created_by`        | Object \| null | Partial [user](/reference/user) who created the view.                                                                                                       |
| `last_edited_time`  | String         | ISO 8601 timestamp when the view was last edited.                                                                                                           |
| `last_edited_by`    | Object \| null | Partial [user](/reference/user) who last edited the view.                                                                                                   |
| `url`               | String         | Deep link to the view in Notion.                                                                                                                            |
| `dashboard_view_id` | String         | Only present for widget views inside a dashboard. The ID of the parent dashboard view.                                                                      |
