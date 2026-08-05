---
title: "API quickstart"
source: https://developers.notion.com/guides/get-started/quick-start
path: guides/get-started/quick-start
---

Create a page in your Notion workspace with a personal access token and a single API request.

You need a Notion account and a terminal.

## Step 1: Get a personal access token

A personal access token (PAT) lets you authenticate API requests as yourself without setting up a connection or completing an OAuth flow.

<Steps>
  <Step>
    Open <a href={personalAccessTokensUrl}>Personal access tokens</a> in the Developer portal.
  </Step>

  <Step>
    Select **New token**.
  </Step>

  <Step>
    Enter a name, select the **Notion API** capability, and then select **Create token**. If a workspace picker appears, select a workspace first.
  </Step>

  <Step>
    Copy the token and save it somewhere secure. You won't be able to see it again.
  </Step>
</Steps>

<Info>
  **Don't see the option to create a token?**

  On Business and Enterprise plans, PAT creation is restricted by default. Ask a workspace owner to enable it in **Settings → Connections**.

  See [Who can create PATs](/guides/get-started/personal-access-tokens#who-can-create-pats).
</Info>

Set the token as an environment variable so you can use it in the examples below. This lasts for your current terminal session — run it again if you open a new window.

<CodeGroup>
  ```bash macOS / Linux theme={null}
  export NOTION_API_KEY=ntn_***
  ```

  ```powershell Windows (PowerShell) theme={null}
  $env:NOTION_API_KEY = "ntn_***"
  ```
</CodeGroup>

## Step 2: Create a page

Make a POST request to the [Create a page](/reference/post-page) endpoint with markdown content. The API creates a private page in your workspace, using the `# heading` as the page title automatically.

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST https://api.notion.com/v1/pages \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11" \
    -H "Content-Type: application/json" \
    -d '{
      "icon": { "emoji": "🚀" },
      "markdown": "# Hello from the API\n\n## Welcome\n\nThis page was created with the Notion API. You just made your first request!\n\n- Read the [API reference](https://developers.notion.com/reference/intro)\n- Explore [examples](https://developers.notion.com/page/examples)"
    }'
  ```

  ```http HTTP theme={null}
  POST https://api.notion.com/v1/pages
  Authorization: Bearer {PERSONAL_ACCESS_TOKEN}
  Content-Type: application/json
  Notion-Version: 2026-03-11

  {
    "icon": { "emoji": "🚀" },
    "markdown": "# Hello from the API\n\n## Welcome\n\nThis page was created with the Notion API. You just made your first request!\n\n- Read the [API reference](https://developers.notion.com/reference/intro)\n- Explore [examples](https://developers.notion.com/page/examples)"
  }
  ```

  ```javascript JavaScript theme={null}
  // Save as quickstart.mjs after running: npm install @notionhq/client
  import { Client } from "@notionhq/client";

  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  async function main() {
    const page = await notion.pages.create({
      icon: { emoji: "🚀" },
      markdown: [
        "# Hello from the API",
        "",
        "## Welcome",
        "",
        "This page was created with the Notion API. You just made your first request!",
        "",
        "- Read the [API reference](https://developers.notion.com/reference/intro)",
        "- Explore [examples](https://developers.notion.com/page/examples)",
      ].join("\n"),
    });

    console.log("Created page:", page.url);
  }

  main();
  ```
</CodeGroup>

The `markdown` field accepts [Notion-flavored Markdown](/guides/data-apis/enhanced-markdown) — headings, lists, code blocks, links, and more. The API converts it to Notion blocks for you.

<Accordion title="Under the hood: markdown → blocks">
  Notion pages are made up of **blocks** — headings, paragraphs, lists, and more. When you send `markdown`, the API converts it into this block structure automatically.

  You can also build this structure directly using the `children` field. Here's what the same page looks like expressed as blocks:

  ```json theme={null}
  {
    "icon": { "emoji": "🚀" },
    "properties": {
      "title": [{ "text": { "content": "Hello from the API" } }]
    },
    "children": [
      {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
          "rich_text": [{ "text": { "content": "Welcome" } }]
        }
      },
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "rich_text": [
            {
              "text": {
                "content": "This page was created with the Notion API. You just made your first request!"
              }
            }
          ]
        }
      }
    ]
  }
  ```

  The block model gives you precise control over every element — formatting, colors, toggles, and block types that markdown can't express. Use `markdown` when you want simplicity, and `children` when you need that control.

  See [Working with page content](/guides/data-apis/working-with-page-content) to learn more about the block model.
</Accordion>

## Check the result

A successful response returns a page object:

```json Response theme={null}
{
  "object": "page",
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "created_time": "2025-01-15T09:30:00.000Z",
  "last_edited_time": "2025-01-15T09:30:00.000Z",
  "icon": {
    "type": "emoji",
    "emoji": "🚀"
  },
  "parent": {
    "type": "workspace",
    "workspace": true
  },
  "properties": {
    "title": {
      "id": "title",
      "type": "title",
      "title": [{ "plain_text": "Hello from the API" }]
    }
  },
  "url": "https://www.notion.com/Hello-from-the-API-a1b2c3d4e5f67890abcdef1234567890",
  "public_url": null
}
```

To see your new page:

* **From the response:** Copy the `url` value and open it in your browser.
* **From Notion:** Look in **Private** in your sidebar for 🚀 **Hello from the API**.

Open the page and you should see your heading, paragraph, and bullet list inside.

<Accordion title="Getting an error?">
  Error responses return a JSON object with a `code` and `message`:

  ```json theme={null}
  {
    "object": "error",
    "status": 401,
    "code": "unauthorized",
    "message": "API token is invalid."
  }
  ```

  | Error              | Fix                                                                                 |
  | :----------------- | :---------------------------------------------------------------------------------- |
  | `unauthorized`     | Double-check that your token is correct and hasn't expired.                         |
  | `validation_error` | Check the request body against the [Create a page](/reference/post-page) reference. |

  For the full list of error codes, see [Status codes](/reference/status-codes).
</Accordion>

## Next steps

Now that you've made your first request, explore what else you can build — create databases, query content, manage comments, upload files, and more.

<CardGroup>
  <Card title="API reference" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/curlyBraces.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=46f7a8b4a34544f9b03002e4ecc35ad5" href="/reference/intro">
    Browse every endpoint, request parameter, and response field.
  </Card>

  <Card title="JavaScript SDK" icon="js" href="https://github.com/makenotion/notion-sdk-js">
    Official client library for Node.js.
  </Card>
</CardGroup>
