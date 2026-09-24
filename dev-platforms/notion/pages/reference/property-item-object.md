---
title: "Page property items"
source: https://developers.notion.com/reference/property-item-object
path: reference/property-item-object
---

Reference for single property items, paginated values, and rollup results.

## Overview

[Retrieve a page property item](/reference/retrieve-a-page-property) reads one property on one page. It returns either a `property_item` object or a `list` of property items. The type determines the response shape.

The [page property values reference](/reference/page-property-values) defines each value type. Its examples include a Property item tab. This page defines the response wrapper and pagination rules.

## Common fields

| Field               | Type   | Meaning                                                                            |
| :------------------ | :----- | :--------------------------------------------------------------------------------- |
| `object`            | String | Always `property_item` for an individual item.                                     |
| `id`                | String | The property ID, shared by all items in that property. It is not a unique item ID. |
| `type`              | String | The property type.                                                                 |
| Key matching `type` | Varies | A single value of that type.                                                       |

A property’s `id` stays the same when its name changes. IDs can be short strings or UUIDs. The Name property always has the ID `title`.

Responses use URL-encoded property IDs, such as `f%5C%5C%3Ap`. Pass the returned ID as-is to the SDK or in an API path. Don’t encode it a second time. You can also use a property ID as a key in a request’s `properties` object.

## Response shape by type

Single-item responses use the same value shape as page responses. Follow a type link for its fields, write rules, and JSON examples.

