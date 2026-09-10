---
title: "Create a bot"
source: https://docs.x.com/x-api/bots/create-a-bot
path: x-api/bots/create-a-bot
---

post /2/bots
Creates a bot account in the calling app's project and returns its bearer token. Idempotent on handle: repeating the request for a handle that already names one of the project's bots returns that bot with a freshly minted token, revoking the previous one — safe to retry when a response was lost, since the replaced token was never seen.
