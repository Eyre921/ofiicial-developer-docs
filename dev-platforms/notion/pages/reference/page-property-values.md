---
title: "Page property values"
source: https://developers.notion.com/reference/page-property-values
path: reference/page-property-values
---

Reference for reading, writing, and clearing each type of page property value.

<span />

<span />

## Overview

A page’s `properties` object holds its property values. In a data source, each page is a row and each property is a column in table view. The data source defines the property names and types.

| Object                                                 | What it describes                                              | Endpoint                                                             |
| :----------------------------------------------------- | :------------------------------------------------------------- | :------------------------------------------------------------------- |
| [Data source property](/reference/property-object)     | A property’s name, type, and settings, also called its schema. | [Retrieve a data source](/reference/retrieve-a-data-source)          |
| [Page property value](/reference/page-property-values) | The value of that property on one page.                        | [Retrieve a page](/reference/retrieve-a-page)                        |
| [Page property item](/reference/property-item-object)  | A single value, or one item in a paginated value.              | [Retrieve a page property item](/reference/retrieve-a-page-property) |

The tabs compare the same property across API objects. Schema and Page value examples each show one entry in a response’s `properties` object. Page write shows an Update page request body; Create page also needs a parent. Read-only types have no Page write tab.

For `title`, `rich_text`, `people`, and `relation`, the Property item tab shows one entry in a paginated `results` array. For other types, it shows the endpoint response. Replace example names and IDs with values from your workspace.

## Attributes

| Field               | Type   | Meaning                                                                   |
| :------------------ | :----- | :------------------------------------------------------------------------ |
| `id`                | String | The property’s ID.                                                        |
| `type`              | String | The API property type, such as `status` or `rich_text`.                   |
| Key matching `type` | Varies | The value. It can be a string, number, boolean, object, array, or `null`. |

A property’s `id` stays the same when its name changes. IDs can be short strings or UUIDs. The Name property always has the ID `title`.

Responses use URL-encoded property IDs, such as `f%5C%5C%3Ap`. Pass the returned ID as-is to the SDK or in an API path. Don’t encode it a second time. You can also use a property ID as a key in a request’s `properties` object.

Page responses map property names to values. Page writes can use names or IDs. A page whose parent is another page has only a `title` property. For pages in a data source, write keys must match that data source’s schema.

The `object: "property_item"` field appears only in [property-item responses](/reference/property-item-object). It is not part of a page response’s `properties` entries.

## Writing and clearing values

[Create page](/reference/post-page) and [Update page](/reference/patch-page) accept a `properties` object. Each entry contains the key for its type and the value to save. Response-only fields such as `id`, `has_more`, and rich text `plain_text` are not needed in a write.

On update, omitted properties keep their values. An array replaces the entire value of that property; it does not append items. Keep any existing people, files, tags, or related pages you still need in the submitted array.

| To clear                                                            | Send                                                              |
| :------------------------------------------------------------------ | :---------------------------------------------------------------- |
| `title`, `rich_text`, `people`, `relation`, `multi_select`, `files` | An empty array: `[]`. An empty Name displays as an untitled page. |
| `number`, `url`, `email`, `phone_number`, `select`, `date`, `place` | `null` as the type’s value.                                       |
| `status`                                                            | `null` resets the value to the default option, if one is set.     |
| `checkbox`                                                          | `false`.                                                          |
| `verification`                                                      | `{ "state": "unverified" }`.                                      |

