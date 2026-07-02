---
title: "Download Chat Media"
source: https://docs.x.com/enterprise-api/chat/download-chat-media
path: enterprise-api/chat/download-chat-media
---

get /2/chat/media/{id}/{media_hash_key}
Downloads encrypted media bytes from an XChat conversation. The response body contains raw binary bytes. For 1:1 conversations, provide the recipient's user ID; the server constructs the canonical conversation ID from the authenticated user and recipient.
