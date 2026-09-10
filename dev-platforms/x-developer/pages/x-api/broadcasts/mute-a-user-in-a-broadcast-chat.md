---
title: "Mute or time out a user in a broadcast chat"
source: https://docs.x.com/x-api/broadcasts/mute-a-user-in-a-broadcast-chat
path: x-api/broadcasts/mute-a-user-in-a-broadcast-chat
---

post /2/broadcasts/{id}/chat/mutes
Prevents a user from posting further messages in a running broadcast chat. When `end_at_ms` is provided, the mute expires at that time. The authenticated user must own the broadcast.
