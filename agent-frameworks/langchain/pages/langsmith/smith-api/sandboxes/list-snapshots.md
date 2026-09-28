---
title: "List snapshots"
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-snapshots
path: langsmith/smith-api/sandboxes/list-snapshots
---

/langsmith/langsmith-platform-openapi.json get /api/v2/sandboxes/snapshots
List workspace and published system snapshots, with optional filtering, sorting, and pagination.
Page with page_size and cursor: replay the response's next_cursor until it comes back null, which is the only signal that no pages remain.
Cursors are opaque and only valid on this endpoint; do not parse or construct one.
