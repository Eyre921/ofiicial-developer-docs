---
title: "Sort data source entries"
source: https://developers.notion.com/reference/sort-data-source-entries
path: reference/sort-data-source-entries
---

A sort is a condition used to order the entries returned from a data source query.

Pass a `sorts` array to [Query a data source](/reference/query-a-data-source). The first sort takes priority. This example sorts by **Food group** in descending order, then by **Name** in ascending order within each group.

```json Request body theme={null}
{
  "sorts": [
    { "property": "Food group", "direction": "descending" },
    { "property": "Name", "direction": "ascending" }
  ]
}
```

```javascript JavaScript theme={null}
import { Client } from "@notionhq/client";

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const response = await notion.dataSources.query({
  data_source_id: process.env.NOTION_DATA_SOURCE_ID,
  sorts: [
    { property: "Food group", direction: "descending" },
    { property: "Name", direction: "ascending" },
  ],
});
console.log(response.results);
```

## Sort object

### Property value sort

This sort orders the data source query by a particular property.

The sort object must contain the following properties:

| Property | Type | Description | Example value |
| :- | :- | :- | :- |
| `property` | `string` | The name of the property to sort against. | `"Ingredients"` |
| `direction` | `string` (enum) | The direction to sort. Possible values include `"ascending"` and `"descending"`. | `"descending"` |

### Entry timestamp sort

This sort orders the data source query by the timestamp associated with a data source entry.

The sort object must contain the following properties:

| Property | Type | Description | Example value |
| :- | :- | :- | :- |
| `timestamp` | `string` (enum) | The name of the timestamp to sort against. Possible values include `"created_time"` and `"last_edited_time"`. | `"last_edited_time"` |
| `direction` | `string` (enum) | The direction to sort. Possible values include `"ascending"` and `"descending"`. | `"descending"` |
