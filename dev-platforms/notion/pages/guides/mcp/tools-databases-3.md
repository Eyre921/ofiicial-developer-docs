---
title: "Manage databases and views"
source: https://developers.notion.com/guides/mcp/tools-databases
path: guides/mcp/tools-databases
---

Create project trackers, manage tasks, and organize content calendars with database properties and views.

Create project trackers and content calendars, then find the work that needs attention. Organize entries by owner, status, and date, and choose views that help your team use them.

## Try a prompt

Create a content calendar in Notion for the campaign we discussed. Add draft ideas with owners, publish dates, and statuses, then create a calendar view and a view of content ready for review.

Create a content calendar in Notion for the campaign we discussed. Add draft ideas with owners, publish dates, and statuses, then create a calendar view and a view of content ready for review.

## Available tools

| Action | What it does | Tool name |
| - | - | - |
| Create a tracker | Create a database with properties and an initial view. | [`notion-create-database`](/guides/mcp/tools-databases-reference#create-a-database) |
| Change properties and layouts | Update the fields and page layout of a data source. | [`notion-update-data-source`](/guides/mcp/tools-databases-reference#update-a-data-source) |
| Add a view | Show work in a table, board, calendar, chart, or another view. | [`notion-create-view`](/guides/mcp/tools-databases-reference#create-a-view) |
| Adjust a view | Change how an existing view displays work. | [`notion-update-view`](/guides/mcp/tools-databases-reference#update-a-view) |
| Find database entries | Read a saved view or find entries matching your question. | [`notion-query-data-sources`](/guides/mcp/tools-databases-reference#query-across-data-sources) |
| Compare data sources | Combine results from multiple data sources to compare work or calculate totals. | [`notion-query-multiple-data-sources`](/guides/mcp/tools-databases-reference#query-multiple-data-sources) |
| Move databases to Trash | Remove a database and its entries after confirmation. | [`notion-delete-databases`](/guides/mcp/tools-databases-reference#delete-databases) |

## Things to know

A database can show the same work in several views, such as a table, board, or calendar. Ask your assistant to add a view when you want a different way to see existing work. To add or update individual entries, use the [page tools](/guides/mcp/tools-pages).

## Technical reference

See the [technical reference](/guides/mcp/tools-databases-reference) for parameters, response formats, requirements, and examples for these tools.
