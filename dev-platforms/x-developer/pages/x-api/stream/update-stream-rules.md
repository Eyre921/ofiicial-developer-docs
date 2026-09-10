---
title: "Update stream rules"
source: https://docs.x.com/x-api/stream/update-stream-rules
path: x-api/stream/update-stream-rules
---

post /2/tweets/search/stream/rules
Adds or deletes rules from the active rule set for the filtered stream. Exactly one of `add`, `delete`, or `?delete_all=true` must be specified. Use `?dry_run=true` to validate without committing.
