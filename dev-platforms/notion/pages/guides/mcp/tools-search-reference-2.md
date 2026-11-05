---
title: "Search and read information — technical reference"
source: https://developers.notion.com/guides/mcp/tools-search-reference
path: guides/mcp/tools-search-reference
---

Find search filters, response formats, and access requirements for Notion MCP search, meeting notes, users, and connected sources.

## Search Notion

`notion-search`

Searches Notion pages and databases, or looks up a workspace user by name or email. It doesn't search connected sources such as Slack or Google Drive. Use `notion-connector-search` for those, when the session lists it. For a question that covers both Notion and connected sources, call both tools in parallel. You don't need to call another tool first.

Content searches report `type: "workspace_search"`. Use short, specific keywords or a page title. When the session lists `notion-connector-search`, a content search result ends with a short note that connected sources weren't searched, except in ChatGPT.

`notion-search` supports location (page, data source, or teamspace), creator or editor, date, title, content-status filters, sorting, and up to 50 results. In `filters.created_by_user_ids` and `filters.edited_by_user_ids`, pass `"me"` for the connected user. Results may include `path` and `verification` details. Fetch important matches before relying on them.

A filter or sort that the workspace's plan doesn't include doesn't fail the call. Notion drops the unavailable options, runs the rest of the search, and adds a `notices` array to the response. A notice names the dropped fields, such as `filters.title_only`, and may include an upgrade link. Results can be broader than requested and use relevance sorting. On a plan without multiple-teamspace search, when `teamspace_id` and `filters.teamspace_ids` select different teamspaces, both are dropped. If dropping the options leaves an empty query with no supported constraint, the response returns no results and a notice asking for a non-empty query or a supported filter.

> [!NOTE]
>
> Full Notion MCP on Business or Enterprise is required to filter by editor, last-edited date, multiple teamspaces, title only, or content status, and to sort by date. Other filters are available on every plan. To see these limits before you call, `notion-get-tool-access` lists each restricted option under `restricted_parameters` with the reason it's unavailable.

For a user lookup, call the search tool the connection lists with `query_type: "user"` and a name or email. `notion-search` and `notion-ai-search` both support it, with the same requirements. Omit content filters and sorting, which return a `validation_error` for a user lookup. The response reports `type: "user_search"` and lists the matching users. A user lookup doesn't need AI access. It requires user information [capabilities](/reference/capabilities), and workspace-owned MCP connections must also expose `notion-get-users`. AI search access alone doesn't grant user lookup. Omit `query_type`, or set it to `internal`, for a content search.

`notion-ai-search` (`ai-search` for OpenAI clients) doesn't appear in `tools/list`. It stays callable by name, so a client with a cached tool list keeps working, and it still searches Notion and connected sources together. In new code, call `notion-search` and `notion-connector-search`.

**Workspace-owned connections keep the earlier behavior.** A connection with a selected tool list lists exactly the tools an admin selected, which can be `notion-search`, `notion-ai-search`, or both. It doesn't list `notion-connector-search`. Use the search tool it lists, for both content search and user lookup. When the user has AI search, `notion-search` runs AI search across Notion and connected sources and reports `type: "ai_search"`. A call that passes an exact filter, an empty query, or a sort other than `relevance` stays on Notion workspace search, and so does every content search on a connection whose selected tool list leaves out AI search. Its tool descriptions still say to call `notion-get-tool-access` first, and its access map includes `ai_search` only when `notion-ai-search` is selected.

## Search connected sources

`notion-connector-search`

Searches the connected sources available to the user, such as Slack, Google Drive, GitHub, Jira, mail, and calendar. It doesn't search Notion pages or databases. Use `notion-search` for those. Hosted Notion MCP sessions list this tool when the user has AI search and the workspace has at least one connected source. Workspace-owned connections don't list it. If it doesn't appear in your client, refresh the client's tool list or reconnect Notion MCP. In ChatGPT, it appears after OpenAI reviews the updated Notion app.

Put the full question in `question`, and distinctive names and terms in `keywords`. `lookback` sets a time window, such as `"7d"`, `"all_time"`, or a date like `"2026-10-01"`. To search only some sources, pass `sources`, such as `["slack"]` or `["google-drive", "github"]`. The names match the ones the response reports in `searchedSources`. Fewer sources return sooner. Omit `sources` to search every connected source.

The response lists the sources it searched in `searchedSources`. A source that failed or timed out appears in `searchTargetStatuses`. Each result has a `url` that opens the item in its source app, and results without one are left out. The `warnings` array explains a requested source that wasn't searched, a source that failed or timed out (with the `sources` value to retry just that source), or a search that found no connected source.

`notion-connector-search` needs the same AI access as AI search: Business or Enterprise with Notion AI. `notion-get-tool-access` reports it under `connector_search`.

