---
title: "Data source properties"
source: https://developers.notion.com/reference/property-object
path: reference/property-object
---

Reference for property types, settings, and examples in a data source schema.

A data source’s `properties` object defines the names, types, and settings of its properties. This is its **schema**. In Notion’s table view, these properties appear as columns.

| Object                                                 | What it describes                                              | Endpoint                                                             |
| :----------------------------------------------------- | :------------------------------------------------------------- | :------------------------------------------------------------------- |
| [Data source property](/reference/property-object)     | A property’s name, type, and settings, also called its schema. | [Retrieve a data source](/reference/retrieve-a-data-source)          |
| [Page property value](/reference/page-property-values) | The value of that property on one page.                        | [Retrieve a page](/reference/retrieve-a-page)                        |
| [Page property item](/reference/property-item-object)  | A single value, or one item in a paginated value.              | [Retrieve a page property item](/reference/retrieve-a-page-property) |

<span />

## Common fields

| Field               | Type             | Meaning                                                 |
| :------------------ | :--------------- | :------------------------------------------------------ |
| `id`                | String           | The property’s stable ID.                               |
| `name`              | String           | The property’s name in Notion.                          |
| `description`       | String or `null` | The property’s description.                             |
| `type`              | String           | The property type, such as `number` or `status`.        |
| Key matching `type` | Object           | Settings for that type. Many types use an empty object. |

A property’s `id` stays the same when its name changes. IDs can be short strings or UUIDs. The Name property always has the ID `title`.

Responses use URL-encoded property IDs, such as `f%5C%5C%3Ap`. Pass the returned ID as-is to the SDK or in an API path. Don’t encode it a second time. You can also use a property ID as a key in a request’s `properties` object.

The tabs compare the same property across API objects. Schema and Page value examples each show one entry in a response’s `properties` object. Page write shows an Update page request body; Create page also needs a parent. Read-only types have no Page write tab.

For `title`, `rich_text`, `people`, and `relation`, the Property item tab shows one entry in a paginated `results` array. For other types, it shows the endpoint response. Replace example names and IDs with values from your workspace.

## Request and response shapes

Schema responses contain the common fields above. For types that support schema writes, create a property by using its name as the key and providing its type’s settings. Button and Verification schemas are response-only; see their limits below. For example, `{"Estimate":{"number":{"format":"number"}}}` is an entry in the request’s `properties` object.

Use [Create a data source](/reference/create-a-data-source) to define an initial schema. Use [Update data source properties](/reference/update-data-source-properties) to add, rename, remove, or change properties. The page-write tabs below change values on a page; they do not change the schema.

<Note>
  For API versions before `2025-09-03`, schemas belong to [database objects](/reference/retrieve-a-database). Those requests use the legacy database endpoints and `database_id` for relation targets. Current API versions use data sources. See [Upgrade to 2025-09-03](/guides/get-started/upgrade-guide-2025-09-03).
</Note>

<span />

## Button

A Button property has an empty `button` object in schema responses. Create Button properties and configure their actions in Notion. The API ignores `button` settings in schema writes; it does not create a Button property or change an existing one. It also does not expose button actions or let you press a button.

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

## Checkbox

The `checkbox` settings object is empty. Page values are booleans.

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

## Created by

The `created_by` settings object is empty. Notion sets each page’s creator; page values are read-only.

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

## Created time

The `created_time` settings object is empty. Notion sets each page’s creation time; page values are read-only.

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

## Date

The `date` settings object is empty. A page value can be a date, a timestamp, or a range.

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

<span />

## Email

The `email` settings object is empty.

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

## Files

The Files & media property uses `files: {}`. A page value is an array of named files.

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

## Formula

