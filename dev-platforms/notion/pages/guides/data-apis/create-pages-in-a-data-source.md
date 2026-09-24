---
title: "Create a page in a data source"
source: https://developers.notion.com/guides/data-apis/create-pages-in-a-data-source
path: guides/data-apis/create-pages-in-a-data-source
---

Check a data source schema and create a page with matching property values.

Use this guide to add a page to an existing data source. The example creates a grocery item with a name, price, and order date.

## Get access and the data source ID

Your connection needs [insert content capabilities](/reference/capabilities) and access to the parent database. The schema check also needs read content capabilities. In Notion, open the database’s `•••` menu and add the connection through `Add connections`.

Use [Retrieve a database](/reference/retrieve-database) to list its `data_sources`. Choose the ID of the source you want. You can also copy a data source ID from `Manage data sources` in Notion.

Set `NOTION_API_KEY` and `NOTION_DATA_SOURCE_ID` in your server’s environment. Tokens must not appear in browser page source, client bundles, or public repositories. The JavaScript example uses the [Notion SDK](https://github.com/makenotion/notion-sdk-js) in a Node.js project.

## Check the schema

[Retrieve the data source](/reference/retrieve-a-data-source). Check its `properties` map for these names and types, or adjust the request to match your source:

| Property name | API type | Value in this example |
| :------------ | :------- | :-------------------- |
| Grocery item  | `title`  | Tomatoes              |
| Price         | `number` | `1.49`                |
| Last ordered  | `date`   | `2026-09-01`          |

Use [Update data source properties](/reference/update-data-source-properties) if you need to add or rename a property. Each data source must have one Name property (`title`).

## Create the page

Set `parent.data_source_id` and supply the page values in `properties`. Property names or IDs can be used as keys. The JavaScript example checks the schema before creating the page. Save it as `create-page.mjs` and run `node create-page.mjs`.

<CodeGroup>
  ```bash cURL theme={null}
  curl --fail-with-body https://api.notion.com/v1/pages \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data "{
      \"parent\": { \"data_source_id\": \"$NOTION_DATA_SOURCE_ID\" },
      \"properties\": {
        \"Grocery item\": { \"title\": [{ \"text\": { \"content\": \"Tomatoes\" } }] },
        \"Price\": { \"number\": 1.49 },
        \"Last ordered\": { \"date\": { \"start\": \"2026-09-01\" } }
      }
    }"
  ```

  ```javascript JavaScript theme={null}
  import { Client } from "@notionhq/client";

  async function main() {
    const token = process.env.NOTION_API_KEY;
    const dataSourceId = process.env.NOTION_DATA_SOURCE_ID;
    if (!token || !dataSourceId) {
      throw new Error("Set NOTION_API_KEY and NOTION_DATA_SOURCE_ID.");
    }

    const notion = new Client({ auth: token });
    const dataSource = await notion.dataSources.retrieve({
      data_source_id: dataSourceId,
    });
    if (!("properties" in dataSource)) {
      throw new Error("The data source response has no schema. Check access.");
    }

    const expectedTypes = {
      "Grocery item": "title",
      Price: "number",
      "Last ordered": "date",
    };
    for (const [name, type] of Object.entries(expectedTypes)) {
      if (dataSource.properties[name]?.type !== type) {
        throw new Error(`Expected a ${type} property named ${name}. Check the schema.`);
      }
    }

    const page = await notion.pages.create({
      parent: { data_source_id: dataSourceId },
      properties: {
        "Grocery item": { title: [{ text: { content: "Tomatoes" } }] },
        Price: { number: 1.49 },
        "Last ordered": { date: { start: "2026-09-01" } },
      },
    });
    console.log("Created page:", page.id);
  }

  main().catch((error) => {
    console.error(error instanceof Error ? error.message : "Could not create the page.");
    process.exitCode = 1;
  });
  ```
</CodeGroup>

The response contains the new page’s `id`. Save it if you need to [update its properties](/reference/patch-page) later. Running this example again creates another page.

## Handle failures

For a `400` validation error, check that each name and value matches the current schema. For a `403`, check the connection’s capabilities. For a `404`, check the data source ID and database sharing settings.

If a request times out, check whether the page was created before retrying. Repeating a create request can create a duplicate.
