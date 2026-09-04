---
title: "Query meeting notes"
source: https://developers.notion.com/reference/query-meeting-notes
path: reference/query-meeting-notes
---

post /v1/blocks/meeting_notes/query
Query meeting notes for the workspace with optional filters, sorts, and a result limit.

### Overview

Returns a list of **meeting notes** as [block objects](/reference/block) (`object` is `block`, `type` is `meeting_notes`) where the **user tied to the integration** (in the workspace) is listed as a attendee on the block.

The response contains:

* `results`: meeting note blocks (including `meeting_notes` payload with title, status, children tab IDs (e.g. summary, notes, transcription), and calendar and recording metadata when present).
* `has_more`: whether additional rows exist beyond this response for the current filter, sort, and `limit`.

**Field selection:** There is no field subset parameter—each `results[]` item is a full [block object](/reference/block). Read the fields you need (for example `meeting_notes`, timestamps, and people) from the response. Use `filter` to control **which** meeting notes are returned; allowed property names and operators are defined on this endpoint’s [request body schema](/reference/query-meeting-notes).

This endpoint does **not** use cursor-based pagination. There is no `start_cursor` or `next_cursor`—tune `filter`, `sort`, and `limit` (up to the maximum below) to refine the result set.

### Request body

The body is a JSON object; every field is optional.

| Field    | Description                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `filter` | A single **property** filter, or a **combinator** (`"and"` / `"or"`) with a `filters` array. See **Filtering**.                  |
| `sort`   | Ordered list of sorts. Each entry has `property` and `direction` (`ascending` or `descending`). Earlier entries take precedence. |
| `limit`  | Maximum number of meeting notes to return. **Integer** from **1** to **50**. If omitted, the server uses **50**.                 |

<CodeGroup>
  ```json Default (implicit limit 50) theme={null}
  {}
  ```

  ```json Sort and cap results theme={null}
  {
    "sort": [
      { "property": "last_edited_time", "direction": "descending" }
    ],
    "limit": 10
  }
  ```
</CodeGroup>

### Filtering

A **filter** is either:

1. **Property filter (single condition)** — an object with `property` and `filter` (operator and optional `value`) at the **root** of the `filter` field.
2. **Combinator** — an object with `operator` (`"and"` or `"or"`) and a `filters` array. Each array element is another property filter or, for one level of nesting, a combinator whose inner `filters` are **property** filters only (see the [request schema](/reference/query-meeting-notes) in the API reference for the exact shape).

Property names, operators, and `value` shapes for text, date, and person filters are fully specified in the [request body schema](/reference/query-meeting-notes). Invalid properties or malformed filters return a **400** validation error.

### Filter examples

Three patterns below cover a **single** property filter, an **`and`** combinator, and an **`or`** combinator. For more properties and operators, use the schema link above. Replace sample strings and UUIDs with your own.

<CodeGroup>
  ```json Single property (title) theme={null}
  {
    "filter": {
      "property": "title",
      "filter": {
        "operator": "string_contains",
        "value": { "type": "exact", "value": "standup" }
      }
    }
  }
  ```

  ```json Combinator: and theme={null}
  {
    "filter": {
      "operator": "and",
      "filters": [
        {
          "property": "title",
          "filter": {
            "operator": "string_contains",
            "value": { "type": "exact", "value": "planning" }
          }
        },
        {
          "property": "attendees",
          "filter": { "operator": "is_not_empty" }
        }
      ]
    }
  }
  ```

  ```json Combinator: or, with sort and limit theme={null}
  {
    "filter": {
      "operator": "or",
      "filters": [
        {
          "property": "title",
          "filter": {
            "operator": "string_contains",
            "value": { "type": "exact", "value": "standup" }
          }
        },
        {
          "property": "title",
          "filter": {
            "operator": "string_contains",
            "value": { "type": "exact", "value": "sprint" }
          }
        }
      ]
    },
    "sort": [
      { "property": "last_edited_time", "direction": "descending" }
    ],
    "limit": 20
  }
  ```
</CodeGroup>

### Sorting

Each sort item has `property` and `direction` (`ascending` or `descending`). Property names are the same set as in the request body schema. **Earlier entries take precedence** when multiple sorts are present.

```json theme={null}
{
  "sort": [
    { "property": "last_edited_time", "direction": "descending" },
    { "property": "title", "direction": "ascending" }
  ]
}
```

### Response shape

Each item in `results` is a meeting note block with a `meeting_notes` object plus the usual block metadata (see the response schema for this endpoint).

<Info>
  **Integration capabilities**

  This endpoint requires an integration with **Read content**. The workspace must include **AI meeting notes** for the integration’s user; otherwise the call returns a validation error. See the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 400 HTTP response if AI meeting notes aren't available for the integration's user, or if the filter or sort is invalid.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

<Danger>
  **Note**: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
</Danger>
