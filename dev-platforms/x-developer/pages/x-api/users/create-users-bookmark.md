---
title: "Create Bookmark"
source: https://docs.x.com/x-api/users/create-users-bookmark
path: x-api/users/create-users-bookmark
---

post /2/users/{id}/bookmarks
Adds one or more Posts to the authenticated user's Bookmarks. Supply `tweet_id` for a single Post, or `tweet_ids` (at most 25) to bookmark several in one request. Optional `folder_id` applies to every Post in the request. Billing and rate limits still apply per HTTP request.
