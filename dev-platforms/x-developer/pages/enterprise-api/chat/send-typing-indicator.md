---
title: "Send Typing Indicator"
source: https://docs.x.com/enterprise-api/chat/send-typing-indicator
path: enterprise-api/chat/send-typing-indicator
---

post /2/chat/conversations/{id}/typing
Sends a typing indicator to a specific Chat conversation on behalf of the authenticated user. For 1:1 conversations, provide the recipient's user ID; the server constructs the canonical conversation ID from the authenticated user and recipient.
