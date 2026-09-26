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
  <Accordion title="Search Notion">
    `notion-search`

    Before a content search, call `notion-get-tool-access` with `{}` and reuse the returned `current_tool_access` map. Follow the routing guidance in "Check tool access" below, and select only tools exposed by the connection. User lookup has additional permission requirements described under "AI search".

    `notion-search` supports short, specific keywords, location (page, data source, or teamspace), creator or editor, date, title, content-status filters, sorting, and up to 50 results.

    When the connection can use AI search, a keyword content search sent to `notion-search` runs AI search instead. It returns the same unified Notion and connected-source results as `notion-ai-search` and reports `type: "ai_search"`. A call that passes an exact filter, an empty query, or a sort other than `relevance` stays on Notion workspace search and reports `type: "workspace_search"`. Routing follows the access that `notion-get-tool-access` reports for the connection, so a connection whose tool list leaves out `notion-ai-search` keeps its content searches on Notion workspace search. A user lookup with `query_type: "user"` always runs the user search.

    Workspace search results may include `path` and `verification` details. Fetch important matches before relying on them. Unified results from AI search omit `verification`, so fetch a Notion result with `notion-fetch` when verification state matters.

    A filter or sort that the workspace's plan doesn't include doesn't fail the call. Notion drops the unavailable options, runs the rest of the search, and adds a `notices` array to the response. A notice names the dropped fields, such as `filters.title_only`, and may include an upgrade link. Results can be broader than requested and use relevance sorting. On a plan without multiple-teamspace search, when `teamspace_id` and `filters.teamspace_ids` select different teamspaces, both are dropped. If dropping the options leaves an empty query with no supported constraint, the response returns no results and a notice asking for a non-empty query or a supported filter.

    <Note>
      Full Notion MCP on Business or Enterprise is required to filter by editor, last-edited date, multiple teamspaces, title only, or content status, and to sort by date. Other filters are available on every plan. On a plan without them, `restricted_parameters` lists each option with the reason it's unavailable. Read the entry for the search tool you're calling, and check each restriction's reason against the values you plan to send.
    </Note>

    **Example prompts:**

    * "Search for documents mentioning 'budget approval process'"
    * "Look for meeting notes from last week with John"
    * "Find all project pages that mention 'ready for dev'"
  </Accordion>

  <Accordion title="AI search">
    `notion-ai-search`

    Use the "Check tool access" guidance below to select an exposed search tool. Search Notion and sources connected to your workspace, such as Slack, Mail, Calendar, Google Drive, and Jira, with keywords, a page title, or a concise natural-language question. It searches a source only when it is connected and available to you. Keep the query under about 50 words, and use one query per call. Narrow results to a page and its descendants, a data source, or a teamspace, and return up to 50 results.

    This tool also accepts the exact filters, sorting, and filter-only browsing supported by `notion-search`. These options return Notion-only results to enforce the constraints exactly; omit them to search Notion and connected sources together. Access to advanced filters and sorting is separate from AI access, so check `current_tool_access.ai_search.restricted_parameters` before sending them. A restricted option is dropped with a notice, the same as on `notion-search`.

    This tool also handles a user lookup. Set `query_type: "user"` and pass a name or email, and omit content filters and sorting, which return a `validation_error` for a user lookup. The response reports `type: "user_search"` and lists the matching users. A user lookup doesn't need AI access. Both search tools require user information [capabilities](/reference/capabilities); workspace-owned MCP connections must also expose `notion-get-users`. AI-search availability alone doesn't grant user lookup, and switching to `notion-search` doesn't bypass these requirements. Omit `query_type`, or set it to `internal`, for a content search.

    Results use the same shape as `notion-search` and may include `path`. Unified results omit `verification` details, so fetch a Notion result with `notion-fetch` when verification state matters. Connected-app results cannot be fetched with `notion-fetch`. The response reports `type: "ai_search"` for every `notion-ai-search` content-search call, including the Notion-only results returned for exact filters, non-relevance sorting, and filter-only browsing.

    When the workspace's plan doesn't include AI search, a content search sent to this exposed tool runs a keyword search in Notion only instead of returning an upgrade error. The response still reports `type: "ai_search"` and adds a `notices` entry saying that connected sources weren't searched, with an upgrade link when available.

    <Note>
      Listed on all plans. Searching connected sources requires Notion AI. An administrator can exclude AI search from a workspace MCP connection's selected tool list. In that case, the connection omits both the tool and its `ai_search` entry in `current_tool_access`. `notion-get-tool-access` reports the API key `ai_search` as `available` when the workspace can use AI search. Otherwise it reports `upgrade_required` with an `upgrade_url`, or `plan_required` with a `landing_page_url` and `landing_page_action` when Notion routes the user through a plan landing page. If the workspace has a billing restriction, such as an unpaid invoice, calls return a permission error that asks a workspace owner to manage billing instead of falling back to keyword search, and `current_tool_access` reports the `ai_search` key as `not_enabled`.
    </Note>

    **Example prompts:**

    * "How did we solve similar authentication bugs?"
    * "What decisions have we made about the mobile launch?"
    * "Find context about our customer onboarding strategy"
    * "Find related work on improving search results for AI workspaces"
    * "Find discussions about this launch in my connected Slack and Mail"
    * "Look up the workspace user with the email [ada@example.com](mailto:ada@example.com)"
  </Accordion>

  <Accordion title="Check tool access">
    `notion-get-tool-access`

    Reports which tools run on the connected workspace's plan, which of their parameters are restricted, and where to upgrade. Call it before you use a tool whose availability depends on the plan, unless you already know that tool's access. Those tools say so in their own descriptions. Ask for the whole map in one call and reuse it across those tools instead of checking them one at a time. It reads connection metadata, so it doesn't grant access or change the workspace.

    Pass `tool_names` to narrow the response, for example `["search", "ai_search"]`. Omit it to get every tool visible to the connection. Unknown names and tools the connection doesn't expose are left out, and an empty list returns an empty map.

    The response contains `current_tool_access`, a map of tool names to their access state on this workspace's plan. Each entry's `status` is `available`, `available_with_limit` (calls can be made up to the limit included with the workspace's plan), `plan_required`, `upgrade_required` (full access requires an upgrade; tools such as AI search can still return fallback results with a notice), `full_version_required`, or `not_enabled`. An entry carries an `upgrade_url` when a workspace upgrade changes the status, a `full_version_url` when the tool needs the full version of Notion MCP, and a `landing_page_url` with a `landing_page_action` of `start_trial`, `request_trial`, or `learn_more` when Notion routes the user through a plan landing page.

    An entry can also carry `restricted_parameters`, a map from a parameter path such as `filters.title_only` to the reason it's unavailable. These restrictions are independent of the entry's `status`. Read each reason and check whether it applies to your requested value. For example, `filters.teamspace_ids` restricts multiple distinct teamspaces below Business; a single teamspace remains supported. Likewise, a restriction on date sorting doesn't prevent `sort: "relevance"`.

    For content search, prefer `notion-ai-search` when `ai_search.status` is `available`. In that case, the map omits `search`, even if you request it by name. Otherwise, use `notion-search` if the connection exposes it. If only `notion-ai-search` is exposed and its status is `upgrade_required` or `plan_required`, it can still return Notion-only keyword results with a notice. A `not_enabled` status doesn't promise this fallback; billing restrictions still return errors. If neither search tool is exposed, the connection needs an administrator to enable one.

    The map can include both `search` and an unavailable `ai_search` entry. A missing entry means the map doesn't advertise that tool; it doesn't identify a usable fallback. For user lookup, choose an exposed search tool and satisfy the separate user-information and `notion-get-users` requirements above, regardless of AI access.

    Tools can be listed on every plan. Consult this map together with each tool's documented fallback behavior. The map covers the tools in a current tool list, so a tool that is no longer advertised has no entry, even when a cached tool list can still call it. For `query_data_sources`, view mode is always available; Business and Enterprise plans with Notion AI can query any number of data sources, while other plans receive metered single-data-source access.

    Keys are the tools' base names. A tool that appears with a `notion-` prefix and hyphens, such as `notion-query-data-sources`, corresponds to the map key with the prefix dropped and hyphens as underscores (`query_data_sources`).

    **Example prompts:**

    * "Can this connection use AI search, or should you use keyword search?"
    * "Which search filters aren't available on this workspace's plan?"
  </Accordion>

  <Accordion title="Search Notion Skills">
    `notion-search-skills`

    Finds active [Notion Skills](/guides/mcp/notion-skills) that the connected user can access. Pass a Skill name or a short description of the task, or omit the query to list up to 10 recent Skills. Results contain compact metadata; fetch the selected Skill's URL before following its instructions.

    **Example prompts:**

    * "Find my usual workflow for preparing a customer briefing"
    * "What reusable workflows do I have for code review?"
    * "Use my weekly project update Skill"
  </Accordion>

  <Accordion title="Download a Notion Skill">
    `notion-download-skill`

    Downloads a complete [Notion Skill](/guides/mcp/notion-skills#download-a-complete-skill). Pass the Skill page's `id`. The response contains `id`, `version_id`, and a signed `url` for a `tar.gz` archive with `SKILL.md` and supporting files and folders. The URL expires after one hour. Skills without supporting files still return an archive. Requires the Skills API to be enabled for the workspace; unavailable in eval mode and workspace-owned MCP connections.

    **Example prompts:**

    * "Download this Skill and its supporting files for my local agent"
    * "Get the complete directory for this Skill"
  </Accordion>

  <Accordion title="Fetch Notion content">
    `notion-fetch`

    Retrieves content from a Notion page, database, data source, or saved database view by its URL or ID. You can pass a data source ID (from `collection://...` tags in database responses) to fetch details about that specific data source, including its schema and properties. When fetching a database, the response includes available templates for each data source, which can be used with the create-pages and update-page tools.

    Fetched pages include `path`, `page_last_edited_at`, and, when available, `verification.state` and `verification.expires_at`. These fields help distinguish pages with similar titles and identify sources that Notion marks as verified.

    Fetched pages, including database items, include `cover` separately from database properties. It is `null` when there is no cover. Otherwise, it uses the REST API's [file object](/reference/file-object) shape: `type: "external"` with `external.url` for linked or Notion gallery images, or `type: "file"` with `file.url` and `file.expiry_time` for uploaded images.

    MCP's signed cover URLs expire after five minutes; the REST API uses one hour. Re-fetching the page returns a fresh URL. An omitted `cover` means the metadata is unavailable or not applicable, not that the page has no cover.

    Fetched pages, including database items, also include `icon`. It is `null` when there is no icon. Otherwise, it uses the REST API's [emoji and icon object](/reference/emoji-and-icon) shapes: `type: "emoji"` with `emoji`, `type: "custom_emoji"` with `custom_emoji.id`, `custom_emoji.name`, and `custom_emoji.url`, or `type: "icon"` with `icon.name` and `icon.color` for a [native Notion icon](/reference/emoji-and-icon#icon). Image icons use the [file object](/reference/file-object) shape: `type: "external"` with `external.url`, or `type: "file"` with `file.url` and `file.expiry_time` for an image uploaded to Notion.

    Signed icon URLs expire after five minutes, the same as cover URLs, and re-fetching the page returns a fresh URL. An omitted `icon` means the metadata is unavailable or not applicable, not that the page has no icon. The `icon` field is read-only. To set or change an icon, pass the icon string that `notion-create-pages` and `notion-update-page` accept: an emoji character (e.g. "🚀"), a custom emoji by name (e.g. ":rocket\_ship:"), a Notion icon identifier as returned by fetch (e.g. "icons/pizza\_blue"), or an external image URL.

    Pass a `view://` URL from a database response to read a saved view's filters, sorts, and display settings. A database URL with a `?v=` parameter still returns the database. To read the rows shown by a view, use `notion-query-data-sources` with `mode: "view"`.

    To check tool availability, call `notion-get-tool-access` with `{}` and reuse the map. See "Check tool access" above for search routing, user-lookup requirements, statuses, recovery links, and parameter restrictions.

    When a page is large enough that some subtrees could not be loaded, the response sets `truncated` to `true` and includes `unknown_block_ids` (up to 50 omitted subtree root IDs) and `unknown_block_count` (the total number of omitted subtree roots). Pass one of the returned IDs back to `notion-fetch` to retrieve that subtree directly. An ID may also represent content the caller cannot access, so treat an `object_not_found` error on retry as a permissions signal rather than a failure to handle.

    **Example prompts:**

    * "What product requirements still need to be implemented from this ticket `https://notion.com/page-url`?"
    * "Fetch the data source `collection://f336d0bc-b841-465b-8045-024475c079dd` to see its schema"
    * "Fetch the view `view://8ac3f3d0-1f2b-4c7e-9d51-4b0c0a9f2e77` to see how it's filtered and sorted"
    * "Fetch the bug tracking database so I can see the available templates"
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

    Creates one or more Notion pages with specified properties and content. Supports applying [database templates](/guides/data-apis/creating-pages-from-templates) to pre-populate new pages with content and property values. Each page can optionally have an icon (an emoji character, a custom emoji by name, a Notion icon identifier as returned by fetch such as "icons/pizza\_blue", or an external image URL) and a cover image. Set `is_skill: true` to create a page as a [Notion Skill](/guides/mcp/notion-skills). If a parent is not specified, a private page will be created.

    Use `creation_mode: "draft"` when the user wants a durable page but has not named a destination. Draft mode creates a workspace-level private page and cannot be combined with `parent`. If the user names a private or shared destination, omit `creation_mode` and create the page under that parent.

    The tool description recommends `allow_async: true` for most page creates. This is guidance to assistants, not a request default. See [Async page create and update](#async-page-create-and-update).

    Markdown in `content` that is too large or too heavily formatted to parse in one call returns a `validation_error`, and the call creates no pages. All pages in one call share the same parse limit, so a call that creates several pages can reach it even when no single page would. With `allow_async: true`, the call still returns an `async_task`, and the task ends as `failed` with that error. Retrying the same call fails the same way. Create the pages with part of the content and add the rest with further calls, or split the content into child pages.

    **Example prompts:**

    * "Create a project kickoff page under our Projects folder with agenda and team info"
    * "Make a new employee onboarding checklist in our HR database"
    * "Create a new bug report in the tracking database using the 'Urgent Bug' template"
    * "Add a new product feature request to our feature database"
    * "Create a page with the 🚀 icon and a cover image"
    * "Draft a private launch plan; we'll decide where it belongs later"
  </Accordion>

  <Accordion title="Update a page">
    `notion-update-page`

    Update a Notion page's properties, content, icon, or cover. You can also [change whether a page is a Skill](/guides/mcp/notion-skills#change-whether-a-page-is-a-skill) or apply [database templates](/guides/data-apis/creating-pages-from-templates) to an existing page. Icon, cover, and `is_skill` can be set alongside any update command.

    <Note>
      The `update_content` command applies content-changing search-and-replace operations as a batch. If any such operation's `old_str` doesn't match content on the page, the call returns a validation error naming the unmatched value and the page is left unchanged. An operation whose `old_str` and `new_str` are identical is ignored without checking for a match. Each `old_str` must be a non-empty string that matches exactly one location, unless `replace_all_matches: true` is set for that operation.
    </Note>

    The tool description recommends `allow_async: true` for most page updates. This is guidance to assistants, not a request default. See [Async page create and update](#async-page-create-and-update).

    **Example prompts:**

    * "Change the status of this task from 'In Progress' to 'Complete'"
    * "Add a new section about risks to the project plan page"
    * "Apply the project kickoff template to this page"
    * "Set the page icon to 🎯 and add a cover image"
    * "Remove the icon from this page"
  </Accordion>

  <Accordion title="Convert a page to a skill">
    `notion-convert-page-to-skill`

    Marks a Notion page as a [Notion Skill](/guides/mcp/notion-skills) without changing its content. Pass the page's full Notion URL. The page must be in the connected workspace, and you must have permission to edit it.

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

    <Note>
      Use a page URL or ID for relation filters. Use a user ID or `"me"` for person, created-by, and last-edited-by filters. Use an option or group name for status filters, and use `"verified"`, `"expired"`, or `"none"` for verification filters. Page and people names aren't accepted, so resolve them to a URL or ID first. Read the `notion://docs/view-dsl-spec` resource for the full syntax.
    </Note>

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

    Update a view's name, filters, sorts, or display configuration. Only the fields you specify will be changed. Supports clearing existing configuration like filters, sorts, and grouping. Uses the same configuration DSL — and the same filter value formats — as `notion-create-view`.

    **Example prompts:**

    * "Rename the 'All Tasks' view to 'Sprint Board'"
    * "Update the board view to filter by status equals 'Done'"
    * "Clear the filters on this view and add a sort by created date"
    * "Change the view to group by priority and only show Name and Status columns"
  </Accordion>

  <Accordion title="Query across data sources">
    `notion-query-data-sources`

    Query Notion data sources with SQL, read rows from one data source, or run a saved view.

    Pass `mode: "rows"` and `data_source_url` to read one data source. Rich-text properties use [Notion markdown](/guides/data-apis/enhanced-markdown) strings to preserve page and user mentions, link targets, formatting, inline dates, and equations.

    Rows mode accepts optional `filter` and `sort` fields. A filter supports two levels of `and` or `or` groups. Sorts run in listed order. `limit` defaults to 50 and has a maximum of 100.

    The response contains `results` and `has_more`. Each result uses property names as keys. Results include only rows and properties that the connected user can read. Rows mode does not return a cursor.

    A query can resolve up to 1,000 distinct mention targets. A query over this limit returns an error instead of partial rich text.

    <Warning>
      SQL output can omit mention text, link targets, and formatting. Their absence in SQL output does not mean that a rich-text property is damaged. Read the property with rows mode or `notion-fetch` before changing it.
    </Warning>

    <Note>
      View mode is available on every plan without a tool-specific quota. SQL across one or more data sources is unlimited on Business and Enterprise plans with Notion AI. Other plans share a per-workspace usage limit for single-data-source SQL and receive an upgrade prompt after the allowance is exhausted. Rows mode uses the same allowance as single-data-source SQL.
    </Note>

    **Example prompts:**

    * "What's due for me this week across all tasks and meeting note action items? Group by priority."
    * "Show all risks from Engineering and Product databases this month, grouped by owner."
    * "Read the in-progress rows from the Specs data source. Keep mentions and links in Notes."
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

  <Accordion title="Work with Custom Agent sessions">
    Use `notion-list-agents` to browse available Custom Agents. Use
    `notion-search-agents` to get the Custom Agent URL needed to start a
    session. Then use these tools to find sessions, start a session, send
    follow-up messages, wait for a reply, stop a run, and read session events:

    * `notion-query-sessions`
    * `notion-search-sessions`
    * `notion-spawn-session`
    * `notion-get-session-status`
    * `notion-wait-session`
    * `notion-stop-session`
    * `notion-send-message-to-session`
    * `notion-list-session-events`
    * `notion-read-session-event`

    Search results include up to 20 matches. Each title is limited to 150
    characters, and each matching text span is limited to 300 characters.

    `notion-search-sessions` returns no matches and a `warning` when the
    workspace's search index is missing or not ready. Use
    `notion-query-sessions` to list sessions while search is unavailable.

    `notion-query-sessions` can return an empty page with a cursor. The same is
    true for `notion-search-agents` when it is called without a `query`. Keep
    following the cursor until the response stops returning one. A
    `notion-search-agents` call with a `query` returns one page without a cursor.

    Session tools return a `session_url` in the form
    `session://<spaceId>/<sessionId>`. Pass it back unchanged. The tools also
    accept the shorthand `session://<sessionId>` and `thread://<sessionId>`,
    which resolve in the connected workspace. A full URL whose workspace ID
    differs from the connected workspace returns HTTP 400 `validation_error`.
    Malformed URLs and URLs for a resource other than a session also return
    HTTP 400 `validation_error`. A valid session URL in the connected workspace
    returns HTTP 404 `object_not_found` if the session is missing, inaccessible,
    or unsupported.

    `notion-send-message-to-session` returns a conflict error when the session
    already has a run in progress. Wait for that run to finish with
    `notion-wait-session`, then send the message.

    <Note>
      Plan eligibility and tool discovery are separate. When Notion MCP advertises
      these tools, calling them requires Notion AI access and access to Custom
      Agents. Without that access, calls return a prompt with a recovery link. When
      a direct upgrade is available, `current_tool_access` reports the tools as
      `upgrade_required` with an `upgrade_url`. When Notion routes the user through
      a plan landing page instead, it reports them as `plan_required` with a
      `landing_page_url` and `landing_page_action`. If the workspace has a billing
      restriction, such as an unpaid invoice, calls return a permission error that
      asks a workspace owner to manage billing, and `current_tool_access` reports
      the tools as `not_enabled`.

      A connection that lacks the "View sessions and interact with agents"
      capability does not advertise these tools or include them in
      `current_tool_access`. Disconnect and reconnect Notion, or enable the
      capability in the integration's settings and re-authorize.
    </Note>

    **Example prompts:**

    * "Ask our Support Agent to summarize this customer issue"
    * "Wait for the agent session to finish, then show me its answer"
    * "Search my past agent sessions for the launch decision"
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

    Retrieves the current status of an async task started by another tool, such as `notion-duplicate-page`, `notion-create-pages` with `allow_async: true`, or `notion-update-page` whenever it returns an `async_task`. Returns one of `queued`, `running`, `retrying`, `succeeded`, or `failed`. When a task has succeeded, the operation's result is included in the response; when it has failed, an error is included instead.

    Poll this tool with the `task_id` from the originating tool's `async_task` response. Wait briefly between polls — the original response includes a suggested backoff.

    **Example prompts:**

    * "Check whether the page I just duplicated is ready"
    * "Poll this async task until it completes and show me the result"
  </Accordion>
</AccordionGroup>

## Async page create and update

The `notion-create-pages` and `notion-update-page` tools support `allow_async: true` for page create and update work. Their tool descriptions recommend that assistants pass it for most page writes. This is guidance to assistants, not a schema or server default: omitting `allow_async` has the same meaning as before. The same validation, permissions, and write operation still apply.

The descriptions recommend `allow_async: false` when the next step needs the created or updated page right away. They also recommend retrying synchronously when an async attempt is rejected as too large to queue.

A request that is too large to queue returns a `validation_error` instead of an `async_task`. Either split it into smaller page writes or retry it with `allow_async: false`.

When a call returns an `async_task` handle, poll `notion-get-async-task` with the returned `async_task.id` passed as `task_id` until the task reaches `succeeded` or `failed`. Wait for `succeeded` before any step that depends on the write, such as linking to a new page or adding content to it.

<Note>
  A `succeeded` status covers the page write, not template application. When dependent work needs template output, follow the webhook flow in [Creating pages from templates](/guides/data-apis/creating-pages-from-templates#step-3-confirm-page-contents-are-ready). For direct checks, look for the expected content or properties and stop after a bounded number of retries.
</Note>

When `allow_async` is omitted or `false`, `notion-create-pages` keeps its synchronous result shape. `notion-update-page` waits for a synchronous result when it can, but it can still return a pollable `async_task` if queued execution runs past the synchronous wait deadline, so handle both shapes.

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

  When connecting with an OpenAI MCP client (e.g. ChatGPT), the `notion-` prefix is automatically omitted from the `notion-fetch`, `notion-search`, and `notion-ai-search` tools, making them appear as `fetch`, `search`, and `ai-search`, respectively. This hyphenated `ai-search` is an OpenAI presentation name; access responses use the underscored API key `ai_search`. The `fetch` and `search` names are required as part of the [Deep Research specification](https://platform.openai.com/docs/guides/deep-research#remote-mcp-servers) for remote MCP servers.
</Info>

## Rate limits

Standard [API request limits](/reference/request-limits) apply per user's usage of Notion MCP, totaled across all tool calls.

Some MCP tools have additional, tool-specific rate limits that are stricter. These are subject to change over time, but the current values are listed below for reference:

* **`notion-search`** (including user lookups): 30 requests per minute. The limit counts every `notion-search` call, including a content search that runs AI search. These calls also count toward the standard per-user limit. `notion-ai-search` has no tool-specific limit.

### What to do if you're rate-limited

If you encounter rate limit errors, prompt your LLM tool to reduce the amount of parallel searches or operations performed using Notion MCP, and/or try again later. AI search calls take longer than keyword workspace search calls, but only `notion-search` has the additional 30-requests-per-minute limit. A client that runs many fast searches in a row is the most likely to hit the `notion-search` rate limit.

Notion MCP retries a rate limit once when the wait is 2 seconds or less. Otherwise it returns the rate limit as a tool error right away instead of waiting it out. The error's `structuredContent.error` has `code: "rate_limited"`, the wait in seconds as `retry_after_seconds` when known, and the limit that was hit as `rate_limit_reason`. See [Request limits](/reference/request-limits#rate-limit-responses).
