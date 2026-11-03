---
title: "Work with files"
source: https://developers.notion.com/guides/mcp/tools-files
path: guides/mcp/tools-files
---

Upload documents, attach files to project pages, organize folders, and get download links.

Add supporting documents to project pages and organize them in folders. Your assistant can upload files, save text as attachments, and retrieve download links.

## Try a prompt

Upload the report I attached to our project page in Notion. Put it in a Project files folder and add a link to it in the project summary.

Upload the report I attached to our project page in Notion. Put it in a Project files folder and add a link to it in the project summary.

## Available tools

| Action | What it does | Tool name |
| - | - | - |
| Upload a file | Upload a local file for use in Notion. | [`notion-create-file-upload`](/guides/mcp/tools-files-reference#create-a-file-upload-url) |
| Create an attachment | Save text, a file from a public URL, or a completed upload as an attachment. | [`notion-create-attachment`](/guides/mcp/tools-files-reference#create-an-attachment) |
| Read a text attachment | Read the text of an attachment created through the connection. | [`notion-download-attachment`](/guides/mcp/tools-files-reference#download-a-text-attachment) |
| Get download links | Get temporary download links for files on a page. | [`notion-get-file-download-urls`](/guides/mcp/tools-files-reference#get-file-download-urls) |
| Create a folder | Add an empty folder under a page. | [`notion-create-folder`](/guides/mcp/tools-files-reference#create-a-folder) |
| Organize a folder | Add or remove files and create subfolders. | [`notion-update-folder`](/guides/mcp/tools-files-reference#update-a-folder) |

## Things to know

File-size limits depend on the upload method and workspace plan. Download links expire, so ask your assistant for a new link if one no longer works.

## Technical reference

See the [technical reference](/guides/mcp/tools-files-reference) for parameters, response formats, requirements, and examples for these tools.
