---
title: "Read every item in a page property"
source: https://developers.notion.com/guides/data-apis/read-page-property-values
path: guides/data-apis/read-page-property-values
---

Read a page property with the JavaScript SDK and follow pagination through the final result.

Use the property-item endpoint to read all the values in a property that refers to many pages or people. This guide also handles single values, such as Status, and waits for a rollup’s final result.

## Get the page and property IDs

Your connection needs [read content capabilities](/reference/capabilities) and access to the page. For relations, formulas, and rollups, share the related databases too.

[Retrieve the page](/reference/retrieve-a-page). Find the property by name in its `properties` object, then copy its `id`. Pass that ID as returned, including any URL encoding.

## Set up the request

Use the [JavaScript SDK](https://github.com/makenotion/notion-sdk-js) in a server-side Node.js project. Set `NOTION_API_KEY`, `NOTION_PAGE_ID`, and `NOTION_PROPERTY_ID` in your environment. Tokens must not appear in browser page source, client bundles, or public repositories.

The cURL example reads one response. The JavaScript example reads every response and prints the items. Save it as `read-property.mjs` and run `node read-property.mjs`.

<CodeGroup>
  ```bash cURL theme={null}
  curl --fail-with-body \
    "https://api.notion.com/v1/pages/$NOTION_PAGE_ID/properties/$NOTION_PROPERTY_ID?page_size=100" \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  import { Client } from "@notionhq/client";

  async function main() {
    const token = process.env.NOTION_API_KEY;
    const pageId = process.env.NOTION_PAGE_ID;
    const propertyId = process.env.NOTION_PROPERTY_ID;
    if (!token || !pageId || !propertyId) {
      throw new Error("Set NOTION_API_KEY, NOTION_PAGE_ID, and NOTION_PROPERTY_ID.");
    }

    const notion = new Client({ auth: token });
    let response = await notion.pages.properties.retrieve({
      page_id: pageId,
      property_id: propertyId,
      page_size: 100,
    });

    if (response.object === "property_item") {
      if (response.type === "formula" && response.formula.type === "unsupported") {
        throw new Error("This formula cannot be calculated by the API.");
      }
      console.log(JSON.stringify(response, null, 2));
      return;
    }

    while (true) {
      for (const item of response.results) {
        console.log(JSON.stringify(item, null, 2));
      }

      if (!response.has_more) {
        if (response.property_item.type === "rollup") {
          const rollup = response.property_item.rollup;
          if (rollup.type === "unsupported" || rollup.type === "incomplete") {
            throw new Error("This rollup has no completed calculation. See the rollup limits.");
          }
          console.log("Final rollup:", JSON.stringify(rollup, null, 2));
        }
        return;
      }

      if (!response.next_cursor) {
        throw new Error("The response has more items but no next cursor.");
      }
      response = await notion.pages.properties.retrieve({
        page_id: pageId,
        property_id: propertyId,
        page_size: 100,
        start_cursor: response.next_cursor,
      });
      if (response.object !== "list") {
        throw new Error("The property response changed while reading it. Start again.");
      }
    }
  }

  main().catch((error) => {
    console.error(error instanceof Error ? error.message : "Could not read the property.");
    process.exitCode = 1;
  });
  ```
</CodeGroup>

## Use the result

For a single property item, read the field named by `type`. For example, a Status value is in `status`, and it can be `null`.

For a list, process every item in `results`. A title or text item contains one rich text object. A people item contains one user. A relation item contains one page reference.

For a calculated rollup, use `property_item.rollup` from the final response. For `show_original`, use the printed items; the final metadata has an empty `array`. See [Rollup response rules](/reference/property-item-object#rollup).

## Handle failures

A `403` means the connection lacks a required capability. A `404` can mean the page or property is missing, or that your connection lacks access. Check the IDs and sharing settings.

The SDK retries rate-limit errors by default. If retries fail, the script exits with an error. For `unsupported` formula or rollup results, review the [calculation limits](/reference/property-item-object#unsupported-rollup). Repeating the same request does not remove those limits.
