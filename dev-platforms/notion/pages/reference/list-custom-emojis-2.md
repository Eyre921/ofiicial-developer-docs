---
title: "List custom emojis"
source: https://developers.notion.com/reference/list-custom-emojis
path: reference/list-custom-emojis
---

get /v1/custom_emojis
Retrieves a list of custom emojis in the workspace.

See [Pagination](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

Use the `name` query parameter to filter by exact name match, which is useful for resolving a custom emoji name to its ID.
