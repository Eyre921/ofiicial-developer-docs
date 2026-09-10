---
title: "Pinned Lists"
source: https://docs.x.com/x-api/lists/pinned-lists/introduction
path: x-api/lists/pinned-lists/introduction
---

The Pinned Lists endpoints let you view, pin, and unpin Lists for the authenticated user. Reference for the X API v2 standard tier covering pinned lists.

The Pinned Lists endpoints let you view, pin, and unpin Lists for the authenticated user. Pinned Lists appear prominently in the user's X interface.

## Overview

<CardGroup>
  <Card title="View pinned" icon="thumbtack">
    Get user's pinned Lists
  </Card>

  <Card title="Pin List" icon="plus">
    Pin a List
  </Card>

  <Card title="Unpin List" icon="minus">
    Unpin a List
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                                        | Description      |
| :----- | :-------------------------------------------------------------- | :--------------- |
| GET    | [`/2/users/:id/pinned_lists`](/x-api/users/get-pinned-lists)    | Get pinned Lists |
| POST   | [`/2/users/:id/pinned_lists`](/x-api/users/pin-list)            | Pin a List       |
| DELETE | [`/2/users/:id/pinned_lists/:list_id`](/x-api/users/unpin-list) | Unpin a List     |

***

## Example: Get pinned Lists

```bash theme={null}
curl "https://api.x.com/2/users/123456789/pinned_lists?\
list.fields=name,description,member_count" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN"
```

## Example: Pin a List

```bash theme={null}
curl -X POST "https://api.x.com/2/users/123456789/pinned_lists" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"list_id": "9876543210"}'
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
  <Card title="Lookup quickstart" icon="thumbtack" href="/x-api/lists/pinned-lists/quickstart/pinned-list-lookup">
    Get pinned Lists
  </Card>

  <Card title="Manage quickstart" icon="plus" href="/x-api/lists/pinned-lists/quickstart/manage-pinned-lists">
    Pin and unpin Lists
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/pinned-lists/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/get-pinned-lists">
    Full endpoint documentation
  </Card>
</CardGroup>
