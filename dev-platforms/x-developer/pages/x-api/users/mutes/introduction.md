---
title: "Mutes"
source: https://docs.x.com/x-api/users/mutes/introduction
path: x-api/users/mutes/introduction
---

Use the X API v2 Mutes endpoints to mute and unmute accounts on behalf of the authenticated user and retrieve the full list of users they have muted on X.

The Mutes endpoints let you mute and unmute users, and retrieve the list of users muted by the authenticated user.

## Overview

<CardGroup>
  <Card title="Mute" icon="volume-xmark">
    Mute a user
  </Card>

  <Card title="Unmute" icon="volume-high">
    Unmute a user
  </Card>

  <Card title="Muted users" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
    Get your muted user list
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                                                      | Description     |
| :----- | :---------------------------------------------------------------------------- | :-------------- |
| GET    | [`/2/users/:id/muting`](/x-api/users/get-muting)                              | Get muted users |
| POST   | [`/2/users/:id/muting`](/x-api/users/mute-user)                               | Mute a user     |
| DELETE | [`/2/users/:source_user_id/muting/:target_user_id`](/x-api/users/unmute-user) | Unmute a user   |

***

## Example: Get muted users

```bash theme={null}
curl "https://api.x.com/2/users/123456789/muting?\
user.fields=username,description" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN"
```

## Example: Mute a user

```bash theme={null}
curl -X POST "https://api.x.com/2/users/123456789/muting" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"target_user_id": "9876543210"}'
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
  <Card title="Mutes lookup quickstart" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5" href="/x-api/users/mutes/quickstart/mutes-lookup">
    Get your muted users
  </Card>

  <Card title="Manage mutes quickstart" icon="volume-xmark" href="/x-api/users/mutes/quickstart/manage-mutes-quickstart">
    Mute and unmute users
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/users/mutes/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/get-muting">
    Full endpoint documentation
  </Card>
</CardGroup>
