---
title: "Direct Messages Lookup"
source: https://docs.x.com/x-api/direct-messages/lookup/introduction
path: x-api/direct-messages/lookup/introduction
---

The Direct Messages lookup endpoints let you retrieve DM events for the authenticated user. Reference for the X API v2 standard tier covering lookup.

The Direct Messages lookup endpoints let you retrieve DM events for the authenticated user, including messages from both one-to-one and group conversations.

## Overview

<CardGroup>
  <Card title="All DM events" icon="messages">
    Get all DM events for the user
  </Card>

  <Card title="One-to-one" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=9fde7d51b4f18c96d3a38a81d519761f">
    Get events from a specific conversation
  </Card>

  <Card title="By conversation ID" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat-unread.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=ce6313d8c0b7b4e5363f2ce80b89f7e4">
    Get events by conversation ID
  </Card>

  <Card title="Event types" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bell.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=5e0b3dcfbb39ba3d4619931d7cd927d1">
    Messages, joins, and leaves
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                                                                                            | Description                             |
| :----- | :------------------------------------------------------------------------------------------------------------------ | :-------------------------------------- |
| GET    | [`/2/dm_events`](/x-api/direct-messages/get-dm-events)                                                              | Get all DM events for the user          |
| GET    | [`/2/dm_conversations/with/:participant_id/dm_events`](/x-api/direct-messages/get-dm-events-for-a-dm-conversation)  | Get events from one-to-one conversation |
| GET    | [`/2/dm_conversations/:dm_conversation_id/dm_events`](/x-api/direct-messages/get-dm-events-for-a-dm-conversation-1) | Get events by conversation ID           |

***

## Event types

| Event               | Description                            |
| :------------------ | :------------------------------------- |
| `MessageCreate`     | A message was sent in the conversation |
| `ParticipantsJoin`  | A user joined the conversation         |
| `ParticipantsLeave` | A user left the conversation           |

***

## Data retention

<Note>
  Events from up to **30 days ago** are available through these endpoints.
</Note>

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * User Access Tokens via [3-legged OAuth](/resources/fundamentals/authentication#obtaining-access-tokens-using-3-legged-oauth-flow)
</Note>

<CardGroup>
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/direct-messages/lookup/quickstart">
    Make your first DM lookup request
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/direct-messages/lookup/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/direct-messages/get-dm-events">
    Full endpoint documentation
  </Card>

  <Card title="Sample code" icon="github" href="https://github.com/xdevplatform/Twitter-API-v2-sample-code">
    Working code examples
  </Card>
</CardGroup>
