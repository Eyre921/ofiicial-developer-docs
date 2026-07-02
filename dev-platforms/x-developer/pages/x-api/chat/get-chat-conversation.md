---
title: "Get Chat Conversation"
source: https://docs.x.com/x-api/chat/get-chat-conversation
path: x-api/chat/get-chat-conversation
---

get /2/chat/conversations/{id}
Returns metadata for a Chat conversation including type, muted status, and group details. Use chat_conversation.fields to select which fields are returned. Use expansions to hydrate member, admin, or participant user objects. Use user.fields to control which profile fields are returned for expanded users.
