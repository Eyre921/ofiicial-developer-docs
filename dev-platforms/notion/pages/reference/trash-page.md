---
title: "Trash a page"
source: https://developers.notion.com/reference/trash-page
path: reference/trash-page
---

> [!NOTE]
>
> The API does not support permanently deleting pages.

To trash a page via the API, send an [Update page](/reference/patch-page) request with the `in_trash` body param set to `true`. To restore a page from the trash, set `in_trash` to `false`.

> [!WARNING]
>
> **`archived` was removed in `2026-03-11`**
>
> In API versions before `2026-03-11`, `archived` was a deprecated alias for `in_trash`. Starting with `2026-03-11`, only `in_trash` is accepted. If your connection uses an older API version and still sends `archived`, update to `in_trash` before upgrading.

## Set your token and page ID

Set your integration token and the ID of the page once in your shell. The cURL and JavaScript examples below read both values from the environment. Never put your token in browser page source, client bundles, or public repositories.

```bash Shell theme={null}
export NOTION_API_KEY="ntn_..." NOTION_PAGE_ID="be633bf1-dfa0-436d-b259-571129a590e5"
```

## Example request: trash a Notion page

```bash cURL theme={null}
curl "https://api.notion.com/v1/pages/$NOTION_PAGE_ID" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2026-03-11" \
  -X PATCH \
  --data '{"in_trash": true}'
```

If you are using Notion’s [JavaScript SDK](https://github.com/makenotion/notion-sdk-js) to interact with the REST API, use the `update` method available for Notion pages.

```javascript JavaScript theme={null}
const { Client } = require("@notionhq/client")

// Initializing a client
const notion = new Client({
	auth: process.env.NOTION_API_KEY,
	notionVersion: "2026-03-11",
})

const trashPage = async () => {
	await notion.pages.update({
	  page_id: process.env.NOTION_PAGE_ID,
	  in_trash: true,
	});
}

trashPage()
```

If successful, the API responds with a `200` HTTP status code and the trashed [page object](/reference/page). This excerpt shows the fields that confirm the change:

```json Response excerpt theme={null}
{
  "object": "page",
  "id": "be633bf1-dfa0-436d-b259-571129a590e5",
  "in_trash": true
}
```

Refer to the [error codes](/reference/status-codes#error-codes) documentation for possible errors.

## Example request: restore a Notion page

The API can't restore a top-level page that isn't in a teamspace. It returns a `400` `validation_error` instead, so restore that page in the Notion app. Top-level teamspace pages also show a `workspace` parent, but the API can restore them.

```bash cURL theme={null}
curl "https://api.notion.com/v1/pages/$NOTION_PAGE_ID" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2026-03-11" \
  -X PATCH \
  --data '{"in_trash": false}'
```

```javascript JavaScript theme={null}
// Restore a trashed page using the Notion JavaScript SDK
const { Client } = require("@notionhq/client")

const notion = new Client({
	auth: process.env.NOTION_API_KEY,
	notionVersion: "2026-03-11",
})

const restorePage = async () => {
	await notion.pages.update({
	  page_id: process.env.NOTION_PAGE_ID,
	  in_trash: false,
	});
}

restorePage()
```

If successful, the API responds with a `200` HTTP status code and the restored [page object](/reference/page). Refer to the [error codes](/reference/status-codes#error-codes) documentation for possible errors.
