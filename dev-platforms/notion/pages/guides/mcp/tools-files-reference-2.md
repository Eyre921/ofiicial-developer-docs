---
title: "Work with files — technical reference"
source: https://developers.notion.com/guides/mcp/tools-files-reference
path: guides/mcp/tools-files-reference
---

Find upload steps, file-size limits, attachment options, and download-link requirements for Notion MCP file tools.

## Create a file upload URL

`notion-create-file-upload`

Creates a short-lived URL for uploading one local file directly to Notion. After calling the tool, the MCP client sends the file as a `multipart/form-data` POST request using the returned URL, headers, and form field. The upload response includes `suggested_markdown`, which can be passed directly to `notion-create-pages` or `notion-update-page`, or included on a separate line in `notion-create-comment` markdown to attach the file.

Files are limited to 20 MiB for this single-part upload flow, and workspace file-size limits still apply. For larger files, use the [file upload API](/guides/data-apis/working-with-files-and-media).

## Create an attachment

`notion-create-attachment`

Creates a Notion attachment from exactly one source: inline UTF-8 text, a file at a direct public HTTPS URL, or a completed file upload created by the same integration. The result includes `suggested_markdown`, which can be passed directly to `notion-create-pages` or `notion-update-page`, or included on a separate line in `notion-create-comment` markdown to attach the file.

Inline content supports text formats such as HTML, Markdown, CSV, JSON, and SVG, up to 200 KiB. URL downloads support binary files, must complete within one minute, and are limited to 5 MiB on free workspaces or 50 MiB on paid workspaces. URLs must not redirect, require request headers or cookies, or resolve to a private network address. For local files, use `notion-create-file-upload` when available. For files that exceed these limits or downloads that require redirects or authentication, use the [file upload API](/guides/data-apis/working-with-files-and-media) and pass the resulting upload ID as `source_file_id`.

## Download a text attachment

`notion-download-attachment`

Downloads the complete UTF-8 text content of an attachment created by `notion-create-attachment`. Pass the `file_upload_id` returned when the attachment was created. The attachment must belong to the same integration, have completed uploading, and use a supported text format such as HTML, Markdown, plain text, CSV, JSON, XML, CSS, YAML, TSV, calendar, GPX, or SVG.

Downloads are limited to 200 KiB. This tool does not fetch arbitrary URLs or return binary files. For larger or binary attachments, use the signed file URL returned when reading the page that contains the attachment.

## Get file download URLs

`notion-get-file-download-urls`

Returns signed download URLs for files that `notion-fetch` output cites with `notion-file-block://` references. Pass up to 25 references in `references`, copied exactly from the fetched markdown. Each reference resolves on its own. `files` lists the ones that resolved, each with `reference`, `url`, and `expiry_time`. `unresolved` lists the rest with a `reason`: `invalid_reference` when the value isn't a `notion-file-block://` reference, or `file_not_found` when the file doesn't exist or the user can't access it.

The URLs expire after a few minutes. Call the tool again for fresh ones. When you edit or copy page markdown, keep the `notion-file-block://` references, not the signed URLs.

## Create a folder

`notion-create-folder`

Create an empty Folder under a parent page.

## Update a folder

`notion-update-folder`

Changes an existing Folder with one command per call. Pass the Folder's `folder_id`, with or without dashes, and exactly one of these command shapes:

* `{"command": "add_files", "file_upload_ids": [...]}` adds files by the file upload IDs that the upload tools return, such as `notion-create-file-upload`.
* `{"command": "remove_files", "file_urls": [...]}` removes files. Fetch the Folder first and pass the exact file URLs from that result.
* `{"command": "add_subfolder", "title": "..."}` creates a nested Folder. The response includes `created_folder_id` and `created_folder_url`.

The response also includes `folder_id`, `command`, and `updated_item_count`.
