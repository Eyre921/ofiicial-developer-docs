---
title: "Update a data source"
source: https://developers.notion.com/reference/update-a-data-source
path: reference/update-a-data-source
---

patch /v1/data_sources/{data_source_id}

Updates a [data source](/reference/data-source)’s name, icon, schema, parent, or trash status. Returns the updated data source object.

Use `properties` to change the schema. See [Update data source properties](/reference/update-data-source-properties) for request bodies and [Property schemas](/reference/property-object) for each type’s settings.

## Parent changes

Set `parent.database_id` to move the data source to another database. Existing views in the original database become linked views. Notion creates a table view in the destination database. See [Views](/reference/view) for the view API.

### How data sources property type changes work

Changing a property’s type changes how Notion reads its existing values. Some values cannot be read in the new type. Test the conversion before applying it to data you need.

The Name property (`title`) cannot be removed or converted. Other properties cannot become `title`. You can add or rename a Place property, but you cannot convert a property to or from `place`. Synced data sources have additional restrictions.

### Interacting with data source rows

This endpoint changes the schema for all pages in the data source. To change one page’s values, use [Update page](/reference/patch-page). To add a page, use [Create page](/reference/post-page).

### Recommended data source schema size limit

Keep the schema within 50 KB. Schema updates that are too large return `validation_error`. The error identifies the largest property by name, ID, and byte size so you can reduce it.

Large option lists and long property descriptions contribute to schema size. Remove unused settings or shorten descriptions before retrying.

<span />

### Access and errors

The connection needs [update content capabilities](/reference/capabilities) and access to the data source. Relations and rollups also need access to the related database.

A missing data source or missing access returns `404`. See [Status codes](/reference/status-codes#error-codes) for other errors.
