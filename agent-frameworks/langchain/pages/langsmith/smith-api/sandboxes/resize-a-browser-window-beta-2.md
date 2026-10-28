---
title: "Resize a browser window (Beta)"
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/resize-a-browser-window-beta
path: langsmith/smith-api/sandboxes/resize-a-browser-window-beta
---

/langsmith/langsmith-platform-openapi.json patch /api/v2/sandboxes/browsers/{name}/attachments/{attachment_id}
Beta: size a window so its page is width by height CSS pixels. The window keeps that size until resized again, through this call or over CDP with Browser.setWindowBounds; the live view scales to fit it rather than resizing it. A browser that is not running cannot be resized.
