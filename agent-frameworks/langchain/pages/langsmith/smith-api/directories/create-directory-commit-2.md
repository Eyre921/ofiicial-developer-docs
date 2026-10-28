---
title: "Create directory commit"
source: https://docs.langchain.com/langsmith/smith-api/directories/create-directory-commit
path: langsmith/smith-api/directories/create-directory-commit
---

/langsmith/langsmith-platform-openapi.json post /api/v1/platform/hub/repos/{owner}/{repo}/directories/commits
Creates a new directory commit for an agent or skill repository by applying file/link create, update, and delete operations. Linked directories default to the LATEST selector; use COMMIT to pin one commit. The legacy commit_id write field is deprecated and resolves as LATEST.