The `formula` object contains an `expression` string. The expression uses [Notion’s formula syntax](https://www.notion.com/help/formulas) and properties from the same data source. The computed page value is read-only.

Example expressions with fixed inputs:

| Expression                                        | Example input                               | Result type | Result     |
| :------------------------------------------------ | :------------------------------------------ | :---------- | :--------- |
| `prop("Price") * 1.1`                             | Price is `10`.                              | Number      | `11`       |
| `if(prop("In stock"), "yes", "no")`               | In stock is checked.                        | String      | `"yes"`    |
| `format(prop("ID"))`                              | ID is `TASK-1`.                             | String      | `"TASK-1"` |
| `dateBetween(prop("Due"), prop("Start"), "days")` | Due is `2026-09-15`; Start is `2026-09-09`. | Number      | `6`        |

`prop("Name")` looks up a property by its current name. The saved formula refers to its ID, so a later rename does not break that reference.

An expression that cannot be parsed or checked returns [validation\_error](/reference/status-codes#error-codes). This includes references to properties that do not exist.

Schema responses normally use the same `prop("Name")` syntax as requests. If an expression cannot be represented that way, the response uses `{{notion:block_property:...}}` references. Those references are also valid in requests.

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

<span />

## Last edited by

The `last_edited_by` settings object is empty. Notion sets each page’s last editor; page values are read-only.

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

## Last edited time

The `last_edited_time` settings object is empty. Notion sets each page’s last edit time; page values are read-only.

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

## Multi-select

The `multi_select` object contains an `options` array. Each page can select zero or more options. [Option fields](#select-options) are shared with select and status properties.

To add or remove available options, use [Multi-select configuration updates](/reference/update-data-source-properties#multi-select-configuration-updates).

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

## Number

The `number` object contains `format`, which controls display in Notion. It does not change the stored number. The default is `number`.

Supported formats are `number`, `number_with_commas`, `percent`, `dollar`, `australian_dollar`, `canadian_dollar`, `singapore_dollar`, `euro`, `pound`, `yen`, `ruble`, `rupee`, `won`, `yuan`, `real`, `lira`, `rupiah`, `franc`, `hong_kong_dollar`, `new_zealand_dollar`, `krona`, `norwegian_krone`, `mexican_peso`, `rand`, `new_taiwan_dollar`, `danish_krone`, `zloty`, `baht`, `forint`, `koruna`, `shekel`, `chilean_peso`, `philippine_peso`, `dirham`, `colombian_peso`, `riyal`, `ringgit`, `leu`, `argentine_peso`, `uruguayan_peso`, `peruvian_sol`, `vietnamese_dong`, `pakistani_rupee`, `nigerian_naira`, and `bitcoin`.

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

## People

The Person property uses `people: {}`. Page values contain people or groups.

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

## Phone number

The Phone property uses `phone_number: {}`.

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

## Place

The Place property uses `place: {}`. Page values contain coordinates and optional place details, or `null` when empty.

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

## Relation

A relation links pages to pages in a target data source.

| Field             | Meaning                                                        |
| :---------------- | :------------------------------------------------------------- |
| `data_source_id`  | The target data source’s ID. Use this in current API requests. |
| `database_id`     | The target’s parent database ID, included in responses.        |
| `type`            | `single_property` or `dual_property`.                          |
| `single_property` | An empty object for a one-way relation.                        |
| `dual_property`   | Settings for the matching relation on the target data source.  |

A one-way relation uses `type: "single_property"` and `single_property: {}`.

A two-way relation uses `type: "dual_property"`. Its response includes `dual_property.synced_property_id` and `dual_property.synced_property_name`. A create request can use `dual_property: {}` to create the matching property.

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

## Rich text

The Text property uses `rich_text: {}`. Its page values are rich text arrays.

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

## Rollup

A rollup reads a property through a relation and applies a `function`.

| Field                                            | Meaning                                                                                       |
| :----------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| `relation_property_name`, `relation_property_id` | The relation in this data source. Supply its name or ID in a request.                         |
| `rollup_property_name`, `rollup_property_id`     | The property in the target data source to calculate over. Supply its name or ID in a request. |
| `function`                                       | The calculation to perform. Required in a request.                                            |

Responses include both names and IDs. The target property belongs to the related data source; the relation property belongs to the source where you define the rollup.

Functions are `count`, `count_values`, `empty`, `not_empty`, `unique`, `show_unique`, `percent_empty`, `percent_not_empty`, `sum`, `average`, `median`, `min`, `max`, `range`, `earliest_date`, `latest_date`, `date_range`, `checked`, `unchecked`, `percent_checked`, `percent_unchecked`, `count_per_group`, `percent_per_group`, and `show_original`.

The function can be configured even when [property-item retrieval cannot calculate it](/reference/property-item-object#unsupported-rollup). Page values are read-only.

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

<span />

## Select

The `select` object contains an `options` array. Each page can select one option or no option.

### Select options

Each select, multi-select, or status option has these fields in a schema response:

| Field         | Type             | Meaning                                                                                      |
| :------------ | :--------------- | :------------------------------------------------------------------------------------------- |
| `id`          | String           | The option’s ID. It stays the same when its name changes in Notion.                          |
| `name`        | String           | The option’s label. Names must be unique without regard to case. Commas are not allowed.     |
| `color`       | String           | `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, or `red`. |
| `description` | String or `null` | The option’s description. This field appears in the schema, not in page values.              |

Page values include `id`, `name`, and `color`. Page writes select an option by `id` or `name`. To change the available options, see [Update data source properties](/reference/update-data-source-properties#select-configuration-updates).

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

## Status

The `status` object contains `options` and `groups` arrays. Each page selects one option. The schema groups options by progress.

Status options use the same [option fields](#select-options). Each group contains `id`, `name`, `color`, and `option_ids`. The `option_ids` array lists that group’s options in order.

Creating `status: {}` adds default options (`Not started`, `In progress`, `Done`) in the `To-do`, `In progress`, and `Complete` groups. Custom request options accept a `group` with one of those group names.

To change options or their group membership, see [Status configuration updates](/reference/update-data-source-properties#status-configuration-updates). Group definitions themselves are managed in Notion.

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

## Title

The Name property uses `title: {}`. Every data source must have exactly one. Its ID is always `title`, even if you rename it.

You cannot remove it, change it to another type, or change another property to `title`. It names each page in the data source. The data source’s own name is its top-level `title` field.

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

## Unique ID

The ID property uses `unique_id`. Its `prefix` is a string or `null`, such as `TASK`. Notion assigns each page a unique number within the data source. You can configure the prefix, but you cannot write a page’s number.

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

## URL

The `url` settings object is empty.

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

## Verification

Notion creates the Verification property for a wiki. Its schema response has an empty `verification` object; the API cannot create this property through a schema write. Verification applies to [wiki pages](/guides/data-apis/working-with-databases#wiki-databases). Its page value includes the state, verification period, and verifier.

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
