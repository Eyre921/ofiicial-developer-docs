---
title: "Blocks"
source: https://docs.x.com/x-api/users/blocks/introduction
path: x-api/users/blocks/introduction
---

The Blocks endpoints let you retrieve the list of users blocked by the authenticated user, as well. Reference for the X API v2 standard tier covering blocks.

The Blocks endpoints let you retrieve the list of users blocked by the authenticated user, as well as block and unblock users.

<Callout icon="/icons/xds/icon-key.svg">
  The block and unblock users endpoints are only available under the Enterprise plan. You can fill out the Enterprise interest form [here](/forms/enterprise-api-interest).
</Callout>

## Overview

<CardGroup>
  <Card title="Blocked users" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
    Get your blocked user list
  </Card>

  <Card title="Block" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-block.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=702a65b4001948aebcc42635b8e2eac7">
    Block a user
  </Card>

  <Card title="Unblock" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-checkmark-circle.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=bd3e78cd745fde73a934535acacaff59">
    Unblock a user
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                             | Description       | Availability                                                   |
| :----- | :--------------------------------------------------- | :---------------- | :------------------------------------------------------------- |
| GET    | [`/2/users/:id/blocking`](/x-api/users/get-blocking) | Get blocked users | <div><Badge>Pay-per-use</Badge><Badge>Enterprise</Badge></div> |
| POST   | `/2/users/:id/blocking`                              | Block a user      | <Badge>Enterprise</Badge>                                      |
| DELETE | `/2/users/:source_user_id/blocking/:target_user_id`  | Unblock a user    | <Badge>Enterprise</Badge>                                      |

***

## Example: Get blocked users

```bash theme={null}
curl "https://api.x.com/2/users/123456789/blocking?\
user.fields=username,description" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN"
```

## Example: Block a user (Enterprise only)

```bash theme={null}
curl -X POST "https://api.x.com/2/users/123456789/blocking" \
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
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/users/blocks/quickstart">
    Get started with blocks
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/users/blocks/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/get-blocking">
    Full endpoint documentation
  </Card>
</CardGroup>
