---
title: "Send Chat Message"
source: https://docs.x.com/enterprise-api/chat/send-chat-message
path: enterprise-api/chat/send-chat-message
---

post /2/chat/conversations/{id}/messages
Sends an encrypted message to a specific Chat conversation. For 1:1 conversations, provide the recipient's user ID; the server constructs the canonical conversation ID from the authenticated user and recipient.
