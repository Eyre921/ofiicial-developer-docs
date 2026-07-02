---
title: "Upload and index a file"
source: https://docs.trychroma.com/reference/sync-api/file-upload/upload-and-index-a-file
path: reference/sync-api/file-upload/upload-and-index-a-file
---

/sync.openapi.json post /api/v1/add-file
Uploads a file and creates an invocation to index it into the specified collection.

The first time this endpoint is called for a database, a `file_upload` source is created automatically; subsequent calls reuse that source. The collection is created on the first invocation if it does not already exist.

**Multipart field ordering:** `database_name` and `collection_name` MUST appear before `file`. The server uses these to authorize the request before streaming file bytes to storage.

**Size limits:** maximum 200 MiB per file. The declared size in `x-upload-content-length` is enforced.