| Type                                                                           | Response                                                   |
| :----------------------------------------------------------------------------- | :--------------------------------------------------------- |
| <span />[`button`](/reference/page-property-values#button)                     | One property item.                                         |
| <span />[`checkbox`](/reference/page-property-values#checkbox)                 | One property item.                                         |
| <span />[`created_by`](/reference/page-property-values#created-by)             | One property item.                                         |
| <span />[`created_time`](/reference/page-property-values#created-time)         | One property item.                                         |
| <span />[`date`](/reference/page-property-values#date)                         | One property item.                                         |
| <span />[`email`](/reference/page-property-values#email)                       | One property item.                                         |
| <span />[`files`](/reference/page-property-values#files)                       | One property item.                                         |
| [`formula`](/reference/page-property-values#formula)                           | One property item.                                         |
| <span />[`last_edited_by`](/reference/page-property-values#last-edited-by)     | One property item.                                         |
| <span />[`last_edited_time`](/reference/page-property-values#last-edited-time) | One property item.                                         |
| <span />[`multi_select`](/reference/page-property-values#multi-select)         | One property item.                                         |
| <span />[`number`](/reference/page-property-values#number)                     | One property item.                                         |
| <span />[`people`](/reference/page-property-values#people)                     | A paginated list; each item contains one user object.      |
| <span />[`phone_number`](/reference/page-property-values#phone-number)         | One property item.                                         |
| <span />[`place`](/reference/page-property-values#place)                       | One property item.                                         |
| <span />[`relation`](/reference/page-property-values#relation)                 | A paginated list; each item contains one page reference.   |
| <span />[`rich_text`](/reference/page-property-values#rich-text)               | A paginated list; each item contains one rich text object. |
| [`rollup`](/reference/page-property-values#rollup)                             | A paginated list with metadata in `property_item.rollup`.  |
| <span />[`select`](/reference/page-property-values#select)                     | One property item.                                         |
| [`status`](/reference/page-property-values#status)                             | One property item.                                         |
| <span />[`title`](/reference/page-property-values#title)                       | A paginated list; each item contains one rich text object. |
| <span />[`unique_id`](/reference/page-property-values#unique-id)               | One property item.                                         |
| <span />[`url`](/reference/page-property-values#url)                           | One property item.                                         |
| <span />[`verification`](/reference/page-property-values#verification)         | One property item.                                         |

## Status

Status is a single property item. The response is not wrapped in a property name or a `properties` object.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Status": {
        "id": "stat",
        "name": "Status",
        "description": null,
        "type": "status",
        "status": {
          "options": [
            {
              "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
              "name": "In progress",
              "color": "blue",
              "description": null
            }
          ],
          "groups": [
            {
              "id": "b9d42483-e576-4858-a26f-ed940a5f678f",
              "name": "To-do",
              "color": "gray",
              "option_ids": []
            },
            {
              "id": "cf4952eb-1265-46ec-86ab-4bded4fa2e3b",
              "name": "In progress",
              "color": "blue",
              "option_ids": [
                "330aeafb-598c-4e1c-bc13-1148aa5963d3"
              ]
            },
            {
              "id": "4fa7348e-ae74-46d9-9585-e773caca6f40",
              "name": "Complete",
              "color": "green",
              "option_ids": []
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Status": {
        "id": "stat",
        "type": "status",
        "status": {
          "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
          "name": "In progress",
          "color": "blue"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Status": {
          "status": {
            "name": "In progress"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "stat",
      "type": "status",
      "status": {
        "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
        "name": "In progress",
        "color": "blue"
      }
    }
    ```
  </Tab>
</Tabs>

## Paginated values

`title`, `rich_text`, `people`, and `relation` always return a list, even if there is only one item. Empty values return `results: []`. Multi-select and files return a single property item whose value is an array.

| Field                    | Type             | Meaning                                                                             |
| :----------------------- | :--------------- | :---------------------------------------------------------------------------------- |
| `object`                 | String           | `list`.                                                                             |
| `type`                   | String           | `property_item`.                                                                    |
| `results`                | Array            | The property items in this response.                                                |
| `has_more`               | Boolean          | Whether another page of results exists.                                             |
| `next_cursor`            | String or `null` | Pass this as `start_cursor` in the next request.                                    |
| `property_item`          | Object           | Metadata for the property being retrieved.                                          |
| `property_item.id`       | String           | The requested property ID.                                                          |
| `property_item.type`     | String           | The requested property type.                                                        |
| `property_item.next_url` | String or `null` | The URL for the next request. This field is nested, not top-level.                  |
| `property_item.{type}`   | Object           | Empty for the four list types above. Rollups include a result or calculation state. |

The metadata under `property_item` is not an individual result and has no `object` field. For a relation item, the nested `relation.id` identifies the related page; the item’s own `id` identifies the property.

```json First page of a relation, with page_size=1 theme={null}
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "id": "proj",
      "type": "relation",
      "relation": { "id": "dd456007-6c66-4bba-957e-ea501dcda3a6" }
    }
  ],
  "next_cursor": "opaque-cursor",
  "has_more": true,
  "type": "property_item",
  "property_item": {
    "id": "proj",
    "next_url": "https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7/properties/proj?start_cursor=opaque-cursor&page_size=1",
    "type": "relation",
    "relation": {}
  }
}
```

Continue with `next_cursor` until `has_more` is `false`. In the final response, `next_cursor` and `property_item.next_url` are `null`. Treat cursors as opaque strings; do not build or interpret them.

The [pagination reference](/reference/pagination) defines `start_cursor` and `page_size`. For a complete SDK example, see [Read every item in a page property](/guides/data-apis/read-page-property-values).

<span />

Select, multi-select, and status [option values](/reference/property-object#select-options) share the same fields.

## Formula

<span />

<span />

<span />

<span />

A formula returns one property item with a typed `formula` result. It does not return a paginated list. See [Formula result types](/reference/page-property-values#formula-result-types) for string, number, boolean, and date examples.

### Unsupported formula

A formula or rollup can return `type: "unsupported"` with `unsupported: {}` when it depends on too many related pages or nested calculations. This result has no usable value. Reduce the related pages or simplify the calculation. Requesting the property again does not remove this limit.

For data source queries, [filter the returned properties](/guides/data-apis/query-large-data-sources) and retrieve details only when you need them.

## Rollup

A rollup returns a list with its calculation in `property_item.rollup`. That object always includes `function` and `type`.

For `show_original`, `results` contains the target property’s values, flattened into individual property items. The metadata uses `type: "array"` and `array: []`; the values are in `results`, not that empty array.

For a supported calculation such as `sum`, `results` contains relation items. The calculation is incomplete until you read the final page. Do not sum partial responses yourself or treat the first response as the final value.

<span />

<span />

<span />

| Rollup `type` | Meaning                                                     |
| :------------ | :---------------------------------------------------------- |
| `number`      | A completed number result in `number`, which can be `null`. |
| `date`        | A completed date result in `date`, which can be `null`.     |
| `array`       | Individual values are in the response’s `results` array.    |
| `incomplete`  | Read the next page to continue the calculation.             |
| `unsupported` | This endpoint has no computed result. See the limits below. |

### Incomplete rollup

These examples show the `property_item` metadata from consecutive responses. The first response has `has_more: true`; the final response has `has_more: false`.

<CodeGroup>
  ```json More results remain theme={null}
  {
    "id": "roll",
    "next_url": "https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7/properties/roll?start_cursor=opaque-cursor&page_size=1",
    "type": "rollup",
    "rollup": { "type": "incomplete", "incomplete": {}, "function": "sum" }
  }
  ```

  ```json Final result theme={null}
  {
    "id": "roll",
    "next_url": null,
    "type": "rollup",
    "rollup": { "type": "number", "number": 13, "function": "sum" }
  }
  ```
</CodeGroup>

### Unsupported rollup

This endpoint does not calculate `show_unique`, `unique`, `median`, `count_per_group`, or `percent_per_group`. It returns the underlying property items in `results` and `type: "unsupported"` in `property_item.rollup`. Pagination can still be needed to read all those items.

A formula or rollup can return `type: "unsupported"` with `unsupported: {}` when it depends on too many related pages or nested calculations. This result has no usable value. Reduce the related pages or simplify the calculation. Requesting the property again does not remove this limit.

For data source queries, [filter the returned properties](/guides/data-apis/query-large-data-sources) and retrieve details only when you need them.

When a dependency limit prevents a calculation, the rollup also returns `unsupported`. An unsupported result is not zero and is not an incomplete result that will become available through more requests.
