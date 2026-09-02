---
title: "Workspace block limits"
source: https://developers.notion.com/reference/workspace-block-limits
path: reference/workspace-block-limits
---

Learn when the Free workspace block limit blocks an API write and how to handle the error.

<Note>
  The REST API now enforces the [existing Free workspace block limit](https://www.notion.com/help/understanding-block-usage) for the connections described below.
</Note>

## Scope

Free workspaces with more than one member have a limit of 1,000 lifetime blocks. Paid workspaces and single-member Free workspaces have unlimited blocks. Guests do not count as members. Deleting blocks does not restore capacity. See [Understanding block usage](https://www.notion.com/help/understanding-block-usage).

The limit applies to internal connections and OAuth connections restricted to selected workspaces. It does not apply to [personal access tokens](/guides/get-started/personal-access-tokens) or OAuth connections that can be installed in any workspace. Notion MCP has a separate enforcement policy.

## Creation and grace period

The limit is shared across the workspace, not assigned to each connection. The write that first reaches the limit succeeds and starts the existing three-day grace period. Creation remains available during grace. API enforcement does not restart an expired grace period.

After grace expires, requests that create blocks fail. Reads, deletes, and edits that do not create blocks remain available. Template jobs check the limit again when they run, so a queued template can fail after the request that scheduled it returned a success.

## Background templates

A successful create or update response does not guarantee that a queued template will finish. The job checks the limit again before copying content and before each content write. If the workspace becomes blocked, the job stops without retrying the plan restriction. The target page is kept, but it may be blank or contain only part of the template. When replacing content, the original content is removed only after the template succeeds.

There is no template-failure webhook or public job-status endpoint. Set a timeout when waiting for template content, then [retrieve the page's block children](/reference/get-block-children) to check the result. Do not automatically reapply a template to a partially populated page: that can duplicate content. Ask a workspace owner to check [block usage](https://www.notion.com/help/understanding-block-usage) before retrying.

## Affected endpoints

A request fails if it would create blocks. Requests that do not create blocks remain available.

| Endpoint                                                       | Behavior after grace expires                                                                                         |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [Create a page](/reference/post-page)                          | Fails. The page itself is a block.                                                                                   |
| [Create a meeting note](/reference/create-meeting-note)        | Fails. Creates a meeting notes block and its child blocks.                                                           |
| [Create a database](/reference/create-database)                | Fails. The database is a block.                                                                                      |
| [Create a database (deprecated)](/reference/create-a-database) | Fails. API versions before `2025-09-03` create a database block with its data source.                                |
| [Create a data source](/reference/create-a-data-source)        | Still works. API versions `2025-09-03` and later add a data source to an existing database without creating a block. |
| [Append block children](/reference/patch-block-children)       | Fails. Every appended child is a block.                                                                              |
| [Update page markdown](/reference/update-page-markdown)        | Fails when the markdown adds blocks.                                                                                 |
| [Update a page](/reference/patch-page)                         | Fails when the update adds blocks, such as applying a template. Title and property edits still work.                 |
| [Update a block](/reference/update-a-block)                    | Fails when the update adds blocks.                                                                                   |
| [Create a view](/reference/create-view)                        | Fails when `create_database` adds a linked database block. A new view tab on an existing database still works.       |
| [Create a comment](/reference/create-a-comment)                | Fails when an attachment adds a block. A comment without attachments still works.                                    |

## Error response

Blocked writes return HTTP 403 with the `restricted_resource` code:

```json theme={null}
{
  "object": "error",
  "status": 403,
  "code": "restricted_resource",
  "message": "This workspace has used all of its free blocks. Upgrade its plan in Notion to create more content. Learn more: https://www.notion.com/help/understanding-block-usage",
  "additional_data": {
    "block_limit": "block_creation"
  }
}
```

This is a plan limit, not a request rate limit. Retrying the same write without a workspace change will not resolve it. A workspace owner can upgrade in Notion. Creation is also available when the Free workspace has only one member.

Other permission failures also use `restricted_resource`. The `additional_data.block_limit` field identifies this limit without relying on message text. See [Status codes](/reference/status-codes) and [Request limits](/reference/request-limits).
