---
title: "Update a scheduled broadcast"
source: https://docs.x.com/x-api/broadcasts/update-a-scheduled-broadcast
path: x-api/broadcasts/update-a-scheduled-broadcast
---

put /2/broadcasts/scheduled/{id}
Fully replaces schedule fields for a broadcast. Path `:id` is the UBS broadcast id; the body must include `scheduled_broadcast_id` and re-send any fields that should be kept.
