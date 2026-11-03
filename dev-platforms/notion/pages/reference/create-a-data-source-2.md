---
title: "Create a data source"
source: https://developers.notion.com/reference/create-a-data-source
path: reference/create-a-data-source
---

post /v1/data_sources

Use this API to add an additional [data source](/reference/data-source) to an existing [database](/reference/database). The `properties` follow the [same structure](/reference/property-object) as the initial schema passed to `initial_data_source[properties]` in the [Create a database](/reference/create-database) API, but can be managed independently of the `properties` of any sibling data sources.

A standard "table" view is created alongside the new data source. To customize database views, use the Notion app. Managing views is not currently supported in the API.
