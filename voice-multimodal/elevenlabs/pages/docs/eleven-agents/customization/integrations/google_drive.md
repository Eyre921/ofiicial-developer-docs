---
title: "Google Drive"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/google_drive.md
path: docs/eleven-agents/customization/integrations/google_drive
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Google Drive

## Overview

Connect [Google Drive](https://drive.google.com) to your ElevenLabs agents to sync documents into your knowledge base. Your agents can then use the synced content for retrieval-augmented generation (RAG) during conversations.

The connection uses the narrow `drive.file` scope. ElevenLabs only sees the files you hand it through the Google File Picker and cannot list or read anything else in your Drive.

After the initial sync, ElevenLabs detects changes and re-syncs incrementally without re-processing unchanged documents.

## Capabilities

| Capability                | Support       |
| ------------------------- | ------------- |
| Zero retention mode (ZRM) | Not supported |

## Setup

#### Connect your Google account

On the ElevenLabs Google Drive integration page, click **Connect**. You will be redirected to Google to authorize the `drive.file` scope.

#### Start a sync

On the knowledge base page, click **Sync Documents** and select the destination folder for the imported files. Optionally enable **Auto sync** to periodically refresh the files (configurable between 1 and 180 days, defaulting to every day) and **Auto remove** to delete a document automatically when you lose access to its source file in Drive.

#### Pick files

Click **Pick files** and select the files you want to sync in the Google File Picker. Only the files you pick are shared with ElevenLabs, and they are imported into the destination folder.

## Supported file types

| Format                          | Supported | Notes                                                                             |
| ------------------------------- | --------- | --------------------------------------------------------------------------------- |
| Google Docs                     | Yes       | Text and formatting are preserved. Embedded images and comments are not included. |
| PDF                             | Yes       |                                                                                   |
| DOCX                            | Yes       |                                                                                   |
| Plain text                      | Yes       |                                                                                   |
| HTML                            | Yes       |                                                                                   |
| Markdown                        | Yes       |                                                                                   |
| EPUB                            | Yes       |                                                                                   |
| Google Sheets, Slides, Drawings | No        |                                                                                   |

Files larger than 20 MB are skipped.

## How it works

**Connection type.** The connection requests the `drive.file` scope, which limits ElevenLabs to the files you select in the Google File Picker.

**Initial sync.** Each picked file is imported individually.

**Incremental sync.** Subsequent syncs only process files that were added, modified, or deleted since the last sync. Deleted files are removed from the knowledge base when auto-remove is enabled.

**Manual sync.** You can trigger a sync at any time, independent of the auto-sync schedule. Use **Sync now** on a file to refresh just that file's content.

## Security and permissions

Access is granted per-user through the standard Google OAuth consent flow and can be revoked at any time from your [Google account permissions](https://myaccount.google.com/permissions). ElevenLabs cannot create, modify, or delete files in your Drive.

| Scope        | Grants                                                                        |
| ------------ | ----------------------------------------------------------------------------- |
| `drive.file` | Read-only access to only the files you select through the Google File Picker. |

## Useful links

* [Knowledge base documentation](https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base)
* [Google Drive API reference](https://developers.google.com/drive/api/reference/rest/v3)
* [Google Picker API](https://developers.google.com/drive/picker/guides/overview)
* [Google OAuth 2.0 scopes for Drive](https://developers.google.com/identity/protocols/oauth2/scopes#drive)
