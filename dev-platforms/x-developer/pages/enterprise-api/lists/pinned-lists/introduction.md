---
title: "Pinned Lists"
source: https://docs.x.com/enterprise-api/lists/pinned-lists/introduction
path: enterprise-api/lists/pinned-lists/introduction
---

The Pinned Lists endpoints let you view, pin, and unpin Lists for the authenticated user. Reference for the Enterprise X API tier covering pinned lists.

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

  <Card title="Integration guide" icon="book" href="/x-api/lists/pinned-lists/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/users/get-pinned-lists">
    Full endpoint documentation
  </Card>
</CardGroup>
