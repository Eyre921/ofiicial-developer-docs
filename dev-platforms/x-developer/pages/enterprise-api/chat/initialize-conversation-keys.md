---
title: "Initialize Conversation Keys"
source: https://docs.x.com/enterprise-api/chat/initialize-conversation-keys
path: enterprise-api/chat/initialize-conversation-keys
---

post /2/chat/conversations/{id}/keys
Initializes encryption keys for a Chat conversation. This is the first step
before sending messages in a new 1:1 conversation.

For 1:1 conversations, provide the recipient's user ID as the conversation_id.
The server constructs the canonical conversation ID from the authenticated user
and recipient.

The request body must contain the conversation key version and participant keys
(the conversation key encrypted for each participant using their public key).

**Workflow (1:1 conversation):**
1. Generate a conversation key using the SDK
2. Encrypt the key for both participants using their public keys
3. Call this endpoint to register the keys
4. Send messages using `POST /chat/conversations/{id}/messages`

**Authentication:**
- Requires OAuth 1.0a User Context or OAuth 2.0 User Context
- Required scopes: `tweet.read`, `users.read`, `dm.write`