For example, `{"properties":{"Due date":{"date":null}}}` clears a page’s date. Setting a whole schema entry to `null` instead [removes the property from the data source](/reference/update-data-source-properties#remove-a-property).

Writes must fit the [request limits](/reference/request-limits). A successful read can contain more items than one write accepts.

## Type objects

<span />

### Button

A Button property returns `button: {}`. The API does not expose its actions or let you press it by updating a page.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Send update": {
        "id": "btnA",
        "name": "Send update",
        "description": null,
        "type": "button",
        "button": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Send update": {
        "id": "btnA",
        "type": "button",
        "button": {}
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "btnA",
      "type": "button",
      "button": {}
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Checkbox

`checkbox` is `true` when checked and `false` when unchecked.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Done": {
        "id": "done",
        "name": "Done",
        "description": null,
        "type": "checkbox",
        "checkbox": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Done": {
        "id": "done",
        "type": "checkbox",
        "checkbox": true
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Done": {
          "checkbox": true
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "done",
      "type": "checkbox",
      "checkbox": true
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

### Created by

`created_by` is a [user object](/reference/user) for the page’s creator. Notion sets this read-only value. The user object may contain only `object` and `id`.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Created by": {
        "id": "crtB",
        "name": "Created by",
        "description": null,
        "type": "created_by",
        "created_by": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Created by": {
        "id": "crtB",
        "type": "created_by",
        "created_by": {
          "object": "user",
          "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "crtB",
      "type": "created_by",
      "created_by": {
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

### Created time

`created_time` is the page’s creation time as an ISO 8601 timestamp. Notion sets this read-only value.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Created time": {
        "id": "crtT",
        "name": "Created time",
        "description": null,
        "type": "created_time",
        "created_time": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Created time": {
        "id": "crtT",
        "type": "created_time",
        "created_time": "2026-09-01T09:00:00.000Z"
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "crtT",
      "type": "created_time",
      "created_time": "2026-09-01T09:00:00.000Z"
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Date

`date` is a date object or `null`. It can hold a date, a time, or a range.

| Field       | Type             | Meaning                                                 |
| :---------- | :--------------- | :------------------------------------------------------ |
| `start`     | String           | Required. An ISO 8601 date or date and time.            |
| `end`       | String or `null` | The end of a range. `null` means a single date or time. |
| `time_zone` | String or `null` | An IANA time zone, such as `America/Los_Angeles`.       |

When you provide `time_zone`, include a time in `start` and `end`, without a UTC offset. Otherwise, use an offset in a timestamp or a date such as `2026-09-15`. Omitted `end` and `time_zone` fields return as `null`.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Due date": {
        "id": "dueD",
        "name": "Due date",
        "description": null,
        "type": "date",
        "date": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Due date": {
        "id": "dueD",
        "type": "date",
        "date": {
          "start": "2026-09-15",
          "end": null,
          "time_zone": null
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Due date": {
          "date": {
            "start": "2026-09-15"
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
      "id": "dueD",
      "type": "date",
      "date": {
        "start": "2026-09-15",
        "end": null,
        "time_zone": null
      }
    }
    ```
  </Tab>
</Tabs>

<CodeGroup>
  ```json Date range theme={null}
  {"date":{"start":"2026-09-15","end":"2026-09-18"}}
  ```

  ```json Time with an offset theme={null}
  {"date":{"start":"2026-09-15T09:00:00-07:00"}}
  ```

  ```json Named time zone theme={null}
  {"date":{"start":"2026-09-15T09:00:00","time_zone":"America/Los_Angeles"}}
  ```
</CodeGroup>

<span />

<span />

<span />

### Email

`email` is an email address string or `null`.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Contact email": {
        "id": "emlA",
        "name": "Contact email",
        "description": null,
        "type": "email",
        "email": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Contact email": {
        "id": "emlA",
        "type": "email",
        "email": "alex@example.com"
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Contact email": {
          "email": "alex@example.com"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "emlA",
      "type": "email",
      "email": "alex@example.com"
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Files

The Files & media property uses the API key `files`. Its value is an array of [file objects](/reference/file-object), each with a `name`.

An external file uses `external: { "url": "https://example.com/file.pdf" }`. A file hosted by Notion returns `type: "file"`, a temporary download URL, and an `expiry_time`. Retrieve the page again to get a fresh URL after it expires.

To attach an uploaded file, use `type: "file_upload"` and `file_upload: { "id": "..." }` with a completed [file upload](/guides/data-apis/uploading-small-files). Reads return the attached file as `type: "file"`, not `file_upload`. A file update replaces the full list, so include files you want to keep.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Attachments": {
        "id": "file",
        "name": "Attachments",
        "description": null,
        "type": "files",
        "files": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Attachments": {
        "id": "file",
        "type": "files",
        "files": [
          {
            "name": "Project brief.pdf",
            "type": "external",
            "external": {
              "url": "https://example.com/project-brief.pdf"
            }
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Attachments": {
          "files": [
            {
              "name": "Project brief.pdf",
              "type": "external",
              "external": {
                "url": "https://example.com/project-brief.pdf"
              }
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "file",
      "type": "files",
      "files": [
        {
          "name": "Project brief.pdf",
          "type": "external",
          "external": {
            "url": "https://example.com/project-brief.pdf"
          }
        }
      ]
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

<span />

<span />

<span />

### Formula

`formula` holds the result of the expression in the [data source schema](/reference/property-object#formula). The result is read-only; the expression can be changed through [Update a data source](/reference/update-a-data-source).

The result’s `type` is `string`, `number`, `boolean`, `date`, or `unsupported`. Read the field with that name. A supported result can be `null` when it has no value.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Double estimate": {
        "id": "calc",
        "name": "Double estimate",
        "description": null,
        "type": "formula",
        "formula": {
          "expression": "prop(\"Estimate\") * 2"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Double estimate": {
        "id": "calc",
        "type": "formula",
        "formula": {
          "type": "number",
          "number": 16
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "calc",
      "type": "formula",
      "formula": {
        "type": "number",
        "number": 16
      }
    }
    ```
  </Tab>
</Tabs>

#### Formula result types

These are the objects inside the `formula` field.

<CodeGroup>
  ```json String theme={null}
  {"type":"string","string":"Ready"}
  ```

  ```json Number theme={null}
  {"type":"number","number":16}
  ```

  ```json Boolean theme={null}
  {"type":"boolean","boolean":true}
  ```

  ```json Date theme={null}
  {"type":"date","date":{"start":"2026-09-15","end":null,"time_zone":null}}
  ```

  ```json Empty result theme={null}
  {"type":"number","number":null}
  ```
</CodeGroup>

#### Unsupported formula

A formula or rollup can return `type: "unsupported"` with `unsupported: {}` when it depends on too many related pages or nested calculations. This result has no usable value. Reduce the related pages or simplify the calculation. Requesting the property again does not remove this limit.

For data source queries, [filter the returned properties](/guides/data-apis/query-large-data-sources) and retrieve details only when you need them.

```json Formula field theme={null}
{"type":"unsupported","unsupported":{}}
```

<span />

<span />

### Last edited by

`last_edited_by` is a [user object](/reference/user) for the page’s last editor. Notion sets this read-only value. The user object may contain only `object` and `id`.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Last edited by": {
        "id": "edtB",
        "name": "Last edited by",
        "description": null,
        "type": "last_edited_by",
        "last_edited_by": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Last edited by": {
        "id": "edtB",
        "type": "last_edited_by",
        "last_edited_by": {
          "object": "user",
          "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "edtB",
      "type": "last_edited_by",
      "last_edited_by": {
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

### Last edited time

`last_edited_time` is the page’s last edit time as an ISO 8601 timestamp. Notion sets this read-only value.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Last edited time": {
        "id": "edtT",
        "name": "Last edited time",
        "description": null,
        "type": "last_edited_time",
        "last_edited_time": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Last edited time": {
        "id": "edtT",
        "type": "last_edited_time",
        "last_edited_time": "2026-09-04T14:30:00.000Z"
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "edtT",
      "type": "last_edited_time",
      "last_edited_time": "2026-09-04T14:30:00.000Z"
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

<span />

### Multi-select

`multi_select` is an array of selected options. Each response option has `id`, `name`, and `color`. Write options by `id` or `name`; use `[]` for no selection.

A new option name adds an option to the schema if your connection can write to the parent data source. Option names cannot contain commas. To edit the available options, see [Multi-select schemas](/reference/property-object#multi-select).

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Tags": {
        "id": "tags",
        "name": "Tags",
        "description": null,
        "type": "multi_select",
        "multi_select": {
          "options": [
            {
              "id": "ff8e9269-9579-47f7-8f6e-83a84716863c",
              "name": "High",
              "color": "red",
              "description": null
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
      "Tags": {
        "id": "tags",
        "type": "multi_select",
        "multi_select": [
          {
            "id": "ff8e9269-9579-47f7-8f6e-83a84716863c",
            "name": "High",
            "color": "red"
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Tags": {
          "multi_select": [
            {
              "name": "High"
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "tags",
      "type": "multi_select",
      "multi_select": [
        {
          "id": "ff8e9269-9579-47f7-8f6e-83a84716863c",
          "name": "High",
          "color": "red"
        }
      ]
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Number

`number` is a JSON number or `null`. The [schema’s number format](/reference/property-object#number) controls its display in Notion. For example, `0.25` displays as 25% with the `percent` format.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Estimate": {
        "id": "estM",
        "name": "Estimate",
        "description": null,
        "type": "number",
        "number": {
          "format": "number"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Estimate": {
        "id": "estM",
        "type": "number",
        "number": 8
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Estimate": {
          "number": 8
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "estM",
      "type": "number",
      "number": 8
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### People

The Person property uses the API key `people`. A page response contains an array of people or groups. [User objects](/reference/user) can be partial, so do not assume that a name or email is present.

Writes accept user IDs, including bots that appear as user objects in the API. Bots used internally by Notion may not be assignable. [Retrieve a page property item](/reference/retrieve-a-page-property) returns a paginated list with one user in each item’s `people` field. Use it when a page response omits people.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Owner": {
        "id": "ownR",
        "name": "Owner",
        "description": null,
        "type": "people",
        "people": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Owner": {
        "id": "ownR",
        "type": "people",
        "people": [
          {
            "object": "user",
            "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Owner": {
          "people": [
            {
              "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "ownR",
      "type": "people",
      "people": {
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Phone number

The Phone property uses the API key `phone_number`. Its value is a string or `null`. The API does not enforce a phone-number format.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Contact phone": {
        "id": "phon",
        "name": "Contact phone",
        "description": null,
        "type": "phone_number",
        "phone_number": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Contact phone": {
        "id": "phon",
        "type": "phone_number",
        "phone_number": "+1 415 555 0123"
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Contact phone": {
          "phone_number": "+1 415 555 0123"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "phon",
      "type": "phone_number",
      "phone_number": "+1 415 555 0123"
    }
    ```
  </Tab>
</Tabs>

<span />

### Place

`place` is a location object or `null`. It supports reading and writing coordinates, with optional place details. It is the property used by [map views](https://www.notion.com/help/maps).

| Field                             | Type             | Meaning                                                    |
| :-------------------------------- | :--------------- | :--------------------------------------------------------- |
| `lat`, `lon`                      | Number           | Required latitude (−90 to 90) and longitude (−180 to 180). |
| `name`                            | String or `null` | The place’s name.                                          |
| `address`                         | String or `null` | The address.                                               |
| `aws_place_id`, `google_place_id` | String or `null` | Optional place IDs from the named provider.                |

The API does not look up coordinates from a name or address. Provide `lat` and `lon` when writing a value.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Office": {
        "id": "plce",
        "name": "Office",
        "description": null,
        "type": "place",
        "place": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Office": {
        "id": "plce",
        "type": "place",
        "place": {
          "lat": 37.7749,
          "lon": -122.4194,
          "name": "San Francisco",
          "address": null,
          "aws_place_id": null,
          "google_place_id": null
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Office": {
          "place": {
            "lat": 37.7749,
            "lon": -122.4194,
            "name": "San Francisco"
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
      "id": "plce",
      "type": "place",
      "place": {
        "lat": 37.7749,
        "lon": -122.4194,
        "name": "San Francisco",
        "address": null,
        "aws_place_id": null,
        "google_place_id": null
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Relation

`relation` is an array of related page IDs. Each page must belong to the data source named by the [relation schema](/reference/property-object#relation).

In a page response, `has_more: true` means the relation has more than 25 page references. Use [property-item pagination](/reference/property-item-object#paginated-values) to read the rest. A page write replaces the relation, so read all existing references before adding one.

Share the related database with your connection too. Missing access can leave relation values empty or make formula and rollup results incomplete. Check access before treating an empty result as missing data.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Projects": {
        "id": "proj",
        "name": "Projects",
        "description": null,
        "type": "relation",
        "relation": {
          "database_id": "668d797c-76fa-4934-9b05-ad288df2d136",
          "data_source_id": "6c4240a9-a3ce-413e-9fd0-8a51a4d0a49b",
          "type": "single_property",
          "single_property": {}
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Projects": {
        "id": "proj",
        "type": "relation",
        "relation": [
          {
            "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
          }
        ],
        "has_more": false
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Projects": {
          "relation": [
            {
              "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "proj",
      "type": "relation",
      "relation": {
        "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Rich text

The Text property uses the API key `rich_text`. Its value is an array of [rich text objects](/reference/rich-text). These can contain formatted text, mentions, and equations.

Writes use the input fields for each rich text type. Responses also include `annotations`, `plain_text`, and `href`. Text in a page property is separate from the page’s [content blocks](/reference/block).

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Summary": {
        "id": "text",
        "name": "Summary",
        "description": null,
        "type": "rich_text",
        "rich_text": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Summary": {
        "id": "text",
        "type": "rich_text",
        "rich_text": [
          {
            "type": "text",
            "text": {
              "content": "Launch checklist",
              "link": null
            },
            "annotations": {
              "bold": false,
              "italic": false,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "Launch checklist",
            "href": null
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Summary": {
          "rich_text": [
            {
              "type": "text",
              "text": {
                "content": "Launch checklist"
              }
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "text",
      "type": "rich_text",
      "rich_text": {
        "type": "text",
        "text": {
          "content": "Launch checklist",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "Launch checklist",
        "href": null
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

<span />

<span />

<span />

### Rollup

`rollup` holds the result of a calculation over a relation. Its value is read-only. The [schema](/reference/property-object#rollup) defines the relation, target property, and `function`.

| Result `type` | Value field                                                       |
| :------------ | :---------------------------------------------------------------- |
| `number`      | `number`: a number or `null`.                                     |
| `date`        | `date`: a date object or `null`.                                  |
| `array`       | `array`: an array of typed property values, without property IDs. |
| `unsupported` | `unsupported`: an empty object. No usable result is available.    |

A page response puts array values in `rollup.array`. The property-item endpoint puts individual values in `results` and rollup metadata in `property_item.rollup`. It can also return `type: "incomplete"` while [pagination is in progress](/reference/property-item-object#rollup).

Share the related database with your connection too. Missing access can leave relation values empty or make formula and rollup results incomplete. Check access before treating an empty result as missing data.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Total estimate": {
        "id": "roll",
        "name": "Total estimate",
        "description": null,
        "type": "rollup",
        "rollup": {
          "relation_property_id": "proj",
          "relation_property_name": "Projects",
          "rollup_property_id": "estM",
          "rollup_property_name": "Estimate",
          "function": "sum"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Total estimate": {
        "id": "roll",
        "type": "rollup",
        "rollup": {
          "type": "number",
          "number": 8,
          "function": "sum"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "list",
      "results": [
        {
          "object": "property_item",
          "id": "proj",
          "type": "relation",
          "relation": {
            "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
          }
        }
      ],
      "next_cursor": null,
      "has_more": false,
      "type": "property_item",
      "property_item": {
        "id": "roll",
        "next_url": null,
        "type": "rollup",
        "rollup": {
          "type": "number",
          "number": 8,
          "function": "sum"
        }
      }
    }
    ```
  </Tab>
</Tabs>

<CodeGroup>
  ```json Date rollup field theme={null}
  {"type":"date","date":{"start":"2026-09-15","end":null,"time_zone":null},"function":"earliest_date"}
  ```

  ```json Array rollup field in a page response theme={null}
  {"type":"array","array":[{"type":"number","number":8},{"type":"number","number":5}],"function":"show_original"}
  ```
</CodeGroup>

#### Unsupported rollup

A formula or rollup can return `type: "unsupported"` with `unsupported: {}` when it depends on too many related pages or nested calculations. This result has no usable value. Reduce the related pages or simplify the calculation. Requesting the property again does not remove this limit.

For data source queries, [filter the returned properties](/guides/data-apis/query-large-data-sources) and retrieve details only when you need them.

```json Rollup field theme={null}
{"type":"unsupported","unsupported":{},"function":"sum"}
```

Some rollup functions also have [endpoint-specific limits](/reference/property-item-object#unsupported-rollup).

<span />

<span />

<span />

### Select

`select` is one option object or `null`. A response option has `id`, `name`, and `color`. Write an option by `id` or `name`.

A new option name adds an option to the schema if your connection can write to the parent data source. Option names cannot contain commas. Option colors belong to the [schema](/reference/property-object#select), not the page value.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Priority": {
        "id": "prio",
        "name": "Priority",
        "description": null,
        "type": "select",
        "select": {
          "options": [
            {
              "id": "ff8e9269-9579-47f7-8f6e-83a84716863c",
              "name": "High",
              "color": "red",
              "description": null
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
      "Priority": {
        "id": "prio",
        "type": "select",
        "select": {
          "id": "ff8e9269-9579-47f7-8f6e-83a84716863c",
          "name": "High",
          "color": "red"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Priority": {
          "select": {
            "name": "High"
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
      "id": "prio",
      "type": "select",
      "select": {
        "id": "ff8e9269-9579-47f7-8f6e-83a84716863c",
        "name": "High",
        "color": "red"
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Status

`status` is one status option or `null`. The response contains `id`, `name`, and `color`, just like a select value. Write an existing status option by `id` or `name`.

A page write does not create a new status option or set its group. Use [Update data source properties](/reference/update-data-source-properties#status-configuration-updates) to manage status options.

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

<span />

<span />

<span />

### Title

The Name property uses the API key `title`. Its value is an array of [rich text objects](/reference/rich-text). Each data source has exactly one Name property, which names each page in that data source.

For a page whose parent is another page, use `title` as the property key. This is separate from the name of the data source itself.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Name": {
        "id": "title",
        "name": "Name",
        "description": null,
        "type": "title",
        "title": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Name": {
        "id": "title",
        "type": "title",
        "title": [
          {
            "type": "text",
            "text": {
              "content": "Launch checklist",
              "link": null
            },
            "annotations": {
              "bold": false,
              "italic": false,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "Launch checklist",
            "href": null
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Name": {
          "title": [
            {
              "type": "text",
              "text": {
                "content": "Launch checklist"
              }
            }
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "title",
      "type": "title",
      "title": {
        "type": "text",
        "text": {
          "content": "Launch checklist",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "Launch checklist",
        "href": null
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

### Unique ID

The ID property uses the API key `unique_id`. It contains `number` and `prefix`. Notion assigns the number; you cannot set it in a page write. The number is unique within the data source. Either field can be `null`.

The [schema’s prefix](/reference/property-object#unique-id) controls labels such as `TASK-42`.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Task ID": {
        "id": "task",
        "name": "Task ID",
        "description": null,
        "type": "unique_id",
        "unique_id": {
          "prefix": "TASK"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Task ID": {
        "id": "task",
        "type": "unique_id",
        "unique_id": {
          "number": 42,
          "prefix": "TASK"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "task",
      "type": "unique_id",
      "unique_id": {
        "number": 42,
        "prefix": "TASK"
      }
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### URL

`url` is a URL string or `null`.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Project link": {
        "id": "link",
        "name": "Project link",
        "description": null,
        "type": "url",
        "url": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Project link": {
        "id": "link",
        "type": "url",
        "url": "https://example.com/projects/launch"
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Project link": {
          "url": "https://example.com/projects/launch"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Property item">
    ```json Property item theme={null}
    {
      "object": "property_item",
      "id": "link",
      "type": "url",
      "url": "https://example.com/projects/launch"
    }
    ```
  </Tab>
</Tabs>

<span />

<span />

<span />

### Verification

`verification` is available on pages in a [wiki database](/guides/data-apis/working-with-databases#wiki-databases). It is an object or `null`.

| Field         | Type                  | Meaning                                                                                        |
| :------------ | :-------------------- | :--------------------------------------------------------------------------------------------- |
| `state`       | String                | `verified`, `unverified`, or `expired`. Writes accept only `verified` and `unverified`.        |
| `date`        | Date object or `null` | The verification period. `start` and any `end` must include a time. `end` sets the expiration. |
| `verified_by` | User object or `null` | Who verified the page. Notion sets this field.                                                 |

Verification dates require timestamps, such as `2026-09-15T09:00:00Z`. Date-only values such as `2026-09-15` return a validation error. Omit `date` or set it to `null` to verify without an expiration.

An unverified value has `date: null` and `verified_by: null`. A verified page becomes expired when its end date passes.

You can write verification through [Create page](/reference/post-page) or [Update page](/reference/patch-page). The acting connection is recorded as the verifier. Omit `verified_by` and do not set the wiki’s verification Owner property in the same request.

<Tabs>
  <Tab title="Schema">
    ```json Schema theme={null}
    {
      "Verification": {
        "id": "vrfy",
        "name": "Verification",
        "description": null,
        "type": "verification",
        "verification": {}
      }
    }
    ```
  </Tab>

  <Tab title="Page value">
    ```json Page value theme={null}
    {
      "Verification": {
        "id": "vrfy",
        "type": "verification",
        "verification": {
          "state": "verified",
          "date": {
            "start": "2026-09-01T09:00:00.000Z",
            "end": "2026-10-01T09:00:00.000Z",
            "time_zone": null
          },
          "verified_by": {
            "object": "user",
            "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="Page write">
    ```json Page write theme={null}
    {
      "properties": {
        "Verification": {
          "verification": {
            "state": "verified",
            "date": {
              "start": "2026-09-01T09:00:00.000Z",
              "end": "2026-10-01T09:00:00.000Z"
            }
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
      "id": "vrfy",
      "type": "verification",
      "verification": {
        "state": "verified",
        "date": {
          "start": "2026-09-01T09:00:00.000Z",
          "end": "2026-10-01T09:00:00.000Z",
          "time_zone": null
        },
        "verified_by": {
          "object": "user",
          "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
        }
      }
    }
    ```
  </Tab>
</Tabs>

### Unsupported properties

Not every property feature in Notion is writable through the API. Button values are empty objects. Unknown or unavailable values must not be copied into page writes. A `null` value can also mean an empty supported property; it does not by itself mean that the type is unsupported.

<span />

### Icon

A page’s `icon` and `cover` are top-level fields on the [page object](/reference/page). They are not entries in `properties`. See [Emoji and icon](/reference/emoji-and-icon) for icon types and examples.

## Paginated page properties

A page response can omit values when a property refers to many pages or people:

| Property             | Page response limit                                                                                  |
| :------------------- | :--------------------------------------------------------------------------------------------------- |
| `relation`           | Up to 25 page references. `has_more: true` means more references exist.                              |
| `people`             | More than 25 people may be omitted.                                                                  |
| `title`, `rich_text` | Up to 25 populated inline page or person mentions. This is a mention limit, not a text-length limit. |
| `formula`, `rollup`  | Results can depend on references that the page response does not fully load.                         |

Use [Retrieve a page property item](/reference/retrieve-a-page-property) when you need the full value. Read every [page of property items](/reference/property-item-object#paginated-values). Formula and rollup [calculation limits](/reference/page-property-values#unsupported-formula) still apply.

The list response and cursor fields are defined in [Page property items](/reference/property-item-object#paginated-values). For a complete SDK example, see [Read every item in a page property](/guides/data-apis/read-page-property-values).
