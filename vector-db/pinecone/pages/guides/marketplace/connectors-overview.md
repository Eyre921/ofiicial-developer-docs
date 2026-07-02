---
title: "Connectors overview"
source: https://docs.pinecone.io/guides/marketplace/connectors-overview
path: guides/marketplace/connectors-overview
---

How Pinecone Marketplace connectors ingest documents, keep them in sync with source systems, and let operators add manually uploaded files.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

A connector is the integration that ingests documents from a source system into a knowledge base. Marketplace handles the ingestion pipeline, normalizes content, and keeps the knowledge base in sync as the source changes. You can also upload files directly when a source connector is not the right fit.

## Available connectors

| Connector     | Type               |
| ------------- | ------------------ |
| Google Drive  | OAuth              |
| Manual upload | Direct file upload |

If you need a connector that is not listed, contact your Pinecone account team or [Pinecone support](https://app.pinecone.io/organizations/-/settings/support).

## How a connector works

When you connect a source to a knowledge base:

1. You authenticate to the source through OAuth or upload files directly.
2. You select the folders, files, or scope the connector should ingest.
3. Marketplace mirrors the selected content, processes each file, and indexes it through Pinecone Assistant.
4. Periodic sync runs detect changes and update the knowledge base.

OAuth secrets are encrypted at rest. Sync runs report status to the deployment dashboard.

## Connector capabilities

Connectors are described by a common adapter contract that covers:

* **Authentication**: how the connector signs in to the source.
* **Selection**: how the operator picks the scope to ingest, such as a folder picker.
* **Sync**: how often the connector polls and how it detects changes.
* **Normalization**: how content is converted to the format Pinecone indexes.
* **Health**: how the connector reports failures or stalled syncs.

## Connect Google Drive

Google Drive is the primary connector for ingesting documents into a deployment.

### Before you begin

* A deployment with at least one knowledge base. See [Create a deployment](/guides/marketplace/create-a-deployment).
* A Google account with access to the folder you want to use.
* Permission from the document owner to ingest the folder if it is shared with you.

### Steps

1. **Open the knowledge base.** In the deployment dashboard, open the knowledge base you want to connect Google Drive to. Select **Add source** and choose **Google Drive**.
2. **Authorize Google Drive.** Sign in with the Google account that has access to the folder. Marketplace requests read-only access to the files you select.
3. **Select files and folders.** Use the Google Picker to select a single folder (recursive ingest of supported file types), a subset of files within a folder, or multiple folders. Selections are scoped to the knowledge base; other knowledge bases in the same deployment have their own selections.
4. **Confirm the sync.** Marketplace runs an initial sync, mirrors the selected files, processes each one, and indexes the content. The dashboard shows progress per file.
5. **Periodic sync runs automatically.** Once the initial sync finishes, Marketplace polls Google Drive on a schedule and re-ingests files that have changed. New files added to a selected folder are picked up on the next sync run.

### Permissions and visibility

Marketplace ingests only the files you select. Documents are scoped to the knowledge base. End users of the knowledge application see content from the knowledge base when they ask questions; they do not get direct access to the underlying Google Drive files.

### Troubleshooting

| Symptom               | What to check                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| Sync fails to start   | The Google account still has access to the selected folders.                                              |
| Files are missing     | The file type is supported by Pinecone Assistant. See [Files overview](/guides/assistant/files-overview). |
| Stale answers         | Check sync status on the dashboard; you can trigger a manual sync.                                        |
| Authentication errors | The Google OAuth grant has not been revoked. Reconnect the source if needed.                              |

## Manual uploads

You can upload files directly to a knowledge base instead of connecting them through a source connector. Manual uploads are useful for one-off documents, small document sets, or content that is not in a supported source system.

### Before you begin

* A deployment with at least one knowledge base. See [Create a deployment](/guides/marketplace/create-a-deployment).
* Files in a format supported by Pinecone Assistant. See [Files overview](/guides/assistant/files-overview).

### Upload files

1. Open the knowledge base in the deployment dashboard.
2. Select **Add source** and choose **Manual upload**.
3. Drag and drop files into the upload area, or browse to select them.
4. Marketplace validates each file, stages it, and queues it for ingestion.

### Updating uploaded files

To update a manually uploaded file, upload the new version with the same name. Marketplace replaces the previous file. To remove a file, delete it from the knowledge base.

<Note>
  Manually uploaded files do not sync from a source. If you want changes in a source to flow through automatically, use a connector instead.
</Note>

## Mixing connectors and uploads

A knowledge base can combine connector-synced content with manually uploaded files. Use connectors for content you want to stay in sync, and manual uploads for one-off documents.

## Sync and freshness

For each connected source, Marketplace stores the operator's selection, polls the source on a schedule, detects new, updated, and deleted files, and re-ingests the knowledge base incrementally. Manually uploaded files do not sync; replace them by uploading a new version.

### Sync status

The deployment dashboard shows sync status per source and per file:

* **Synced**: the file is up to date with the source.
* **Syncing**: the file is being processed.
* **Failed**: ingestion failed. The error is shown next to the file.
* **Removed**: the file was deleted from the source and removed from the knowledge base.

### Trigger a manual sync

To force an immediate sync, open the source in the deployment dashboard and select **Sync now**. Manual syncs do not change the periodic schedule.

### Freshness across versions

When you publish a new version of a deployment, Marketplace re-runs introspection and starter generation against the latest content. End users always interact with the active version. If a sync change introduces unexpected behavior, you can roll back to a previous version. See [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).

### Limits

Sync frequency and connector behavior are governed by the underlying connector adapter.
