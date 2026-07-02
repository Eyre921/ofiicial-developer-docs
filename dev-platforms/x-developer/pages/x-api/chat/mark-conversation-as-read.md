---
title: "Mark Conversation as Read"
source: https://docs.x.com/x-api/chat/mark-conversation-as-read
path: x-api/chat/mark-conversation-as-read
---

post /2/chat/conversations/{id}/read
Marks a specific Chat conversation as read on behalf of the authenticated user. For 1:1 conversations, provide the recipient's user ID; the server constructs the canonical conversation ID from the authenticated user and recipient.
