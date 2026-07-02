---
title: "List Responses"
source: https://docs.fireworks.ai/api-reference/list-responses
path: api-reference/list-responses
---

get /v1/responses
Get a list of all responses for the authenticated account.

Args:
    limit: Maximum number of responses to return (default: 20, max: 100)
    after: Cursor for pagination - return responses after this ID
    before: Cursor for pagination - return responses before this ID
