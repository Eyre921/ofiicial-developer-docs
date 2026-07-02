---
title: "Preparing your connection for users"
source: https://developers.notion.com/guides/get-started/preparing-for-users
path: guides/get-started/preparing-for-users
---

Learn how to create databases, pages, and views in a user's workspace right after they install your public connection.

Most public connections need specific databases, pages, or views to work. Traditionally, that meant waiting for the user to [share pages](/guides/get-started/authorization) manually or [duplicate a static template](/guides/get-started/authorization#prompt-for-a-connection-with-a-notion-template-option) during OAuth — both add friction and delay how quickly your connection delivers value.

With the Notion API, public connections can skip those steps entirely. Right after a user authorizes your connection, you can create the exact databases, pages, and views your connection needs — no extra user action required.

In this guide, you'll learn how to:

* Create databases and pages directly in a user's workspace
* Configure views with filters, sorts, and layout types
* Populate pages using database templates

## How it works

<Steps>
  <Step title="User authorizes your connection">
    The user goes through the standard [OAuth flow](/guides/get-started/authorization). You receive an `access_token` with the capabilities your connection requested. No template URL is needed.
  </Step>

  <Step title="Create databases and pages">
    Use the API to create [databases](/reference/create-database) and [pages](/reference/post-page) at the workspace level. These appear in the user's **Private** section in Notion.
  </Step>

  <Step title="Configure views">
    Use the [views API](/guides/data-apis/working-with-views) to add views (table, board, calendar, etc.) to your newly created databases, with the filters and sorts your connection needs.
  </Step>

  <Step title="Optionally apply templates">
    If your databases have [data source templates](/guides/data-apis/creating-pages-from-templates), you can create pages that start from those templates for a richer initial experience.
  </Step>
</Steps>

## Creating workspace-level content

Public connections and [personal access tokens](/guides/get-started/personal-access-tokens) can create pages and databases at the **workspace level** by omitting the `parent` parameter (or setting it to `{ "type": "workspace", "workspace": true }`). This places the content in the associated user's Private section.

<Info>
  This capability is only available to **public connections**. Internal connections cannot create workspace-level content because they aren't owned by a single user.
</Info>

### Create a database

<CodeGroup>
  ```bash cURL expandable theme={null}
  curl -X POST https://api.notion.com/v1/databases \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "title": [{ "type": "text", "text": { "content": "Project Tracker" } }],
      "is_inline": false,
      "initial_data_source": {
        "properties": {
          "Task": { "title": {} },
          "Status": {
            "status": {
              "options": [
                { "name": "Not started", "color": "default" },
                { "name": "In progress", "color": "blue" },
                { "name": "Done", "color": "green" }
              ]
            }
          },
          "Assignee": { "people": {} },
          "Due date": { "date": {} }
        }
      }
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  const { Client } = require("@notionhq/client");

  const notion = new Client({ auth: process.env.NOTION_API_KEY });

  const database = await notion.databases.create({
    // Omitting "parent" creates a workspace-level database
    title: [{ type: "text", text: { content: "Project Tracker" } }],
    is_inline: false,
    initial_data_source: {
      properties: {
        Task: { title: {} },
        Status: {
          status: {
            options: [
              { name: "Not started", color: "default" },
              { name: "In progress", color: "blue" },
              { name: "Done", color: "green" },
            ],
          },
        },
        Assignee: { people: {} },
        "Due date": { date: {} },
      },
    },
  });

  const dataSourceId = database.data_sources[0].id;
  ```
</CodeGroup>

The new database is created with one data source and one default Table view. Store the `database.id` and `database.data_sources[0].id` — you'll need them to create views and pages.

### Create a standalone page

<CodeGroup>
  ```bash cURL expandable theme={null}
  curl -X POST https://api.notion.com/v1/pages \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "properties": {
        "title": {
          "title": [{ "type": "text", "text": { "content": "Getting Started" } }]
        }
      },
      "children": [
        {
          "object": "block",
          "type": "heading_2",
          "heading_2": {
            "rich_text": [{ "type": "text", "text": { "content": "Welcome!" } }]
          }
        },
        {
          "object": "block",
          "type": "paragraph",
          "paragraph": {
            "rich_text": [
              { "type": "text", "text": { "content": "This page was created by your connection. You can move it anywhere in your workspace." } }
            ]
          }
        }
      ]
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  const page = await notion.pages.create({
    // Omitting "parent" creates a workspace-level page
    properties: {
      title: {
        title: [{ type: "text", text: { content: "Getting Started" } }],
      },
    },
    children: [
      {
        object: "block",
        type: "heading_2",
        heading_2: {
          rich_text: [{ type: "text", text: { content: "Welcome!" } }],
        },
      },
      {
        object: "block",
        type: "paragraph",
        paragraph: {
          rich_text: [
            {
              type: "text",
              text: {
                content:
                  "This page was created by your connection. You can move it anywhere in your workspace.",
              },
            },
          ],
        },
      },
    ],
  });
  ```
</CodeGroup>

## Adding views

After creating a database, you can add views that match your connection's use cases. Each database starts with a default Table view, but you'll likely want to create additional views with specific filters, sorts, and layout types.

For a project tracker, you might want a Board view grouped by status and a Calendar view for due dates:

<CodeGroup>
  ```bash cURL expandable theme={null}
  # Board view: tasks grouped by status
  curl -X POST https://api.notion.com/v1/views \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "database_id": "DATABASE_ID",
      "data_source_id": "DATA_SOURCE_ID",
      "name": "Task board",
      "type": "board"
    }'

  # Calendar view: tasks by due date
  curl -X POST https://api.notion.com/v1/views \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "database_id": "DATABASE_ID",
      "data_source_id": "DATA_SOURCE_ID",
      "name": "Schedule",
      "type": "calendar"
    }'

  # Filtered table: only active tasks
  curl -X POST https://api.notion.com/v1/views \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "database_id": "DATABASE_ID",
      "data_source_id": "DATA_SOURCE_ID",
      "name": "Active tasks",
      "type": "table",
      "filter": {
        "property": "Status",
        "status": {
          "does_not_equal": "Done"
        }
      },
      "sorts": [
        {
          "property": "Due date",
          "direction": "ascending"
        }
      ]
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  // Board view: tasks grouped by status
  const boardView = await notion.views.create({
    database_id: database.id,
    data_source_id: dataSourceId,
    name: "Task board",
    type: "board",
  });

  // Calendar view: tasks by due date
  const calendarView = await notion.views.create({
    database_id: database.id,
    data_source_id: dataSourceId,
    name: "Schedule",
    type: "calendar",
  });

  // Filtered table: only active tasks
  const activeView = await notion.views.create({
    database_id: database.id,
    data_source_id: dataSourceId,
    name: "Active tasks",
    type: "table",
    filter: {
      property: "Status",
      status: {
        does_not_equal: "Done",
      },
    },
    sorts: [
      {
        property: "Due date",
        direction: "ascending",
      },
    ],
  });
  ```
</CodeGroup>

See the [Working with views](/guides/data-apis/working-with-views) guide for full details on creating, updating, and querying views.

## Applying templates

If your connection pre-configures [database templates](https://www.notion.com/help/database-templates) for the data source, you can create pages that start from those templates. This is useful for providing users with structured starting points — for example, a "Bug report" template with pre-filled sections.

<CodeGroup>
  ```bash cURL expandable theme={null}
  # List available templates for the data source
  curl -X GET "https://api.notion.com/v1/data_sources/DATA_SOURCE_ID/templates" \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Notion-Version: 2026-03-11"

  # Create a page using the default template
  curl -X POST https://api.notion.com/v1/pages \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2026-03-11" \
    --data '{
      "parent": {
        "type": "data_source_id",
        "data_source_id": "DATA_SOURCE_ID"
      },
      "properties": {
        "Task": {
          "title": [{ "type": "text", "text": { "content": "My first task" } }]
        }
      },
      "template": {
        "type": "default"
      }
    }'
  ```

  ```javascript JavaScript expandable theme={null}
  // List available templates for the data source
  const templates = await notion.dataSources.listTemplates({
    data_source_id: dataSourceId,
  });

  // Create a page using the default template
  const page = await notion.pages.create({
    parent: {
      type: "data_source_id",
      data_source_id: dataSourceId,
    },
    properties: {
      Task: {
        title: [{ type: "text", text: { content: "My first task" } }],
      },
    },
    template: {
      type: "default",
    },
  });
  ```
</CodeGroup>

<Tip>
  Template content is applied asynchronously after the page is created. If your connection needs to take action once the template is fully applied, use [webhooks](/reference/webhooks) to listen for `page.content_updated` events. See the [Creating pages from templates](/guides/data-apis/creating-pages-from-templates) guide for the full workflow.
</Tip>

## Programmatic setup vs. template duplication

|                        | Template URL (OAuth)                               | Programmatic setup                                      |
| :--------------------- | :------------------------------------------------- | :------------------------------------------------------ |
| **Customization**      | Static — every user gets the same template         | Dynamic — tailor content to each user                   |
| **Schema control**     | Snapshot; changes require updating the source page | Full control over properties and views at creation time |
| **Multiple databases** | One template page per connection                   | Create as many databases and pages as needed            |
| **View configuration** | Views duplicated as-is                             | Create views with specific filters, sorts, and types    |
| **User interaction**   | User must choose "Duplicate template" during OAuth | No extra steps — setup happens after authorization      |

<Tip>
  Template duplication still works well for simple connections where a single static page is enough. Use programmatic setup when you need multiple resources, per-user customization, or want to keep the workspace in sync with an external system.
</Tip>

**What's next**

Now that you know how to set up workspace content, explore the APIs used in this guide:

* [Working with databases](/guides/data-apis/working-with-databases) — schemas, querying, and page management
* [Working with views](/guides/data-apis/working-with-views) — creating, updating, and querying views
* [Creating pages from templates](/guides/data-apis/creating-pages-from-templates) — using data source templates
* [Authorization](/guides/get-started/authorization) — the OAuth flow for public connections
