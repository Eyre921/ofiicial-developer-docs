---
title: "Add Conversation Keys"
source: https://docs.x.com/x-api/chat/add-conversation-keys
path: x-api/chat/add-conversation-keys
---

post /2/chat/conversations/{id}/keys
Adds (initializes or rotates) the encryption keys for a Chat conversation. Call this before sending messages in a new 1:1 conversation, and again with a newer key version to rotate the conversation key. For 1:1 conversations, provide the recipient's user ID as the conversation id; the server constructs the canonical conversation ID from the authenticated user and recipient. The request body must contain the conversation key version and participant keys (the conversation key encrypted for each participant using their public key).
