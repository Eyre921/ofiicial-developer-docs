---
title: "Initialize Chat Group"
source: https://docs.x.com/x-api/chat/initialize-chat-group
path: x-api/chat/initialize-chat-group
---

post /2/chat/conversations/group/initialize
Initializes a new XChat group conversation and returns a unique conversation ID.

This endpoint is the first step in creating a group chat. The returned conversation_id 
should be used in subsequent calls to POST /chat/conversations/group to fully create and 
configure the group with members, admins, encryption keys, and other settings.

**Workflow:**
1. Call this endpoint to get a `conversation_id`
2. Use that `conversation_id` when calling `POST /chat/conversations/group` to create the group

**Authentication:**
- Requires OAuth 1.0a User Context or OAuth 2.0 User Context
- Required scope: `dm.write`
