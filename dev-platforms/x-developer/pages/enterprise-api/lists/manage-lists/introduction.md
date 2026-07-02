---
title: "Manage Lists"
source: https://docs.x.com/enterprise-api/lists/manage-lists/introduction
path: enterprise-api/lists/manage-lists/introduction
---

Use the Enterprise Manage Lists endpoints to create, update, and delete X Lists on behalf of authenticated users and organize accounts into curated timelines.

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
  <Card title="Quickstart" icon="rocket" href="/x-api/lists/manage-lists/quickstart">
    Create your first List
  </Card>

  <Card title="Integration guide" icon="book" href="/x-api/lists/manage-lists/integrate">
    Key concepts and best practices
  </Card>

  <Card title="List members" icon="users" href="/x-api/lists/list-members/introduction">
    Add and remove members
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/lists/create-list">
    Full endpoint documentation
  </Card>
</CardGroup>
