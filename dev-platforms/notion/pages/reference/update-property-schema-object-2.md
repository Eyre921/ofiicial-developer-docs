---
title: "Update database properties (legacy)"
source: https://developers.notion.com/reference/update-property-schema-object
path: reference/update-property-schema-object
---

Update property schemas with API versions through 2022-06-28.

<Warning>
  This page applies to API versions through `2022-06-28`. For `2025-09-03` and later, use [Update data source properties](/reference/update-data-source-properties). See the [upgrade guide](/guides/get-started/upgrade-guide-2025-09-03) for the database and data source split.
</Warning>

[Retrieve the legacy database](/reference/retrieve-a-database) to get its property IDs. Send the operation’s JSON body to [Update a database](/reference/update-a-database), at `PATCH /v1/databases/{database_id}`. Your connection needs access and [update content capabilities](/reference/capabilities).

The operations below use the same `properties` format as data source updates. For legacy relation settings, use `database_id` instead of `data_source_id` to identify the target.

## Add a property

Add a new key to `properties` and provide the type’s settings. This example adds a number and a date property. Existing properties that you omit stay unchanged.

```json Request body theme={null}
{
  "properties": {
    "Estimate": { "number": { "format": "number" } },
    "Due date": { "date": {} }
  }
}
```

See [Property schemas](/reference/property-object) for every type and its settings.

## Remove a property

Set the property entry to `null`. This removes the column for all pages in the data source. To clear a value on one page instead, use [Update page](/reference/page-property-values#writing-and-clearing-values).

<CodeGroup>
  ```json By ID theme={null}
  {
    "properties": {
      "oldP": null
    }
  }
  ```

  ```json By name theme={null}
  {
    "properties": {
      "Old estimate": null
    }
  }
  ```
</CodeGroup>

## Rename a property

Set `name` on the existing entry. Its ID stays the same. Prefer the ID if another user might rename the property while your connection is running.

<CodeGroup>
  ```json By ID theme={null}
  {
    "properties": {
      "estM": { "name": "Hours" }
    }
  }
  ```

  ```json By name theme={null}
  {
    "properties": {
      "Estimate": { "name": "Hours" }
    }
  }
  ```
</CodeGroup>

To update a property’s `description`, include it beside the type’s settings. Repeat the current description when changing settings if you want to keep it. A rename that sends only `name` preserves the description.

## Update property type

Supply the new type’s settings under the existing name or ID.

```json Change Estimate to a number theme={null}
{
  "properties": {
    "Estimate": { "number": { "format": "number" } }
  }
}
```

<Warning>
  Changing a type can make existing values unreadable in the new type. Check the change on a test data source first. The Name property (`title`) cannot be removed or converted. Other properties cannot become `title`. Place properties cannot be converted to or from another type.
</Warning>

### Select configuration updates

Set `select.options` to the complete list of options you want to keep. Omitted options are removed. New names add options. Omitting `options` keeps the current list.

<Warning>
  When updating `select` or `multi_select` settings, include the current property-level `description` to keep it. Omitting it clears it. This is separate from each option’s description. The examples below assume the property descriptions shown; copy yours from the retrieved schema.
</Warning>

```json Keep High and add Medium theme={null}
{
  "properties": {
    "Priority": {
      "description": "How soon this work needs attention.",
      "select": {
        "options": [
          { "id": "ff8e9269-9579-47f7-8f6e-83a84716863c" },
          { "name": "Medium", "color": "yellow", "description": "Schedule after high-priority work." }
        ]
      }
    }
  }
}
```

#### Existing select options

Use an existing option’s `id` or `name` to retain it. You can update its `description`. The API does not rename existing options or change their colors; make those changes in Notion. New options accept `name`, optional `color`, and optional `description`. See [Option fields](/reference/property-object#select-options).

### Multi-select configuration updates

Set `multi_select.options` using the same rules as select. Include every option to retain. This changes the available tags, not the tags selected on one page.

```json Keep High and add Launch theme={null}
{
  "properties": {
    "Tags": {
      "description": "Labels used to organize work.",
      "multi_select": {
        "options": [
          { "id": "ff8e9269-9579-47f7-8f6e-83a84716863c" },
          { "name": "Launch", "color": "blue" }
        ]
      }
    }
  }
}
```

#### Existing multi-select options

Existing options follow the [same ID, name, color, and description rules](#existing-select-options).

### Status configuration updates

Set `status.options` to the complete list to retain. Use `group` to place an option in `To-do`, `In progress`, or `Complete`.

```json Keep In progress and add Shipped theme={null}
{
  "properties": {
    "Status": {
      "status": {
        "options": [
          { "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3", "group": "In progress" },
          { "name": "Shipped", "color": "green", "group": "Complete" }
        ]
      }
    }
  }
}
```

#### Existing status options

Existing options follow the [same ID, name, color, and description rules](#existing-select-options). When you omit `group`, an existing option keeps its group. A new option uses `To-do` if that group exists, or the first existing group otherwise.

Removed options are also removed from their groups. To rename, reorder, or change the groups themselves, use Notion. To select an option on a page, [write the page’s status value](/reference/page-property-values#status).

## Limitations

Keep schema changes within the [schema size limit](/reference/update-a-data-source#recommended-data-source-schema-size-limit). Changes to synced data sources are restricted. Share related databases with the connection before configuring relations or rollups.

After a change, retrieve the data source again and check the returned names, IDs, and settings. Read a sample page if you changed a property’s type.
