---
title: "Create a browser (Beta)"
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-browser-beta
path: langsmith/smith-api/sandboxes/create-a-browser-beta
---

/langsmith/langsmith-platform-openapi.json post /api/v2/sandboxes/browsers
Beta: create a browser sandbox, which runs one persistent Chrome that other sandboxes attach to. Logins made in it persist across restarts. It keeps its memory when it stops. A stopped browser is deleted after the sandbox default, along with its logins, unless delete_after_stop_seconds sets another delay or 0 to keep it.
