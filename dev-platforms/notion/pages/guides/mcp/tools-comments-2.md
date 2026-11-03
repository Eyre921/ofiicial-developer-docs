---
title: "Work together in Notion"
source: https://developers.notion.com/guides/mcp/tools-comments
path: guides/mcp/tools-comments
---

Add comments, follow discussions, suggest edits, and track changes with your team and AI assistants.

Notion gives you, your teammates, and your AI assistants a shared place to work on documents. See what changed and who changed it, discuss feedback, and propose edits without applying them immediately.

Suggestions stay on the page for you or a teammate to review later. You can also ask your AI assistant to review and accept or reject them. Read earlier versions to understand how the work developed, or recover pages from Trash.

## Try a prompt

Review our launch proposal in Notion. Summarize what changed since Monday and who made the changes, read the unresolved comments, and suggest edits to address them. Leave the suggestions pending for my team to review.

Review our launch proposal in Notion. Summarize what changed since Monday and who made the changes, read the unresolved comments, and suggest edits to address them. Leave the suggestions pending for my team to review.

## Available tools

| Action | What it does | Tool name |
| - | - | - |
| Review changes | See what changed, who changed it, and whether the edits came from a person, AI, or an MCP client. | [`notion-get-version-changes`](/guides/mcp/tools-comments-reference#get-version-changes) |
| Read an earlier version | See a page as it was at a previous point in time. | [`notion-view-version`](/guides/mcp/tools-comments-reference#view-a-past-version) |
| Restore pages | Recover pages from Trash. | [`notion-restore-pages`](/guides/mcp/tools-comments-reference#restore-pages) |
| Add feedback | Comment on a page or specific content, or reply to a discussion. | [`notion-create-comment`](/guides/mcp/tools-comments-reference#add-a-comment) |
| Read feedback | Read comments, discussions, and pending suggestions on a page. | [`notion-get-comments`](/guides/mcp/tools-comments-reference#get-comments) |
| Edit your comments | Update or delete comments you wrote. | [`notion-update-comment`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments)  [`notion-delete-comment`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) |
| Resolve a discussion | Mark a discussion as resolved or reopen it. | [`notion-set-discussion-resolved`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) |
| React to a comment | Add or remove your emoji reaction. | [`notion-set-comment-reaction`](/guides/mcp/tools-comments-reference#edit-and-react-to-comments) |
| Suggest a change | Propose a page edit for review. | [`notion-create-suggested-edit`](/guides/mcp/tools-comments-reference#suggest-edits) |
| Review a suggestion | Read the proposed change before deciding whether to apply it. | [`notion-get-suggested-edit`](/guides/mcp/tools-comments-reference#suggest-edits) |
| Accept or reject a suggestion | Apply a proposed change or discard it. | [`notion-resolve-suggested-edit`](/guides/mcp/tools-comments-reference#suggest-edits) |

## Things to know

Suggested edits do not change a page until they are accepted. Your assistant acts with your permissions; accepting a suggestion requires edit access. Your assistant can edit or delete only comments you wrote. Editing comments and working with suggested edits require a Business or Enterprise plan.

Viewing page history requires edit access and is limited to the history retained by your workspace plan. Restoring a page recovers it from Trash; it does not revert it to an earlier version.

## Technical reference

See the [technical reference](/guides/mcp/tools-comments-reference) for parameters, response formats, requirements, and examples for these tools.
