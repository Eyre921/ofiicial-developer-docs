---
title: "Delete Chat messages"
source: https://docs.x.com/x-api/chat/delete-chat-messages
path: x-api/chat/delete-chat-messages
---

post /2/chat/conversations/{id}/messages/delete
Deletes one or more messages from a Chat conversation. For 1:1 conversations, provide the recipient's user ID; the server constructs the canonical conversation ID from the authenticated user and recipient. Delete for all removes a message you sent (or, in groups you administer, any message) for every participant; delete for self removes any message only from your own view.
