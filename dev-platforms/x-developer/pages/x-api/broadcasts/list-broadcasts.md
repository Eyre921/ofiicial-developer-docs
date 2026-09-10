---
title: "List broadcasts"
source: https://docs.x.com/x-api/broadcasts/list-broadcasts
path: x-api/broadcasts/list-broadcasts
---

get /2/broadcasts
Returns the authenticated user's live-video broadcasts, or selected owned broadcasts when ids are provided.

At most one of `ids`, `max_results` may be provided. At most one of `ids`, `pagination_token` may be provided.
