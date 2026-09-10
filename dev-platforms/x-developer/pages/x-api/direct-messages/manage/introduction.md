---
title: "Manage Direct Messages"
source: https://docs.x.com/x-api/direct-messages/manage/introduction
path: x-api/direct-messages/manage/introduction
---

Use the X API v2 Manage Direct Messages endpoints to create conversations, send new DMs, and delete DM events on behalf of authenticated users on X.

The Manage Direct Messages endpoints let you send and delete Direct Messages on behalf of authenticated users.

## Overview

<CardGroup>
  <Card title="Send message" icon="paper-plane">
    Send a DM to another user
  </Card>

  <Card title="Delete message" icon="trash">
    Delete a DM for yourself
  </Card>

  <Card title="Create conversation" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat-unread.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=ce6313d8c0b7b4e5363f2ce80b89f7e4">
    Start a new conversation
  </Card>

  <Card title="Group messages" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980">
    Send to group conversations
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                            | Description                     |
| :----- | :-------------------------------------------------- | :------------------------------ |
| POST   | `/2/dm_conversations`                               | Create a new conversation       |
| POST   | `/2/dm_conversations/with/:participant_id/messages` | Send to one-to-one conversation |
| POST   | `/2/dm_conversations/:dm_conversation_id/messages`  | Send to existing conversation   |
| DELETE | `/2/dm_events/:id`                                  | Delete a DM event               |

***

## Example: Send a message

```bash theme={null}
curl -X POST "https://api.x.com/2/dm_conversations/with/1234567890/messages" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello! How are you?"}'
```

## Example response

```json theme={null}
{
  "data": {
    "dm_conversation_id": "1234567890-0987654321",
    "dm_event_id": "1122334455667788990"
  }
}
```

***

## Message types

You can send text messages and attach media:

```json theme={null}
{
  "text": "Check out this photo!",
  "attachments": [{
    "media_id": "1234567890123456789"
  }]
}
```

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * User Access Tokens via [OAuth 2.0 PKCE](/resources/fundamentals/authentication#oauth-2-0-authorization-code-flow-with-pkce-2)
</Note>

<CardGroup>
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/direct-messages/manage/quickstart">
    Send your first DM
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/direct-messages/manage/integrate">
    Key concepts and best practices
  </Card>

  <Card title="DM lookup" icon="messages" href="/x-api/direct-messages/lookup/introduction">
    Retrieve DM events
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/direct-messages/create-dm-message-by-conversation-id">
    Full endpoint documentation
  </Card>
</CardGroup>
