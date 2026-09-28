---
title: "List commits"
source: https://docs.langchain.com/langsmith/smith-api/commits/list-commits
path: langsmith/smith-api/commits/list-commits
---

/langsmith/langsmith-platform-openapi.json get /api/v1/commits/{owner}/{repo}
List commits for a repository, with pagination support.
This endpoint supports both authenticated and unauthenticated access.
Authenticated users can access private repositories; unauthenticated users can only access public repositories.
The include_stats parameter controls whether download and view statistics are computed (defaults to true).
