---
title: "Get a Message"
source: https://upstash.com/docs/qstash/api-reference/messages/get-a-message
path: docs/qstash/api-reference/messages/get-a-message
---

> Retrieve details of a specific message

`GET /v2/messages/{messageId}`

<Warning>Messages are removed from the database shortly after they’re delivered, so you will not be able to retrieve a message after. This endpoint is intended to be used for accessing messages that are in the process of being delivered/retried.</Warning>
