---
title: "Get Chat Conversation Events"
source: https://docs.x.com/x-api/chat/get-chat-conversation-events
path: x-api/chat/get-chat-conversation-events
---

get /2/chat/conversations/{id}/events
Retrieves messages and key change events for a specific Chat conversation with pagination support. For 1:1 conversations, provide the recipient's user ID; the server constructs the canonical conversation ID from the authenticated user and recipient.
