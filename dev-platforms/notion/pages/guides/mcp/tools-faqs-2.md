---
title: "Notion MCP tool FAQs"
source: https://developers.notion.com/guides/mcp/tools-faqs
path: guides/mcp/tools-faqs
---

Browse the complete Notion MCP tool list and find answers about tool access, AI assistant differences, and rate limits.

## Why do tool names and results differ in OpenAI clients?

In OpenAI clients, `notion-search` and `notion-fetch` appear as `search` and `fetch`. ChatGPT also receives a different response shape for content searches and fetched content. See [OpenAI client tool names and results](/guides/mcp/tools-search-reference#how-do-tool-names-and-results-differ-in-openai-clients) for details.

## Why is a tool or option unavailable?

An admin may limit the tools in a workspace-owned connection. Some tools and parameters also depend on the workspace plan or the connection’s capabilities. Use [`notion-get-tool-access`](/guides/mcp/tools-search-reference#check-tool-access) to check access, and read the relevant tool reference for its requirements.

## What should I do if I reach a rate limit?

Ask your AI assistant to reduce parallel operations or try again later. See [Notion MCP rate limits](/guides/mcp/rate-limits) for retry behavior and error fields.

## Where can I find a complete list of Notion MCP tools?

The table below lists the tools documented in these guides, in alphabetical order. Select a tool name for its requirements and usage details. The tools available to you depend on your connection, permissions, and workspace plan.

| Tool | What it does |
| - | - |
| [`notion-ai-search`](/guides/mcp/tools-search-reference#search-notion) | Search Notion and connected sources together using the older search tool. For new clients, use notion-search and notion-connector-search. |
| [`notion-calendar-cancel-events`](/guides/mcp/tools-calendars-reference#cancel-calendar-events) | Cancel a calendar event. |
| [`notion-calendar-create-events`](/guides/mcp/tools-calendars-reference#create-calendar-events) | Create events on calendars you can edit. |
| [`notion-calendar-list-calendar-resources`](/guides/mcp/tools-calendars-reference#find-calendar-resources) | Find rooms and other calendar resources for a chosen time. |
| [`notion-calendar-list-calendars`](/guides/mcp/tools-calendars-reference#list-calendars) | See calendars grouped by connected account. |
| [`notion-calendar-list-contacts`](/guides/mcp/tools-calendars-reference#find-contacts) | Find contacts by name or email. |
| [`notion-calendar-list-coworkers-events`](/guides/mcp/tools-calendars-reference#list-coworkers-events) | Read coworkers’ events within your organization. |
| [`notion-calendar-list-events`](/guides/mcp/tools-calendars-reference#list-calendar-events) | Read events across connected calendars for a chosen period. |
| [`notion-calendar-update-events`](/guides/mcp/tools-calendars-reference#update-calendar-events) | Update an existing event. |
| [`notion-connector-search`](/guides/mcp/tools-search-reference#search-connected-sources) | Find relevant content in connected apps, such as Slack and Google Drive. |
| [`notion-convert-page-to-skill`](/guides/mcp/tools-skills-agents-reference#convert-a-page-to-a-skill) | Turn an existing instructions page into a Notion Skill. |
| [`notion-create-attachment`](/guides/mcp/tools-files-reference#create-an-attachment) | Save text, a file from a public URL, or a completed upload as an attachment. |
| [`notion-create-comment`](/guides/mcp/tools-comments-reference#add-a-comment) | Comment on a page or specific content, or reply to a discussion. |
| [`notion-create-database`](/guides/mcp/tools-databases-reference#create-a-database) | Create a database with properties and an initial view. |
| [`notion-create-file-upload`](/guides/mcp/tools-files-reference#create-a-file-upload-url) | Create an upload URL for a local file to use in Notion. |
| [`notion-create-folder`](/guides/mcp/tools-files-reference#create-a-folder) | Add an empty folder under a page. |
| [`notion-create-pages`](/guides/mcp/tools-pages-reference#create-pages) | Draft documents and apply database templates. |
| [`notion-create-suggested-edit`](/guides/mcp/tools-comments-reference#suggest-edits) | Propose a page edit for review. |
| [`notion-create-view`](/guides/mcp/tools-databases-reference#create-a-view) | Show work in a table, board, calendar, chart, or another view. |
| [`notion-delete-comment`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) | Delete a comment you wrote. |
| [`notion-delete-databases`](/guides/mcp/tools-databases-reference#delete-databases) | Remove a database and its entries after confirmation. |
| [`notion-delete-pages`](/guides/mcp/tools-pages-reference#delete-pages) | Remove pages you no longer need. |
| [`notion-download-attachment`](/guides/mcp/tools-files-reference#download-a-text-attachment) | Read the text of an attachment created through the connection. |
| [`notion-download-skill`](/guides/mcp/tools-skills-agents-reference#download-a-notion-skill) | Export a Skill and its supporting files. |
| [`notion-duplicate-page`](/guides/mcp/tools-pages-reference#duplicate-a-page) | Duplicate an existing page. |
| [`notion-fetch`](/guides/mcp/tools-search-reference#fetch-notion-content) | Open a page, database, or supported connected-source result. |
| [`notion-get-async-task`](/guides/mcp/tools-pages-reference#get-async-task-status) | Check whether a page creation or update has finished. |
| [`notion-get-comments`](/guides/mcp/tools-comments-reference#get-comments) | Read comments, discussions, and pending suggestions on a page. |
| [`notion-get-enabled-skills`](/guides/mcp/tools-skills-agents-reference#manage-enabled-skills) | List the Skills you have enabled. |
| [`notion-get-file-download-urls`](/guides/mcp/tools-files-reference#get-file-download-urls) | Get temporary download links for files on a page. |
| [`notion-get-groups`](/guides/mcp/tools-search-reference#get-groups) | Look up permission groups you can see. |
| [`notion-get-self`](/guides/mcp/tools-search-reference#identify-the-current-connection) | Identify the connected workspace and user. |
| [`notion-get-session-status`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Check the progress of a Custom Agent session. |
| [`notion-get-suggested-edit`](/guides/mcp/tools-comments-reference#suggest-edits) | Read the proposed change before deciding whether to apply it. |
| [`notion-get-teams`](/guides/mcp/tools-search-reference#get-teams) | List the teamspaces in the workspace. |
| [`notion-get-tool-access`](/guides/mcp/tools-search-reference#check-tool-access) | See which tools and options your connection can use. |
| [`notion-get-users`](/guides/mcp/tools-search-reference#get-users) | Find workspace members and guests by name or email. |
| [`notion-get-version-changes`](/guides/mcp/tools-comments-reference#get-version-changes) | See what changed, who changed it, and whether the edits came from a person, AI, or an MCP client. |
| [`notion-list-favorite-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages) | List your favorite pages in sidebar order. |
| [`notion-list-page-backlinks`](/guides/mcp/tools-search-reference#list-page-backlinks) | Find pages that link to or mention a page. |
| [`notion-list-private-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages) | List top-level pages and databases in your Private section. |
| [`notion-list-recent-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages) | List pages and databases you recently viewed. |
| [`notion-list-session-events`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | List activity in a Custom Agent session. |
| [`notion-list-shared-pages`](/guides/mcp/tools-search-reference#list-sidebar-pages) | List pages and databases in your Shared section. |
| [`notion-memory-search`](/guides/mcp/tools-skills-agents-reference#search-personal-memories) | Search preferences and decisions saved by your connected agents. |
| [`notion-move-pages`](/guides/mcp/tools-pages-reference#move-pages) | Put pages in a different location. |
| [`notion-query-data-sources`](/guides/mcp/tools-databases-reference#query-across-data-sources) | Read a saved view or find entries matching your question. |
| [`notion-query-meeting-notes`](/guides/mcp/tools-search-reference#query-meeting-notes) | Find your meeting notes by meeting details, such as a title. |
| [`notion-query-multiple-data-sources`](/guides/mcp/tools-databases-reference#query-multiple-data-sources) | Combine results from multiple data sources to compare work or calculate totals. |
| [`notion-query-sessions`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Browse existing Custom Agent sessions. |
| [`notion-read-session-event`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Read an event from a Custom Agent session. |
| [`notion-resolve-suggested-edit`](/guides/mcp/tools-comments-reference#suggest-edits) | Apply a proposed change or discard it. |
| [`notion-restore-pages`](/guides/mcp/tools-comments-reference#restore-pages) | Recover pages from Trash. |
| [`notion-restore-version`](/guides/mcp/tools-comments-reference#restore-a-past-version) | Put a page or database back to how it looked at a past time. |
| [`notion-search`](/guides/mcp/tools-search-reference#search-notion) | Find pages and databases by topic or title. |
| [`notion-search-agents`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Find an agent shared with you that can take on a task. |
| [`notion-search-sessions`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Search existing Custom Agent sessions. |
| [`notion-send-message-to-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Send a follow-up message to a Custom Agent session. |
| [`notion-set-comment-reaction`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) | Add or remove your emoji reaction. |
| [`notion-set-discussion-resolved`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) | Mark a discussion as resolved or reopen it. |
| [`notion-spawn-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Start a Custom Agent session to carry out a task. |
| [`notion-stop-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Stop a running Custom Agent session. |
| [`notion-update-comment`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) | Edit a comment you wrote. |
| [`notion-update-data-source`](/guides/mcp/tools-databases-reference#update-a-data-source) | Update the fields and page layout of a data source. |
| [`notion-update-enabled-skills`](/guides/mcp/tools-skills-agents-reference#manage-enabled-skills) | Enable or disable Skills for your own use. |
| [`notion-update-folder`](/guides/mcp/tools-files-reference#update-a-folder) | Add or remove files and create subfolders. |
| [`notion-update-page`](/guides/mcp/tools-pages-reference#update-a-page) | Update a page’s content and properties. |
| [`notion-update-view`](/guides/mcp/tools-databases-reference#update-a-view) | Change how an existing view displays work. |
| [`notion-upload-skill`](/guides/mcp/tools-skills-agents-reference#upload-a-notion-skill) | Import a Skill into a page in a Skills database. |
| [`notion-view-version`](/guides/mcp/tools-comments-reference#view-a-past-version) | See a page as it was at a previous point in time. |
| [`notion-wait-session`](/guides/mcp/tools-skills-agents-reference#work-with-custom-agent-sessions) | Wait for a Custom Agent session to respond. |
