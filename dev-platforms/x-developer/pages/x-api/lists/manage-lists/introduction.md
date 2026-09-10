---
title: "Manage Lists"
source: https://docs.x.com/x-api/lists/manage-lists/introduction
path: x-api/lists/manage-lists/introduction
---

Use the X API v2 Manage Lists endpoints to create, update, and delete X Lists on behalf of authenticated users and organize accounts into curated timelines.

The Manage Lists endpoints let you create, update, and delete Lists on behalf of authenticated users.

## Overview

<CardGroup>
  <Card title="Create" icon="plus">
    Create a new List
  </Card>

  <Card title="Update" icon="pen">
    Update List name and description
  </Card>

  <Card title="Delete" icon="trash">
    Delete a List
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                   | Description       |
| :----- | :----------------------------------------- | :---------------- |
| POST   | [`/2/lists`](/x-api/lists/create-list)     | Create a new List |
| PUT    | [`/2/lists/:id`](/x-api/lists/update-list) | Update a List     |
| DELETE | [`/2/lists/:id`](/x-api/lists/delete-list) | Delete a List     |

***

## Example: Create a List

```bash theme={null}
curl -X POST "https://api.x.com/2/lists" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tech News",
    "description": "My favorite tech journalists",
    "private": false
  }'
```

## Example response

```json theme={null}
{
  "data": {
    "id": "1234567890",
    "name": "Tech News"
  }
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
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/lists/manage-lists/quickstart">
    Create your first List
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/manage-lists/integrate">
    Key concepts and best practices
  </Card>

  <Card title="List members" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980" href="/x-api/lists/list-members/introduction">
    Add and remove members
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/lists/create-list">
    Full endpoint documentation
  </Card>
</CardGroup>
