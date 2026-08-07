---
title: "Supported tools"
source: https://developers.notion.com/guides/mcp/mcp-supported-tools
path: guides/mcp/mcp-supported-tools
---

Learn what you can do with Notion MCP tools.

Notion MCP provides tools for searching, reading, and changing content in your Notion workspace.

An MCP client can call several tools in one task. For example, it can search for pages, create a page from the results, and then update page properties.

## MCP tools

<AccordionGroup>
  <Accordion title="Search Notion and connected sources">
    `notion-search`

    Search across your Notion workspace and connected tools like Slack, Google Drive, and Jira.

    <Note>
      Requires Notion AI access. Without a Notion AI plan, search is limited to your Notion workspace only.
    </Note>

    **Example prompts:**

    * "Check Slack for how we solved this bug in the past"
    * "Search for documents mentioning 'budget approval process'"
    * "Look for meeting notes from last week with John"
    * "Find all project pages that mention 'ready for dev'"
  </Accordion>

  <Accordion title="Fetch Notion content">
    `notion-fetch`

    Retrieves content from a Notion page, database, or data source by its URL or ID. You can pass a data source ID (from `collection://...` tags in database responses) to fetch details about that specific data source, including its schema and properties. When fetching a database, the response includes available templates for each data source, which can be used with the create-pages and update-page tools.

    Pass the special id `self` to retrieve the connected workspace and user identity instead of an entity. The response includes a `self` object with the workspace's ID and name, and the authenticated user's ID, name, type, and email — useful for labeling a connection after OAuth.

    The `self` object also includes `current_tool_access`, a map of tool names to their access state on this workspace's plan: `available`, `available_with_limit` (calls can be made up to the limit included with the workspace's plan), `upgrade_required` (calls return an upgrade prompt, and the map entry carries an `upgrade_url`), or `not_enabled`. Tools are listed on every plan, so consult this map to route away from tools that would only return an upgrade prompt. Keys are the tools' base names; when tools appear with a `notion-` prefix and hyphens (e.g. `notion-query-data-sources`), they correspond to the map key with the prefix dropped and hyphens as underscores (`query_data_sources`).

    **Example prompts:**

    * "What product requirements still need to be implemented from this ticket `https://notion.com/page-url`?"
    * "Fetch the data source `collection://f336d0bc-b841-465b-8045-024475c079dd` to see its schema"
    * "Fetch the bug tracking database so I can see the available templates"
    * "Fetch `self` to see which workspace and user this connection is for"
  </Accordion>

  <Accordion title="Create a file upload URL">
    `notion-create-file-upload`

    Creates a short-lived URL for uploading one local file directly to Notion. After calling the tool, the MCP client sends the file as a `multipart/form-data` POST request using the returned URL, headers, and form field. The upload response includes `suggested_markdown`, which can be passed directly to `notion-create-pages` or `notion-update-page`, or included on a separate line in `notion-create-comment` markdown to attach the file.

    Files are limited to 20 MiB for this single-part upload flow, and workspace file-size limits still apply. For larger files, use the [file upload API](/guides/data-apis/working-with-files-and-media).

    **Example prompts:**

    * "Upload `diagram.png` and add it to the project plan"
    * "Attach `report.pdf` to a new page"
    * "Upload this file and include it in my comment"
  </Accordion>

  <Accordion title="Create an attachment">
    `notion-create-attachment`

    Creates a Notion attachment from exactly one source: inline UTF-8 text, a file at a direct public HTTPS URL, or a completed file upload created by the same integration. The result includes `suggested_markdown`, which can be passed directly to `notion-create-pages` or `notion-update-page`, or included on a separate line in `notion-create-comment` markdown to attach the file.

    Inline content supports text formats such as HTML, Markdown, CSV, JSON, and SVG, up to 200 KiB. URL downloads support binary files, must complete within one minute, and are limited to 5 MiB on free workspaces or 50 MiB on paid workspaces. URLs must not redirect, require request headers or cookies, or resolve to a private network address. For local files, use `notion-create-file-upload` when available. For files that exceed these limits or downloads that require redirects or authentication, use the [file upload API](/guides/data-apis/working-with-files-and-media) and pass the resulting upload ID as `source_file_id`.

    **Example prompts:**

    * "Create an HTML attachment from this report and add it to the project page"
    * "Attach the PDF at this direct download URL to my meeting notes"
    * "Add the file I just uploaded to a comment"
  </Accordion>

  <Accordion title="Download a text attachment">
    `notion-download-attachment`

    Downloads the complete UTF-8 text content of an attachment created by `notion-create-attachment`. Pass the `file_upload_id` returned when the attachment was created. The attachment must belong to the same integration, have completed uploading, and use a supported text format such as HTML, Markdown, plain text, CSV, JSON, XML, CSS, YAML, TSV, calendar, GPX, or SVG.

    Downloads are limited to 200 KiB. This tool does not fetch arbitrary URLs or return binary files. For larger or binary attachments, use the signed file URL returned when reading the page that contains the attachment.

    **Example prompts:**

    * "Download the HTML attachment I just created so I can edit it"
    * "Read the contents of this Markdown attachment"
    * "Retrieve the text attachment with this file upload ID"
  </Accordion>

  <Accordion title="Create pages">
    `notion-create-pages`

    Creates one or more Notion pages with specified properties and content. Supports applying [database templates](/guides/data-apis/creating-pages-from-templates) to pre-populate new pages with content and property values. Each page can optionally have an icon (emoji, custom emoji by name, or external URL) and a cover image. If a parent is not specified, a private page will be created.

    **Example prompts:**

    * "Create a project kickoff page under our Projects folder with agenda and team info"
    * "Make a new employee onboarding checklist in our HR database"
    * "Create a new bug report in the tracking database using the 'Urgent Bug' template"
    * "Add a new product feature request to our feature database"
    * "Create a page with the 🚀 icon and a cover image"
  </Accordion>

  <Accordion title="Update a page">
    `notion-update-page`

    Update a Notion page's properties, content, icon, or cover. Supports applying [database templates](/guides/data-apis/creating-pages-from-templates) to existing pages. Icon and cover can be set alongside any update command.

    **Example prompts:**

    * "Change the status of this task from 'In Progress' to 'Complete'"
    * "Add a new section about risks to the project plan page"
    * "Apply the project kickoff template to this page"
    * "Set the page icon to 🎯 and add a cover image"
    * "Remove the icon from this page"
  </Accordion>

  <Accordion title="Convert a page to a skill">
    `notion-convert-page-to-skill`

    Marks a Notion page as an AI skill. Pass the page's full Notion URL. The page must be in the connected workspace, and you must have permission to edit it.

    **Example prompts:**

    * "Convert this page into a skill: `https://www.notion.so/example-page-url`"
    * "Make our engineering guidelines page available as an AI skill"
  </Accordion>

  <Accordion title="Move pages">
    `notion-move-pages`

    Move one or more Notion pages or databases to a new parent.

    **Example prompts:**

    * "Move my weekly meeting notes page to the 'Team Meetings' page"
    * "Reorganize all project documents under the 'Active Projects' section"
  </Accordion>

  <Accordion title="Duplicate a page">
    `notion-duplicate-page`

    Duplicate a Notion page within your workspace. This action completes asynchronously.

    **Example prompts:**

    * "Duplicate my project template page so I can use it for the new Q3 initiative"
    * "Make a copy of the meeting agenda template for next week's planning session"
  </Accordion>

  <Accordion title="Create a database">
    `notion-create-database`

    Creates a new Notion database, initial data source, and initial view with the specified properties.

    **Example prompts:**

    * "Create a new database to track our customer feedback with fields for customer name, feedback type, priority, and status"
    * "Set up a content calendar database with columns for publish date, content type, and approval status"
  </Accordion>

  <Accordion title="Create a folder">
    `notion-create-folder`

    Create an empty Folder under a parent page.

    **Example prompts:**

    * "Create a folder named 'Project files' under this page"
    * "Create a folder named 'Supporting documents' under this project page"
  </Accordion>

  <Accordion title="Update a data source">
    `notion-update-data-source`

    Update a Notion data source's properties, name, description, or other attributes.

    **Example prompts:**

    * "Add a status field to track project completion"
    * "Update the task database to include priority levels"
  </Accordion>

  <Accordion title="Create a view">
    `notion-create-view`

    Create a new view on a Notion database. Supports table, board, list, calendar, timeline, gallery, form, chart, map, and dashboard view types. Use the optional configuration DSL for filters, sorts, grouping, and display options.

    **Example prompts:**

    * "Create a board view grouped by Status in my tasks database"
    * "Add a calendar view to the project tracker that shows items by due date"
    * "Set up a filtered table view that only shows in-progress items, sorted by priority"
    * "Create a timeline view for the roadmap database using start and end dates"
    * "Create a chart view showing task counts by status as a bar chart"
    * "Add a form view to the feedback database for collecting responses"
    * "Create a map view of office locations using the Address property"
  </Accordion>

  <Accordion title="Update a view">
    `notion-update-view`

    Update a view's name, filters, sorts, or display configuration. Only the fields you specify will be changed. Supports clearing existing configuration like filters, sorts, and grouping.

    **Example prompts:**

    * "Rename the 'All Tasks' view to 'Sprint Board'"
    * "Update the board view to filter by status equals 'Done'"
    * "Clear the filters on this view and add a sort by created date"
    * "Change the view to group by priority and only show Name and Status columns"
  </Accordion>

  <Accordion title="Query across data sources">
    `notion-query-data-sources`

    Query Notion data sources with SQL, or run an existing view, with structured summaries, grouping, and filters. Returns organized results with counts and rollups for quick scanning.

    <Note>
      Single-data-source SQL queries have a usage limit on select plans. Queries across multiple data sources require the latest Enterprise plan.
    </Note>

    **Example prompts:**

    * "What's due for me this week across all tasks and meeting note action items? Group by priority."
    * "Show all risks from Engineering and Product databases this month, grouped by owner."
  </Accordion>

  <Accordion title="Query a database view">
    `notion-query-database-view`

    Query data from a Notion database using a pre-defined [view's filters and sorts](https://www.notion.com/help/views-filters-and-sorts).

    **Example prompts:**

    * "Query my 'In Progress' tasks view to see what I'm currently working on"
    * "Get all items from the 'High Priority' view in our feature requests database"
    * "Export the filtered data from the 'Q1 Goals' view for analysis"
  </Accordion>

  <Accordion title="Query meeting notes">
    `notion-query-meeting-notes`

    Query the current user's meeting notes, filtering by meeting-specific properties (such as a title keyword search). Returns meetings where the user is an attendee or creator by default.

    <Note>
      Available on all plans, but using it requires a Business plan or higher with Notion AI. On other plans the tool returns an upgrade prompt.
    </Note>

    **Example prompts:**

    * "Find my meeting notes from this week"
    * "What were the action items from my sprint planning meetings?"
    * "Show my 1:1 meeting notes with Alice"
  </Accordion>

  <Accordion title="Add a comment">
    `notion-create-comment`

    Add a comment to a page or specific content. Supports page-level comments,
    block-level comments (via content selection), and replies to existing discussions.

    **Example prompts:**

    * "Add a feedback comment to this design proposal"
    * "Comment on the 'Budget' section of the quarterly review"
    * "Reply to the discussion about deadline concerns"
    * "Leave a note on the meeting notes about the action items"
  </Accordion>

  <Accordion title="Get comments">
    `notion-get-comments`

    Lists all comments and discussions on a page. Can include block-level and
    inline discussions, resolved threads, and full comment content.

    **Example prompts:**

    * "Get all discussions on this page, including resolved ones"
    * "Show me the comments on the Requirements section"
    * "Get all feedback comments from last week's review"
  </Accordion>

  <Accordion title="Get teams">
    `notion-get-teams`

    Retrieves a list of teams (teamspaces) in the current workspace.

    **Example prompts:**

    * "Search for teams by name, and your membership status in each team"
    * "Get a team's ID to use as a filter for a search"
  </Accordion>

  <Accordion title="Get users">
    `notion-get-users`

    Lists workspace members and guests with their IDs, names, emails (when available), and types (person or bot). Supports pagination and search by name or email. You can also retrieve a specific user by ID, or the current user (or bot) by passing `self`.

    **Example prompts:**

    * "Get contact details for the user who created this page"
    * "Look up the profile of the person assigned to this task"
    * "Find users whose name or email matches 'john'"
    * "What's my Notion user ID and email?"
  </Accordion>

  <Accordion title="Get async task status">
    `notion-get-async-task`

    Retrieves the current status of an async task started by another tool (such as `notion-duplicate-page`, or `notion-create-pages` when invoked with `allow_async: true`). Returns one of `queued`, `running`, `retrying`, `succeeded`, or `failed`. When a task has succeeded, the operation's result is included in the response; when it has failed, an error is included instead.

    Poll this tool with the `task_id` from the originating tool's `async_task` response. Wait briefly between polls — the original response includes a suggested backoff.

    **Example prompts:**

    * "Check whether the page I just duplicated is ready"
    * "Poll this async task until it completes and show me the result"
  </Accordion>
</AccordionGroup>

## Async page create and update

The `notion-create-pages` and `notion-update-page` tools support `allow_async: true` for long-running page create and update work. When `allow_async` is omitted or `false`, the tools keep their normal synchronous result shape. `allow_async` changes response behavior only; the same validation, permissions, and write operation still apply.

Use async mode when asking an assistant to create or update a page with a large amount of markdown content. The initial tool call returns an `async_task` handle, and the assistant can poll `notion-get-async-task` with the returned `async_task.id` passed as `task_id` until the task reaches `succeeded` or `failed`.

```json theme={null}
{
  "tool": "notion-create-pages",
  "arguments": {
    "allow_async": true,
    "parent": { "page_id": "YOUR_PAGE_ID" },
    "pages": [
      {
        "properties": { "title": "Migration plan" },
        "content": "# Migration plan\n\nLarge markdown content..."
      }
    ]
  }
}
```

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "queued",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "poll_after_seconds": 2,
  "operation": {
    "surface": "mcp",
    "name": "create_pages"
  }
}
```

```json theme={null}
{
  "tool": "notion-update-page",
  "arguments": {
    "allow_async": true,
    "page_id": "YOUR_PAGE_ID",
    "command": "replace_content",
    "new_str": "# Updated plan\n\nLarge replacement markdown..."
  }
}
```

```json theme={null}
{
  "tool": "notion-get-async-task",
  "arguments": {
    "task_id": "task_abc123"
  }
}
```

If the task is still `queued`, `running`, or `retrying`, wait at least the suggested `poll_after_seconds` before polling again. A `succeeded` task includes the operation result. A `failed` task includes an error object that the assistant can summarize or use to retry with a corrected request.

<Info>
  **Tool names may vary for OpenAI**

  When connecting with an OpenAI MCP client (e.g. ChatGPT), the `notion-` prefix is automatically omitted from the `notion-fetch` and `notion-search` tools, making them appear as `fetch` and `search`, respectively. This is because these specific tool names are required as part of the [Deep Research specification](https://platform.openai.com/docs/guides/deep-research#remote-mcp-servers) for remote MCP servers.
</Info>

## Rate limits

Standard [API request limits](/reference/request-limits) apply per user's usage of Notion MCP (totaled across all tool calls). Currently, this is an average of **180 requests per minute** (3 requests per second). A separate limit applies per workspace, shared across all of its connections and scaled to the workspace's plan. Because it's shared, you can be rate limited even when you're under the per-user limit above.

Some MCP tools have additional, tool-specific rate limits that are stricter. These are subject to change over time, but the current values are listed below for reference:

* **Search**: 30 requests per minute

### Examples

To illustrate the above limitations, you'll experience rate limit errors in your MCP client of choice in any of the following example scenarios (assuming we take the average rate over a large enough time window):

* 35 searches per minute (exceeds search-specific limit)
* 12 searches & 170 fetches per minute (exceeds general 180 requests/min limit)
* 185 fetches per minute (exceeds general 180 requests/min limit)

### What to do if you're rate-limited

In most cases, the time it takes to do a complex AI-powered search across Notion and your connected tools means that sequential searches will typically stay under the rate limit. In general, if you encounter rate limit errors, prompt your LLM tool to reduce the amount of parallel searches or operations performed using Notion MCP, and/or try again later.
