---
title: "Data source"
source: https://developers.notion.com/reference/data-source
path: reference/data-source
---

Learn more about Notion's data source object.

**Data sources** are the individual tables of data that live under a Notion database. [Pages](/reference/page) are the items (or children) in a data source. [Page property values](/reference/page-property-values) must conform to the [property objects](/reference/property-object) laid out in the parent data source object.

![](https://mintcdn.com/notion-demo/Muj7K3D7I6gj-QAA/images/reference/6dc5c7eccb432e908290e2642c84579936d55ee79c6cd60a5b0807e70cdeb55a-image.png?fit=max\&auto=format\&n=Muj7K3D7I6gj-QAA\&q=85\&s=732ada865d8d25def0ba61090c6e9f2e)

Diagram of the new Notion API data model. A database is a parent of one or more data sources, each of which parents zero or more pages. Previously, databases could only have one data source, so the concepts were combined in the API until 2025.

As of API version `2025-09-03`, there's a suite of APIs for managing data sources:

* [Create a data source](/reference/create-a-data-source): add an additional data source for an existing [Database](/reference/database)
* [Update a data source](/reference/update-a-data-source): update attributes, such as the `properties`, of a data source
* [Retrieve a data source](/reference/retrieve-a-data-source)
* [Query a data source](/reference/query-a-data-source)

## Object fields

> [!NOTE]
>
> Properties marked with an asterisk (\*) are available to connections with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. For more information on connection capabilities, see the [capabilities guide](/reference/capabilities).

| Field | Type | Description | Example value |
| :- | :- | :- | :- |
| `object`\* | `string` | Always `"data_source"`. | `"data_source"` |
| `id`\* | `string` (UUID) | Unique identifier for the data source. | `"2f26ee68-df30-4251-aad4-8ddc420cba3d"` |
| `properties`\* | `object` | Schema of properties for the data source as they appear in Notion.  `key` string The name of the property as it appears in Notion.  `value` object A [Property object](/reference/property-object). | |
| `parent` | `object` | Information about the data source's immediate parent. Most data sources are parented by a database (`type: "database_id"`). Some externally synced data sources can be parented by another data source (`type: "data_source_id"`) and include the containing `database_id`. See [Parent object](/reference/parent-object). | `{"type": "database_id", "database_id": "842a0286-cef0-46a8-abba-eac4c8ca644e"}` |
| `database_parent` | `object` | Information about the containing database's parent. See [Parent object](/reference/parent-object). | `{ "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }` |
| `database_type` | `string` or `null` | The type of typed database this data source belongs to. `null` for a regular data source. | `"skills"` |
| `created_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this data source was created. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2020-03-17T19:10:04.968Z"` |
| `created_by` | [Partial User](/reference/user) | User who created the data source. | `{"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}` |
| `last_edited_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this data source was updated. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2020-03-17T21:49:37.913Z"` |
| `last_edited_by` | [Partial User](/reference/user) | User who last edited the data source. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}` |
| `title` | array of [rich text objects](/reference/rich-text) | Name of the data source as it appears in Notion. See [rich text object](/reference/rich-text)) for a breakdown of the properties. | `[ { "type": "text", "text": { "content": "Can I create a URL property", "link": null }, "annotations": { "bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default" }, "plain_text": "Can I create a URL property", "href": null } ]` |
| `description` | array of [rich text objects](/reference/rich-text) | Description of the data source as it appears in Notion. See [rich text object](/reference/rich-text)) for a breakdown of the properties. | |
| `icon` | [Emoji](/reference/emoji-and-icon#emoji), [Icon](/reference/emoji-and-icon#icon), [Custom emoji](/reference/emoji-and-icon#custom-emoji), or [File](/reference/file-object) | Data source icon. See [Icon](/reference/emoji-and-icon) for all supported types. | |
| `archived` | `boolean` | **Deprecated.** Use `in_trash` instead. This is an alias for `in_trash` and always returns the same value. | `false` |
| `in_trash` | `boolean` | Whether the data source has been trashed. | `false` |
| `sync_metadata` | `object` | Optional, read-only stored sync information included when listing or retrieving a data source. See [Sync metadata](#sync-metadata). | `{"sync_id": "2f26ee68-df30-4251-aad4-8ddc420cba3d"}` |

## Sync metadata

The optional, read-only `sync_metadata` field describes stored sync information. It is returned when retrieving or listing a readable synced data source. [Retrieve a database](/reference/retrieve-database) also includes it on each readable entry in `data_sources`. Search, create, and update responses do not include it.

The field requires read access to the data source and a read capability on the connection. It is omitted from partial responses and when stored metadata is unavailable or invalid. Its absence does not prove that the data source is not synced. These reads do not refresh the sync or query its provider, so the metadata is not a live health check.

The object has one of these stored representations:

| Field | Type | Meaning |
| - | - | - |
| `external_database_sync` | object | An external database sync's identity: `sync_id` is a UUID and `provider` is one of `github` (GitHub), `jira` (Jira), or `salesforce` (Salesforce). |
| `external_collection_type` | string enum | A legacy synced data source's provider: `Jira` or `Salesforce`. These values are case-sensitive. An optional `sync_state` may accompany this field. |
| `sync_id` | string (UUID) | A stored sync ID when provider details are unavailable, including older synced data sources. |
| `synced_collection_key` | string | An opaque, developer-defined collection key for a worker sync, such as `issues`. It is not a fixed enum or a globally unique identifier. Worker status is not included. |

Sync IDs and collection keys are identifiers, not credentials, and do not grant access to manage a sync. This field does not include credentials, errors from the provider, or sync configuration.

For example, an external database sync returns:

```json theme={null}
{
  "sync_metadata": {
    "external_database_sync": {
      "sync_id": "2f26ee68-df30-4251-aad4-8ddc420cba3d",
      "provider": "github"
    }
  }
}
```

### Legacy sync state

`sync_state` is optional and applies only to legacy synced data sources. When present, it contains a required `syncing` field and may contain the timestamps below.

All timestamps are UTC ISO 8601 strings. Missing timestamps and timestamps that cannot be represented are omitted rather than returned as `null`.

| Field | Type | Meaning |
| - | - | - |
| `syncing` | boolean or string enum | `true` means syncing, `false` means not syncing, and `"row_limit_exceeded"` means the row limit stopped syncing. `false` does not guarantee that the last sync succeeded. |
| `last_synced_at` | string (date-time) | The stored legacy sync update time. It does not guarantee that all source changes have been imported. |
| `last_sync_checkpoint_at` | string (date-time) | The stored checkpoint used by the legacy sync to track progress. |
| `last_sync_heartbeat_at` | string (date-time) | The last stored heartbeat from the legacy sync. |

```json theme={null}
{
  "sync_metadata": {
    "external_collection_type": "Jira",
    "sync_state": {
      "syncing": false,
      "last_synced_at": "2026-10-29T12:34:56.789Z",
      "last_sync_checkpoint_at": "2026-10-29T12:30:00.000Z",
      "last_sync_heartbeat_at": "2026-10-29T12:34:50.000Z"
    }
  }
}
```

> [!WARNING]
>
> **Schema limitations**
>
> Notion recommends a max property count of **500** or a max schema size of **50KB**. Updates to database schemas that are too large will be blocked to help maintain database performance.
