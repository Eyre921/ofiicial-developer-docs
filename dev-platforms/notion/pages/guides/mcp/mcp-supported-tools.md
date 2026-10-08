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

    Searches Notion for content, or looks up a workspace user by name or email. Hosted Notion MCP sessions list this as their one content-search tool, except for the sessions described at the end of this section. Use it for every content search. You don't need to call another tool first.

    The tool's description in `tools/list` matches the user's AI search access in the workspace:

    * When the user has AI search, `notion-search` runs AI search. It takes keywords, a page title, or a natural-language question, and it searches Notion plus connected sources available to the user, such as Slack, Mail, Calendar, Google Drive, and Jira. Keep a question under about 50 words, with one topic per call. The response reports `type: "ai_search"`.
    * When the workspace's plan doesn't include AI search, `notion-search` runs a keyword search in Notion. Its description adds one line saying that AI search needs a Business or Enterprise plan with Notion AI. Use short, specific keywords.
    * When an admin setting or a billing restriction, such as an unpaid invoice, blocks AI search, `notion-search` runs a keyword search in Notion. Its description has no upgrade line, because an upgrade wouldn't help.

    A call that passes an exact filter, an empty query, or a sort other than `relevance` stays on Notion workspace search and reports `type: "workspace_search"`, even when the user has AI search. A connection whose selected tool list leaves out AI search also keeps its content searches on Notion workspace search.

    `notion-search` supports location (page, data source, or teamspace), creator or editor, date, title, content-status filters, sorting, and up to 50 results. Workspace search results may include `path` and `verification` details. Fetch important matches before relying on them. Results from AI search omit `verification`, so fetch a Notion result with `notion-fetch` when verification state matters. Connected-app results can't be fetched with `notion-fetch`.

    A filter or sort that the workspace's plan doesn't include doesn't fail the call. Notion drops the unavailable options, runs the rest of the search, and adds a `notices` array to the response. A notice names the dropped fields, such as `filters.title_only`, and may include an upgrade link. Results can be broader than requested and use relevance sorting. On a plan without multiple-teamspace search, when `teamspace_id` and `filters.teamspace_ids` select different teamspaces, both are dropped. If dropping the options leaves an empty query with no supported constraint, the response returns no results and a notice asking for a non-empty query or a supported filter.

    <Note>
      Full Notion MCP on Business or Enterprise is required to filter by editor, last-edited date, multiple teamspaces, title only, or content status, and to sort by date. Other filters are available on every plan. To see these limits before you call, `notion-get-tool-access` lists each restricted option under `restricted_parameters` with the reason it's unavailable.
    </Note>

    For a user lookup, call the search tool the connection lists with `query_type: "user"` and a name or email. `notion-search` and `notion-ai-search` both support it, with the same requirements. Omit content filters and sorting, which return a `validation_error` for a user lookup. The response reports `type: "user_search"` and lists the matching users. A user lookup doesn't need AI access. It requires user information [capabilities](/reference/capabilities), and workspace-owned MCP connections must also expose `notion-get-users`. AI search access alone doesn't grant user lookup. Omit `query_type`, or set it to `internal`, for a content search.

    In sessions that list one search tool, `notion-ai-search` (`ai-search` for OpenAI clients) no longer appears in `tools/list`. It stays callable by name, so a client with a cached tool list keeps working, and it behaves as before. In new code, call `notion-search`.

    **Workspace-owned connections keep the earlier behavior.** A connection with a selected tool list lists exactly the tools an admin selected, which can be `notion-search`, `notion-ai-search`, or both. Use the search tool it lists, for both content search and user lookup. Its tool descriptions still say to call `notion-get-tool-access` first, and its access map includes `ai_search` only when `notion-ai-search` is selected. A session where Notion can't read the user's AI search access while it builds the tool list also gets the earlier tool list.

    **Example prompts:**

    * "Search for documents mentioning 'budget approval process'"
    * "Look for meeting notes from last week with John"
    * "What decisions have we made about the mobile launch?"
    * "Find discussions about this launch in my connected Slack and Mail"
    * "Look up the workspace user with the email [ada@example.com](mailto:ada@example.com)"
  </Accordion>

  <Accordion title="Check tool access">
    `notion-get-tool-access`

    Reports which tools run on the connected workspace's plan, which of their parameters are restricted, and where to upgrade. Calling it is optional, except where a workspace-owned connection's descriptions still ask for it (see "Search Notion" above). Tools enforce their own access limits when you call them, so you don't need to check first. Use it when your client wants plan or parameter details before calling a tool, when the user asks which Notion tools or features they can use, or after a result reports restricted access or an upgrade requirement. It reads connection metadata, so it doesn't grant access or change the workspace.

    Pass `tool_names` to narrow the response, for example `["search", "ai_search"]`. Request both search keys, because the map reports only one of them when AI search is available. Omit it to get every tool visible to the connection. Unknown names and tools the connection doesn't expose are left out, and an empty list returns an empty map.

    The response contains `current_tool_access`, a map of tool names to their access state on this workspace's plan. Each entry's `status` is `available`, `available_with_limit` (calls can be made up to the limit included with the workspace's plan), `plan_required`, `upgrade_required` (full access requires an upgrade; tools can still return fallback results with a notice), `full_version_required`, or `not_enabled`. An entry carries an `upgrade_url` when a workspace upgrade changes the status, a `full_version_url` when the tool needs the full version of Notion MCP, and a `landing_page_url` with a `landing_page_action` of `start_trial`, `request_trial`, or `learn_more` when Notion routes the user through a plan landing page.

    An entry can also carry `restricted_parameters`, a map from a parameter path such as `filters.title_only` to the reason it's unavailable. These restrictions are independent of the entry's `status`. Read each reason and check whether it applies to your requested value. For example, `filters.teamspace_ids` restricts multiple distinct teamspaces below Business; a single teamspace remains supported. Likewise, a restriction on date sorting doesn't prevent `sort: "relevance"`.

    In sessions that list one search tool, the map still reports AI search access under the key `ai_search`, even though `tools/list` doesn't show `notion-ai-search`. Its status is `available` when the user has AI search. Otherwise it's `upgrade_required` with an `upgrade_url`, or `plan_required` with a landing page, when the plan lacks AI search. It's `not_enabled` when an admin setting or a billing restriction blocks AI search. When `ai_search` is `available`, the map leaves out `search`, even if you request it by name. Either way, keep calling `notion-search`. The `search` and `ai_search` entries carry the same `restricted_parameters`.

    Tools can be listed on every plan. Read this map together with each tool's documented fallback behavior. A missing entry means the map doesn't advertise that tool; it doesn't identify a usable fallback. For `query_data_sources`, view mode is always available; Business and Enterprise plans with Notion AI can query any number of data sources, while other plans receive metered single-data-source access.

    Keys are the tools' base names. A tool that appears with a `notion-` prefix and hyphens, such as `notion-query-data-sources`, corresponds to the map key with the prefix dropped and hyphens as underscores (`query_data_sources`).

    **Example prompts:**

    * "Which Notion tools can I use on this workspace's plan?"
    * "Which search filters aren't available on this workspace's plan?"
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

    To create a top-level page in a teamspace, pass `parent: {"teamspace_id": "…"}` with an ID from `notion-get-teams`. All pages in the call share that parent. See [Teamspace root pages](#teamspace-root-pages) for permissions and an example.

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

    When part of the input was changed or ignored, the result includes a `warnings` array. Examples are lines dropped for incorrect indentation and text auto-corrected to match the page. Each warning has a `code` and a `message`. Each message is at most 500 characters; a longer one is cut and ends with a note giving its original length, such as `… (truncated from 12000 characters)`. Markdown parser warnings also carry `category`, such as `unsupported_tag`, and `autofix`, which is `true` when the parser changed the content to apply it. A clean update has no `warnings` key. Read any warnings before you treat the edit as done.

    ```json theme={null}
    {
      "page_id": "3f20509d-d76d-81a9-8a48-ebb7c86a786e",
      "warnings": [
        {
          "code": "update_warning",
          "message": "The following lines were dropped due to incorrect indentation: Dropped line"
        }
      ]
    }
    ```

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

## Teamspace root pages

`notion-create-pages` accepts `parent.teamspace_id` to create pages directly in a teamspace, alongside its other top-level pages. Get the ID from `notion-get-teams`; IDs with or without dashes are accepted. Pass only one parent ID per call.

Use a connection that acts as a Notion user. Bot-scoped workspace connections don't support this destination. The user must have permission to edit the teamspace's pages and add top-level pages. If the teamspace limits top-level page edits to owners, the user must be a teamspace owner. Listing a teamspace with `notion-get-teams` doesn't grant permission to create pages there.

New pages inherit the teamspace's permissions, so people with access to its pages can access the new pages. The teamspace must be active and belong to the connected workspace. Omit `creation_mode`: draft mode creates private pages and can't be combined with a teamspace parent.

For example, replace the sample ID with a teamspace ID returned by `notion-get-teams`:

```json theme={null}
{
  "tool": "notion-create-pages",
  "arguments": {
    "parent": { "teamspace_id": "195de922-1179-449f-ab80-75a27c979105" },
    "allow_async": true,
    "pages": [
      {
        "properties": { "title": "Project kickoff" },
        "content": "# Project kickoff\n\nGoals, owners, and next steps."
      }
    ]
  }
}
```

Teamspace root creation supports both synchronous and [async page creation](#async-page-create-and-update). When the tool returns an `async_task`, wait for it to succeed before using the new pages. This parent option is specific to Notion MCP; it isn't a parent option for the REST [Create a page](/reference/post-page) endpoint.

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

If the task is still `queued`, `running`, or `retrying`, wait at least the suggested `poll_after_seconds` before polling again. A `succeeded` task includes the operation result. For `notion-update-page`, that result includes the same `warnings` array as a direct call. A `failed` task includes an error object that the assistant can summarize or use to retry with a corrected request.

<Info>
  **Tool names and results differ for OpenAI clients**

  When you connect with an OpenAI MCP client, such as ChatGPT, Notion MCP drops the `notion-` prefix from `notion-fetch` and `notion-search`, so they appear as `fetch` and `search`. OpenAI's [MCP requirements](https://developers.openai.com/api/docs/mcp) use these names for ChatGPT company knowledge and deep research. A client with a cached tool list can still call `notion-ai-search` by its OpenAI name, `ai-search`. Access responses use the API key `ai_search`.

  For ChatGPT connections, content searches with `search` and calls to `fetch` return OpenAI's result shape, as both `structuredContent` and JSON text. A user lookup with `query_type: "user"` keeps the standard response. A connection counts as ChatGPT when its OAuth redirect URI is a trusted ChatGPT redirect URI. Other clients, including other OpenAI clients such as Codex, get the standard results. So do `ai-search` calls.

  `search` returns `{ results: [{ id, title, url }] }`. Each `id` works with `fetch`, so results that `fetch` can't open, such as connected-app results, are left out. These results don't include highlights, `path`, timestamps, or `notices`.

  `fetch` returns `{ id, title, text, url, metadata }`, where `id` is the id you passed. When you pass `include_file_urls: true`, `metadata.references` maps each uploaded file's `notion-file-block://` source in `text` to a signed download URL. Without it, the response has no `references`.
</Info>

## Rate limits

Notion MCP uses the standard [API request limits](/reference/request-limits). Every tool call counts toward them. These limits can change over time.

### What to do if you're rate-limited

If you encounter rate limit errors, prompt your LLM tool to reduce parallel operations, or try again later.

Notion MCP retries a rate limit once when the wait is 2 seconds or less. Otherwise it returns the rate limit as a tool error right away instead of waiting it out. The error's `structuredContent.error` has `code: "rate_limited"`, the wait in seconds as `retry_after_seconds` when known, and the limit that was hit as `rate_limit_reason`. The text content includes the same `structuredContent` JSON for clients that read only text. See [Request limits](/reference/request-limits#rate-limit-responses).
