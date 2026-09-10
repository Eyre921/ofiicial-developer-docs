---
title: "Go live on a scheduled broadcast"
source: https://docs.x.com/x-api/broadcasts/go-live-on-a-scheduled-broadcast
path: x-api/broadcasts/go-live-on-a-scheduled-broadcast
---

post /2/broadcasts/scheduled/{id}/live
Publishes a schedule that was created or updated with `manual_publish: true`. Without that flag the coordinator auto-publishes at start and this call is rejected.