To read a full item, pass the result's `id` or `url` to `notion-fetch`. Fetch reads the item through the user's own connection to that source, so it returns only what that connection can see. This works for results from Slack, Google Drive, GitHub, Jira, Microsoft Teams, SharePoint, Gmail, Notion Mail, Linear, Salesforce, Asana, and Box. Fetch can't open Outlook, Google Calendar, or Confluence results. To read a Notion Calendar event, use `notion-calendar-list-events` with a time range that covers it.

Only connections that act as a user can open these results: Notion MCP OAuth connections and personal access tokens. The user needs the same AI access as `notion-connector-search`. Custom Agents and other bots can't open them. If fetch can't load an item, for example because the source isn't connected for the user or the item is gone, it returns an error that names the source and says to use the search result's title, highlight, and `url` instead.

## Fetch Notion content

`notion-fetch`

Retrieves content from a Notion page, database, data source, or saved database view by its URL or ID. You can pass a data source ID (from `collection://...` tags in database responses) to fetch details about that specific data source, including its schema and properties. When fetching a database, the response includes available templates for each data source, which can be used with the create-pages and update-page tools.

For [personal memories](/guides/mcp/tools-skills-agents-reference#read-save-and-update-memories), pass `id: "memory"` to read the connected user's About page and Memories database in this workspace. This doesn't create them.

Fetched pages include `path`, `page_last_edited_at`, and, when available, `verification.state` and `verification.expires_at`. These fields help distinguish pages with similar titles and identify sources that Notion marks as verified.

Fetched pages, including database items, include `cover` separately from database properties. It is `null` when there is no cover. Otherwise, it uses the REST API's [file object](/reference/file-object) shape: `type: "external"` with `external.url` for linked or Notion gallery images, or `type: "file"` with `file.url` and `file.expiry_time` for uploaded images.

MCP's signed cover URLs expire after five minutes; the REST API uses one hour. Re-fetching the page returns a fresh URL. An omitted `cover` means the metadata is unavailable or not applicable, not that the page has no cover.

Fetched pages, including database items, also include `icon`. It is `null` when there is no icon. Otherwise, it uses the REST API's [emoji and icon object](/reference/emoji-and-icon) shapes: `type: "emoji"` with `emoji`, `type: "custom_emoji"` with `custom_emoji.id`, `custom_emoji.name`, and `custom_emoji.url`, or `type: "icon"` with `icon.name` and `icon.color` for a [native Notion icon](/reference/emoji-and-icon#icon). Image icons use the [file object](/reference/file-object) shape: `type: "external"` with `external.url`, or `type: "file"` with `file.url` and `file.expiry_time` for an image uploaded to Notion.

Signed icon URLs expire after five minutes, the same as cover URLs, and re-fetching the page returns a fresh URL. An omitted `icon` means the metadata is unavailable or not applicable, not that the page has no icon. The `icon` field is read-only. To set or change an icon, pass the icon string that `notion-create-pages` and `notion-update-page` accept: an emoji character (e.g. "🚀"), a custom emoji by name (e.g. ":rocket\_ship:"), a Notion icon identifier as returned by fetch (e.g. "icons/pizza\_blue"), or an external image URL.

Page markdown cites files in page blocks by stable `notion-file-block://` references and doesn't sign them. Files in database properties are still signed inline. To get download URLs, call `notion-get-file-download-urls` with those references, or pass `include_file_urls: true` to get a `references` map from each reference to a signed URL. `include_file_urls` defaults to `false`.

Pass a `view://` URL from a database response to read a saved view's filters, sorts, and display settings. A database URL with a `?v=` parameter still returns the database. To read the rows shown by a view, use `notion-query-data-sources` with `mode: "view"`.

When a page is large enough that some subtrees could not be loaded, the response sets `truncated` to `true` and includes `unknown_block_ids` (up to 50 omitted subtree root IDs) and `unknown_block_count` (the total number of omitted subtree roots). Pass one of the returned IDs back to `notion-fetch` to retrieve that subtree directly. An ID may also represent content the caller cannot access, so treat an `object_not_found` error on retry as a permissions signal rather than a failure to handle.

`notion-fetch` also opens results from `notion-connector-search`, such as a Slack thread or a GitHub file, by their `id` or `url`. The response has the item's `title`, `url`, and full `text`, and `metadata.type` is `connector`. See [Search connected sources](/guides/mcp/tools-search-reference#search-connected-sources) for which sources and connections support it.

Older clients can pass the id `self` to get the connected workspace and user instead of a page. This path still works, but new clients should [use `notion-get-self`](/guides/mcp/build-mcp-client#identify-the-connected-workspace).

## List sidebar pages

These tools list pages and databases from the user's sidebar:

* `notion-list-private-pages`: top-level pages and databases in the user's **Private** section.
* `notion-list-shared-pages`: pages and databases in the user's **Shared** section.
* `notion-list-favorite-pages`: the user's favorites, in sidebar order.
* `notion-list-recent-pages`: pages and databases the user recently viewed, ranked by recency and visit frequency. It covers only the user's 1,000 top-ranked pages. This list reflects views, not edits. To find pages the user edited, use `notion-search` with `filters.edited_by_user_ids: ["me"]` and `sort: "last_edited"`.

Each result has a `type` of `page` or `database`, a `url`, and, when available, a `title` and an `icon`.

`limit` is 1 to 200 and defaults to 50. When more results follow, the response includes `nextCursor`. Pass it back as `cursor` until the response stops returning one. A page of results can be shorter than `limit`, or empty, and still include `nextCursor`.

For content searches, including by title, use `notion-search`.

## List page backlinks

`notion-list-page-backlinks`

Lists the pages in the connected workspace that link to or mention a page or database. Pass the page's ID or URL as `page_id`. The tool returns IDs, titles, and URLs, never page content. To read a result, fetch it with `notion-fetch`. Requires the read content [capability](/reference/capabilities).

Each entry in `backlinks` has a `type` and a `source` with the linking page's `id`, `url`, `title`, and `last_edited_time`. An entry can also show where the mention is: `block_id` for a block in the source page, `comment_id` for a comment, or `property` (`id` and `name`) for a database property. Within one response, each source page appears at most once per type. The same page can appear again in a later response, because a page boundary can fall between two entries for it. `type` is one of these values:

* `page_mention`: an inline mention in text, a title, or a caption.
* `link_to_page`: a link to page block.
* `property_mention`: a mention in a database property.
* `comment_mention`: a mention in a comment.

Pass `types` to return only some kinds. Omit it to get all of them.

The list includes only pages the user can open. It never says how many backlinks it left out. Backlinks from other workspaces aren't included. A page the user can reach only through view-only web sharing returns an empty list.

`page_size` is 1 to 100 and defaults to 25. The response includes `next_cursor` only when another backlink the user can open follows. Pass it as `cursor`, with the same `page_id` and `types`, to get the next page. A response can have fewer than `page_size` backlinks, or none. The list can also end early, with no `next_cursor` and no error, for example when many backlinks come from pages the user can't open.

A page that doesn't exist, or that the user can't read, returns an HTTP 400 `validation_error` with `additional_data.tool_error_code` set to `page_not_found`. The two cases look the same. A block ID that isn't a page or database returns a `validation_error`. So does a cursor from a different request, or one that was changed.

## Query meeting notes

`notion-query-meeting-notes`

Query the current user's meeting notes, filtering by meeting-specific properties (such as a title keyword search). Returns meetings where the user is an attendee or creator by default.

> [!NOTE]
>
> Available on all plans, but using it requires a Business plan or higher with Notion AI. On other plans the tool returns an upgrade prompt.

## FAQs

### How do tool names and results differ in OpenAI clients?

When you connect with an OpenAI MCP client, such as ChatGPT, Notion MCP drops the `notion-` prefix from `notion-fetch` and `notion-search`, so they appear as `fetch` and `search`. OpenAI's [MCP requirements](https://developers.openai.com/api/docs/mcp) use these names for ChatGPT company knowledge and deep research. A client with a cached tool list can still call `notion-ai-search` by its OpenAI name, `ai-search`. `notion-connector-search` keeps its `notion-` prefix. Access responses report AI search access under the API key `connector_search`, or under `ai_search` in workspace-owned connections.

For ChatGPT connections, content searches with `search` and calls to `fetch` return OpenAI's result shape, as both `structuredContent` and JSON text. A user lookup with `query_type: "user"` keeps the standard response. A connection counts as ChatGPT when its OAuth redirect URI is a trusted ChatGPT redirect URI. Other clients, including other OpenAI clients such as Codex, get the standard results. So do `ai-search` calls.

`search` returns `{ results: [{ id, title, url }] }`. Each `id` works with `fetch`. Connected-app results and other results that `fetch` can't open are left out. These results don't include highlights, `path`, timestamps, or `notices`.

`fetch` returns `{ id, title, text, url, metadata }`, where `id` is the id you passed. Other fields of the standard response stay in place, so `fetch` with the id `self` still returns the `self` object. When you pass `include_file_urls: true`, `metadata.references` maps each uploaded file's `notion-file-block://` source in `text` to a signed download URL. Without it, the response has no `references`.

## Identify the current connection

`notion-get-self`

Returns the workspace and user for the current connection. Call it with an empty object. The response contains these stable fields:

* `workspace.id` and `workspace.name`: the connected workspace. The name can be an empty string.
* `user.type`: `person` or `bot`.
* `user.id` and `user.name`: the connected user. The name can be an empty string.
* `user.email`: present only when `user.type` is `person` and the user has an email address.

For user and workspace IDs right after OAuth, prefer the fields in the [token response](/guides/mcp/build-mcp-client#identify-the-connected-workspace). They don't need a tool call.

## Get teams

`notion-get-teams`

Retrieves a list of teams (teamspaces) in the current workspace.

## Get groups

`notion-get-groups`

Lists the permission groups in the current workspace that the user can see, with each group's ID and name. Pass an optional `query` to search by name, or pass a group reference from a People property value (`space_permission_group-<id>`, or the bare ID) to look up that group's name. Returns at most 25 groups and reports when there are more.

Workspace members see every group in the workspace, as they do in the People picker. Guests and connections that don't act as a user get no groups.

## Get users

`notion-get-users`

Lists workspace members and guests with their IDs, names, emails (when available), and types (person or bot). Supports pagination and search by name or email. You can also retrieve a specific user by ID, or the current user (or bot) by passing `self`.

## Check tool access

`notion-get-tool-access`

Reports which tools run on the connected workspace's plan, which of their parameters are restricted, and where to upgrade. Calling it is optional, except where a workspace-owned connection's descriptions still ask for it (see [Search Notion](/guides/mcp/tools-search-reference#search-notion)). Tools enforce their own access limits when you call them, so you don't need to check first. Use it when your client wants plan or parameter details before calling a tool, when the user asks which Notion tools or features they can use, or after a result reports restricted access or an upgrade requirement. It reads connection metadata, so it doesn't grant access or change the workspace.

Pass `tool_names` to narrow the response, for example `["search", "connector_search"]`. Omit it to get every tool visible to the connection. Unknown names and tools the connection doesn't expose are left out, and an empty list returns an empty map.

The response contains `current_tool_access`, a map of tool names to their access state on this workspace's plan. Each entry's `status` is `available`, `available_with_limit` (calls can be made up to the limit included with the workspace's plan), `plan_required`, `upgrade_required` (full access requires an upgrade; tools can still return fallback results with a notice), `full_version_required`, or `not_enabled`. An entry carries an `upgrade_url` when a workspace upgrade changes the status, a `full_version_url` when the tool needs the full version of Notion MCP, and a `landing_page_url` with a `landing_page_action` of `start_trial`, `request_trial`, or `learn_more` when Notion routes the user through a plan landing page.

An entry can also carry `restricted_parameters`, a map from a parameter path such as `filters.title_only` to the reason it's unavailable. These restrictions are independent of the entry's `status`. Read each reason and check whether it applies to your requested value. For example, `filters.teamspace_ids` restricts multiple distinct teamspaces below Business; a single teamspace remains supported. Likewise, a restriction on date sorting doesn't prevent `sort: "relevance"`.

The map reports AI search access under `connector_search`. Its status is `available` when the user has AI search. Otherwise it's `upgrade_required` with an `upgrade_url`, or `plan_required` with a landing page, when the plan lacks AI search. It's `not_enabled` when an admin setting or a billing restriction blocks AI search. The map always includes `search` and leaves out `ai_search`. In workspace-owned connections, the map reports `ai_search` only when `notion-ai-search` is selected, and leaves out `search` when `ai_search` is `available`, so request both keys there. The `search` and `ai_search` entries carry the same `restricted_parameters`.

Tools can be listed on every plan. Read this map together with each tool's documented fallback behavior. A missing entry means the map doesn't advertise that tool; it doesn't identify a usable fallback. For `query_data_sources`, view mode is always available; Business and Enterprise plans with Notion AI can query any number of data sources, while other plans receive metered single-data-source access.

Keys are the tools' base names. A tool that appears with a `notion-` prefix and hyphens, such as `notion-query-data-sources`, corresponds to the map key with the prefix dropped and hyphens as underscores (`query_data_sources`).

## Workspace-owned connections

Workspace-owned MCP connections expose only the tools an admin selected from the set below. Other tools in this reference aren’t available in these connections.

| Category | Tools available for an admin to select |
| - | - |
| Search and reading | `notion-search`, `notion-ai-search`, `notion-fetch` |
| Pages | `notion-create-pages`, `notion-update-page`, `notion-move-pages`, `notion-duplicate-page`, `notion-get-async-task` |
| Databases and views | `notion-create-database`, `notion-update-data-source`, `notion-create-view`, `notion-update-view`, `notion-query-data-sources`, `notion-query-multiple-data-sources` |
| Files | `notion-create-attachment`, `notion-create-file-upload`, `notion-download-attachment`, `notion-get-file-download-urls` |
| Comments | `notion-create-comment`, `notion-get-comments` |
| Skills | `notion-convert-page-to-skill` |
| Workspace and access | `notion-get-self`, `notion-get-tool-access`, `notion-get-users` |
