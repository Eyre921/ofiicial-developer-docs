---
title: "Download DM Media"
source: https://docs.x.com/x-api/direct-messages/download-dm-media
path: x-api/direct-messages/download-dm-media
---

get /2/dm_conversations/media/{dm_id}/{media_id}/{resource_id}
Downloads media attached to a legacy Direct Message. The requesting user must be a participant in the conversation containing the specified DM event. The response body contains raw binary bytes.
