---
title: "Search and read information"
source: https://developers.notion.com/guides/mcp/tools-search
path: guides/mcp/tools-search
---

Find project decisions, summarize meeting notes, and search Notion pages and connected apps.

Find decisions, summarize meeting notes, and gather context for a project. Search your Notion pages and connected sources, read the relevant documents, and find teammates and teamspaces.

## Try a prompt

Search Notion for our latest launch decisions and meeting notes. Summarize what we agreed, what is still unresolved, and link to the sources.

Search Notion for our latest launch decisions and meeting notes. Summarize what we agreed, what is still unresolved, and link to the sources.

## Available tools

| Action | What it does | Tool name |
| - | - | - |
| Find Notion content | Find pages and databases by topic or title. | [`notion-search`](/guides/mcp/tools-search-reference#search-notion) |
| Search connected sources | Find relevant content in connected apps, such as Slack and Google Drive. | [`notion-connector-search`](/guides/mcp/tools-search-reference#search-connected-sources) |
| Read content | Open a page, database, or supported connected-source result. | [`notion-fetch`](/guides/mcp/tools-search-reference#fetch-notion-content) |
| Browse your pages | Find private, shared, favorite, and recently viewed pages. | [`notion-list-private-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages)  [`notion-list-shared-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages)  [`notion-list-favorite-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages)  [`notion-list-recent-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages) |
| Find related pages | Find pages that link to or mention a page. | [`notion-list-page-backlinks`](/guides/mcp/tools-search-reference#list-page-backlinks) |
| Find meeting notes | Find your meeting notes by meeting details, such as a title. | [`notion-query-meeting-notes`](/guides/mcp/tools-search-reference#query-meeting-notes) |
| Check your connection | Identify the connected workspace and user. | [`notion-get-self`](/guides/mcp/tools-search-reference#identify-the-current-connection) |
| Find teamspaces | List the teamspaces in the workspace. | [`notion-get-teams`](/guides/mcp/tools-search-reference#get-teams) |
| Find groups | Look up permission groups you can see. | [`notion-get-groups`](/guides/mcp/tools-search-reference#get-groups) |
| Find teammates | Find workspace members and guests by name or email. | [`notion-get-users`](/guides/mcp/tools-search-reference#get-users) |
| Check tool access | See which tools and options your connection can use. | [`notion-get-tool-access`](/guides/mcp/tools-search-reference#check-tool-access) |

## Things to know

Your assistant can only read content you have access to. Notion search and connected-source search cover different places; ask for both when your question spans Notion and other apps.

## Technical reference

See the [technical reference](/guides/mcp/tools-search-reference) for parameters, response formats, requirements, and examples for these tools.
